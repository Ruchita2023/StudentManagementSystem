from services.student_service import *
import unittest
from unittest.mock import patch, MagicMock
from openapi_server.services.pagination_sorting import pagination_sorting
from openapi_server.models.student import Student, Student_schema, Students_schema
from openapi_server.services.student_service import StudentService


class TestStudentService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.student_service = StudentService()

    def test_get_student_list(self):
        with patch('openapi_server.services.student_service.abort') as mock_abort:
            students = [Student(id=1, name='John Doe', email='john.doe@example.com'),
                        Student(id=2, name='Jane Doe', email='jane.doe@example.com')]
            pagination_sorting = MagicMock(return_value=students)
            with patch('openapi_server.services.pagination_sorting.pagination_sorting', pagination_sorting):
                result = self.student_service.get_student_list()
                self.assertEqual(result, Students_schema.dump(students))
                pagination_sorting.assert_called_once_with(Student)

            pagination_sorting = MagicMock(return_value=None)
            with patch('openapi_server.services.pagination_sorting.pagination_sorting', pagination_sorting):
                self.student_service.get_student_list()
                mock_abort.assert_called_once_with(404, "No student found")

    def test_get_student(self):
        with patch('openapi_server.services.student_service.abort') as mock_abort:
            student = Student(id=1, name='John Doe', email='john.doe@example.com')
            Student.query.filter = MagicMock(return_value=Student.query)
            Student.query.one_or_none = MagicMock(return_value=student)
            result = self.student_service.get_student(1)
            self.assertEqual(result, Student_schema.dump(student))
            Student.query.filter.assert_called_once_with(Student.id == 1)
            Student.query.one_or_none.assert_called_once()

            Student.query.one_or_none = MagicMock(return_value=None)
            self.student_service.get_student(0)
            mock_abort.assert_called_once_with(404, "Invalid ID: 0.")

            Student.query.one_or_none = MagicMock(return_value=None)
            self.student_service.get_student(1)
            mock_abort.assert_called_once_with(404, "Student with ID: 1 does not exist")

    def test_add_student(self):
        with patch('openapi_server.services.student_service.abort') as mock_abort:
            student = {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}
            Student.query.filter = MagicMock(return_value=None)
            Student_schema.load = MagicMock(return_value=student)
            db_session = MagicMock()
            with patch('openapi_server.services.student_service.db.session', db_session):
                result = self.student_service.add_student(student)
                self.assertEqual(result, Student_schema.dump(student))
                Student.query.filter.assert_called_once_with(Student.id == 1)
                Student_schema.load.assert_called_once_with(student, session=db_session)
                db_session.add.assert_called_once_with(student)
                db_session.commit.assert_called_once()

            Student.query.filter = MagicMock(return_value=Student(id=1))
            self.student_service.add_student(student)
            mock_abort.assert_called_once_with(400, "Student with ID: 1 already exists")

    def test_update_student(self):
        with patch('openapi_server.services.student_service.abort') as mock_abort:
            student = {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}
            Student.query.filter = MagicMock(return_value=Student(id=1))
            Student_schema.load = MagicMock(return_value=Student(id=1, name="Jane Doe", email="jane.doe@example.com"))
            db_session = MagicMock()
            with patch('openapi_server.services.student_service.db.session', db_session):
                result = self.student_service.update_student(student)
                self.assertEqual(result, Student_schema.dump(Student(id=1, name="Jane Doe", email="jane.doe@example.com")))
                Student.query.filter.assert_called_once_with(Student.id == 1)
                Student_schema.load.assert_called_once_with(student, session=db_session)
                db_session.merge.assert_called_once_with(Student(id=1, name="Jane Doe", email="jane.doe@example.com"))
                db_session.commit.assert_called_once()

            Student.query.filter = MagicMock(return_value=None)
            self.student_service.update_student(student)
            mock_abort.assert_called_once_with(404, "Student with ID: 1 not found")

    def test_delete_student(self):
        with patch('openapi_server.services.student_service.abort') as mock_abort:
            Student.query.filter = MagicMock(return_value=Student(id=1))
            db_session = MagicMock()
            with patch('openapi_server.services.student_service.db.session', db_session):
                result = self.student_service.delete_student(1)
                self.assertEqual(result, "Student with ID: 1 successfully deleted")
                Student.query.filter.assert_called_once_with(Student.id == 1)
                db_session.delete.assert_called_once_with(Student(id=1))
                db_session.commit.assert_called_once()

            Student.query.filter = MagicMock(return_value=None)
            self.student_service.delete_student(1)
            mock_abort.assert_called_once_with(400, "Student with ID: 1 not found")
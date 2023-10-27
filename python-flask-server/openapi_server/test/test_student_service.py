from services.student_service import *
import unittest
from unittest.mock import patch
from openapi_server.services.pagination_sorting import pagination_sorting
from openapi_server.models.student import Student, Student_schema, Students_schema
from openapi_server.config_test import db
from openapi_server.services.student_service import StudentService
from flask import abort

class TestStudentService(unittest.TestCase):
    def setUp(self):
        self.app = db.create_all()

    def test_get_student_list(self):
        with patch('openapi_server.services.student_service.logging') as mock_logging:
            result = StudentService.get_student_list()
            self.assertEqual(result.status_code, 200)
            mock_logging.info.assert_called_once()

    def test_get_student(self):
        with patch('openapi_server.services.student_service.logging') as mock_logging:
            with patch('openapi_server.services.student_service.abort') as mock_abort:
                result = StudentService.get_student(1)
                self.assertIsNotNone(result)
                mock_logging.info.assert_called_once()
                mock_abort.assert_not_called()

    def test_add_student(self):
        with patch('openapi_server.services.student_service.logging') as mock_logging:
            with patch('openapi_server.services.student_service.abort') as mock_abort:
                student = {'id': 1, 'name': 'John'}
                result = StudentService.add_student(student)
                self.assertIsNotNone(result)
                mock_logging.info.assert_called_once()

    def test_add_existing_student(self):
        with patch('openapi_server.services.student_service.logging') as mock_logging:
            with patch('openapi_server.services.student_service.abort') as mock_abort:
                student = {'id': 1, 'name': 'John'}
                result = StudentService.add_student(student)
                self.assertIsNotNone(result)
                result = StudentService.add_student(student)
                mock_logging.error.assert_called_once()

    def test_update_student(self):
        with patch('openapi_server.services.student_service.logging') as mock_logging:
            with patch('openapi_server.services.student_service.abort') as mock_abort:
                student = {'id': 1, 'name': 'John'}
                StudentService.add_student(student)
                student = {'id': 1, 'name': 'Jane'}
                result = StudentService.update_student(student)
                self.assertIsNotNone(result)
                mock_logging.info.assert_called_once()

    def test_delete_student(self):
        with patch('openapi_server.services.student_service.logging') as mock_logging:
            with patch('openapi_server.services.student_service.abort') as mock_abort:
                StudentService.add_student({'id': 1, 'name': 'John'})
                result = StudentService.delete_student(1)
                self.assertIsNotNone(result)
                mock_logging.info.assert_called_once()

if __name__ == '__main__':
    unittest.main()
from services.course_service import *
import unittest
from openapi_server.config_test import db
from openapi_server.services.pagination_sorting import pagination_sorting
from openapi_server.models.course import Course, Course_schema, Courses_schema
from unittest.mock import patch, MagicMock

class TestCourseService(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_course_list(self):
        with patch('openapi_server.services.course.pagination_sorting') as mock_pagination_sorting:
            mock_pagination_sorting.return_value = [Course(id=1, name="Test Course 1", description="Description 1", duration=30),
                                                     Course(id=2, name="Test Course 2", description="Description 2", duration=60)]
            result = CourseService.get_course_list()
            expected_result = Courses_schema.dump([Course(id=1, name="Test Course 1", description="Description 1", duration=30),
                                                   Course(id=2, name="Test Course 2", description="Description 2", duration=60)])
            self.assertEqual(result, expected_result)

    def test_get_course(self):
        course_id = 1
        course = Course(id=course_id, name="Test Course", description="Description", duration=30)
        db.session.add(course)
        db.session.commit()

        result = CourseService.get_course(course_id)
        expected_result = Course_schema.dump(course)
        self.assertEqual(result, expected_result)

        with self.assertRaises(TypeError):
            CourseService.get_course("invalid_id")

        with self.assertRaises(TypeError):
            CourseService.get_course(None)

        with self.assertRaises(ValueError):
            CourseService.get_course(0)

        with self.assertRaises(TypeError):
            CourseService.get_course(1.1)

        with self.assertRaises(TypeError):
            CourseService.get_course(True)

        with self.assertRaises(TypeError):
            CourseService.get_course([])

    def test_add_course(self):
        course = {"id": 1, "name": "Test Course", "description": "Description", "duration": 30}

        result = CourseService.add_course(course)
        expected_result = Course_schema.dump(Course(id=1, name="Test Course", description="Description", duration=30))
        self.assertEqual(result, expected_result)

        with self.assertRaises(TypeError):
            CourseService.add_course("invalid_course")

        with self.assertRaises(TypeError):
            CourseService.add_course(None)

        with self.assertRaises(ValueError):
            CourseService.add_course({"id": None, "name": "Test Course", "description": "Description", "duration": 30})

        with self.assertRaises(ValueError):
            CourseService.add_course({"id": -1, "name": "Test Course", "description": "Description", "duration": 30})

        with self.assertRaises(TypeError):
            CourseService.add_course({"id": 1, "name": "Test Course", "description": "Description", "duration": "invalid_duration"})

        with self.assertRaises(ValueError):
            CourseService.add_course({"id": 1, "name": "Test Course", "description": "Description", "duration": 0})

        with self.assertRaises(TypeError):
            CourseService.add_course({"id": 1, "name": "Test Course", "description": "Description", "duration": 30, "extra_field": "extra_value"})

        course = {"id": 1, "name": "Test Course", "description": "Description", "duration": 30}
        existing_course = Course_schema.load(course, session=db.session)
        db.session.add(existing_course)
        db.session.commit()

        with self.assertRaises(Exception):
            CourseService.add_course(course)

    def test_update_course(self):
        course_id = 1
        course = Course(id=course_id, name="Test Course", description="Description", duration=30)
        db.session.add(course)
        db.session.commit()

        result = CourseService.update_course({"id": course_id, "name": "Updated Course", "description": "Updated Description", "duration": 60})
        expected_result = Course_schema.dump(Course(id=course_id, name="Updated Course", description="Updated Description", duration=60))
        self.assertEqual(result, expected_result)

        with self.assertRaises(TypeError):
            CourseService.update_course("invalid_course")

        with self.assertRaises(TypeError):
            CourseService.update_course(None)

        with self.assertRaises(ValueError):
            CourseService.update_course({"id": None, "name": "Test Course", "description": "Description", "duration": 30})

        with self.assertRaises(ValueError):
            CourseService.update_course({"id": -1, "name": "Test Course", "description": "Description", "duration": 30})

        with self.assertRaises(TypeError):
            CourseService.update_course({"id": 1, "name": "Test Course", "description": "Description", "duration": "invalid_duration"})

        with self.assertRaises(ValueError):
            CourseService.update_course({"id": 1, "name": "Test Course", "description": "Description", "duration": 0})

        with self.assertRaises(TypeError):
            CourseService.update_course({"id": 1, "name": "Test Course", "description": "Description", "duration": 30, "extra_field": "extra_value"})

        with self.assertRaises(Exception):
            CourseService.update_course({"id": 2, "name": "Test Course", "description": "Description", "duration": 30})

    def test_delete_course(self):
        course_id = 1
        course = Course(id=course_id, name="Test Course", description="Description", duration=30)
        db.session.add(course)
        db.session.commit()

        result = CourseService.delete_course(course_id)
        expected_result = f"Course with ID: {course_id} successfully deleted"
        self.assertEqual(result, expected_result)

        with self.assertRaises(TypeError):
            CourseService.delete_course("invalid_id")

        with self.assertRaises(TypeError):
            CourseService.delete_course(None)

        with self.assertRaises(ValueError):
            CourseService.delete_course(0)

        with self.assertRaises(TypeError):
            CourseService.delete_course(1.1)

        with self.assertRaises(TypeError):
            CourseService.delete_course(True)

        with self.assertRaises(TypeError):
            CourseService.delete_course([])

        with self.assertRaises(Exception):
            CourseService.delete_course(2)

if __name__ == '__main__':
    unittest.main()
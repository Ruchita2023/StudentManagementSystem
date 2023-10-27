from services.course_service import *
import unittest
from unittest.mock import patch
from openapi_server.models.course import Course_schema, Courses_schema
from openapi_server.services.pagination_sorting import pagination_sorting
from openapi_server.services.course_service import CourseService


class TestCourseService(unittest.TestCase):

    def setUp(self):
        self.course = {"id": 1, "name": "Python Programming", "duration": 30, "instructor": "John Doe"}

    def test_get_course_list(self):
        with patch('openapi_server.services.course_service.pagination_sorting') as mocked_pagination_sorting:
            mocked_pagination_sorting.return_value = [self.course]
            result = CourseService.get_course_list()
            self.assertEqual(result, Courses_schema.dump([self.course]))
    
    def test_get_course(self):
        with patch('openapi_server.services.course_service.Course.query.filter.one_or_none') as mocked_course_query:
            mocked_course_query.return_value = Course_schema.load(self.course)
            result = CourseService.get_course(1)
            self.assertEqual(result, Course_schema.dump(self.course))
            
            mocked_course_query.return_value = None
            with self.assertRaises(Exception):
                CourseService.get_course(-1)

    def test_add_course(self):
        with patch('openapi_server.services.course_service.Course.query.filter.one_or_none') as mocked_course_query:
            mocked_course_query.return_value = None
            with patch('openapi_server.services.course_service.Course_schema.load') as mocked_course_schema_load:
                mocked_course_schema_load.return_value = Course_schema.load(self.course)
                with patch('openapi_server.services.course_service.db.session.add') as mocked_db_session_add:
                    with patch('openapi_server.services.course_service.db.session.commit') as mocked_db_session_commit:
                        result = CourseService.add_course(self.course)
                        self.assertEqual(result, Course_schema.dump(self.course))
    
            mocked_course_query.return_value = Course_schema.load(self.course)
            with self.assertRaises(Exception):
                CourseService.add_course(self.course)
    
    def test_update_course(self):
        with patch('openapi_server.services.course_service.Course.query.filter.one_or_none') as mocked_course_query:
            mocked_course_query.return_value = Course_schema.load(self.course)
            with patch('openapi_server.services.course_service.Course_schema.load') as mocked_course_schema_load:
                mocked_course_schema_load.return_value = Course_schema.load(self.course)
                with patch('openapi_server.services.course_service.db.session.merge') as mocked_db_session_merge:
                    with patch('openapi_server.services.course_service.db.session.commit') as mocked_db_session_commit:
                        result = CourseService.update_course(self.course)
                        self.assertEqual(result, Course_schema.dump(self.course))

            mocked_course_query.return_value = None
            with self.assertRaises(Exception):
                CourseService.update_course(self.course)
    
    def test_delete_course(self):
        with patch('openapi_server.services.course_service.Course.query.filter.one_or_none') as mocked_course_query:
            mocked_course_query.return_value = Course_schema.load(self.course)
            with patch('openapi_server.services.course_service.db.session.delete') as mocked_db_session_delete:
                with patch('openapi_server.services.course_service.db.session.commit') as mocked_db_session_commit:
                    result = CourseService.delete_course(1)
                    self.assertEqual(result, "Course with ID: 1 successfully deleted")
            
            mocked_course_query.return_value = None
            with self.assertRaises(Exception):
                CourseService.delete_course(-1)
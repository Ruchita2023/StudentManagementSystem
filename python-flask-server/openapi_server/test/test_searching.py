from services.searching import *
import unittest

class TestSearching(unittest.TestCase):

    def test_searching_with_no_params(self):
        """
        Test searching function with no search parameters
        """
        search_params = ''
        Model = SomeModel
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.all())

    def test_searching_with_one_param(self):
        """
        Test searching function with one search parameter
        """
        search_params = 'field = "value"'
        Model = SomeModel
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(getattr(Model, 'field') == 'value').all())

    def test_searching_with_multiple_params(self):
        """
        Test searching function with multiple search parameters
        """
        search_params = 'field1 = "value1"; field2 > 5; field3 like "%test%"'
        Model = SomeModel
        result = searching(search_params, Model)
        query_filters = [getattr(Model, 'field1') == 'value1', getattr(Model, 'field2') > 5, getattr(Model, 'field3').like('%test%')]
        self.assertEqual(result.all(), Model.query.filter(*query_filters).all())

    def test_searching_with_less_than_operator(self):
        """
        Test searching function with less than operator
        """
        search_params = 'field < 5'
        Model = SomeModel
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(getattr(Model, 'field') < 5).all())

    def test_searching_with_greater_than_operator(self):
        """
        Test searching function with greater than operator
        """
        search_params = 'field > 5'
        Model = SomeModel
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(getattr(Model, 'field') > 5).all())

    def test_searching_with_less_than_or_equal_to_operator(self):
        """
        Test searching function with less than or equal to operator
        """
        search_params = 'field <= 5'
        Model = SomeModel
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(getattr(Model, 'field') <= 5).all())

    def test_searching_with_greater_than_or_equal_to_operator(self):
        """
        Test searching function with greater than or equal to operator
        """
        search_params = 'field >= 5'
        Model = SomeModel
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(getattr(Model, 'field') >= 5).all())

    def test_searching_with_like_operator(self):
        """
        Test searching function with like operator
        """
        search_params = 'field like "%test%"'
        Model = SomeModel
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(getattr(Model, 'field').like('%test%')).all())

    def test_searching_with_between_operator(self):
        """
        Test searching function with between operator
        """
        search_params = 'field BETWEEN "2" AND "7"'
        Model = SomeModel
        result = searching(search_params, Model)
        self.assertEqual(result.all(), Model.query.filter(getattr(Model, 'field').between('2', '7')).all())

if __name__ == '__main__':
    unittest.main()
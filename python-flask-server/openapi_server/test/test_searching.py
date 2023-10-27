from services.searching import *
import unittest

class TestSearching(unittest.TestCase):
    
    def test_search_params_none(self):
        result = searching(None, Model)
        self.assertEqual(result, Model.query)
        
    def test_search_params_empty_string(self):
        result = searching("", Model)
        self.assertEqual(result, Model.query)
        
    def test_search_params_only_spaces(self):
        result = searching("   ", Model)
        self.assertEqual(result, Model.query)
        
    def test_search_params_single_criterion_equals(self):
        result = searching("name = 'John'", Model)
        self.assertEqual(result.filter_by(name='John'), Model.query.filter_by(name='John'))
        
    def test_search_params_single_criterion_less_than(self):
        result = searching("age < 30", Model)
        self.assertEqual(result.filter(Model.age < 30), Model.query.filter(Model.age < 30))
        
    def test_search_params_single_criterion_greater_than(self):
        result = searching("age > 30", Model)
        self.assertEqual(result.filter(Model.age > 30), Model.query.filter(Model.age > 30))
        
    def test_search_params_single_criterion_less_than_equals(self):
        result = searching("age <= 30", Model)
        self.assertEqual(result.filter(Model.age <= 30), Model.query.filter(Model.age <= 30))
        
    def test_search_params_single_criterion_greater_than_equals(self):
        result = searching("age >= 30", Model)
        self.assertEqual(result.filter(Model.age >= 30), Model.query.filter(Model.age >= 30))
        
    def test_search_params_single_criterion_like(self):
        result = searching("name like '%John%'", Model)
        self.assertEqual(result.filter(Model.name.like('%John%')), Model.query.filter(Model.name.like('%John%')))
        
    def test_search_params_single_criterion_between(self):
        result = searching("age BETWEEN 20 AND 30", Model)
        self.assertEqual(result.filter(Model.age.between(20,30)), Model.query.filter(Model.age.between(20,30)))
        
    def test_search_params_multiple_criteria(self):
        result = searching("name = 'John'; age >= 30; email like '%@gmail.com%'", Model)
        self.assertEqual(result.filter_by(name='John').filter(Model.age >= 30).filter(Model.email.like('%@gmail.com%')), Model.query.filter_by(name='John').filter(Model.age >= 30).filter(Model.email.like('%@gmail.com%')))
        
if __name__ == '__main__':
    unittest.main()
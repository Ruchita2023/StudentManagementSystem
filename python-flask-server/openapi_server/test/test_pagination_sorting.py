from services.pagination_sorting import *
import unittest
from unittest.mock import Mock, patch
from openapi_server.routes.pagination_sorting import pagination_sorting

class TestPaginationSorting(unittest.TestCase):

  def setUp(self):
    self.model = Mock()
    self.model.query = Mock()
    self.model.query.order_by = Mock()
    self.model.query.paginate = Mock()
    self.request = Mock()
    self.request.args = {}
    self.request.args.get = Mock()
  
  def test_pagination_sorting(self):
    self.request.args.get.side_effect = lambda x, default, type: {
        'pageNumber': 1,
        'pageSize': 10,
        'sortBy': 'id',
        'sortDir': 'asc'
    }[x] if x in ('pageNumber', 'pageSize', 'sortBy', 'sortDir') else default
    with patch('openapi_server.routes.pagination_sorting.searching') as searching_mock:
        searching_mock.return_value = self.model.query
        result = pagination_sorting(self.model)
        self.model.query.order_by.assert_called_with(self.model.id.asc())
        self.model.query.paginate.assert_called_with(page=1, per_page=10)
        self.assertEqual(result, self.model.query.paginate().items)

  def test_pagination_sorting_desc(self):
    self.request.args.get.side_effect = lambda x, default, type: {
        'pageNumber': 1,
        'pageSize': 10,
        'sortBy': 'id',
        'sortDir': 'desc'
    }[x] if x in ('pageNumber', 'pageSize', 'sortBy', 'sortDir') else default
    with patch('openapi_server.routes.pagination_sorting.searching') as searching_mock:
        searching_mock.return_value = self.model.query
        result = pagination_sorting(self.model)
        self.model.query.order_by.assert_called_with(self.model.id.desc())
        self.model.query.paginate.assert_called_with(page=1, per_page=10)
        self.assertEqual(result, self.model.query.paginate().items)

  def test_pagination_sorting_search(self):
    self.request.args.get.side_effect = lambda x, default, type: {
        'pageNumber': 1,
        'pageSize': 10,
        'sortBy': 'id',
        'sortDir': 'asc',
        'search': 'test'
    }[x] if x in ('pageNumber', 'pageSize', 'sortBy', 'sortDir', 'search') else default
    with patch('openapi_server.routes.pagination_sorting.searching') as searching_mock:
        searching_mock.return_value = self.model.query
        result = pagination_sorting(self.model)
        searching_mock.assert_called_with('test', self.model)
        self.model.query.order_by.assert_called_with(self.model.id.asc())
        self.model.query.paginate.assert_called_with(page=1, per_page=10)
        self.assertEqual(result, self.model.query.paginate().items)

if __name__ == '__main__':
    unittest.main()
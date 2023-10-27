from services.pagination_sorting import *
import unittest
from unittest.mock import Mock

from openapi_server.utils.constants import PARAM_PAGE_NUMBER, PARAM_PAGE_SIZE, PARAM_SORT_BY, PARAM_SORT_DIR
from openapi_server.services.searching import searching
from app import pagination_sorting


class TestPaginationSorting(unittest.TestCase):

    def setUp(self):
        self.model = Mock()
        self.page_number = 1
        self.page_size = 10
        self.sort_by = 'id'
        self.sort_dir = 'asc'
        self.search_params = 'test'

    def test_pagination_sorting_default_values(self):
        request = Mock(args={})
        expected_result = self.model.query.order_by(getattr(self.model, self.sort_by).asc()).paginate(page=self.page_number, per_page=self.page_size).items
        self.assertEqual(pagination_sorting(self.model), expected_result)

    def test_pagination_sorting_custom_values(self):
        request = Mock(args={PARAM_PAGE_NUMBER: 2, PARAM_PAGE_SIZE: 20, PARAM_SORT_BY: 'name', PARAM_SORT_DIR: 'desc'})
        expected_result = self.model.query.order_by(getattr(self.model, 'name').desc()).paginate(page=2, per_page=20).items
        self.assertEqual(pagination_sorting(self.model), expected_result)

    def test_pagination_sorting_search_params(self):
        request = Mock(args={'search': self.search_params})
        q = searching(self.search_params, self.model)
        expected_result = q.order_by(getattr(self.model, self.sort_by).asc()).paginate(page=self.page_number, per_page=self.page_size).items
        self.assertEqual(pagination_sorting(self.model), expected_result)
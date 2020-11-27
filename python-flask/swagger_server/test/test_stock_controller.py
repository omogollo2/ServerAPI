# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.stock_product import StockProduct  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStockController(BaseTestCase):
    """StockController integration test stubs"""

    def test_put_stock(self):
        """Test case for put_stock

        actualiza el stock de un producto
        """
        body = StockProduct()
        response = self.client.open(
            '/omogollo2/ServerAPI/1.0.0/stock/{productId}'.format(product_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_stock(self):
        """Test case for search_stock

        devuelve el stock de la tienda
        """
        query_string = [('search_string', 'search_string_example'),
                        ('limit', 5)]
        response = self.client.open(
            '/omogollo2/ServerAPI/1.0.0/stock',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

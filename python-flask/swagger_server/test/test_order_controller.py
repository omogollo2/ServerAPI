# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.order import Order  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrderController(BaseTestCase):
    """OrderController integration test stubs"""

    def test_delete_order(self):
        """Test case for delete_order

        borra un pedido
        """
        response = self.client.open(
            '/omogollo2/ServerAPI/1.0.0/order/{orderId}'.format(order_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_order(self):
        """Test case for get_order

        Devuelve los datos un pedido
        """
        response = self.client.open(
            '/omogollo2/ServerAPI/1.0.0/order/{orderId}'.format(order_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_order(self):
        """Test case for post_order

        crea un nuevo pedido
        """
        body = Order()
        response = self.client.open(
            '/omogollo2/ServerAPI/1.0.0/order',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

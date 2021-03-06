# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.product import Product  # noqa: F401,E501
from swagger_server import util


class StockProduct(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, product: Product=None, stock: int=None):  # noqa: E501
        """StockProduct - a model defined in Swagger

        :param product: The product of this StockProduct.  # noqa: E501
        :type product: Product
        :param stock: The stock of this StockProduct.  # noqa: E501
        :type stock: int
        """
        self.swagger_types = {
            'product': Product,
            'stock': int
        }

        self.attribute_map = {
            'product': 'product',
            'stock': 'stock'
        }
        self._product = product
        self._stock = stock

    @classmethod
    def from_dict(cls, dikt) -> 'StockProduct':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StockProduct of this StockProduct.  # noqa: E501
        :rtype: StockProduct
        """
        return util.deserialize_model(dikt, cls)

    @property
    def product(self) -> Product:
        """Gets the product of this StockProduct.


        :return: The product of this StockProduct.
        :rtype: Product
        """
        return self._product

    @product.setter
    def product(self, product: Product):
        """Sets the product of this StockProduct.


        :param product: The product of this StockProduct.
        :type product: Product
        """
        if product is None:
            raise ValueError("Invalid value for `product`, must not be `None`")  # noqa: E501

        self._product = product

    @property
    def stock(self) -> int:
        """Gets the stock of this StockProduct.


        :return: The stock of this StockProduct.
        :rtype: int
        """
        return self._stock

    @stock.setter
    def stock(self, stock: int):
        """Sets the stock of this StockProduct.


        :param stock: The stock of this StockProduct.
        :type stock: int
        """
        if stock is None:
            raise ValueError("Invalid value for `stock`, must not be `None`")  # noqa: E501

        self._stock = stock

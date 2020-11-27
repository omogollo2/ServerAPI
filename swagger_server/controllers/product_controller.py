import connexion
import six

from swagger_server.models.product import Product  # noqa: E501
from swagger_server import util


def delete_product(product_id):  # noqa: E501
    """borrar un producto

     # noqa: E501

    :param product_id: id del producto a borrar
    :type product_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_product(product_id):  # noqa: E501
    """devuelve la información de un producto

     # noqa: E501

    :param product_id: id del producto a consultar
    :type product_id: int

    :rtype: Product
    """
    return 'do some magic!'


def put_product(product_id, body=None):  # noqa: E501
    """actuliza la información de un producto

     # noqa: E501

    :param product_id: id del producto a actualizar
    :type product_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Product.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

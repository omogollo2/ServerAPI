import connexion
import six

from swagger_server.models.order import Order  # noqa: E501
from swagger_server.models.product import Product  # noqa: E501
from swagger_server.models.stock_product import StockProduct  # noqa: E501
from swagger_server import util


def delete_order(order_id):  # noqa: E501
    """borra un pedido

     # noqa: E501

    :param order_id: id del pedido a eliminar
    :type order_id: int

    :rtype: None
    """
    return 'do some magic!'


def delete_product(product_id):  # noqa: E501
    """borrar un producto

     # noqa: E501

    :param product_id: id del producto a borrar
    :type product_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_order(order_id):  # noqa: E501
    """Devuelve los datos un pedido

     # noqa: E501

    :param order_id: id del pedido a consultar
    :type order_id: int

    :rtype: Order
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


def post_order(order_id, body=None):  # noqa: E501
    """crea un nuevo pedido

     # noqa: E501

    :param order_id: id del pedido recien creado
    :type order_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: Order
    """
    if connexion.request.is_json:
        body = Order.from_dict(connexion.request.get_json())  # noqa: E501
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


def put_stock(body=None):  # noqa: E501
    """actualiza el stock de un producto

    actualiza el stock de un producto con determinado identificador # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [StockProduct.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def search_stock(search_string=None, limit=None):  # noqa: E501
    """devuelve el stock de la tienda

    By passing in the appropriate options, you can search for available inventory in the system  # noqa: E501

    :param search_string: parametro que permite obtener el stock de un determinado producto
    :type search_string: str
    :param limit: número máximo de productos de los que se devolverá info
    :type limit: int

    :rtype: List[StockProduct]
    """
    return 'do some magic!'

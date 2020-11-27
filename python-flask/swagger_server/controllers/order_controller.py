import connexion
import six

from swagger_server.models.order import Order  # noqa: E501
from swagger_server import util


def delete_order(order_id):  # noqa: E501
    """borra un pedido

     # noqa: E501

    :param order_id: id del pedido a eliminar
    :type order_id: int

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

import connexion
import pymongo
import six

from swagger_server.models.order import Order  # noqa: E501
from swagger_server import util


client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.m8mga.mongodb.net/test?retryWrites=true&w=majority")
db=client.get_database('ist')

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


def post_order(body=None):  # noqa: E501
    """crea un nuevo pedido

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Order
    """
    if connexion.request.is_json:
        body = Order.from_dict(connexion.request.get_json())  # noqa: E501
        collection = db.order
        order_data = {
            'id': body.id,
            'orderDate': body.order_date,
            'shipDate': body.ship_date,
            'items': body.items,
            'totalPrice': body.total_price,
            'shipAddress': body.ship_adress,
            'client': body.client
        }
        collection.insert_one(order_data)
    return 'do some magic!'

import connexion
import pymongo

from swagger_server.models.order import Order  # noqa: E501

client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.m8mga.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('ist')


def delete_order(order_id):  # noqa: E501
    """borra un pedido

     # noqa: E501

    :param order_id: id del pedido a eliminar
    :type order_id: int

    :rtype: None
    """

    collection = db.order
    collection.delete_one({'id': order_id})

    return 'OK'


def get_order(order_id):  # noqa: E501
    """Devuelve los datos un pedido

     # noqa: E501

    :param order_id: id del pedido a consultar
    :type order_id: int

    :rtype: Order
    """

    collection = db.order
    order = collection.find_one({'id': order_id})

    return Order(order['id'], order['orderDate'], order['shipDate'], order['items'], order['shipAddress'],
                 order['client'])


def post_order(body):  # noqa: E501
    """crea un nuevo pedido

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Order
    """

    if connexion.request.is_json:
        # body = Order.from_dict(connexion.request.get_json())  # noqa: E501
        collection = db.order
        order_data = {
            'id': body['id'],
            'orderDate': str(body['orderDate']),
            'shipDate': str(body['shipDate']),
            'item_id': body['items'][0]['id'],
            'item_name': body['items'][0]['name'],
            'item_price': body['items'][0]['price'],
            'totalPrice': body['totalPrice'],
            'shipAddress': body['shipAddress'],
            'client': body['client']['name']
        }

        collection.insert_one(order_data)
    return 'OK'

import connexion
import pymongo
import six

from swagger_server.models.product import Product  # noqa: E501
from swagger_server import util

client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.m8mga.mongodb.net/test?retryWrites=true&w=majority")
db=client.get_database('ist')

def delete_product(product_id):  # noqa: E501
    """borrar un producto

     # noqa: E501

    :param product_id: id del producto a borrar
    :type product_id: int

    :rtype: None
    """
    collection = db.product
    collection.delete_one({'id': product_id})

    return 'OK'


def get_product(product_id):  # noqa: E501
    """devuelve la información de un producto

     # noqa: E501

    :param product_id: id del producto a consultar
    :type product_id: int

    :rtype: Product
    """

    collection = db.product
    product = collection.find_one({'id': product_id})
    return Product(product['id'], product['name'], product['price'])


def put_product(product_id, body):  # noqa: E501
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
        collection = db.product
        myquery = {"product_id": product_id}
        new_values = {"$set": {
            'id': body.id,
            'name': body.name,
            'price': body.price
        }}

        collection.update_one(myquery, new_values)
    return 'OK!'

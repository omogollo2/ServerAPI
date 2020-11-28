import connexion
import pymongo
import six

from swagger_server.models import Product
from swagger_server.models.stock_product import StockProduct  # noqa: E501
from swagger_server import util

client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.m8mga.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('ist')


def put_stock(product_id, body=None):  # noqa: E501
    """actualiza el stock de un producto

    actualiza el stock de un producto con determinado identificador # noqa: E501

    :param product_id: id del producto a actualizar
    :type product_id: int
    :param body:
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        # body = StockProduct.from_dict(connexion.request.get_json())  # noqa: E501

        collection = db.stock
        myquery = {"product.id": product_id}
        new_values = {"$set": {
            'stock': body['stock']
        }}

        collection.update_one(myquery, new_values)

    return 'OK'


def search_stock(search_string=None, limit=None):  # noqa: E501
    """devuelve el stock de la tienda
    Devuelve el stock de cada producto de la tienda o de uno en especifico  # noqa: E501
    :param search_string: parametro que permite obtener el stock de un determinado producto
    :type search_string: str
    :param limit: número máximo de productos de los que se devolverá info
    :type limit: int
    :rtype: List[StockProduct]
    """

    collection = db.stock
    stock = list()
    if search_string is None:
        # Obtener el stock de la tienda

        for i in collection.find():
            stock.append(StockProduct(Product(i['product']['id'], i['product']['name'], i['product']['price']), i['stock']))
    else:
        # Obtener stock de un producto
        s = collection.find_one({'product.name': search_string})
        stock.append(StockProduct(Product(s['product']['id'], s['product']['name'], s['product']['price']), s['stock']))

    return stock

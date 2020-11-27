import connexion
import pymongo
import six

from swagger_server.models.stock_product import StockProduct  # noqa: E501
from swagger_server import util

client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.m8mga.mongodb.net/test?retryWrites=true&w=majority")
db=client.get_database('ist')

def put_stock(product_id, body=None):  # noqa: E501
    """actualiza el stock de un producto

    actualiza el stock de un producto con determinado identificador # noqa: E501

    :param product_id: id del producto a actualizar
    :type product_id: int
    :param body:
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [StockProduct.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501

    collection = db.stock
    myquery = {"product": product_id }
    new_values = {"$set": {
        'product': body[0].product,
        'stock': body[0].stock
    }}

    collection.update_one(myquery, new_values)
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

    collection = db.stock
    stock = collection.find_one({'product': search_string})
    return StockProduct(stock['product'], stock['stock'])

import connexion
import six

from swagger_server.models.stock_product import StockProduct  # noqa: E501
from swagger_server import util


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

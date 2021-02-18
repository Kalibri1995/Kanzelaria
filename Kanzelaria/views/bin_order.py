from pyramid.view import view_config
from pyramid.response import Response

from sqlalchemy.exc import DBAPIError

from .. import models
from ..main.canzelaria_parser import parse_products_info
from ..main.bin_saver import append_order


@view_config(route_name='bin', renderer='../templates/bin_order.jinja2')
def my_view(request):
    products = parse_products_info(request)
    orders = append_order(request, products)

    try:
        shops = request.dbsession.query(models.Shop).all()
    except DBAPIError:
        return Response("db_err_msg", content_type='text/plain', status=500)
    return {'bin': orders[request.client_addr], 'shops': shops, 'project': 'Kanzelaria'}

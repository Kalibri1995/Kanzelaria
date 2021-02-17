from pyramid.view import view_config
from pyramid.response import Response

from sqlalchemy.exc import DBAPIError

from .. import models


@view_config(route_name='home', renderer='../templates/shop_content.jinja2')
def my_view(request):
    try:
        products = request.dbsession.query(models.Product).all()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'products': products, 'project': 'Kanzelaria'}


db_err_msg = "Ошибка БД"

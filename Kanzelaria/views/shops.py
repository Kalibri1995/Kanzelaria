from pyramid.view import view_config
from pyramid.response import Response

from sqlalchemy.exc import DBAPIError

from .. import models


@view_config(route_name='shops', renderer='../templates/shops.jinja2')
def my_view(request):
    try:
        shops = request.dbsession.query(models.Shop).all()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'shops': shops, 'project': 'Kanzelaria'}


db_err_msg = "Ошибка БД"
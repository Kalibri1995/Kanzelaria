from pyramid.view import view_config
from pyramid.response import Response

from sqlalchemy.exc import DBAPIError

from .. import models


@view_config(route_name='order', renderer='../templates/final_order.jinja2')
def my_view(request):
    # Нужно вернуть объект order класса OrderDB
    return {'project': 'Kanzelaria'}


db_err_msg = "Ошибка БД"

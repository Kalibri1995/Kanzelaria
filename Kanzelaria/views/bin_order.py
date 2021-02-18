from pyramid.view import view_config
from pyramid.response import Response

from sqlalchemy.exc import DBAPIError

from .. import models


@view_config(route_name='bin', renderer='../templates/bin_order.jinja2')
def my_view(request):
    """
    В реквесте будут данные из чекбоксов по имени check_product, они несут с собой id товаров

    Так же есть поля 'count_of_{product.id}, т.е. нужно собрать сначала айдишники, а потом пройтись по ним и взять
    из параметров соотв. поля

    Ну и взять из таблицы записи, отдать их на страницу, можно сразу посчитать стоимость, и тут уже переходим
    к оформлению заказа
    """
    try:
        shops = request.dbsession.query(models.Shop).all()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'shops': shops, 'project': 'Kanzelaria'}


db_err_msg = "Ошибка БД"

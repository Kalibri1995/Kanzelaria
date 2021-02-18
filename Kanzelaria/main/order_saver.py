import transaction

from Kanzelaria.models.Order import Order
from Kanzelaria.models.Bin import Bin


def save_order_info(request, name: str, phone: str, shop_id: int, bin: Bin):
    order = Order(
        name=name,
        phone=phone,
        shop_id=shop_id,
        sum=bin.total_sum,
        products=str(bin.products)
    )
    request.dbsession.add(order)
    transaction.commit()

    query = request.dbsession.query(Order)
    return query.first()

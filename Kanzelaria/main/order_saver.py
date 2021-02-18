import transaction

from Kanzelaria.models.Order import Order
from Kanzelaria.models.Bin import Bin


def get_products_info(products: list) -> str:
    res = ""
    for product in products:
        res += f"{product.name} {product.desc} {product.count} шт. по {product.price} руб.\n"

    return res


def save_order_info(request, name: str, phone: str, shop_id: int, bin: Bin):
    order = Order(
        name=name,
        phone=phone,
        shop_id=shop_id,
        sum=bin.total_sum,
        products=get_products_info(bin.products)
    )
    request.dbsession.add(order)
    transaction.commit()

    query = request.dbsession.query(Order)
    return query.order_by(Order.id.desc()).first()

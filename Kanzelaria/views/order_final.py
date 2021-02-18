from pyramid.view import view_config
from ..main.bin_saver import all_orders
from ..main.order_saver import save_order_info
from ..models.order_frontend import OrderFrontend


@view_config(route_name='order', renderer='../templates/final_order.jinja2')
def my_view(request):
    order_info = save_order_info(
        request,
        request.params['name'],
        request.params['phone_number'],
        int(request.params['choose_shop']),
        all_orders[request.client_addr])
    order_front = OrderFrontend(
        request,
        order_info.id,
        order_info.name,
        order_info.phone,
        order_info.sum,
        order_info.shop_id,
        order_info.products
    )
    all_orders[request.client_addr] = None
    return {'order': order_front, 'project': 'Kanzelaria'}

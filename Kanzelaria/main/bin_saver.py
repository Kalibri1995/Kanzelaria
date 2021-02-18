from Kanzelaria.models.Bin import Bin

all_orders = dict()


def append_order(request, products: list):
    all_orders[request.client_addr] = Bin(request.client_addr, products)
    return all_orders

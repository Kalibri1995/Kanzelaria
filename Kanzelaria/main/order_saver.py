from Kanzelaria.models.Bin import Bin

all_orders = dict()


def append_order(request, products: list):
    #if not all_orders.__contains__(request.client_addr):
    all_orders[request.client_addr] = Bin(request.client_addr, products)

    return all_orders

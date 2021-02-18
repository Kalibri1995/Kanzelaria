class Bin(object):
    def __init__(self, owner_id, products: list):
        self.owner_id = owner_id
        self.products = products
        self.total_sum = calculate_sum(products)


def calculate_sum(products: list) -> int:
    summa = 0
    for product in products:
        summa += product.price * product.count

    return summa

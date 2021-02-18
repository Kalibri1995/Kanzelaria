from Kanzelaria import models
from Kanzelaria.models import Shop


class OrderFrontend(object):
    def __init__(self, request, id, name, phone, sum, shop_id, products):
        self.id = id
        self.name = name
        self.phone = phone
        self.sum = sum
        self.shop = get_shop_by_id(request, shop_id)
        self.products = products

    def get_shop_info(self):
        return f"{self.shop.name}\n{self.shop.desc}"


def get_shop_by_id(request, shop_id: int) -> Shop:
    shops = request.dbsession.query(models.Shop).all()
    for shop in shops:
        if shop.id == shop_id:
            return shop

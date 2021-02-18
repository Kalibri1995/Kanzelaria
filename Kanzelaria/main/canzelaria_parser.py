from Kanzelaria import models
from Kanzelaria.models.product_info import ProductInfo


def parse_products_info(request) -> list:
    selected_products = request.params.getall('check_product')
    selected_products_set = set(selected_products)
    prods = request.dbsession.query(models.Product).all()
    result = list()

    for prod in prods:
        if str(prod.id) in selected_products_set:
            result.append(ProductInfo(
                prod.id, prod.name, prod.desc, prod.price, int(request.params[f'count_of_{prod.id}']), prod.adr))

    return result

import json


def read_data(path='data/categories.json'):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def read_products(category_id=None, kw=None, tuGia=None, denGia=None):
    products = read_data('data/products.json')

    if category_id:
        category_id = int(category_id)
        products = [p for p in products if p['category_id'] == category_id]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    if tuGia and denGia:
        tuGia = float(tuGia)
        denGia = float(denGia)
        products = [p for p in products if tuGia <= p['price'] <= denGia]
    return products


def get_product_by_id(product_id):
    products = read_data(path='data/products.json')
    for p in products:
        if p["id"] == product_id:
            return p

from flask import render_template, request
from saleapp import app, utils


@app.route("/")
def index():
    categories = utils.read_data()

    return render_template('index.html', categories=categories)


@app.route('/products', methods=['POST', 'GET'])
def product_list():
    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')
    tuGia = request.args.get('tugia')
    denGia = request.args.get('dengia')

    products = utils.read_products(cate_id, kw, tuGia, denGia)

    return render_template('products.html', products=products)


@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = utils.get_product_by_id(product_id=product_id)

    return render_template('product-detail.html',
                           product=product)


if __name__ == "__main__":
    app.run(debug=True)

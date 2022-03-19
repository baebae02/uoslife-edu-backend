from flask import Blueprint, render_template

from rental_products.models import Product

bp = Blueprint('product', __name__, url_prefix='/product')


@bp.route('/list')
def _list():
    product_list = Product.query.order_by(Product.created_at.desc())
    return render_template('product/product_list.html', product_list=product_list)


@bp.route('/detail/<product_id>')
def detail(product_id):
    product = Product.query.get_or_404(product_id)
    # return product + '물품이름'
    return render_template('product/product_detail.html', product=product)

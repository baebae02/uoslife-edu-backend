import uuid
from datetime import datetime
from flask import Blueprint, render_template, request, jsonify, session
from rental_products import db
from rental_products.models import Product

bp = Blueprint('product', __name__, url_prefix='/product')


@bp.route('/list')
def _list():
    product_list = Product.query.order_by(Product.created_at.desc())
    return render_template('product/product_list.html', product_list=product_list)


@bp.route('/add', methods=['POST'])
def _add_product():
    result = request.json
    nickname = result.get('nickname')
    category = result.get('category')
    admin_id = "96fc6cb6-c6b8-4a7e-9f6d-959828a6b832"
    student_id = "96fc6cb6-c6b8-4a7e-9f6d-959828a6b839"
    try:
        product = Product(id=uuid.uuid4(),
                          nickname=nickname,
                          category=category,
                          admin_id=admin_id,
                          student_id=student_id,
                          created_at=datetime.now(),
                          updated_at=datetime.now())
        db.session.add(product)
        db.session.commit()
        return "success"
    except Exception as e:
        print(e)
        return "fail"

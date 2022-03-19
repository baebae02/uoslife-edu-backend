from flask import Blueprint, url_for, redirect
from rental_products.models import User, Product
bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return redirect(url_for('product._list'))


@bp.route('/user', methods=['GET'])
def get_user():
    users = User.query.first()
    return users.nickname


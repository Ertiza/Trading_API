from flask import Blueprint, request, jsonify
from ..models.order import Order
from .. import db

order_routes = Blueprint('order_routes', __name__)

@order_routes.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.__repr__() for order in orders])

@order_routes.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify(order.__repr__())

@order_routes.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = Order(user_id=data['user_id'], asset_id=data['asset_id'], quantity=data['quantity'], price=data['price'], order_type=data['order_type'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify(new_order.__repr__()), 201
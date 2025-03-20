from flask import Blueprint, request, jsonify
from ..models.portfolio import Portfolio
from .. import db

portfolio_routes = Blueprint('portfolio_routes', __name__)

@portfolio_routes.route('/portfolios', methods=['GET'])
def get_portfolios():
    portfolios = Portfolio.query.all()
    return jsonify([portfolio.__repr__() for portfolio in portfolios])

@portfolio_routes.route('/portfolios/<int:portfolio_id>', methods=['GET'])
def get_portfolio(portfolio_id):
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    return jsonify(portfolio.__repr__())

@portfolio_routes.route('/portfolios', methods=['POST'])
def create_portfolio():
    data = request.get_json()
    new_portfolio = Portfolio(user_id=data['user_id'], asset_id=data['asset_id'], quantity=data['quantity'])
    db.session.add(new_portfolio)
    db.session.commit()
    return jsonify(new_portfolio.__repr__()), 201
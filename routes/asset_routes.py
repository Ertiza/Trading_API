from flask import Blueprint, request, jsonify
from ..models.asset import Asset
from .. import db

asset_routes = Blueprint('asset_routes', __name__)

@asset_routes.route('/assets', methods=['GET'])
def get_assets():
    assets = Asset.query.all()
    return jsonify([asset.__repr__() for asset in assets])

@asset_routes.route('/assets/<int:asset_id>', methods=['GET'])
def get_asset(asset_id):
    asset = Asset.query.get_or_404(asset_id)
    return jsonify(asset.__repr__())

@asset_routes.route('/assets', methods=['POST'])
def create_asset():
    data = request.get_json()
    new_asset = Asset(name=data['name'], symbol=data['symbol'], price=data['price'])
    db.session.add(new_asset)
    db.session.commit()
    return jsonify(new_asset.__repr__()), 201
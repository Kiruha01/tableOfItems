from flask import Blueprint, request
from flask_restful import Api, Resource, marshal_with

from models import Item, item_fields

items_page = Blueprint('table_page', __name__)
api = Api(items_page)


class ItemsView(Resource):

    @marshal_with(item_fields)
    def get(self):
        return Item.query.all()



api.add_resource(ItemsView, '/')

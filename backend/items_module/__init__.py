from flask import Blueprint
from flask_restful import Api, Resource, marshal_with, reqparse

from models import Item, item_fields

items_page = Blueprint('table_page', __name__)
api = Api(items_page)


class ItemsView(Resource):

    @marshal_with(item_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('sorting', choices=('name', 'count', 'distance'))
        parser.add_argument('filter_field', choices=('name', 'date', 'count', 'distance'))
        parser.add_argument('filter_type', choices=('eq', 'in', 'lt', 'gt'))
        parser.add_argument('filter_value', type=str)
        args = parser.parse_args()

        query = Item.query

        if args['sorting']:
            query = query.order_by(args['sorting'])

        return query.all()



api.add_resource(ItemsView, '/')

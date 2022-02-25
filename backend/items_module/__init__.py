from flask import Blueprint
from flask_restful import Api, Resource, marshal, reqparse, abort
from sqlalchemy.exc import DataError


from models import Item, item_fields

items_page = Blueprint('table_page', __name__)
api = Api(items_page)


def filter_query(Model, query, field: str, type: str, value: str):
    if not (field or type or value):
        return query

    if field is None:
        abort(400, message={'filter_field': 'field is missing'})
    if type is None:
        abort(400, message={'filter_type': 'field is missing'})
    if value is None:
        abort(400, message={'filter_value': 'field is missing'})

    if type == 'eq':
        return query.filter(getattr(Model, field) == value)
    elif type == 'in':
        if field == 'name':
            return query.filter(getattr(Model, field).like(value))
        else:
            abort(400, message={'field_type': "type 'in' support only 'name' field"})
    elif type == 'lt':
        return query.filter(getattr(Model, field) < value)
    elif type == 'gt':
        return query.filter(getattr(Model, field) > value)
    return query


class ItemsView(Resource):
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

        query = filter_query(Item, query, args['filter_field'], args['filter_type'], args['filter_value'])

        try:
            return marshal(query.all(), item_fields)
        except DataError as e:
            print(e.params)
            abort(400, messgae={"filter_value": "Invalid format"})


api.add_resource(ItemsView, '/')

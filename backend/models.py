from flask_sqlalchemy import SQLAlchemy
from flask_restful import fields

db = SQLAlchemy()


class Item(db.Model):
    __tablename__ = 'table'
    item_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    count = db.Column(db.Integer, nullable=False, default=1)
    distance = db.Column(db.Numeric(6, 2), nullable=False)


item_fields = {
    'item_id': fields.Integer,
    'date': fields.DateTime,
    'name': fields.String,
    'count': fields.Integer,
    'distance': fields.Float
}

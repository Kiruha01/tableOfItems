from flask_sqlalchemy import SQLAlchemy
from flask_restful import fields

db = SQLAlchemy()


class DateFormat(fields.Raw):
    def format(self, value):
        return value.strftime('%Y-%m-%d')


class Item(db.Model):
    __tablename__ = 'table'
    __table_args__ = (
        db.CheckConstraint('count > 0'),
        db.CheckConstraint('distance > 0'),
    )
    item_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    count = db.Column(db.Integer, nullable=False, default=1)
    distance = db.Column(db.Numeric(6, 2), nullable=False)


item_fields = {
    'item_id': fields.Integer,
    'date': DateFormat,
    'name': fields.String,
    'count': fields.Integer,
    'distance': fields.Float
}

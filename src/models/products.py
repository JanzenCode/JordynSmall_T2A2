from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Products(db.Model):
    __tablename__ = 'Products'

    brand = db.Column(db.String(20), nullable=True)
    description = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    type = db.Column(db.String)
    sku = db.Column(db.String(12))
    item_number = db.Column(db.Integer, nullable=False)



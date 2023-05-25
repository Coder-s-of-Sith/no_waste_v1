from .database import db
from flask_login import UserMixin

class Customer(db.Model,UserMixin):
    customer_id = db.Column(db.Integer, primary_key=True,autoincrement = True)
    c_name = db.Column(db.String(100), nullable=False)
    c_mail = db.Column(db.String(100), nullable=False)
    c_password = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    daily_collection = db.Column(db.Boolean)
    daily_collection_reward_points = db.Column(db.Integer)
    
    def __init__(self, c_name, c_mail, c_password, address, daily_collection, daily_collection_reward_points):
        self.c_name = c_name
        self.c_mail = c_mail
        self.c_password = c_password
        self.address = address
        self.daily_collection = daily_collection
        self.daily_collection_reward_points = daily_collection_reward_points

# class DailyCollectionOrders(db.Model):
#     dc_order_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
#     collector_id = db.Column(db.Integer, db.ForeignKey('collector.collector_id'), nullable=False)
#     date = db.Column(db.DateTime)
#     organic_waste = db.Column(db.Integer)
#     dry_waste = db.Column(db.Integer)
#     non_recyclable_waste = db.Column(db.Integer)
#     rating = db.Column(db.Integer)
#     feedback = db.Column(db.String(200))

# class Collector(db.Model):
#     collector_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
#     name = db.Column(db.String(100), nullable=False)
#     contact_number = db.Column(db.Integer)
#     email_id = db.Column(db.String(100), nullable=False)
#     aadhaar_number = db.Column(db.String(16), nullable=False)
#     location_id = db.Column(db.Integer)
#     collector_address = db.Column(db.String(200))


# class LocalVendor(db.Model):
#     vendor_id = db.Column(db.Integer, primary_key=True)
#     vendor_name = db.Column(db.String(100), nullable=False)
#     location_id = db.Column(db.Integer, nullable=False)
#     area_covered = db.Column(db.Integer)
#     address = db.Column(db.String(200))
#     vmail = db.Column(db.String(100))
#     password = db.Column(db.String(50))

#     orders_on_demand = db.relationship('OrderOnDemand', secondary='order_on_demand_vendors')

# class OrderOnDemand(db.Model):
#     ood_order_id = db.Column(db.Integer, primary_key=True)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
#     product_selected_1 = db.Column(db.String(100))
#     product_selected_2 = db.Column(db.String(100))
#     product_selected_3 = db.Column(db.String(100))
#     product_selected_4 = db.Column(db.String(100))
#     product_selected_5 = db.Column(db.String(100))

#     vendors = db.relationship('LocalVendor', secondary='order_on_demand_vendors')
#     order_details = db.relationship('OrderOnDemandOrder', backref='order')

# class OrderOnDemandVendor(db.Model):
#     ood_order_id = db.Column(db.Integer, db.ForeignKey('order_on_demand.ood_order_id'), primary_key=True)
#     vendor_id = db.Column(db.Integer, db.ForeignKey('local_vendor.vendor_id'), primary_key=True)
#     rating = db.Column(db.Integer)
#     feedback = db.Column(db.String(200))
from Data.Models.customers import Customer
from Data.db import session


def get_all_customers():
    return session.query(Customer).all()


def get_customer_by_id(id):
    return session.query(Customer).filter(Customer.customerNumber == id).first()


def get_customer_by_name(pattern):
    # Post.query.filter(Post.tags.like(search)).all()
    return session.query(Customer).filter(Customer.customerName.like(f'%{pattern}%')).all()


def store_changes():
   session.commit()


def store_new_first_name(customer, new_value):
    try:
        customer.contactFirstName = new_value
        # ....
        session.commit()
    except:
        session.rollback()
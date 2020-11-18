from Data.db import Base
import sqlalchemy as sa

class Customer(Base):
    __tablename__ = 'customers'

    customerNumber = sa.Column(sa.Integer, primary_key=True)
    customerName = sa.Column(sa.String(50), nullable=False)
    contactLastName = sa.Column(sa.String(50), nullable=False)
    contactFirstName = sa.Column(sa.String(50), nullable=False)
    phone = sa.Column(sa.String(50), nullable=False)
    addressLine1 = sa.Column(sa.String(50), nullable=False)
    addressLine2 = sa.Column(sa.String(50), nullable=True)
    city = sa.Column(sa.String(50), nullable=False)
    state = sa.Column(sa.String(50), nullable=True)
    postalCode = sa.Column(sa.String(15), nullable=True)
    country = sa.Column(sa.String(50), nullable=False)

    def __repr__(self):
        return self.customerName
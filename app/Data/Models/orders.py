from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

class Order(Base):
    __tablename__ = 'orders'

    orderNumber = sa.Column(sa.Integer, primary_key=True)
    orderDate = sa.Column(sa.Date, nullable=False)
    requiredDate = sa.Column(sa.Date, nullable=False)
    shippedDate = sa.Column(sa.Date, nullable=True)
    status = sa.Column(sa.String(15), nullable=False)
    comments = sa.Column(sa.Text, nullable=True)
    customerNumber = sa.Column(sa.Integer, sa.ForeignKey('customers.customerNumber'), nullable=True)

    order_lines = relationship("OrderDetail", back_populates="order")

    def __repr__(self):
        return self.status
from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

class OrderDetail(Base):
    __tablename__ = 'orderdetails'

    orderNumber = sa.Column(sa.Integer, sa.ForeignKey('orders.orderNumber'), primary_key=True)
    productCode = sa.Column(sa.String(15), sa.ForeignKey('products.productCode'), primary_key=True)
    quantityOrdered = sa.Column(sa.Integer, nullable=False)
    priceEach = sa.Column(sa.DECIMAL(10, 2), nullable=False)
    orderLineNumber = sa.Column(sa.SmallInteger, nullable=False)

    order = relationship("Order", back_populates="order_lines")
    product = relationship("Product", back_populates="orders")
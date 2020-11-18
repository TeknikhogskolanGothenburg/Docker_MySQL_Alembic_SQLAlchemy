from Data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'products'

    productCode = sa.Column(sa.String(15), primary_key=True)
    productName = sa.Column(sa.String(70), nullable=False)
    productLine = sa.Column(sa.String(50), nullable=False)
    productScale = sa.Column(sa.String(10), nullable=False)
    productVendor = sa.Column(sa.String(50), nullable=False)
    productDescription = sa.Column(sa.Text, nullable=False)
    quantityInStock = sa.Column(sa.SmallInteger, nullable=False)
    buyPrice = sa.Column(sa.DECIMAL(10, 2), nullable=False)
    MSRP = sa.Column(sa.DECIMAL(10, 2), nullable=False)

    orders = relationship("OrderDetail", back_populates="product")

    def __repr__(self):
        return self.productName
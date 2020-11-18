"""Create OrderDetails Table

Revision ID: ddcc8f6a0a1f
Revises: 943e20c70d03
Create Date: 2020-11-18 10:03:13.130946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddcc8f6a0a1f'
down_revision = '943e20c70d03'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orderdetails',
        sa.Column('orderNumber', sa.Integer, sa.ForeignKey('orders.orderNumber'), primary_key=True),
        sa.Column('productCode', sa.String(15), sa.ForeignKey('products.productCode'), primary_key=True),
        sa.Column('quantityOrdered', sa.Integer, nullable=False),
        sa.Column('priceEach', sa.DECIMAL(10, 2), nullable=False),
        sa.Column('orderLineNumber', sa.SmallInteger, nullable=False),
    )


def downgrade():
    op.drop_table('orderdetails')

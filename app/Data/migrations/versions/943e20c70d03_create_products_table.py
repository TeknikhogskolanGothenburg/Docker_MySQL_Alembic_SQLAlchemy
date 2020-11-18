"""Create Products Table

Revision ID: 943e20c70d03
Revises: b90f5e00c818
Create Date: 2020-11-18 10:02:56.810003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '943e20c70d03'
down_revision = 'b90f5e00c818'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'products',
        sa.Column('productCode', sa.String(15), primary_key=True),
        sa.Column('productName', sa.String(70), nullable=False),
        sa.Column('productLine', sa.String(50), nullable=False),
        sa.Column('productScale', sa.String(10), nullable=False),
        sa.Column('productVendor', sa.String(50), nullable=False),
        sa.Column('productDescription', sa.Text, nullable=False),
        sa.Column('quantityInStock', sa.SmallInteger, nullable=False),
        sa.Column('buyPrice', sa.DECIMAL(10, 2), nullable=False),
        sa.Column('MSRP', sa.DECIMAL(10, 2), nullable=False),
    )


def downgrade():
    op.drop_table('products')

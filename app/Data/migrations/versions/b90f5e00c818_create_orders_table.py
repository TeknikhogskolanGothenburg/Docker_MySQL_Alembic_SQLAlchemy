"""Create Orders Table

Revision ID: b90f5e00c818
Revises: b79efe169ade
Create Date: 2020-11-18 10:02:35.803208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b90f5e00c818'
down_revision = 'b79efe169ade'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orders',
        sa.Column('orderNumber', sa.Integer, primary_key=True),
        sa.Column('orderDate', sa.Date, nullable=False),
        sa.Column('requiredDate', sa.Date, nullable=False),
        sa.Column('shippedDate', sa.Date, nullable=True),
        sa.Column('status', sa.String(15), nullable=False),
        sa.Column('comments', sa.Text, nullable=True),
        sa.Column('customerNumber', sa.Integer, sa.ForeignKey('customers.customerNumber'))
    )


def downgrade():
    op.drop_table('orders')

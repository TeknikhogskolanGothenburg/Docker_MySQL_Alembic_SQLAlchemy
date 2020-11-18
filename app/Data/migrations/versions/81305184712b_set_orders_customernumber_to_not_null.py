"""Set orders.customerNumber to not null

Revision ID: 81305184712b
Revises: ddcc8f6a0a1f
Create Date: 2020-11-18 10:51:10.173691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81305184712b'
down_revision = 'ddcc8f6a0a1f'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('orders', 'customerNumber', existing_type=sa.Integer, nullable=False)


def downgrade():
    op.alter_column('orders', 'customerNumber', existing_type=sa.Integer, nullable=True)

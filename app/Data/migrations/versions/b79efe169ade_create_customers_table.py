"""Create Customers Table

Revision ID: b79efe169ade
Revises: 
Create Date: 2020-11-18 10:02:13.915668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b79efe169ade'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'customers',
        sa.Column('customerNumber', sa.Integer, primary_key=True),
        sa.Column('customerName', sa.String(50), nullable=False),
        sa.Column('contactLastName', sa.String(50), nullable=False),
        sa.Column('contactFirstName', sa.String(50), nullable=False),
        sa.Column('phone', sa.String(50), nullable=False),
        sa.Column('addressLine1', sa.String(50), nullable=False),
        sa.Column('addressLine2', sa.String(50), nullable=True),
        sa.Column('city', sa.String(50), nullable=False),
        sa.Column('state', sa.String(50), nullable=True),
        sa.Column('postalCode', sa.String(15), nullable=True),
        sa.Column('country', sa.String(50), nullable=False)
    )


def downgrade():
    op.drop_table('customers')

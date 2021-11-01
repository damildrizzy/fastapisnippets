"""add tags model

Revision ID: 1640a8dd94d5
Revises: 
Create Date: 2021-11-01 12:45:10.020759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1640a8dd94d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('tag', sa.Column('last_transaction_date', sa.DateTime))


def downgrade():
    op.drop_column('tag', 'last_transaction_date')

"""create posts table

Revision ID: 69c4f0623556
Revises: f4c1203796c5
Create Date: 2022-03-08 22:08:14.490052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69c4f0623556'
down_revision = 'f4c1203796c5'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    op.drop_table('posts')
    pass

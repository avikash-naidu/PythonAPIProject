"""add content column

Revision ID: 225de9f94e80
Revises: 69c4f0623556
Create Date: 2022-03-09 10:21:51.939414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '225de9f94e80'
down_revision = '69c4f0623556'
branch_labels = None
depends_on = None


def upgrade():
    #op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass

"""add content column2

Revision ID: 11ea84c14363
Revises: 225de9f94e80
Create Date: 2022-03-09 10:26:42.273173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11ea84c14363'
down_revision = '225de9f94e80'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass

"""add last columns to posts

Revision ID: 24365dc631a4
Revises: 96d29987511a
Create Date: 2022-03-09 10:59:22.293339

"""
from http import server
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24365dc631a4'
down_revision = '96d29987511a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),)
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default="True"),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass

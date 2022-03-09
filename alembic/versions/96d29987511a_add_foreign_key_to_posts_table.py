"""add foreign-key to posts table

Revision ID: 96d29987511a
Revises: c1cbfae9184b
Create Date: 2022-03-09 10:53:18.814812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96d29987511a'
down_revision = 'c1cbfae9184b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fkey', source_table="posts", referent_table="users",local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass

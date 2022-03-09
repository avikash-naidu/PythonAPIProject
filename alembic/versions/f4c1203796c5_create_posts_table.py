"""create posts table

Revision ID: f4c1203796c5
Revises: 
Create Date: 2022-03-08 21:51:19.750048

"""
from ast import Try
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4c1203796c5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), primary_key=True), sa.Column('title', sa.String()))
    pass


def downgrade():
    op.drop_table('posts')
    pass

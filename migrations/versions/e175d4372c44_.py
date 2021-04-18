"""empty message

Revision ID: e175d4372c44
Revises: af49a896bafe
Create Date: 2021-04-18 01:34:04.535913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e175d4372c44'
down_revision = 'af49a896bafe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('birth', sa.String(length=120), nullable=False),
    sa.Column('gender', sa.String(length=80), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('character')
    # ### end Alembic commands ###

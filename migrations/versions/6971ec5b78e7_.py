"""empty message

Revision ID: 6971ec5b78e7
Revises: c72a188869a5
Create Date: 2021-04-29 01:19:57.898591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6971ec5b78e7'
down_revision = 'c72a188869a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idUser', sa.Integer(), nullable=True),
    sa.Column('idCharacter', sa.Integer(), nullable=True),
    sa.Column('idPlanet', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idCharacter'], ['character.id'], ),
    sa.ForeignKeyConstraint(['idPlanet'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['idUser'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite')
    # ### end Alembic commands ###
"""empty message

Revision ID: 7e80f366adf2
Revises: f97ab5cd6b1f
Create Date: 2022-06-18 22:08:57.334372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e80f366adf2'
down_revision = 'f97ab5cd6b1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('funds', sa.Column('value', sa.Float(), nullable=True))
    op.add_column('funds', sa.Column('all_deposit', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('funds', 'all_deposit')
    op.drop_column('funds', 'value')
    # ### end Alembic commands ###

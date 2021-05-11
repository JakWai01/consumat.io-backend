"""Add cache.

Revision ID: 6676c18417dc
Revises: 
Create Date: 2021-05-11 15:52:28.227351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6676c18417dc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cache',
    sa.Column('query', sa.Text(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('last_changed', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('query')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cache')
    # ### end Alembic commands ###

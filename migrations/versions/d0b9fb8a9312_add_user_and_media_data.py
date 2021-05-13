"""Add user and media_data.

Revision ID: d0b9fb8a9312
Revises: 066863c10e01
Create Date: 2021-05-12 20:10:02.391921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0b9fb8a9312'
down_revision = '066863c10e01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cache',
    sa.Column('query_content', sa.Text(), nullable=False),
    sa.Column('body_content', sa.Text(), nullable=True),
    sa.Column('last_changed', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('query_content')
    )
    op.create_table('user',
    sa.Column('user_id_content', sa.Integer(), nullable=False),
    sa.Column('external_id_content', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('user_id_content')
    )
    op.create_table('media_data',
    sa.Column('user_data_id_content', sa.Integer(), nullable=False),
    sa.Column('watch_status_content', sa.String(length=255), nullable=True),
    sa.Column('rating_content', sa.Float(), nullable=True),
    sa.Column('media_id_content', sa.Integer(), nullable=False),
    sa.Column('media_type_content', sa.String(length=30), nullable=False),
    sa.Column('user_id_content', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id_content'], ['user.user_id_content'], ),
    sa.PrimaryKeyConstraint('user_data_id_content')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('media_data')
    op.drop_table('user')
    op.drop_table('cache')
    # ### end Alembic commands ###
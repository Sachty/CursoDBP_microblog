"""empty message

Revision ID: 20f248a74d5d
Revises: 502fbce7e863
Create Date: 2022-09-19 17:59:49.275856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20f248a74d5d'
down_revision = '502fbce7e863'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('review', 'rating',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=2),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('review', 'rating',
               existing_type=sa.String(length=2),
               type_=sa.INTEGER(),
               existing_nullable=True,
               postgresql_using="rating::integer")
    # ### end Alembic commands ###

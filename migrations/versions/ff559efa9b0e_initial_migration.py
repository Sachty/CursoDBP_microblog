"""Initial migration.

Revision ID: ff559efa9b0e
Revises: 
Create Date: 2022-09-19 17:49:34.460955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff559efa9b0e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('estudiante',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('codigo', sa.String(length=8), nullable=True),
    sa.Column('nombre', sa.String(length=20), nullable=True),
    sa.Column('apellido', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_estudiante_codigo'), 'estudiante', ['codigo'], unique=True)
    op.create_index(op.f('ix_estudiante_nombre'), 'estudiante', ['nombre'], unique=True)
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=20), nullable=True),
    sa.Column('password', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('review')
    op.drop_index(op.f('ix_estudiante_nombre'), table_name='estudiante')
    op.drop_index(op.f('ix_estudiante_codigo'), table_name='estudiante')
    op.drop_table('estudiante')
    # ### end Alembic commands ###

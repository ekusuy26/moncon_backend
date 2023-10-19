"""create payment table

Revision ID: 9bc5334b3125
Revises: 3cb262d71f81
Create Date: 2023-10-19 07:22:26.987472

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '9bc5334b3125'
down_revision: Union[str, None] = '3cb262d71f81'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Integer(), nullable=True, comment='利用日'),
    sa.Column('name', sa.String(length=255), nullable=True, comment='店・商品名'),
    sa.Column('amount', sa.Integer(), nullable=True, comment='利用金額'),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_payments_id'), 'payments', ['id'], unique=False)
    op.drop_index('ix_items_description', table_name='items')
    op.drop_index('ix_items_id', table_name='items')
    op.drop_index('ix_items_title', table_name='items')
    op.drop_table('items')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('description', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('owner_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name='items_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_items_title', 'items', ['title'], unique=False)
    op.create_index('ix_items_id', 'items', ['id'], unique=False)
    op.create_index('ix_items_description', 'items', ['description'], unique=False)
    op.drop_index(op.f('ix_payments_id'), table_name='payments')
    op.drop_table('payments')
    # ### end Alembic commands ###

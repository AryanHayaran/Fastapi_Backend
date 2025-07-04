"""add review table

Revision ID: b769097b2357
Revises: 2f64833c6506
Create Date: 2025-06-14 00:43:58.317876

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b769097b2357'
down_revision: Union[str, None] = '2f64833c6506'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    op.add_column('reviews', sa.Column('rating', sa.Integer(), nullable=False))
    op.add_column('reviews', sa.Column('review_text', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('reviews', sa.Column('user_uid', sa.Uuid(), nullable=True))
    op.add_column('reviews', sa.Column('book_uid', sa.Uuid(), nullable=True))
    op.create_foreign_key(None, 'reviews', 'books', ['book_uid'], ['uid'])
    op.create_foreign_key(None, 'reviews', 'users', ['user_uid'], ['uid'])
    op.drop_column('reviews', 'last_name')
    op.drop_column('reviews', 'password_hash')
    op.drop_column('reviews', 'first_name')
    op.drop_column('reviews', 'is_verified')
    op.drop_column('reviews', 'role')
    op.drop_column('reviews', 'username')
    op.drop_column('reviews', 'email')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('reviews', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('reviews', sa.Column('role', sa.VARCHAR(), server_default=sa.text("'user'::character varying"), autoincrement=False, nullable=False))
    op.add_column('reviews', sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('reviews', sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('reviews', sa.Column('password_hash', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('reviews', sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'reviews', type_='foreignkey')
    op.drop_constraint(None, 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'book_uid')
    op.drop_column('reviews', 'user_uid')
    op.drop_column('reviews', 'review_text')
    op.drop_column('reviews', 'rating')
    op.create_table('review',
    sa.Column('uid', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('role', sa.VARCHAR(), server_default=sa.text("'user'::character varying"), autoincrement=False, nullable=False),
    sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('password_hash', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('uid', name=op.f('review_pkey'))
    )
    # ### end Alembic commands ###

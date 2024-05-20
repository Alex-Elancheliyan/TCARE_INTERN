"""empty message

Revision ID: 86ac1295ef5e
Revises: 
Create Date: 2024-04-29 11:03:57.555719

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '86ac1295ef5e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bank_deposit',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Date', sa.Date(), nullable=False),
    sa.Column('Type', sa.String(length=50), nullable=True),
    sa.Column('Amount', sa.Float(), nullable=False),
    sa.Column('Deposit_Mode', sa.String(length=50), nullable=True),
    sa.Column('Remaining_Amount', sa.Float(), nullable=False),
    sa.Column('Terminal_Id', sa.Integer(), nullable=False),
    sa.Column('Merchant_Id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('petty_cash',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Date', sa.Date(), nullable=False),
    sa.Column('Description', sa.String(length=300), nullable=False),
    sa.Column('Amount', sa.Float(), nullable=False),
    sa.Column('Balance_Amount', sa.Float(), nullable=False),
    sa.Column('Terminal_Id', sa.Integer(), nullable=False),
    sa.Column('Merchant_Id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('petty_cash')
    op.drop_table('bank_deposit')
    # ### end Alembic commands ###

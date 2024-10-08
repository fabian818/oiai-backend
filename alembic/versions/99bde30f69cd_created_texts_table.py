"""created texts table

Revision ID: 99bde30f69cd
Revises: 
Create Date: 2024-08-25 17:38:46.286463

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99bde30f69cd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('texts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_texts_content'), 'texts', ['content'], unique=False)
    op.create_index(op.f('ix_texts_id'), 'texts', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_texts_id'), table_name='texts')
    op.drop_index(op.f('ix_texts_content'), table_name='texts')
    op.drop_table('texts')
    # ### end Alembic commands ###

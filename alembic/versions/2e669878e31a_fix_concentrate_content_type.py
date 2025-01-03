"""fix concentrate content type

Revision ID: 2e669878e31a
Revises: 020026c31f66
Create Date: 2024-12-28 11:58:17.919076

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e669878e31a'
down_revision: Union[str, None] = '020026c31f66'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('concentrate', sa.Column('aluminium_content', sa.Float(), nullable=False))
    op.alter_column('concentrate', 'iron_content',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)
    op.alter_column('concentrate', 'silicon_content',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)
    op.alter_column('concentrate', 'calcium_content',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)
    op.alter_column('concentrate', 'sulfur_content',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)
    op.drop_column('concentrate', 'aluminum_content')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('concentrate', sa.Column('aluminum_content', sa.INTEGER(), autoincrement=False, nullable=False))
    op.alter_column('concentrate', 'sulfur_content',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('concentrate', 'calcium_content',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('concentrate', 'silicon_content',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('concentrate', 'iron_content',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.drop_column('concentrate', 'aluminium_content')
    # ### end Alembic commands ###

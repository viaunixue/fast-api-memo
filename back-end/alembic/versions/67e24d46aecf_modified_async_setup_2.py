"""modified async setup 2

Revision ID: 67e24d46aecf
Revises: cb17762ad94f
Create Date: 2024-06-18 18:26:58.968336

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67e24d46aecf'
down_revision: Union[str, None] = 'cb17762ad94f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

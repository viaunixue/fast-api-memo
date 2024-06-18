"""modified async setup 3

Revision ID: 40e7653b5459
Revises: 67e24d46aecf
Create Date: 2024-06-18 18:30:23.099450

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40e7653b5459'
down_revision: Union[str, None] = '67e24d46aecf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

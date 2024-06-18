"""modified async setup

Revision ID: cb17762ad94f
Revises: 40486ab26105
Create Date: 2024-06-18 18:00:23.160376

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb17762ad94f'
down_revision: Union[str, None] = '40486ab26105'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

"""update async setup

Revision ID: 40486ab26105
Revises: 82f71b778674
Create Date: 2024-06-17 20:00:25.315680

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40486ab26105'
down_revision: Union[str, None] = '82f71b778674'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

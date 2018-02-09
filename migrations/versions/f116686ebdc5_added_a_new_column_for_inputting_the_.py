"""added a new column for inputting the authors name in the pitches table

Revision ID: f116686ebdc5
Revises: b45d81571c32
Create Date: 2018-02-06 08:12:08.481879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f116686ebdc5'
down_revision = 'b45d81571c32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('author', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'author')
    # ### end Alembic commands ###
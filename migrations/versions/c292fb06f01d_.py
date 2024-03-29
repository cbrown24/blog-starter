"""empty message

Revision ID: c292fb06f01d
Revises: 
Create Date: 2020-01-19 23:10:06.959586

"""
from alembic import op
import sqlalchemy as sa
from datetime import date, datetime
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, DateTime, Boolean
from alembic import op
from sqlalchemy.sql import insert
from sqlalchemy import orm


# revision identifiers, used by Alembic.
revision = 'c292fb06f01d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('topic',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('body', sa.String(length=800), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('public_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('blog',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_by', sa.String(length=255), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('body', sa.String(length=800), nullable=True),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['topic_id'], ['topic.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    user = table('user',
        column('username', String),
        column('email', String),
        column('password_hash', String),
        column('admin', Boolean),
        column('public_id', String),
        column('registered_on', DateTime),
    )  
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    data = {
        "email": "am@foo",
        "username": "admin",
        "password_hash": "$2b$12$o2xHM5LMHk/j6YwQOEMLCuT/7j6KLULYZTtMZKeg5D8.kPfWjHm4i",
        "admin": True,
        "public_id": "admin",
        "registered_on": datetime.utcnow()
    }
    ret = session.execute(insert(user).values(data))
    session.commit()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog')
    op.drop_table('user')
    op.drop_table('topic')
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###

"""create tables

Revision ID: 8f1e7f5c5d8b
Revises:
Create Date: 2025-02-06 19:06:56.934683

"""

from alembic import op
import sqlalchemy as sa

import os

environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = "8f1e7f5c5d8b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=40), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "playlists",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("image_url", sa.String(length=2083), nullable=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "songs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("audio_url", sa.String(length=2083), nullable=False),
        sa.Column("duration", sa.Integer(), nullable=False),
        sa.Column("lyrics", sa.Text(), nullable=False),
        sa.Column("genre", sa.String(length=100), nullable=False),
        sa.Column("release_year", sa.Integer(), nullable=False),
        sa.Column("image_url", sa.String(length=2083), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "likes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("song_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["song_id"], ["songs.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "song_id", name="_user_song_uc"),
    )
    op.create_table(
        "playlist_songs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("playlist_id", sa.Integer(), nullable=False),
        sa.Column("song_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["playlist_id"], ["playlists.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["song_id"], ["songs.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )

    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE songs SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE playlists SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE playlist_songs SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE likes SET SCHEMA {SCHEMA};")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("playlist_songs")
    op.drop_table("likes")
    op.drop_table("songs")
    op.drop_table("playlists")
    op.drop_table("users")
    # ### end Alembic commands ###

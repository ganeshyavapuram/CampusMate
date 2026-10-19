"""Alembic migration environment (ADR-017). The database URL comes from core/config.py, not alembic.ini."""
from logging.config import fileConfig

from alembic import context

import db.models  # noqa: F401  (registers every table on Base.metadata)
from core.config import get_settings
from db.database import Base, engine

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata
database_url = get_settings().database_url


def run_migrations_offline() -> None:
    """Write the SQL to the screen instead of running it."""
    context.configure(
        url=database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_as_batch=True,
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations against the app's own engine, so SQLite foreign keys stay on."""
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            # SQLite can't alter columns in place; batch mode copies the table instead.
            render_as_batch=True,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

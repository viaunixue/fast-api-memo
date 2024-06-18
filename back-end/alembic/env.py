import os
from logging.config import fileConfig

from sqlalchemy.ext.asyncio import async_engine_from_config
from alembic import context
from dotenv import load_dotenv
import asyncio

load_dotenv()

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = None
# Your model's MetaData object here for 'autogenerate' support
from app.core.db import Base  # Replace with actual model
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def get_url():
    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("MYSQL_PASSWORD", "")
    server = os.getenv("MYSQL_SERVER", "db")
    port = os.getenv("MYSQL_PORT", "3306")
    db = os.getenv("MYSQL_DB", "app")
    return f"mysql+aiomysql://{user}:{password}@{server}:{port}/{db}"


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    # url = config.get_main_option("sqlalchemy.url")
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata
    )

    with context.begin_transaction():
        context.run_migrations()

async def run_async_migrations():
    configuration = config.get_section(config.config_ini_section)
    configuration['sqlalchemy.url'] = get_url()

    connectable = async_engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        future=True
    )
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    
    await connectable.dispose()

def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    asyncio.run(run_async_migrations())
    

if context.is_offline_mode():
    # asyncio.run(run_migrations_offline())
    run_migrations_offline()
else:
    # asyncio.run(run_migrations_online())
    run_migrations_online()

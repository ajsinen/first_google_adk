import asyncpg
import os

DATABASE_URL = os.getenv("DATABASE_URL")

pool: asyncpg.Pool | None = None
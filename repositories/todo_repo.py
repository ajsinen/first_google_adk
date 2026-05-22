from app.core.database import pool


async def insert_todo(title: str):

    async with pool.acquire() as conn:
        row = await conn.fetchrow(
            """
            INSERT INTO todos (title)
            VALUES ($1)
            RETURNING id, title, is_done, created_at
            """,
            title
        )

    return row

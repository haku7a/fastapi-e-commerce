from sqlmodel import SQLModel
from app.db.session import engine
from app.models.product import Product


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.books.routes import book_router
from src.auth.routes import auth_router
from src.db.main import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    await init_db()
    yield
    print("Shutting down...")

version = "v1"

app = FastAPI(
    title="Book API",
    description="A simple API to manage books",
    version=version,
    lifespan=lifespan
)

app.include_router(book_router, prefix=f"/api/{version}/books",tags=["books"])
app.include_router(auth_router, prefix=f"/api/{version}/auth",tags=["auth"])
  # Latest stable version with Python 3.13 support
from fastapi import FastAPI, status
from contextlib import asynccontextmanager

from fastapi.responses import JSONResponse
from src.books.routes import book_router
from src.auth.routes import auth_router
from src.reviews.routes import review_router
from src.db.main import init_db
from .errors import create_exception_handler, InvalidCredentials, TagAlreadyExists, BookNotFound, UserAlreadyExists, UserNotFound, InsufficientPermission, AccessTokenRequired, InvalidToken, RefreshTokenRequired, RevokedToken
from .middleware import register_middleware

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

app.add_exception_handler(
    UserAlreadyExists,
    create_exception_handler(
        status_code=403,
        initial_detail={
            "message": "User with email already exists",
            "error_code": "user_exists",
        },
    ),
)

@app.exception_handler(500)
async def internal_server_error(request, exc):
    return JSONResponse(
        content={
            "message": "Oops! Something went wrong.",
            "error_code": "internal_server_error",
        },
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


register_middleware(app)

app.include_router(book_router, prefix=f"/api/{version}/books",tags=["books"])
app.include_router(auth_router, prefix=f"/api/{version}/auth",tags=["auth"])
app.include_router(review_router, prefix=f"/api/{version}/reviews",tags=["reviews"])
  # Latest stable version with Python 3.13 support
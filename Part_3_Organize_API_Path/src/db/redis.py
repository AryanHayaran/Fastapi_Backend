from redis.asyncio import Redis
from src.config import Config

JTI_EXPIRY = 3600  # 1 hour in seconds

# Create Redis connection
token_blocklist = Redis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    db=0,
)


async def add_jti_to_blocklist(jti: str) -> None:
    await token_blocklist.set(
        name=jti,
        value="blocked",  # Must set a value (empty string not recommended)
        ex=JTI_EXPIRY  # Use 'exp' for expiry in seconds
    )


async def token_in_blocklist(jti: str) -> bool:
    exists = await token_blocklist.exists(jti)
    return exists == 1  # EXISTS returns integer 1/0
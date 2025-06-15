from fastapi import FastAPI,status
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import time
import logging
from fastapi.middleware.trustedhost import TrustedHostMiddleware

logger = logging.getLogger('uvicorn.access')
logger.disabled = True  # Disable Uvicorn's default access logging

def register_middleware(app: FastAPI):

    @app.middleware("http")
    async def custom_logging(request: Request, call_next):
        start_time = time.time()

        response = await call_next(request)
        processing_time = time.time() - start_time


        message = f"{request.method} {request.url.path} - completed after {processing_time} seconds"
        print(message)

        return response
    
    # @app.middleware("http")
    # async def authorization(request: Request, call_next):
    #    if not "Authorization" in request.headers:
    #          return JSONResponse(
    #              content={
    #                  "message": "No authorization",
    #                  "resolution": "Please provide the right credentials to proceed"
    #              },
    #              status_code=status.HTTP_401_UNAUTHORIZED
    #          )
       
    #    response = await call_next(request)

    #    return response

    app.add_middleware(
        CORSMiddleware,
        allow_origins = ["*"],
        allow_methods = ["*"],
        allow_headers = ["*"],
        allow_credentials = True,
    )

    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["*"],  # Adjust this to your needs, e.g., ["localhost", "example.com"]
    )





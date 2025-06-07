from fastapi import FastAPI
from app.utils.response import create_response
from app.utils.exception_handlers import http_exception_handler, validation_exception_handler
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

@app.get("/")
def health_check():
    return create_response(message="health check successful")

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
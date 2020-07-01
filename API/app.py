
import settings
from routers import users, sessions, authentication
from fastapi import FastAPI, APIRouter
from fastapi.openapi.utils import get_openapi

app = FastAPI(docs_url='/')
router = APIRouter()

# Add routers
app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(sessions.router)
# Set schema
def custom_openapi(openapi_prefix: str):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Lavatory Predictor API",
        version="1.0.0",
        description="This is the API for Lavatory Predictor.",
        routes=app.routes,
        openapi_prefix=openapi_prefix,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" # TODO Replace
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host=settings.SERVER_NAME, port=settings.PORT)

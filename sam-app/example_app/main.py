from fastapi import FastAPI
from mangum import Mangum

from example_app.api.api_v1.api import router as api_router
from example_app.core.config import API_V1_STR, PROJECT_NAME

app = FastAPI(
    title=PROJECT_NAME,
    # if not custom domain
    # openapi_prefix="/prod"
)


app.include_router(api_router, prefix=API_V1_STR)


@app.get("/ping")
def pong():
    """
    Sanity check.

    This will let the user know that the service is operational.

    And this path operation will:
    * show a lifesign

    """
    return {"ping": "pong!"}

@app.get("/hello-world")
def pong():
   
    return {"msg": "Hello World!"}


handler = Mangum(app, lifespan="off")

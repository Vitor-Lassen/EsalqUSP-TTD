from fastapi import FastAPI
from infra.api.routes import user_routers


app = FastAPI()
app.include_router(user_routers.router)   
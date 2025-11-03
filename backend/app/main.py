from fastapi import FastAPI

from apps.users.routes import users_router

app = FastAPI()

def get_application() -> FastAPI:
    app = FastAPI()

    app.include_router(users_router, prefix='/users', tags=['Users', "Auth"])

    return app


app = get_application()
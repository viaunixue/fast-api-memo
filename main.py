from fastapi import FastAPI, Request, Depends
from fastapi.routing import APIRoute
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.core.db import Base, engine
from app.core.config import settings
from app.api.main import api_router

def custom_generate_unique_id(route: APIRoute) -> str:
    if route.tags:
        return f"{route.tags[0]}-{route.name}"
    return route.name

app = FastAPI(
    title = settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id
)

app.add_middleware(SessionMiddleware, secret_key=settings.BACKEND_SESSION_SECRET_KEY)
Base.metadata.create_all(bind=engine)

# Set All CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

app.include_router(api_router, prefix=settings.API_V1_STR)

templates = Jinja2Templates(directory="app/templates")

# 기존 라우트 
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse('home.html', {"request": request})
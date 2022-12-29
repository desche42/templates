#!/usr/bin/env python
"""
Entry point of the API
"""
import os

from logger import init_logging
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from api.middlewares.auth import make_session_params
from api.routers.example import router as example_router

from fastapi import FastAPI

ROOT_PATH = (
    "/my-awesome-deployed-app/api" if os.getenv("ENVIRONMENT") else ""
)

# The app
app = FastAPI(title="Nuxt3+FastAPI Boilerplate", root_path=ROOT_PATH, docs_url="/")

# Initialise logger
init_logging()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex="https?:\\/\\/(localhost|127\\.0\\.0\\.1)(:\\d{1,5})?",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Required for authentication
app.add_middleware(SessionMiddleware, **make_session_params())

# Include routers
app.include_router(example_router, tags=["Example"], prefix="/example")

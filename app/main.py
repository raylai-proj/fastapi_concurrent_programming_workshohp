from fastapi import FastAPI

from app.routers import health

def create_app() -> FastAPI:
    """Create and configure the Book API application."""
    app = FastAPI(title="Book API")

    # Register health.router to app.
    app.include_router(health.router)

    return app
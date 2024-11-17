from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import logging
import sys
from fastapi.responses import JSONResponse
from api.routes.combined_routes import router
from mangum import Mangum
from fastapi.openapi.docs import get_swagger_ui_html

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="EchoBlog API",
    description="API for the EchoBlog application",
    version="1.0.0",
    docs_url=None,  # Disable default docs URL
    redoc_url=None  # Disable redoc URL
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom Swagger UI route
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="EchoBlog API Documentation",
        swagger_favicon_url="/favicon.ico"
    )

# Global error handler
@app.middleware("http")
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        logger.error(f"Global error: {str(e)}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={"detail": f"Internal server error: {str(e)}"}
        )

# Include the combined router
app.include_router(router)

@app.get("/")
async def root():
    try:
        logger.info("Root endpoint called")
        return {
            "message": "Welcome to EchoBlog API",
            "documentation": "/docs",
            "health_check": "/health"
        }
    except Exception as e:
        logger.error(f"Error in root endpoint: {str(e)}", exc_info=True)
        raise

@app.get("/health")
async def health_check():
    try:
        return {
            "status": "healthy",
            "python_version": sys.version,
            "fastapi_status": "ok"
        }
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}", exc_info=True)
        raise

# Handler for AWS Lambda
handler = Mangum(app) 
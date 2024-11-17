from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from api.routes.combined_routes import router
import logging
import sys
from fastapi.responses import JSONResponse

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
        return {"message": "Welcome to EchoBlog API"}
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

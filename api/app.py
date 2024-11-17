from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import auth, blog, user, comment, test

app = FastAPI(
    title="EchoBlog API",
    description="Backend API for EchoBlog",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(blog.router, prefix="/blogs", tags=["blogs"])
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(comment.router, prefix="/comments", tags=["comments"])
app.include_router(test.router, tags=["test"])

@app.get("/", tags=["root"])
async def root():
    return {
        "message": "Welcome to EchoBlog API",
        "version": "1.0.0",
        "status": "active"
    }

@app.get("/health", tags=["health"])
async def health():
    return {
        "status": "healthy",
        "api": "running"
    } 
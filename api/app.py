from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from api.routes import auth, blog, user, comment, test

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers directly (without combined_routes)
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(blog.router, prefix="/blogs", tags=["blogs"])
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(comment.router, prefix="/comments", tags=["comments"])
app.include_router(test.router, tags=["test"])

@app.get("/")
async def root():
    return {"message": "Welcome to EchoBlog API"}

@app.get("/health")
async def health():
    return {"status": "ok"}

# Create handler for AWS Lambda / Vercel
handler = Mangum(app) 
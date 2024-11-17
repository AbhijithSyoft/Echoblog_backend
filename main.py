from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import auth, blog, user, comment
import uvicorn

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(comment.router)

@app.get("/")
async def root():
    return {"message": "Welcome to EchoBlog API"}

# Remove this if deploying to Vercel
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.combined_routes import router

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the combined router
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to EchoBlog API"}

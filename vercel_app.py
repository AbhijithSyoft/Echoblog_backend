from api.index import app

# This is for local development
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("vercel_app:app", host="0.0.0.0", port=8000, reload=True) 
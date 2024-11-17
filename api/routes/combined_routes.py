from fastapi import APIRouter
from api.routes import auth, blog, user, comment

# Create a single combined router
router = APIRouter()

# Include all routes under the combined router
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(blog.router, prefix="/blogs", tags=["blogs"])
router.include_router(user.router, prefix="/users", tags=["users"])
router.include_router(comment.router, prefix="/comments", tags=["comments"]) 
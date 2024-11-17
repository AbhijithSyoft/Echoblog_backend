import logging
from mangum import Mangum
from api.app import app

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create handler for AWS Lambda / Vercel
try:
    handler = Mangum(app, lifespan="off")
    logger.info("Mangum handler initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize Mangum handler: {str(e)}")
    raise 
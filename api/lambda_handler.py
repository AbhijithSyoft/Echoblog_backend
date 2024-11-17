from mangum import Mangum
from api.app import app

# Create handler for AWS Lambda / Vercel
handler = Mangum(app, lifespan="off") 
import os
import logging
import serverless_wsgi
from main import app

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Configure static files path for Netlify environment
app.static_folder = os.path.join(os.path.dirname(__file__), "..", "..", "static")

def handler(event, context):
    """
    Handle incoming requests to the Flask app in a serverless context
    using serverless-wsgi adapter.
    """
    logger.info(f"Received request for path: {event.get('path', '/')}")
    logger.info(f"HTTP method: {event.get('httpMethod', 'GET')}")
    logger.info(f"Query parameters: {event.get('queryStringParameters', {})}")

    if event.get("path", "").startswith("/static/"):
        # Let Netlify handle static files directly
        logger.info("Redirecting static file request to Netlify CDN")
        return {
            "statusCode": 301,
            "headers": {
                "Location": event["path"]
            },
            "body": ""
        }

    return serverless_wsgi.handle_request(app, event, context)
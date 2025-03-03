import os
import serverless_wsgi
from main import app

# Configure static files path for Netlify environment
app.static_folder = os.path.join(os.getcwd(), "static")

def handler(event, context):
    """
    Handle incoming requests to the Flask app in a serverless context
    using serverless-wsgi adapter.
    """
    if event.get("path", "").startswith("/static/"):
        # Let Netlify handle static files directly
        return {
            "statusCode": 404,
            "body": "Static file not found"
        }
    return serverless_wsgi.handle_request(app, event, context)
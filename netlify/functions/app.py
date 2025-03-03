import serverless_wsgi
from main import app

def handler(event, context):
    """
    Handle incoming requests to the Flask app in a serverless context
    using serverless-wsgi adapter.
    """
    return serverless_wsgi.handle_request(app, event, context)
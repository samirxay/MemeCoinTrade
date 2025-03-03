from flask import Flask
from flask.logging import create_logger
import logging
from handler import app as flask_app

def handler(event, context):
    """Handle incoming requests to the Flask app in a serverless context."""
    try:
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        logger = create_logger(flask_app)
        
        # Get the path and method from the event
        path = event.get('path', '/')
        http_method = event.get('httpMethod', 'GET')
        
        # Convert the event to WSGI format
        environ = {
            'PATH_INFO': path,
            'REQUEST_METHOD': http_method,
            'SERVER_NAME': 'netlify',
            'SERVER_PORT': '443',
            'wsgi.url_scheme': 'https',
            'wsgi.input': event.get('body', ''),
            'QUERY_STRING': event.get('queryStringParameters', {}),
        }
        
        # Handle the request
        response = flask_app(environ)
        
        return {
            'statusCode': response.status_code,
            'body': response.get_data(as_text=True),
            'headers': dict(response.headers)
        }
        
    except Exception as e:
        logger.error(f"Error handling request: {str(e)}")
        return {
            'statusCode': 500,
            'body': 'Internal Server Error',
            'headers': {'Content-Type': 'text/plain'}
        }

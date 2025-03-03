# Meme Traders Forum

A lightweight memecoin discussion forum with a dark/purple theme. Built with Flask for easy deployment on both Replit and Netlify.

## Features
- News section for memecoin updates
- Forum for community discussions
- File attachments (images/videos) support
- Dark/purple theme
- Mobile-responsive design
- No complex dependencies - just pure Python!

## Deployment Options

### Option 1: Deploy on Replit (Recommended for Beginners)
1. Go to [Replit](https://replit.com)
2. Click "Create Repl"
3. Choose "Import from GitHub"
4. Paste your GitHub repository URL
5. Click "Import from GitHub"
6. Once imported, click the "Run" button
7. Your forum is now live at your Replit URL!

### Option 2: Deploy on Netlify
1. Fork this repository to your GitHub account
2. Log in to [Netlify](https://netlify.com)
3. Click "New site from Git"
4. Choose your forked repository
5. Leave the default settings as they are - the netlify.toml file handles all configuration
6. Click "Deploy site"

Note: The application uses Netlify Functions to run the Flask app, and static files (CSS, JS, images) are served directly by Netlify for better performance. All routing is handled automatically through the netlify.toml configuration.

## Development Setup
1. Clone the repository
2. Make sure you have Python 3.11+ installed
3. Install dependencies:
   ```bash
   pip install flask flask-sqlalchemy gunicorn email-validator psycopg2-binary serverless-wsgi
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Project Structure
```
├── netlify/
│   └── functions/        # Netlify serverless functions
├── static/              # Static assets (CSS, JS)
├── templates/           # HTML templates
├── main.py             # Main application file
├── netlify.toml        # Netlify configuration
└── README.md           # This file
```

## How It Works
- **Replit Deployment**: Uses Python's Flask server directly, perfect for development and small to medium projects.
- **Netlify Deployment**: Uses serverless functions to handle Flask routes, with static files served directly by Netlify's CDN. The netlify.toml file handles all routing configuration automatically.

## Contributing
1. Fork the repository
2. Create your feature branch
3. Make your changes
4. Test thoroughly on both Replit and Netlify
5. Create a pull request

## Support
If you need help deploying or developing:
- For Replit issues: Create an issue in the GitHub repository
- For Netlify issues: Check [Netlify Support](https://docs.netlify.com/)

## License
MIT License - Feel free to use this project however you like!
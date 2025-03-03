from flask import Flask, render_template, request, redirect, url_for
import logging
import os
from datetime import datetime
from dataclasses import dataclass
from typing import List, Dict
import base64

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev_secret_key")

@dataclass
class Post:
    id: int
    title: str
    content: str
    timestamp: datetime
    author: str
    attachments: List[Dict]
    category: str

# In-memory storage
posts = []
post_counter = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    news_posts = [post for post in posts if post.category == 'news']
    return render_template('news.html', posts=news_posts)

@app.route('/forum', methods=['GET', 'POST'])
def forum():
    global post_counter
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author', 'Anonymous')
        category = request.form.get('category', 'general')
        
        attachments = []
        if 'file' in request.files:
            file = request.files['file']
            if file:
                file_data = base64.b64encode(file.read()).decode('utf-8')
                attachments.append({
                    'type': 'image' if file.content_type.startswith('image') else 'video',
                    'data': file_data
                })

        new_post = Post(
            id=post_counter,
            title=title,
            content=content,
            timestamp=datetime.now(),
            author=author,
            attachments=attachments,
            category=category
        )
        posts.append(new_post)
        post_counter += 1
        return redirect(url_for('forum'))

    forum_posts = [post for post in posts if post.category == 'general']
    return render_template('forum.html', posts=forum_posts)

@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    search_results = [
        post for post in posts
        if query in post.title.lower() or query in post.content.lower()
    ]
    return render_template('forum.html', posts=search_results, search=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

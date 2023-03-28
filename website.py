import os
import glob
from flask import Flask, render_template, url_for
from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)

CONTENT_DIR = 'content'

def get_posts():
    post_files = glob.glob(f"{CONTENT_DIR}/*/*.md")
    posts = []
    for post_file in post_files:
        with open(post_file) as f:
            content = f.read()
            title = os.path.basename(post_file[:-3])
            category = os.path.basename(os.path.dirname(post_file))
            posts.append({'title': title, 'category': category, 'content': content})
    return posts

@app.route('/')
def home():
    posts = get_posts()
    return render_template('index.html', posts=posts)

@app.route('/post/<category>/<title>')
def post(category, title):
    posts = get_posts()
    post = next((post for post in posts if post['title'] == title and post['category'] == category), None)
    if post:
        return render_template('post.html', post=post)
    else:
        return render_template('404.html'), 404

@app.route('/category/<category>')
def category(category):
    posts = get_posts()
    category_posts = [post for post in posts if post['category'] == category]
    if category_posts:
        return render_template('category.html', category=category, posts=category_posts)
    else:
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

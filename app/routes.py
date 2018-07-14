from flask import render_template, request, redirect, url_for
from app import app
from . models import User, Post, db
import datetime

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Doggo'}
	# posts = Post.query.all()
	posts = {}
	return render_template('index.html', title="Home", user=user, posts=posts)


@app.route('/boot_test')
def boot_test():
	return render_template('boot_test.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    author = request.form['author']
    date_posted = request.form['date_posted']
    content = request.form['content']

    post = Post(title=title, author=author, date_posted=datetime.Now(), content=content)

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))
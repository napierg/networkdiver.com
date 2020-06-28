from flask import Flask, render_template
from flask_frozen import Freezer
from flask_flatpages import FlatPages
import sys

DEBUG = False
FREEZER_DESTINATION = "docs"
FREEZER_DESTINATION_IGNORE = ["CNAME","404.html"]
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ['.html', '.md']
FLATPAGES_ROOT = 'content'
CORP_POST_DIR = 'corp_posts'
app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)


# Root of the Site /
@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template('index.html')


# About the Site /
@app.route("/about")
@app.route("/about.html")
def about():
    return render_template('FrontPages/about.html')


# Consultancy /
@app.route("/consultancy")
@app.route("/consultancy.html")
def consultancy():
    return render_template('FrontPages/consultancy.html')


# Services /
@app.route("/services")
@app.route("/services.html")
def services():
    return render_template('FrontPages/services.html')


# Main content - Dynamic to the pages
@app.route('/content/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    return render_template('content.html', page=page)


# Corporate Blog
@app.route('/c-blog/')
def posts():
    posts = [p for p in pages if p.path.startswith(CORP_POST_DIR)]
    return render_template('Bits/CompanyBlog.html', posts=posts)


# posts links
@app.route('/c-blog/<name>/')
def post(name):
    path = '{}/{}'.format(CORP_POST_DIR, name)
    post = pages.get_or_404(path)
    return render_template('Bits/CompanyBlog.html', post=post)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        app.debug = True
        freezer.freeze()
    else:
        app.debug = True
        app.run(port=8000)
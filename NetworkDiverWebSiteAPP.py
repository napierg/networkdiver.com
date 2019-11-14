from flask import Flask, render_template
from flask_frozen import Freezer
import sys

DEBUG = False
FREEZER_DESTINATION = "docs"
FREEZER_DESTINATION_IGNORE = ["CNAME","404.html"]


app = Flask(__name__)
app.config.from_object(__name__)
freezer = Freezer(app)


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        app.debug = True
        freezer.freeze()
    else:
        app.debug = True
        app.run(port=8000)


from flask import Flask, send_from_directory
import random

app = Flask(__name__)

# Path for our main Svelte page


@app.route("/")
def base():
    return send_from_directory('../frontend/src', 'app.html')

# Path for all the static files (compiled JS/CSS, etc.)


@app.route("/<path:path>")
def home(path):
    return send_from_directory('../frontend/static', path)

'''
TODO
1. routing to get ML embedding
2. patient info loading


'''


if __name__ == "__main__":
    app.run(debug=True)

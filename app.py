from flask import Flask

# create Flask instance (app)
app = Flask(__name__)

# Create Flask route for home

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/free_world')
def free_world():
    return 'Fuck "Free World" 3-1-3'
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
# def index():
#     return "<h1>Hello World!</h1>"

def index():
    first_name = 'john'
    return render_template('index.html')

# filters:
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags

@app.route('/user/<name>')
def user(name):
    return  render_template('user.html',name=name)

# Create Custom ErrorPages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500

from flask import Flask, render_template
from jinja2.utils import markupsafe

mainapp = Flask(__name__)

@mainapp.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    mainapp.run(debug=True,port=3000,host='0.0.0.0')

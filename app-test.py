activate_this = '/var/www/flask/a/venv/bin/activate_this.py'

#with open(activate_this) as file_:
with open(activate_this) as file:
   exec(file.read(), dict(__file__=activate_this))

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') 
def hello_world():
   return 'Hello world from Flask!' 


@app.route('/hello') 
def hello():
   return render_template('home.html')


@app.route('/html') 
def index():
   return render_template('index.html')

#if __name__ == '__main__':
#      app.run()

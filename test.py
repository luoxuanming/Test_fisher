from flask import Flask
__author__ = 'July'

app = Flask(__name__)
@app.route('/hello')
def hello():
  return "1234"

app.run()  
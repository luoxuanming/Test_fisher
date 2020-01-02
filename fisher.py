'''
Created by luo on 2019/12/11
'''

from flask import Flask, make_response
from helper import is_ibsn_or_key
__author__ = 'July'

app = Flask(__name__)
app.config.from_object('config')
# print(app.config['DEBUG'])



@app.route('/book/search/<q>/<page>')
def search(q, page):
  '''
  q:普通关键字或isbn
  page: 页数   
  isbn 13个0-9的数字组成，含有一些'-'
  '''
  is_ibsn_or_key = is_ibsn_or_key(q)
  
  pass

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=app.config['DEBUG'], port=81)
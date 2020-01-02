'''
Created by luo on 2019/12/11
'''

from flask import Flask, make_response
__author__ = 'July'

app = Flask(__name__)
app.config.from_object('config')
# print(app.config['DEBUG'])

@app.route('/hello')
def hello():
  # 视图函数会返回 status code 200, 404, 301
  # content-type http headers  content-type告诉接收方如何解析放回的内容 
  # 默认值 context-type = text/html 这时服务器告诉浏览器要以html的格式来解析返回的文本
  # reSponse对象  flask的make_response()函数可以帮我们创建response对象
  headers = {
    'content-type': 'text/json'
  }

  response.headers = headers
  # return '<html></html>',301, headers

  response = make_response('<html></html>', 200)
  return response

def helloo():
  return 'Hello, QiYue'

# 基于类的视图（即插视图）
# app.add_url_rule('/hello', view_func=hello)

if __name__ == '__main__':
  # 如果加了这个判断，下面的语句只在入口文件里执行，如果fisher.py不是作为入口文件的话，而是被其他模块导入的，下面的app.run是不会执行的
  # 生产环境下是不会使用flask自带启动服务启动项目的 
  # 生产环境： nginx + uwsgi   nginx作为前置服务器用来接收我们浏览器发来的请求然后把请求转发给uwsgi, uwsgi加载fisher.py这个模块启动flask相关的代码
  # 生产环境下不会启动flask自带的服务器
  app.run(host='0.0.0.0',debug=app.config['DEBUG'], port=81)
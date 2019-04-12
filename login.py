#!/usr/bin/python
#coding:utf-8
import tornado.ioloop
import tornado.web
from tornado import web,gen,httpclient
import requests
import json
class loginHandler(tornado.web.RequestHandler):
    def post(self):
        username=self.get_argument('j_username')
        password=self.get_argument('j_password')
        url='http://192.168.27.102:8080/j_acegi_security_check'
	data={'j_username':username,'j_password':password,"from":"/","Submit":"Sign+in"}
        headers={
        'Referer':'http://192.168.27.102:8080/'}
        s = requests.session()
        response=s.post(url,headers = headers,data=data)
        c=requests.cookies.RequestsCookieJar()
        s.cookies.update(c)
        print s.cookies.get_dict()
        for key in s.cookies.get_dict():
		self.set_cookie(key,s.cookies.get_dict()[key])
        self.redirect('http://192.168.27.102:8080/项目地址')
def make_app():
    return tornado.web.Application([
        (r"/", loginHandler),
    ])
if __name__ == "__main__":
    app = make_app()
    app.listen(666)
    tornado.ioloop.IOLoop.current().start()

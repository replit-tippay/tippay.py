import base64
import requests
import os
from flask import request

class instance:
  def __init__(self,app):
    self.products = {}
    self.app = app
    @app.route('/_tippay/check', methods=['POST'])
    def check():
      if request.json['item'] and request.json['price']:
        if self.products[request.json['item']] and self.products[request.json['item']]['price'] == request.json['price']:
          return f"{self.products[request.json['item']]['redirect']}|||{os.environ['REPL_ID']}"
        else:
            return '404', 404
      else:
          return '400', 400

    @app.route('/_tippay/complete/<username>/<token>/<item>', methods=['GET'])
    def complete(username, token, item):
      r = requests.get(f'https://tippay.repl.co/verify/{token}')
      if r.status_code == 200:
        self.products[item]['callback'](username)
      return 'Yas'

  def product(self,name, price, redirect, callback):
    self.products[name] = {
        'price': price,
        'callback': callback,
        'redirect': redirect
    }

    return {
        'name': name,
        'price': price
    }

  def url(self,data):
    based = base64.b64encode(f"{os.environ['REPL_OWNER']}|{os.environ['REPL_SLUG']}|{data['name']}|{data['price']}".encode('utf-8')).decode('utf-8')
    return f'https://tippay.repl.co/pay/{based}'
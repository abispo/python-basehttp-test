#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from functools import reduce

from api.users import UsersAPI

class MyRequestHandler(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        self.user_api = UsersAPI()
        super().__init__(*args, **kwargs)
 
    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type','application/json')
        self.end_headers()

        if self.path[-1:] == '/':
            self.path = self.path[:-1]

        url = self.path.split("/")

        message = json.dumps({'message': 'users api'})

        if len(url) >= 2 and len(url) < 4:
            
            cpf = None
            if len(url) == 3:
                cpf = url[2]

            try:
                message = json.dumps(getattr(self.user_api, url[1])(cpf))

            except AttributeError:
                message = json.dumps({'error': 'No such path'})

        self.wfile.write(bytes(message, "utf8"))        
        return
 
def run():
    print('Starting server...')
 
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print('Server running!')
    httpd.serve_forever()
 
if __name__ == '__main__':
    run()
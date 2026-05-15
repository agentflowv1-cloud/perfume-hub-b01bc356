import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_parts = urlparse(self.path)
        if url_parts.path == '/fragrance':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            fragrance_details = {
                'name': 'Example Fragrance',
                'ingredients': ['ingredient1', 'ingredient2'],
                'notes': ['top note', 'middle note', 'base note'],
                'suggested_application': 'apply to wrist'
            }
            self.wfile.write(json.dumps(fragrance_details).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not found')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Received post request')

port = int(os.environ.get('PORT', 8080))
server_address = ('', port)
httpd = HTTPServer(server_address, RequestHandler)
print('Listening on port %d' % port)
httpd.serve_forever()
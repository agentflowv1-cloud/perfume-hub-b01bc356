import os
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class PerfumeCatalog:
    def __init__(self):
        self.perfumes = [
            {'title': 'Perfume 1', 'rating': 4.5, 'image': 'https://example.com/perfume1.jpg', 'link': 'https://example.com/perfume1'},
            {'title': 'Perfume 2', 'rating': 4.8, 'image': 'https://example.com/perfume2.jpg', 'link': 'https://example.com/perfume2'}
        ]

    def get_perfumes(self):
        return self.perfumes

    def add_perfume(self, title, rating, image, link):
        self.perfumes.append({'title': title, 'rating': rating, 'image': image, 'link': link})

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        catalog = PerfumeCatalog()
        perfumes = catalog.get_perfumes()
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(perfumes).encode())

    def do_POST(self):
        catalog = PerfumeCatalog()
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        perfume_data = json.loads(body)
        catalog.add_perfume(perfume_data['title'], perfume_data['rating'], perfume_data['image'], perfume_data['link'])
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(catalog.get_perfumes()).encode())

port = int(os.environ.get('PORT', 8080))
server_address = ('', port)
httpd = HTTPServer(server_address, RequestHandler)
print('Server started on port', port)
httpd.serve_forever()
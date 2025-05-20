import sys
from http.server import SimpleHTTPRequestHandler
import socketserver
import json
import query
sys.path.append("autocomplite")
from autocomplite.autocomplite import fill_trie

class Engine():
    def __init__(self):
        self.tree = fill_trie()
    
    def start(self):
        PORT = 8080
        Handler = CORSRequestHandler

        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("Server running on port", PORT)
            httpd.serve_forever()
            
class CORSRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.tree = fill_trie()
        super().__init__(*args, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_POST(self):
        if self.path == '/admin':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode())
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            query.add_page(data.get('content'))
            response_data = {'status': 'success', 'message': data.get('content')}
            response_json = json.dumps(response_data)
            self.wfile.write(response_json.encode())

        if self.path == '/templates':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode())
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response_data = {'status': 'success', 'message': data.get('content')}
            words_ind = query.get_words_indexes(response_data.get('message'))
            query_res = query.get_words_links(words_ind)
            query_json = json.dumps(query_res)
            self.wfile.write(query_json.encode())
        
        if self.path == '/search':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode())
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            res = self.tree.autocomplite(data.get('content'))
            print(res)
            json_data = json.dumps(res)
            self.wfile.write(json_data.encode())



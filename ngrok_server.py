import http.server
import socketserver
import ssl

PORT = 8000

# Load the certificate and private key
certfile = r'C:\Users\userTK427\Desktop\Studying\Python\PROJECTS\EbayBot\cert.pem'
keyfile = r'C:\\Users\\userTK427\\Desktop\\Studying\\Python\\PROJECTS\\EbayBot\\key.pem'

class AccountDeletionHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the request body
        content_length = int(self.headers['Content-Length'])
        request_body = self.rfile.read(content_length)

        # Process the request body (e.g. parse the JSON payload)
        # ...

        # Send a response to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'OK')

# Set up the web server
httpd = socketserver.TCPServer(("", PORT), AccountDeletionHandler)

# Wrap the HTTP server in an SSL context
httpd.socket = ssl.wrap_socket(httpd.socket, certfile=certfile, keyfile=keyfile, server_side=True)

print(f'Listening on port {PORT}...')
httpd.serve_forever()
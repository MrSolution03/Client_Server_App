import http.server
import socketserver
import threading

PORT = 8080

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"GET request received")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"POST request received with data: " + post_data)

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"PUT request received with data: " + put_data)

    def do_DELETE(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"DELETE request received")

def run_server():
    global httpd
    with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

def listen_for_shutdown_command():
    while True:
        command = input()
        if command.lower() == 'q':
            print("Shutdown command received. Stopping server...")
            httpd.shutdown()
            break

if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

    listen_for_shutdown_command()
    server_thread.join()

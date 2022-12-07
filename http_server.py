import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def header(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _resp_content(self, msg):
        self.wfile.write(bytes("<html><head><title>http server demo</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes(f"<p>{msg}</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_GET(self):
        self.header()
        self._resp_content("get")

    def do_POST(self):
        self.header()
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        print(post_body)
        self._resp_content(post_body)

    def do_PUT(self):
        self.header()
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        print(post_body)
        self._resp_content(post_body)


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

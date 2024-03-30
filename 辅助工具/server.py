from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class DanmakuHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        danmaku_data = post_data.decode('utf-8-sig')
        print("Received Danmaku Data:", danmaku_data)

        # 保存到本地文本文件
        with open('danmaku_data.txt', 'a') as file:
            file.write(danmaku_data + '\n')

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Danmaku data received and saved successfully!')

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, DanmakuHandler)
    print('Danmaku Server is running on port', port)
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
""" Module http.server and socketserver"""
import http.server
import socketserver

PORT = 8000

""" Class TestMe """
class TestMe():
    """ Method take_five """
    def take_five(self):
        return 4

    """ Method port """
    def port(self):
        return PORT


if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port: ", PORT)
        http.serve_forever()

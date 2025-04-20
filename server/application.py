""" Module http.server and socketserver"""
import http.server
import socketserver

PORT = 8000

class TestMe():
    """ Class TestMe() """
    def take_five(self):
        """ Method take_five() """
        return 5

    def port(self):
        """ Method port() """
        return PORT


if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port: ", PORT)
        http.serve_forever()

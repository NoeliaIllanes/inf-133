from http.server import HTTPServer, SimpleHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    try:
        server_address = ('', 8000)
        httpd = server_class(server_address, handler_class)
        print('Iniciando servidor web en http://localhost:8000/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando servidor web')
        httpd.socket.close()

if _name_ == '_main_':
    run()
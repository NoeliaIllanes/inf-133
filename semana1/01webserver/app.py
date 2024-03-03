from http.server import HTTPServer, SimpleHTTPRequestHandler

def run (server_class=HTTPServer, handler_class= SimpleHTTPRequestHandler):
    try:
        server_adress  = ("", 8000)
        httpd = server_class(server_adress , handler_class)
        print('iniciando servidor web en https://localhost:8000')

        httpd.serve_forever()
    except KeyboardInterrupt:
        print('apagando servicio web')
        httpd.socket.close()

if __name__ == "__main__":
    run()

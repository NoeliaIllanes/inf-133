from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def suma_dos_numeros(num1, num2):
    return num1 + num2

def cadena_palindromo(cadena):
    
    cadena = cadena.replace(" ", "").lower()
    
    return cadena == cadena[::-1]

dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    soap_prefix="soap12",
)

dispatcher.register_function(suma_dos_numeros, "suma_dos_numeros")
dispatcher.register_function(cadena_palindromo, "cadena_palindromo")


server = HTTPServer(("localhost", 8000), SOAPHandler)
server.dispatcher = dispatcher

print("Servidor SOAP iniciado en http://localhost:8000")
server.serve_forever()

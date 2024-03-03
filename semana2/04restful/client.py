import requests

url = "http://localhost:8000/"

# GET obtener todas las carreras
ruta_get_carreras = url + "carreras"
get_carreras_response = requests.request(method="GET", url=ruta_get_carreras)
print("Carreras:", get_carreras_response.text)

# GET obtener a todos los estudiantes de Economía
ruta_get_estudiantes_economia = url + "estudiantes_economia"
get_estudiantes_economia_response = requests.request(method="GET", url=ruta_get_estudiantes_economia)
print("Estudiantes de Economía:", get_estudiantes_economia_response.text)

# Agregar 2 estudiantes de Economía
ruta_post = url + "estudiantes"
nuevos_estudiantes = [
    {"nombre": "María", "apellido": "López", "carrera": "Economía"},
    {"nombre": "Carlos", "apellido": "Gómez", "carrera": "Economía"}
]

for estudiante in nuevos_estudiantes:
    post_response = requests.request(method="POST", url=ruta_post, json=estudiante)
    print("Nuevo estudiante:", post_response.text)

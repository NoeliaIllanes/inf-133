import requests

# Consultando a un servidor RESTful
base_url = "http://localhost:8000/estudiantes"

# GET obtener a todos los estudiantes
get_response = requests.get(base_url)
print(get_response.text)

# POST agrega un nuevo estudiante
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
post_response = requests.post(base_url, json=nuevo_estudiante)
print(post_response.text)

# DELETE elimina todos los estudiantes
delete_response = requests.delete(base_url)
print(delete_response.text)

# Agregando otro estudiante
nuevo_estudiante2 = {
    "nombre": "Pedrito",
    "apellido": "Lopez",
    "carrera": "Ingeniería",
}
post_response = requests.post(base_url, json=nuevo_estudiante2)
print(post_response.text)

# GET busca a un estudiante por id
get_by_id_response = requests.get(base_url + "/1")
print(get_by_id_response.text)

# PUT actualiza un estudiante
estudiante_actualizado = {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
put_response = requests.put(base_url, json=estudiante_actualizado)
print(put_response.text)

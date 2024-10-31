import requests  # Importa la biblioteca requests para realizar solicitudes HTTP.

class APIHandler:  # Define una clase llamada APIHandler.
    def __init__(self, url):  # Método inicializador que se ejecuta al crear una instancia de la clase.
        self.url = url  # Guarda la URL proporcionada en un atributo de la instancia.

    def fetch_data(self):  # Define un método para obtener datos de la API.
        try:
            response = requests.get(self.url)  # Realiza una solicitud GET a la URL guardada.
            response.raise_for_status()  # Verifica si la respuesta es exitosa (código 200); lanza un error si no.
            return response.json()  # Si la respuesta es correcta, convierte el contenido JSON en un objeto Python y lo devuelve.
        except requests.exceptions.RequestException as e:  # Captura cualquier excepción relacionada con la solicitud.
            print(f"Error al obtener datos: {e}")  # Muestra un mensaje de error si ocurre un problema.
            return []  # Devuelve una lista vacía si hay un error al obtener los datos.

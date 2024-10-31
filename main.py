from api_handler import APIHandler  #Importa la clase APIHandler del módulo api_handler
from data_displayer import DataDisplayer  #Importa la clase DataDisplayer del módulo data_displayer

def main():  # Define la función principal
    url = "https://671be4272c842d92c381a5ab.mockapi.io/test"  #Define la URL de la API que se utilizará
    api_handler = APIHandler(url)  #Crea una instancia de APIHandler, pasando la URL como argumento
    displayer = DataDisplayer(api_handler)  #Crea una instancia de DataDisplayer, pasando la instancia de APIHandler
    displayer.run()  #Llama al método run de DataDisplayer para iniciar la aplicación

if __name__ == "__main__":  #Verifica si este script se está ejecutando como el programa principal
    main()  #Llama a la función main para iniciar la ejecución

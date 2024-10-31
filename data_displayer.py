import tkinter as tk  # Importa la biblioteca principal de Tkinter
from record_table import RecordTable  # Importa la clase para mostrar la tabla de registros
from input_frame import InputFrame  # Importa la clase para el marco de entrada
from api_handler import APIHandler  # Importa el manejador de API

class DataDisplayer:  # Clase para gestionar la interfaz y mostrar datos
    def __init__(self, api_handler):  #Inicializador de la clase
        self.api_handler = api_handler  #Almacena el manejador de API
        self.root = tk.Tk()  #Crea la ventana principal
        self.root.title("Aplicación de Registros")  #Establece el título de la ventana
        self.root.resizable(False, False)  #Desactiva el cambio de tamaño de la ventana
        self.setup_ui()  #Configura la interfaz de usuario

    def setup_ui(self):  # Método para configurar la interfaz
        self.table = RecordTable(self.root)  #Crea la tabla de registros
        self.table.pack(padx=20, pady=20)  #Ajusta el espacio alrededor de la tabla

        #Crea el marco de entrada y vincula funciones para mostrar registros
        self.input_frame = InputFrame(self.root, self.show_selected_record, self.show_all_records, self.refresh_records)
        self.input_frame.frame.pack(pady=10)  #Ajusta el espacio alrededor del marco de entrada

        self.show_all_records()  #Muestra todos los registros al iniciar

    def show_selected_record(self):  # Muestra el registro seleccionado por ID
        try:
            selected_id = int(self.input_frame.get_id())  #Obtiene el ID ingresado
            #Filtra y muestra el registro correspondiente
            self.table.insert_data(
                [record for record in self.fetch_data() if int(record["Id"]) == selected_id])
        except ValueError:  #Maneja el caso de un ID no válido
            print("Ingrese un ID válido")

    def show_all_records(self):  #Muestra todos los registros
        self.table.insert_data(self.fetch_data())  #Inserta los datos obtenidos en la tabla

    def fetch_data(self):  #Método para obtener datos de la API
        return self.api_handler.fetch_data()  #Llama al método de API para obtener datos

    def refresh_records(self):  #Refresca los registros en la tabla
        self.show_all_records()  #Vuelve a mostrar todos los registros

    def run(self):  #Método para ejecutar la aplicación
        self.root.mainloop()  #Inicia el bucle principal de la interfaz

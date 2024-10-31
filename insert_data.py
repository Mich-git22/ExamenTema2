import tkinter as tk  #Importa la biblioteca principal de Tkinter
from tkinter import ttk  #Importa ttk para usar widgets mejorados

class RecordTable(tk.Frame):  #Clase para la tabla de registros
    def __init__(self, master):  #Inicializador de la clase
        super().__init__(master)  #Llama al inicializador de la clase base Frame
        self.frame = tk.Frame(master)  #Crea un nuevo marco dentro del master
        self.frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)  #Ajusta el marco para que ocupe espacio

        #Crear la tabla con columnas específicas
        self.table = ttk.Treeview(self.frame, columns=("mensajeId", "nombre", "lugarOrigen", "motivoMensaje", "Id"), show="headings", height=10)

        # Definir encabezados de la tabla y centrarlos
        for col in ("mensajeId", "nombre", "lugarOrigen", "motivoMensaje", "Id"):
            self.table.heading(col, text=col.capitalize(), anchor="center")  #Establece el texto del encabezado
            self.table.column(col, anchor="center", width=120)  #Configura el ancho de cada columna

        # Configurar la barra de desplazamiento vertical
        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.table.yview)  # Crea la barra de desplazamiento
        self.table.configure(yscroll=self.scrollbar.set)  #Asocia la barra de desplazamiento a la tabla

        #Usar grid para organizar la tabla y la barra de desplazamiento
        self.table.grid(row=0, column=0, sticky='nsew')  #Coloca la tabla
        self.scrollbar.grid(row=0, column=1, sticky='ns')  #Coloca la barra de desplazamiento

        # Configurar la expansión de la tabla
        self.frame.grid_columnconfigure(0, weight=1)  #Permite que la columna de la tabla se expanda
        self.frame.grid_rowconfigure(0, weight=1)     #Permite que la fila de la tabla se expanda

    def insert_data(self, data):  # Método para insertar datos en la tabla
        self.table.delete(*self.table.get_children())  #Borra los datos existentes en la tabla
        for record in data:  #Itera sobre cada registro de datos
            self.table.insert("", "end", values=(  #Inserta un nuevo registro en la tabla
                record.get("mensajeId", "N/A"),  #Obtiene el mensajeId, usa "N/A" si no existe
                record.get("nombre", "N/A"),  #Obtiene el nombre
                record.get("lugarOrigen", "N/A"),  #Obtiene el lugar de origen
                record.get("motivoMensaje", "N/A"),  #Obtiene el motivo del mensaje
                record.get("Id", "N/A")  #Obtiene el Id
            ))

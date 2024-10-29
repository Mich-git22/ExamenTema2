# data_displayer.py
import tkinter as tk

class DataDisplayer:
    def __init__(self, data):
        self.data = data
        self.index = 0  # Índice para rastrear el registro actual

    def display_data(self):
        # Crear la ventana principal de Tkinter
        self.root = tk.Tk()
        self.root.title("Registros de Datos")

        # Contador de registros
        total_records = len(self.data)
        self.record_label = tk.Label(self.root, text=f"Total de registros: {total_records}")
        self.record_label.pack(pady=10)

        # Label para mostrar el contenido del registro actual
        self.record_text = tk.StringVar()
        self.record_label_content = tk.Label(self.root, textvariable=self.record_text, anchor="w", justify="left")
        self.record_label_content.pack(padx=20, pady=10)

        # Botones de navegación
        self.prev_button = tk.Button(self.root, text="Anterior", command=self.show_previous, state="disabled")
        self.prev_button.pack(side="left", padx=20, pady=20)

        self.next_button = tk.Button(self.root, text="Siguiente", command=self.show_next)
        self.next_button.pack(side="right", padx=20, pady=20)

        # Muestra el primer registro
        self.update_record_display()

        # Ejecutar la ventana de Tkinter
        self.root.mainloop()

    def update_record_display(self):
        # Obtener el registro actual y actualizar el contenido en pantalla
        record = self.data[self.index]
        text = (
            f"Registro {self.index + 1}:\n\n"
            f"Mensaje ID: {record.get('mensajeId', 'N/A')}\n"
            f"Nombre: {record.get('nombre', 'N/A')}\n"
            f"Lugar de Origen: {record.get('lugarOrigen', 'N/A')}\n"
            f"Motivo del Mensaje: {record.get('motivoMensaje', 'N/A')}\n"
            f"ID: {self.index + 1}\n"
        )
        self.record_text.set(text)

        # Actualizar el estado de los botones
        self.prev_button["state"] = "normal" if self.index > 0 else "disabled"
        self.next_button["state"] = "normal" if self.index < len(self.data) - 1 else "disabled"

    def show_previous(self):
        if self.index > 0:
            self.index -= 1
            self.update_record_display()

    def show_next(self):
        if self.index < len(self.data) - 1:
            self.index += 1
            self.update_record_display()

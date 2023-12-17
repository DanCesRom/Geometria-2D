import tkinter as tk
from tkinter import ttk
import math

class Figura2DApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Figuras 2D App")

        self.figuras = ["Circulo", "Cuadrado", "Rectangulo", "Pentagono"]
        self.colores = ["Rojo", "Verde", "Azul", "Amarillo"]

        self.figura_seleccionada = tk.StringVar()
        self.color_seleccionado = tk.StringVar()

        self.canvas = tk.Canvas(self.root, width=300, height=300, bg="white")
        self.canvas.grid(row=3, column=0, columnspan=2, pady=10)

        self.traduccion_colores = {
            "Rojo": "red",
            "Verde": "green",
            "Azul": "blue",
            "Amarillo": "yellow"
        }

        self.create_widgets()

        # Agregar mensaje de creador
        creador_label = tk.Label(self.root, text="By Daniel Cespedes 22-0390", anchor="se", foreground="gray")
        creador_label.grid(row=5, column=1, pady=(0, 5), sticky="se", columnspan=2)

    def create_widgets(self):
        figura_label = ttk.Label(self.root, text="Selecciona una figura:")
        figura_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        figura_combobox = ttk.Combobox(self.root, textvariable=self.figura_seleccionada, values=self.figuras)
        figura_combobox.grid(row=0, column=1, padx=10, pady=10)

        color_label = ttk.Label(self.root, text="Selecciona un color:")
        color_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        color_combobox = ttk.Combobox(self.root, textvariable=self.color_seleccionado, values=self.colores)
        color_combobox.grid(row=1, column=1, padx=10, pady=10)

        crear_figura_button = ttk.Button(self.root, text="Crear Figura", command=self.crear_figura)
        crear_figura_button.grid(row=2, column=0, columnspan=2, pady=20)

        borrar_figura_button = ttk.Button(self.root, text="Borrar Figura", command=self.borrar_figura)
        borrar_figura_button.grid(row=4, column=0, columnspan=2, pady=20)

    def crear_figura(self):
        figura = self.figura_seleccionada.get()
        color = self.color_seleccionado.get()

        # Convertir el nombre del color a inglés usando el diccionario de traducción
        color_ingles = self.traduccion_colores.get(color, color)

        self.canvas.delete("all")  # Limpiar el canvas antes de dibujar una nueva figura

        if figura == "Circulo":
            self.dibujar_circulo(color_ingles)
        elif figura == "Cuadrado":
            self.dibujar_cuadrado(color_ingles)
        elif figura == "Rectangulo":
            self.dibujar_rectangulo(color_ingles)
        elif figura == "Pentagono":
            self.dibujar_pentagono(color_ingles)

    def dibujar_circulo(self, color):
        x, y, radio = 150, 150, 50
        self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill=color)

    def dibujar_cuadrado(self, color):
        lado = 100
        self.canvas.create_rectangle(100, 100, 100 + lado, 100 + lado, fill=color)

    def dibujar_rectangulo(self, color):
        ancho, alto = 120, 80
        self.canvas.create_rectangle(90, 110, 90 + ancho, 110 + alto, fill=color)

    def dibujar_pentagono(self, color):
        x, y, longitud = 150, 150, 50

        # Coordenadas para dibujar una estrella de cinco puntas
        puntos_pentagono = []
        for i in range(5):
            angulo = math.radians(72 * i - 90)
            x_i = x + longitud * math.cos(angulo)
            y_i = y + longitud * math.sin(angulo)
            puntos_pentagono.extend([x_i, y_i])

        # Unir los puntos para formar la estrella
        self.canvas.create_polygon(puntos_pentagono, fill=color)

    def borrar_figura(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    root = tk.Tk()
    app = Figura2DApp(root)
    root.mainloop()

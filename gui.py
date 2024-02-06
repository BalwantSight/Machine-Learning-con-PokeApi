import tkinter as tk
from tkinter import ttk
from sklearn.ensemble import RandomForestClassifier
import joblib
from PIL import Image, ImageTk

# Cargar el modelo entrenado
model = joblib.load('pokemon_model.joblib')


def predecir_tipo(atributos):
    tipo_predicho = model.predict([atributos])
    return tipo_predicho[0]


def predecir_tipo_gui():
    exp_base = float(entry_exp_base.get())
    altura = float(entry_altura.get())
    peso = float(entry_peso.get())

    atributos = [exp_base, altura, peso]
    tipo_predicho = predecir_tipo(atributos)

    label_resultado.config(text=f"Tipo predicho: {tipo_predicho}")


# Crear la interfaz gráfica
root = tk.Tk()
root.title("Predicción de Tipo de Pokemon")

# Crear etiquetas y campos de entrada
label_exp_base = ttk.Label(root, text="Experiencia Base:")
entry_exp_base = ttk.Entry(root)

label_altura = ttk.Label(root, text="Altura:")
entry_altura = ttk.Entry(root)

label_peso = ttk.Label(root, text="Peso:")
entry_peso = ttk.Entry(root)

# Botón para realizar la predicción
button_prediccion = ttk.Button(
    root, text="Realizar Predicción", command=predecir_tipo_gui)

# Etiqueta para mostrar el resultado
label_resultado = ttk.Label(root, text="Tipo predicho: ")

# Etiqueta para mostrar el título de la imagen
label_descripcion = ttk.Label(root, text="Scatter Plot de Atributos")

# Cargar la figura de dispersión
scatter_image = ImageTk.PhotoImage(Image.open('scatter_plot.png'))
scatter_label = ttk.Label(root, image=scatter_image)
scatter_label.image = scatter_image

# Diseño de la interfaz
label_exp_base.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_exp_base.grid(row=0, column=1, padx=10, pady=5)

label_altura.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_altura.grid(row=1, column=1, padx=10, pady=5)

label_peso.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entry_peso.grid(row=2, column=1, padx=10, pady=5)

button_prediccion.grid(row=3, column=0, columnspan=2, pady=10)

label_resultado.grid(row=4, column=0, columnspan=2)

# Mostrar el título de la imagen
label_descripcion.grid(row=5, column=0, columnspan=2, pady=5)

# Centrar la imagen más abajo
scatter_label.grid(row=6, column=0, columnspan=2, pady=10)

# Ejecutar la interfaz gráfica
root.mainloop()
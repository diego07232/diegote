# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pVbjjMlsVT6LDGv55LSgdaYjkmX2xDZk
"""

import matplotlib.pyplot as plt
import numpy as np

# Crear el corazón con ecuaciones paramétricas
t = np.linspace(0, 2 * np.pi, 100)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Crear la figura
plt.figure(figsize=(6,6))
plt.plot(x, y, 'r', linewidth=3)  # Dibuja el corazón en rojo
plt.fill(x, y, 'red', alpha=0.6)  # Rellena el corazón con color rojo

# Agregar el texto "Te quiero"
plt.text(0, -2, 'Te quiero', fontsize=20, fontweight='bold', color='white',
         ha='center', va='center', bbox=dict(facecolor='red', edgecolor='none', boxstyle='round,pad=0.5'))

# Quitar ejes
plt.axis("off")

# Mostrar la imagen
plt.show()
import matplotlib.pyplot as plt

# Datos
tiempo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # en minutos
interaccion = [2,2,5,6,8,9,9,9,10,10]  # contacto visual

# Crear la gráfica
plt.figure(figsize=(12, 10))
plt.plot(tiempo, interaccion, marker='o', linestyle='-', color='red', label='Atencion Vs Tiempo')

# Personalización
plt.title('Atencion en el Tiempo (Mantener contecto visual)')
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Nivel de Atencion')
plt.ylim(0, 12)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Mostrar gráfica
plt.show()

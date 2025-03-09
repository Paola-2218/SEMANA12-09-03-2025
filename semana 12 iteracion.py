import random

# Definir dimensiones
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Número de semanas a considerar

# Generar la matriz 3D con temperaturas aleatorias entre 10 y 30 grados
matriz_temperaturas = [[[random.uniform(10, 30) for _ in dias] for _ in range(semanas)] for _ in ciudades]

# Calcular y mostrar promedios semanales por ciudad
for i, ciudad in enumerate(ciudades):
    print(f"Temperaturas promedio en {ciudad} por semana:")
    for semana in range(semanas):
        promedio_semana = sum(matriz_temperaturas[i][semana]) / len(dias)
        print(f"  Semana {semana + 1}: {promedio_semana:.2f}°C")
    print()
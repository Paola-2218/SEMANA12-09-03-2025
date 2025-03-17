import random


# cambios

def calcular_temperatura_promedio(datos_temperaturas):
    """
    Calcular la temperatura promedio de cada ciudad por semana.

    :param datos_temperaturas: Diccionario con ciudades como claves y listas de listas de temperaturas semanales como valores.
    :return: Diccionario con ciudades como claves y listas de temperaturas promedio semanales como valores.
    """
    promedios = {}
    for ciudad, semanas in datos_temperaturas.items():
        promedios[ciudad] = [sum(semana) / len(semana) for semana in semanas]
    return promedios


# Definir dimensiones
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Número de semanas a considerar

# Generar la matriz 3D con temperaturas aleatorias entre 10 y 30 grados
datos_temperaturas = {
    ciudad: [[random.uniform(10, 30) for _ in dias] for _ in range(semanas)]
    for ciudad in ciudades
}

# Calcular y mostrar promedios semanales por ciudad
resultados = calcular_temperatura_promedio(datos_temperaturas)

for ciudad, promedios in resultados.items():
    print(f"Temperaturas promedio en {ciudad} por semana:")
    for semana, promedio in enumerate(promedios, start=1):
        print(f"  Semana {semana}: {promedio:.2f}°C")
    print()
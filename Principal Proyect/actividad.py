from typing import Tuple
from collections import Counter
#aqui creamos la calse DatosMeteorologicos
class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]: #aqui indicamos que el metodo devuelve una tupla de cinco valores, los primeros cuatro valores son de tipo float y el ultimo que es la lista es tipo str
        temperatura_total = 0
        humedad_total = 0
        presion_total = 0
        velocidad_viento_total = 0
        direccion_viento = []

        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                if linea.startswith('Temperatura:'):
                    temperatura = float(linea.split(':')[1])
                    temperatura_total += temperatura
                elif linea.startswith('Humedad:'):
                    humedad = float(linea.split(':')[1])
                    humedad_total += humedad
                elif linea.startswith('Presión:'):
                    presion = float(linea.split(':')[1])
                    presion_total += presion
                elif linea.startswith('Viento:'):
                    velocidad_viento, direccion = linea.split(':')[1].split(',')
                    velocidad_viento_total += float(velocidad_viento)
                    direccion_viento.append(direccion.strip())

        temperatura_promedio = temperatura_total / len(direccion_viento)
        humedad_promedio = humedad_total / len(direccion_viento)
        presion_promedio = presion_total / len(direccion_viento)
        velocidad_promedio_viento = velocidad_viento_total / len(direccion_viento)
        direccion_predominante_viento = Counter(direccion_viento).most_common(1)[0][0]

        return (temperatura_promedio, humedad_promedio, presion_promedio, velocidad_promedio_viento, direccion_predominante_viento)

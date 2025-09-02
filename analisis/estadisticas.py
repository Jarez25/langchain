import csv
import os

CSV_FILE = "detecciones.csv"

# Crear CSV con cabecera si no existe
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "objeto", "genero", "edad", "imagen"])


def registrar_deteccion(timestamp, objeto, genero, edad, imagen_path):
    """
    Registra cada detección en el archivo CSV.
    """
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, objeto, genero, edad, imagen_path])

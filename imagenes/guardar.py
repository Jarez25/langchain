import cv2
import os
from datetime import datetime

OUTPUT_DIR = "capturas_personas"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def guardar_foto(frame, genero="desconocido"):
    """
    Guarda la imagen con un nombre que incluye el género.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(OUTPUT_DIR, f"{genero}_{timestamp}.jpg")
    cv2.imwrite(filename, frame)
    print(f"[+] Foto guardada: {filename}")
    return filename

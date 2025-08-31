# config/config.py
import os

# Ruta base del proyecto (carpeta raíz)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Modelo YOLO (archivo afuera de /config)
MODEL_PATH = os.path.join(BASE_DIR, "yolov8m.pt")

LLM_MODEL = "deepseek-r1:latest"

CAM_WIDTH = 1280
CAM_HEIGHT = 720
CAM_FPS = 30

CONF_THRESHOLD = 0.5
IOU_THRESHOLD = 0.5
LLM_COOLDOWN = 5  # segundos


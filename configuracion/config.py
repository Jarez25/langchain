# config/config.py
import os

# Ruta base del proyecto (carpeta raíz)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Modelo YOLO (archivo afuera de /config)
MODEL_PATH = os.path.join(BASE_DIR, "yolov8m.pt")
# nota podemos usar incluso yolov8n.pt para un modelo más ligero
# o u yolov8x.pt para un modelo más pesado y preciso

# LLM_MODEL = "gpt-oss:20b" # modelo LLM pc trabajo local
LLM_MODEL = "deepseeek-r1:lastest"  # modelo LLM pc casa

CAM_WIDTH = 1280
CAM_HEIGHT = 720
CAM_FPS = 30

CONF_THRESHOLD = 0.5
IOU_THRESHOLD = 0.5
LLM_COOLDOWN = 5  # segundos

from ultralytics import YOLO
from configuracion.config import MODEL_PATH, CONF_THRESHOLD, IOU_THRESHOLD

model = YOLO(MODEL_PATH)

def detectar(frame):
    results = model(frame, conf=CONF_THRESHOLD, iou=IOU_THRESHOLD)
    return results

def extraer_labels(results, min_conf=0.6):
    labels = []
    for box in results[0].boxes:
        if box.conf[0] > min_conf:
            cls = int(box.cls[0])
            label = model.names[cls]
            if label not in labels:
                labels.append(label)
    return labels

import cv2
from detection.camara import init_camera
from detection.image_utils import mejorar_calidad_imagen
from detection.yolo_detector import detectar, extraer_labels
from llm.processor import enviar_detecciones

def main():
    cap = init_camera()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_mejorado = mejorar_calidad_imagen(frame)
        frame_procesamiento = cv2.resize(frame_mejorado, (640, 480))

        results = detectar(frame_procesamiento)
        labels = extraer_labels(results)

        annotated_frame = results[0].plot()
        annotated_frame = cv2.resize(annotated_frame, (1280, 720))

        cv2.imshow("Detecciones YOLO + LLM", annotated_frame)

        enviar_detecciones(labels)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC para salir
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

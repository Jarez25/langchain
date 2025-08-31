import cv2

def mejorar_calidad_imagen(frame, alpha=1.2, beta=10):
    """Ajusta brillo/contraste y reduce ruido"""
    frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
    frame = cv2.GaussianBlur(frame, (3, 3), 0)
    return frame

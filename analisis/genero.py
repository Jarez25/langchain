from deepface import DeepFace


def predecir_genero(frame, save_path=None):
    """
    Predice el género y edad de una persona en un frame (imagen).
    """
    try:
        result = DeepFace.analyze(
            frame, actions=["gender", "age"], enforce_detection=False)
        genero = result[0]["dominant_gender"]
        edad = result[0]["age"]

        # Normalizar salida
        if genero.lower() in ["man", "male"]:
            genero = "hombre"
        elif genero.lower() in ["woman", "female"]:
            genero = "mujer"
        else:
            genero = "desconocido"

        return genero, edad
    except Exception as e:
        print(f"Error predicción género: {e}")
        return "desconocido", None

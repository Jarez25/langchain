from langchain_ollama import ChatOllama
from langchain.schema import HumanMessage, SystemMessage

# Inicializar el modelo Ollama
llm = ChatOllama(model="deepseek-r1:latest")

def preguntar(pregunta):
    mensaje = [
        SystemMessage(content="Eres un asistente útil y amable."),
        HumanMessage(content=pregunta)
    ]
    respuesta = llm.invoke(mensaje)
    return respuesta.content

if __name__ == "__main__":
    while True:
        entrada = input("Pregunta: ")
        if entrada.lower() in ["salir", "exit", "quit"]:
            break
        respuesta = preguntar(entrada)
        print(f"Asistente: {respuesta}\n")

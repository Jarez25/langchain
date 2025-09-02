# llm/processor.py - versión mejorada
import time
import threading
from collections import deque
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from configuracion.config import LLM_MODEL, LLM_COOLDOWN

llm = ChatOllama(model=LLM_MODEL, temperature=0.7)

prompt = PromptTemplate(
    input_variables=["detecciones"],
    template="""
Eres un asistente que interpreta escenas visuales. 
Basado en estas detecciones: {detecciones}

Genera una descripción concisa y natural (2-3 oraciones máximo) de lo que se ve en la escena.
Sé descriptivo pero evita listar objetos. Ejemplo: "Parece una habitación con una persona usando su celular cerca de una mesa" en lugar de "Persona, celular, mesa".
"""
)

last_llm_call = 0
detection_history = deque(maxlen=5)
llm_thread_pool = []


def procesar_llm(detecciones):
    try:
        if not detecciones or detecciones == "":
            return

        final_prompt = prompt.format(detecciones=detecciones)
        respuesta = llm.invoke(final_prompt)
        print("\n🤖 Resumen IA:", respuesta.content)
        print("─" * 50)
    except Exception as e:
        print(f"Error en LLM: {e}")


def enviar_detecciones(labels):
    global last_llm_call, llm_thread_pool

    if not labels:
        print("No se detectaron objetos")
        return

    current_time = time.time()
    detecciones_str = ", ".join(labels)
    print(f"📷 Detectado: {detecciones_str}")

    if current_time - last_llm_call > LLM_COOLDOWN:
        detection_history.append(detecciones_str)
        contexto = "; ".join(list(detection_history)[-3:])

        # Limpiar threads terminados
        llm_thread_pool = [t for t in llm_thread_pool if t.is_alive()]

        if len(llm_thread_pool) < 2:
            thread = threading.Thread(target=procesar_llm, args=(contexto,))
            thread.daemon = True
            thread.start()
            llm_thread_pool.append(thread)
            last_llm_call = current_time

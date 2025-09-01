import time
import threading
from collections import deque
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from configuracion.config import LLM_MODEL, LLM_COOLDOWN

llm = ChatOllama(model=LLM_MODEL)

prompt = PromptTemplate(
    input_variables=["detecciones"],
    template="""
Eres un asistente que interpreta escenas. 
Con las siguientes detecciones de YOLO:
{detecciones}
Genera un resumen breve y amigable (máximo 2 oraciones).
"""
)

last_llm_call = 0
detection_history = deque(maxlen=10)
llm_thread_pool = []


def procesar_llm(detecciones):
    try:
        final_prompt = prompt.format(detecciones=detecciones)
        respuesta = llm.invoke(final_prompt)
        print(" Resumen IA:", respuesta.content)
    except Exception as e:
        print(f"Error en LLM: {e}")


def enviar_detecciones(labels):
    global last_llm_call, llm_thread_pool

    if not labels:
        return

    current_time = time.time()
    if current_time - last_llm_call > LLM_COOLDOWN:
        detecciones = ", ".join(labels)
        detection_history.append(detecciones)
        contexto = "; ".join(list(detection_history)[-3:])

        if len(llm_thread_pool) < 2:
            thread = threading.Thread(target=procesar_llm, args=(contexto,))
            thread.daemon = True
            thread.start()
            llm_thread_pool.append(thread)
            last_llm_call = current_time

        llm_thread_pool = [t for t in llm_thread_pool if t.is_alive()]

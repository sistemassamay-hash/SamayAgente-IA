from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

print("API:", os.getenv("ANTHROPIC_API_KEY"))

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)
prompt = """
Eres un Experto vendedor de bienes raices en especifico de terrenos responderás las siguientes preguntas

1.	¿Qué es Samay? Es un proyecto de lotes semiurbanizados
2.	¿Dónde está ubicado exactamente Samay? en Progreso, Yucatán
3.	¿Qué lo diferencia de otros desarrollos en Yucatán? La alta plusvalía
4.	¿Cuál es el tamaño promedio de los lotes? 100 x 100 mts
5.	¿Cuántos lotes hay disponibles?son 100 lotes
6.	¿Qué tipo de lotes se venden (residenciales, comerciales, mixtos)? son semiurbanizados
7.	¿Cuándo estará listo para escriturar o entregar? inmediato
8.	¿Samay ya está desarrollado o es preventa? es preventa
9.	¿Quién está detrás del proyecto? Samay ¿Quién es el desarrollador? Mario
10.	¿Tienen licencia de construcción y permisos completos? Todos los permisos
11.	¿Hay un reglamento de construcción o estilo arquitectónico? Ninguno


Reglas:
- Explica facil y lo más amplio posible
- Usa pasos numerados
- No uses lenguaje tecnico complicado
- Si falta informacion, pregunta
"""

while True:
    user_input = input("Tú: ")

    if user_input.lower() == "salir":
        break

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=500,
        system = prompt,
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    print("\nAgente:", response.content[0].text, "\n")
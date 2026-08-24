from dotenv import load_dotenv
import os

from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class GeminiService:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.chat = self.client.chats.create(
            model="gemini-3.5-flash-lite"
        )

    def generate_cards(self, content: str) -> str:
        prompt = f""""
                Você é um especialista em criação de flashcards para estudo.

                Analise a nota abaixo e crie flashcards úteis para revisão.

                REGRAS:
                
                - Use SOMENTE informações presentes na nota.
                - Não invente informações.
                - Priorize conceitos importantes.
                - Evite perguntas triviais.
                - Varie os tipos de pergunta.
                - Crie perguntas que exijam compreensão, não apenas memorização.
                - Gere entre 10 e 20 cards, dependendo da quantidade de conteúdo.

                FORMATO DE RETORNO:

                {{
                    "discipline": str,
                    "cards": [
                        {{
                            "front": str,
                            "back": str,
                            "discipline": str,
                            "topic": str,
                        }}, ...
                    ]
                }}

                Retorne APENAS o JSON válido.
                Não use blocos de código Markdown.
                Não inclua ```json ou ``` na resposta.

                DADOS:

                Disciplina: teste
                Tópico: teste

                Nota:

                {content}
            """

        response = self.chat.send_message(prompt)
        
        return response.text

import os

from dotenv import load_dotenv
from google import genai
from google.genai import errors
from tenacity import (
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


class GeminiService:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = "gemini-3.1-flash-lite"

    @staticmethod
    def is_retryable(exception: Exception) -> bool:
        return isinstance(exception, errors.ServerError)

    # tenta gerar conteúdo até 5 vezes com espera exponencial entre as tentativas
    @retry(
        retry=retry_if_exception(is_retryable),
        stop=stop_after_attempt(5),
        wait=wait_exponential(
            multiplier=1,
            min=2,
            max=30,
        ),
    )
    def generate_content(self, prompt: str, contents: list) -> str:
        response = self.client.models.generate_content(
            model=self.model, contents=[prompt] + contents
        )
        return response.text

    def generate_cards(self, content: str) -> str:
        prompt = f"""
                Você é um especialista em criação de flashcards para estudo.

                Analise a nota abaixo e crie flashcards úteis para revisão.

                REGRAS:
                
                - Use SOMENTE informações presentes na nota.
                - Não invente informações.
                - Priorize conceitos importantes.
                - Evite perguntas triviais.
                - Varie os tipos de pergunta.
                - Crie perguntas que exijam compreensão, não apenas memorização.
                - A quantidade deve ser proporcional à quantidade e à densidade de conteúdo relevante.
                - Nunca utilize aspas duplas dentro de strings, apenas aspas simples.
                - Para fórmulas e termos matemáticos em LaTex, use apenas \\( formula \\)
                - Não utilize caracteres matemáticos ou fórmulas Unicode (\\uXXX...), use LaTex

                FORMATO DE RETORNO:

                {{
                "discipline": "Nome da Disciplina",
                "cards": [
                    {{
                    "front": "Pergunta do card",
                    "back": "Resposta do card",
                    "discipline": "Nome da Disciplina",
                    "topic": "Tópico da Matéria"
                    }}
                ]
                }}

                Retorne APENAS o JSON válido.
                Não inclua ```json ou ``` na resposta.

                DADOS:

                Disciplina: teste
                Tópico: teste

                Nota:

                {content}
            """

        return self.generate_content(prompt=prompt, contents=[])

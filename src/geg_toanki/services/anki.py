from typing import Any

from geg_toanki.models import Card

import requests
import subprocess
import time

from dotenv import load_dotenv
import os

load_dotenv()

class AnkiService():
    def __init__(self):
        self.anki_connect_url = os.getenv("ANKI_CONNECT_URL")

    # confere se o servidor esta rodando
    def _is_running(self) -> bool:
        try:
            response = requests.post(
                self.anki_connect_url,
                json={"action": "version", "version": 6},
                timeout= 2,
            )

            data = response.json()
            return response.status_code == 200 and data["error"] == None
        except requests.exceptions.RequestException:
            return False

    # inicia a execução do anki
    def _start(self) -> None:
        subprocess.Popen(["open", "-a", "Anki"])

    # garante que o anki esteja rodando
    def ensure_running(self):
        if self._is_running():
            return

        self._start()

        for _ in range(5):
            time.sleep(1)
            if self._is_running():
                return 

        raise RuntimeError("Não foi possível conectar ao AnkiConnect.")

    # tranforma lista de Cards em note
    def card_to_anki_note(self, deck_name: str, cards: list[Card]) -> list[dict[str, Any]]:
        notes = [
            {
                "deckName": deck_name,
                "modelName": "Basic",
                "fields": {
                    "front": card.front,
                    "back": card.back,
                },
                "tags": [
                    card.discipline,
                    card.topic
                ]
            }
            for card in cards
        ]

        return notes

    # adiciona cartões ao anki
    def add_cards(self, deck_name: str, cards: list[Card]) -> list[int | None]:
        notes = self.card_to_anki_note(deck_name, cards)

        response = requests.post(
            self.anki_connect_url,
            json={
                "action": "addNotes",
                "version": 6,
                "params": {
                    "notes": notes,
                },
            },
        )

        response.raise_for_status()
        data = response.json()

        if data["error"]:
            raise RuntimeError(data["error"])
        return data["result"]

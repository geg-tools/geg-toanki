import json
from dataclasses import dataclass

from .utils import clean_json_string


@dataclass
class Card:
    front: str
    back: str
    discipline: str
    topic: str


# recebe um JSON e retorna uma lista de objetos Card
def cards_from_json(json_str: str) -> list[Card]:
    json_str = clean_json_string(json_str)
    # print("JSON:", json_str)  # Adicione esta linha para depuração
    data = json.loads(json_str)
    cards_data = data["cards"]

    return [
        Card(
            front=card["front"],
            back=card["back"],
            discipline=card["discipline"],
            topic=card["topic"],
        )
        for card in cards_data
    ]

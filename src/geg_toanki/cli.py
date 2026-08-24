import typer

from geg_toanki.file_type import detect_file_type
from geg_toanki.parser.text import parse_text

from geg_toanki.services.llm import GeminiService
from geg_toanki.services.anki import AnkiService

from geg_toanki.models import Card, cards_from_json

app = typer.Typer()

# comando CLI para criação de decks
@app.command()
def create(
    file_path: str,
    deck_name: str = typer.Option(..., "-deck=", "-d"),
):
    file_type = detect_file_type(file_path)

    # extrai o texto do arquivo
    if file_type in (".txt", ".md"):
        text = parse_text(file_path)
    elif file_type in (".pdf"):
        print("chamando pdf")
    else:
        raise typer.BadParameter(
            f"Tipo de arquivo não suportado: {file_type}"
        )

    print ("Texto extraído...")

    # llm
    gemini_service = GeminiService()
    response = gemini_service.generate_cards(content=text)

    print("Questões criadas...")

    # cards
    cards = cards_from_json(response)

    # manda para o anki
    anki_service = AnkiService()
    anki_service.ensure_running()

    print("Anki ativo...")

    anki_service.add_cards(deck_name="teste", cards=cards)

    print("Processo concluído.")

app()
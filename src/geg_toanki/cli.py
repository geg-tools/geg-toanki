import shutil
from pathlib import Path

import typer
from geg_tomd import convert_to_md

from geg_toanki.models import cards_from_json
from geg_toanki.services.anki import AnkiService
from geg_toanki.services.llm import GeminiService

app = typer.Typer()


# comando CLI para criação de decks
@app.command()
def create(
    input_path_str: str,
    deck: str = typer.Option(..., "--deck", "-d", help="Nome do deck no Anki"),
    subdecks: bool = typer.Option(
        None,
        "--subdecks",
        "-s",
        help="Gera subdecks, filhos do deck principal, gerados de acordo com a estrutura de diretórios",
    ),
    generate_md: str = typer.Option(
        None,
        "--generate-md",
        "-m",
        help="Gera arquivos intermediários em Markdown no diretório indicado",
    ),
    raw: bool = typer.Option(
        None, "--raw", "-r", help="Processa o material diretamente sem gerar resumos"
    ),
    ai_summarize: bool = typer.Option(
        None, "--ai-summary", "-a", help="Gerar resumo do arquivo com I.A."
    ),
):
    if not raw:
        if generate_md:
            # cria diretório de saída se não existir
            output_path = Path(generate_md)
            output_path.mkdir(parents=True, exist_ok=True)
        else:
            # cria diretório temporário para arquivos intermediários
            output_path = Path("./.geg/toanki/temp")
            output_path.mkdir(parents=True, exist_ok=True)

        # converte arquivos para Markdown
        convert_to_md(
            file_path_str=input_path_str,
            output_path_str=str(output_path),
            summarize=True,
            complete=True,
            use_ai=ai_summarize,
        )
    else:
        output_path = Path(input_path_str)
        print(
            "Processando arquivos diretamente de:",
            [f for f in output_path.rglob("*.md")],
        )

    print("Arquivos convertidos para Markdown...")

    # itera sobre arquivos de .geg/toanki
    anki_service = AnkiService()
    anki_service.ensure_running()

    gemini_service = GeminiService()

    for md_file in output_path.glob("**/*.md"):
        print(f"Processando arquivo: {md_file}")
        with open(md_file, "r", encoding="utf-8") as f:
            text = f.read()

        # cria os cartões anki
        cards_json = gemini_service.generate_cards(content=text)
        cards = cards_from_json(json_str=cards_json)

        if subdecks:
            # pega o caminho até o arquivo para montar o deck
            folders = md_file.relative_to(output_path).parent
            deck_name = "::".join([deck, *folders.parts])
        else:
            deck_name = deck

        print("DECK NAME: ", deck_name)

        anki_service.add_cards(deck_name=deck_name, cards=cards)
        print("adicionado")

    # move temporarios para /processed
    # mudar apenas para output_path para depois poder guardar histórico em .geg/anki
    if not raw and not generate_md:
        shutil.rmtree(".geg/toanki")


app()

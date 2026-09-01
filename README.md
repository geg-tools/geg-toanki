<p align="center">
    <img src="./docs/banner.png" alt="geg-toanki Banner" width="200">
</p>

<h1 align="center">geg-toanki</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-0062AF?style=for-the-badge&logo=python&logoColor=f6f6f6" />
  <img src="https://img.shields.io/badge/Gemini-0062AF?style=for-the-badge&logo=googlegemini&logoColor=f6f6f6" />
  <img src="https://img.shields.io/badge/Typer-0062AF?style=for-the-badge&logo=python&logoColor=f6f6f6" />
  <img src="https://img.shields.io/badge/uv-0062AF?style=for-the-badge&logo=uv&logoColor=f6f6f6" />
</p>

<p align="center">
  Ferramenta CLI para transformar materiais em Markdown em flashcards e enviá-los diretamente para o Anki, com suporte a geração automática de cartões por IA.
</p>

## Funcionalidades

- [x] Suporte a arquivos `.pdf`, `.txt` e `.md`
- [x] Conversão de entrada para Markdown via `geg-tomd`
- [x] Geração automática de flashcards com Gemini
- [x] Criação de decks e subdecks no Anki
- [x] Envio de cartões via AnkiConnect
- [x] Organização dos cartões por estrutura de diretórios

## Próximas funcionalidades

- [ ] **Validação dos flashcards** — filtrar respostas vagas, duplicadas ou incompletas.
- [ ] **Divisão em chunks** — processar conteúdos grandes em partes menores antes da geração.
- [ ] **Preview no terminal** — visualizar cards antes de enviar ao Anki.
- [ ] **Exportação para `.apkg`** — gerar pacotes de deck diretamente.
- [ ] **Tags e personalização** — adicionar tags e configurações por disciplina/tópico.
- [ ] **Tratamento de erros e logs** — melhorar diagnósticos e mensagens de falha.
- [ ] **Testes automatizados** — cobrir parser, geração e integração com o Anki.

## Pré-requisitos

Antes de usar o projeto, confirme que você tenha:

- Python 3.14+
- `uv` instalado
- Anki instalado localmente
- AnkiConnect em execução
- Chave da API Gemini configurada em `GEMINI_API_KEY`

A aplicação também depende do pacote local `geg-tomd`, que é adicionado automaticamente no `pyproject.toml`.

## Instalação

```bash
git clone https://github.com/gabrielescorelguerra/geg-toanki.git
cd geg-toanki

uv sync
```

Configure as variáveis de ambiente antes de executar a CLI:

```bash
export GEMINI_API_KEY="sua_chave_api"
export ANKI_CONNECT_URL="http://localhost:8765"
```

## Uso

### Ver ajuda

```bash
uv run geg-toanki --help
```

### Gerar cards a partir de um arquivo

```bash
uv run geg-toanki create ./material.pdf --deck "Biologia" --subdecks
```

### Gerar arquivos intermediários em Markdown

```bash
uv run geg-toanki create ./material.pdf --deck "História" --generate-md
```

### Opções

| Opção | Descrição |
| --- | --- |
| `-d`, `--deck` | Nome do deck principal no Anki |
| `-s`, `--subdecks` | Cria subdecks a partir da estrutura de diretórios |
| `-m`, `--generate-md` | Gera arquivos intermediários em Markdown no diretório temporário |
| `input_path_str` | Caminho do arquivo de entrada (PDF, TXT ou MD) |

## Fluxo do projeto

1. O arquivo de entrada é processado e convertido para Markdown.
2. O conteúdo é lido em um diretório temporário `.geg/toanki/temp`.
3. Cada arquivo Markdown é enviado para o modelo Gemini.
4. O modelo retorna um JSON com flashcards estruturados.
5. Os cards são enviados ao Anki via AnkiConnect.

## Observações

- O projeto usa `geg-tomd` como dependência local para converter conteúdos em Markdown antes da geração dos flashcards.
- A integração com o Anki depende do AnkiConnect estar acessível no endpoint configurado.
- O comando atual foi pensado para fluxo de estudo e geração de cards a partir de materiais acadêmicos ou de referência.

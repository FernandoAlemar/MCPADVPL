# Setup do dicionario de dados

O dicionario **oficial deste MCP** vem do export SX3 do seu ambiente Protheus (arquivo JSON enviado pela equipe), convertido para a estrutura local abaixo.

**Nao use** o repositorio [protheus-dicionario](https://github.com/FernandoAlemar/protheus-dicionario) como fonte — ele pode estar incompleto em relacao ao seu ambiente.

## Estrutura local (modelo protheus-dicionario)

```text
data/dicionario/
  index.json
  tabelas/{PREFIXO}/{CODIGO}.json
data/dicionario-meta.json    # tabelas do projeto (secao, uso, PK)
docs/dicionario-projeto.md   # gerado — subset legivel
```

Schema por tabela: `tabela`, `nome`, `campos[]`, `indices[]`, `gatilhos[]`, `relacionamentos[]` (indices/gatilhos vazios na conversao SX3 v1).

## Conversao do export SX3 (obrigatorio)

Formato de entrada: array JSON com registros `X3_ARQUIVO`, `X3_CAMPO`, `X3_TIPO`, etc.

```powershell
cd mcp-rest-tlpp
.venv\Scripts\activate
pip install ijson
python scripts/converter_sx3_para_dicionario.py --clean --input "C:\Users\alemar\Downloads\Dicionário de dados PROTHEUS.json"
python scripts/gerar_dicionario_projeto.py
```

- `--clean` apaga `data/dicionario/tabelas/` anterior (ex.: clone Git incorreto)
- A conversao do arquivo ~538 MB pode levar **10–30+ minutos** e ocupar ~1 GB em disco
- Reinicie o MCP no Cursor apos concluir

## Uso no MCP

| Recurso / tool | Uso |
|----------------|-----|
| `rest-tlpp://docs/dicionario-projeto` | Tabelas usadas no PROTHEUS-ADVPL |
| `rest-tlpp://docs/dicionario-index` | Indice resumido |
| `consultar_tabela_dicionario` | Definicao completa de uma tabela |

## Git

`data/dicionario/` esta no `.gitignore` (volume grande). Versione `data/dicionario-meta.json` e `docs/dicionario-projeto.md`, ou publique o convertido em repositorio interno.

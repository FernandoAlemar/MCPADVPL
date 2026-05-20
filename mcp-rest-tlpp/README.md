# MCP - Agente de Criacao de APIs REST TLPP

Este repositorio e autocontido: contem o servidor MCP, a documentacao e as rules necessarias para apoiar a criacao de APIs REST TLPP no Protheus.

## Estrutura

```text
mcp-rest-tlpp/
├── server.py
├── requirements.txt
├── data/
│   ├── dicionario/           # JSON por tabela (gerado; ver .gitignore)
│   └── dicionario-meta.json  # subset e metadados do projeto
├── scripts/
│   ├── converter_sx3_para_dicionario.py
│   └── gerar_dicionario_projeto.py
├── docs/
│   ├── dicionario-projeto.md
│   ├── setup-dicionario-dados.md
│   └── ...
└── rules/
```

## Uso rapido

1. Clone ou copie esta pasta para onde quiser.
2. Crie o ambiente e instale dependencias:
   ```powershell
   cd mcp-rest-tlpp
   py -3 -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Gere o dicionario a partir do **seu export SX3** (nao use o Git publico): `docs/setup-dicionario-dados.md`
4. Configure o Cursor ou o VS Code conforme `docs/manual-configuracao-mcp-equipe-dev.md`.

## Recursos expostos

| URI | Descricao |
|-----|-----------|
| `rest-tlpp://docs/style-guide` | Style guide resumido |
| `rest-tlpp://docs/prompt-criar-api` | Prompt de criacao de API |
| `rest-tlpp://docs/instrucoes-agente` | Instrucoes operacionais do agente |
| `rest-tlpp://docs/manual-desenvolvedor` | Manual do desenvolvedor |
| `rest-tlpp://docs/manual-configuracao-mcp` | Manual de configuracao do MCP |
| `rest-tlpp://docs/dicionario-dados` | Guia do dicionario (JSON + tools) |
| `rest-tlpp://docs/dicionario-projeto` | Tabelas do PROTHEUS-ADVPL |
| `rest-tlpp://docs/dicionario-index` | Indice resumido de tabelas |
| `rest-tlpp://rules/api-rest-processo` | Rule de processo |
| `rest-tlpp://rules/api-rest-tlpp` | Rule tecnica |
| `rest-tlpp://contexto/criar-api` | Contexto agregado para criacao de API |

## Prompt e tools

### Prompt

- `criar_api_rest_tlpp`

### Tools

- `validar_solicitacao_api_rest_tlpp`
- `gerar_especificacao_api_rest_tlpp`
- `gerar_template_api_rest_tlpp`
- `consultar_tabela_dicionario` — definicao JSON de uma tabela (ex.: SA1)

## Requisitos

- Python 3.10+
- Cursor ou VS Code com suporte a MCP
- ~1 GB disco livre para `data/dicionario/` (apos setup)

## Documentacao completa

- `docs/manual-configuracao-mcp-equipe-dev.md`
- `docs/manual-desenvolvedor-rest-tlpp.md`
- `docs/setup-dicionario-dados.md`
- `docs/dicionario-projeto.md` — subset do projeto

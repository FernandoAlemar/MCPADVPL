# MCP - Agente de Criacao de APIs REST TLPP

Este repositorio e autocontido: contem o servidor MCP, a documentacao e as rules necessarias para apoiar a criacao de APIs REST TLPP no Protheus.

## Estrutura

```text
mcp-rest-tlpp/
├── server.py
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── README.md
├── docs/
│   ├── style-guide-rest-tlpp.md
│   ├── prompt-criar-api-rest.md
│   ├── instrucoes-agente.md
│   ├── manual-desenvolvedor-rest-tlpp.md
│   ├── manual-configuracao-mcp-equipe-dev.md
│   └── dicionario-dados-protheus.md
├── rules/
│   ├── api-rest-processo.mdc
│   └── api-rest-tlpp.mdc
├── .vscode/
│   └── mcp.json
└── .cursor/
    └── mcp.json.example
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
3. Configure o Cursor ou o VS Code conforme `docs/manual-configuracao-mcp-equipe-dev.md`.

## Recursos expostos

| URI | Descricao |
|-----|-----------|
| `rest-tlpp://docs/style-guide` | Style guide resumido |
| `rest-tlpp://docs/prompt-criar-api` | Prompt de criacao de API |
| `rest-tlpp://docs/instrucoes-agente` | Instrucoes operacionais do agente |
| `rest-tlpp://docs/manual-desenvolvedor` | Manual do desenvolvedor |
| `rest-tlpp://docs/manual-configuracao-mcp` | Manual de configuracao do MCP |
| `rest-tlpp://docs/dicionario-dados` | Dicionario de dados Protheus (tabelas/campos para APIs) |
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

## Requisitos

- Python 3.10+
- Cursor ou VS Code com suporte a MCP

## Documentacao completa

- `docs/manual-configuracao-mcp-equipe-dev.md`
- `docs/manual-desenvolvedor-rest-tlpp.md`
- `docs/dicionario-dados-protheus.md` — dicionario de dados para montagem de queries e APIs

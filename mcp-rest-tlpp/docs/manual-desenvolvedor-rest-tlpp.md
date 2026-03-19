# Manual do Desenvolvedor - MCP REST TLPP

## Visao geral

O `mcp-rest-tlpp` e um projeto isolado para apoiar o processo completo de criacao de APIs REST TLPP.

Ele centraliza:

- documentacao
- rules
- prompt base
- tools de validacao, especificacao e geracao de template

## Fluxo recomendado

1. Validar a solicitacao com `validar_solicitacao_api_rest_tlpp`
2. Gerar a especificacao com `gerar_especificacao_api_rest_tlpp`
3. Gerar o template com `gerar_template_api_rest_tlpp`
4. Ajustar o endpoint ao contexto real do projeto destino

## Tools disponiveis

### `validar_solicitacao_api_rest_tlpp`

Confere se a demanda possui os dados minimos para iniciar.

### `gerar_especificacao_api_rest_tlpp`

Consolida metodo, rota, pasta, nome do arquivo, funcao, filtros e campos de retorno.

### `gerar_template_api_rest_tlpp`

Gera um template base TLPP para GET, POST, PUT e DELETE.

## Prompt

### `criar_api_rest_tlpp`

Prompt base para criacao de API com reforco da pergunta obrigatoria sobre a pasta.

## Resources

- `rest-tlpp://docs/style-guide`
- `rest-tlpp://docs/prompt-criar-api`
- `rest-tlpp://docs/instrucoes-agente`
- `rest-tlpp://docs/manual-desenvolvedor`
- `rest-tlpp://docs/manual-configuracao-mcp`
- `rest-tlpp://rules/api-rest-processo`
- `rest-tlpp://rules/api-rest-tlpp`
- `rest-tlpp://contexto/criar-api`

## Evolucao

Ao atualizar este projeto:

- revise `server.py`
- revise os arquivos de `docs/`
- revise os arquivos de `rules/`
- valide com `python -m py_compile server.py`
- teste o MCP no Cursor ou VS Code

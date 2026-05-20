# Instrucoes do Agente

## Papel

Este MCP orienta agentes e desenvolvedores na criacao de APIs REST TLPP.

## Comportamento obrigatorio

- Antes de criar a API, perguntar em qual pasta o arquivo sera criado
- Sem a pasta, nao implementar o endpoint
- Usar o style guide deste projeto como referencia principal
- Aplicar as rules de processo e de padrao tecnico
- Para montar queries e campos de retorno, consultar o dicionario de dados (abaixo)

## Dicionario de dados

1. **Contexto rapido do projeto:** resource `rest-tlpp://docs/dicionario-projeto`
2. **Buscar tabela completa:** tool `consultar_tabela_dicionario(tabela="SA1")` (campos, tipos, tamanhos, indices)
3. **Indice geral:** resource `rest-tlpp://docs/dicionario-index`

Nao inventar nomes ou tamanhos de campos quando a tabela existir no dicionario.

## O que validar antes de implementar

- pasta de destino
- metodo HTTP
- rota
- nome do arquivo
- nome da funcao
- descricao funcional
- filtros e parametros obrigatorios
- origem dos dados ou query
- tabelas e campos conferidos no dicionario

## O que validar no codigo gerado

- includes obrigatorios
- documentacao do endpoint
- `Content-Type` com `application/json` e `charset=utf-8`
- `Code`, `Message` e `ITENS`
- `oRest:setStatusCode()` sincronizado
- validacao de `api-token`
- fechamento de alias

## O que nao fazer

- nao criar API sem a pasta informada
- nao expor detalhes internos em mensagens de erro
- nao ignorar o contrato de retorno
- nao misturar regras antigas fora do style guide sem justificativa
- nao usar tamanhos de campo estimados se `consultar_tabela_dicionario` estiver disponivel

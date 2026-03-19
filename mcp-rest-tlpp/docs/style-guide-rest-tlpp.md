# Style Guide REST TLPP

Guia resumido e autocontido para criacao de APIs REST TLPP no Protheus.

## Objetivo

Padronizar o desenvolvimento de endpoints REST TLPP com:

- contrato de retorno consistente
- autenticacao padronizada
- documentacao uniforme
- tratamento previsivel de erros

## Estrutura de arquivo

- Arquivos REST devem ficar na pasta `Rest/` do projeto de destino
- Extensao obrigatoria: `.tlpp`
- Agrupar endpoints relacionados no mesmo arquivo
- Nome do arquivo deve refletir o dominio da API

## Includes obrigatorios

```tlpp
#include 'tlpp-core.th'
#include 'tlpp-rest.th'
#INCLUDE "TOTVS.CH"
#INCLUDE "PROTHEUS.CH"
#INCLUDE "TBICONN.CH"
#INCLUDE "TOPCONN.CH"
```

## Cabecalho do endpoint

Todo endpoint deve ter bloco de documentacao com:

- funcao
- tipo e rota
- descricao
- parametros
- retorno
- historico de atualizacao

## Contrato JSON obrigatorio

Toda resposta deve seguir:

```json
{
  "Code": 200,
  "Message": "Solicitacao concluida",
  "ITENS": []
}
```

## Status code

- Sempre sincronizar `oRest:setStatusCode()` com `Code`
- `200` para consulta/operação bem-sucedida sem criacao
- `201` para inclusao com criacao efetiva
- `400` para parametros invalidos, regra de negocio ou JSON invalido
- `401` para token ausente ou nao configurado
- `403` para token invalido
- `500` para erro interno inesperado

## Autenticacao

Usar o header `api-token`.

Regras:

- `401` quando `GetMV("BB_TOKFLG")` estiver vazio
- `401` quando o header `api-token` nao for enviado
- `403` quando o token enviado for diferente do esperado

## GET

- Ler query params com `oRest:getQueryRequest()`
- Validar parametros obrigatorios antes da query
- Retornar `ITENS` com array de objetos

## POST e PUT

- Ler body com `oRest:getBodyRequest()`
- Fazer parse com `oBody:fromJson(cBody)`
- Retornar `400` se o JSON for invalido

## SQL e alias

- Preferir `%table:%`, `%notDel%` e `%exp:%` em `BeginSql`
- Sempre fechar alias com `DbCloseArea()`

## Gravacao

- Usar `RecLock()`
- Sempre executar `MsUnlock()` apos a gravacao

## Erros

- Nao expor stacktrace
- Nao expor SQL bruto
- Nao expor informacao sensivel no campo `Message`

## Processo obrigatorio

Antes de criar a API, perguntar obrigatoriamente:

`Em qual pasta essa API deve ser criada?`

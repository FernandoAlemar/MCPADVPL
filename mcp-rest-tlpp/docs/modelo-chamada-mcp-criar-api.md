# Modelo de Chamada do MCP para Criação de API

Use estes exemplos ao chamar as tools do MCP `rest-tlpp` para criar APIs REST TLPP.

---

## 1. Validar a solicitação

Confira se todos os dados obrigatórios estão presentes antes de gerar a API.

```json
{
  "tool": "validar_solicitacao_api_rest_tlpp",
  "arguments": {
    "folder": "Producao/Rest",
    "file_name": "apiFuncionarios.tlpp",
    "method": "GET",
    "route": "/v1/funcionarios/consulta",
    "function_name": "getFuncionarios",
    "description": "Consulta funcionarios por matricula"
  }
}
```

---

## 2. Gerar especificação

Consolida método, rota, pasta, filtros e campos de retorno.

```json
{
  "tool": "gerar_especificacao_api_rest_tlpp",
  "arguments": {
    "folder": "Producao/Rest",
    "file_name": "apiFuncionarios.tlpp",
    "method": "GET",
    "route": "/v1/funcionarios/consulta",
    "function_name": "getFuncionarios",
    "description": "Consulta funcionarios por matricula",
    "filters": ["matricula", "filial"],
    "response_fields": ["RA_FILIAL", "RA_MAT", "RA_NOME"],
    "source_query": "SELECT RA_FILIAL, RA_MAT, RA_NOME FROM SRA200 WHERE RA_MAT = cMat"
  }
}
```

---

## 3. Modelo GET – Consulta

Gera template de endpoint de consulta (leitura).

```json
{
  "tool": "gerar_template_api_rest_tlpp",
  "arguments": {
    "folder": "Producao/Rest",
    "method": "GET",
    "route": "/v1/funcionarios/consulta",
    "function_name": "getFuncionarios",
    "description": "Consulta funcionarios por matricula",
    "query_params": [
      {
        "name": "matricula",
        "description": "Matricula do funcionario",
        "required": true
      },
      {
        "name": "filial",
        "description": "Filial do funcionario",
        "required": false
      }
    ],
    "response_fields": ["RA_FILIAL", "RA_MAT", "RA_NOME"],
    "source_query": "SELECT RA_FILIAL, RA_MAT, RA_NOME FROM %table:SRA% WHERE RA_MAT = :cMatricula AND D_E_L_E_T_ = ''"
  }
}
```

---

## 4. Modelo POST – Inclusão

Gera template de endpoint de inclusão (criação de registro).

```json
{
  "tool": "gerar_template_api_rest_tlpp",
  "arguments": {
    "folder": "Producao/Rest",
    "method": "POST",
    "route": "/v1/funcionarios/inclusao",
    "function_name": "postFuncionario",
    "description": "Inclusao de funcionario",
    "body_fields": ["codigo", "nome", "filial", "cpf", "data_admissao"],
    "response_fields": [],
    "source_query": ""
  }
}
```

---

## 5. Modelo PUT – Alteração

Gera template de endpoint de alteração (atualização de registro).

```json
{
  "tool": "gerar_template_api_rest_tlpp",
  "arguments": {
    "folder": "Producao/Rest",
    "method": "PUT",
    "route": "/v1/funcionarios/alteracao",
    "function_name": "putFuncionario",
    "description": "Alteracao de funcionario",
    "body_fields": ["matricula", "nome", "filial", "cpf"],
    "response_fields": [],
    "source_query": ""
  }
}
```

---

## 6. Prompt – Contexto completo

Use o prompt quando quiser enviar o contexto completo para o agente (inclui reforço da pergunta da pasta).

```json
{
  "prompt": "criar_api_rest_tlpp",
  "arguments": {
    "objetivo": "Criar API de consulta de funcionarios por matricula",
    "metodo": "GET",
    "rota": "/v1/funcionarios/consulta",
    "pasta": "Producao/Rest",
    "nome_arquivo": "apiFuncionarios.tlpp",
    "nome_funcao": "getFuncionarios",
    "query_origem": "SELECT RA_FILIAL, RA_MAT, RA_NOME FROM SRA200 WHERE RA_MAT = cMat"
  }
}
```

---

## Campos obrigatórios (resumo)

| Campo            | Obrigatório | Descrição                          |
|------------------|-------------|------------------------------------|
| `folder`         | Sim         | Pasta onde o arquivo será criado   |
| `method`         | Sim         | GET, POST, PUT ou DELETE           |
| `route`          | Sim         | Rota do endpoint (ex: /v1/recurso) |
| `function_name`  | Sim         | Nome da User Function              |
| `description`    | Sim         | Descrição da API                   |
| `query_params`   | GET         | Parâmetros de query                |
| `body_fields`    | POST/PUT    | Campos esperados no body           |
| `response_fields`| GET         | Campos retornados em ITENS         |
| `source_query`   | Opcional    | Query SQL de referência            |

---

## Regra do MCP

**Sem `folder` informado**, as tools `gerar_especificacao_api_rest_tlpp` e `gerar_template_api_rest_tlpp` retornam bloqueio e a pergunta:

> Em qual pasta essa API deve ser criada?

Sempre informe a pasta antes de solicitar a geração do template.

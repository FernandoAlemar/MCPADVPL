#!/usr/bin/env python3
"""
MCP Server - Agente de Criacao de APIs REST TLPP (projeto isolado)

Expoe como resources a documentacao e as rules embutidas neste projeto.
Mantem tools e prompt para apoiar o processo completo de criacao de APIs REST TLPP.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field


def _project_root() -> Path:
    return Path(__file__).resolve().parent


_PROJECT_ROOT = _project_root()
mcp = FastMCP("rest-tlpp")

REQUIRED_INCLUDES = [
    "#include 'tlpp-core.th'",
    "#include 'tlpp-rest.th'",
    '#INCLUDE "TOTVS.CH"',
    '#INCLUDE "PROTHEUS.CH"',
    '#INCLUDE "TBICONN.CH"',
    '#INCLUDE "TOPCONN.CH"',
]


class QueryParam(BaseModel):
    name: str = Field(description="Nome do parametro")
    description: str | None = Field(default=None, description="Descricao do parametro")
    required: bool = Field(default=True, description="Se o parametro e obrigatorio")


def _read_file(relative_path: str, encoding: str = "utf-8") -> str:
    path = _PROJECT_ROOT / relative_path.lstrip("/")
    try:
        return path.read_text(encoding=encoding)
    except FileNotFoundError:
        return f"[Arquivo nao encontrado: {relative_path}]"
    except Exception as exc:
        return f"[Erro ao ler {relative_path}: {exc}]"


def _normalize_route(route: str) -> str:
    if not route:
        return "/"
    return route if route.startswith("/") else f"/{route}"


def _method_decorator(method: str) -> str:
    decorators = {
        "GET": "@Get",
        "POST": "@Post",
        "PUT": "@Put",
        "DELETE": "@Delete",
    }
    return decorators[method.upper()]


def _build_variable_name(name: str) -> str:
    cleaned = "".join(ch if ch.isalnum() else " " for ch in (name or "").strip())
    parts = [part for part in cleaned.split() if part]
    camel = "".join(part.lower().capitalize() for part in parts)
    return f"c{camel or 'Parametro'}"


def _build_header_params(query_params: list[QueryParam]) -> list[str]:
    lines = [
        "              - Header 'api-token' (Character): Token de seguranca (Obrigatorio)"
    ]
    for param in query_params:
        required = "Obrigatorio" if param.required else "Opcional"
        description = param.description or "Parametro de consulta"
        lines.append(
            f"              - Query Param '{param.name}' (Character): {description} ({required})"
        )
    return lines


def _build_local_variables(query_params: list[QueryParam]) -> list[str]:
    if not query_params:
        return ['    Local cParametro := ""']
    return [f'    Local {_build_variable_name(param.name)} := ""' for param in query_params]


def _build_param_validations(
    query_params: list[QueryParam], response_object_name: str
) -> list[str]:
    if not query_params:
        return ["        // Validar parametros obrigatorios aqui"]

    lines: list[str] = []
    for param in query_params:
        variable_name = _build_variable_name(param.name)
        lines.append(
            f'        {variable_name} := IIf(aNames["{param.name}"] == NIL, "", AllTrim(aNames["{param.name}"]))'
        )
        if param.required:
            lines.extend(
                [
                    "",
                    f"        If Empty({variable_name})",
                    f'            {response_object_name}["Code"]    := 400',
                    f'            {response_object_name}["Message"] := "Parametro obrigatorio {param.name} nao informado"',
                    f'            {response_object_name}["ITENS"]   := {{}}',
                    "            BREAK",
                    "        EndIf",
                ]
            )
        lines.append("")

    while lines and lines[-1] == "":
        lines.pop()

    return lines


def _build_field_assignments(response_fields: list[str]) -> list[str]:
    if not response_fields:
        return ['            aDadosRet[Len(aDadosRet)]["Campo"] := (cAlias)->CAMPO']
    return [
        f'            aDadosRet[Len(aDadosRet)]["{field.strip()}"] := (cAlias)->{field.strip()}'
        for field in response_fields
    ]


def _build_query_comments(source_query: str) -> list[str]:
    if not source_query.strip():
        return ["            // Escreva aqui a query conforme a regra de negocio"]
    return [f"            // {line}" for line in source_query.splitlines()]


def _build_get_template(
    function_name: str,
    route: str,
    description: str,
    query_params: list[QueryParam],
    response_fields: list[str],
    source_query: str,
) -> str:
    lines: list[str] = []
    lines.extend(REQUIRED_INCLUDES)
    lines.extend(
        [
            "",
            "/*",
            "------------------------------------------------------------------------------------------------------------",
            f"Funcao      : {function_name}",
            f"Tipo        : Metodo GET - {route}",
            f"Descricao   : {description}",
            "Parametros  :",
        ]
    )
    lines.extend(_build_header_params(query_params))
    lines.extend(
        [
            "Retorno     : (Nilean) - A resposta e enviada via oRest:setResponse no formato JSON",
            "------------------------------------------------------------------------------------------------------------",
            "Atualizacoes:",
            "- MM/YYYY - EMPRESA - DESENVOLVEDOR - Criacao do endpoint",
            "------------------------------------------------------------------------------------------------------------",
            "*/",
            f'{_method_decorator("GET")}("{route}")',
            f"User Function {function_name}()",
            "",
            '    Local cRetGet   := ""',
            "    Local oRetGet   := JsonObject():New()",
            "    Local oHeader   := NIL",
            "    Local aNames    := JsonObject():New()",
            "    Local aDadosRet := {}",
            '    Local tokenAtual := GetMV("BB_TOKFLG")',
            '    Local cApiToken := ""',
            '    Local cAlias    := ""',
        ]
    )
    lines.extend(_build_local_variables(query_params))
    lines.extend(
        [
            "",
            '    oRest:setKeyHeaderResponse("Content-Type", "application/json", "charset=utf-8")',
            "",
            "    aNames  := oRest:getQueryRequest()",
            "    oHeader := oRest:getHeaderRequest()",
            "",
            "    BEGIN SEQUENCE",
            "",
            '        cApiToken := oHeader["api-token"]',
            "",
            "        If Empty(tokenAtual)",
            '            oRetGet["Code"]    := 401',
            '            oRetGet["Message"] := "Erro token procurar ADM integracao"',
            '            oRetGet["ITENS"]   := {}',
            "            BREAK",
            "        EndIf",
            "",
            "        If Empty(cApiToken)",
            '            oRetGet["Code"]    := 401',
            '            oRetGet["Message"] := "Token nao informado no header"',
            '            oRetGet["ITENS"]   := {}',
            "            BREAK",
            "        EndIf",
            "",
            "        If AllTrim(cApiToken) <> AllTrim(tokenAtual)",
            '            oRetGet["Code"]    := 403',
            '            oRetGet["Message"] := "Token de Seguranca invalido"',
            '            oRetGet["ITENS"]   := {}',
            "            BREAK",
            "        EndIf",
            "",
        ]
    )
    lines.extend(_build_param_validations(query_params, "oRetGet"))
    lines.extend(
        [
            "        cAlias := GetNextAlias()",
            "        BeginSql alias cAlias",
            "            %noparser%",
        ]
    )
    lines.extend(_build_query_comments(source_query))
    lines.extend(
        [
            "        EndSql",
            "",
            "        While !(cAlias)->(Eof())",
            "            AAdd(aDadosRet, JsonObject():New())",
        ]
    )
    lines.extend(_build_field_assignments(response_fields))
    lines.extend(
        [
            "            (cAlias)->(DbSkip())",
            "        EndDo",
            "",
            "        (cAlias)->(DbCloseArea())",
            "",
            "        If Len(aDadosRet) == 0",
            '            oRetGet["Code"]    := 400',
            '            oRetGet["Message"] := "Nao ha dados para os parametros informados"',
            '            oRetGet["ITENS"]   := {}',
            "            BREAK",
            "        EndIf",
            "",
            '        oRetGet["Code"]    := 200',
            '        oRetGet["Message"] := "Solicitacao concluida"',
            '        oRetGet["ITENS"]   := aDadosRet',
            "",
            "    END SEQUENCE",
            "",
            "    cRetGet := oRetGet:toJson()",
            '    oRest:setStatusCode(oRetGet["Code"])',
            "    oRest:setResponse(cRetGet)",
            "",
            "Return",
        ]
    )
    return "\n".join(lines) + "\n"


def _build_mutation_template(
    method: str,
    function_name: str,
    route: str,
    description: str,
    body_fields: list[str],
) -> str:
    response_name = "oRetPost"
    response_var = "cRetPost"
    body_lines = (
        [f"              - Body JSON '{field}': Campo esperado" for field in body_fields]
        if body_fields
        else ["              - Body JSON: Campos esperados da operacao"]
    )

    lines: list[str] = []
    lines.extend(REQUIRED_INCLUDES)
    lines.extend(
        [
            "",
            "/*",
            "------------------------------------------------------------------------------------------------------------",
            f"Funcao      : {function_name}",
            f"Tipo        : Metodo {method} - {route}",
            f"Descricao   : {description}",
            "Parametros  :",
            "              - Header 'api-token' (Character): Token de seguranca (Obrigatorio)",
        ]
    )
    lines.extend(body_lines)
    lines.extend(
        [
            "Retorno     : (Nilean) - A resposta e enviada via oRest:setResponse no formato JSON",
            "------------------------------------------------------------------------------------------------------------",
            "Atualizacoes:",
            "- MM/YYYY - EMPRESA - DESENVOLVEDOR - Criacao do endpoint",
            "------------------------------------------------------------------------------------------------------------",
            "*/",
            f'{_method_decorator(method)}("{route}")',
            f"User Function {function_name}()",
            "",
            '    Local cBody     := ""',
            f'    Local {response_var}  := ""',
            f"    Local {response_name} := JsonObject():New()",
            "    Local oBody     := JsonObject():New()",
            "    Local oHeader   := NIL",
            '    Local cError    := ""',
            '    Local tokenAtual := GetMV("BB_TOKFLG")',
            '    Local cApiToken := ""',
            "",
            '    oRest:setKeyHeaderResponse("Content-Type", "application/json", "charset=utf-8")',
            "",
            "    cBody   := oRest:getBodyRequest()",
            "    cError  := oBody:fromJson(cBody)",
            "    oHeader := oRest:getHeaderRequest()",
            "",
            "    BEGIN SEQUENCE",
            "",
            "        If !Empty(cError)",
            f'            {response_name}["Code"]    := 400',
            f'            {response_name}["Message"] := "Erro requisicao. Formato do objeto/Json pode estar invalido"',
            f'            {response_name}["ITENS"]   := cError',
            "            BREAK",
            "        EndIf",
            "",
            '        cApiToken := oHeader["api-token"]',
            "",
            "        If Empty(tokenAtual)",
            f'            {response_name}["Code"]    := 401',
            f'            {response_name}["Message"] := "Erro token procurar ADM integracao"',
            f'            {response_name}["ITENS"]   := {{}}',
            "            BREAK",
            "        EndIf",
            "",
            "        If Empty(cApiToken)",
            f'            {response_name}["Code"]    := 401',
            f'            {response_name}["Message"] := "Token nao informado no header"',
            f'            {response_name}["ITENS"]   := {{}}',
            "            BREAK",
            "        EndIf",
            "",
            "        If AllTrim(cApiToken) <> AllTrim(tokenAtual)",
            f'            {response_name}["Code"]    := 403',
            f'            {response_name}["Message"] := "Token de Seguranca invalido"',
            f'            {response_name}["ITENS"]   := {{}}',
            "            BREAK",
            "        EndIf",
            "",
            "        // Validar campos obrigatorios e regras de negocio aqui",
            "        // Implementar processamento da operacao aqui",
            "",
            f'        {response_name}["Code"]    := {"201" if method.upper() == "POST" else "200"}',
            f'        {response_name}["Message"] := "Operacao realizada com sucesso"',
            f'        {response_name}["ITENS"]   := {{}}',
            "",
            "    END SEQUENCE",
            "",
            f"    {response_var} := {response_name}:toJson()",
            f'    oRest:setStatusCode({response_name}["Code"])',
            f"    oRest:setResponse({response_var})",
            "",
            "Return",
        ]
    )
    return "\n".join(lines) + "\n"


def _build_template(
    method: str,
    route: str,
    function_name: str,
    description: str,
    query_params: list[QueryParam],
    body_fields: list[str],
    response_fields: list[str],
    source_query: str,
) -> str:
    normalized_route = _normalize_route(route)
    if method.upper() == "GET":
        return _build_get_template(
            function_name=function_name,
            route=normalized_route,
            description=description,
            query_params=query_params,
            response_fields=response_fields,
            source_query=source_query,
        )
    return _build_mutation_template(
        method=method.upper(),
        function_name=function_name,
        route=normalized_route,
        description=description,
        body_fields=body_fields,
    )


def _build_missing_folder_response() -> dict:
    return {
        "ready": False,
        "required_question": "Em qual pasta essa API deve ser criada?",
        "message": (
            "Processo bloqueado: antes de criar a API, informe obrigatoriamente "
            "a pasta onde o arquivo sera criado."
        ),
    }


# Resources - docs/
@mcp.resource("rest-tlpp://docs/style-guide")
def resource_style_guide() -> str:
    """Style guide resumido para APIs REST TLPP."""
    return _read_file("docs/style-guide-rest-tlpp.md")


@mcp.resource("rest-tlpp://docs/prompt-criar-api")
def resource_prompt_criar_api() -> str:
    """Prompt de referencia para criacao de APIs REST TLPP."""
    return _read_file("docs/prompt-criar-api-rest.md")


@mcp.resource("rest-tlpp://docs/instrucoes-agente")
def resource_instrucoes_agente() -> str:
    """Instrucoes operacionais do agente."""
    return _read_file("docs/instrucoes-agente.md")


@mcp.resource("rest-tlpp://docs/manual-desenvolvedor")
def resource_manual_desenvolvedor() -> str:
    """Manual do desenvolvedor do MCP REST TLPP."""
    return _read_file("docs/manual-desenvolvedor-rest-tlpp.md")


@mcp.resource("rest-tlpp://docs/manual-configuracao-mcp")
def resource_manual_configuracao() -> str:
    """Manual de configuracao do MCP para equipe DEV."""
    return _read_file("docs/manual-configuracao-mcp-equipe-dev.md")


@mcp.resource("rest-tlpp://docs/dicionario-dados")
def resource_dicionario_dados() -> str:
    """Dicionario de dados Protheus para montagem de queries e APIs REST TLPP."""
    return _read_file("docs/dicionario-dados-protheus.md")


# Resources - rules/
@mcp.resource("rest-tlpp://rules/api-rest-processo")
def resource_rule_api_rest_processo() -> str:
    """Rule: processo obrigatorio para criacao de APIs REST."""
    return _read_file("rules/api-rest-processo.mdc")


@mcp.resource("rest-tlpp://rules/api-rest-tlpp")
def resource_rule_api_rest_tlpp() -> str:
    """Rule: padrao tecnico obrigatorio para APIs REST TLPP."""
    return _read_file("rules/api-rest-tlpp.mdc")


@mcp.resource("rest-tlpp://contexto/criar-api")
def resource_contexto_criar_api() -> str:
    """Contexto agregado para criacao de APIs REST TLPP."""
    prompt = _read_file("docs/prompt-criar-api-rest.md")
    instrucoes = _read_file("docs/instrucoes-agente.md")
    style = _read_file("docs/style-guide-rest-tlpp.md")
    rule_processo = _read_file("rules/api-rest-processo.mdc")
    rule_tecnica = _read_file("rules/api-rest-tlpp.mdc")
    return (
        "# PROMPT CRIAR API\n\n"
        + prompt
        + "\n\n# INSTRUCOES DO AGENTE\n\n"
        + instrucoes
        + "\n\n# RULE PROCESSO\n\n"
        + rule_processo
        + "\n\n# RULE TECNICA\n\n"
        + rule_tecnica
        + "\n\n# STYLE GUIDE REST TLPP\n\n"
        + style
    )


@mcp.prompt()
def criar_api_rest_tlpp(
    objetivo: str,
    metodo: str,
    rota: str,
    pasta: str | None = None,
    nome_arquivo: str | None = None,
    nome_funcao: str | None = None,
    query_origem: str | None = None,
) -> str:
    """Prompt base para criar uma API REST TLPP respeitando a pasta obrigatoria e o style guide."""
    folder_instruction = (
        f"A pasta informada para criacao e `{pasta}`."
        if pasta
        else "Antes de qualquer implementacao, pergunte obrigatoriamente: Em qual pasta essa API deve ser criada?"
    )
    return (
        f"Crie uma API REST TLPP com o seguinte objetivo: {objetivo}\n\n"
        f"{folder_instruction}\n\n"
        f"Metodo: {metodo}\n"
        f"Rota: {_normalize_route(rota)}\n"
        f"Arquivo: {nome_arquivo or '(definir)'}\n"
        f"Funcao: {nome_funcao or '(definir)'}\n"
        f"Query de origem:\n{query_origem or '(definir)'}\n\n"
        "Antes de implementar, consulte:\n"
        "- rest-tlpp://docs/instrucoes-agente\n"
        "- rest-tlpp://rules/api-rest-processo\n"
        "- rest-tlpp://rules/api-rest-tlpp\n"
        "- rest-tlpp://docs/style-guide\n"
        "- rest-tlpp://docs/dicionario-dados (tabelas/campos para montar a query)\n\n"
        "Se a pasta nao tiver sido informada, nao gere o endpoint ainda."
    )


@mcp.tool()
def validar_solicitacao_api_rest_tlpp(
    folder: str | None = None,
    file_name: str | None = None,
    method: str | None = None,
    route: str | None = None,
    function_name: str | None = None,
    description: str | None = None,
) -> dict:
    """Valida se a solicitacao possui os dados minimos para iniciar a criacao da API REST TLPP."""
    missing = []
    if not folder:
        missing.append("folder")
    if not file_name:
        missing.append("file_name")
    if not method:
        missing.append("method")
    if not route:
        missing.append("route")
    if not function_name:
        missing.append("function_name")
    if not description:
        missing.append("description")

    return {
        "ready": len(missing) == 0,
        "missing": missing,
        "required_question": (
            "Em qual pasta essa API deve ser criada?" if not folder else None
        ),
        "message": (
            "Solicitacao completa para iniciar a criacao da API."
            if not missing
            else "Ainda faltam dados obrigatorios para iniciar a criacao da API: "
            + ", ".join(missing)
            + "."
        ),
    }


@mcp.tool()
def gerar_especificacao_api_rest_tlpp(
    file_name: str,
    method: str,
    route: str,
    function_name: str,
    description: str,
    folder: str | None = None,
    source_query: str | None = None,
    filters: list[str] | None = None,
    response_fields: list[str] | None = None,
) -> dict:
    """Gera uma especificacao operacional da API REST TLPP, incluindo checklist de processo e padrao tecnico."""
    if not folder:
        return _build_missing_folder_response()

    return {
        "ready": True,
        "folder": folder,
        "file_name": file_name,
        "method": method,
        "route": _normalize_route(route),
        "function_name": function_name,
        "description": description,
        "filters": filters or [],
        "response_fields": response_fields or [],
        "source_query": source_query or "",
        "references": [
            "rest-tlpp://rules/api-rest-processo",
            "rest-tlpp://rules/api-rest-tlpp",
            "rest-tlpp://docs/style-guide",
        ],
    }


@mcp.tool()
def gerar_template_api_rest_tlpp(
    method: str,
    route: str,
    function_name: str,
    description: str,
    folder: str | None = None,
    query_params: list[QueryParam] | None = None,
    body_fields: list[str] | None = None,
    response_fields: list[str] | None = None,
    source_query: str | None = None,
) -> dict:
    """Gera um template de endpoint TLPP conforme o style guide e o processo definido para o projeto."""
    if not folder:
        return _build_missing_folder_response()

    template = _build_template(
        method=method,
        route=route,
        function_name=function_name,
        description=description,
        query_params=query_params or [],
        body_fields=body_fields or [],
        response_fields=response_fields or [],
        source_query=source_query or "",
    )

    return {
        "ready": True,
        "generated": True,
        "folder": folder,
        "method": method.upper(),
        "route": _normalize_route(route),
        "function_name": function_name,
        "template": template,
    }


def main() -> None:
    if os.environ.get("MCP_DEBUG"):
        print(f"[rest-tlpp] Project root: {_PROJECT_ROOT}", file=sys.stderr)
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()

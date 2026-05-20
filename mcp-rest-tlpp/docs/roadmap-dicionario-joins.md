# Roadmap — JOINs e relacionamentos no dicionario

Melhoria planejada para implementacao futura. O dicionario atual (SX3 + meta do projeto) permanece como esta.

## Estado atual

- `data/dicionario/` — campos por tabela (export SX3 local, nao versionado)
- Tool `consultar_tabela_dicionario`
- `data/dicionario-meta.json` — PK e contexto das tabelas do projeto
- `indices[]` / `relacionamentos[]` vazios na conversao v1

## Fase 1 — Meta do projeto

- [ ] Estender `dicionario-meta.json` com bloco `relacionamentos` por tabela
- [ ] Exemplo SE1 → SA1: `E1_CLIENTE+E1_LOJA` → `A1_COD+A1_LOJA`
- [ ] Documentar joins usados no codigo (U13/CN9, U97/SE2, etc.)

## Fase 2 — Heuristica no conversor

- [ ] Detectar `ExistCpo("SA1")` em `X3_VALID`
- [ ] Detectar pares `*_CLIENTE` + `*_LOJA`, `*_FORNECE` + `*_LOJA`
- [ ] Preencher `relacionamentos[]` candidatos no JSON por tabela

## Fase 3 — Tools MCP

- [ ] `sugerir_join(tabela_origem, tabela_destino)`
- [ ] `listar_relacionamentos(tabela)`
- [ ] Atualizar `instrucoes-agente.md` e prompt `criar_api_rest_tlpp`

## Fase 4 — Dados oficiais

- [ ] Export SIX (indices) do ambiente
- [ ] Export relacionamentos (SX9 ou equivalente)
- [ ] Mesclar no conversor

## Fase 5 — Indice MCP (opcional)

- [ ] Busca/paginacao no resource `dicionario-index` (hoje resumo de 200 tabelas)

## Criterios de aceite

- `sugerir_join("SE1", "SA1")` retorna ON alinhado ao meta/heuristica
- Agente documenta JOIN na API sem inventar campo de ligacao

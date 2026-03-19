# Dicionário de Dados — MCP-REST-TLPP (Projeto PROTHEUS-ADVPL)

Documento de referência do projeto **MCP-REST-TLPP** para apoio à criação de APIs REST TLPP. Ao solicitar uma API informando os dados desejados, o agente utiliza este dicionário para **montar a query** (tabelas, alias, campos, JOINs) e **construir o endpoint** (rotas, parâmetros, filtros e contrato de retorno).

- **Uso:** Informe ao agente qual recurso deseja (ex.: clientes, títulos a receber, funcionários) e, se quiser, quais campos ou filtros; o dicionário traz tabelas **padrão TOTVS** e **customizadas** (Stage/Integração) levantadas no repositório PROTHEUS-ADVPL.
- **Chaves e relacionamentos** descritos aqui evitam erros em consultas e ajudam a definir filtros e paginação.

---

Documento gerado a partir do levantamento de tabelas identificadas no código-fonte do repositório.  
Inclui tabelas **padrão TOTVS Protheus** e tabelas **customizadas** (Stage / Integração).

---

## Índice

1. [Financeiro — Contas a Receber / Cobrança](#1-financeiro--contas-a-receber--cobrança)
2. [Financeiro — Contas a Pagar](#2-financeiro--contas-a-pagar)
3. [Contabilidade](#3-contabilidade)
4. [Folha de Pagamento / RH (SIGAGPE)](#4-folha-de-pagamento--rh-sigagpe)
5. [Tabelas de Estrutura e Genéricas](#5-tabelas-de-estrutura-e-genéricas)
6. [Tabelas Customizadas — Stage / Integração](#6-tabelas-customizadas--stage--integração)
7. [Contratos / Fluig](#7-contratos--fluig)
8. [Workflow / Outros](#8-workflow--outros)

---

## 1. Financeiro — Contas a Receber / Cobrança

---

### SA1 — Clientes

| Atributo       | Valor                                          |
|----------------|------------------------------------------------|
| **Módulo**     | SIGAFAT / SIGAFIN                              |
| **Tipo**       | Padrão TOTVS                                   |
| **Descrição**  | Cadastro de clientes                           |
| **Uso no projeto** | BBFIN41 (Prepare), M030INC, FA200FIL       |

| Campo       | Tipo    | Tam. | Descrição                   |
|-------------|---------|------|-----------------------------|
| SA1_FILIAL  | Char    | 8    | Filial                      |
| SA1_COD     | Char    | 6    | Código do cliente           |
| SA1_LOJA    | Char    | 2    | Loja                        |
| SA1_NOME    | Char    | 40   | Nome do cliente             |
| SA1_NREDUZ  | Char    | 20   | Nome reduzido               |
| SA1_END     | Char    | 40   | Endereço                    |
| SA1_MUN     | Char    | 20   | Município                   |
| SA1_CEP     | Char    | 8    | CEP                         |
| SA1_EST     | Char    | 2    | Estado (UF)                 |
| SA1_CGC     | Char    | 14   | CNPJ / CPF                  |
| SA1_PESSOA  | Char    | 1    | Tipo de pessoa (F/J)        |
| SA1_MSBLQL  | Char    | 1    | Bloqueio (1=Sim)            |
| SA1_EMAIL   | Char    | 250  | E-mail                      |
| SA1_TIPO    | Char    | 1    | Tipo (R=Revendedor, etc.)   |

**Chave Primária:** `SA1_FILIAL + SA1_COD + SA1_LOJA`

---

### SE1 — Títulos a Receber

| Atributo       | Valor                                      |
|----------------|--------------------------------------------|
| **Módulo**     | SIGAFIN                                    |
| **Tipo**       | Padrão TOTVS                               |
| **Descrição**  | Títulos a receber (duplicatas/boletos)     |
| **Uso no projeto** | FA200FIL (Cobrança)                    |

| Campo         | Tipo    | Tam. | Descrição                        |
|---------------|---------|------|----------------------------------|
| E1_FILIAL     | Char    | 8    | Filial                           |
| E1_PREFIXO    | Char    | 3    | Prefixo do título                |
| E1_NUM        | Char    | 9    | Número do título                 |
| E1_PARCELA    | Char    | 2    | Parcela                          |
| E1_TIPO       | Char    | 3    | Tipo do título (NF, DP, etc.)    |
| E1_CLIENTE    | Char    | 6    | Código do cliente                |
| E1_LOJA       | Char    | 2    | Loja do cliente                  |
| E1_EMISSAO    | Date    | 8    | Data de emissão                  |
| E1_VENCTO     | Date    | 8    | Data de vencimento original      |
| E1_VENCREA    | Date    | 8    | Data de vencimento real          |
| E1_VALOR      | Numeric | 15,2 | Valor do título                  |
| E1_SALDO      | Numeric | 15,2 | Saldo em aberto                  |
| E1_SITUACAO   | Char    | 1    | Situação (A=Aberto, B=Baixado)   |
| E1_PORTADO    | Char    | 3    | Portador (banco)                 |
| E1_NATUREZ    | Char    | 10   | Natureza financeira              |
| E1_HISTOR     | Char    | 40   | Histórico                        |

**Chave Primária:** `E1_FILIAL + E1_PREFIXO + E1_NUM + E1_PARCELA + E1_TIPO + E1_CLIENTE + E1_LOJA`

---

### SE5 — Movimentação Contas a Receber

| Atributo       | Valor                                          |
|----------------|------------------------------------------------|
| **Módulo**     | SIGAFIN                                        |
| **Tipo**       | Padrão TOTVS                                   |
| **Descrição**  | Movimentação de contas a receber               |
| **Uso no projeto** | F430BXA.PRW (ponto de entrada baixa)       |

| Campo         | Tipo    | Tam. | Descrição                      |
|---------------|---------|------|--------------------------------|
| E5_FILIAL     | Char    | 8    | Filial                         |
| E5_DATA       | Date    | 8    | Data da movimentação           |
| E5_BANCO      | Char    | 3    | Banco                          |
| E5_AGENCIA    | Char    | 5    | Agência                        |
| E5_CONTA      | Char    | 10   | Conta corrente                 |
| E5_PREFIXO    | Char    | 3    | Prefixo do título              |
| E5_NUM        | Char    | 9    | Número do título               |
| E5_PARCELA    | Char    | 2    | Parcela                        |
| E5_TIPO       | Char    | 3    | Tipo                           |
| E5_CLIFOR     | Char    | 6    | Cliente/Fornecedor             |
| E5_LOJA       | Char    | 2    | Loja                           |
| E5_NATUREZ    | Char    | 10   | Natureza financeira            |
| E5_VALOR      | Numeric | 15,2 | Valor da movimentação          |
| E5_RECPAG     | Char    | 1    | Recebimento (R) ou Pagamento (P)|
| E5_HISTOR     | Char    | 40   | Histórico                      |
| E5_MOEDA      | Char    | 2    | Moeda                          |

**Chave Primária:** `E5_FILIAL + E5_PREFIXO + E5_NUM + E5_PARCELA + E5_TIPO + E5_CLIFOR + E5_LOJA + E5_DATA`

---

## 2. Financeiro — Contas a Pagar

---

### SA2 — Fornecedores

| Atributo       | Valor                                        |
|----------------|----------------------------------------------|
| **Módulo**     | SIGACOM / SIGAFIN                            |
| **Tipo**       | Padrão TOTVS                                 |
| **Descrição**  | Cadastro de fornecedores                     |
| **Uso no projeto** | BBFIN21, BBAJUFOR, M020INC               |

| Campo       | Tipo    | Tam. | Descrição                    |
|-------------|---------|------|------------------------------|
| SA2_FILIAL  | Char    | 8    | Filial                       |
| SA2_COD     | Char    | 6    | Código do fornecedor         |
| SA2_LOJA    | Char    | 2    | Loja                         |
| SA2_NOME    | Char    | 40   | Nome do fornecedor           |
| SA2_NREDUZ  | Char    | 20   | Nome reduzido                |
| SA2_END     | Char    | 40   | Endereço                     |
| SA2_MUN     | Char    | 20   | Município                    |
| SA2_CEP     | Char    | 8    | CEP                          |
| SA2_EST     | Char    | 2    | Estado (UF)                  |
| SA2_CGC     | Char    | 14   | CNPJ / CPF                   |
| SA2_PESSOA  | Char    | 1    | Tipo de pessoa (F/J)         |
| SA2_MSBLQL  | Char    | 1    | Bloqueio (1=Sim)             |
| SA2_EMAIL   | Char    | 250  | E-mail                       |
| SA2_BANCO   | Char    | 3    | Banco domicílio              |
| SA2_AGENCIA | Char    | 5    | Agência bancária             |
| SA2_CONTA   | Char    | 10   | Conta corrente               |

**Chave Primária:** `SA2_FILIAL + SA2_COD + SA2_LOJA`

---

### SE2 — Títulos a Pagar

| Atributo       | Valor                                            |
|----------------|--------------------------------------------------|
| **Módulo**     | SIGAFIN                                          |
| **Tipo**       | Padrão TOTVS                                     |
| **Descrição**  | Títulos a pagar (duplicatas a fornecedores)      |
| **Uso no projeto** | U97Stagecpagar.tlpp (join com U97), dash_integracao.tlpp |

| Campo         | Tipo    | Tam. | Descrição                         |
|---------------|---------|------|-----------------------------------|
| E2_FILIAL     | Char    | 8    | Filial                            |
| E2_PREFIXO    | Char    | 3    | Prefixo do título                 |
| E2_NUM        | Char    | 9    | Número do título                  |
| E2_PARCELA    | Char    | 2    | Parcela                           |
| E2_TIPO       | Char    | 3    | Tipo do título                    |
| E2_FORNECE    | Char    | 6    | Código do fornecedor              |
| E2_LOJA       | Char    | 2    | Loja do fornecedor                |
| E2_EMISSAO    | Date    | 8    | Data de emissão                   |
| E2_VENCTO     | Date    | 8    | Data de vencimento                |
| E2_VENCREA    | Date    | 8    | Data de vencimento real           |
| E2_VALOR      | Numeric | 15,2 | Valor do título                   |
| E2_SALDO      | Numeric | 15,2 | Saldo em aberto                   |
| E2_SITUACAO   | Char    | 1    | Situação (A=Aberto, B=Baixado)    |
| E2_PORTADO    | Char    | 3    | Portador (banco)                  |
| E2_NATUREZ    | Char    | 10   | Natureza financeira               |
| E2_HISTOR     | Char    | 40   | Histórico                         |

**Chave Primária:** `E2_FILIAL + E2_PREFIXO + E2_NUM + E2_PARCELA + E2_TIPO + E2_FORNECE + E2_LOJA`

---

### FIL — Contas Bancárias do Fornecedor

| Atributo       | Valor                                      |
|----------------|--------------------------------------------|
| **Módulo**     | SIGAFIN                                    |
| **Tipo**       | Padrão TOTVS                               |
| **Descrição**  | Contas bancárias vinculadas a fornecedores |
| **Uso no projeto** | BBFIN21                                |

| Campo       | Tipo | Tam. | Descrição                    |
|-------------|------|------|------------------------------|
| FIL_FILIAL  | Char | 8    | Filial                       |
| FIL_FORNECE | Char | 6    | Código do fornecedor         |
| FIL_LOJA    | Char | 2    | Loja do fornecedor           |
| FIL_BANCO   | Char | 3    | Código do banco              |
| FIL_AGENCIA | Char | 5    | Agência                      |
| FIL_CONTA   | Char | 10   | Conta corrente               |
| FIL_DTINC   | Date | 8    | Data de inclusão             |

**Chave Primária:** `FIL_FILIAL + FIL_FORNECE + FIL_LOJA + FIL_BANCO + FIL_AGENCIA + FIL_CONTA`

---

## 3. Contabilidade

---

### CTD — Plano de Contas / Itens Contábeis

| Atributo       | Valor                                      |
|----------------|--------------------------------------------|
| **Módulo**     | SIGACTB                                    |
| **Tipo**       | Padrão TOTVS                               |
| **Descrição**  | Plano de contas e itens contábeis          |
| **Uso no projeto** | M020INC, M030INC                       |

| Campo        | Tipo    | Tam. | Descrição                         |
|--------------|---------|------|-----------------------------------|
| CTD_FILIAL   | Char    | 8    | Filial                            |
| CTD_ITEM     | Char    | 20   | Código do item contábil           |
| CTD_DESC01   | Char    | 40   | Descrição (Português)             |
| CTD_DESC02   | Char    | 40   | Descrição (Inglês)                |
| CTD_DESC03   | Char    | 40   | Descrição (Espanhol)              |
| CTD_CLASSE   | Char    | 1    | Classe (A=Ativo, P=Passivo, etc.) |
| CTD_NORMAL   | Char    | 1    | Saldo normal (D=Devedor, C=Credor)|
| CTD_REDUZ    | Char    | 20   | Código reduzido                   |
| CTD_GRPVEN   | Char    | 6    | Grupo de vendas                   |
| CTD_MSBLQL   | Char    | 1    | Bloqueio                          |

**Chave Primária:** `CTD_FILIAL + CTD_ITEM`

---

### CTT — Centros de Custo

| Atributo       | Valor                                          |
|----------------|------------------------------------------------|
| **Módulo**     | SIGACTB                                        |
| **Tipo**       | Padrão TOTVS                                   |
| **Descrição**  | Centros de custo contábeis                     |
| **Uso no projeto** | recibo.PRX, INTEGRACAO_APPUS.tlpp, fRel005.prw |

| Campo        | Tipo | Tam. | Descrição                        |
|--------------|------|------|----------------------------------|
| CTT_FILIAL   | Char | 8    | Filial                           |
| CTT_CUSTO    | Char | 9    | Código do centro de custo        |
| CTT_DESC01   | Char | 40   | Descrição (Português)            |
| CTT_DESC02   | Char | 40   | Descrição (Inglês)               |
| CTT_CLASS    | Char | 1    | Classificação                    |
| CTT_BLOQ     | Char | 1    | Bloqueio (1=Sim)                 |
| CTT_CTARED   | Char | 20   | Conta reduzida associada         |

**Chave Primária:** `CTT_FILIAL + CTT_CUSTO`

---

### CTF — Lançamentos Contábeis

| Atributo       | Valor                                  |
|----------------|----------------------------------------|
| **Módulo**     | SIGACTB                                |
| **Tipo**       | Padrão TOTVS                           |
| **Descrição**  | Lançamentos do livro-razão contábil    |
| **Uso no projeto** | BBCTB01.PRW                        |

| Campo         | Tipo    | Tam. | Descrição                        |
|---------------|---------|------|----------------------------------|
| CF_FILIAL     | Char    | 8    | Filial                           |
| CF_LOTE       | Char    | 8    | Número do lote                   |
| CF_SUBLOTE    | Char    | 5    | Sub-lote                         |
| CF_DATA       | Date    | 8    | Data do lançamento               |
| CF_HIST       | Char    | 40   | Histórico                        |
| CF_DEBITO     | Char    | 20   | Conta débito                     |
| CF_CREDITO    | Char    | 20   | Conta crédito                    |
| CF_VALOR      | Numeric | 15,2 | Valor do lançamento              |
| CF_CCUSTO     | Char    | 9    | Centro de custo                  |
| CF_MOEDA      | Char    | 2    | Moeda                            |
| CF_SISTEMA    | Char    | 5    | Sistema de origem                |

**Chave Primária:** `CF_FILIAL + CF_LOTE + CF_SUBLOTE`

---

### SI3 — Centros de Custo (Descrição Complementar)

| Atributo       | Valor                               |
|----------------|-------------------------------------|
| **Módulo**     | SIGACTB / SIGAGPE                   |
| **Tipo**       | Padrão TOTVS                        |
| **Descrição**  | Descrição complementar de CC        |
| **Uso no projeto** | recibo.PRX                      |

| Campo       | Tipo | Tam. | Descrição             |
|-------------|------|------|-----------------------|
| I3_FILIAL   | Char | 8    | Filial                |
| I3_CCUSTO   | Char | 9    | Código centro de custo|
| I3_DESCRI   | Char | 40   | Descrição             |

**Chave Primária:** `I3_FILIAL + I3_CCUSTO`

---

## 4. Folha de Pagamento / RH (SIGAGPE)

---

### SRA — Funcionários

| Atributo       | Valor                                                         |
|----------------|---------------------------------------------------------------|
| **Módulo**     | SIGAGPE                                                       |
| **Tipo**       | Padrão TOTVS                                                  |
| **Descrição**  | Cadastro de funcionários                                      |
| **Uso no projeto** | recibo.PRX, BCGPE007, INTEGRACAO_APPUS.tlpp, PROCU16.TLPP |

| Campo        | Tipo    | Tam. | Descrição                          |
|--------------|---------|------|------------------------------------|
| RA_FILIAL    | Char    | 8    | Filial                             |
| RA_MAT       | Char    | 6    | Matrícula do funcionário           |
| RA_NOME      | Char    | 40   | Nome                               |
| RA_ADMISSA   | Date    | 8    | Data de admissão                   |
| RA_DEMISSA   | Date    | 8    | Data de demissão                   |
| RA_SITFOLH   | Char    | 1    | Situação na folha                  |
| RA_DEPTO     | Char    | 9    | Departamento                       |
| RA_CARGO     | Char    | 3    | Cargo                              |
| RA_CC        | Char    | 9    | Centro de custo                    |
| RA_SALARIO   | Numeric | 14,2 | Salário                            |
| RA_TPCONTR   | Char    | 1    | Tipo de contrato                   |
| RA_CATFUNC   | Char    | 3    | Categoria de função                |
| RA_SINDICA   | Char    | 3    | Código do sindicato                |
| RA_REGIPRE   | Char    | 1    | Regime previdenciário              |
| RA_CIC       | Char    | 11   | CPF                                |
| RA_EMAIL     | Char    | 250  | E-mail corporativo                 |

**Chave Primária:** `RA_FILIAL + RA_MAT`

---

### SRC — Verbas de Competência

| Atributo       | Valor                              |
|----------------|------------------------------------|
| **Módulo**     | SIGAGPE                            |
| **Tipo**       | Padrão TOTVS                       |
| **Descrição**  | Verbas fixas/variáveis por competência |
| **Uso no projeto** | recibo.PRX                     |

| Campo         | Tipo    | Tam. | Descrição                 |
|---------------|---------|------|---------------------------|
| RC_FILIAL     | Char    | 8    | Filial                    |
| RC_MAT        | Char    | 6    | Matrícula do funcionário  |
| RC_COMPETENCIA| Char    | 6    | Competência (AAAAMM)      |
| RC_CODVB      | Char    | 5    | Código de verba           |
| RC_VALOR      | Numeric | 14,2 | Valor da verba            |
| RC_QTDHOR     | Numeric | 6,2  | Quantidade de horas       |

**Chave Primária:** `RC_FILIAL + RC_MAT + RC_COMPETENCIA + RC_CODVB`

---

### SRD — Verbas de Débito (Folha)

| Atributo       | Valor                               |
|----------------|-------------------------------------|
| **Módulo**     | SIGAGPE                             |
| **Tipo**       | Padrão TOTVS                        |
| **Descrição**  | Verbas de débito calculadas na folha|
| **Uso no projeto** | recibo.PRX, BCGPE007            |

| Campo       | Tipo    | Tam. | Descrição                |
|-------------|---------|------|--------------------------|
| RD_FILIAL   | Char    | 8    | Filial                   |
| RD_MAT      | Char    | 6    | Matrícula                |
| RD_DATARQ   | Date    | 8    | Data de referência       |
| RD_CODVB    | Char    | 5    | Código de verba          |
| RD_VALOR    | Numeric | 14,2 | Valor                    |
| RD_QTDHOR   | Numeric | 6,2  | Horas/Quantidade         |

**Chave Primária:** `RD_FILIAL + RD_MAT + RD_DATARQ + RD_CODVB`

---

### SRV — Verbas / Códigos de Folha

| Atributo       | Valor                              |
|----------------|------------------------------------|
| **Módulo**     | SIGAGPE                            |
| **Tipo**       | Padrão TOTVS                       |
| **Descrição**  | Tabela de verbas e códigos da folha|
| **Uso no projeto** | BCGPE007                       |

| Campo       | Tipo | Tam. | Descrição                      |
|-------------|------|------|--------------------------------|
| RV_FILIAL   | Char | 8    | Filial                         |
| RV_COD      | Char | 5    | Código da verba                |
| RV_DESCRI   | Char | 40   | Descrição                      |
| RV_TIPO     | Char | 1    | Tipo (P=Provento, D=Desconto)  |
| RV_CTDCR    | Char | 20   | Conta crédito contábil         |
| RV_CTDDB    | Char | 20   | Conta débito contábil          |
| RV_INCBASE  | Char | 1    | Incide na base                 |

**Chave Primária:** `RV_FILIAL + RV_COD`

---

### SRY — Roteiros de Folha

| Atributo       | Valor                            |
|----------------|----------------------------------|
| **Módulo**     | SIGAGPE                          |
| **Tipo**       | Padrão TOTVS                     |
| **Descrição**  | Roteiros de cálculo da folha     |
| **Uso no projeto** | recibo.PRX                   |

| Campo       | Tipo | Tam. | Descrição             |
|-------------|------|------|-----------------------|
| RY_FILIAL   | Char | 8    | Filial                |
| RY_COD      | Char | 3    | Código do roteiro     |
| RY_DESCRI   | Char | 40   | Descrição             |
| RY_TIPO     | Char | 1    | Tipo de roteiro       |

**Chave Primária:** `RY_FILIAL + RY_COD`

---

### SRH — Histórico do Funcionário

| Atributo       | Valor                                |
|----------------|--------------------------------------|
| **Módulo**     | SIGAGPE                              |
| **Tipo**       | Padrão TOTVS                         |
| **Descrição**  | Histórico de alterações do funcionário|
| **Uso no projeto** | recibo.PRX                       |

| Campo        | Tipo    | Tam. | Descrição                  |
|--------------|---------|------|----------------------------|
| RH_FILIAL    | Char    | 8    | Filial                     |
| RH_MAT       | Char    | 6    | Matrícula                  |
| RH_DTINI     | Date    | 8    | Data início da vigência    |
| RH_DTFIM     | Date    | 8    | Data fim da vigência       |
| RH_SALARIO   | Numeric | 14,2 | Salário no período         |
| RH_CARGO     | Char    | 3    | Cargo no período           |
| RH_CC        | Char    | 9    | Centro de custo no período |

**Chave Primária:** `RH_FILIAL + RH_MAT + RH_DTINI`

---

### SRJ — Função / Cargo (RH)

| Atributo       | Valor                                       |
|----------------|---------------------------------------------|
| **Módulo**     | SIGAGPE                                     |
| **Tipo**       | Padrão TOTVS                                |
| **Descrição**  | Funções e cargos dos funcionários           |
| **Uso no projeto** | INTEGRACAO_APPUS.tlpp                   |

| Campo       | Tipo | Tam. | Descrição        |
|-------------|------|------|------------------|
| RJ_FILIAL   | Char | 8    | Filial           |
| RJ_COD      | Char | 3    | Código da função |
| RJ_DESCRI   | Char | 40   | Descrição        |

**Chave Primária:** `RJ_FILIAL + RJ_COD`

---

### SRK — (RH — Cancelamento)

| Atributo       | Valor                          |
|----------------|--------------------------------|
| **Módulo**     | SIGAGPE                        |
| **Tipo**       | Padrão TOTVS                   |
| **Descrição**  | Registros de cancelamento (RH) |
| **Uso no projeto** | GP030CAN.prw               |

| Campo       | Tipo | Tam. | Descrição             |
|-------------|------|------|-----------------------|
| RK_FILIAL   | Char | 8    | Filial                |
| RK_MAT      | Char | 6    | Matrícula             |
| RK_DATA     | Date | 8    | Data do cancelamento  |
| RK_MOTIVO   | Char | 3    | Motivo                |

**Chave Primária:** `RK_FILIAL + RK_MAT + RK_DATA`

---

### SR8 / SRE — Consultas SQL de Folha

| Atributo       | Valor                                         |
|----------------|-----------------------------------------------|
| **Módulo**     | SIGAGPE                                       |
| **Tipo**       | Padrão TOTVS                                  |
| **Descrição**  | Tabelas auxiliares utilizadas em consultas SQL|
| **Uso no projeto** | BCGPE007.prw                              |

> Estas tabelas são acessadas via consultas SQL dinâmicas (`RetSqlName`) e seguem a estrutura interna do SIGAGPE.

---

### SQB — Departamentos (RH)

| Atributo       | Valor                                      |
|----------------|--------------------------------------------|
| **Módulo**     | SIGAGPE                                    |
| **Tipo**       | Padrão TOTVS                               |
| **Descrição**  | Cadastro de departamentos                  |
| **Uso no projeto** | recibo.PRX, INTEGRACAO_APPUS.tlpp      |

| Campo       | Tipo | Tam. | Descrição                 |
|-------------|------|------|---------------------------|
| QB_FILIAL   | Char | 8    | Filial                    |
| QB_DEPTO    | Char | 9    | Código do departamento    |
| QB_DESCRI   | Char | 40   | Descrição                 |
| QB_CC       | Char | 9    | Centro de custo associado |

**Chave Primária:** `QB_FILIAL + QB_DEPTO`

---

### SQ3 — Cargos (RH)

| Atributo       | Valor                         |
|----------------|-------------------------------|
| **Módulo**     | SIGAGPE                       |
| **Tipo**       | Padrão TOTVS                  |
| **Descrição**  | Cadastro de cargos            |
| **Uso no projeto** | recibo.PRX                |

| Campo       | Tipo | Tam. | Descrição        |
|-------------|------|------|------------------|
| Q3_FILIAL   | Char | 8    | Filial           |
| Q3_CARGO    | Char | 3    | Código do cargo  |
| Q3_DESCRI   | Char | 40   | Descrição        |
| Q3_CBO      | Char | 6    | Código CBO       |

**Chave Primária:** `Q3_FILIAL + Q3_CARGO`

---

### RCH — Calendário / Período Folha

| Atributo       | Valor                              |
|----------------|------------------------------------|
| **Módulo**     | SIGAGPE                            |
| **Tipo**       | Padrão TOTVS                       |
| **Descrição**  | Períodos de competência da folha   |
| **Uso no projeto** | recibo.PRX                     |

| Campo       | Tipo | Tam. | Descrição                 |
|-------------|------|------|---------------------------|
| CH_FILIAL   | Char | 8    | Filial                    |
| CH_PERREF   | Char | 6    | Período de referência (AAAAMM) |
| CH_DTINI    | Date | 8    | Data início do período    |
| CH_DTFIM    | Date | 8    | Data fim do período       |
| CH_TIPO     | Char | 1    | Tipo de folha             |

**Chave Primária:** `CH_FILIAL + CH_PERREF`

---

### RCC — Códigos de Folha

| Atributo       | Valor                                |
|----------------|--------------------------------------|
| **Módulo**     | SIGAGPE                              |
| **Tipo**       | Padrão TOTVS                         |
| **Descrição**  | Códigos de eventos da folha          |
| **Uso no projeto** | recibo.PRX, BCGPE41              |

| Campo       | Tipo | Tam. | Descrição            |
|-------------|------|------|----------------------|
| CC_FILIAL   | Char | 8    | Filial               |
| CC_COD      | Char | 5    | Código              |
| CC_DESCRI   | Char | 40   | Descrição            |

**Chave Primária:** `CC_FILIAL + CC_COD`

---

### RCE — Sindicatos

| Atributo       | Valor                        |
|----------------|------------------------------|
| **Módulo**     | SIGAGPE                      |
| **Tipo**       | Padrão TOTVS                 |
| **Descrição**  | Cadastro de sindicatos       |
| **Uso no projeto** | BCGPE007                 |

| Campo       | Tipo | Tam. | Descrição                 |
|-------------|------|------|---------------------------|
| CE_FILIAL   | Char | 8    | Filial                    |
| CE_COD      | Char | 3    | Código do sindicato       |
| CE_DESCRI   | Char | 40   | Descrição                 |
| CE_CNPJ     | Char | 14   | CNPJ                      |

**Chave Primária:** `CE_FILIAL + CE_COD`

---

### RCF — Semana Folha

| Atributo       | Valor                             |
|----------------|-----------------------------------|
| **Módulo**     | SIGAGPE                           |
| **Tipo**       | Padrão TOTVS                      |
| **Descrição**  | Controle de semanas na folha      |
| **Uso no projeto** | recibo.PRX                    |

| Campo       | Tipo | Tam. | Descrição                 |
|-------------|------|------|---------------------------|
| CF_FILIAL   | Char | 8    | Filial                    |
| CF_SEMANA   | Char | 2    | Semana                    |
| CF_DTINI    | Date | 8    | Data início da semana     |
| CF_DTFIM    | Date | 8    | Data fim da semana        |

**Chave Primária:** `CF_FILIAL + CF_SEMANA`

---

### RCB — Seguro Vida (RH)

| Atributo       | Valor                                |
|----------------|--------------------------------------|
| **Módulo**     | SIGAGPE                              |
| **Tipo**       | Padrão TOTVS                         |
| **Descrição**  | Controle de seguro de vida           |
| **Uso no projeto** | BCGPE41                          |

| Campo        | Tipo    | Tam. | Descrição                 |
|--------------|---------|------|---------------------------|
| RCB_FILIAL   | Char    | 8    | Filial                    |
| RCB_MAT      | Char    | 6    | Matrícula                 |
| RCB_TPBENEF  | Char    | 3    | Tipo de benefício         |
| RCB_VALOR    | Numeric | 14,2 | Valor do seguro           |

**Chave Primária:** `RCB_FILIAL + RCB_MAT + RCB_TPBENEF`

---

### RGG — Categorias (RH)

| Atributo       | Valor                           |
|----------------|---------------------------------|
| **Módulo**     | SIGAGPE                         |
| **Tipo**       | Padrão TOTVS                    |
| **Descrição**  | Categorias de funcionários      |
| **Uso no projeto** | recibo.PRX                  |

| Campo       | Tipo | Tam. | Descrição         |
|-------------|------|------|-------------------|
| GG_FILIAL   | Char | 8    | Filial            |
| GG_COD      | Char | 3    | Código            |
| GG_DESCRI   | Char | 40   | Descrição         |

**Chave Primária:** `GG_FILIAL + GG_COD`

---

### VAM — Municípios

| Atributo       | Valor                              |
|----------------|------------------------------------|
| **Módulo**     | SIGAGPE / geral                    |
| **Tipo**       | Padrão TOTVS                       |
| **Descrição**  | Tabela de municípios               |
| **Uso no projeto** | recibo.PRX                     |

| Campo       | Tipo | Tam. | Descrição          |
|-------------|------|------|--------------------|
| AM_COD      | Char | 7    | Código do município|
| AM_DESCRI   | Char | 30   | Nome do município  |
| AM_EST      | Char | 2    | Estado (UF)        |
| AM_IBGE     | Char | 7    | Código IBGE        |

**Chave Primária:** `AM_COD`

---

### RFS / CUP / CUU — Tabelas RH (PROCU16)

| Atributo       | Valor                                   |
|----------------|-----------------------------------------|
| **Módulo**     | SIGAGPE                                 |
| **Tipo**       | Padrão TOTVS                            |
| **Descrição**  | Tabelas complementares de RH            |
| **Uso no projeto** | PROCU16.TLPP                        |

> Tabelas utilizadas em processos de cálculo de contribuições previdenciárias e sindicais. Estrutura detalhada disponível no dicionário padrão TOTVS (SX3).

---

## 5. Tabelas de Estrutura e Genéricas

---

### SX5 — Tabelas Genéricas

| Atributo       | Valor                                        |
|----------------|----------------------------------------------|
| **Módulo**     | Geral (todos os módulos)                     |
| **Tipo**       | Padrão TOTVS (metadados)                     |
| **Descrição**  | Tabelas auxiliares / de domínio do sistema   |
| **Uso no projeto** | recibo.PRX, CHGX5FIL.PRW                |

| Campo       | Tipo | Tam. | Descrição                           |
|-------------|------|------|-------------------------------------|
| X5_FILIAL   | Char | 8    | Filial                              |
| X5_TABELA   | Char | 2    | Identificador da tabela             |
| X5_CHAVE    | Char | 3    | Chave (código do domínio)           |
| X5_DESCRI   | Char | 40   | Descrição (Português)               |
| X5_DESCPOR  | Char | 40   | Descrição alternativa               |

**Chave Primária:** `X5_FILIAL + X5_TABELA + X5_CHAVE`

---

### SX3 — Estrutura de Campos (Cache)

| Atributo       | Valor                                          |
|----------------|------------------------------------------------|
| **Módulo**     | Geral (todos os módulos)                       |
| **Tipo**       | Padrão TOTVS (metadados)                       |
| **Descrição**  | Dicionário de campos do sistema                |
| **Uso no projeto** | Vários (TamSX3, GetSx3Cache)               |

| Campo       | Tipo    | Tam. | Descrição                          |
|-------------|---------|------|------------------------------------|
| X3_ARQUIVO  | Char    | 10   | Nome da tabela                     |
| X3_CAMPO    | Char    | 10   | Nome do campo                      |
| X3_TIPO     | Char    | 1    | Tipo (C=Char, N=Num, D=Date, L=Lóg)|
| X3_TAMANHO  | Numeric | 5    | Tamanho do campo                   |
| X3_DECIMAL  | Numeric | 3    | Casas decimais                     |
| X3_TITULO   | Char    | 25   | Título do campo                    |
| X3_DESCRI   | Char    | 50   | Descrição completa                 |
| X3_USED     | Char    | 1    | Habilitado (S/N)                   |
| X3_VALID    | Char    | 250  | Validação                          |

**Chave Primária:** `X3_ARQUIVO + X3_CAMPO`

---

### SCP — Cadastro Protheus (Parâmetros Fluig)

| Atributo       | Valor                                        |
|----------------|----------------------------------------------|
| **Módulo**     | Geral                                        |
| **Tipo**       | Padrão TOTVS                                 |
| **Descrição**  | Parâmetros e pré-requisitos do sistema       |
| **Uso no projeto** | GERPREREQ.prw (integração Fluig)         |

| Campo       | Tipo | Tam. | Descrição             |
|-------------|------|------|-----------------------|
| CP_FILIAL   | Char | 8    | Filial                |
| CP_CODIGO   | Char | 10   | Código do parâmetro   |
| CP_DESCRI   | Char | 40   | Descrição             |
| CP_CONTEUD  | Char | 250  | Conteúdo do parâmetro |

**Chave Primária:** `CP_FILIAL + CP_CODIGO`

---

## 6. Tabelas Customizadas — Stage / Integração

> Tabelas criadas especificamente para este projeto. Não fazem parte do dicionário padrão TOTVS.

---

### ZAZ — Stage Controle de Cobrança (Custom)

| Atributo       | Valor                                        |
|----------------|----------------------------------------------|
| **Módulo**     | Custom — Financeiro/Cobrança                 |
| **Tipo**       | **Customizada**                              |
| **Descrição**  | Controle de stage do Job de Cobrança         |
| **Uso no projeto** | BBFIN41 (Job Cobrança)                   |

| Campo        | Tipo    | Tam. | Descrição                                 |
|--------------|---------|------|-------------------------------------------|
| ZAZ_FILIAL   | Char    | 8    | Filial                                    |
| ZAZ_COD      | Char    | 20   | Código de controle                        |
| ZAZ_STATUS   | Char    | 1    | Status (P=Pendente, E=Enviado, E=Erro)    |
| ZAZ_DATA     | Date    | 8    | Data do registro                          |
| ZAZ_TITULO   | Char    | 9    | Número do título referenciado             |
| ZAZ_PREFIXO  | Char    | 3    | Prefixo do título                         |
| ZAZ_PARCELA  | Char    | 2    | Parcela do título                         |
| ZAZ_CLIENTE  | Char    | 6    | Código do cliente                         |
| ZAZ_LOJA     | Char    | 2    | Loja do cliente                           |
| ZAZ_MSBLQL   | Char    | 1    | Bloqueio do registro                      |

**Chave Primária:** `ZAZ_FILIAL + ZAZ_COD`

---

### U97 — Stage Contas a Pagar (Custom REST)

| Atributo       | Valor                                              |
|----------------|----------------------------------------------------|
| **Módulo**     | Custom — REST / Integração CP                      |
| **Tipo**       | **Customizada**                                    |
| **Descrição**  | Stage de integração REST para Contas a Pagar       |
| **Uso no projeto** | U97Stagecpagar.tlpp, dash_integracao.tlpp      |

| Campo         | Tipo    | Tam. | Descrição                                  |
|---------------|---------|------|--------------------------------------------|
| U97_FILIAL    | Char    | 8    | Filial                                     |
| U97_ID        | Char    | 36   | Identificador único (GUID)                 |
| U97_STATUS    | Char    | 1    | Status (P=Pendente, I=Integrado, E=Erro)   |
| U97_FORNECE   | Char    | 6    | Código do fornecedor                       |
| U97_LOJA      | Char    | 2    | Loja do fornecedor                         |
| U97_PREFIXO   | Char    | 3    | Prefixo do título                          |
| U97_NUM       | Char    | 9    | Número do título                           |
| U97_PARCELA   | Char    | 2    | Parcela                                    |
| U97_TIPO      | Char    | 3    | Tipo do título                             |
| U97_VALOR     | Numeric | 15,2 | Valor do título                            |
| U97_VENCTO    | Date    | 8    | Data de vencimento                         |
| U97_DTINCL    | Date    | 8    | Data de inclusão no stage                  |
| U97_DTPROC    | Date    | 8    | Data de processamento                      |
| U97_ERRMSG    | Char    | 250  | Mensagem de erro (quando status = E)       |
| U97_MSBLQL    | Char    | 1    | Bloqueio do registro                       |

**Chave Primária:** `U97_FILIAL + U97_ID`

**Índice secundário:** `U97_FILIAL + U97_FORNECE + U97_LOJA + U97_PREFIXO + U97_NUM + U97_PARCELA + U97_TIPO` (join com SE2)

---

### UA3 — Stage Lançamento Contábil (Custom REST)

| Atributo       | Valor                                             |
|----------------|---------------------------------------------------|
| **Módulo**     | Custom — REST / Integração Contabilidade          |
| **Tipo**       | **Customizada**                                   |
| **Descrição**  | Stage de integração REST para lançamentos contábeis|
| **Uso no projeto** | stage_contabil.tlpp                           |

| Campo         | Tipo    | Tam. | Descrição                                  |
|---------------|---------|------|--------------------------------------------|
| UA3_FILIAL    | Char    | 8    | Filial                                     |
| UA3_ID        | Char    | 36   | Identificador único (GUID)                 |
| UA3_STATUS    | Char    | 1    | Status (P=Pendente, I=Integrado, E=Erro)   |
| UA3_LOTE      | Char    | 8    | Lote do lançamento                         |
| UA3_SUBLOTE   | Char    | 5    | Sub-lote                                   |
| UA3_DATA      | Date    | 8    | Data do lançamento                         |
| UA3_DEBITO    | Char    | 20   | Conta débito                               |
| UA3_CREDITO   | Char    | 20   | Conta crédito                              |
| UA3_VALOR     | Numeric | 15,2 | Valor do lançamento                        |
| UA3_HIST      | Char    | 40   | Histórico                                  |
| UA3_CCUSTO    | Char    | 9    | Centro de custo                            |
| UA3_DTINCL    | Date    | 8    | Data de inclusão no stage                  |
| UA3_DTPROC    | Date    | 8    | Data de processamento                      |
| UA3_ERRMSG    | Char    | 250  | Mensagem de erro (quando status = E)       |
| UA3_MSBLQL    | Char    | 1    | Bloqueio do registro                       |

**Chave Primária:** `UA3_FILIAL + UA3_ID`

---

### U98 — Stage Contas a Receber — Integração Legado (Custom)

| Atributo       | Valor                                                            |
|----------------|------------------------------------------------------------------|
| **Módulo**     | Custom — Financeiro / Integração Sistema Legado                  |
| **Tipo**       | **Customizada**                                                  |
| **Descrição**  | Stage de integração REST/Job para Contas a Receber vindos do sistema legado |
| **Uso no projeto** | SCHBBPRCU98.tlpp (Job de processamento)                      |

**Fluxo:** O sistema legado popula a U98 → o Job `SCHBBPRCU98` lê os registros pendentes e efetua inclusão, alteração, baixa ou exclusão de títulos em **SE1**, criando ou localizando o cliente em **SA1** quando necessário.

| Campo         | Tipo    | Tam. | Descrição                                              |
|---------------|---------|------|--------------------------------------------------------|
| U98_FILIAL    | Char    | 8    | Filial                                                 |
| U98_TIPOIN    | Char    | 1    | Tipo de integração (I=Inclusão, A=Alteração, B=Baixa, E=Exclusão) |
| U98_PREFIX    | Char    | 3    | Prefixo do título (mapeado para E1_PREFIXO)            |
| U98_NUM       | Char    | 9    | Número do título (mapeado para E1_NUM)                 |
| U98_PARCEL    | Char    | 2    | Parcela (mapeada para E1_PARCELA)                      |
| U98_TIPO      | Char    | 3    | Tipo do título (mapeado para E1_TIPO)                  |
| U98_CLIENT    | Char    | 20   | Código do cliente no sistema legado                    |
| U98_EMISSA    | Date    | 8    | Data de emissão do título                              |
| U98_VENCRE    | Date    | 8    | Data de vencimento real                                |
| U98_VALOR     | Numeric | 15,2 | Valor do título                                        |
| U98_SALDO     | Numeric | 15,2 | Saldo do título                                        |
| U98_MOEDA     | Char    | 2    | Moeda                                                  |
| U98_HIST      | Char    | 40   | Histórico                                              |
| U98_BCOCLI    | Char    | 3    | Banco do cliente (para baixa)                          |
| U98_AGECLI    | Char    | 5    | Agência do cliente (para baixa)                        |
| U98_CTACLI    | Char    | 10   | Conta do cliente (para baixa)                          |
| U98_PORTAD    | Char    | 3    | Portador / Banco cobrador                              |
| U98_DTBAIX    | Date    | 8    | Data da baixa                                          |
| U98_NUMBCO    | Char    | 20   | Número do boleto bancário                              |
| U98_CODBAR    | Char    | 60   | Código de barras                                       |
| U98_CODDIG    | Char    | 60   | Linha digitável                                        |
| U98_AGEDEP    | Char    | 5    | Agência de depósito                                    |
| U98_CONTA     | Char    | 10   | Conta corrente de depósito                             |
| U98_XCODLE    | Char    | 20   | Código legado do título (mapeado para E1_XCODLEG)      |
| U98_XNUMTI    | Char    | 9    | Número alternativo do título (uso TAA)                 |
| U98_XTID      | Char    | 20   | TID de transação de cartão                             |
| U98_XNTRAN    | Char    | 20   | Número da transação                                    |
| U98_XCARTA    | Char    | 20   | Identificador do cartão                                |
| U98_VLBRUT    | Numeric | 15,2 | Valor bruto                                            |
| U98_XVLRBX    | Numeric | 15,2 | Valor efetivo para baixa                               |
| U98_XEFETB    | Char    | 2    | Flag de efetivação de baixa                            |
| U98_XVLDCR    | Numeric | 15,2 | Valor do crédito (cartão)                              |
| U98_XCNVCR    | Char    | 10   | Convênio cartão                                        |
| U98_XVLRCO    | Numeric | 15,2 | Valor comercial                                        |
| U98_XFORCO    | Char    | 10   | Forma comercial                                        |
| U98_XCODPE    | Char    | 20   | Código do período                                      |
| U98_XNUMNE    | Char    | 20   | Número da negociação                                   |
| U98_TIPOBX    | Char    | 3    | Tipo/motivo de baixa                                   |
| U98_XJUROS    | Numeric | 15,2 | Juros (COBMAIS)                                        |
| U98_XMULTA    | Numeric | 15,2 | Multa (COBMAIS)                                        |
| U98_XCORRE    | Numeric | 15,2 | Correção monetária (COBMAIS)                           |
| U98_XDESCO    | Numeric | 15,2 | Desconto (COBMAIS)                                     |
| U98_A1NOME    | Char    | 40   | Nome do cliente (para inclusão automática em SA1)      |
| U98_A1NRED    | Char    | 20   | Nome reduzido do cliente                               |
| U98_A1CGC     | Char    | 14   | CNPJ/CPF do cliente                                    |
| U98_A1PESS    | Char    | 1    | Tipo de pessoa (F/J)                                   |
| U98_A1TIPO    | Char    | 1    | Tipo do cliente                                        |
| U98_A1END     | Char    | 40   | Endereço do cliente                                    |
| U98_A1BAIR    | Char    | 20   | Bairro do cliente                                      |
| U98_A1EST     | Char    | 2    | UF do cliente                                          |
| U98_A1ESTA    | Char    | 20   | Estado do cliente (extenso)                            |
| U98_A1CEP     | Char    | 8    | CEP do cliente                                         |
| U98_A1CDMU    | Char    | 7    | Código do município do cliente                         |
| U98_A1MUN     | Char    | 20   | Município do cliente                                   |
| U98_A1DDD     | Char    | 3    | DDD do cliente                                         |
| U98_A1TEL     | Char    | 15   | Telefone do cliente                                    |
| U98_A1EMAI    | Char    | 250  | E-mail do cliente                                      |
| U98_A1CDPA    | Char    | 3    | Código do país                                         |
| U98_A1PAIS    | Char    | 20   | País                                                   |
| U98_A1NATU    | Char    | 10   | Natureza financeira                                    |
| U98_OBS       | Char    | 250  | Observação / Mensagem do processamento                 |
| U98_CODOBS    | Char    | 1    | Status do processamento (''=Pendente, 1=OK, 2=Erro, 3=Aviso, 4=Erro Auto, 5=Cliente NF, 6=Manual, Z=Em proc.) |
| U98_DTOBS     | Date    | 8    | Data do último processamento                           |
| U98_HROBS     | Char    | 8    | Hora do último processamento                           |

**Chave Primária:** `U98_FILIAL + U98_PREFIX + U98_NUM + U98_PARCEL + U98_TIPO + U98_CLIENT`

**Índice de processamento:** `U98_FILIAL + U98_CODOBS + U98_TIPOIN + U98_VENCRE` (ORDER BY usado no Job)

---

## 7. Contratos / Fluig

---

### U13 — Stage de Medições Fluig — Contratos (Custom)

| Atributo       | Valor                                                         |
|----------------|---------------------------------------------------------------|
| **Módulo**     | Custom — Contratos (SIGAGCT) / Integração Fluig               |
| **Tipo**       | **Customizada**                                               |
| **Descrição**  | Stage de medições enviadas pelo Fluig para processamento no Protheus (inclusão de medição e geração de pré-nota) |
| **Uso no projeto** | GERMEDICAO.tlpp (Job de processamento de medições)        |

**Fluxo:** O Fluig popula a U13 com os dados da medição → o Job `GERMEDIC` lê os registros pendentes, aciona o modelo `CNTA121` para incluir a medição, encerra a medição e gera a pré-nota de entrada a partir do pedido de compra (SC7).

| Campo         | Tipo    | Tam. | Descrição                                                       |
|---------------|---------|------|-----------------------------------------------------------------|
| U13_FILIAL    | Char    | 8    | Filial                                                          |
| U13_CONTRA    | Char    | 15   | Número do contrato (mapeado para CNA_CONTRA / CND_CONTRA)       |
| U13_REVISA    | Char    | 3    | Revisão do contrato (mapeado para CND_REVISA)                   |
| U13_NFLUIG    | Char    | 10   | Número do chamado/documento no Fluig (chave de rastreio)        |
| U13_PLANIL    | Char    | 10   | Código da planilha do contrato (mapeado para CND_NUMERO)        |
| U13_COMPET    | Char    | 6    | Competência da medição (formato MMAAAA)                         |
| U13_PARCEL    | Char    | 2    | Parcela da medição                                              |
| U13_SERIE     | Char    | 3    | Série da nota fiscal de medição                                 |
| U13_NOTA      | Char    | 9    | Número da nota fiscal de medição                                |
| U13_EMISSA    | Char    | 8    | Data de emissão da nota fiscal (formato AAAAMMDD)               |
| U13_DTVENC    | Char    | 8    | Data de vencimento (formato AAAAMMDD)                           |
| U13_XCHVNF    | Char    | 44   | Chave da NF-e                                                   |
| U13_CONDPG    | Char    | 3    | Condição de pagamento                                           |
| U13_ESPECI    | Char    | 5    | Espécie do documento fiscal (ex.: SPED, NFS)                    |
| U13_NFAT      | Char    | 20   | Número da fatura                                                |
| U13_OBSMED    | Char    | 250  | Observação da medição (mapeado para CND_OBS)                    |
| U13_PRODUT    | Char    | 15   | Código do produto/serviço do item da planilha                   |
| U13_ITEM      | Char    | 4    | Número do item na planilha                                      |
| U13_QTD       | Numeric | 12,3 | Quantidade medida (mapeado para CNE_QUANT)                       |
| U13_VLUNIT    | Numeric | 15,2 | Valor unitário (mapeado para CNE_VLUNIT)                        |
| U13_TIPDOC    | Char    | 5    | Tipo do documento do pedido (mapeado para CNE_PEDTIT)           |
| U13_CCITEM    | Char    | 9    | Centro de custo do item (mapeado para CNE_CC)                   |
| U13_CLVLIT    | Char    | 9    | Classe de valor do item (mapeado para CNE_CLVL)                 |
| U13_NUMMED    | Char    | 10   | Número da medição gerada no Protheus                            |
| U13_CODOBS    | Char    | 1    | Status do processamento (''=Pendente, X=Processado, 1=Pré-nota OK, 2=Erro, 4=Erro pré-nota, Z=Reservado) |
| U13_OBS       | Char    | 250  | Observação / Mensagem do processamento                          |
| U13_DTOBS     | Date    | 8    | Data do processamento                                           |

**Chave Primária:** `U13_FILIAL + U13_NFLUIG + U13_ITEM`

**Índice de processamento:** `U13_FILIAL + U13_NFLUIG` (busca por número Fluig)

**Tabelas relacionadas:**
- **CN9** — Contratos (cabeçalho): via `U13_CONTRA + U13_REVISA`
- **SC7** — Pedidos de Compra: via número de pedido gerado na medição
- **SE2** — Títulos a Pagar: atualizado após encerramento da medição (`E2_XNFLUIG`)

---

## 8. Workflow / Outros

---

### U05 — Cadastro Workflow (Custom)

| Atributo       | Valor                                  |
|----------------|----------------------------------------|
| **Módulo**     | Custom — Workflow                      |
| **Tipo**       | **Customizada**                        |
| **Descrição**  | Cadastro de controle de Workflow       |
| **Uso no projeto** | F240OK.prw (código comentado)      |

> **Observação:** O uso desta tabela encontra-se comentado no código-fonte (`F240OK.prw`). Verificar se ainda está ativa no ambiente de produção.

---

## Observações Gerais

| # | Observação |
|---|------------|
| 1 | **SQL** em `SELECTTABLE.prw` é alias de resultado de query dinâmica, não é uma tabela física do dicionário de dados. |
| 2 | **MED** em `BCGPE007.prw` é alias da query `RetSqlName("SRD")`, não é uma tabela física. |
| 3 | Tabelas **U97**, **UA3** e **ZAZ** são de staging/integração e foram criadas para este projeto. |
| 4 | **DAYSPROCESSING** referenciada em `dash_integracao.tlpp` pode ser uma view ou tabela de data warehouse. Não é tabela padrão do Protheus. |
| 5 | Os tamanhos de campos indicados são estimativas baseadas no padrão TOTVS. Conferir os valores exatos via `SX3` no ambiente. |
| 6 | Tabelas **RGI**, **RCA**, **SRK**, **SR8**, **SRE** têm uso mais restrito; estrutura disponível no dicionário padrão via `SX3`. |
| 7 | **U98** é o stage de integração entre o sistema legado e o Contas a Receber (SE1/SA1). Campos prefixados `U98_A1*` contêm os dados do cliente para inclusão automática no SA1. |
| 8 | **U13** é populada pelo Fluig com os dados das medições de contratos. O Job `GERMEDIC` processa os registros e aciona o modelo `CNTA121` para inclusão da medição e geração de pré-nota. |

---

## Legenda

| Símbolo / Valor  | Significado                                  |
|------------------|----------------------------------------------|
| **Padrão TOTVS** | Tabela entregue pela TOTVS no pacote padrão  |
| **Customizada**  | Tabela criada especificamente para o projeto |
| `Char`           | Campo alfanumérico                           |
| `Numeric`        | Campo numérico                               |
| `Date`           | Campo data                                   |
| `Logical`        | Campo lógico (Sim/Não)                       |
| `MSBLQL = 1`     | Registro bloqueado/excluído logicamente      |

---

*Documento adaptado ao projeto MCP-REST-TLPP — Projeto PROTHEUS-ADVPL*

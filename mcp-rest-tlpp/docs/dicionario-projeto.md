# Dicionario do Projeto — PROTHEUS-ADVPL

Subset do projeto. Campos completos: tool `consultar_tabela_dicionario`.

---

## Financeiro — Contas a Receber / Cobrança

### SA1 — Clientes

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAFAT / SIGAFIN |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Cadastro de clientes |
| **Uso no projeto** | BBFIN41 (Prepare), M030INC, FA200FIL |

**Campos (265 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| A1_FILIAL | Char | 4 | 0 | Filial |
| A1_COD | Char | 6 | 0 | Codigo |
| A1_LOJA | Char | 2 | 0 | Loja |
| A1_PESSOA | Char | 1 | 0 | Fisica/Jurid |
| A1_NOME | Char | 50 | 0 | Nome |
| A1_NREDUZ | Char | 20 | 0 | N Fantasia |
| A1_END | Char | 40 | 0 | Endereco |
| A1_TIPO | Char | 1 | 0 | Tipo |
| A1_EST | Char | 2 | 0 | Estado |
| A1_ESTADO | Char | 20 | 0 | Nome Estado |
| A1_COD_MUN | Char | 5 | 0 | Cd.Municipio |
| A1_MUN | Char | 60 | 0 | Municipio |
| A1_BAIRRO | Char | 30 | 0 | Bairro |
| A1_XNATURE | Char | 10 | 0 | Dig Natureza |
| A1_NATUREZ | Char | 10 | 0 | Natureza |
| A1_IBGE | Char | 11 | 0 | Cod.IBGE |
| A1_CEP | Char | 8 | 0 | CEP |
| A1_DDD | Char | 3 | 0 | DDD |
| A1_DDI | Char | 6 | 0 | DDI |
| A1_TEL | Char | 15 | 0 | Telefone |
| A1_TELEX | Char | 10 | 0 | Telex |
| A1_FAX | Char | 15 | 0 | FAX |
| A1_PAIS | Char | 3 | 0 | Pais |
| A1_ENDCOB | Char | 40 | 0 | End.Cobranca |
| A1_PAISDES | Char | 25 | 0 | Descr. Pais |
| A1_ENDREC | Char | 40 | 0 | End.Recebto |
| A1_TRIBFAV | Char | 1 | 0 | Pes.Tri.Fav. |
| A1_ENDENT | Char | 40 | 0 | End.Entrega |
| A1_CONTATO | Char | 15 | 0 | Contato |
| A1_CGC | Char | 14 | 0 | CNPJ/CPF |
| A1_PFISICA | Char | 18 | 0 | RG/Ced.Estr. |
| A1_INSCR | Char | 18 | 0 | Ins. Estad. |
| A1_INSCRM | Char | 18 | 0 | Ins. Municip |
| A1_VEND | Char | 6 | 0 | Vendedor |
| A1_COMIS | Numeric | 5 | 2 | % Comissao |
| A1_REGIAO | Char | 3 | 0 | Regiao |
| A1_CONTA | Char | 20 | 0 | C. Contabil |
| A1_BCO1 | Char | 3 | 0 | Banco 1 |
| A1_BCO2 | Char | 3 | 0 | Banco 2 |
| A1_BCO3 | Char | 3 | 0 | Banco 3 |
| A1_BCO4 | Char | 3 | 0 | Banco 4 |
| A1_BCO5 | Char | 3 | 0 | Banco 5 |
| A1_TRANSP | Char | 6 | 0 | Transp. |
| A1_TPFRET | Char | 1 | 0 | Tipo Frete |
| A1_COND | Char | 3 | 0 | Cond. Pagto |
| A1_DESC | Numeric | 2 | 0 | Desconto |
| A1_PRIOR | Char | 1 | 0 | Prioridade |
| A1_RISCO | Char | 1 | 0 | Risco |
| A1_LC | Numeric | 14 | 2 | Lim. Credito |
| A1_VENCLC | Date | 8 | 0 | Venc.Lim.Cre |
| A1_CLASSE | Char | 1 | 0 | Classe Cred. |
| A1_LCFIN | Numeric | 14 | 2 | Lim Cred Sec |
| A1_MOEDALC | Numeric | 2 | 0 | Moeda do LC |
| A1_MSALDO | Numeric | 16 | 2 | Maior Saldo |
| A1_MCOMPRA | Numeric | 16 | 2 | Maior Compra |
| A1_METR | Numeric | 12 | 2 | Media Atraso |
| A1_PRICOM | Date | 8 | 0 | 1a Compra |
| A1_ULTCOM | Date | 8 | 0 | Ult. Compra |
| A1_NROCOM | Numeric | 5 | 0 | Nro Compras |
| A1_FORMVIS | Char | 3 | 0 | Form. Visita |
| A1_TEMVIS | Numeric | 3 | 0 | Freq.Visitas |
| A1_ULTVIS | Date | 8 | 0 | Ult. Visita |
| A1_TMPVIS | Char | 5 | 0 | Tempo Visita |
| A1_CLASVEN | Char | 1 | 0 | Classif.Vend |
| A1_TMPSTD | Char | 5 | 0 | Tempo Padrao |
| A1_MENSAGE | Char | 3 | 0 | Mensagem |
| A1_SALDUP | Numeric | 16 | 2 | Saldo Titulo |
| A1_RECISS | Char | 1 | 0 | Recolhe ISS |
| A1_NROPAG | Numeric | 4 | 0 | Nro Pagtos |
| A1_SALPEDL | Numeric | 16 | 2 | Sld Ped. Lib |
| A1_TRANSF | Char | 1 | 0 | Transf. Arq. |
| A1_SUFRAMA | Char | 12 | 0 | SUFRAMA |
| A1_ATR | Numeric | 16 | 2 | Atrasados |
| A1_VACUM | Numeric | 16 | 2 | Vlr.Acumul. |
| A1_SALPED | Numeric | 16 | 2 | Saldo Pedido |
| A1_TITPROT | Numeric | 3 | 0 | Tit.Protest. |
| A1_CHQDEVO | Numeric | 3 | 0 | Cheques Dev. |
| A1_DTULTIT | Date | 8 | 0 | Ult.Protesto |
| A1_MATR | Numeric | 4 | 0 | Maior Atraso |
| A1_DTULCHQ | Date | 8 | 0 | DT.Dev.Cheq. |

> +185 campos. Use consultar_tabela_dicionario("SA1").

**Chave primaria:** `SA1_FILIAL + SA1_COD + SA1_LOJA`

---

### SE1 — Títulos a Receber

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAFIN |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Títulos a receber (duplicatas/boletos) |
| **Uso no projeto** | FA200FIL (Cobrança) |

**Campos (320 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| E1_FILIAL | Char | 4 | 0 | Filial |
| E1_PREFIXO | Char | 3 | 0 | Prefixo |
| E1_NUM | Char | 9 | 0 | No. Titulo |
| E1_PARCELA | Char | 3 | 0 | Parcela |
| E1_TIPO | Char | 3 | 0 | Tipo |
| E1_NATUREZ | Char | 10 | 0 | Natureza |
| E1_PORTADO | Char | 3 | 0 | Portador |
| E1_AGEDEP | Char | 5 | 0 | Depositaria |
| E1_CLIENTE | Char | 6 | 0 | Cliente |
| E1_LOJA | Char | 2 | 0 | Loja |
| E1_NOMCLI | Char | 20 | 0 | Nome Cliente |
| E1_EMISSAO | Date | 8 | 0 | DT Emissao |
| E1_VENCTO | Date | 8 | 0 | Vencimento |
| E1_VENCREA | Date | 8 | 0 | Vencto real |
| E1_VALOR | Numeric | 16 | 2 | Vlr.Titulo |
| E1_BASEIRF | Numeric | 16 | 2 | Base Imposto |
| E1_IRRF | Numeric | 14 | 2 | IRRF |
| E1_ISS | Numeric | 14 | 2 | ISS |
| E1_NUMBCO | Char | 15 | 0 | Nº no Banco |
| E1_INDICE | Char | 3 | 0 | Reajuste |
| E1_BAIXA | Date | 8 | 0 | DT Baixa |
| E1_NUMBOR | Char | 6 | 0 | Num. Bordero |
| E1_DATABOR | Date | 8 | 0 | DT Bordero |
| E1_EMIS1 | Date | 8 | 0 | DT Contab. |
| E1_HIST | Char | 40 | 0 | Historico |
| E1_LA | Char | 1 | 0 | Ident. Lanc. |
| E1_LOTE | Char | 6 | 0 | Lote Contabl |
| E1_MOTIVO | Char | 20 | 0 | Motivo |
| E1_MOVIMEN | Date | 8 | 0 | Ult.Moviment |
| E1_OP | Char | 14 | 0 | Ord Producao |
| E1_SITUACA | Char | 1 | 0 | Situacao |
| E1_CONTRAT | Char | 15 | 0 | Contrato |
| E1_SALDO | Numeric | 16 | 2 | Saldo |
| E1_SUPERVI | Char | 6 | 0 | Supervisor |
| E1_VEND1 | Char | 6 | 0 | Vendedor 1 |
| E1_VEND2 | Char | 6 | 0 | Vendedor 2 |
| E1_VEND3 | Char | 6 | 0 | Vendedor 3 |
| E1_VEND4 | Char | 6 | 0 | Vendedor 4 |
| E1_VEND5 | Char | 6 | 0 | Vendedor 5 |
| E1_COMIS1 | Numeric | 6 | 2 | % Comissao 1 |
| E1_COMIS2 | Numeric | 6 | 2 | % Comissao 2 |
| E1_COMIS3 | Numeric | 6 | 2 | % Comissao 3 |
| E1_COMIS4 | Numeric | 6 | 2 | % Comissao 4 |
| E1_DESCONT | Numeric | 16 | 2 | Desconto |
| E1_COMIS5 | Numeric | 6 | 2 | % Comissao 5 |
| E1_MULTA | Numeric | 16 | 2 | Multa |
| E1_JUROS | Numeric | 16 | 2 | Juros |
| E1_CORREC | Numeric | 16 | 2 | Correcao |
| E1_VALLIQ | Numeric | 16 | 2 | Vlr.Liq Baix |
| E1_VENCORI | Date | 8 | 0 | Vencto Orig |
| E1_CONTA | Char | 10 | 0 | Num da Conta |
| E1_VALJUR | Numeric | 14 | 2 | Taxa Perman. |
| E1_PORCJUR | Numeric | 5 | 2 | Porc Juros |
| E1_MOEDA | Numeric | 2 | 0 | Moeda |
| E1_BASCOM1 | Numeric | 16 | 2 | Base Comis 1 |
| E1_BASCOM2 | Numeric | 16 | 2 | Base Comis 2 |
| E1_BASCOM3 | Numeric | 16 | 2 | Base Comis 3 |
| E1_BASCOM4 | Numeric | 16 | 2 | Base Comis 4 |
| E1_BASCOM5 | Numeric | 16 | 2 | Base Comis 5 |
| E1_FATPREF | Char | 3 | 0 | Pref. Fatura |
| E1_FATURA | Char | 9 | 0 | Fatura |
| E1_OK | Char | 2 | 0 | Iden.Selecao |
| E1_PROJETO | Char | 6 | 0 | Projeto |
| E1_CLASCON | Char | 5 | 0 | Classific. |
| E1_VALCOM1 | Numeric | 16 | 2 | Vlr. comis.1 |
| E1_VALCOM2 | Numeric | 16 | 2 | Vlr. comis.2 |
| E1_VALCOM3 | Numeric | 16 | 2 | Vlr. comis.3 |
| E1_VALCOM4 | Numeric | 16 | 2 | Vlr. comis.4 |
| E1_VALCOM5 | Numeric | 16 | 2 | Vlr. comis.5 |
| E1_OCORREN | Char | 2 | 0 | Cod Ocorrenc |
| E1_INSTR1 | Char | 2 | 0 | Inst.Primar. |
| E1_INSTR2 | Char | 2 | 0 | Instr.Secund |
| E1_PEDIDO | Char | 6 | 0 | No. Pedido |
| E1_DTVARIA | Date | 8 | 0 | Dt UIt.Var. |
| E1_VARURV | Numeric | 16 | 2 | Vlr.Variacao |
| E1_VLCRUZ | Numeric | 16 | 2 | Vlr R$ |
| E1_DTFATUR | Date | 8 | 0 | Data Faturam |
| E1_NUMNOTA | Char | 9 | 0 | Nota Fiscal |
| E1_SERIE | Char | 3 | 0 | Serie |
| E1_STATUS | Char | 1 | 0 | Status |

> +240 campos. Use consultar_tabela_dicionario("SE1").

**Chave primaria:** `E1_FILIAL + E1_PREFIXO + E1_NUM + E1_PARCELA + E1_TIPO + E1_CLIENTE + E1_LOJA`

---

### SE5 — Movimentação Contas a Receber

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAFIN |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Movimentação de contas a receber |
| **Uso no projeto** | F430BXA.PRW (ponto de entrada baixa) |

**Campos (109 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| E5_FILIAL | Char | 4 | 0 | Filial |
| E5_DATA | Date | 8 | 0 | DT Movimen |
| E5_TIPO | Char | 3 | 0 | Tipo Titulo |
| E5_MOEDA | Char | 2 | 0 | Numerario |
| E5_VALOR | Numeric | 16 | 2 | Vlr.Movim. |
| E5_NATUREZ | Char | 10 | 0 | Natureza |
| E5_BANCO | Char | 3 | 0 | Banco |
| E5_AGENCIA | Char | 5 | 0 | Agencia |
| E5_CONTA | Char | 10 | 0 | Conta Banco |
| E5_NUMCHEQ | Char | 15 | 0 | Num Cheque |
| E5_DOCUMEN | Char | 50 | 0 | Documento |
| E5_VENCTO | Date | 8 | 0 | Vencimento |
| E5_RECPAG | Char | 1 | 0 | Rec/Pag |
| E5_BENEF | Char | 30 | 0 | Beneficiario |
| E5_HISTOR | Char | 40 | 0 | Historico |
| E5_TIPODOC | Char | 2 | 0 | Tipo do Doc. |
| E5_VLMOED2 | Numeric | 14 | 2 | Vlr.Moeda 2 |
| E5_LA | Char | 2 | 0 | Ident.L.A. |
| E5_SITUACA | Char | 1 | 0 | Situacao |
| E5_LOTE | Char | 6 | 0 | Lote |
| E5_PREFIXO | Char | 3 | 0 | Prefixo |
| E5_NUMERO | Char | 9 | 0 | Titulo |
| E5_PARCELA | Char | 3 | 0 | Parcela |
| E5_CLIFOR | Char | 6 | 0 | Cli/For |
| E5_LOJA | Char | 2 | 0 | Loja |
| E5_DTDIGIT | Date | 8 | 0 | Data Digit. |
| E5_TIPOLAN | Char | 1 | 0 | Tipo Lanc. |
| E5_DEBITO | Char | 20 | 0 | Cta Debito |
| E5_CREDITO | Char | 20 | 0 | Cta Credito |
| E5_MOTBX | Char | 3 | 0 | MOT BAIXA |
| E5_RATEIO | Char | 1 | 0 | Rateio |
| E5_RECONC | Char | 1 | 0 | Reconciliado |
| E5_SEQ | Char | 2 | 0 | Sequencia |
| E5_DTDISPO | Date | 8 | 0 | Data Dispon |
| E5_CCD | Char | 20 | 0 | C.Custo Deb. |
| E5_CCC | Char | 20 | 0 | C.Custo Crd. |
| E5_OK | Char | 2 | 0 | Iden.Selecao |
| E5_ARQRAT | Char | 50 | 0 | Arq Rateio |
| E5_IDENTEE | Char | 6 | 0 | Ident Comp |
| E5_ORDREC | Char | 6 | 0 | Rec/Ordem |
| E5_FILORIG | Char | 4 | 0 | Filial Orig |
| E5_ARQCNAB | Char | 50 | 0 | Arq CNAB |
| E5_VLJUROS | Numeric | 16 | 2 | Valor juros |
| E5_VLMULTA | Numeric | 16 | 2 | Valor Multa |
| E5_VLCORRE | Numeric | 16 | 2 | Valor Correc |
| E5_VLDESCO | Numeric | 16 | 2 | Valor Descto |
| E5_CNABOC | Char | 2 | 0 | Ocorr CNAB |
| E5_SITUA | Char | 2 | 0 | Situacao Frt |
| E5_ITEMD | Char | 9 | 0 | Item Debito |
| E5_ITEMC | Char | 9 | 0 | Item Credito |
| E5_CLVLDB | Char | 9 | 0 | Cl Valor Deb |
| E5_CLVLCR | Char | 9 | 0 | Cl Valor Crd |
| E5_PROJPMS | Char | 10 | 0 | Projeto |
| E5_EDTPMS | Char | 12 | 0 | EDT |
| E5_TASKPMS | Char | 12 | 0 | Tarefa |
| E5_MODSPB | Char | 1 | 0 | Modalid. SPB |
| E5_TXMOEDA | Numeric | 11 | 4 | Tx moeda tit |
| E5_FATURA | Char | 9 | 0 | Fatura |
| E5_CODORCA | Char | 8 | 0 | Cod. Orcam. |
| E5_FATPREF | Char | 3 | 0 | Pref. Fatura |
| E5_SITCOB | Char | 1 | 0 | Sit.Cobranca |
| E5_FORNADT | Char | 6 | 0 | Forn. Adto. |
| E5_LOJAADT | Char | 2 | 0 | Loja Adto. |
| E5_CLIENTE | Char | 6 | 0 | Cliente |
| E5_FORNECE | Char | 6 | 0 | Fornecedor |
| E5_SERREC | Char | 3 | 0 | Serie Recibo |
| E5_OPERAD | Char | 6 | 0 | Operador |
| E5_MOVCX | Char | 1 | 0 | Mov.Caixinha |
| E5_KEY | Char | 50 | 0 | Chave Titulo |
| E5_MULTNAT | Char | 1 | 0 | Mult.Naturez |
| E5_AGLIMP | Char | 9 | 0 | Agl.Impostos |
| E5_VLACRES | Numeric | 16 | 2 | Valor Acresc |
| E5_VLDECRE | Numeric | 16 | 2 | Valor Decres |
| E5_VRETPIS | Numeric | 14 | 2 | Valor Rt PIS |
| E5_VRETCOF | Numeric | 14 | 2 | Valor Rt COF |
| E5_VRETCSL | Numeric | 14 | 2 | Valor Rt CSL |
| E5_PRETPIS | Char | 1 | 0 | Pend.Rt.PIS |
| E5_PRETCOF | Char | 1 | 0 | Pend.Rt.COF |
| E5_PRETCSL | Char | 1 | 0 | Pend.Rt.CSL |
| E5_AUTBCO | Char | 25 | 0 | Aut.Bancaria |

> +29 campos. Use consultar_tabela_dicionario("SE5").

**Chave primaria:** `E5_FILIAL + E5_PREFIXO + E5_NUM + E5_PARCELA + E5_TIPO + E5_CLIFOR + E5_LOJA + E5_DATA`

---

---

## Financeiro — Contas a Pagar

### SA2 — Fornecedores

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGACOM / SIGAFIN |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Cadastro de fornecedores |
| **Uso no projeto** | BBFIN21, BBAJUFOR, M020INC |

**Campos (255 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| A2_FILIAL | Char | 4 | 0 | Filial |
| A2_COD | Char | 6 | 0 | Código |
| A2_LOJA | Char | 2 | 0 | Loja |
| A2_TIPO | Char | 1 | 0 | Tipo |
| A2_CGC | Char | 14 | 0 | CNPJ/CPF |
| A2_NOME | Char | 50 | 0 | Razão Social |
| A2_NREDUZ | Char | 20 | 0 | N Fantasia |
| A2_XNOMCPL | Char | 100 | 0 | Nom Completo |
| A2_END | Char | 40 | 0 | Endereço |
| A2_CONTPRE | Char | 1 | 0 | Contrib.Prev |
| A2_NR_END | Char | 6 | 0 | Numero |
| A2_BAIRRO | Char | 20 | 0 | Bairro |
| A2_EST | Char | 2 | 0 | Estado |
| A2_ESTADO | Char | 20 | 0 | Nome Estado |
| A2_COD_MUN | Char | 5 | 0 | Cod. Municip |
| A2_MUN | Char | 60 | 0 | Munícipio |
| A2_PAIS | Char | 3 | 0 | Pais |
| A2_PAISDES | Char | 25 | 0 | Descr. Pais |
| A2_IBGE | Char | 11 | 0 | Cod.IBGE |
| A2_CEP | Char | 8 | 0 | CEP |
| A2_DDD | Char | 3 | 0 | DDD |
| A2_PFISICA | Char | 18 | 0 | RG/Ced.Estr. |
| A2_TEL | Char | 50 | 0 | Telefone |
| A2_INSCR | Char | 18 | 0 | Ins. Estad. |
| A2_INSCRM | Char | 18 | 0 | Ins. Municip |
| A2_DDI | Char | 6 | 0 | DDI |
| A2_FAX | Char | 15 | 0 | FAX |
| A2_EMAIL | Char | 100 | 0 | E-Mail |
| A2_MSBLQL | Char | 1 | 0 | Bloqueado |
| A2_SWIFT | Char | 30 | 0 | Swift |
| A2_NATUREZ | Char | 10 | 0 | Natureza |
| A2_CONTATO | Char | 15 | 0 | Contato |
| A2_CX_POST | Char | 5 | 0 | Caixa Postal |
| A2_BANCO | Char | 3 | 0 | Banco |
| A2_AGENCIA | Char | 5 | 0 | Cod Agencia |
| A2_DVAGE | Char | 1 | 0 | DV Ag Cnab |
| A2_NUMCON | Char | 10 | 0 | Cta Corrente |
| A2_DVCTA | Char | 2 | 0 | DV Cta Cnab |
| A2_TRANSP | Char | 6 | 0 | Transp. |
| A2_PRIOR | Char | 1 | 0 | Prioridade |
| A2_RISCO | Char | 3 | 0 | Risco |
| A2_COND | Char | 3 | 0 | Cond. Pagto |
| A2_LC | Char | 14 | 0 | Lim. Credito |
| A2_MATR | Numeric | 4 | 0 | Maior Atraso |
| A2_MCOMPRA | Numeric | 16 | 2 | Maior Compra |
| A2_ULTCOM | Date | 8 | 0 | Ult Compra |
| A2_CONTA | Char | 20 | 0 | C Contabil |
| A2_TIPORUR | Char | 1 | 0 | Tp.Contr.Soc |
| A2_METR | Numeric | 5 | 1 | Media Atraso |
| A2_MSALDO | Numeric | 16 | 2 | Maior Saldo |
| A2_PRICOM | Date | 8 | 0 | 1a Compra |
| A2_NROCOM | Numeric | 6 | 0 | No Compras |
| A2_ID_FBFN | Char | 7 | 0 | Identificac. |
| A2_STATUS | Char | 1 | 0 | Status |
| A2_GRUPO | Char | 3 | 0 | Grupo |
| A2_ATIVIDA | Char | 7 | 0 | Cod.Ativida. |
| A2_SALDUP | Numeric | 16 | 2 | Sld Duplict |
| A2_DESVIO | Numeric | 6 | 1 | Desvio |
| A2_SALDUPM | Numeric | 16 | 2 | Sld Moed.For |
| A2_RECISS | Char | 1 | 0 | Recolhe ISS |
| A2_REPRES | Char | 52 | 0 | Represent. |
| A2_REPCONT | Char | 50 | 0 | Contato Repr |
| A2_REPRTEL | Char | 50 | 0 | Tel. Repres. |
| A2_REPRFAX | Char | 30 | 0 | FAX Repres. |
| A2_DEPTO | Char | 30 | 0 | Departamento |
| A2_ORIG_1 | Char | 3 | 0 | Origem 1 |
| A2_ORIG_2 | Char | 3 | 0 | Origem 2 |
| A2_REPRMUN | Char | 30 | 0 | Cidade |
| A2_REPREST | Char | 2 | 0 | Estado Reprs |
| A2_REPRCEP | Char | 8 | 0 | CEP Repres. |
| A2_REPPAIS | Char | 3 | 0 | Pais Repres. |
| A2_ORIG_3 | Char | 3 | 0 | Origem 3 |
| A2_REPR_BA | Char | 3 | 0 | Bco. Repres. |
| A2_VINCULA | Char | 1 | 0 | Vinculacao |
| A2_REPR_EM | Char | 30 | 0 | E-Mail Repr. |
| A2_REPR_EN | Char | 52 | 0 | End.Repres. |
| A2_REPBAIR | Char | 30 | 0 | Bairro Repr. |
| A2_COMI_SO | Char | 1 | 0 | Tipo Comis. |
| A2_ID_REPR | Char | 1 | 0 | Identif.Repr |
| A2_REPR_AG | Char | 5 | 0 | Agenc. Repr. |

> +175 campos. Use consultar_tabela_dicionario("SA2").

**Chave primaria:** `SA2_FILIAL + SA2_COD + SA2_LOJA`

---

### SE2 — Títulos a Pagar

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAFIN |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Títulos a pagar (duplicatas a fornecedores) |
| **Uso no projeto** | U97Stagecpagar.tlpp (join com U97), dash_integracao.tlpp |

**Campos (282 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| E2_FILIAL | Char | 4 | 0 | Filial |
| E2_PREFIXO | Char | 3 | 0 | Prefixo |
| E2_NUM | Char | 9 | 0 | No. Titulo |
| E2_XNUMSP | Char | 10 | 0 | Número da SP |
| E2_XNFLUIG | Char | 10 | 0 | Num FLUIG |
| E2_PARCELA | Char | 3 | 0 | Parcela |
| E2_TIPO | Char | 3 | 0 | Tipo |
| E2_NUMBOR | Char | 6 | 0 | Num Bordero |
| E2_NATUREZ | Char | 10 | 0 | Natureza |
| E2_XCCUSTO | Char | 20 | 0 | Centro Custo |
| E2_PORTADO | Char | 3 | 0 | Portador |
| E2_FORNECE | Char | 6 | 0 | Fornecedor |
| E2_LOJA | Char | 2 | 0 | Loja |
| E2_NOMFOR | Char | 20 | 0 | Nome Fornece |
| E2_EMISSAO | Date | 8 | 0 | DT Emissao |
| E2_VENCTO | Date | 8 | 0 | Vencimento |
| E2_VENCREA | Date | 8 | 0 | Vencto Real |
| E2_VALOR | Numeric | 16 | 2 | Vlr.Titulo |
| E2_ISS | Numeric | 14 | 2 | ISS |
| E2_IRRF | Numeric | 14 | 2 | IRRF |
| E2_NUMBCO | Char | 15 | 0 | Nº do Cheque |
| E2_INDICE | Char | 3 | 0 | Reajuste |
| E2_BAIXA | Date | 8 | 0 | DT Baixa |
| E2_BCOPAG | Char | 3 | 0 | Bco de Pgto |
| E2_EMIS1 | Date | 8 | 0 | DT Contab. |
| E2_HIST | Char | 40 | 0 | Historico |
| E2_LA | Char | 1 | 0 | Ident. Lanc. |
| E2_LOTE | Char | 6 | 0 | Lote Contabl |
| E2_OK | Char | 2 | 0 | Ident.Baixa |
| E2_MOTIVO | Char | 20 | 0 | Motivo |
| E2_MOVIMEN | Date | 8 | 0 | Ult.Moviment |
| E2_OP | Char | 14 | 0 | Ord Producao |
| E2_SALDO | Numeric | 16 | 2 | Saldo |
| E2_DESCONT | Numeric | 16 | 2 | Desconto |
| E2_MULTA | Numeric | 16 | 2 | Multa |
| E2_JUROS | Numeric | 16 | 2 | Juros |
| E2_CORREC | Numeric | 16 | 2 | Correcao |
| E2_VALLIQ | Numeric | 14 | 2 | Val Liq Baix |
| E2_VENCORI | Date | 8 | 0 | Vencto Orig |
| E2_VALJUR | Numeric | 14 | 2 | Taxa Perman. |
| E2_PORCJUR | Numeric | 5 | 2 | Porc Juros |
| E2_MOEDA | Numeric | 2 | 0 | Moeda |
| E2_FATPREF | Char | 3 | 0 | Pref. Fatura |
| E2_FATURA | Char | 9 | 0 | Num Fatura |
| E2_PROJETO | Char | 6 | 0 | Projeto |
| E2_CLASCON | Char | 5 | 0 | Classific. |
| E2_RATEIO | Char | 1 | 0 | Rateio |
| E2_DTVARIA | Date | 8 | 0 | Dt.Ult.Var. |
| E2_VARURV | Numeric | 16 | 2 | Vl.Var.Acum. |
| E2_VLCRUZ | Numeric | 16 | 2 | Vlr R$ |
| E2_DTFATUR | Date | 8 | 0 | Data Faturam |
| E2_PARCIR | Char | 3 | 0 | Parc. IRF |
| E2_ARQRAT | Char | 30 | 0 | Arq Rateio |
| E2_ACRESC | Numeric | 16 | 2 | Acrescimo |
| E2_TITORIG | Char | 50 | 0 | Tit. Origem |
| E2_IDENTEE | Char | 6 | 0 | Ident CEC |
| E2_FLUXO | Char | 1 | 0 | Fluxo Caixa |
| E2_PARCISS | Char | 3 | 0 | Parc ISS |
| E2_IMPCHEQ | Char | 1 | 0 | Imp.Cheque |
| E2_OCORREN | Char | 2 | 0 | Ocorr CNAB |
| E2_ORIGEM | Char | 8 | 0 | Origem |
| E2_PARCINS | Char | 3 | 0 | Parc. INSS |
| E2_ORDPAGO | Char | 6 | 0 | Ordem Pagto |
| E2_DESDOBR | Char | 1 | 0 | Desdobramen. |
| E2_INSS | Numeric | 14 | 2 | INSS |
| E2_NUMLIQ | Char | 6 | 0 | No.Liquidaç. |
| E2_BCOCHQ | Char | 3 | 0 | Bco Cheque |
| E2_AGECHQ | Char | 5 | 0 | Agência Cheq |
| E2_CTACHQ | Char | 10 | 0 | Cta Cheque |
| E2_FLAGFAT | Char | 1 | 0 | Flag Faturas |
| E2_DATALIB | Date | 8 | 0 | Dt Aprov |
| E2_XHORLIB | Char | 8 | 0 | Hora Aprov. |
| E2_XNAPROV | Char | 100 | 0 | Aprovado Por |
| E2_APROVA | Char | 20 | 0 | Aprovador |
| E2_TIPOFAT | Char | 3 | 0 | Tipo Fatura |
| E2_ANOBASE | Char | 4 | 0 | Ano Base |
| E2_MESBASE | Char | 2 | 0 | Mes Base |
| E2_TXMOEDA | Numeric | 11 | 4 | Taxa moeda |
| E2_NUMTIT | Char | 50 | 0 | Tit IRRF Off |
| E2_SDACRES | Numeric | 16 | 2 | Sld.Acresc. |

> +202 campos. Use consultar_tabela_dicionario("SE2").

**Chave primaria:** `E2_FILIAL + E2_PREFIXO + E2_NUM + E2_PARCELA + E2_TIPO + E2_FORNECE + E2_LOJA`

---

### FIL — Contas Bancárias do Fornecedor

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAFIN |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Contas bancárias vinculadas a fornecedores |
| **Uso no projeto** | BBFIN21 |

**Campos (13 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| FIL_FILIAL | Char | 4 | 0 | Filial |
| FIL_FORNEC | Char | 6 | 0 | Fornecedor |
| FIL_LOJA | Char | 2 | 0 | Loja Ori. |
| FIL_BANCO | Char | 3 | 0 | Banco |
| FIL_AGENCI | Char | 5 | 0 | Agencia |
| FIL_CONTA | Char | 10 | 0 | Conta |
| FIL_DETRAC | Char | 1 | 0 | C. de Detrac |
| FIL_MOEDA | Numeric | 2 | 0 | Moeda |
| FIL_TIPO | Char | 1 | 0 | Tipo C/C |
| FIL_DVAGE | Char | 1 | 0 | DV Agência |
| FIL_DVCTA | Char | 2 | 0 | DV Conta |
| FIL_TIPCTA | Char | 1 | 0 | Tipo Conta |
| FIL_MOVCTO | Char | 1 | 0 | Permite C/C |
**Chave primaria:** `FIL_FILIAL + FIL_FORNECE + FIL_LOJA + FIL_BANCO + FIL_AGENCIA + FIL_CONTA`

---

---

## Contabilidade

### CTD — Plano de Contas / Itens Contábeis

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGACTB |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Plano de contas e itens contábeis |
| **Uso no projeto** | M020INC, M030INC |

**Campos (42 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| CTD_FILIAL | Char | 4 | 0 | Filial |
| CTD_ITEM | Char | 9 | 0 | Item Conta |
| CTD_CLASSE | Char | 1 | 0 | Classe |
| CTD_NORMAL | Char | 1 | 0 | Cond Normal |
| CTD_DESC01 | Char | 40 | 0 | Desc Moeda 1 |
| CTD_DESC02 | Char | 40 | 0 | Desc Moeda 2 |
| CTD_DESC03 | Char | 40 | 0 | Desc Moeda 3 |
| CTD_DESC04 | Char | 40 | 0 | Desc Moeda 4 |
| CTD_DESC05 | Char | 40 | 0 | Desc Moeda 5 |
| CTD_BLOQ | Char | 1 | 0 | Item Bloq |
| CTD_DTBLIN | Date | 8 | 0 | Dt Ini Bloq |
| CTD_DTBLFI | Date | 8 | 0 | Dt Fim Bloq |
| CTD_DTEXIS | Date | 8 | 0 | Dt Ini Exist |
| CTD_DTEXSF | Date | 8 | 0 | Dt Fim Exist |
| CTD_ITLP | Char | 9 | 0 | Item L/P |
| CTD_ITPON | Char | 9 | 0 | Item Ponte |
| CTD_BOOK | Char | 20 | 0 | Conf. Livros |
| CTD_ITSUP | Char | 9 | 0 | Item Superi |
| CTD_RES | Char | 10 | 0 | Cod Red.Item |
| CTD_CRGNV1 | Char | 12 | 0 | Cnt Reg Niv1 |
| CTD_CRGNV2 | Char | 12 | 0 | Cnt Reg Niv2 |
| CTD_RGNV3 | Char | 12 | 0 | Regra Nivel3 |
| CTD_CLOBRG | Char | 1 | 0 | Cl.Vlr Obrig |
| CTD_ACCLVL | Char | 1 | 0 | Ac.Cl.Valor |
| CTD_ITVM | Char | 9 | 0 | It.Var.Monet |
| CTD_ITRED | Char | 9 | 0 | It.Red.V.Mon |
| CTD_ACATIV | Char | 1 | 0 | Ac.Outra At? |
| CTD_ATOBRG | Char | 1 | 0 | Outr.At.Ob? |
| CTD_ACAT01 | Char | 1 | 0 | Ativ.01 Ac. |
| CTD_AT01OB | Char | 1 | 0 | Ativ.01 Ob. |
| CTD_ACAT02 | Char | 1 | 0 | Ativ.02 Ac. |
| CTD_AT02OB | Char | 1 | 0 | Ativ.02 Ob. |
| CTD_ACAT03 | Char | 1 | 0 | Ativ.03 Ac. |
| CTD_AT03OB | Char | 1 | 0 | Ativ.03 Ob. |
| CTD_ACAT04 | Char | 1 | 0 | Ativ.04 Ac. |
| CTD_AT04OB | Char | 1 | 0 | Ativ.04 Ob. |
| CTD_TPO04 | Char | 2 | 0 | Tipo Ctb 04 |
| CTD_TPO03 | Char | 2 | 0 | Tipo Ctb 03 |
| CTD_TPO02 | Char | 2 | 0 | Tipo Ctb 02 |
| CTD_TPO01 | Char | 2 | 0 | Tipo Ctb 01 |
| CTD_DESC06 | Char | 40 | 0 | Desc Moeda 6 |
| CTD_DESC07 | Char | 40 | 0 | Desc Moeda 7 |
**Chave primaria:** `CTD_FILIAL + CTD_ITEM`

---

### CTT — Centros de Custo

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGACTB |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Centros de custo contábeis |
| **Uso no projeto** | recibo.PRX, INTEGRACAO_APPUS.tlpp, fRel005.prw |

**Campos (96 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| CTT_FILIAL | Char | 4 | 0 | Filial |
| CTT_CUSTO | Char | 20 | 0 | C Custo |
| CTT_CLASSE | Char | 1 | 0 | Classe |
| CTT_NORMAL | Char | 1 | 0 | Cond Normal |
| CTT_DESC01 | Char | 40 | 0 | Desc Moeda 1 |
| CTT_DESC02 | Char | 40 | 0 | Desc Moeda 2 |
| CTT_DESC03 | Char | 40 | 0 | Desc Moeda 3 |
| CTT_DESC04 | Char | 40 | 0 | Desc Moeda 4 |
| CTT_DESC05 | Char | 40 | 0 | Desc Moeda 5 |
| CTT_BLOQ | Char | 1 | 0 | CC Bloq |
| CTT_DTBLIN | Date | 8 | 0 | Dt Ini Bloq |
| CTT_DTBLFI | Date | 8 | 0 | Dt Fim Bloq |
| CTT_DTEXIS | Date | 8 | 0 | Dt Ini Exist |
| CTT_DTEXSF | Date | 8 | 0 | Dt Fim Exist |
| CTT_CCLP | Char | 20 | 0 | CC Lucr/Perd |
| CTT_CCPON | Char | 20 | 0 | CC Ponte LP |
| CTT_TIPO00 | Char | 2 | 0 | Tipo Terc. |
| CTT_BOOK | Char | 20 | 0 | Conf. Livros |
| CTT_TIPO01 | Char | 2 | 0 | Tp Doc Ter. |
| CTT_CCSUP | Char | 20 | 0 | CC Superior |
| CTT_RES | Char | 10 | 0 | Cod Red. CC. |
| CTT_CRGNV1 | Char | 12 | 0 | Cnt Reg Niv1 |
| CTT_RGNV2 | Char | 12 | 0 | Regra Nivel2 |
| CTT_RGNV3 | Char | 12 | 0 | Regra Nivel3 |
| CTT_STATUS | Char | 1 | 0 | Status |
| CTT_FILMAT | Char | 4 | 0 | Fil.Respons. |
| CTT_MAT | Char | 6 | 0 | Cod.Respons. |
| CTT_LOCAL | Char | 2 | 0 | Almoxarifado |
| CTT_ITOBRG | Char | 1 | 0 | Item Obrigat |
| CTT_CLOBRG | Char | 1 | 0 | Cl.Vlr Obrig |
| CTT_ACITEM | Char | 1 | 0 | Aceita Item |
| CTT_ACCLVL | Char | 1 | 0 | Aceita Cl.Vl |
| CTT_CCVM | Char | 20 | 0 | C.C.Var.Mon. |
| CTT_CCRED | Char | 20 | 0 | CC.Red. Var. |
| CTT_CSINCO | Char | 1 | 0 | C. Sinco |
| CTT_OPERAC | Char | 3 | 0 | Operacao |
| CTT_ACATIV | Char | 1 | 0 | Ac.Outra At? |
| CTT_ATOBRG | Char | 1 | 0 | Outr.At.Ob? |
| CTT_ACAT01 | Char | 1 | 0 | Ativ.01 Ac. |
| CTT_AT01OB | Char | 1 | 0 | Ativ.01 Ob. |
| CTT_ACAT02 | Char | 1 | 0 | Ativ.02 Ac. |
| CTT_AT02OB | Char | 1 | 0 | Ativ.02 Ob. |
| CTT_ACAT03 | Char | 1 | 0 | Ativ.03 Ac. |
| CTT_AT03OB | Char | 1 | 0 | Ativ.03 Ob. |
| CTT_ACAT04 | Char | 1 | 0 | Ativ.04 Ac. |
| CTT_AT04OB | Char | 1 | 0 | Ativ.04 Ob. |
| CTT_RHEXP | Char | 6 | 0 | Contr.Exp.RH |
| CTT_TPO01 | Char | 2 | 0 | Tipo Ctb 01 |
| CTT_TPO02 | Char | 2 | 0 | Tipo Ctb 02 |
| CTT_TPO03 | Char | 2 | 0 | Tipo Ctb 03 |
| CTT_TPO04 | Char | 2 | 0 | Tipo Ctb 04 |
| CTT_INTRES | Char | 1 | 0 | Int. Reserve |
| CTT_RESERV | Char | 1 | 0 | Sinc Reserve |
| CTT_DESC06 | Char | 40 | 0 | Desc Moeda 6 |
| CTT_DESC07 | Char | 40 | 0 | Desc Moeda 7 |
| CTT_XNCOMP | Char | 200 | 0 | Nom Completo |
| CTT_TPLOT | Char | 2 | 0 | Tipo Lotação |
| CTT_DTPLO | Char | 100 | 0 | Desc.Lotação |
| CTT_NOME | Char | 40 | 0 | Nome Tomador |
| CTT_TIPO | Char | 1 | 0 | T.Insc.Tomad |
| CTT_CEI | Char | 14 | 0 | CNPJ/CEI Tom |
| CTT_TIPO2 | Char | 1 | 0 | Tp eSocial |
| CTT_CEI2 | Char | 14 | 0 | Insc eSocial |
| CTT_ENDER | Char | 40 | 0 | End.Tomador |
| CTT_BAIRRO | Char | 20 | 0 | Bair.Tomador |
| CTT_CEP | Char | 8 | 0 | Cep Tomador |
| CTT_ESTADO | Char | 2 | 0 | Estado |
| CTT_CODMUN | Char | 7 | 0 | Cod.Munic. |
| CTT_MUNIC | Char | 20 | 0 | Mun.Tomador |
| CTT_FPAS | Char | 3 | 0 | Cód. FPAS |
| CTT_CODTER | Char | 4 | 0 | Terc FPAS |
| CTT_PEREMP | Numeric | 8 | 4 | % Empresa |
| CTT_PERFPA | Numeric | 7 | 3 | % Terceiros |
| CTT_PERCAC | Numeric | 8 | 4 | % Acid.Trab. |
| CTT_EMAIL | Char | 60 | 0 | E-mail Resp. |
| CTT_PERRAT | Numeric | 6 | 4 | % RAT |
| CTT_DESCRI | Char | 100 | 0 | Escritório |
| CTT_FAP | Numeric | 6 | 4 | Fat.Acd.Prev |
| CTT_CESCRI | Char | 5 | 0 | Cód. Escrit |
| CTT_OCORRE | Char | 2 | 0 | Ocorrencia |

> +16 campos. Use consultar_tabela_dicionario("CTT").

**Chave primaria:** `CTT_FILIAL + CTT_CUSTO`

---

### CTF — Lançamentos Contábeis

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGACTB |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Lançamentos do livro-razão contábil |
| **Uso no projeto** | BBCTB01.PRW |

**Campos (7 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| CTF_FILIAL | Char | 4 | 0 | Filial |
| CTF_DOC | Char | 6 | 0 | Nro Documen |
| CTF_LOTE | Char | 6 | 0 | Nro Lote |
| CTF_SBLOTE | Char | 3 | 0 | Sub-Lote |
| CTF_DATA | Date | 8 | 0 | Data |
| CTF_LINHA | Char | 3 | 0 | Ult Linha |
| CTF_USADO | Char | 1 | 0 | Doc Usado |
**Chave primaria:** `CF_FILIAL + CF_LOTE + CF_SUBLOTE`

---

### SI3 — Centros de Custo (Descrição Complementar)

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGACTB / SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Descrição complementar de CC |
| **Uso no projeto** | recibo.PRX |

**Campos (67 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| I3_FILIAL | Char | 4 | 0 | Filial |
| I3_CUSTO | Char | 20 | 0 | Cod Custo |
| I3_CONTA | Char | 20 | 0 | Cod Conta |
| I3_MOEDA | Char | 1 | 0 | Moeda |
| I3_DESC | Char | 25 | 0 | Desc CCusto |
| I3_SALINI | Numeric | 16 | 2 | Saldo Inic |
| I3_DEB01 | Numeric | 16 | 2 | Deb Per 01 |
| I3_CRE01 | Numeric | 16 | 2 | Cred Per 01 |
| I3_DEB02 | Numeric | 16 | 2 | Deb Per 02 |
| I3_CRE02 | Numeric | 16 | 2 | Cred Per 02 |
| I3_DEB03 | Numeric | 16 | 2 | Deb Per 03 |
| I3_CRE03 | Numeric | 16 | 2 | Cred Per 03 |
| I3_DEB04 | Numeric | 16 | 2 | Deb Per 04 |
| I3_CRE04 | Numeric | 16 | 2 | Cred Per 04 |
| I3_DEB05 | Numeric | 16 | 2 | Deb Per 05 |
| I3_CRE05 | Numeric | 16 | 2 | Cred Per 05 |
| I3_DEB06 | Numeric | 16 | 2 | Deb Per 06 |
| I3_CRE06 | Numeric | 16 | 2 | Cred Per 06 |
| I3_DEB07 | Numeric | 16 | 2 | Deb Per 07 |
| I3_CRE07 | Numeric | 16 | 2 | Cred Per 07 |
| I3_DEB08 | Numeric | 16 | 2 | Deb Per 08 |
| I3_CRE08 | Numeric | 16 | 2 | Cred Per 08 |
| I3_DEB09 | Numeric | 16 | 2 | Deb Per 09 |
| I3_CRE09 | Numeric | 16 | 2 | Cred Per 09 |
| I3_DEB10 | Numeric | 16 | 2 | Deb Per 10 |
| I3_CRE10 | Numeric | 16 | 2 | Cred Per 10 |
| I3_DEB11 | Numeric | 16 | 2 | Deb Per 11 |
| I3_CRE11 | Numeric | 16 | 2 | Cred Per 11 |
| I3_DEB12 | Numeric | 16 | 2 | Deb Per 12 |
| I3_CRE12 | Numeric | 16 | 2 | Cred Per 12 |
| I3_DEB13 | Numeric | 16 | 2 | Deb Per 13 |
| I3_CRE13 | Numeric | 16 | 2 | Cred Per 13 |
| I3_DEB14 | Numeric | 16 | 2 | Deb Per 14 |
| I3_CRE14 | Numeric | 16 | 2 | Cred Per 14 |
| I3_DEB15 | Numeric | 16 | 2 | Deb Per 15 |
| I3_CRE15 | Numeric | 16 | 2 | Cred Per 15 |
| I3_DEB16 | Numeric | 16 | 2 | Deb Per 16 |
| I3_CRE16 | Numeric | 16 | 2 | Cred Per 16 |
| I3_DEB17 | Numeric | 16 | 2 | Deb Per 17 |
| I3_CRE17 | Numeric | 16 | 2 | Cred Per 17 |
| I3_PERCACI | Numeric | 8 | 4 | % Acid.Trab. |
| I3_DESCEST | Char | 25 | 0 | Desc Estrang |
| I3_PERFPAS | Numeric | 7 | 3 | % Terceiros |
| I3_PERLP | Char | 6 | 0 | Periodo LP |
| I3_STATUS | Char | 1 | 0 | Status |
| I3_VLRLPD | Numeric | 16 | 2 | Vlr LP Debit |
| I3_FILMAT | Char | 4 | 0 | Fil.Respons |
| I3_VLRLPC | Numeric | 16 | 2 | Vlr LP Credt |
| I3_MAT | Char | 6 | 0 | Cod.Respons. |
| I3_NMAT | Char | 40 | 0 | Nom.Respons. |
| I3_NOME | Char | 40 | 0 | Nome Tomador |
| I3_ENDEREC | Char | 40 | 0 | End. Tomador |
| I3_BAIRRO | Char | 20 | 0 | Bair.Tomador |
| I3_CEP | Char | 8 | 0 | Cep  Tomador |
| I3_MUNICIP | Char | 20 | 0 | Mun.Tomador |
| I3_ESTADO | Char | 2 | 0 | Estado |
| I3_TIPO | Char | 1 | 0 | T.Insc.Tomad |
| I3_CEI | Char | 14 | 0 | CNPJ/CEI Tom |
| I3_VALFAT | Numeric | 12 | 2 | Vlr.Fatura |
| I3_RETIDO | Numeric | 12 | 2 | Vlr.Retido |
| I3_LOCAL | Char | 2 | 0 | Almoxarifado |
| I3_OCORREN | Char | 2 | 0 | Ocorrencia |
| I3_OPERAC | Char | 3 | 0 | Operacao |
| I3_DTEXIS | Date | 8 | 0 | Dt.Ini.Exis. |
| I3_CODMUN | Char | 7 | 0 | Cod.Munic. |
| I3_PEREMP | Numeric | 8 | 4 | % Empresa |
| I3_RECFAT | Char | 1 | 0 | Rec.Fatur. |
**Chave primaria:** `I3_FILIAL + I3_CCUSTO`

---

---

## Folha de Pagamento / RH (SIGAGPE)

### SRA — Funcionários

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Cadastro de funcionários |
| **Uso no projeto** | recibo.PRX, BCGPE007, INTEGRACAO_APPUS.tlpp, PROCU16.TLPP |

**Campos (358 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| RA_FILIAL | Char | 4 | 0 | Filial |
| RA_MAT | Char | 6 | 0 | Matricula |
| RA_CC | Char | 20 | 0 | Centro Custo |
| RA_DESCCC | Char | 20 | 0 | Descr.CCusto |
| RA_NOME | Char | 30 | 0 | Nome |
| RA_ITEM | Char | 9 | 0 | Item |
| RA_CLVL | Char | 9 | 0 | Classe Valor |
| RA_CIC | Char | 11 | 0 | CPF |
| RA_PIS | Char | 12 | 0 | P.I.S. |
| RA_RG | Char | 15 | 0 | R.G. |
| RA_TIPENDE | Char | 1 | 0 | Tip.Endereço |
| RA_COMPLRG | Char | 20 | 0 | Complem. RG |
| RA_NUMCP | Char | 7 | 0 | Cart.Profis. |
| RA_SERCP | Char | 5 | 0 | Série Cart. |
| RA_UFCP | Char | 2 | 0 | UF Cart.Prof |
| RA_HABILIT | Char | 11 | 0 | Cart.Habil. |
| RA_NOMECMP | Char | 70 | 0 | Nome complet |
| RA_TITULOE | Char | 12 | 0 | Tit.Eleit. |
| RA_ENDEREC | Char | 30 | 0 | Endereço |
| RA_RESEXT | Char | 1 | 0 | Res.Exterior |
| RA_ZONASEC | Char | 8 | 0 | Zona Eleit. |
| RA_NUMENDE | Char | 6 | 0 | Num.Endereço |
| RA_LOGRTP | Char | 4 | 0 | Tipo Lograd |
| RA_COMPLEM | Char | 15 | 0 | Compl.Ender. |
| RA_BAIRRO | Char | 15 | 0 | Bairro |
| RA_ESTADO | Char | 2 | 0 | Estado |
| RA_SECAO | Char | 4 | 0 | Seção Eleit. |
| RA_LOGRTPD | Char | 10 | 0 | Des.Tp.Logr |
| RA_MUNICIP | Char | 20 | 0 | Municipio |
| RA_LOGRDSC | Char | 80 | 0 | Descr.Lograd |
| RA_CEP | Char | 8 | 0 | Cep |
| RA_CPOSTAL | Char | 9 | 0 | Caixa Postal |
| RA_LOGRNUM | Char | 10 | 0 | NrLogradouro |
| RA_ALTEND | Char | 1 | 0 | Alterou End. |
| RA_DDDFONE | Char | 2 | 0 | DDD Telefone |
| RA_CODMUN | Char | 5 | 0 | Cod Municip |
| RA_TELEFON | Char | 20 | 0 | Telefone |
| RA_DDDCELU | Char | 2 | 0 | DDD Celular |
| RA_NUMCELU | Char | 10 | 0 | Num. Celular |
| RA_CODMUNE | Char | 80 | 0 | Nom Municip |
| RA_NATURAL | Char | 2 | 0 | Naturalidade |
| RA_DDDRESP | Char | 2 | 0 | DDD Num Resp |
| RA_NUMRESP | Char | 10 | 0 | Num Responsa |
| RA_MAE | Char | 40 | 0 | Nome Mae |
| RA_PAI | Char | 40 | 0 | Nome Pai |
| RA_NACIONA | Char | 2 | 0 | Nacionalid. |
| RA_ESTCIVI | Char | 1 | 0 | Est. Civil |
| RA_SEXO | Char | 1 | 0 | Sexo |
| RA_ANOCHEG | Char | 2 | 0 | Ano Chegada |
| RA_DEPIR | Char | 2 | 0 | Dep. I.R. |
| RA_DEPSF | Char | 2 | 0 | Dep.Sal.Fam. |
| RA_SITFOLH | Char | 1 | 0 | Sit. Folha |
| RA_NASC | Date | 8 | 0 | Data Nasc. |
| RA_CEPCXPO | Char | 8 | 0 | CEP C.Postal |
| RA_ALTNASC | Char | 1 | 0 | Alt.Dt. Nasc |
| RA_ADMISSA | Date | 8 | 0 | Data Admis. |
| RA_CHAPA | Char | 5 | 0 | Cod. Chapa |
| RA_MUNNASC | Char | 30 | 0 | Municp.Nasc. |
| RA_OPCAO | Date | 8 | 0 | Dt.Op.FGTS |
| RA_LOCBNF | Char | 4 | 0 | Local Benef. |
| RA_CODMUNN | Char | 5 | 0 | Cod Mun Nasc |
| RA_BRNASEX | Char | 1 | 0 | Bra.Nasc.Ext |
| RA_TNOTRAB | Char | 3 | 0 | Turno Trab. |
| RA_DESCTUR | Char | 50 | 0 | Desc.Turno |
| RA_DEMISSA | Date | 8 | 0 | Dt. Demissao |
| RA_VCTOEXP | Date | 8 | 0 | Ven. Exper.1 |
| RA_CODFUNC | Char | 5 | 0 | Cod. Funcao |
| RA_DESCFUN | Char | 20 | 0 | Desc.Funcao |
| RA_CPAISOR | Char | 5 | 0 | Cod.Pais Ori |
| RA_VCTEXP2 | Date | 8 | 0 | Vc.Exp.2Per. |
| RA_PAISORI | Char | 20 | 0 | País Origem |
| RA_EXAMEDI | Date | 8 | 0 | Ven.Exa.Med. |
| RA_CBO | Char | 5 | 0 | C.B.O.  1994 |
| RA_CODCBO | Char | 6 | 0 | C.B.O. 2002 |
| RA_PGCTSIN | Char | 1 | 0 | Con.Sindical |
| RA_BCDEPSA | Char | 8 | 0 | Bco.Ag.D.Sal |
| RA_ALTCBO | Char | 1 | 0 | Alt. CBO |
| RA_CTDEPSA | Char | 12 | 0 | Cta.Dep.Sal. |
| RA_SINDICA | Char | 2 | 0 | C. Sindicato |
| RA_PROCES | Char | 5 | 0 | Cod Processo |

> +278 campos. Use consultar_tabela_dicionario("SRA").

**Chave primaria:** `RA_FILIAL + RA_MAT`

---

### SRC — Verbas de Competência

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Verbas fixas/variáveis por competência |
| **Uso no projeto** | recibo.PRX |

**Campos (42 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| RC_FILIAL | Char | 4 | 0 | Filial |
| RC_MAT | Char | 6 | 0 | Matricula |
| RC_NOME | Char | 30 | 0 | Nome |
| RC_PD | Char | 3 | 0 | Codigo Verba |
| RC_DESCPD | Char | 20 | 0 | Descricao |
| RC_TIPO1 | Char | 1 | 0 | Tipo |
| RC_QTDSEM | Numeric | 9 | 2 | Aulas Semana |
| RC_HORINFO | Numeric | 6 | 2 | Horas Inform |
| RC_HORAS | Numeric | 8 | 2 | Horas Lanc. |
| RC_VALINFO | Numeric | 12 | 2 | Valor Inform |
| RC_VALOR | Numeric | 12 | 2 | Vlr. Lancam. |
| RC_VNAOAPL | Numeric | 12 | 2 | Vl Nao Aplic |
| RC_DATA | Date | 8 | 0 | Dt. Pagto. |
| RC_DTREF | Date | 8 | 0 | Dt. Ref. |
| RC_SEMANA | Char | 2 | 0 | Nro. Semana |
| RC_CC | Char | 20 | 0 | Centro Custo |
| RC_PARCELA | Numeric | 2 | 0 | Nr. Parcelas |
| RC_TIPO2 | Char | 1 | 0 | Origem |
| RC_SEQ | Char | 1 | 0 | Seq. Verba |
| RC_VALORBA | Numeric | 12 | 2 | Valor Base |
| RC_PROCES | Char | 5 | 0 | Cod Processo |
| RC_PERIODO | Char | 6 | 0 | Cod. Periodo |
| RC_POSTO | Char | 9 | 0 | Cod. Posto |
| RC_NUMID | Char | 26 | 0 | Num.Identif. |
| RC_ROTEIR | Char | 3 | 0 | Roteiro |
| RC_DEPTO | Char | 9 | 0 | Cod. Depto. |
| RC_NODIA | Char | 10 | 0 | Seq. Diario |
| RC_DIACTB | Char | 2 | 0 | Cod. Diario |
| RC_ITEM | Char | 9 | 0 | Item |
| RC_CLVL | Char | 9 | 0 | Classe Valor |
| RC_EMPCONS | Char | 1 | 0 | Emp. Cons. |
| RC_IDCMPL | Char | 6 | 0 | ID. Comp. |
| RC_PLNUCO | Char | 12 | 0 | Nr. Cobranca |
| RC_CODB1T | Char | 12 | 0 | Seq. Lancto. |
| RC_LOTPLS | Char | 10 | 0 | Lote Pls |
| RC_CODRDA | Char | 6 | 0 | Cod.RDA.Pag. |
| RC_CONVOC | Char | 6 | 0 | Cod. Covoc |
| RC_SEQMV | Char | 1 | 0 | Seq.Calc. MV |
| RC_NRBEN | Char | 20 | 0 | Nr. Benef. |
| RC_IN2110 | Char | 1 | 0 | IN 2110 |
| RC_TRIBIR | Char | 1 | 0 | Trib. IR |
| RC_FERSUB | Char | 3 | 0 | Vb Subs. Fer |
**Chave primaria:** `RC_FILIAL + RC_MAT + RC_COMPETENCIA + RC_CODVB`

---

### SRD — Verbas de Débito (Folha)

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Verbas de débito calculadas na folha |
| **Uso no projeto** | recibo.PRX, BCGPE007 |

**Campos (50 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| RD_FILIAL | Char | 4 | 0 | Filial |
| RD_MAT | Char | 6 | 0 | Matricula |
| RD_PD | Char | 3 | 0 | Codigo Verba |
| RD_DESCPD | Char | 20 | 0 | Descricao |
| RD_TIPO1 | Char | 1 | 0 | Tipo |
| RD_QTDSEM | Numeric | 9 | 2 | Aulas Semana |
| RD_HORINFO | Numeric | 9 | 2 | Horas Inform |
| RD_HORAS | Numeric | 9 | 2 | Horas/Dias |
| RD_VALINFO | Numeric | 12 | 2 | Valor Inform |
| RD_VALOR | Numeric | 12 | 2 | Valor |
| RD_VNAOAPL | Numeric | 12 | 2 | Vl Nao Aplic |
| RD_DATARQ | Char | 6 | 0 | Dt.Arq. |
| RD_DATPGT | Date | 8 | 0 | Dt.Pagamento |
| RD_CC | Char | 20 | 0 | Centro Custo |
| RD_SEQ | Char | 1 | 0 | Seq. Verba |
| RD_EMPRESA | Char | 2 | 0 | Empresa |
| RD_TIPO2 | Char | 1 | 0 | Origem |
| RD_MES | Char | 2 | 0 | Dez.Mes.Acum |
| RD_VSTATUS | Char | 10 | 0 | Status |
| RD_STATUS | Char | 1 | 0 | A/M/I |
| RD_INSS | Char | 1 | 0 | INSS |
| RD_IR | Char | 1 | 0 | IRRF |
| RD_FGTS | Char | 1 | 0 | FGTS |
| RD_PROCES | Char | 5 | 0 | Cod Processo |
| RD_PERIODO | Char | 6 | 0 | Cod. Periodo |
| RD_SEMANA | Char | 2 | 0 | Semana |
| RD_ROTEIR | Char | 3 | 0 | Roteiro |
| RD_DTREF | Date | 8 | 0 | Dt. Refer. |
| RD_POSTO | Char | 9 | 0 | Cod. Posto |
| RD_NUMID | Char | 26 | 0 | Num. Identif |
| RD_DEPTO | Char | 9 | 0 | Cod. Depto. |
| RD_NODIA | Char | 10 | 0 | Seq. Diario |
| RD_DIACTB | Char | 2 | 0 | Cod. Diario |
| RD_PLNUCO | Char | 12 | 0 | Nr. Cobranca |
| RD_CODB1T | Char | 12 | 0 | Seq. Lancto. |
| RD_ITEM | Char | 9 | 0 | Item |
| RD_CLVL | Char | 9 | 0 | Classe Valor |
| RD_EMPCONS | Char | 1 | 0 | Emp. Cons. |
| RD_IDCMPL | Char | 6 | 0 | ID. Comp. |
| RD_CRITER | Char | 2 | 0 | Critério Ac. |
| RD_SEQUE | Char | 2 | 0 | Seq. Acum. |
| RD_LOTPLS | Char | 10 | 0 | Lote Pls |
| RD_CODRDA | Char | 6 | 0 | Cod.RDA.Pag. |
| RD_VALORBA | Numeric | 12 | 2 | Valor Base |
| RD_CONVOC | Char | 6 | 0 | Cod. Convoc. |
| RD_SEQMV | Char | 1 | 0 | Seq.Calc. MV |
| RD_NRBEN | Char | 20 | 0 | Nr. Benef. |
| RD_IN2110 | Char | 1 | 0 | IN 2110 |
| RD_TRIBIR | Char | 1 | 0 | Trib. IR |
| RD_FERSUB | Char | 3 | 0 | Vb Subs. Fer |
**Chave primaria:** `RD_FILIAL + RD_MAT + RD_DATARQ + RD_CODVB`

---

### SRV — Verbas / Códigos de Folha

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Tabela de verbas e códigos da folha |
| **Uso no projeto** | BCGPE007 |

**Campos (130 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| RV_FILIAL | Char | 4 | 0 | Filial |
| RV_COD | Char | 3 | 0 | Codigo Verba |
| RV_DESC | Char | 20 | 0 | Descricao |
| RV_DESCDET | Char | 50 | 0 | Desc. Det. |
| RV_TIPOCOD | Char | 1 | 0 | Tipo do Cod. |
| RV_IMPRIPD | Char | 1 | 0 | Impr. Verba |
| RV_PERC | Numeric | 7 | 3 | Percentual |
| RV_CODCORR | Char | 3 | 0 | Cod.Corresp. |
| RV_CODFOL | Char | 4 | 0 | Id.p/Calculo |
| RV_TIPO | Char | 1 | 0 | Tipo Verba |
| RV_OBRIGAT | Char | 1 | 0 | Pagto.Obrig. |
| RV_QTDLANC | Char | 1 | 0 | Qtde.Lancto |
| RV_LCTODIA | Char | 1 | 0 | Lcto Diario |
| RV_VLIMDE | Numeric | 12 | 2 | Valor De |
| RV_VLIMATE | Numeric | 12 | 2 | Valor Ate |
| RV_CLORC | Char | 6 | 0 | Classe Orc. |
| RV_RLIMDE | Numeric | 12 | 2 | Ref. De |
| RV_RLIMATE | Numeric | 12 | 2 | Ref. Ate |
| RV_INSS | Char | 1 | 0 | INSS |
| RV_IR | Char | 1 | 0 | IR |
| RV_FGTS | Char | 1 | 0 | FGTS |
| RV_INCORP | Char | 1 | 0 | Incorp. Sal. |
| RV_REF13 | Char | 1 | 0 | Ref. a 13o. |
| RV_REFFER | Char | 1 | 0 | Ref.a Ferias |
| RV_ADIANTA | Char | 1 | 0 | Ref. Adiant. |
| RV_PERICUL | Char | 1 | 0 | Periculosid. |
| RV_INSALUB | Char | 1 | 0 | Insalubrid. |
| RV_PENSAO | Char | 1 | 0 | Pensao Alim. |
| RV_DSRHE | Char | 1 | 0 | DSR H.Extra |
| RV_HE | Char | 1 | 0 | Hora Extra |
| RV_ADICTS | Char | 1 | 0 | Adic.T.Serv. |
| RV_SINDICA | Char | 1 | 0 | C. Sindical |
| RV_SALFAMI | Char | 1 | 0 | Sal. Familia |
| RV_SEGVIDA | Char | 1 | 0 | Seguro Vida |
| RV_DEDINSS | Char | 1 | 0 | Ded. G. INSS |
| RV_TAREFA | Char | 3 | 0 | Cod.Tarefa |
| RV_PIS | Char | 1 | 0 | PIS |
| RV_ENCARCC | Char | 1 | 0 | Rateio C.Cto |
| RV_CUSTO | Char | 1 | 0 | Custo |
| RV_LCTOP | Char | 3 | 0 | Lcto. Padrao |
| RV_MED13 | Char | 2 | 0 | Media 13o. |
| RV_MEDFER | Char | 2 | 0 | Media Ferias |
| RV_MEDAVI | Char | 2 | 0 | Med.Av.Prev. |
| RV_GRAMED | Char | 3 | 0 | C.Agrup.Med. |
| RV_CONVCOL | Char | 1 | 0 | Conv.Colet. |
| RV_VALDISS | Char | 1 | 0 | Recal.lan.vl |
| RV_MEDREAJ | Char | 1 | 0 | Med.Reajust. |
| RV_RAIS | Char | 60 | 0 | RAIS |
| RV_DIRF | Char | 2 | 0 | DIRF |
| RV_COMPL_ | Char | 1 | 0 | Dissid. Ret. |
| RV_CODCOM_ | Char | 3 | 0 | Verba P.Diss |
| RV_DSRPROF | Char | 1 | 0 | DSR Prof. |
| RV_HRSATIV | Char | 1 | 0 | Hs.Atividade |
| RV_CUSTEMP | Char | 1 | 0 | Ag.Custo PMS |
| RV_COD13 | Char | 3 | 0 | Código 13o. |
| RV_CODFER | Char | 3 | 0 | Cód.Férias |
| RV_CODMSEG | Char | 3 | 0 | V. Mes Segui |
| RV_DESMSEG | Char | 20 | 0 | Desc. Verba |
| RV_LANCPCO | Char | 2 | 0 | Lancto PCO |
| RV_GRPVERB | Char | 10 | 0 | Grupo Verba |
| RV_CODDSR | Char | 3 | 0 | Verba DSR |
| RV_CODBASE | Char | 3 | 0 | Cod.Base Cor |
| RV_RRA | Char | 1 | 0 | RRA |
| RV_HOMOLOG | Char | 3 | 0 | V.Homolognet |
| RV_XDEPA | Char | 3 | 0 | Verb.Datasul |
| RV_XDEBIT | Char | 15 | 0 | Cta.Debito |
| RV_XCREDIT | Char | 15 | 0 | Cta. Credito |
| RV_XINCCON | Char | 1 | 0 | INC.M.CONSIG |
| RV_XPLR | Char | 1 | 0 | Incide PLR |
| RV_XPREVID | Char | 1 | 0 | Prev Privada |
| RV_AGLTRCT | Char | 1 | 0 | Aglut.TRCT |
| RV_INSSFER | Char | 1 | 0 | INSS Fer. |
| RV_LEEINC | Char | 1 | 0 | Funcionarios |
| RV_LEEPRE | Char | 1 | 0 | Futuros |
| RV_LEEAUS | Char | 1 | 0 | Ausencia |
| RV_LEEBEN | Char | 1 | 0 | Beneficiario |
| RV_LEEFIX | Char | 1 | 0 | Fixos |
| RV_FECCOMP | Char | 1 | 0 | Fech Compete |
| RV_DESMEMO | Memo | 10 | 0 | Expr. Filtro |
| RV_CODMEMO | Char | 6 | 0 | Cód. Expr |

> +50 campos. Use consultar_tabela_dicionario("SRV").

**Chave primaria:** `RV_FILIAL + RV_COD`

---

### SRY — Roteiros de Folha

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Roteiros de cálculo da folha |
| **Uso no projeto** | recibo.PRX |

**Campos (18 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| RY_FILIAL | Char | 4 | 0 | Filial |
| RY_CALCULO | Char | 3 | 0 | Roteiro |
| RY_DESC | Char | 30 | 0 | Desc.Rot. |
| RY_ORIGEM | Char | 1 | 0 | Origem |
| RY_CODOBS | Char | 6 | 0 | Cod. Observ. |
| RY_DESOBS | Memo | 10 | 0 | Obs. Roteiro |
| RY_VERSAO | Char | 3 | 0 | Versäo |
| RY_ALIAS | Char | 3 | 0 | Arq. Mestre |
| RY_RECOMP | Char | 1 | 0 | Recompilar |
| RY_ORDINAR | Char | 1 | 0 | Ordinario |
| RY_TIPO | Char | 1 | 0 | Tipo Roteiro |
| RY_PERGUNT | Char | 10 | 0 | Grp Pergunte |
| RY_SEQFIL | Char | 2 | 0 | Seq.Fil. |
| RY_INTEGRA | Char | 1 | 0 | Integra? |
| RY_CONTAB | Char | 1 | 0 | Contabiliza? |
| RY_USERLGI | Char | 17 | 0 | Log de Inclu |
| RY_USERLGA | Char | 17 | 0 | Log de Alter |
| RY_MODULO | Char | 1 | 0 | Módulo |
**Chave primaria:** `RY_FILIAL + RY_COD`

---

### SRH — Histórico do Funcionário

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Histórico de alterações do funcionário |
| **Uso no projeto** | recibo.PRX |

**Campos (42 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| RH_FILIAL | Char | 4 | 0 | Filial |
| RH_MAT | Char | 6 | 0 | Matricula |
| RH_NOME | Char | 30 | 0 | Nome |
| RH_SALMES | Numeric | 12 | 2 | Salario Mes |
| RH_SALDIA | Numeric | 12 | 2 | Salario Dia |
| RH_SALDIA1 | Numeric | 12 | 4 | Sal Dia Seg |
| RH_SALHRS | Numeric | 12 | 2 | Salario Hora |
| RH_SALHRS1 | Numeric | 12 | 2 | Sal Hora Seg |
| RH_DATABAS | Date | 8 | 0 | Base Fer.Ini |
| RH_DBASEAT | Date | 8 | 0 | Base Fer.Fim |
| RH_DFERVEN | Numeric | 6 | 1 | Dias Fer.Ven |
| RH_DFERIAS | Numeric | 6 | 1 | Dias Ferias |
| RH_DABONPE | Numeric | 6 | 1 | Dias Ab.Pec. |
| RH_ABOPEC | Char | 1 | 0 | Per.de Abono |
| RH_DFALTAS | Numeric | 5 | 1 | Dias Faltas |
| RH_PERC13S | Numeric | 3 | 0 | % 13 Salario |
| RH_XADIANT | Numeric | 6 | 2 | % Adiant. |
| RH_XNUMPAR | Numeric | 2 | 0 | Num Parc Adt |
| RH_DATAINI | Date | 8 | 0 | Inic. Ferias |
| RH_DATAFIM | Date | 8 | 0 | Fim   Férias |
| RH_DIALRE1 | Numeric | 6 | 1 | D.Lic.Rem MS |
| RH_DTAVISO | Date | 8 | 0 | Dt.Av.Ferias |
| RH_SALDIF | Numeric | 12 | 2 | Salario Dif. |
| RH_DTRECIB | Date | 8 | 0 | Dt.Rec.Fer. |
| RH_DIALREM | Numeric | 6 | 1 | Dias Lic.Rem |
| RH_ROTEIR | Char | 3 | 0 | Roteiro |
| RH_SALMIN | Numeric | 12 | 2 | Salario Min. |
| RH_SALMIND | Numeric | 12 | 2 | Sal. Min.Dif |
| RH_SALARIO | Numeric | 12 | 2 | Salário |
| RH_SALARDF | Numeric | 12 | 2 | Dif. Salário |
| RH_TIPCAL | Char | 1 | 0 | Tipo Calculo |
| RH_PERIODO | Char | 6 | 0 | Periodo |
| RH_NPAGTO | Char | 2 | 0 | Nr.Pagamento |
| RH_MEDATU | Char | 1 | 0 | Mes p/Media |
| RH_DAFASTA | Numeric | 3 | 0 | Dias Afast. |
| RH_OBSERVA | Char | 40 | 0 | Observacao |
| RH_PROCES | Char | 5 | 0 | Cod.Processo |
| RH_RHEXP | Char | 6 | 0 | Contr.Exp.RH |
| RH_USERLGI | Char | 17 | 0 | Log de Inclu |
| RH_USERLGA | Char | 17 | 0 | Log de Alter |
| RH_ACEITE | Char | 80 | 0 | Aceite |
| RH_POSTUMT | Char | 1 | 0 | Post. 1/3? |
**Chave primaria:** `RH_FILIAL + RH_MAT + RH_DTINI`

---

### SRJ — Função / Cargo (RH)

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Funções e cargos dos funcionários |
| **Uso no projeto** | INTEGRACAO_APPUS.tlpp |

**Campos (34 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| RJ_FILIAL | Char | 4 | 0 | Filial |
| RJ_FUNCAO | Char | 5 | 0 | Funcao |
| RJ_DESC | Char | 20 | 0 | Descricao |
| RJ_CODCBO | Char | 6 | 0 | CBO 2002 |
| RJ_CBO | Char | 5 | 0 | CBO 1994 |
| RJ_MAOBRA | Char | 1 | 0 | Mao de Obra |
| RJ_CARGO | Char | 5 | 0 | Cargo |
| RJ_SALARIO | Numeric | 12 | 2 | Salario |
| RJ_VALDIA | Numeric | 13 | 2 | VALOR DIARIA |
| RJ_DESCREQ | Char | 6 | 0 | REQUISITOS |
| RJ_MEMOREQ | Memo | 80 | 0 | Requisitos |
| RJ_DESCDE | Char | 200 | 0 | Desc Detalha |
| RJ_LIDER | Char | 1 | 0 | Func. Lider? |
| RJ_RHEXP | Char | 6 | 0 | Contr.Exp.RH |
| RJ_ADTPFUN | Char | 1 | 0 | Tp.de Funcao |
| RJ_ADTPJU | Char | 1 | 0 | Tp.Reg.Jurid |
| RJ_ADTPESC | Char | 2 | 0 | Tp.Escolar. |
| RJ_ADATIV | Char | 1 | 0 | Exerc.Ativ. |
| RJ_ADTPROV | Char | 1 | 0 | Tp.Prov. |
| RJ_ADHORAS | Numeric | 6 | 2 | Tot.Hrs Trab |
| RJ_ADDATA | Date | 8 | 0 | Dt. Criação |
| RJ_CTESP | Char | 1 | 0 | Cnt Especial |
| RJ_ACUM | Char | 1 | 0 | Acum de Carg |
| RJ_DEDEXC | Char | 1 | 0 | Ded Exclusiv |
| RJ_LEI | Char | 12 | 0 | Lei Criação |
| RJ_DTLEI | Date | 8 | 0 | Data da Lei |
| RJ_SIT | Char | 1 | 0 | Sit Cargo |
| RJ_PPPIMP | Char | 1 | 0 | Impr.no PPP? |
| RJ_MSBLQL | Char | 1 | 0 | Bloqueado? |
| RJ_CUMADIC | Char | 1 | 0 | Cum. Adic? |
| RJ_XPERFAI | Char | 1 | 0 | % Faixa Sal |
| RJ_XCOTAPZ | Char | 1 | 0 | Cot Aprendiz |
| RJ_XCTAPCD | Char | 1 | 0 | Cota PCD? |
| RJ_XCOMISS | Char | 1 | 0 | Comissionado |
**Chave primaria:** `RJ_FILIAL + RJ_COD`

---

### SRK — (RH — Cancelamento)

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Tabelas auxiliares utilizadas em consultas SQL |
| **Uso no projeto** | BCGPE007.prw |

**Campos (48 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| RK_FILIAL | Char | 4 | 0 | Filial |
| RK_MAT | Char | 6 | 0 | Matricula |
| RK_PD | Char | 3 | 0 | Codigo Verba |
| RK_DESCPD | Char | 20 | 0 | Descricao |
| RK_VALORTO | Numeric | 12 | 2 | Vr.Principal |
| RK_PARCELA | Numeric | 2 | 0 | Nr. Parcelas |
| RK_JUROANO | Numeric | 6 | 2 | %.Juros Ano |
| RK_JUROMES | Numeric | 6 | 2 | % Juro Mes |
| RK_VALORPA | Numeric | 12 | 2 | Vr. Parcela |
| RK_PARCPAG | Numeric | 4 | 0 | Nr.Parc.Paga |
| RK_VLRPAGO | Numeric | 12 | 2 | Vlr.Pago |
| RK_VALORAR | Numeric | 12 | 2 | Vr. Residuo |
| RK_DTVENC | Date | 8 | 0 | Dt.Prox.Vect |
| RK_DTMOVI | Date | 8 | 0 | Dt.Movimento |
| RK_DOCUMEN | Char | 6 | 0 | Nr.Document. |
| RK_CC | Char | 20 | 0 | Centro Custo |
| RK_PERINI | Char | 6 | 0 | Per. Inicio |
| RK_NUMPAGO | Char | 2 | 0 | Num. Pagto |
| RK_REGRADS | Char | 1 | 0 | Reg. Descont |
| RK_STATUS | Char | 1 | 0 | Situacao |
| RK_VLSALDO | Numeric | 12 | 2 | Saldo |
| RK_NUMID | Char | 26 | 0 | Num.Identif. |
| RK_QUITAR | Char | 1 | 0 | Quitar Lanc. |
| RK_PROCES | Char | 5 | 0 | Cod.Processo |
| RK_POSTO | Char | 9 | 0 | Cod. Posto |
| RK_ITEM | Char | 9 | 0 | Item |
| RK_CLVL | Char | 9 | 0 | Classe Valor |
| RK_VALPARE | Numeric | 12 | 2 | Vl. Especial |
| RK_EMPCONS | Char | 1 | 0 | Emp. Cons. |
| RK_MESDISS | Char | 6 | 0 | Referência |
| RK_IDCMPL | Char | 6 | 0 | ID. Comp. |
| RK_TIPO | Char | 1 | 0 | Origem |
| RK_HORAS | Numeric | 6 | 2 | Horas Lanc. |
| RK_PDJUROS | Char | 3 | 0 | Verba Juros |
| RK_VLJUROS | Numeric | 12 | 2 | Valor Juros |
| RK_PCJUROS | Numeric | 12 | 2 | Parc. Juros |
| RK_PGJUROS | Numeric | 12 | 2 | Juros Pagos |
| RK_USERLGI | Char | 17 | 0 | Log de Inclu |
| RK_USERLGA | Char | 17 | 0 | Log de Alter |
| RK_DTREF | Date | 8 | 0 | Data Ref. |
| RK_NRCONTR | Char | 15 | 0 | Nr.Contrato |
| RK_CONSFGT | Char | 1 | 0 | Consig. FGTS |
| RK_BCOCONS | Char | 5 | 0 | Mat.Inst.Con |
| RK_XPARCEL | Numeric | 4 | 0 | Nr.Parc.Paga |
| RK_XVLRPAG | Numeric | 12 | 2 | Vlr.Pago |
| RK_XVLSALD | Numeric | 12 | 2 | Saldo Rest |
| RK_XNUMID | Char | 26 | 0 | Backup ID |
| RK_OBSECON | Memo | 10 | 0 | Obs. eConsig |
**Chave primaria:** `RK_FILIAL + RK_MAT + RK_DATA`

---

### SQB — Departamentos (RH)

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Cadastro de departamentos |
| **Uso no projeto** | recibo.PRX, INTEGRACAO_APPUS.tlpp |

**Campos (30 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| QB_FILIAL | Char | 4 | 0 | Filial |
| QB_DEPTO | Char | 9 | 0 | Departamento |
| QB_DESCRIC | Char | 30 | 0 | Descricao |
| QB_CC | Char | 20 | 0 | Centro Custo |
| QB_DESCCC | Char | 30 | 0 | Descr.CCusto |
| QB_REGIAO | Char | 6 | 0 | Região |
| QB_DESCREG | Char | 30 | 0 | Descr.Região |
| QB_FILRESP | Char | 4 | 0 | Filial Resp. |
| QB_MATRESP | Char | 6 | 0 | Matric Resp |
| QB_DEPSUP | Char | 9 | 0 | Depto Super |
| QB_GRUPO | Char | 2 | 0 | Grupo |
| QB_ARELIN | Char | 10 | 0 | Ar.Lin.Neg. |
| QB_FILTIT | Char | 4 | 0 | Filial Tit |
| QB_MATTIT | Char | 6 | 0 | Mat Titular |
| QB_XFILSUB | Char | 4 | 0 | Fil Subst |
| QB_XMATSUB | Char | 6 | 0 | Mat Subst |
| QB_XNOMCPL | Char | 200 | 0 | Nom Completo |
| QB_KEYINI | Char | 60 | 0 | Chave de bus |
| QB_USERLGI | Char | 17 | 0 | Log de Inclu |
| QB_USERLGA | Char | 17 | 0 | Log de Alter |
| QB_XPREDIO | Char | 42 | 0 | Predio |
| QB_XANDAR | Char | 22 | 0 | Andar |
| QB_MSBLQL | Char | 1 | 0 | Bloqueado? |
| QB_FILRSP2 | Char | 4 | 0 | Fil. 2 Resp. |
| QB_MATRSP2 | Char | 6 | 0 | Matr. 2 Resp |
| QB_COMARC | Char | 6 | 0 | Comarca |
| QB_CONOME | Char | 30 | 0 | Nome Comarca |
| QB_EMPRESP | Char | 2 | 0 | Emp. Resp. |
| QB_ABOSAB | Char | 1 | 0 | Abono Sabado |
| QB_DTALTRE | Date | 8 | 0 | Dt Alt.Resp. |
**Chave primaria:** `QB_FILIAL + QB_DEPTO`

---

### SQ3 — Cargos (RH)

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Cadastro de cargos |
| **Uso no projeto** | recibo.PRX |

**Campos (50 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| Q3_FILIAL | Char | 4 | 0 | Filial |
| Q3_CARGO | Char | 5 | 0 | Cargo |
| Q3_DESCSUM | Char | 30 | 0 | Desc.Sumaria |
| Q3_DESCDE | Char | 200 | 0 | Desc Detalha |
| Q3_CC | Char | 20 | 0 | Centro Custo |
| Q3_DESCCC | Char | 40 | 0 | Descr.CCusto |
| Q3_MEMO1 | Memo | 80 | 0 | Ds.Detalhada |
| Q3_DESCDET | Char | 6 | 0 | Ds.Detalhada |
| Q3_DRESP | Char | 6 | 0 | Responsabil. |
| Q3_MEMO2 | Memo | 10 | 0 | Responsabil. |
| Q3_DRELINT | Char | 6 | 0 | Relac. int. |
| Q3_MEMO3 | Memo | 10 | 0 | Relac. int. |
| Q3_DHABILI | Char | 6 | 0 | Habilidades |
| Q3_MEMO4 | Memo | 10 | 0 | Habilidades |
| Q3_GRUPO | Char | 2 | 0 | Grupo |
| Q3_DGRUPO | Char | 15 | 0 | Desc. Grupo |
| Q3_DEPTO | Char | 9 | 0 | Departamento |
| Q3_DDEPTO | Char | 30 | 0 | Desc Depto. |
| Q3_TIPO | Char | 2 | 0 | Tipo |
| Q3_DESCTIP | Char | 30 | 0 | Desc Tipo |
| Q3_PONTOSI | Numeric | 7 | 3 | Pontos |
| Q3_TABELA | Char | 3 | 0 | Tabela Sal. |
| Q3_TABNIVE | Char | 2 | 0 | Nivel Tabela |
| Q3_XTABELA | Char | 3 | 0 | Tabela ADI |
| Q3_XTABNIV | Char | 2 | 0 | Nivel ADI |
| Q3_TABFAIX | Char | 2 | 0 | Faixa Inic. |
| Q3_CLASSE | Char | 3 | 0 | Classe |
| Q3_CATEG | Char | 1 | 0 | Class.Cargo |
| Q3_ADTPCAR | Char | 1 | 0 | Tp. Cargo |
| Q3_ADTPJU | Char | 1 | 0 | Tp.Reg.Jurid |
| Q3_ADTPESC | Char | 2 | 0 | Tp.Escolar. |
| Q3_ADATIV | Char | 1 | 0 | Exerc.Ativ. |
| Q3_ADTPROV | Char | 1 | 0 | Tp.Prov. |
| Q3_ADHORAS | Numeric | 6 | 2 | Tot.Hrs Trab |
| Q3_ADCP | Char | 1 | 0 | Cargo Polit. |
| Q3_ADRESP | Date | 8 | 0 | Dt.Ini.Resp. |
| Q3_CBO | Char | 6 | 0 | Código CBO |
| Q3_ACUM | Char | 1 | 0 | Acum. Cargo |
| Q3_CTESP | Char | 1 | 0 | Cnt.Especial |
| Q3_DEDEXC | Char | 1 | 0 | D. Exclusiva |
| Q3_LEI | Char | 12 | 0 | Lei do Cargo |
| Q3_DTLEI | Date | 8 | 0 | Data da Lei |
| Q3_SIT | Char | 1 | 0 | Sit. Cargo |
| Q3_PORTAL | Char | 6 | 0 | Grupo Portal |
| Q3_SUBSTIT | Char | 1 | 0 | Nec.Substit. |
| Q3_PRIORL | Char | 5 | 0 | Prior Lotac |
| Q3_DESCLAS | Char | 30 | 0 | Desc.Classe |
| Q3_MSBLQL | Char | 1 | 0 | Bloqueado? |
| Q3_XDESCDE | Char | 200 | 0 | Desc Detalha |
| Q3_XMULTPL | Numeric | 4 | 2 | Multiplo PLR |
**Chave primaria:** `Q3_FILIAL + Q3_CARGO`

---

### RCH — Calendário / Período Folha

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Períodos de competência da folha |
| **Uso no projeto** | recibo.PRX |

**Campos (34 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| RCH_FILIAL | Char | 4 | 0 | Filial |
| RCH_PER | Char | 6 | 0 | Cod. Periodo |
| RCH_NUMPAG | Char | 2 | 0 | Numero Pagto |
| RCH_PROCES | Char | 5 | 0 | Processo |
| RCH_ROTEIR | Char | 3 | 0 | Roteiro Calc |
| RCH_MES | Char | 2 | 0 | Mes Compet. |
| RCH_ANO | Char | 4 | 0 | Ano Compet. |
| RCH_DTINI | Date | 8 | 0 | Data Inicial |
| RCH_DTFIM | Date | 8 | 0 | Data Final |
| RCH_DTPAGO | Date | 8 | 0 | Data Pagto |
| RCH_DTPGAD | Date | 8 | 0 | Dt Pgto Adto |
| RCH_DTPG13 | Date | 8 | 0 | Dt Pagto 13o |
| RCH_DTCORT | Date | 8 | 0 | Data Corte |
| RCH_DTFECH | Date | 8 | 0 | Data Fecham |
| RCH_DTCONT | Date | 8 | 0 | Data Contab. |
| RCH_PERSEL | Char | 1 | 0 | Per.selec ? |
| RCH_STATUS | Char | 1 | 0 | Status |
| RCH_ACUM1 | Numeric | 2 | 0 | Mes Acum 1 |
| RCH_ACUM2 | Numeric | 2 | 0 | Mes Acum 2 |
| RCH_ACUM3 | Numeric | 2 | 0 | Mes Acum 3 |
| RCH_ACUM4 | Numeric | 2 | 0 | Mes Acum 4 |
| RCH_MODULO | Char | 3 | 0 | Módulo |
| RCH_PDPERI | Char | 3 | 0 | Pad.Período |
| RCH_DIAUTI | Numeric | 8 | 0 | Dia Util |
| RCH_COND1 | Char | 8 | 0 | Condição 1 |
| RCH_COND2 | Char | 8 | 0 | Condição 2 |
| RCH_CRITER | Char | 60 | 0 | Critério Ac. |
| RCH_SEQUE | Char | 60 | 0 | Sequência Ac |
| RCH_TARINI | Date | 8 | 0 | Ini Tarefa |
| RCH_TARFIM | Date | 8 | 0 | Fim Tarefa |
| RCH_DTINTE | Date | 8 | 0 | Dt. Integ. |
| RCH_COMPL | Char | 1 | 0 | Complementar |
| RCH_BLOQ | Char | 1 | 0 | Bloqueado |
| RCH_USERFE | Char | 40 | 0 | Usuário Fec. |
**Chave primaria:** `CH_FILIAL + CH_PERREF`

---

### RCC — Códigos de Folha

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Códigos de eventos da folha |
| **Uso no projeto** | recibo.PRX, BCGPE41 |

**Campos (8 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| RCC_FILIAL | Char | 4 | 0 | Filial |
| RCC_CODIGO | Char | 4 | 0 | Codigo |
| RCC_FIL | Char | 4 | 0 | Filial |
| RCC_CHAVE | Char | 6 | 0 | Mes / Ano |
| RCC_SEQUEN | Char | 3 | 0 | Sequencia |
| RCC_CONTEU | Char | 250 | 0 | Conteudo |
| RCC_USERGI | Char | 17 | 0 | Log de Inclu |
| RCC_USERGA | Char | 17 | 0 | Log de Alter |
**Chave primaria:** `CC_FILIAL + CC_COD`

---

### RCE — Sindicatos

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Cadastro de sindicatos |
| **Uso no projeto** | BCGPE007 |

**Campos (148 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| RCE_FILIAL | Char | 4 | 0 | Filial |
| RCE_CODIGO | Char | 2 | 0 | Codigo |
| RCE_DESCRI | Char | 40 | 0 | Descricao |
| RCE_CGC | Char | 14 | 0 | CNPJ Ent.Sin |
| RCE_ENTSIN | Char | 15 | 0 | Cod.Ent.Sind |
| RCE_ENDER | Char | 30 | 0 | Endereco |
| RCE_NUMER | Char | 5 | 0 | Numero |
| RCE_COMPLE | Char | 10 | 0 | Complemento |
| RCE_BAIRRO | Char | 20 | 0 | Bairro |
| RCE_CEP | Char | 8 | 0 | CEP |
| RCE_UF | Char | 2 | 0 | Estado |
| RCE_MUNIC | Char | 20 | 0 | Municipio |
| RCE_MESDIS | Char | 2 | 0 | Mes Dissidio |
| RCE_MESANT | Char | 2 | 0 | Mes Antecip. |
| RCE_MED01 | Numeric | 2 | 0 | Meses Med 1o |
| RCE_MED02 | Numeric | 2 | 0 | Meses Med.2o |
| RCE_MED03 | Numeric | 2 | 0 | Meses Med 3o |
| RCE_MED04 | Numeric | 2 | 0 | Meses Med 4o |
| RCE_NROSEM | Numeric | 3 | 1 | Semana Mes |
| RCE_DSR | Numeric | 8 | 4 | % DSR Prof. |
| RCE_HSATIV | Numeric | 8 | 4 | % Hrs Ativ. |
| RCE_GCOMIS | Numeric | 12 | 2 | G.Comissao |
| RCE_INI1SM | Char | 4 | 0 | D/M Ini 1.Sm |
| RCE_FIM1SM | Char | 4 | 0 | D/M Fim 1.Sm |
| RCE_DDD | Char | 3 | 0 | Cod. DDD |
| RCE_FONE | Char | 20 | 0 | Telefone |
| RCE_FAX | Char | 20 | 0 | Fax |
| RCE_EMAIL | Char | 60 | 0 | E-Mail |
| RCE_INI2SM | Char | 4 | 0 | D/M Ini 2.Sm |
| RCE_FIM2SM | Char | 4 | 0 | D/M Fim 2.Sm |
| RCE_PISO | Numeric | 12 | 2 | Piso Categ |
| RCE_ASSJAN | Numeric | 12 | 2 | Ref Janeiro |
| RCE_ASSFEV | Numeric | 12 | 2 | Ref Fevereir |
| RCE_ASSMAR | Numeric | 12 | 2 | Ref Marco |
| RCE_ASSABR | Numeric | 12 | 2 | Ref Abril |
| RCE_ASSMAI | Numeric | 12 | 2 | Ref Maio |
| RCE_ASSJUN | Numeric | 12 | 2 | Ref Junho |
| RCE_ASSJUL | Numeric | 12 | 2 | Ref Julho |
| RCE_ASSAGO | Numeric | 12 | 2 | Ref Agosto |
| RCE_ASSSET | Numeric | 12 | 2 | Ref Setembro |
| RCE_ASSOUT | Numeric | 12 | 2 | Ref Outubro |
| RCE_ASSNOV | Numeric | 12 | 2 | Ref Novembro |
| RCE_ASSDEZ | Numeric | 12 | 2 | Ref Dezembro |
| RCE_ASSREF | Char | 1 | 0 | Tipo Referen |
| RCE_ASSSAL | Char | 1 | 0 | Tipo Salario |
| RCE_ASSMIN | Numeric | 12 | 2 | Desc Minimo |
| RCE_ASSMAX | Numeric | 12 | 2 | Desc Maximo |
| RCE_CONJAN | Numeric | 12 | 2 | Ref Janeiro |
| RCE_CONFEV | Numeric | 12 | 2 | Ref Fevereir |
| RCE_CONMAR | Numeric | 12 | 2 | Ref Marco |
| RCE_CONABR | Numeric | 12 | 2 | Ref Abril |
| RCE_CONMAI | Numeric | 12 | 2 | Ref Maio |
| RCE_CONJUN | Numeric | 12 | 2 | Ref Junho |
| RCE_CONJUL | Numeric | 12 | 2 | Ref Julho |
| RCE_CONAGO | Numeric | 12 | 2 | Ref Agosto |
| RCE_CONSET | Numeric | 12 | 2 | Ref Setembro |
| RCE_CONOUT | Numeric | 12 | 2 | Ref Outubro |
| RCE_CONNOV | Numeric | 12 | 2 | Ref Novembro |
| RCE_CONDEZ | Numeric | 12 | 2 | Ref Dezembro |
| RCE_CONREF | Char | 1 | 0 | Tipo Referen |
| RCE_CONSAL | Char | 1 | 0 | Tipo Salario |
| RCE_CONMIN | Numeric | 12 | 2 | Desc Minimo |
| RCE_CONMAX | Numeric | 12 | 2 | Desc Maximo |
| RCE_MENSIN | Numeric | 12 | 2 | Mens Sindica |
| RCE_MENREF | Char | 1 | 0 | Tipo Referen |
| RCE_MENSAL | Char | 1 | 0 | Tipo Salario |
| RCE_MENMIN | Numeric | 12 | 2 | Desc Minimo |
| RCE_MENMAX | Numeric | 12 | 2 | Desc Maximo |
| RCE_RHEXP | Char | 6 | 0 | Contr.Exp.Rh |
| RCE_XMESES | Numeric | 2 | 0 | Meses Media |
| RCE_XTIPOC | Char | 1 | 0 | Tipo Calculo |
| RCE_XMESE2 | Numeric | 2 | 0 | 2° Meses |
| RCE_XMESE3 | Numeric | 2 | 0 | 3° Meses |
| RCE_XEXERC | Char | 1 | 0 | 13 Exercicio |
| RCE_XCOMPE | Char | 1 | 0 | 13 no exerci |
| RCE_DIADIS | Numeric | 2 | 0 | Dia Dissidio |
| RCE_DIASAV | Numeric | 2 | 0 | Dias Av.Prev |
| RCE_XMESAT | Char | 1 | 0 | Mes Atual? |
| RCE_PLRTPC | Char | 1 | 0 | Tp. de Cálc. |
| RCE_PLRBSC | Char | 1 | 0 | Bs. De Cálc. |

> +68 campos. Use consultar_tabela_dicionario("RCE").

**Chave primaria:** `CE_FILIAL + CE_COD`

---

### RCF — Semana Folha

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Controle de semanas na folha |
| **Uso no projeto** | recibo.PRX |

**Campos (29 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| RCF_FILIAL | Char | 4 | 0 | Filial |
| RCF_MES | Char | 2 | 0 | Mes Compet. |
| RCF_ANO | Char | 4 | 0 | Ano Compet. |
| RCF_PER | Char | 6 | 0 | Periodo |
| RCF_PROCES | Char | 5 | 0 | Cod.Processo |
| RCF_ROTEIR | Char | 3 | 0 | Roteiro Calc |
| RCF_TNOTRA | Char | 3 | 0 | Turno Trab. |
| RCF_SEMANA | Char | 2 | 0 | Semana |
| RCF_DTINI | Date | 8 | 0 | Data Inicial |
| RCF_DTFIM | Date | 8 | 0 | Data Final |
| RCF_DCALCM | Numeric | 4 | 0 | Dias Mensal |
| RCF_HRSDIA | Numeric | 5 | 2 | Horas Dia |
| RCF_DIATRA | Numeric | 2 | 0 | Nº.Dias Trab |
| RCF_HRSTRA | Numeric | 7 | 2 | Hrs. Trabalh |
| RCF_DIADSR | Numeric | 2 | 0 | Nº.Dias DSR |
| RCF_HRSDSR | Numeric | 7 | 2 | Horas DSR |
| RCF_DNTRAB | Numeric | 4 | 0 | Dias Nao Tra |
| RCF_DUTILT | Numeric | 4 | 0 | D.Uteis V.T. |
| RCF_DNUTIL | Numeric | 2 | 0 | D.Nao Ut.VT |
| RCF_DDIFVT | Numeric | 2 | 0 | Nº.D.Dif.V.T |
| RCF_DREFEI | Numeric | 2 | 0 | Dias V.Ref. |
| RCF_DALIM | Numeric | 2 | 0 | Dias V.Alim. |
| RCF_CONTAB | Char | 1 | 0 | Per. Contab. |
| RCF_FECHAD | Char | 1 | 0 | Per. Fechado |
| RCF_DPERIO | Numeric | 4 | 0 | Dias Período |
| RCF_DUTEIS | Numeric | 4 | 0 | Dias Uteis |
| RCF_MODULO | Char | 3 | 0 | Modulo |
| RCF_USERGI | Char | 17 | 0 | Log de Inclu |
| RCF_USERGA | Char | 17 | 0 | Log de Alter |
**Chave primaria:** `CF_FILIAL + CF_SEMANA`

---

### RCB — Seguro Vida (RH)

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Controle de seguro de vida |
| **Uso no projeto** | BCGPE41 |

**Campos (17 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| RCB_FILIAL | Char | 4 | 0 | Filial |
| RCB_CODIGO | Char | 4 | 0 | Codigo |
| RCB_DESC | Char | 30 | 0 | Descricao |
| RCB_ORDEM | Char | 2 | 0 | Ordem |
| RCB_CAMPOS | Char | 10 | 0 | Campos |
| RCB_DESCPO | Char | 25 | 0 | Desc.Campo |
| RCB_TIPO | Char | 1 | 0 | Tipo |
| RCB_TAMAN | Numeric | 3 | 0 | Tamanho |
| RCB_DECIMA | Numeric | 2 | 0 | Decimal |
| RCB_PICTUR | Char | 45 | 0 | Picture |
| RCB_VALID | Char | 120 | 0 | Validacao |
| RCB_PADRAO | Char | 6 | 0 | Cons.Padrao |
| RCB_VERSAO | Char | 3 | 0 | Versäo |
| RCB_PESQ | Char | 1 | 0 | Usado Pesq ? |
| RCB_SHOWMA | Char | 1 | 0 | Exibe MesAno |
| RCB_MODULO | Char | 1 | 0 | Modulo |
| RCB_PROCES | Char | 30 | 0 | Processo Log |
**Chave primaria:** `RCB_FILIAL + RCB_MAT + RCB_TPBENEF`

---

### RGG — Categorias (RH)

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Categorias de funcionários |
| **Uso no projeto** | recibo.PRX |

**Chave primaria:** `GG_FILIAL + GG_COD`

---

### VAM — Municípios

| Atributo | Valor |
|----------|-------|
| **Modulo** | SIGAGPE |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Tabelas complementares de RH |
| **Uso no projeto** | PROCU16.TLPP |

**Campos (15 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| VAM_FILIAL | Char | 4 | 0 | Filial |
| VAM_IBGE | Char | 11 | 0 | IBGE |
| VAM_CODCID | Char | 6 | 0 | Cod Cidad |
| VAM_DESCID | Char | 40 | 0 | Desc Cidade |
| VAM_ESTADO | Char | 2 | 0 | UF |
| VAM_DDD | Char | 2 | 0 | DDD |
| VAM_REGIAO | Char | 3 | 0 | Regiao |
| VAM_REGATU | Char | 1 | 0 | Reg Atuacao |
| VAM_REGATG | Char | 1 | 0 | RegAtuacGrup |
| VAM_CEP1 | Char | 8 | 0 | CEP Inicial |
| VAM_CEP2 | Char | 8 | 0 | CEP Final |
| VAM_BANCO | Char | 3 | 0 | Banco |
| VAM_AGBCO | Char | 5 | 0 | Agencia |
| VAM_NOMEAG | Char | 30 | 0 | Nome Agen |
| VAM_AGDEP | Char | 40 | 0 | Nome Agencia |
**Chave primaria:** `AM_COD`

---

---

## Tabelas de Estrutura e Genéricas

### SX5 — Tabelas Genéricas

| Atributo | Valor |
|----------|-------|
| **Modulo** | Geral (todos os módulos) |
| **Tipo** | Padrão TOTVS (metadados) |
| **Descricao** | Tabelas auxiliares / de domínio do sistema |
| **Uso no projeto** | recibo.PRX, CHGX5FIL.PRW |

**Campos (6 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| X5_FILIAL | Char | 4 | 0 | Filial |
| X5_TABELA | Char | 2 | 0 | Tabela |
| X5_CHAVE | Char | 6 | 0 | Chave |
| X5_DESCRI | Char | 55 | 0 | Descricao |
| X5_DESCSPA | Char | 55 | 0 | Desc Spanish |
| X5_DESCENG | Char | 55 | 0 | Desc English |
**Chave primaria:** `X5_FILIAL + X5_TABELA + X5_CHAVE`

---

### SX3 — Estrutura de Campos (Cache)

| Atributo | Valor |
|----------|-------|
| **Modulo** | Geral (todos os módulos) |
| **Tipo** | Padrão TOTVS (metadados) |
| **Descricao** | Dicionário de campos do sistema |
| **Uso no projeto** | Vários (TamSX3, GetSx3Cache) |

**Chave primaria:** `X3_ARQUIVO + X3_CAMPO`

---

### SCP — Cadastro Protheus (Parâmetros Fluig)

| Atributo | Valor |
|----------|-------|
| **Modulo** | Geral |
| **Tipo** | Padrão TOTVS |
| **Descricao** | Parâmetros e pré-requisitos do sistema |
| **Uso no projeto** | GERPREREQ.prw (integração Fluig) |

**Campos (44 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| CP_FILIAL | Char | 4 | 0 | Filial |
| CP_NUM | Char | 6 | 0 | Nr.S.A. |
| CP_ITEM | Char | 2 | 0 | Item S.A. |
| CP_PRODUTO | Char | 15 | 0 | Produto |
| CP_DESCRI | Char | 50 | 0 | Descricao |
| CP_UM | Char | 2 | 0 | Unid Medida |
| CP_SEGUM | Char | 2 | 0 | Segunda UM |
| CP_QUANT | Numeric | 12 | 2 | Quantidade |
| CP_QTSEGUM | Numeric | 12 | 2 | Qtd. 2a UM |
| CP_LOCAL | Char | 2 | 0 | Armazem |
| CP_CC | Char | 20 | 0 | Centro Custo |
| CP_OBS | Char | 254 | 0 | Observacao |
| CP_SOLICIT | Char | 25 | 0 | Solicitante |
| CP_DATPRF | Date | 8 | 0 | Necessidade |
| CP_EMISSAO | Date | 8 | 0 | DT Emissao |
| CP_OP | Char | 14 | 0 | Ord Producao |
| CP_CONTA | Char | 20 | 0 | Cta Contabil |
| CP_QUJE | Numeric | 12 | 2 | Quant.Atend. |
| CP_OK | Char | 2 | 0 | Ok |
| CP_PREREQU | Char | 1 | 0 | Flag P.Re. |
| CP_STATUS | Char | 1 | 0 | Status da SA |
| CP_NUMOS | Char | 8 | 0 | Nr.OS |
| CP_SEQRC | Char | 2 | 0 | Sq.Rp.Center |
| CP_ITEMCTA | Char | 9 | 0 | Item Conta |
| CP_CLVL | Char | 9 | 0 | Classe Valor |
| CP_PROJETO | Char | 1 | 0 | Ger.Projetos |
| CP_NUMSC | Char | 6 | 0 | Numero SC |
| CP_ITSC | Char | 4 | 0 | Item Sc |
| CP_STATSA | Char | 1 | 0 | Status SA |
| CP_SALBLQ | Numeric | 12 | 2 | Saldo Bloq. |
| CP_MEDIDA | Char | 6 | 0 | Medida Pneu |
| CP_SULCMI | Numeric | 6 | 2 | Sulco Mínimo |
| CP_SULCMA | Numeric | 6 | 2 | Sulco Maximo |
| CP_TIPMOD | Char | 10 | 0 | Tipo Modelo |
| CP_LOTE | Char | 6 | 0 | Numero Lote |
| CP_RATEIO | Char | 1 | 0 | Rateio |
| CP_CODSOLI | Char | 6 | 0 | Cod. Solici |
| CP_VUNIT | Numeric | 12 | 2 | Prc Estimado |
| CP_CONSEST | Char | 1 | 0 | Consome Est. |
| CP_NRBPIMS | Char | 10 | 0 | Nr. Boletim |
| CP_XNFLUIG | Char | 10 | 0 | Num FLUIG |
| CP_USER | Char | 6 | 0 | Usuário |
| CP_TRT | Char | 3 | 0 | Sequência |
| CP_ORDSEP | Char | 6 | 0 | Ordem Sep. |
**Chave primaria:** `CP_FILIAL + CP_CODIGO`

---

---

## Tabelas Customizadas — Stage / Integração

### ZAZ — Stage Controle de Cobrança (Custom)

| Atributo | Valor |
|----------|-------|
| **Modulo** | Custom — Financeiro/Cobrança |
| **Tipo** | **Customizada** |
| **Descricao** | Controle de stage do Job de Cobrança |
| **Uso no projeto** | BBFIN41 (Job Cobrança) |

**Campos (11 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| ZAZ_FILIAL | Char | 4 | 0 | Filial |
| ZAZ_IDCOB | Char | 10 | 0 | Id Cobranca |
| ZAZ_CODIGO | Char | 10 | 0 | Codigo |
| ZAZ_ARQUIV | Char | 50 | 0 | Arquivo |
| ZAZ_DATINI | Date | 8 | 0 | Data Inicio |
| ZAZ_TIMEIN | Char | 8 | 0 | Hora Inicio |
| ZAZ_DATAFI | Date | 8 | 0 | Data Fim |
| ZAZ_TIMEFI | Char | 8 | 0 | Hora Fim |
| ZAZ_USER | Char | 6 | 0 | ID Usuario |
| ZAZ_USERNM | Char | 40 | 0 | Name User |
| ZAZ_VLARQ | Numeric | 14 | 2 | Vlr. Arquivo |
**Chave primaria:** `ZAZ_FILIAL + ZAZ_COD`

---

### U97 — Stage Contas a Pagar (Custom REST)

| Atributo | Valor |
|----------|-------|
| **Modulo** | Custom — REST / Integração CP |
| **Tipo** | **Customizada** |
| **Descricao** | Stage de integração REST para Contas a Pagar |
| **Uso no projeto** | U97Stagecpagar.tlpp, dash_integracao.tlpp |

**Campos (37 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| U97_FILIAL | Char | 4 | 0 | Filial |
| U97_PREFIX | Char | 3 | 0 | Prefixo |
| U97_NUM | Char | 9 | 0 | No. Titulo |
| U97_PARCEL | Char | 3 | 0 | Parcela |
| U97_TIPO | Char | 3 | 0 | Tipo |
| U97_NATURE | Char | 10 | 0 | Natureza |
| U97_FORNEC | Char | 14 | 0 | Fornecedor |
| U97_LOJA | Char | 2 | 0 | Loja |
| U97_EMISSA | Date | 8 | 0 | DT Emissao |
| U97_VENCTO | Date | 8 | 0 | Vencimento |
| U97_VENCRE | Date | 8 | 0 | Vencto real |
| U97_VALOR | Numeric | 16 | 2 | Vlr.Titulo |
| U97_HIST | Char | 40 | 0 | Historico |
| U97_SALDO | Numeric | 16 | 2 | Saldo |
| U97_MOEDA | Numeric | 2 | 0 | Moeda |
| U97_XNUMTI | Char | 10 | 0 | Num. Titulo |
| U97_TIPOIN | Char | 1 | 0 | Tipo integra |
| U97_IDSTAG | Char | 50 | 0 | IDSTAGE |
| U97_DTIMPO | Date | 8 | 0 | Dt Import |
| U97_HRIMPO | Char | 15 | 0 | Hr import |
| U97_OBS | Memo | 10 | 0 | Obs Job |
| U97_CODOBS | Char | 1 | 0 | Cod OBS |
| U97_DTOBS | Date | 8 | 0 | Dt Obs |
| U97_HROBS | Char | 15 | 0 | Hora Obs |
| U97_XSETOR | Char | 6 | 0 | Setor |
| U97_FORAGE | Char | 5 | 0 | Agencia For. |
| U97_FAGEDV | Char | 1 | 0 | DV Agencia |
| U97_FORCTA | Char | 25 | 0 | Conta For. |
| U97_FCTADV | Char | 2 | 0 | DV Conta |
| U97_FORBCO | Char | 3 | 0 | Banco For. |
| U97_XSOLIC | Char | 30 | 0 | Solicitante |
| U97_LINDIG | Char | 48 | 0 | Lin Digit |
| U97_ACRESC | Numeric | 16 | 2 | Acrescimo |
| U97_TENTAT | Numeric | 3 | 0 | Qt.Reprocess |
| U97_DTNXRT | Date | 8 | 0 | Data do Repr |
| U97_HRNXRT | Char | 10 | 0 | Hora do Repr |
| U97_OBSANT | Memo | 10 | 0 | Obs.Reproces |
**Chave primaria:** `U97_FILIAL + U97_ID`

---

### UA3 — Stage Lançamento Contábil (Custom REST)

| Atributo | Valor |
|----------|-------|
| **Modulo** | Custom — REST / Integração Contabilidade |
| **Tipo** | **Customizada** |
| **Descricao** | Stage de integração REST para lançamentos contábeis |
| **Uso no projeto** | stage_contabil.tlpp |

**Campos (25 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| UA3_FILIAL | Char | 4 | 0 | Filial |
| UA3_DATA | Date | 8 | 0 | Data Lanc |
| UA3_IDV | Char | 15 | 0 | ID VENDA |
| UA3_ITEMV | Char | 15 | 0 | ITEM VENDA |
| UA3_PCRINT | Char | 20 | 0 | Processo Int |
| UA3_CODIGO | Char | 9 | 0 | Codigo |
| UA3_DC | Char | 1 | 0 | Deb./Cred. |
| UA3_CONTA | Char | 20 | 0 | Conta Contab |
| UA3_CC | Char | 20 | 0 | Centro Custo |
| UA3_ITEM | Char | 9 | 0 | Item Contab |
| UA3_CLVL | Char | 9 | 0 | Classe Valor |
| UA3_VALOR | Numeric | 14 | 2 | Valor |
| UA3_DTOBS | Date | 8 | 0 | DT OBS |
| UA3_CODOBS | Char | 2 | 0 | COD OBS |
| UA3_OBS | Char | 250 | 0 | Per. Aquisit |
| UA3_DOCUME | Char | 40 | 0 | Documento |
| UA3_LOTE | Char | 6 | 0 | Lote |
| UA3_HIST | Char | 200 | 0 | Historico |
| UA3_DTIMP | Date | 8 | 0 | Dt Impo |
| UA3_SEQ | Char | 3 | 0 | SEQUENCIA |
| UA3_CNPJCL | Char | 14 | 0 | CNPJ CLIENTE |
| UA3_IDCLI | Char | 15 | 0 | ID CLIENTE |
| UA3_CNPJFO | Char | 14 | 0 | CNPJ FORNEC |
| UA3_IDFORN | Char | 15 | 0 | ID FORNEC |
| UA3_SBLOTE | Char | 3 | 0 | SUBLOTE |
**Chave primaria:** `UA3_FILIAL + UA3_ID`

---

### U98 — Stage Contas a Receber — Integração Legado (Custom)

| Atributo | Valor |
|----------|-------|
| **Modulo** | Custom — Financeiro / Integração Sistema Legado |
| **Tipo** | **Customizada** |
| **Descricao** | Stage de integração REST/Job para Contas a Receber vindos do sistema legado |
| **Uso no projeto** | SCHBBPRCU98.tlpp (Job de processamento) |

**Campos (77 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| U98_FILIAL | Char | 4 | 0 | Filial |
| U98_PREFIX | Char | 3 | 0 | Prefixo |
| U98_NUM | Char | 9 | 0 | No. Titulo |
| U98_PARCEL | Char | 3 | 0 | Parcela |
| U98_TIPO | Char | 3 | 0 | Tipo |
| U98_NATURE | Char | 10 | 0 | Natureza |
| U98_PORTAD | Char | 3 | 0 | Portador |
| U98_AGEDEP | Char | 5 | 0 | Depositaria |
| U98_CLIENT | Char | 15 | 0 | Cliente |
| U98_LOJA | Char | 2 | 0 | Loja |
| U98_EMISSA | Date | 8 | 0 | DT Emissao |
| U98_VENCTO | Date | 8 | 0 | Vencimento |
| U98_VENCRE | Date | 8 | 0 | Vencto real |
| U98_VALOR | Numeric | 16 | 2 | Vlr.Titulo |
| U98_NUMBCO | Char | 15 | 0 | Nº no Banco |
| U98_HIST | Char | 40 | 0 | Historico |
| U98_SALDO | Numeric | 16 | 2 | Saldo |
| U98_CONTA | Char | 10 | 0 | Num da Conta |
| U98_MOEDA | Numeric | 2 | 0 | Moeda |
| U98_CODBAR | Char | 44 | 0 | Codig.Barras |
| U98_CODDIG | Char | 48 | 0 | Codig.Digita |
| U98_BCOCLI | Char | 3 | 0 | Banco Client |
| U98_AGECLI | Char | 5 | 0 | Agencia Cli. |
| U98_CTACLI | Char | 25 | 0 | Conta Cli. |
| U98_XNUMTI | Char | 10 | 0 | Num. Titulo |
| U98_XCARTA | Char | 16 | 0 | Num Cartao |
| U98_XVLDCR | Date | 8 | 0 | Val Cartao |
| U98_XCNVCR | Char | 10 | 0 | Conv Cartao |
| U98_XVLRCO | Numeric | 14 | 2 | Vlr Comissão |
| U98_XFORCO | Char | 14 | 0 | Fornec Com |
| U98_XCODPE | Char | 10 | 0 | Cód Periodo |
| U98_XNUMNE | Char | 10 | 0 | Numero Neg |
| U98_XVLRBX | Numeric | 14 | 2 | Valor Baixa |
| U98_XEFETB | Char | 2 | 0 | Efetua Bx |
| U98_TIPOIN | Char | 1 | 0 | Tipo integra |
| U98_TIPOBX | Char | 3 | 0 | Tp Baixa |
| U98_DTBAIX | Date | 8 | 0 | Dt Baixa |
| U98_IDSTAG | Char | 50 | 0 | IDSTAGE |
| U98_DTIMPO | Date | 8 | 0 | Dt Import |
| U98_HRIMPO | Char | 15 | 0 | Hr import |
| U98_OBS | Memo | 10 | 0 | Obs Job |
| U98_CODOBS | Char | 1 | 0 | Cod OBS |
| U98_DTOBS | Date | 8 | 0 | Dt Obs |
| U98_HROBS | Char | 15 | 0 | Hora Obs |
| U98_XIDBVT | Char | 15 | 0 | U98_XIDBVT |
| U98_XCODTR | Char | 15 | 0 | U98_XCODTR |
| U98_XTID | Char | 30 | 0 | U98_XTID |
| U98_XNTRAN | Char | 15 | 0 | U98_XNTRAN |
| U98_XMAQUI | Char | 20 | 0 | U98_XMAQUI |
| U98_XPDV | Char | 3 | 0 | U98_XPDV |
| U98_XADMCT | Char | 5 | 0 | U98_XADMCT |
| U98_XCODCV | Char | 30 | 0 | U98_XCODCV |
| U98_XNCTCR | Char | 30 | 0 | U98_XNCTCR |
| U98_VLBRUT | Numeric | 14 | 2 | Vl Bruto |
| U98_XCODLE | Char | 15 | 0 | Cod Legado |
| U98_XJUROS | Numeric | 16 | 2 | Juros |
| U98_XMULTA | Numeric | 16 | 2 | Multa |
| U98_XCORRE | Numeric | 16 | 2 | Correcao |
| U98_XDESCO | Numeric | 16 | 2 | Desconto |
| U98_A1PESS | Char | 1 | 0 | Pessoa |
| U98_A1NOME | Char | 40 | 0 | Nome |
| U98_A1NRED | Char | 20 | 0 | Nome reduzid |
| U98_A1TIPO | Char | 1 | 0 | Tipo |
| U98_A1END | Char | 40 | 0 | Endereco |
| U98_A1BAIR | Char | 30 | 0 | Bairro |
| U98_A1EST | Char | 2 | 0 | UF |
| U98_A1ESTA | Char | 20 | 0 | Estado |
| U98_A1CEP | Char | 8 | 0 | CEP |
| U98_A1CDMU | Char | 5 | 0 | COD mun |
| U98_A1MUN | Char | 60 | 0 | Municipio do |
| U98_A1CGC | Char | 14 | 0 | cgc |
| U98_A1DDD | Char | 3 | 0 | ddd |
| U98_A1TEL | Char | 15 | 0 | TEL |
| U98_A1EMAI | Char | 120 | 0 | Email |
| U98_A1CDPA | Char | 5 | 0 | Cod pais |
| U98_A1PAIS | Char | 3 | 0 | Pais |
| U98_A1NATU | Char | 10 | 0 | Natureza |
**Chave primaria:** `U98_FILIAL + U98_PREFIX + U98_NUM + U98_PARCEL + U98_TIPO + U98_CLIENT`

---

---

## Contratos / Fluig

### U13 — Stage de Medições Fluig — Contratos (Custom)

| Atributo | Valor |
|----------|-------|
| **Modulo** | Custom — Contratos (SIGAGCT) / Integração Fluig |
| **Tipo** | **Customizada** |
| **Descricao** | Stage de medições enviadas pelo Fluig para processamento no Protheus (inclusão de medição e geração de pré-nota) |
| **Uso no projeto** | GERMEDICAO.tlpp (Job de processamento de medições) |

**Campos (29 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| U13_FILIAL | Char | 4 | 0 | Filial |
| U13_CONTRA | Char | 15 | 0 | Nr. Contrato |
| U13_REVISA | Char | 3 | 0 | Revisao |
| U13_COMPET | Char | 7 | 0 | Competencia |
| U13_NOTA | Char | 9 | 0 | Numero Nf |
| U13_SERIE | Char | 3 | 0 | Serie |
| U13_EMISSA | Date | 8 | 0 | Emissao |
| U13_ITEM | Char | 3 | 0 | Item |
| U13_PRODUT | Char | 15 | 0 | Produto |
| U13_QTD | Numeric | 16 | 8 | Quantidade |
| U13_VLUNIT | Numeric | 16 | 4 | Vl. Unitario |
| U13_NUMMED | Char | 6 | 0 | Num Medicao |
| U13_DTIMPO | Date | 8 | 0 | Dt Imp |
| U13_HRIMPO | Char | 15 | 0 | Hora Imp |
| U13_CODOBS | Char | 1 | 0 | Cod Obs |
| U13_DTOBS | Date | 8 | 0 | Data Obs |
| U13_OBS | Memo | 10 | 0 | Obs |
| U13_NFLUIG | Char | 15 | 0 | Num Fluig |
| U13_PLANIL | Char | 6 | 0 | Num Planilha |
| U13_PARCEL | Char | 3 | 0 | Parcela |
| U13_DTVENC | Date | 8 | 0 | Dt Vencto |
| U13_TIPDOC | Char | 1 | 0 | Tip Doc |
| U13_OBSMED | Memo | 10 | 0 | Obs Medicao |
| U13_XCHVNF | Char | 44 | 0 | U13_XCHVNF |
| U13_CCITEM | Char | 20 | 0 | C Custo Item |
| U13_CLVLIT | Char | 9 | 0 | Clvl Item |
| U13_CONDPG | Char | 2 | 0 | Forma PGTO |
| U13_ESPECI | Char | 5 | 0 | Especie NF |
| U13_NFAT | Char | 10 | 0 | Nº Fatura |
**Chave primaria:** `U13_FILIAL + U13_NFLUIG + U13_ITEM`

---

---

## Workflow / Outros

### U05 — Cadastro Workflow (Custom)

| Atributo | Valor |
|----------|-------|
| **Modulo** | Custom — Workflow |
| **Tipo** | **Customizada** |
| **Descricao** | Cadastro de controle de Workflow |
| **Uso no projeto** | F240OK.prw (código comentado) |

**Campos (5 no dicionario):**

| Campo | Tipo | Tam. | Dec. | Titulo |
|-------|------|------|------|--------|
| U05_FILIAL | Char | 4 | 0 | Filial |
| U05_NUMBOR | Char | 6 | 0 | Núm Bordero |
| U05_CODAPR | Char | 6 | 0 | Aprovador |
| U05_DESCAP | Char | 40 | 0 | Nome Aprov |
| U05_SITUA | Char | 1 | 0 | Situacao |

---

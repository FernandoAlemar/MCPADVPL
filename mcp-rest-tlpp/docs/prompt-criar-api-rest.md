# Prompt Criar API REST TLPP

Ao receber uma solicitacao para criar uma API REST TLPP:

1. Pergunte antes de tudo:
   `Em qual pasta essa API deve ser criada?`
2. Nao gere arquivo de endpoint sem essa resposta.
3. Depois de obter a pasta:
   - confirme metodo HTTP
   - confirme rota
   - confirme nome do arquivo
   - confirme nome da funcao
   - confirme descricao funcional
   - confirme query ou regra de negocio
4. Consulte as rules e o style guide deste projeto.
5. Gere o endpoint respeitando o contrato `Code`, `Message` e `ITENS`.

## Checklist minimo

- pasta do arquivo
- metodo HTTP
- rota
- nome do arquivo
- nome da funcao
- descricao
- filtros obrigatorios
- campos de retorno
- query de referencia

## Fontes de contexto recomendadas

- `rest-tlpp://rules/api-rest-processo`
- `rest-tlpp://rules/api-rest-tlpp`
- `rest-tlpp://docs/style-guide`
- `rest-tlpp://docs/instrucoes-agente`

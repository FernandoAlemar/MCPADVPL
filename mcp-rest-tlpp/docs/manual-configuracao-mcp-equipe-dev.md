# Manual de Configuracao - MCP REST TLPP (Equipe DEV)

Este manual permite configurar o MCP `rest-tlpp` em um ambiente local.

## 1. O que voce precisa

- Python 3.10 ou superior
- Cursor ou VS Code com suporte a MCP
- acesso a esta pasta do projeto

Na raiz do projeto devem existir:

```text
server.py
requirements.txt
pyproject.toml
docs/
rules/
```

## 2. Criar ambiente virtual

### Windows

```powershell
cd CAMINHO_DO_PROJETO
python -m venv .venv
.venv\Scripts\activate
```

Se `python` nao funcionar:

```powershell
py -3 -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
cd CAMINHO_DO_PROJETO
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 4. Validar ambiente

```bash
python -c "from mcp.server.fastmcp import FastMCP; print('OK')"
```

## 5. Configurar no Cursor

Crie ou edite `.cursor/mcp.json` no projeto que vai consumir este MCP:

```json
{
  "mcpServers": {
    "rest-tlpp": {
      "command": "CAMINHO_ABSOLUTO_ATE_MCP_REST_TLPP/.venv/Scripts/python.exe",
      "args": ["CAMINHO_ABSOLUTO_ATE_MCP_REST_TLPP/server.py"],
      "cwd": "CAMINHO_ABSOLUTO_ATE_MCP_REST_TLPP"
    }
  }
}
```

## 6. Configurar no VS Code

Detalhes em **docs/configurar-vscode.md**. Resumo:

- **Workspace = pasta mcp-rest-tlpp:** use o `.vscode/mcp.json` do proprio projeto (com `"command": "${workspaceFolder}/.venv/Scripts/python.exe"`).
- **Workspace = outro projeto (ex.: Protheus):** crie `.vscode/mcp.json` nesse projeto com caminho absoluto para o Python e o `server.py` do mcp-rest-tlpp.
- **Qualquer projeto:** use o comando **MCP: Open User Configuration** e adicione o servidor com caminho absoluto.

## 7. Reiniciar o editor

Depois de alterar a configuracao do MCP, reinicie o Cursor ou o VS Code.

## 8. Verificar se esta funcionando

Confirme se o servidor aparece listado e se os resources abaixo ficam disponiveis:

- `rest-tlpp://docs/style-guide`
- `rest-tlpp://rules/api-rest-processo`
- `rest-tlpp://rules/api-rest-tlpp`
- `rest-tlpp://contexto/criar-api`

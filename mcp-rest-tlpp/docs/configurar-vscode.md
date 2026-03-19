# Configurar o MCP rest-tlpp no VS Code

O VS Code usa o arquivo `mcp.json` para definir os servidores MCP. Você pode configurar no **workspace** (só neste projeto) ou no **perfil do usuário** (todos os projetos).

---

## Onde fica o mcp.json

| Local | Caminho | Uso |
|-------|---------|-----|
| **Workspace** | `.vscode/mcp.json` na raiz do projeto aberto | Só quando essa pasta for a raiz do workspace |
| **Usuário** | Abrir pelo comando **MCP: Open User Configuration** | Vale para qualquer projeto |

---

## Cenário 1: Workspace é a pasta do MCP (`mcp-rest-tlpp`)

Se você abre no VS Code a pasta `mcp-rest-tlpp` como raiz do workspace, use o `.vscode/mcp.json` que já existe:

```json
{
  "servers": {
    "rest-tlpp": {
      "type": "stdio",
      "command": "${workspaceFolder}/.venv/Scripts/python.exe",
      "args": ["${workspaceFolder}/server.py"]
    }
  }
}
```

- **Windows:** `${workspaceFolder}/.venv/Scripts/python.exe`
- **macOS/Linux:** use `${workspaceFolder}/.venv/bin/python` no `command`

Antes de abrir, crie o venv e instale as dependências na pasta do MCP:

```powershell
cd D:\PROTHEUS-ADVPL-GIT\mcp-rest-tlpp
py -3 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## Cenário 2: Workspace é outro projeto (ex: Protheus-ADVPL)

Se você trabalha no projeto principal e quer que o MCP funcione lá, crie ou edite `.vscode/mcp.json` **nesse projeto** com o **caminho absoluto** do MCP:

**Exemplo no projeto Protheus-ADVPL** (ajuste o caminho se for outro):

`.vscode/mcp.json` na raiz do workspace Protheus:

```json
{
  "servers": {
    "rest-tlpp": {
      "type": "stdio",
      "command": "D:/PROTHEUS-ADVPL-GIT/mcp-rest-tlpp/.venv/Scripts/python.exe",
      "args": ["D:/PROTHEUS-ADVPL-GIT/mcp-rest-tlpp/server.py"]
    }
  }
}
```

No Windows pode usar barras `/` ou `\\`. Troque `D:/PROTHEUS-ADVPL-GIT` pelo caminho real da sua máquina.

---

## Configuração no perfil do usuário (qualquer projeto)

1. **Ctrl+Shift+P** (ou **Cmd+Shift+P** no Mac) → digite: **MCP: Open User Configuration**
2. Será aberto o `mcp.json` do usuário. Adicione o servidor:

```json
{
  "servers": {
    "rest-tlpp": {
      "type": "stdio",
      "command": "D:/PROTHEUS-ADVPL-GIT/mcp-rest-tlpp/.venv/Scripts/python.exe",
      "args": ["D:/PROTHEUS-ADVPL-GIT/mcp-rest-tlpp/server.py"]
    }
  }
}
```

3. Salve. O MCP ficará disponível em qualquer workspace.

---

## Comandos úteis no VS Code

| Comando | Descrição |
|---------|-----------|
| **MCP: Open User Configuration** | Abre o `mcp.json` do usuário |
| **MCP: Open Workspace Folder MCP Configuration** | Abre o `.vscode/mcp.json` do workspace |
| **MCP: List Servers** | Lista servidores; permite Iniciar, Parar, Reiniciar, Ver saída |
| **MCP: Browse Resources** | Ver resources dos servidores MCP |

---

## Verificar se está funcionando

1. **Ctrl+Shift+P** → **MCP: List Servers**
2. O servidor **rest-tlpp** deve aparecer. Se estiver parado, use **Start**.
3. No Copilot Chat (ou ferramenta que use MCP), os resources e o prompt `criar_api_rest_tlpp` devem estar disponíveis.

Se o servidor não iniciar, use **Show Output** em **MCP: List Servers** para ver erros (por exemplo, Python ou caminho do `server.py` incorreto).

---

## Resumo rápido

- **Só no projeto MCP:** use `.vscode/mcp.json` com `${workspaceFolder}` (já existe no repositório).
- **No projeto Protheus (ou outro):** crie `.vscode/mcp.json` nesse projeto com o caminho absoluto do `mcp-rest-tlpp`.
- **Em todo lugar:** use **MCP: Open User Configuration** e coloque o mesmo bloco com caminho absoluto.

Depois de alterar o `mcp.json`, reinicie o VS Code ou use **MCP: List Servers** → Restart no servidor **rest-tlpp**.

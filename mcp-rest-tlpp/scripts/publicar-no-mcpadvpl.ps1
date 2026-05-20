# Sincroniza esta pasta com MCPADVPL/mcp-rest-tlpp e faz commit + push no monorepo.
param(
    [Parameter(Mandatory = $true)]
    [string]$CommitMessage
)

$ErrorActionPreference = "Stop"
$src = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$mcadvplRoot = Join-Path (Split-Path $src -Parent) "MCPADVPL"
$dst = Join-Path $mcadvplRoot "mcp-rest-tlpp"

if (-not (Test-Path (Join-Path $mcadvplRoot ".git"))) {
    Write-Error "Clone o monorepo primeiro: git clone https://github.com/FernandoAlemar/MCPADVPL.git em $mcadvplRoot"
}

robocopy $src $dst /MIR /XD .git .venv data\dicionario data\_dicionario_clone __pycache__ /XF .cursor\mcp.json /NFL /NDL /NJH /NJS | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy falhou com codigo $LASTEXITCODE" }

Push-Location $mcadvplRoot
try {
    git add mcp-rest-tlpp
    $status = git status --porcelain mcp-rest-tlpp
    if (-not $status) {
        Write-Host "Nenhuma alteracao em mcp-rest-tlpp para commitar."
        exit 0
    }
    git commit -m $CommitMessage
    git push origin main
    Write-Host "Publicado em https://github.com/FernandoAlemar/MCPADVPL"
}
finally {
    Pop-Location
}

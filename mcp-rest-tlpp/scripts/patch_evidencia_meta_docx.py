"""Atualiza Evidência Meta Estrutura.docx: 4 oportunidades + seção 4.4 MCP REST TLPP."""
from __future__ import annotations

import shutil
import zipfile
from pathlib import Path

DOCX = Path(r"d:\backup\BACKUP11-11\META PDF\2026\Evidência Meta Estrutura.docx")
BACKUP = DOCX.with_suffix(DOCX.suffix + ".bak")

OLD_INTRO = (
    "No escopo do projeto MCP FLUIG foram identificadas três oportunidades concretas de uso de IA "
    "no desenvolvimento e na virada tecnológica, atendendo ao critério de "
    "\u201cidentificar ao menos 3 oportunidades\u201d."
)
NEW_INTRO = (
    "Foram identificadas quatro oportunidades concretas de uso de IA no desenvolvimento Fluig/ADVPL "
    "e na virada tecnológica, cobrindo formulários e datasets Fluig, revisão Voyager 2.0 e "
    "APIs REST TLPP no Protheus (servidor MCP mcp-rest-tlpp), atendendo ao critério de "
    "\u201cidentificar ao menos 4 oportunidades\u201d."
)

OLD_GATILHO_SNIP = "\u22653 oportunidades de IA; 1 POC funcional; documentação parcial da metodologia."
NEW_GATILHO_SNIP = "\u22654 oportunidades de IA; 1 POC funcional; documentação parcial da metodologia."

ANCHOR_BEFORE_SEC5 = (
    "fluig-voyager-2.0).</w:t></w:r></w:p><w:p><w:pPr><w:pStyle w:val=\"Heading1\"/></w:pPr>"
    "<w:r><w:t>5. POCs planejados / validação (caminho para 80% e 100%)</w:t></w:r></w:p>"
)

SEC_4_4 = (
    "<w:p><w:pPr><w:pStyle w:val=\"Heading2\"/></w:pPr><w:r><w:t>4.4 APIs REST TLPP (Protheus) com MCP</w:t>"
    "</w:r></w:p><w:p><w:r><w:t>Acelerar a criação e a padronização de APIs REST em TLPP no Protheus com "
    "servidor MCP que expõe style guide, rules, manuais, dicionário de dados e ferramentas de validação, "
    "especificação e geração de template (projeto mcp-rest-tlpp: integração com Cursor/VS Code).</w:t>"
    "</w:r></w:p>"
)

OLD_POC_TAIL = (
    "issues registradas).</w:t></w:r></w:p><w:p><w:r><w:t>Para Limite (120%): incluir terceiro POC "
    "(ex.: combinação datasets + revisão Voyager) e registrar processo reutilizável para o time, "
    "apresentação a stakeholders e roadmap de expansão do uso de IA até março/2026.</w:t></w:r></w:p>"
)
NEW_POC_TAIL = (
    "issues registradas); ou (C) POC APIs REST TLPP – piloto com criação/validação assistida de "
    "endpoints no Protheus via MCP (mcp-rest-tlpp), medindo tempo até aprovação técnica.</w:t></w:r></w:p>"
    "<w:p><w:r><w:t>Para Limite (120%): incluir terceiro POC (ex.: combinação datasets + revisão Voyager "
    "ou APIs REST TLPP) e registrar processo reutilizável para o time, apresentação a stakeholders e "
    "roadmap de expansão do uso de IA até março/2026.</w:t></w:r></w:p>"
)


def main() -> None:
    if not DOCX.is_file():
        raise SystemExit(f"Arquivo não encontrado: {DOCX}")

    if not BACKUP.is_file():
        shutil.copy2(DOCX, BACKUP)

    with zipfile.ZipFile(DOCX, "r") as zin:
        xml = zin.read("word/document.xml").decode("utf-8")

    if OLD_INTRO not in xml:
        raise SystemExit("Texto do parágrafo introdutório (4) não encontrado; abortando.")
    if OLD_GATILHO_SNIP not in xml:
        raise SystemExit("Trecho do Gatilho (≥3 oportunidades...) não encontrado; abortando.")
    if ANCHOR_BEFORE_SEC5 not in xml:
        raise SystemExit("Âncora antes da seção 5 não encontrada; abortando.")
    if OLD_POC_TAIL not in xml:
        raise SystemExit("Bloco POC/Limite não encontrado; abortando.")

    xml = xml.replace(OLD_INTRO, NEW_INTRO, 1)
    xml = xml.replace(OLD_GATILHO_SNIP, NEW_GATILHO_SNIP, 1)
    xml = xml.replace(
        ANCHOR_BEFORE_SEC5,
        "fluig-voyager-2.0).</w:t></w:r></w:p>"
        + SEC_4_4
        + "<w:p><w:pPr><w:pStyle w:val=\"Heading1\"/></w:pPr>"
        "<w:r><w:t>5. POCs planejados / validação (caminho para 80% e 100%)</w:t></w:r></w:p>",
        1,
    )
    xml = xml.replace(OLD_POC_TAIL, NEW_POC_TAIL, 1)

    new_bytes = xml.encode("utf-8")

    tmp = DOCX.with_suffix(".tmp.docx")
    with zipfile.ZipFile(DOCX, "r") as zin, zipfile.ZipFile(tmp, "w") as zout:
        for info in zin.infolist():
            data = zin.read(info.filename)
            if info.filename == "word/document.xml":
                data = new_bytes
            zout.writestr(info, data)

    tmp.replace(DOCX)
    print(f"OK: {DOCX}")
    print(f"Backup: {BACKUP}")


if __name__ == "__main__":
    main()

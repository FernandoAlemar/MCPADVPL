"""Utilitarios do dicionario Protheus."""
from __future__ import annotations
import json, re
from pathlib import Path
from typing import Any
WINDOWS_RESERVED = frozenset({"CON", "NUL"})
TIPO_LABEL = {"C": "Char", "N": "Numeric", "D": "Date", "L": "Logical", "M": "Memo"}

def project_root() -> Path:
    return Path(__file__).resolve().parent.parent

def dicionario_dir(root: Path | None = None) -> Path:
    return (root or project_root()) / "data" / "dicionario"

def meta_path(root: Path | None = None) -> Path:
    return (root or project_root()) / "data" / "dicionario-meta.json"

def normalize_tabela(codigo: str) -> str:
    return (codigo or "").strip().upper()

def table_prefix(tabela: str) -> str:
    code = normalize_tabela(tabela)
    return "_" if code in WINDOWS_RESERVED else (code[0] if code else "X")

def table_filename(tabela: str) -> str:
    code = normalize_tabela(tabela)
    return f"_{code}.json" if code in WINDOWS_RESERVED else f"{code}.json"

def table_json_path(tabela: str, root: Path | None = None) -> Path:
    return dicionario_dir(root) / "tabelas" / table_prefix(tabela) / table_filename(tabela)

def index_path(root: Path | None = None) -> Path:
    return dicionario_dir(root) / "index.json"

def _clean(v: Any) -> str:
    if v is None: return ""
    if isinstance(v, float) and v.is_integer(): return str(int(v))
    return str(v).strip()

def sx3_record_to_campo(record: dict[str, Any]) -> dict[str, Any]:
    tam = int(float(record.get("X3_TAMANHO") or 0))
    dec = int(float(record.get("X3_DECIMAL") or 0))
    c = {"campo": _clean(record.get("X3_CAMPO")), "titulo": _clean(record.get("X3_TITULO")) or _clean(record.get("X3_CAMPO")), "tipo": _clean(record.get("X3_TIPO")) or "C", "tam": tam, "dec": dec, "obrig": "x" in _clean(record.get("X3_OBRIGAT")).lower()}
    v = _clean(record.get("X3_VALID"))
    if v: c["validacao"] = v
    cb = _clean(record.get("X3_CBOX"))
    if cb: c["combo"] = cb
    return c

def build_table_object(tabela: str, campos: list[dict]) -> dict:
    code = normalize_tabela(tabela)
    return {"tabela": code, "nome": code, "nome_eng": "", "modo": "C", "arquivo": "", "campos": campos, "indices": [], "gatilhos": [], "relacionamentos": []}

def load_table_json(tabela: str, root: Path | None = None):
    p = table_json_path(tabela, root)
    if not p.is_file(): return None
    return json.loads(p.read_text(encoding="utf-8"))

def tipo_label(tipo: str) -> str:
    return TIPO_LABEL.get((tipo or "C").upper(), tipo or "C")

def parse_meta_from_markdown(md_path: Path) -> dict:
    text = md_path.read_text(encoding="utf-8")
    tabelas, secao, cur = [], "", None
    for line in text.splitlines():
        m = re.match(r"^##\s+\d+\.\s+(.+)$", line)
        if m: secao = m.group(1).strip(); continue
        t = re.match(r"^###\s+([A-Z0-9_]+)\s+[—\-]\s+(.+)$", line)
        if t and "/" not in t.group(1):
            cur = {"codigo": t.group(1).strip(), "nome": t.group(2).strip(), "secao": secao}
            tabelas.append(cur); continue
        if cur:
            for pat, key in [(r"\*\*Módulo\*\*\s*\|\s*(.+?)\s*\|", "modulo"), (r"\*\*Tipo\*\*\s*\|\s*(.+?)\s*\|", "tipo"), (r"\*\*Descrição\*\*\s*\|\s*(.+?)\s*\|", "descricao"), (r"\*\*Uso no projeto\*\*\s*\|\s*(.+?)\s*\|", "uso_no_projeto")]:
                x = re.search(pat, line)
                if x: cur[key] = x.group(1).strip()
            pk = re.match(r"^\*\*Chave Primária:\*\*\s*`(.+)`", line)
            if pk: cur["chave_primaria"] = pk.group(1).strip()
    return {"tabelas": tabelas, "versao": 1}
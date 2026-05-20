#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from dicionario_lib import load_table_json, meta_path, parse_meta_from_markdown, project_root, tipo_label

def generate_markdown(meta, root, limit=80):
    parts = ["# Dicionario do Projeto — PROTHEUS-ADVPL", "", "Subset do projeto. Campos completos: tool `consultar_tabela_dicionario`.", ""]
    secao = ""
    for e in meta.get("tabelas", []):
        c = e.get("codigo", "")
        if not c: continue
        if e.get("secao") and e["secao"] != secao:
            secao = e["secao"]; parts += ["---", "", f"## {secao}", ""]
        parts += [f"### {c} — {e.get('nome', c)}", "", "| Atributo | Valor |", "|----------|-------|"]
        for k, lb in [("modulo","Modulo"),("tipo","Tipo"),("descricao","Descricao"),("uso_no_projeto","Uso no projeto")]:
            if e.get(k): parts.append(f"| **{lb}** | {e[k]} |")
        parts.append("")
        tj = load_table_json(c, root)
        if tj and tj.get("campos"):
            campos = tj["campos"]
            parts.append(f"**Campos ({len(campos)} no dicionario):**")
            parts += ["", "| Campo | Tipo | Tam. | Dec. | Titulo |", "|-------|------|------|------|--------|"]
            for campo in (campos if limit is None else campos[:limit]):
                parts.append(f"| {campo.get('campo','')} | {tipo_label(campo.get('tipo','C'))} | {campo.get('tam','')} | {campo.get('dec',0)} | {campo.get('titulo','')} |")
            if limit and len(campos) > limit:
                parts.append(f"\n> +{len(campos)-limit} campos. Use consultar_tabela_dicionario(\"{c}\").\n")
        if e.get("chave_primaria"):
            parts.append(f"**Chave primaria:** `{e['chave_primaria']}`")
        parts += ["", "---", ""]
    return "\n".join(parts)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=project_root())
    ap.add_argument("--extract-meta", action="store_true")
    ap.add_argument("--campos-limit", type=int, default=80)
    args = ap.parse_args()
    mf = meta_path(args.root)
    if args.extract_meta or not mf.is_file():
        leg = args.root / "docs" / "dicionario-dados-protheus.md"
        meta = parse_meta_from_markdown(leg)
        mf.parent.mkdir(parents=True, exist_ok=True)
        mf.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        meta = json.loads(mf.read_text(encoding="utf-8"))
    out = args.root / "docs" / "dicionario-projeto.md"
    lim = None if args.campos_limit == 0 else args.campos_limit
    out.write_text(generate_markdown(meta, args.root, lim), encoding="utf-8")
    print(f"OK: {out}")

if __name__ == "__main__":
    main()
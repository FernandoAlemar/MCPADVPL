#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from dicionario_lib import build_table_object, dicionario_dir, index_path, normalize_tabela, project_root, sx3_record_to_campo, table_json_path, table_prefix
try:
    import ijson
except ImportError:
    ijson = None

def flush(tabela, campos, index, root, stats):
    if not tabela or not campos: return
    code = normalize_tabela(tabela)
    obj = build_table_object(code, campos)
    p = table_json_path(code, root)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    index.append({"codigo": code, "nome": code, "prefixo": table_prefix(code)})
    stats["tabelas"] += 1
    stats["campos"] += len(campos)

def convert(inp, root):
    if not ijson: raise RuntimeError("pip install ijson")
    index, stats = [], {"tabelas": 0, "campos": 0, "registros": 0}
    cur_t, cur_c = "", []
    with inp.open("rb") as f:
        for rec in ijson.items(f, "item"):
            stats["registros"] += 1
            arq = normalize_tabela(str(rec.get("X3_ARQUIVO", "")))
            if not arq: continue
            if cur_t and arq != cur_t:
                flush(cur_t, cur_c, index, root, stats); cur_c = []
            cur_t, cur_c = arq, cur_c + [sx3_record_to_campo(rec)]
            if stats["registros"] % 500000 == 0:
                print(f"  {stats['registros']:,} registros...", file=sys.stderr)
    flush(cur_t, cur_c, index, root, stats)
    index.sort(key=lambda x: x["codigo"])
    index_path(root).write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    return stats

def _clean_output(root: Path) -> None:
    import shutil
    base = dicionario_dir(root)
    tabelas = base / "tabelas"
    if tabelas.is_dir():
        shutil.rmtree(tabelas)
    tabelas.mkdir(parents=True, exist_ok=True)
    idx = index_path(root)
    if idx.is_file():
        idx.unlink()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=Path, default=Path(r"C:\Users\alemar\Downloads\Dicionário de dados PROTHEUS.json"))
    ap.add_argument("--clean", action="store_true")
    ap.add_argument("--output-root", type=Path, default=project_root())
    args = ap.parse_args()
    if args.clean:
        print("Limpando data/dicionario/...", file=sys.stderr)
        _clean_output(args.output_root)
    if not args.input.is_file():
        print("Arquivo nao encontrado", file=sys.stderr); return 1
    print("Convertendo...", file=sys.stderr)
    s = convert(args.input, args.output_root)
    print(f"OK: {s}", file=sys.stderr)
    return 0

if __name__ == "__main__":
    sys.exit(main() or 0)

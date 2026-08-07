#!/usr/bin/env python3
"""文字檔行去重 CLI"""
from __future__ import annotations
import argparse
from pathlib import Path

def main() -> None:
    p = argparse.ArgumentParser(description='文字檔行去重 CLI')
    p.add_argument("file", type=Path)
    p.add_argument("-o", "--output", type=Path)
    args = p.parse_args()
    seen: set[str] = set()
    out_lines: list[str] = []
    for line in args.file.read_text(encoding="utf-8").splitlines():
        if line in seen:
            continue
        seen.add(line)
        out_lines.append(line)
    text = "\n".join(out_lines) + ("\n" if out_lines else "")
    if args.output:
        args.output.write_text(text, encoding="utf-8")
        print(f"wrote {len(out_lines)} unique lines -> {args.output}")
    else:
        print(text, end="")

if __name__ == "__main__":
    main()

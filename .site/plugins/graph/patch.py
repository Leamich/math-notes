#!/usr/bin/env python3
"""Патч для @quartz-community/graph.

Апстрим не умеет двух вещей, которые здесь нужны:

1. Раскраска узлов по типу заметки. Родная функция цвета различает только
   «текущая / посещённая / тег», поэтому темы и понятия выглядят одинаково.
   Тип берётся из тегов узла — их проставляет экспортёр хранилища.
2. Размер подписей при зуме. Подписи лежат внутри контейнера, который
   масштабируется, и растут вместе с ним. Здесь масштаб делится на текущий
   зум, так что подпись остаётся одного размера на любом приближении.

Внимание: браузерный код графа лежит в пакете **дважды** — в `dist/index.js`
и в `dist/components/index.js`. Сборка берёт второй, поэтому патчить нужно
оба; правка только одного тихо ничего не меняет.

Как пользоваться после обновления плагина:

    rm -rf dist && cp -r ../../node_modules/@quartz-community/graph/dist ./dist
    python patch.py

Скрипт падает, если ни в одном файле не нашёл места для замены, — значит
апстрим переписал этот кусок и патч нужно чинить, а не молча выкидывать.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DIST = Path(__file__).resolve().parent / "dist"

# Цвета узлов по типу. Подобраны так, чтобы читаться и на светлой, и на
# тёмной теме: графу переопределять переменные темы неоткуда.
COLOR_TOPIC = "#e0af68"  # тема (type: index)
COLOR_COURSE = "#9ece6a"  # занятие и материалы курса

MARK = "/*пропатчено*/"

COLOR_RE = re.compile(
    r'function ([\w$]+)\(([\w$]+)\)\{var ([\w$]+)=\2\.id===([\w$]+);'
    r'return \3\?([\w$]+):([\w$]+)\.has\(\2\.id\)\|\|\2\.id\.startsWith\("tags/"\)\?([\w$]+):([\w$]+)\}'
)
LABEL_RE = re.compile(r"function ([\w$]+)\(\)\{for\(var ([\w$]+)=1/([\w$]+),")
ZOOM_RE = re.compile(
    r"(var ([\w$]+)=function\([\w$]+\)\{j=[\w$]+\.transform,[\w$]+\.scale\.set\(j\.k,j\.k\))"
)


def patch_colors(src: str) -> tuple[str, bool]:
    m = COLOR_RE.search(src)
    if not m:
        return src, False
    fn, node, _cur, here, current, visited, tertiary, gray = m.groups()
    new = (
        f"function {fn}({node}){{{MARK}"
        f"if({node}.id==={here})return {current};"
        f'if({node}.id.startsWith("tags/"))return {tertiary};'
        f"var _t={node}.tags||[];"
        f'if(_t.indexOf("тема")!==-1)return "{COLOR_TOPIC}";'
        f'if(_t.indexOf("занятие")!==-1||_t.indexOf("материалы")!==-1)return "{COLOR_COURSE}";'
        f"return {visited}.has({node}.id)?{tertiary}:{gray}}}"
    )
    return src.replace(m.group(0), new), True


def patch_label_scale(src: str) -> tuple[str, bool]:
    m = LABEL_RE.search(src)
    z = ZOOM_RE.search(src)
    if not m or not z:
        return src, False
    fn, var, scale = m.groups()
    src = src.replace(
        m.group(0), f"function {fn}(){{{MARK}for(var {var}=1/({scale}*(j&&j.k?j.k:1)),"
    )
    # Пересчитывать на каждом шаге зума, иначе размер застынет на начальном.
    src = src.replace(z.group(1), z.group(1) + f",{fn}()")
    return src, True


def main() -> int:
    if not DIST.exists():
        raise SystemExit(f"нет {DIST} — скопируй dist из node_modules")

    touched = []
    for path in sorted(DIST.rglob("*.js")):
        src = path.read_text(encoding="utf-8")
        if MARK in src:
            print(f"  {path.relative_to(DIST)}: уже пропатчен")
            continue
        src, colors = patch_colors(src)
        src, labels = patch_label_scale(src)
        if colors or labels:
            path.write_text(src, encoding="utf-8")
            what = ", ".join(n for n, ok in (("цвет", colors), ("подписи", labels)) if ok)
            print(f"  {path.relative_to(DIST)}: {what}")
            touched.append(path)

    if not touched and not any(
        MARK in p.read_text(encoding="utf-8") for p in DIST.rglob("*.js")
    ):
        raise SystemExit("ни в одном файле не нашёл, что патчить — апстрим изменился")
    return 0


if __name__ == "__main__":
    sys.exit(main())

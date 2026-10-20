# Advent of Code

Meine Lösungen für [Advent of Code](https://adventofcode.com) in Python.
Advent of Code ist ein jährlicher Adventskalender aus Programmierrätseln, jedes Rätsel hat zwei Teile.
Ich nutze es, um Algorithmen und sauberes Programmieren zu trainieren.

## Fortschritt

| Jahr | Gelöste Tage | Sterne |
|------|--------------|--------|
| 2025 | 10 / 12      | 20 ⭐  |

## Aufbau

```
AdventOfCode/
├── 2025/
│   ├── aoc_2025_01.py
│   ├── aoc_2025_02.py
│   ├── ...
│   └── Inputs/          # nicht im Repository (siehe unten)
└── requirements.txt
```

Jede Datei enthält `func1()` (Teil A) und `func2()` (Teil B).

## Ausführen

```bash
pip install -r requirements.txt
python 2025/aoc_2025_01.py
```

Die Puzzle-Inputs sind personalisiert und werden laut den Regeln von
Advent of Code nicht veröffentlicht. Zum Ausführen den eigenen Input als
`Inputs/aoc_2025_01.txt` (Name passend zur jeweiligen Python-Datei) in den Jahresordner legen.

## Lösungen 2025 im Überblick

| Tag | Thema / Technik |
|-----|-----------------|
| 01 | Modulo-Arithmetik, Simulation eines Drehschlosses |
| 02 | Mustererkennung in Strings, sich wiederholende Teilfolgen |
| 03 | Greedy-Algorithmus: größte n-stellige Zahl aus einer Ziffernfolge |
| 04 | Gitter und Nachbarschaftssuche, iterative Simulation bis zum stabilen Zustand |
| 05 | Intervalle sortieren und zusammenführen |
| 06 | Parsing und Transponieren von spaltenweise strukturierten Daten |
| 07 | Simulation, Zählen von Pfaden mit Dictionaries (dynamische Programmierung) |
| 08 | Union-Find (Disjoint Set) zum Clustern von Punkten nach Abstand |
| 09 | Computergeometrie: größtes Rechteck mit Shapely |
| 10 | Teil A: Bit-Manipulation (XOR) und Kombinatorik · Teil B: ganzzahlige lineare Optimierung (MILP) mit SciPy |

## Technik

- Python 3.9+
- Standardbibliothek (`itertools`, `functools`, `re`, `pathlib`, `math`)
- [NumPy](https://numpy.org), [SciPy](https://scipy.org), [Shapely](https://shapely.readthedocs.io)

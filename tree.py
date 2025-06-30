import os

def tree_structure(cesta, odsazeni=""):
    for polozka in os.listdir(cesta):
        cesta_polozky = os.path.join(cesta, polozka)
        print(odsazeni + polozka)
        if os.path.isdir(cesta_polozky):
            tree_structure(cesta_polozky, odsazeni + "  ")

with open("tree_structure.txt", "w", encoding="utf-8") as f:
    import sys
    sys.stdout = f
    tree_structure(".")
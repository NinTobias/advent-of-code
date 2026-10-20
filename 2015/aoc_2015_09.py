inp = """
Faerun to Norrath = 129
Faerun to Tristram = 58
Faerun to AlphaCentauri = 13
Faerun to Arbre = 24
Faerun to Snowdin = 60
Faerun to Tambi = 71
Faerun to Straylight = 67
Norrath to Tristram = 142
Norrath to AlphaCentauri = 15
Norrath to Arbre = 135
Norrath to Snowdin = 75
Norrath to Tambi = 82
Norrath to Straylight = 54
Tristram to AlphaCentauri = 118
Tristram to Arbre = 122
Tristram to Snowdin = 103
Tristram to Tambi = 49
Tristram to Straylight = 97
AlphaCentauri to Arbre = 116
AlphaCentauri to Snowdin = 12
AlphaCentauri to Tambi = 18
AlphaCentauri to Straylight = 91
Arbre to Snowdin = 129
Arbre to Tambi = 53
Arbre to Straylight = 40
Snowdin to Tambi = 15
Snowdin to Straylight = 99
Tambi to Straylight = 70
"""

inp = [i for i in inp.split("\n") if i != ""]
inp_real = []
set_of_cities = []
for i in inp:
    x = i.split(" ")
    inp_real.append([x[0], x[2], x[4]])
    set_of_cities.append(x[0])
    set_of_cities.append(x[2])
set_of_cities = sorted(list(set(set_of_cities)))


# Graphen-Implementierung

class Knoten:
    def __init__(self, ort : str):
        self.ort = ort
        self.flag = False

    def ort_geben(self):
        return self.ort

class Graph:
    def __init__(self, anzahl_max : int):
        self.anzahl = 0
        self.anzahl_max = anzahl_max
        self.knoten = []
        self.adjazenz = [[-1 for i in range(anzahl_max+1)] for j in range(anzahl_max+1)]

    def knoten_einfügen(self, knoten_neu : Knoten) -> bool:
        if self.anzahl <= self.anzahl_max:
            self.anzahl = self.anzahl + 1
            self.knoten.append(knoten_neu)
            return True
        else:
            return False

    def adjazenz_setzen(self, zeile : int, spalte : int, wert : int) -> bool:
        if zeile < self.anzahl and spalte < self.anzahl and zeile < self.anzahl_max:
            self.adjazenz[zeile][spalte] = wert
            self.adjazenz[spalte][zeile] = wert
            return True
        else:
            return False


g = Graph(len(set_of_cities))
for element in set_of_cities:
    g.knoten_einfügen(Knoten(element))

#for element in inp_real:
for element in inp_real:
    g.adjazenz_setzen(set_of_cities.index(element[0]), set_of_cities.index(element[1]), element[2])

for i in range(len(g.adjazenz)):
    print(g.adjazenz[i])

# Metodi per la ricerca di radici di funzioni
# Metodo delle bisezioni successive
import numpy as np
import math
import matplotlib.pyplot as plt

# Funzione di cui si vuole trovare la radice
def f(x):
    return x**2 - 3

# Epsilon = tolleranza
def bisezioniSuccessive(a, b, tolleranza):
    iterazioniNecessarie = math.ceil((np.log(b - a) - np.log(tolleranza)) / (np.log(2)) - 1)
    print("Iterazioni necessarie: %d\n" % iterazioniNecessarie)

    print("|   i   |   a   |   b   |   m   |   f(a)   |   f(b)   |   f(m)   |")
    print("-----------------------------------------------------------------")

    if (f(a) * f(b) < 0):
        
        for i in range (iterazioniNecessarie):
            m = (a + b) / 2 # Punto medio dell'intervallo [a, b]
            print("|   %d   | %5.12f | %5.12f | %5.12f | %5.12f | %5.12f | %5.12f |" % (i + 1, a, b, m, f(a), f(b), f(m)))

            if (f(a) * f(m) < 0):
            # Se la funzione cambia segno prima del punto medio, allora la radice è nell'intervallo [a, m]
                b = m 
            else:
                # Se la funzione cambia segno dopo il punto medio, allora la radice è nell'intervallo [m, b]
                a = m

    return m # Ritorna il valore della radice
    
a = 0
b = 4
tolleranza = 1.0e-7
radiceCalcolata = bisezioniSuccessive(a, b, tolleranza)
print("\nRadice calcolata: %5.12f" % radiceCalcolata)
print("Radice di f(x): %5.12f" % math.sqrt(3))
print("Distanza tra la radice calcolata e quella reale con tolleranza %e" % tolleranza)
print("|c - x*|:", abs(radiceCalcolata - math.sqrt(3)))




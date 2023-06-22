# Studio del condizionamento del prodotto

# Inserimento valori esatti per l'esperimento
x = float(input("Inserire primo fattore: "))
y = float(input("Inserire secondo fattore: "))

# Costruzione dei dati perturbati
from random import random

# Il prodotto per la costante 1.0e-6 serve per avere una perturbazione piccola sui dati esatti
deltax = random() * 1.0e-6 
deltay = random() * 1.0e-6

# Dati perturbati, costituiti dalla somma dei dati esatti più la perturbazione generata
xPerturbato = x + deltax
yPerturbato = y + deltay

# Calcolo dei prodotti
p = x * y # Prodotto dei dati esatti
pt = xPerturbato * yPerturbato # Prodotto dei dati perturbati

# Calcolo errori sui dati e sul risultato
ex = abs(x - xPerturbato) / abs(x)
ey = abs(y - yPerturbato) / abs(y)
ep = abs(p - pt) / abs(p)

# Visualizzazione risultati
print('Prodotto dati esatti %f + %f = %f' % (x, y, p))
print('Prodotto dei dati perturbati %f + %f = %f' % (xPerturbato, yPerturbato, pt))
print('Errore su x: %e' % ex)
print('Errore su y: %e' % ey)
print('Errore sul prodotto: %e' % ep)

# Il prodotto, a differenza della somma, risulterà sempre ben condizionato

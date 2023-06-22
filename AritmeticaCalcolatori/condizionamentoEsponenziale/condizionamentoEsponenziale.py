# Studio del condizionamento della funzione esponenziale f(x) = e^x

# Inserimento valori esatti per l'esperimento
x = float(input("Inserire l'esponente: "))

# Costruzione della perturbazione
from random import random

# Il prodotto per la costante 1.0e-6 serve per avere una perturbazione piccola sui dati esatti
deltax = random() * 1.0e-6 

# Per verificare il condizionamento della funzione, studio l'indice di condizionamento
kfx = abs(x)
er = kfx * abs(deltax / x)

'''
Bisogna calcolare l'indice di condizione oppure basta fare:
er = abs(x - xPerturbato) / abs(x)
'''

print('\nPerturbazione: %f' % deltax)
print('Indice di condizione: %f' % kfx)
print('Errore sulla funzione: %e' % er)
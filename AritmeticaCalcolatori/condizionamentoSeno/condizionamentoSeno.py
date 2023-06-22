# Studio del condizionamento della funzione seno
from random import random
import numpy as np

# Inserimento del valore x, argomento della funzione sin(x)
x = float(input("Inserire l'argomento di sin(x): "))

# Costruzione della perturbazione
deltax = random() * 1.0e-6
xPerturbato = x + deltax

# Calcolo della funzione sin(x)
sinx = np.sin(x)
sinPerturbato = np.sin(xPerturbato)

# Calcolo dell'errore sui dati dell'esperimento
ex = abs(x - xPerturbato) / abs(x)
esinx = abs(sinx - sinPerturbato) / abs(sinx)

# Visualizzazione dei risultati
print('Funzione seno esatta: sin(%f) = %f' % (x, sinx))
print('Funzione seno sui dati perturbati: sin(%f) = %f' % (xPerturbato, sinPerturbato))
print('Errore su x: %e' % ex)
print('Errore sul risultato: %e' % esinx)


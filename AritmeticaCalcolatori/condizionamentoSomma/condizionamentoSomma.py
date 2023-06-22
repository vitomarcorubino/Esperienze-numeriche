# Studio del condizionamento della somma

# Inserimento valori per l'esperimento

x = float(input("Inserire primo addendo: "))
y = float(input("Inserire secondo addendo: "))

# Costruzione dei dati perturbati
from random import random

deltax = random() * 1.0e-6
deltay = random() * 1.0e-6

xt = x + deltax
yt = y + deltay

# Calcolo delle somme
s = x + y
st = xt + yt

# Calcolo errori sui dati e sul risultato
ex = abs(x - xt) / abs(x)
ey = abs(y - yt) / abs(y)
es = abs(s - st) / abs(s)

# Visualizzazione risultati
print('Somma dati esatti %f + %f = %f' % (x, y, s))
print('Somma dei dati perturbati %f + %f = %f' % (xt, yt, st))
print('Errore su x: %e' % ex)
print('Errore su y: %e' % ey)
print('Errore sulla somma: %e' % es)

# La somma risulterà mal condizionata se i dati x è vicino a -y


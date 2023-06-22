# Calcolo dell'Epsilon-Machine

U = 1.0

while U + 1 > 1:
    Umem = U
    U = U / 2

em = Umem

print('Epsilon machine = %e' % em)

# Calcolo precisione
import numpy as np

p = 1 - np.log(em) / np.log(2)

print('Precisione p = %d' % p)
# Regressione lineare per mercato immobiliare
import numpy as np
import matplotlib.pyplot as plt

# Superfici degli appartamenti
S = np.array([1.0, 2.0, 2.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
# Prezzi degli appartamenti
C = np.array([1.6, 2.5, 3.0, 2.8, 3.5, 4.5, 4.5, 5.0, 5.7, 6.4])

# Mostro la relazione tra superficie e costo
plt.figure(1)
plt.plot(S, C, 'r*')
plt.xlabel('Superficie')
plt.ylabel('Costo')

n = len(S)
A = np.zeros((n, 2))
A[:, 0] = S
A[:, 1] = np.ones(n)

# Costruisco la pseudo-inversa di A
U, S, Vt = np.linalg.svd(A, full_matrices = False) # Uso la versione economy
Ap = Vt.T @ np.diag(1/S) @ U.T

# Calcolo la soluzione del sistema in cui il vettore b dei termini noti è il vettore dei costi C
x = Ap @ C

# Mostro la retta di regressione
# Si cerca la retta che meglio approssima i dati e che quindi abbia distanza minima dai punti
s = np.array([1.0, 10.0])
y = x[0]*s + x[1]
plt.plot(s, y, 'b-')
plt.show()



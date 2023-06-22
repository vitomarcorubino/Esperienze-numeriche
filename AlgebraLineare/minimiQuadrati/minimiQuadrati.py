# Problema dei minimi quadrati
import numpy as np

A = np.array([[1, 1], [2, -1], [3, 1]])

b = np.array([0, 3, 1]) # vettore dei termini noti

# Calcolo SVD
U, S, Vt = np.linalg.svd(A, full_matrices = False) # Uso la versione econsomy

# Costruisco la pseudo-inversa di A
# Faccio Vt.t, cioè la trasposta della trasposta di V, per ottenere V
# Devo fare questo passaggio perchè il calcolo di SVD restituisce la trasposta di V
# quindi devo riportarla alla forma originale
Ap = Vt.T @ np.diag(1/S) @ U.T

# Dovrebbe essere zero (il calcolatore effettua errori di arrotondamento)
print('\nA Ap A - A  = %e' % np.linalg.norm(A @ Ap @ A - A)) 

# Risoluzione problema ai minimi quadrati mediante pseudo-inversa
# Calcolo la soluzione del sistema
x = Ap @ b
bb = A @ x

print('Confronto tra b e bb = A*x')

for i in range (A.shape[0]):
    print('i = %d b[i] = %f bb[i] = %f' % (i, b[i], bb[i]))




# Fattorizzazione SVD
import numpy as np

# Costruzione matrice rettangolare
n = 5 ; m = 2
A = np.random.random((n, m))

# Calcolo e verifica della SVD
U, S, Vt = np.linalg.svd(A, full_matrices = False) # Si usa la versione economy
AA = U @ np.diag(S) @ Vt
print('|| A - USVt || = %e' % np.linalg.norm(A - AA))

# Costruiamo una matrice di rango basso, ossia non tutte le colonne sono linearmente indipedenti
n = 10 ; m = 4
A = np.zeros((n, m))
A[:,0] = np.ones(n) # La prima colonna è costituita da tutti 1
A[:,1] = np.random.rand(n) # La seconda colonna è costituita da elementi pseudo-casuali
A[:,2] = 0.5 * A[:,0] + 1.5 * A[:,1] # La terza colonna è ottenuta come combinazione lineare delle prime due
                                     # (I coefficienti sono scelti casualmente)
U, S, Vt = np.linalg.svd(A, full_matrices = False) # Si usa la versione economy

print('\nValori singolari')
for i in range(m):
    print('S[%d] = %e' % (i, S[i]))

print('\nRango della matrice A = %d' % np.linalg.matrix_rank(A))

# Costruzione della pseudo-inversa
tolleranza = 1.0e-15 # Tolleranza perchè alcuni valori singolari sono molto piccoli ma non sempre 0
p = np.where(S <= tolleranza)[0][0] # Indici dei valori singolari che sono minori della tolleranza
Ap = Vt.T[0: p, :] @ np.diag(1 / S[0: p]) @ U[:, 0: p].T # Pseudo-inversa ottenuta con i valori singolari diversi da 0

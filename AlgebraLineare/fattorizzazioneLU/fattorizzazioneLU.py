import numpy as np
import scipy.linalg as la

# Costruzione della matrice test
# Aumentando N aumenta sia il tempo di calcolo che l'errore commesso
n = 5
a = -3
b = 6
A = a + (b - a)*np.random.random((n, n))
A = np.round(A)

# Costruzione del problema test
xsol = np.ones((n, 1))
b = np.dot(A, xsol)
# Fattorizzazione LU
# P = matrice di permutazione
# L = matrice triangolare inferiore
# U = matrice triangolare superiore
P, L, U = la.lu(A)

# Verifica correttezza fattorizzazione
differenza = la.norm(A - P @ L @ U)
print('|| A - PLU || = %e' % differenza)

y = la.solve_triangular(L, P.T @ b, lower = True) # P.T fa la trasposta di P
x = la.solve_triangular(U, y, lower=False)
print('Errore risoluzione sistema: || x - xsol || = %e' % la.norm(x - xsol))




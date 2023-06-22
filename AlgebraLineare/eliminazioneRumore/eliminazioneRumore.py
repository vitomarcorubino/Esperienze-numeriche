import numpy as np
import matplotlib.pyplot as plt

#  Cancellazione rumore da un segnale audio
def segnale(t):
    y = 0.4 * t + 0.9
    return y

n = 50
t = np.linspace(1, 10, n) # Istanti di campionamento

rumore = (-1 + 2 * np.random.random(t.shape)) * 0.2 # Rumore (valori tra -0.2 e 0.2
yt = segnale(t) + rumore # Segnale campionato con rumore

plt.figure(1)
plt.plot(t, yt, '*r')
plt.xlabel('Tempo')
plt.ylabel('Segnale')


A = np.zeros((n, 2))
A[:, 0] = t
A[:, 1] = np.ones(n)

# Costruisco la pseudo-inversa
U, S, Vt = np.linalg.svd(A, full_matrices=False)
Ap = Vt.T @ np.diag(1 / S) @ U.T
x = Ap @ yt

print('Valori del segnale x[1] = %f x[2] = %f' % (x[0], x[1]))
s = np.array([0.0, 11.0])
y = x[0] * s + x[1]
plt.plot(s, y, '-b')
plt.show()



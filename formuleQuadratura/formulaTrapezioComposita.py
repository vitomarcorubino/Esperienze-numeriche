import numpy as np
import matplotlib.pyplot as plt


# Funzione test da integrare
def f(x):
    y = -6*x**2 + 16*x - 4
    # y = 2*x + 1
    return y

# Primitiva della funzione test
def F(x):
    y = -2*x**3 + 8*x**2 - 4*x
    # y = x**2 + x
    return y

# Intervallo di integrazione
a = 1
b = 2

# Numero di sottointervalli
N = 3
x = np.linspace(a, b, N + 1) # Nodi di integrazione
fx = f(x) # Valori della funzione nei nodi 
S = 0 # Somma delle aree dei trapezi
for i in range(1, N):
    S = S + fx[i]

TN = (b - a) / 2 / N * (fx[0] + 2 * S + fx[N])

# Calcolo l'integrale esatto
I = F(b) - F(a)
E = abs(I - TN)

# Stampa dei risultati
print("Integrale esatto: %f" % I)
print("Integrale trapezio composito (%d): %f" % (N, TN))
print("Errore commesso: %e" % E)

# Grafico della funzione
x = np.linspace(a-0.1, b+0.1, 200)
y = f(x)
plt.plot(x, y, "r-", label="f(x)")

xn = np.linspace(a, b, N + 1)
yn = f(xn)

for i in range (0, N):
    xx = np.array([xn[i], xn[i], xn[i+1], xn[i+1], xn[i]])
    yy = np.array([0, yn[i], yn[i+1], 0, 0])
    plt.plot(xx, yy, "b-", label="Trapezio")

plt.show()

# Studio della convergenza al crescere di N
Nmax = 100
N_range = range(0, Nmax, 5)
Err_Trap = np.zeros(len(N_range))
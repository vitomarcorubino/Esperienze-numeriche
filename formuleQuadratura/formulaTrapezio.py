import numpy as np
import matplotlib.pyplot as plt

# Funzione test da integrare
def f(x):
    y = -6 * x**2 + 16*x - 4
    #y = np.sqrt(4*x)   
    # y = 2*x + 1
    return y

# Primitiva della funzione test
def F(x):
    y = -2 * x**3 + 8*x**2 - 4*x
    # y = (4/3)*x**(3/2)
    # y = x**2 + x
    return y

# Intervallo di integrazione
a = 1
b = 2

# Calcolo formula del trapezio
T = (b - a) / 2 * (f(a) + f(b))

# Calcolo l'integrale esatto
I = F(b) - F(a)
E = abs(I - T)

# Stampa dei risultati
print("Integrale esatto: %f" % I)
print("Integrale trapezio: %f" % T)
print("Errore commesso: %e" % E)

# Grafico della funzione
x = np.linspace(a-0.1, b+0.1, 200)
y = f(x)
plt.plot(x, y, "r-", label="f(x)")

# Grafico del trapezio
# Coordinate x e y dei vertici del trapezio
xx = np.array([a, a, b, b, a]) 
yy = np.array([0, f(a), f(b), 0, 0])
plt.plot(xx, yy, "b-", label="Trapezio")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()





import numpy as np
import matplotlib.pyplot as plt
import interpolazioneLagrange as interpolazione

# Funzione test da integrare
def f(x):
    y = np.sqrt(4*x)
    # y = 2*x + 1
    return y

# Primitiva della funzione test
def F(x):
    y = (4/3)*x**(3/2)
    # y = x**2 + x
    return y

# Intervallo di integrazione
a = 1
b = 9
c = (a + b) / 2 # Punto medio dell'intervallo

# Calcolo formula di Simpson
S = (b - a) / 6 * (f(a) + 4*f((a+b)/2) + f(b))

# Calcolo l'integrale esatto
I = F(b) - F(a)
E = abs(I - S) # Errore commesso

# Stampa dei risultati
print("Integrale esatto: %f" % I)
print("Integrale Simpson: %f" % S)
print("Errore commesso: %e" % E)

# Grafico della funzione
x = np.linspace(a-0.1, b+0.1, 200)
y = f(x)
plt.plot(x, y, "r-", label="f(x)")

# Grafico del polinomio di interpolazione usando Lagrange
# Dati di interpolazione
n = 2 # Grado del polinomio
x_nodi = np.linspace(a, b, n+1)
y_nodi = f(x_nodi)

x = np.linspace(a,b,200)
p = interpolazione.Lagrange(x_nodi,y_nodi,x)
f = f(x)

# Visualizzazione dei risultati
plt.figure(1)
plt.plot(x,p,'b-',label='p_2(x)')
plt.plot(x_nodi,y_nodi,'r.')
plt.xlabel('x')
plt.legend()
plt.show()



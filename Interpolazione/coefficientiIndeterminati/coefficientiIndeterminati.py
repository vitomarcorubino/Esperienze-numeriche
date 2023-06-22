import numpy as np
import matplotlib.pyplot as plt

# Funzione da interpolare
def fun(x):
    y = 1 + np.sin(x) + 3 * np.cos(2 * x)
    return y

# Dati del problema
n = 20 # Grado del polinomio
x_nodi = np.linspace(0, 2 * np.pi, n + 1) # n + 1 Nodi equispaziati tra 0 e 2pi
y_nodi = fun(x_nodi) # Valori della funzione nei nodi

# Costruzione del polinomio di interpolazione
# con metodo dei coefficienti indeterminati
c = np.polyfit(x_nodi, y_nodi, n) # Coefficienti del polinomio esatto
x_grafico = np.linspace(0, 2 * np.pi, 200) # Ascisse dei punti del grafico
pn = np.polyval(c, x_grafico) # Valori del polinomio nei punti x_grafico

# Rappresentazione grafica dei risultati
# I nodi mostrati sono i vincoli di interpolazione, cioè i punti da cui deve passare la curva della funzione
plt.figure(1)
plt.plot(x_nodi, y_nodi, 'ro')
plt.plot(x_grafico, fun(x_grafico), 'b-', label = 'f(x)')
plt.plot(x_grafico, pn, 'k--', label = 'p_n(x)')
plt.xlabel('x')
plt.legend()
plt.title('Polinomio interpolazione sui dati esatti')

# Calcolo dell'errore di interpolazione
yt = y_nodi + (2 * np.random.random(n + 1) - 1) * 0.01 # Sposto al massimo di 0.01 i punti della funzione
# Polyfit è mal condizionata perchè usa la matrice di Vandermonde
ct = np.polyfit(x_nodi, yt, n) # Coefficienti del polinomio perturbato
pnt = np.polyval(ct, x_grafico) # Valori del polinomio nei punti x_grafico

# Rappresentazione grafica dei risultati
plt.figure(2)
plt.plot(x_nodi, yt, 'ro')
plt.plot(x_grafico, fun(x_grafico), 'b-', label = 'f(x)')
plt.plot(x_grafico, pnt, 'k--', label = 'p_n(x)')
plt.xlabel('x')
plt.legend()
plt.title('Polinomio interpolazione sui dati perturbati')
plt.show()





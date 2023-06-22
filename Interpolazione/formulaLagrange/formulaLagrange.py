import numpy as np
import matplotlib.pyplot as plt

# Calcolo dei coefficienti zj
def Z_coeff(x_nodi,y_nodi): 
    n = len(x_nodi)
    X = np.ones((n,n))
    for i in range(n):
        for j in range(n):
            if j > i:
                X[i,j] = x_nodi[i]-x_nodi[j]
            else:
                if j < i:
                    X[i,j] = -X[j,i]
    z = np.zeros(n)
    for j in range(n):
        z[j] = y_nodi[j]/np.prod(X[j,:])
    return z

# Calcolo polinomio di Lagrange
# x_nodi : nodi di interpolazione
# y_nodi : valori associati ai nodi
# x : punto o punti in cui calcolare il polinomio
def Lagrange(x_nodi, y_nodi, x):
    tolleranza = 1e-14 # Tolleranza per il confronto tra x[i] e x_nodi[j]
    n = len(x_nodi) # Numero di nodi
    
    # Calcolo dei coefficienti zj
    z = Z_coeff(x_nodi,y_nodi)

    # Calcolo polinomio nei punti di x
    p = np.zeros(len(x))
    
    for i in range(len(x)):
        check = abs(x[i] - x_nodi) < tolleranza # Controllo se x[i] è molto vicino ad un nodo
        if True in check:
            # Determino quale nodo è uguale a x[i]
            temp = np.where(check == True)
            j = temp[0][0]
            p[i] = y_nodi[j] 
        else:
            S = 0 
            for j in range(n):
                S = S + z[j] / (x[i]-x_nodi[j])
            p[i] = np.prod(x[i]-x_nodi) * S
    
    return p

# Prova interpolazione di Lagrange
def f(x):
    y = np.sin(x)
    return y

# Dati di interpolazione
# Intervallo di interpolazione
a = 0
b = 2*np.pi
# Grado del polinomio
n = 5
x_nodi = np.linspace(a, b, n + 1)
y_nodi = f(x_nodi)

# Calcolo del polinomio di interpolazione e della funzione
x = np.linspace(a, b, 200) # Punti in cui calcolare il polinomio
p = Lagrange(x_nodi, y_nodi, x)
f = f(x) # Valori della funzione nei punti di x

# Visualizzazione dei risultati
plt.figure(1)
plt.plot(x, f, 'k-', label='f(x)')
plt.plot(x, p, 'b-', label='p_n(x)')
plt.plot(x_nodi, y_nodi,'r.')
plt.xlabel('x')
plt.legend()
plt.show()



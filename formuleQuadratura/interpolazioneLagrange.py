import numpy as np

# Calcolo dei coefficienti zj
def Z_coeff(x_nodi,y_nodi):
    n = len(x_nodi)
    X = np.ones((n,n))
    for i in range(n):
        for j in range(n):
            if j > i:
                X[i,j] = x_nodi[i]-x_nodi[j]
            elif j < i:
                X[i,j] = -X[j,i]
    z = np.zeros(n)
    for j in range(n):
        z[j] = y_nodi[j]/np.prod(X[j,:])
    return z

# Calcolo polinomio di Lagrange
# x_nodi : nodi di interpolazione
# y_nodi : valori associati ai nodi
# x : punto o punti in cui calcolare il polinomio
def Lagrange(x_nodi,y_nodi,x):
    
    n = len(x_nodi) # Numero di nodi
    
    # Calcolo dei coefficienti zj
    z = Z_coeff(x_nodi,y_nodi)

    # Calcolo polinomio nei punti di x
    p = np.zeros(len(x))
    for i in range(len(x)):
        check = abs(x[i]-x_nodi)<1.0e-14
        if True in check:
            # Determino quale nodo è uguale a x[i]
            temp = np.where(check == True)
            j = temp[0][0]
            p[i] = y_nodi[j]
        else:
            S = 0 
            for j in range(n):
                S = S + z[j]/(x[i]-x_nodi[j])
            p[i] = np.prod(x[i]-x_nodi)*S
    
    return p


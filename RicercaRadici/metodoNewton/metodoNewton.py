# Metodo di Newton o delle tangenti per la ricerca di radici di funzioni
import math
import matplotlib.pyplot as plt
import numpy as np

# Funzione di cui si vuole trovare la radice
def f(x):
    return x**2 - 3

# Derivata della funzione di cui si vuole trovare la radice
def df(x):
    return 2*x

def Newton(x0,tolleranza, maxIterazioni):
    fx0 = f(x0) # Valore della funzione in x0
    dfx0 = df(x0) # Valore della derivata della funzione in x0


    i = 0 # Contatore delle iterazioni
    stop = 0 # Flag per l'arresto del ciclo

    print('+-------+------------------+------------------+------------------+')
    print('|   i   |        x0        |       f(x0)      |   Diff it succ.  |')
    print('|-------+------------------+------------------+------------------+')

    while i < maxIterazioni and not(stop):

        x1 = x0 - fx0/dfx0
        fx1 = f(x1)
        valFunz = abs(fx1)
        
        diffItSucc = abs(x1 - x0) 
        stop = valFunz + diffItSucc / abs(x1) < tolleranza / 5 # C = 5 scelto nell'intervallo [1, 10]
        print('|   %d   |   %e   |   %e   |   %e   |' % (i, x0, fx0, diffItSucc))
        i = i + 1

        if(not(stop)):
            x0 = x1
            fx0 = fx1
            dfx0 = df(x0)

            
            m = df(x1)
            q = fx1 - m*x1
            tangente = m*xnodi + q
            plt.plot(xnodi, tangente, 'r')
        else:
            print('+-------+------------------+------------------+------------------+')
            print("\nNumero di iterazioni effettuate: ", i)
            if not(stop):
                print("\nMetodo non converge in %d iterazioni" % i)
            return x1


# Plot della funzione f(x)
xnodi = np.linspace(0, 2.5, 100)
ynodi = f(xnodi)
plt.plot(xnodi, ynodi, 'b')

#Dati del problema
x0 = 1
tolleranza = 1.0e-5
print("Tolleranza: ", tolleranza)
maxIterazioni = 100
zeroCercato = Newton(x0, tolleranza, maxIterazioni)

if(zeroCercato != None):
    print('\nRadice ottenuta col metodo di Newton %f' % zeroCercato)
    print('|x* - x_n| = %e' % abs(zeroCercato - math.sqrt(3)))




plt.show()
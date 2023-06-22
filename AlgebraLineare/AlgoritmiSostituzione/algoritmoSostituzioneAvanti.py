import numpy as np

# Algoritmo di sostituzione in avanti
def sostituzioneAvanti(A, b):
    n = len(A) # Ottengo la dimensione della matrice A
    x = np.zeros((n, 1)) # Inizializzo il vettore soluzione

    # Il ciclo termina ad n perchè la matrice è triangolare inferiore.
    # Quindi si fermerà quando incontrerà l'ultimo valore della diagonale principale
    for i in range(n):
        somma = 0   # Inizializzo la somma a 0
        
        for j in range(i):  
           somma = somma + (A[i][j] * x[j]) # Sommo i valori della matrice A e del vettore soluzione x
        
        x[i] = (b[i] - somma) / A[i][i] # Assegno al vettore soluzione il valore calcolato

    return x

# Costruzione di una matrice test triangolare inferiore
n = 8
A = np.random.random((n, n)) # Matrice casuale
A = np.tril(A)  # Definisco A come una matrice triangolare inferiore

# Costruzione di un problema test
xs = np.ones((n, 1)) # Vettore soluzione di tutti 1
print('Vettore delle soluzioni:')
print(xs)

b = np.dot(A, xs) # Vettore dei termini noti

# Risoluzione del sistema
print('Vettore delle soluzioni calcolato:')
x = sostituzioneAvanti(A, b)    
print(x)

# Visualizzazione del risultato
for i in range(n):
    # Stampa la differenza tra il valore calcolato e il valore reale
    print('i = %d |x(i) - xs(i)| = %e' % (i, abs(x[i] - xs[i]))) 


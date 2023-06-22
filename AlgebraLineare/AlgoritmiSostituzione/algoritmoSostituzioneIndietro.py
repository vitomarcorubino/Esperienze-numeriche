import numpy as np

# Algoritmo di sostituzione all'indietro
def SostituzioneIndietro(A, b):
    n = len(A) # Ottengo la dimensione della matrice A
    x = np.zeros((n, 1)) # Inizializzo il vettore soluzione
    
    # Indichiamo come fine del ciclo -1 perchè -1 è il primo valore da escludere dal range.
    # Quindi, il ciclo si fermerà a 0
    for i in range(n - 1, -1, -1): # (inizio, fine, step)
        somma = 0 # Inizializzo la somma

        for j in range(i + 1, n):
            somma = somma + A[i, j] * x[j] 

        x[i] = (b[i] - somma) / A[i, i]

    return x

# Costruzione di una matrice test triangolare superiore
n = 3
A = np.random.random((n, n))
A = np.triu(A) # Matrice triangolare superiore

# Costruzione di un problema test
xs = np.ones((n, 1)) # Vettore soluzione di tutti 1
b = np.dot(A, xs) # Vettore dei termini noti

# Risoluzione del sistema
# Passo come secondo argomento la soluzione ottenuta tramite il vettore soluzione
# in modo da ottenere x, cioè il vettore di termini noti [Axs = b]
print('Vettore delle soluzioni')
print(xs)

x = SostituzioneIndietro(A, b)
print('Vettore delle soluzioni calcolato')
print(x)

# Visualizzazione dell'errore tra gli elementi del vettore soluzione e il vettore calcolato
for i in range(n):
    print('i = %d |x(i) - xs(i)| = %e' % (i, abs(x[i] - xs[i])))




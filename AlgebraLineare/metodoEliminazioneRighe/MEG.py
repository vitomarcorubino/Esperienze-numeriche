import numpy as np
import scipy.linalg as la

# Algoritmo di sostituzione all'indietro
def SostituzioneIndietro(A, b):
    n = len(A) # Ottengo la dimensione della matrice A
    x = np.zeros(n) # Inizializzo il vettore soluzione
    
    # Indichiamo come fine del ciclo -1 perchè -1 è il primo valore da escludere dal range.
    # Quindi, il ciclo si fermerà a 0
    for i in range(n - 1, -1, -1): # (inizio, fine, step)
        somma = 0 # Inizializzo la somma

        for j in range(i + 1, n):
            somma = somma + A[i, j] * x[j] 

        x[i] = (b[i] - somma) / A[i, i]

    return x

# Algoritmo di eliminazione di Gauss
def MEG(A, b):
    n = len(A) # Ottengo la dimensione della matrice A

    A = np.copy(A) # Copio la matrice A in modo da non modificare quella originale
    b = np.copy(b) # Copio il vettore dei termini noti in modo da non modificarlo

    for j in range(0, n - 1):
        for i in range(j + 1, n):
            m = A[i, j] / A[j, j] # Calcolo il moltiplicatore
            A[i, j] = 0
            
            for k in range(j + 1, n):
                A[i, k] = A[i, k] - m * A[j, k]
            
            b[i] = b[i] - m * b[j] # Aggiorno il vettore dei termini noti

    return A, b # Restituisco il sistema equivalente

# Costruzione di un problema test
# Indico il primo elemento come valore reale perchè altrimenti numpy lo considera come un intero
# e questo potrebbe generare errori molto grandi quando viene applicato il MEG
A = np.array([[2.0,3,4,5], [-1,2,3,8], [2,3,1,8], [6,4,5,2]])
#A = np.array([[4.0, -4, 12], [-3, 3, 2], [0, -2, 4]])
n = len(A)

xs = np.ones((n, 1)) # Vettore soluzione di tutti 1
b = np.dot(A, xs) # Vettore dei termini noti

[U, c] = MEG(A, b) # Applico l'algoritmo di eliminazione delle righe di Gauss su A, per ottenere C
x = SostituzioneIndietro(U, c)

# Risoluzione del sistema
# Passo come secondo argomento la soluzione ottenuta tramite il vettore soluzione
# in modo da ottenere x, cioè il vettore di termini noti [Axs = b]
print('Vettore delle soluzioni')
print(xs)

# Visualizzazione dell'errore tra gli elementi del vettore soluzione e il vettore calcolato
print('\nErrore tra vettore soluzione e vettore calcolato')
for i in range(n):
    print('i = %d |x(i) - xs(i)| = %e' % (i, abs(x[i] - xs[i])))

print('\nMatrice A')
print(A)
print('\nMatrice U equivalente ad A')
print(U)

print('\ndet(A) = %20.18f' % la.det(A)) # Calcolo il determinante di A
# Siccome dopo il MEG U è diventata una matrice triangolare
# per calcolare il determinante di U basta moltiplicare gli elementi sulla diagonale
# (Era analogo utilizzare la.det(U))
print('det(U) = %20.18f' % np.prod(np.diag(U))) 

# Verifico che il determinante di A abbia una distanza minore di 1.0e-10 rispetto al determinante di U
# considerando gli errori di arrotondamento
if (abs(la.det(A) - np.prod(np.diag(U)) < 1.0e-10)): 
    print('Risultato esatto') # I determinanti si possono considerare uguali
else:
    print('Risultato errato')




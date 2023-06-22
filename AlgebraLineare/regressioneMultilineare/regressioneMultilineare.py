# Regressione multilineare
import numpy as np
import matplotlib.pyplot as plt

dati = np.genfromtxt('regressioneMultilineare\BostonHousing.csv', delimiter = ',')

# Elimino la prima riga che contiene le intestazioni
dati = dati[1:,:]

# Numero di colonne, cioè di tipo di dati
m = dati.shape[1]
A = dati[1:, 0: m - 1] # Prime m colonne
b = dati[1:, m - 1] # Ultima colonna

# Una parte dei dati la uso per il training, l'altra per il test
n = A.shape[0]
iPari = range(0, n, 2) # Indici pari
iDispari = range(1, n, 2) # Indici dispari

A_train = A[iPari, :] # Prendo le righe con indici pari
b_train = b[iPari]

A_test = A[iDispari, :] # Prendo le righe con indici dispari
b_test = b[iDispari]

# Calcolo della SVD e della pseudo-inversa del set di training
U, S, Vt = np.linalg.svd(A_train, full_matrices = False)
Ap_train = Vt.T @ np.diag(1 / S) @ U.T
x = Ap_train @ b_train

# Confronto grafico tra previsioni del modello e i valori reali
plt.figure(1)
plt.plot(b_train, label = 'Dati')
plt.legend()
plt.show()

prediction_train = A_train @ x
plt.plot(prediction_train, label = 'Previsioni')
plt.xlabel('N.ro Appartamento')
plt.ylabel('Costo')
plt.legend()

# Confronto grafico tra previsioni del modello e valori reali su un altro set di dati
plt.figure(2)
plt.plot(b_test, label = 'Dati')

prediction_test = A_test @ x # Previsioni sul set di test
plt.plot(prediction_test, label = 'Previsioni')

plt.xlabel('N.ro Appartamento')
plt.ylabel('Costo')
plt.legend()
plt.title('Dati di test')
plt.show()


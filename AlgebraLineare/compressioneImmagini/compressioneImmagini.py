# Compressione di immagini
import matplotlib.pyplot as plt # Per la visualizzazione delle immagini
import numpy as np

A = plt.imread('compressioneImmagini\\fiore.jpg')

# Visualizzazione dell'immagine
plt.figure(1)
plt.imshow(A)
plt.axis('off')
# plt.show()

# Estrazione dei vari colori
Z = np.zeros(A.shape[0:2])
Ared = np.copy(A) ; Ared[:,:,1] = Z ; Ared[:,:,2] = Z
plt.figure(2)
plt.imshow(Ared)
plt.axis('off')
# plt.show()

# Convertiamo l'immagine a colori in immagine bianco e nero
A_gray = 0.3 * A[:,:,0] + 0.3 * A[:,:,1] + 0.4 * A[:,:,2]
plt.figure(3)
plt.imshow(A_gray, cmap = 'gray')
plt.axis('off')
# plt.show()

# Calcolo della SVD
U, S, Vt = np.linalg.svd(A_gray, full_matrices = False)
m = len(S)

# Visualizzazione dei valori singolari
plt.figure(4)
plt.semilogy(range(m), S, 'r.', label = '$\sigma_i$')
plt.legend()
# plt.show()

# Costruzione immagine ridotta
N = 20
U_low = U[:,:N]
S_low = S[:N]
Vt_low = Vt[:N,:]
A_low = U_low @ np.diag(S_low) @ Vt_low
plt.figure(5)
plt.imshow(A_low, cmap = 'gray')
plt.axis('off')
plt.show()

print('A.size: ' , A.size)
print('Elementi immagine originale: ' , A_gray.size)
print('Elementi matrice ridotta: ' , S_low.size + U_low.size + Vt_low.size)









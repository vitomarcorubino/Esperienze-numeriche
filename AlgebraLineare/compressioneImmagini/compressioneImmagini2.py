# Compressione di immagini
import matplotlib.pyplot as plt # Per la visualizzazione delle immagini
import numpy as np

A = plt.imread('compressioneImmagini\\fiore.jpg')

# Visualizzazione dell'immagine
plt.figure(1)
plt.imshow(A)
plt.axis('off')

righeA = A.shape[0]
colonneA = A.shape[1]

B = np.zeros((3 * righeA, colonneA))

Z = np.zeros(A.shape[0:2])
Ared = np.copy(A) ; Ared[:,:,1] = Z ; Ared[:,:,2] = Z
Agreen = np.copy(A) ; Agreen[:,:,0] = Z ; Agreen[:,:,2] = Z 
Ablue = np.copy(A) ; Ablue[:,:,0] = Z ; Ablue[:,:,1] = Z

B[0 : righeA, :] =  Ared[:, :, 0]
B[righeA : 2 * righeA, :] = Agreen[:, :, 1]
B[2 * righeA : 3 * righeA, :] = Ablue[:, :, 2]

plt.figure(2)
plt.imshow(B)
plt.axis('off')

# Calcolo della SVD
U, S, Vt = np.linalg.svd(B, full_matrices = False)
m = len(S)

# Costruzione immagine ridotta
N = 600

U_low = U[:, : N]
S_low = S[: N]
Vt_low = Vt[: N, :]

B_low = U_low @ np.diag(S_low) @ Vt_low

X = np.zeros((righeA, colonneA, 3))
X[:, :, 0] = B_low[0 : righeA, :]
X[:, :, 1] = B_low[righeA : 2 * righeA , :]
X[:, :, 2] = B_low[2 * righeA : 3 * righeA, :]

plt.figure(3)
plt.imshow(X)
plt.axis('off')
plt.show()

print('Elementi immagine originale: ' , B.size)
print('Elementi matrice ridotta: ' , S_low.size + U_low.size + Vt_low.size)
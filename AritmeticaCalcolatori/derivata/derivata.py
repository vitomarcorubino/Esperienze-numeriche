# Calcolo della derivata prima mediante rapporto incrementale
import numpy as np
import matplotlib.pyplot as plt

# Funzione di cui calcolare la derivata
def f(x):
    y = np.sqrt(x)
    return y

# Derivata prima della funzione
def f1(x):
    y = 1 / (2 * np.sqrt(x))
    return y

# Punto in cui calcolare la derivata
x = 1

# Sequenza di passi h con cui approssimare la derivata
h_vett = np.logspace(-16, 0, 17)

# Equivale a: h_vett = np.array([1.0e-7, 1.0e-6, 1.0e-5, ... , 1.0e-2, 1.0e-0])
# -7 indica l'esponente iniziale, 0 l'esponente finale e 8 il numero di elementi da generare

# Calcolo della derivata esatta
df = f1(x)
print("Valore derivata = %.10f" % df)

# Approssimazione della derivata mediante rapporto incrementale al variare di h
errore = np.zeros(len(h_vett))

for k in range(len(h_vett)):
    h = h_vett[k]
    dfh = (f(x + h) - f(x)) / h
    print("Valore approssimato (h = %e) = %.10f" % (h, dfh))
    errore[k] = abs(df - dfh) # Calcolo dell'errore assoluto tra derivata approssimata e derivata esatta

# Grafico in scala logaritmica
plt.loglog(h_vett, errore, '*-r', label = "Errore")
plt.legend()
plt.xlabel("h")
plt.title("Errore nel calcolo della derivata")
plt.show()
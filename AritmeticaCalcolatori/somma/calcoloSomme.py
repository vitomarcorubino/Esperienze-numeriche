a = 0.25
# Se mettessi a = 0.25, cioè un numero di macchina, l'errore sarebbe 0.
N = 10

# Calcolo delle somme
S = 0

for n in range(N):
    S = S + a

# Calcolo del prodotto
P = a * N

# Visualizzazione dei risultati
print("Somma    = %.20f" % S)
print("Prodotto = %.20f" % P)
print("Differenza = %e" % abs(P - S))

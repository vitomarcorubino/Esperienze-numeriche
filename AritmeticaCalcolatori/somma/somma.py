# a = 0.5 Numero di macchina che non genera errori
a = 0.2 # Numero che genera errori di conversione

S = 0

# Verifico se la distanza tra la somma e il mio termine,
# cioè 2 è più grande di un numero vicino all'epsilon machine

while (abs(S - 3) > 10e-14):
    S = S + a
    print("La somma parziale e': %3.21f" % S)

    if (S > 10):
        break



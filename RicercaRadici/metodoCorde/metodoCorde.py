import math

def MetodoCorde(f, x0, x1, itMax, atol):
    it = 0
    stop = 0
    while it < itMax and not(stop):
        x2 = x1 - ((x1-x0)/(f(x1)-f(x0)) * f(x1))
        stop = abs(f(x2)) + abs(x2 - x1)/abs(x2) < tol
        if(not(stop)):
            x1 = x2

        it = it + 1
    if not(stop):
        print("Metodo non converge in %d iterazioni" %it)
    else:
        print("Numero di iterazioni effettuate: ", it)

    return stop, x1

def fun(x): 
    return math.pow(x, 3)-x-1

#Dati del problema
x0 = 1
x1 = 2
itMax = 100
tol = 1.0e-5
stop, zeroCercato = MetodoCorde(fun, x0, x1, itMax, tol)
if(stop):
    print("Zero di funzione:",zeroCercato)

    
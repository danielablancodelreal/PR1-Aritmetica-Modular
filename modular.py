import math

def es_primo(n):
    if n <= 1: return False
    for i in range (2,int(math.sqrt(n)+1)):
        if n%i == 0: 
            return False
    return True

def lista_primos(a,b):
    lista = []
    if a <= 2: lista.append(2) 
    if a%2 == 0: a += 1
    for i in range(a,b+1,2):
        if es_primo(i): lista.append(i)
    return lista

def factorizar(n, lista, exponentes):
    for i in range(len(lista)):
        if n%lista[i] == 0:
            p = lista.index(lista[i])
            exponentes[p] += 1
            return factorizar(int(n/lista[i]), lista, exponentes)
    return exponentes

def mcd(a,b):
    if a%b == 0 or b%a == 0: return min(a,b)
    elif a == 0 or b == 0: return max(a,b)
    else: return mcd(min(a,b), max(a,b) % min(a,b))

def coprimos(a,b):
    if a%b == 0 or b%a == 0: return False
    elif a == 0 or b == 0: return False
    else: coprimos(min(a,b), max(a,b) % min(a,b))
    return True
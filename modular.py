import sys
import math

################################ funciones #####################################
def es_primo(n):
    if n <= 1:
        return False
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
    diccionario = {}
    for j in range(len(lista)):
        diccionario[lista[j]] = exponentes[j]
    return diccionario

'''
n = 48
lista = lista_primos(2,n)
exponentes = [0]*len(lista)
factorizar(n, lista, exponentes)
'''

def mcd(a,b):
    if a < 0 or b <0: return 1
    elif a%b == 0 or b%a == 0: return min(a,b)
    elif a == 0 or b == 0: return max(a,b)
    else: return mcd(min(a,b), max(a,b) % min(a,b))

def bezout(a,b,l1,l2,mcd,a0,b0):
    if  a != mcd and b != mcd:
        c = max(a,b) // min(a,b)
        if a > b:
            l1[0] -= l2[0] *c
            l1[1] -= l2[1] *c
            a = a%b
        elif b > a:
            l2[0] -= l1[0] *c
            l2[1] -= l1[1] *c
            b = b%a
        return bezout(a,b,l1,l2,mcd,a0,b0)
    if mcd == l1[0]*a0 + l1[1]*b0:
        return(mcd, l1[0], l1[1])
    else:
        return(mcd, l2[0], l2[1])

def coprimos(a,b):
    if a < 0: a *= -1
    if b < 0: b *= -1
    if a == 1 or b == 1: return True
    elif a%b == 0 or b%a == 0: return False
    elif a == 0 or b == 0: return False
    else: coprimos(min(a,b), max(a,b) % min(a,b))
    return True

def potencia_mod_p(base, exp, p):
    if exp == p and es_primo(p):
        return (base % p)
    elif es_primo(p):
        exp = exp%(p-1)
        return (base ** exp) % p
    else:
        return (base ** exp) % p

def inversa_mod_p(n,p):
    if coprimos(n,p):
        if n<0:
            p -= n
            n *= -1
        m, x, y = bezout(n,p,[1,0],[0,1], mcd(n,p),n,p)
        return x

def euler(n):
    contador = 0
    if es_primo(n):
        return n-1
    for i in range(1,n):
        if mcd(i,n) == 1:
            contador += 1
    return(contador)

def legendre(n,p):
    if n%p == 0: return 0
    elif math.sqrt(n%p) == int(math.sqrt(n%p)): return 1
    else: return -1

def resolver_sistema_congruencias(a,b,p):
    a_ec = []
    M = 1
    for i in range(len(a)):
        a_ec.append(inversa_mod_p(a[i],p[i])*b[i])
        M *= p[i]
        
    lista = []
    for j in range(len(a_ec)):
        lista.append(inversa_mod_p((M/p[j]), p[j]))
    
    x = 0
    for k in range(len(a_ec)):
        x += a_ec[k]*lista[k]*(M/p[k])
    
    return (int(x%M), M)

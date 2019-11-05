#
# Hello
# Autor: Yeiskel Cisneros
# Lab07Ejercicio1.py
# DESCRIPCION: Un programa que dado un arreglo de enteros S de tamaño N y
#              un numero A determina cuantas veces se encuentra A en S
# Valores iniciales
N = (int(input('N: ')))
A = (int(input('A: ')))
S = [int(input("S[" + str(i) + "]= ")) for i in range(0,N)]
contador_A = 0
# Precondicion:
assert(N>0 )

# Cota N-i
for i in range(0,N):
    assert(0<=i<=N and contador_A ==sum(1 for j in range(0,i) if (S[j]==A) ))
    if S[i] == A:
        contador_A = contador_A + 1
    else:
        pass

#Postcondicion
assert(contador_A ==sum(1 for i in range(0,N) if (S[i]==A) ))

#Salida
print(contador_A)

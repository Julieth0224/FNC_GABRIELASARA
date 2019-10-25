# -*- coding: utf-8 -*-

# Subrutinas para la transformacion de una
# formula a su forma clausal

# Subrutina de Tseitin para encontrar la FNC de
# la formula en la pila
# Input: A (cadena) de la forma
#                   p=-q
#                   p=(qYr)
#                   p=(qOr)
#                   p=(q>r)
# Output: B (cadena), equivalente en FNC
def enFNC(A):
    assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    # print('p', p)
    if "-" in A:
        q = A[-1]
        # print('q', q)
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif ">" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')

    return B

# Algoritmo de transformacion de Tseitin
# Input: A (cadena) en notacion inorder
# Output: B (cadena), Tseitin
def Tseitin(A, letrasProposicionalesA):
    letrasProposicionalesB = [chr(x) for x in range(256, 300)]
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"

    # CODIGO AQUI

    return "OK"

# Subrutina Clausula para obtener lista de literales
# Input: C (cadena) una clausula
# Output: L (lista), lista de literales
def Clausula(C):

    # CODIGO AQUI

    return "OK"

# Algoritmo para obtencion de forma clausal
# Input: A (cadena) en notacion inorder en FNC
# Output: L (lista), lista de listas de literales
def formaClausal(A):

    # CODIGO AQUI

    return "OK"

# Test enFNC()
# Descomente el siguiente código y corra el presente archivo
# formula = "p=(qYr)"
# print(enFNC(formula)) # Debe obtener qO-pYrO-pY-qO-rOp

# Test Tseitin()
# Descomente el siguiente código y corra el presente archivo
# formula = "(pYq)"
# print(Tseitin(formula)) # Debe obtener AYpO-AYqO-AY-pO-qOA (la A tiene una raya encima)

# Test Clausula()
# Descomente el siguiente código y corra el presente archivo
# c = "pO-qOr"
# print(Clausula(c)) # Debe obtener ['p', '-q', 'r']

# Test formaClausal()
# Descomente el siguiente código y corra el presente archivo
# f = "pO-qOrY-sOt"
# print(formaClausal(f)) # Debe obtener [['p', '-q', 'r'], ['-s', 't']]

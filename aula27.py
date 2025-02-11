"""
Fatiamento de strings
012345678
Olá mundo
Fatiamento [1:f:p] [::]
Obs.: a função len retorna a quantidade de caractere
"""

variavel = 'Olá mundo'
print(len(variavel[7:]))
print(variavel[0:len(variavel):2])
print(variavel[0:9:1])

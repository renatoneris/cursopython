# Interpolação básica de strings
# s - strings
# d e i - int
# f - float
# x e X - hexadecimal (ABCDEF0123456789)
# """

nome = 'Renato'
preco = 1000.232434
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %X' % (18, 46))

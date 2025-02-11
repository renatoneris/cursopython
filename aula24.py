# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
# R e n a t o
#-6-5-4-3-2-1

# nome = 'Renato'
# print('h' not in nome)
# print(10 * '-')
# print('t' in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
        

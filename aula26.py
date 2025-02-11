# .<nímero de difitos>f
# x ou X - Hexadecimal
# (Caractere)(><^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# Sinal - + ou -
# Ex.: 0>-100, .1f
#Conversion flags - !r !s !a
# """
#      
variavel = 'ABC'
print(f'{variavel: >11}')
print(f'{variavel: <11}.')
print(f'{variavel: ^11}')
print(f'{1000.34435343:-,.1f}')

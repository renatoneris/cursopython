"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito -> quanto um código não tem fim
"""
contador = 0

while contador < 50:
    contador += 1

    if contador == 6:
        print('Náo vou mostrar o 6')
        continue

    if contador >= 10 and contador <=27:
        continue

    print(contador)

    if contador == 40:
        break



print('ACABOU')
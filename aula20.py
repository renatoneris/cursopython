#Exercicios

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')
primeiro = f'O primeiro valor {primeiro_valor=} é maior que segundo valor {segundo_valor=}'
segundo = f'O segundo valor {segundo_valor=} é maior que primeiro valor {primeiro_valor=}'
if primeiro_valor > segundo_valor:
    print(primeiro)
elif segundo_valor > primeiro_valor:
    print(segundo)
else:
    print('Valor igual')
    
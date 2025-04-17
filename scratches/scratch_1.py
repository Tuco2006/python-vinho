numero = float(input('Qual o número?'))
numero2 = float(input('Qual o outro número?'))
equacao = input('Deseja fazer soma, subtração, divisão ou multiplicação?')

if equacao == 'soma':
    print(f'O valor é de {numero + numero2}')
elif equacao == 'subtração':
    print(f'O valor é de {numero - numero2}')
elif equacao == 'divisão':
    print(f'O valor é de {numero // numero2}')
elif equacao == 'multiplicação':
    print(f'O valor é de {numero * numero2}')



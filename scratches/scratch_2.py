x = float(input('Qual o valor de X?'))

if x < 2:
    print('y = x')
elif 3.5 >= x:
    print('y = 2')
elif 5 > x:
    print('y = 3')
else:
    print(f'y = {(x ** 2) - (10 * x) + 28}')


nome = input('Qual seu nome?')
idade = float(input('Qual a sua idade?'))
endereço = input('Qual seu endereço?')


if idade < 18:
    print('Infelizmente não é permitida a venda de bebidas para o senhor!')

elif 60 > idade > 18:
    print(f'Seja bem vindo {nome}, de idade {idade}, segue nosso catálogo de vinhos.')
    vinho = input('Vinho X R$50, vinho Y R$60 e vinho Z R$70, qual o senhor gostaria de comprar?')
    quantidade = float(input('Quantas garrafas o senhor deseja comprar?'))

    if vinho == 'X':
        val1 = 50 * quantidade
        if val1 > 150:
            soma = val1
            print(f'O pedido está com valor de R$:{val1} (garrafas mais frete)!')
        elif val1 < 150:
            soma = val1 + 25
            print(f'O pedido ficou no valor de R$:{val1 + 25} (frete grátis)!')
    elif vinho == 'Y':
        val1 = 60 * quantidade
        if val1 > 150:
            soma = val1
            print(f'O pedido está com valor de R$:{val1} (garrafas mais frete)!')
        elif val1 < 150:
            soma = val1 + 25
            print(f'O pedido ficou no valor de R$:{val1 + 25} (frete grátis)!')
    elif vinho == 'Z':
        val1 = 70 * quantidade
        if val1 < 150:
            soma = val1 + 25
            print(f'O pedido está com valor de R$:{val1 + 25} (garrafas mais frete)!')
        elif val1 > 150:
            soma = val1
            print(f'O pedido ficou no valor de R$:{val1} (frete grátis)!')

    final = input('O senhor gostaria de finalizar seu pedido?')
    if final == 'sim':
        print(f'Obrigado pela sua compra! Seu pedido ficou no valor de R$:{soma}, para entregar no endereço: {endereço}!')
    else:
        print('Sem problemas! Volte sempre!')
elif idade >= 60:
    print(f'Seja bem vindo {nome}, de idade {idade}, segue nosso catálogo de vinhos.')
    vinho = input('Vinho X R$50, vinho Y R$60 e vinho Z R$70, qual o senhor gostaria de comprar?')
    quantidade = float(input('Quantas garrafas o senhor deseja comprar?'))

    if vinho == 'X':
        val1 = 50 * quantidade
        if val1 > 150:
            soma = val1 - (val1 * 10//100)
            print(f'O pedido está com valor de R$:{soma} (garrafas mais frete)!')
        elif val1 < 150:
            soma = (val1 - (val1 * 10//100)) + 25
            print(f'O pedido ficou no valor de R$:{soma} (frete grátis)!')
    elif vinho == 'Y':
        val1 = 60 * quantidade
        if val1 > 150:
            soma = (val1 - (val1 * 10//100))
            print(f'O pedido está com valor de R$:{soma} (garrafas mais frete)!')
        elif val1 < 150:
            soma = (val1 - (val1 * 10//100)) + 25
            print(f'O pedido ficou no valor de R$:{soma} (frete grátis)!')
    elif vinho == 'Z':
        val1 = 70 * quantidade
        if val1 < 150:
            soma = (val1 - (val1 * 10//100)) + 25
            print(f'O pedido está com valor de R$:{soma} (garrafas mais frete)!')
        elif val1 > 150:
            soma = (val1 - (val1 * 10//100))
            print(f'O pedido ficou no valor de R$:{soma} (frete grátis)!')

    final = input('O senhor gostaria de finalizar seu pedido?')
    if final == 'sim':
        print(f'Obrigado pela sua compra! Seu pedido ficou no valor de R$:{soma}, com desconto para pessoas com mais de 60 anos, para entregar no endereço: {endereço}!')
    else:
        print('Sem problemas! Volte sempre!')




print('-='*30)
print('(1)adição')
print('(2)subtração')
print('(3)multiplicação')
print('(4)divisão')
print('-='*30)
valores = int(input('Digite o valor que você deseja:'))
print('=-'*30)

num1 = int(input('digite o primeiro valor:'))
num2 = int(input('digite o segundo valor:'))
adicao = num1+num2
sub = num1-num2
mult = num1*num2
div = num1/num2


if valores == 1:
    print(f'o resultado da adição de {num1} + {num2} é igual ah:{adicao}')
elif valores == 2:
    print(f'o resultado da subtração de {num1} - {num2} é igual ah: {sub}')
elif valores == 3 :
    print(f'o resultado da multiplicação  de {num1} * {num2} é igual ah: {mult}')
elif valores == 4:
    print(f'o resultado da divisão de {num1} / {num2} é igual ah: {div}')


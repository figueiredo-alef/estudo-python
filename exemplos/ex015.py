print('=' * 5, 'EX_015', '=' * 5)
# aluguel de carros
dias = int(input('Informe quantos dias de locação: '))
km = float(input('Informe a quantidade de km rodado: '))
loc = (dias * 60) + (km * 0.15)
print('Total a pagar por {:.1f}km rodados em {} dias: R${:.2f}'.format(km, dias, loc))

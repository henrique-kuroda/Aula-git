print('Esse programa irá calcular uma equação do segundo grau de tipo ax²+bx+c')
a = float(input('Forneça o valor de a: '))
b = float(input('Forneça o valdor de b: '))
c = float(input('Forneça o valor de c: '))
delta = b**2 - 4 * a * c
x1 = (-b + delta**0.5)/2*a
x2 = (-b - delta**0.5)/2*a
if delta < 0:
  print('Erro: o valor de delta deu negativo.')
else:
  print('O conjunto solução dessa equação é: ', x1 , x2)




##calculadora
while True: 
 valor1=float(input("digite um valor: "))
 operador=str(input("digite um operador ent "))
 valor2=float(input("digite outro valor: "))

 if operador == '+':
  print(valor1+valor2)
 elif operador =='-':
  print(valor1-valor2)
 elif operador == ':' or '/':
  print(valor1/valor2)
 elif operador == '*'or'x':
  print (valor1*valor2)
 elif valor1 or valor2 == 0 and operador == ":"or"/":
  print('operação invalida')
##calculadora
while True: 
 valor1=float(input("digite um valor: "))
 operador=str(input("digite um operador: "))
 valor2=float(input("digite outro valor: "))

 if  (operador == ":"or operador == "/") and valor2 == 0 :
  print('operação invalida')
 elif operador == '+':
  print(valor1+valor2)
 elif operador == '-':
  print(valor1-valor2)
 elif operador == ':' or operador == '/':
  print(valor1/valor2)
 elif operador == '*' or operador == 'x':
  print (valor1*valor2)
 

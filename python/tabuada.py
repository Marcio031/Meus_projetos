##entrada
print("Descubra a tabuada de um numero especifico")
valor=int(input("digite um valor: "))
##tabuada
tabuada=[1,2,3,4,5,6,7,8,9,10]
for numeros in tabuada:
 resultado=valor*numeros
 print(f"{valor}x{numeros} = {resultado}")
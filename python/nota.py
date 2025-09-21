n1=float(input("digite a nota 1:"))
n2=float(input("digite a nota 2:"))
n3=float(input("digite a nota 3:"))
####################################
n_media=((n1+n2+n3)/3)
print(f"sua nota mmedia é {n_media:.2}")
if n_media >=7:
  print("Parabens você foi aprovado")
elif n_media >= 5 and n_media <7:
    print("Você esta de recuperação")
elif n_media <5:
      print("Você foi reprovado")
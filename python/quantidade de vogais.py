frase=input("digite uma frase: ")
#################################
vg="aeiouAEIOU"
nvg=0
for letras in frase:
  if  letras in vg:
    nvg+=1
#################################
print(f"sua frase tem",nvg,"vogais")


import random 
numero = random.randint(1, 100)
palpite=0
while palpite != numero:
    palpite = int(input("Digite um número entre 1 e 100: "))

    if palpite < 1 or palpite > 100:
        print("⚠️ Número inválido! Digite apenas entre 1 e 100.")
    elif palpite > numero:
        print("O valor digitado é maior que o número secreto")
    elif palpite < numero:
        print("O valor digitado é menor que o número secreto")
    else:
        print("🎉 Seu valor está correto:", numero)
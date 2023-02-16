idade = int(input("Digite a sua idade:" ))
dinheiro = int(input("Digite a quantidsde de dinheiro que voce tem: "))
carteira = input("voce tem carteira de motorista? (s/n)")

if (idade >= 18 and dinheiro >= 50) or carteira == "s":
     print("voce pode alugar o carro.")
else:
    print("voce nao pode alugar o carro.")
    
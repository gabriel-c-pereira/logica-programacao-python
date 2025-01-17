nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$ "))
quantidade = int(input("Digite a quantidade do produto: "))

if quantidade <= 10:
    desconto = 0.0
elif quantidade <= 20:
    desconto = 0.1
elif quantidade <= 50:
    desconto = 0.2
else:
    desconto = 0.25

valor_final = preco - (desconto * preco)

print("O valor final ficou do produto " + nome + " é: R$ " + str(valor_final))
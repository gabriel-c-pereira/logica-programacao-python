lista_produtos = [ 
    { 
        "id": 1, 
        "nome": "Arroz", 
        "quantidade": 50, 
        "preco": 20.99 
    }, 
    { "id": 2, "nome": "Feijão", "quantidade": 30, "preco": 8.50 }, { "id": 3, "nome": "Macarrão", "quantidade": 40, "preco": 5.90 }, { "id": 4, "nome": "Açúcar", "quantidade": 25, "preco": 4.20 }, { "id": 5, "nome": "Café", "quantidade": 60, "preco": 14.70 }, { "id": 6, "nome": "Leite", "quantidade": 100, "preco": 4.80 }, { "id": 7, "nome": "Óleo de Soja", "quantidade": 70, "preco": 9.50 }, { "id": 8, "nome": "Sabonete", "quantidade": 200, "preco": 1.50 }, { "id": 9, "nome": "Detergente", "quantidade": 150, "preco": 2.30 }, { "id": 10, "nome": "Papel Higiênico", "quantidade": 80, "preco": 12.00 } ] 

valor_total = 0

for produto in lista_produtos:
    valor_total += produto["preco"] * produto["quantidade"]
    print("ID do produto: " + str(produto["id"]))
    print("Nome do produto: " + produto["nome"])
    print("Quantidade: " + str(produto["quantidade"]))
    print("Preço do produto: " + str(produto["preco"]))

print("O valor total é: R$ " + str(valor_total))
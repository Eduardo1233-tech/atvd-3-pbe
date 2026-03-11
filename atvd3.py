estoque_mercado = [
    {"nome": "Arroz 5kg", "preco": 25.00},
    {"nome": "Feijão Preto 1kg", "preco": 8.50},
    {"nome": "Leite Integral 1L", "preco": 4.90},
    {"nome": "Café Torrado 500g", "preco": 25.00},
    {"nome": "Açúcar Refinado 1kg", "preco": 4.20},
    {"nome": "Óleo de Soja 1L", "preco": 6.75},
    {"nome": "Pão de Forma", "preco": 7.30},
    {"nome": "Manteiga 200g", "preco": 7.00}
]

def mostra_estoque():
    print("\n" + "="*30)
    print(" ESTOQUE DO MERCADO")
    print("="*30)

    while i, item in enumerate(estoque_mercado):
        print(f"{i} | {item['nome']:20} | R$ {item['preco']:>6.2f}")
    print("-" * 30)

def adiciona_produto(nome, preco):
    novo = {"nome": nome, "preco": preco}
    estoque_mercado.append(novo)
    print(f"n[+] Sucesso: {nome} adicionado ao estoque.")

def remove_produto(indice):
    try:
        removido = estoque_mercado.pop(indice)
        print(f"n[-] Removido: {removido['nome']}")
    except IndexError:
        print("n[!] Erro: Posição não encontrada no estoque.")



mostra_estoque()

adiciona_produto("Detergente Neutro", 2.50)

remove_produto(3)

mostra_estoque()

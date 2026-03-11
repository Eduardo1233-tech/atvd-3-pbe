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
    print("\n" + "="*35)
    print("      ESTOQUE DO MERCADO")
    print("="*35)
    
    i = 0  
    while i < len(estoque_mercado):
        item = estoque_mercado[i]
        print(f"{i} | {item['nome']:20} | R$ {item['preco']:>6.2f}")
        i += 1  
        
    print("-" * 35)

def adiciona_produto(nome, preco):
    novo = {"nome": nome, "preco": preco}
    estoque_mercado.append(novo)
    print(f"\n[+] Sucesso: {nome} adicionado.")

def remove_produto(indice):
    
    if 0 <= indice < len(estoque_mercado):
        removido = estoque_mercado.pop(indice)
        print(f"\n[-] Removido: {removido['nome']}")
    else:
        print(f"\n[!] Erro: Índice {indice} inexistente.")


mostra_estoque()
adiciona_produto("Detergente Neutro", 2.50)
remove_produto(3)
mostra_estoque()

let estoque_mercado = [
    { nome: "Arroz 5kg", preco: 25.00 },
    { nome: "Feijão Preto 1kg", preco: 8.50 },
    { nome: "Leite Integral 1L", preco: 4.90 },
    { nome: "Café Torrado 500g", preco: 25.00 },
    { nome: "Açúcar Refinado 1kg", preco: 4.20 },
    { nome: "Óleo de Soja 1L", preco: 6.75 },
    { nome: "Pão de Forma", preco: 7.30 },
    { nome: "Manteiga 200g", preco: 7.00 }
];
function mostra_estoque() {
    console.log("\n" + "=".repeat(35));
    console.log("      ESTOQUE DO MERCADO");
    console.log("=".repeat(35));
    let i = 0;
    while (i < estoque_mercado.length) {
        let item = estoque_mercado[i];

        let nomeFormatado = item.nome.padEnd(20, " ");
        let precoFormatado = item.preco.toFixed(2).padStart(6, " ");
        
        console.log(`${i} | ${nomeFormatado} | R$ ${precoFormatado}`);
        i++;
    }
    console.log("-".repeat(35));
}
function adiciona_produto(nome, preco) {
    let novo = { nome: nome, preco: preco };
    estoque_mercado.push(novo);
    console.log(`\n[+] Sucesso: ${nome} adicionado.`);
}

function remove_produto(indice) {
    if (indice >= 0 && indice < estoque_mercado.length) {
        let removido = estoque_mercado.splice(indice, 1);
        console.log(`\n[-] Removido: ${removido[0].nome}`);
    } else {
        console.log(`\n[!] Erro: Índice ${indice} inexistente.`);
    }
}
mostra_estoque();
adiciona_produto("Detergente Neutro", 2.50);
remove_produto(3);
mostra_estoque();

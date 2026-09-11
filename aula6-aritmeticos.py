primeiro_numero = 42;
segundo_numero = 25;

print(primeiro_numero + segundo_numero); #Soma 
print(primeiro_numero - segundo_numero); #subtração
print(primeiro_numero * segundo_numero); #Multiplicação
print(primeiro_numero / segundo_numero); #Divisão real retorna float
print(primeiro_numero // segundo_numero); #Divisão inteira retorna int desconsiderando as dízimas
print(primeiro_numero % segundo_numero); #Divisão modular, retorna o resto da divisão
print(primeiro_numero ** segundo_numero); #Exponenciação

#Ordem de precedência (), **, * e /, + e - sempre da esquerda pra direita

#Sistema de vendas com desconto
produto = input("Qual produto comprado? ");
valor_produto = input("Valor do produto: ");
valor_produto = float(valor_produto);
print("COMPRA A VISTA 10% DESCONTO");
desconto = valor_produto * 0.10;
valor_final_produto = valor_produto - desconto;
valor_recebido = input("Qual o valor recebido? ");
valor_recebido = float(valor_recebido);

troco = valor_recebido - valor_final_produto;

print("--- CUPOM DE VENDA ---");
print(f"PRODUTO: {produto}");
print(f"VALOR: {valor_produto}"); 
print(F"DESCONTO: {desconto}")
print(F"VALOR FINAL: {valor_final_produto}")
print(f"RECEBIDO: {valor_recebido}");
print(f"TROCO: {troco}");
print("VOLTE SEMPRE!");
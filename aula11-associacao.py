#Serve para verificar se um elemento está contido dentro de uma lista [,]
#in e not in com mesmo padrão dos operadores de identidade
#Essa pesquisa é case Sensitive

pessoas = ["Alex", "José", "Daniel"];
compras = ["Arroz", "Feijão", "Cuscuz"];
valores = [6.50, 8.20, 0.99];

nome = "Alex"; 

print(nome in pessoas);  #Pesuisa por variável
print("Alex" in pessoas);  #Pesquisa direto Valor 
print("Banana" not in compras); #Pesquisa se não está
print(10.50 in valores); #Pesquisa por valor se está
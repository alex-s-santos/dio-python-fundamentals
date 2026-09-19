#FOR EM PYTHON
#for itemParaRetorno in localDaInteração:
#   BLOCO

texto = input("Digite qualquer texto: ");
VOGAIS = "AEIOU";

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra.upper(), end=" | ");
        
#Função range para usar com for, ele retorna uma lista 
#range(inicio, fim, passo); O passo é opcional

print(list(range(1, 10, 1)))

for numero in range(0, 11, 2):
    print(numero, end=" | ")
    
#While: Serve para repetir o bloco enquanto o usuário não sabe a quantidade de repetições, esperando um evento
contador = 10;

while contador != -1:
    if(contador >= 1):
        print(contador, end=", ");
    else:
        print(contador, end=".");
    contador -= 1;
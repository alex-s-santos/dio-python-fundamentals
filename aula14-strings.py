#Métodos em string para manipular:

texto = "Estou aprendendo a manipular string em Python";

print(texto.upper()); #Maiúsculo
print(texto.lower()); #Minúsculo
print(texto.title()); #iniciais maiúsculas

python = "   python   ";
print(python);
print(python.strip()); #remove os espaços dos dois lados
print(python.lstrip()); #remove os espaços a esquerda
print(python.rstrip()); #remove os espaços a direita
print(python.center(10, "#")); #Centraliza, primeiro parâmetro é o tamanho determinado e segundo o que vai usar pra completar
print(".".join(python)); #Para juntar um elemento com a variável


#FORMATACAO DE STRING

PI = 3.14159;
print(f"Valor de PI: {PI:.2f}"); #Para determinar tamanho e casas decimais, antes do ponto coloca-se o valor referente a tamanho, sem nada o tamanho é 0, após a quantidade de casas decimais e o f indica que é um float

#fatiamento de string nome[incio:fim:passo] onde o segundo e terceiro parâmetros são opcionais
nome = "Alex Santos";
print(nome[0]); #Pega por indice o caractere
print(nome[0:5]); #Pega cactere de inicio até caractere de fim sem usar o último
print(nome[0:5:2]); #Pega o início até o fim com passo 
print(nome[:5]); #Pega até o fim tendo como início 0
print(nome[::5]); #Pega fo inicio ao fim apenas com passo
print(nome[::-1]); #inverte

#Variável de múltiplas linhas """ TEXTO """ pode ser com aspas duplas ou simples

mensagem_1 = """ Esse é um
texto    
que representa uma 

STRIG

Com últiplas linhas""";

print(mensagem_1);

mensagem_2 = F"""Só pra provar que

dá pra 

            interpolar 

com variáveis         {nome}

também""";

print(mensagem_2);
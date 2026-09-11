#Pra entrada input("Pede pra o usuário digitar CLI")

nome = input("Qual seu nome?");
print(f"Olá, {nome}");

idade = input("Digite sua idade: ");
idade = int(idade); #Converter para inteiro

print(f"Ano que vem você terá {idade + 1}");

#propriedades do print
#end="" -> Serve para colocar algo no fim da (\n adiciona uma quebra de linha no final)
#sep="" -> Serve para mudar o separador entre os textos, por padrão vem um espaço, com ele coloca-se o que quiser


sobrenome = "Santos";
print(nome, sobrenome); #Por padrão separa por espaço
print(nome, sobrenome, sep="#"); #Muda o separador
print(nome, sobrenome, sep=",");
print(nome, sobrenome, end="\n") #quebra de linha
print(nome, sobrenome, end="..."); #muda apenas o fim
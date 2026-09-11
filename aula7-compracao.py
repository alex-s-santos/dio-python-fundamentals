primeiro_numero = 55;
segundo_numero = 133;

print(primeiro_numero == segundo_numero); #Igual
print(primeiro_numero != segundo_numero); #Diferente
print(primeiro_numero > segundo_numero); #Maior
print(primeiro_numero < segundo_numero);#menor
print(primeiro_numero >= segundo_numero); #Maior ou igual
print(primeiro_numero <= segundo_numero); #Mebnor ou igual

#Teste maior de idade
nome = input("Usuário: ");
idade = input("Qual a sua idade? ");
idade = int(idade);

maior_de_idade = idade >= 18;

print(f"Maior de idade: {maior_de_idade}");
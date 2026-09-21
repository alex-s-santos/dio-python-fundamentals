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

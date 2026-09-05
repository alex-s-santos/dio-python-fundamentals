#Em python não tem necessidade de declarar palavra reservada nem tipo para declarar uma variável, o interpretador sabe o tipo, e chama-se apenas pelo nome declarado da variável
#Para declarar uma constante em Python não tem palavra reservada, apenas uma convenão de colocar ela com letras maiúsculas

nome = "Alex";
print(nome);

nome = 'José'; #redeclara o valor
print(nome);

idade = 33;

print(idade);

#constante com convenção / Muda o valor, mas usando a convenção por prática não se muda

CPF = '12345678900';
SEXO = 'M';

#Boas práticas - snake_case, nomes claros

preco_produto = 50;
desconto_produto = 5;
CPF_DO_USUARIO = '000.000.000-00'; #constante

#Pode declarar mais de uma variável na mesma lina

a, b, c = 1, 2, 3;

print(b);

#Pode-se interpolar string em Python como template string do JS, usando o f String
print(f"Olá, {nome}, seja bem-vindo, vi que sua idade é {idade} anos e seu CPF é: {CPF_DO_USUARIO}");
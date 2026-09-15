#and, or, not
saldo = 1000;
saque = 500;
limite = 900;

print(saque <= limite and saldo >= saque); #true e true
print(saque <= limite or saldo < saque); #true e false
print(not saque <= 0); #false, negado virta true

#desafio pode dirigir
idade = input("Qual sua idade?");
idade = int(idade);
possui_cnh = input("Possui CNH? S - Para SIM | N - Para não")
possui_cnh = possui_cnh.upper(); #PARA FORÇAR A SER MAIÚSCULO
analise = (idade >= 18 and possui_cnh == 'S');

print(f"APTO A DIRIGIR? {analise}");

#desafio valor recebido
#BValor do projeto 1: 500
#BValor do projeto 1: 500
#BValor do projeto 1: 500
#valor da TV: 1000
#valor do viagem: 500
#Prioridade compra a TV
#Se tudo der errado passear no shopping

divisor = "--------------------------------";
print(divisor);
print("PARA RESPONDER USE S PARA SIM E N PARA NÃO", end="\n");
projeto_1 = input("Fez projeto 1: ");
projeto_1 = projeto_1.upper();
projeto_2 = input("Fez projeto 2: ");
projeto_2 = projeto_2.upper();
projeto_3 = input("Fez projeto 3: ");
projeto_3 = projeto_3.upper();
S = "S";


comprar_tv = (projeto_1 == S and projeto_2 == S) or (projeto_1 == S and projeto_3 == S) or (projeto_2 == S and projeto_3 == S);
viajar = (projeto_1 == S) and (projeto_2 == S) and (projeto_3 == S);
passear_no_shopping = (comprar_tv == False) and (viajar == False);

print(divisor);

print(f"COMPRAR TV: {comprar_tv}");
print(f"VIAJAR: {viajar}");
print(f"PASSEIO NO SHOPPING: {passear_no_shopping}");
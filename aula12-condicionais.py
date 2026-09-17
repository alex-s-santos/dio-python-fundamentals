#identação em Python conta como código

# EX EM JS
# if(saque > saldo) {
#   console.log("Saldo insuficiente");    
#} else {
#   saldo = saldo - saque;
#   console.log("Saldo atual: " + saldo);    
#   console.log("Obrigado por usar nossos serviços");    
#}

# MESMO CÓDIGO EM PYTHON
# if(saque > saldo):
#   print("Saldo insuficiente");    
# else:
#   saldo = saldo - saque;
#   print("Saldo atual: " + saldo);    
#   print("Obrigado por usar nossos serviços");    

#CONDICIONAIS SIMPLES if
#CONDICIONAIS COMPOSTAS if else
#CONDICIONAIS ANINHADAS if elif elif elif ... else (opcional)

separador = "---------------------------";

#Desafio condicionais simples - Radar de velocidade
print(separador);
VELOCIDADE_MAXIMA_PERMITIDA = 60;
VELOCIDADE_MAXIMA_PERMITIDA +=  VELOCIDADE_MAXIMA_PERMITIDA * 0.10; #Tem 10% de tolerância
velocidade = input("Velocidade que passou no radar: ");
velocidade = int(velocidade);

if(velocidade > VELOCIDADE_MAXIMA_PERMITIDA):
    print(f"Multado! {velocidade - VELOCIDADE_MAXIMA_PERMITIDA}km a cima do permitido")
    

#Desafio condicionais compostas - Aprovação escolar
print(separador);
MEDIA_APROVACAO = 7.0;
nota1 = float(input("1ª NOTA: "));
nota2 = float(input("2ª NOTA: "));
nota3 = float(input("3ª NOTA: "));


media = (nota1 + nota2 + nota3) / 3;
resultado = "Resultado";

if(media >= MEDIA_APROVACAO):
    resultado = "Aprovado";
else:
    resultado = "Reprovado";
    
print(f"Média: {media} | {resultado}!")

#Desafio condicional aninhada - Calculadora de IMC (IMC = peso ÷ altura²)
peso = float(input("Digite seu peso: "));
altura = float(input("Digite seu altura: "));

IMC = peso / (altura ** 2);
resultado = "Verificando...";

if(IMC < 18.5):
    resultado = "A baixo do peso";
    
elif(IMC < 24.9):
    resultado = "No peso normal";
    
elif(IMC < 29.9):
    resultado = "Com sobrepeso";
    
elif(IMC < 34.9):
    resultado = "Com obesidade Grau 1";
    
elif(IMC < 39.9):
    resultado = "Com obesidade Grau 2";
    
elif(IMC > 40):
    resultado = "Com obesidade Mórbida";

print(separador);
print(f"Seu IMC é {IMC} | Resultado: Você está: {resultado}");
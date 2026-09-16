#Servem para verificar se os elementos (variaveis) ocupam o mesmo lugar de memória
#is = para verificar se ocpam e is not = para verificar se não ocupam

name = "Alex";
user_name = name;

print(name is user_name); #True
print(name is not user_name); #False

numero_1, numero_2 = 100, 100;
print(numero_1 is numero_2); #False, pois mesmo tendo o mesmo valor não apontam para o mesmo local na memória
print(numero_1 is not numero_2);

numero_2 = numero_1;
print(numero_1 is numero_2);
print(numero_2 is numero_1);
#Ambos os casos retornam True pois agora apontam para o mesmo endereço na memória
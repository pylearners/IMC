
nome = input("qual seu nome:")  
#aqui estamos criando a variável nome
#print é para mostrar na tela
#input é para que o usuário possa dar alguma resposta
#toda função tem que estar entre parênteses e o nome entre aspas

print("olá ", nome)

peso = float(input("qual seu peso:"))

#colocou float porque peso é uma variável não inteira
#type é o tipo de variável (pode ser str,float,inte,boolena)

altura = float(input("qual sua altura:"))

imc = peso/(altura*altura)

print("seu imc é ", imc)

print("muito abaixo do peso:", imc < 17)

print("abaixo do peso normal:", imc >= 17 and imc < 18.5)

print("peso dentro do normal:", imc>= 18.5 and imc < 25)

print("peso acima do normal:", imc >= 25 and imc >= 30)

habituado= str(input("o animal está habituado?"))

if (habituado== "sim"):
    print("iniciar protoloco de aproximação")

elif (habituado== "nao"):
    print("habituar o animal")

from random import randint 

aproximacao= randint(1, 100)
print('o animal está a',aproximacao,'cm da barra.' )

if(aproximacao< 30):
    print("liberar 0,5ml de recompensa ")

else:
    print('animal precisa se aproximar da barra.')  
tbarra = int(input("quantas vezes o animal tocou na barra?"))

if(tbarra >= 20):
    print("animal passou para a proxima fase")

else:
    print("animal permanece na mesma fase")
print("fase de discriminação de sons")

from random import randint
som1= randint(0,1)
barraesq= randint(0,1)


if(som1 == barraesq):
    print('animal ouviu som 1 e tocou na barra esquerda.')
    print("0,5 ml de recomenpensa liberada")

else:
    print("animal não realizou a tarefa corretamente")
    print("recompensa não liberada")
    from random import randint
som2= randint(0,1)
barradir= randint(0,1)


if(som2 == barradir):
    print('animal ouviu som 2 e tocou na barra direta.')
    print("0,5 ml de recomenpensa liberada")else:
    print("animal não realizou a tarefa corretamente")
    print("recompensa não liberada")
from random import randint
proximafase= randint(48,100)
minutos= randint(25,32)

if(proximafase>=50 and minutos<30):

    print("animal realizou a tarefa corretamente e passou para próxima fase")

else:
    print("animal não realizou a tarefa corretamente")

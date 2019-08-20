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

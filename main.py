#Exercícios: Tomada de Decisão e Estruturas de Repetição

#1. Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input("Digite o primeiro número:" '\n'))
n2 = float(input("Digite o segundo número:" '\n'))

if n1 > n2:
  print (n1)
else: 
  print (n2)

#2. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. #obs.: if para a primeiroa comparação, elif quando tem mais opções que precisam ser comparadas antes da validação final de else - o else final vem para tratar erros.

turno = input("Em que período você estuda? Digite M para matutino; V para Vespertino; ou N para Noturno" '\n')

if turno == "M":
  print ("Bom dia!")
  
elif turno == "V":
  print ("Boa tarde!")
  
elif turno == "N":  
  print ("Boa noite!")

else:
  print("Valor inválido")

#3. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = -1 #definir antes de entrar no while
while nota < 0 or nota > 10:
  nota = int (input("Digite uma nota entre 0 e 10" '\n'))
  if nota < 0 or nota > 10:
    print("Valor inválido")

print("saiu")

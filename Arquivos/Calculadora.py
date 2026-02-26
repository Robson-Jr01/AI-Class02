#CALCULADORA
import math

d = input("Escolha a operação desejada: 1-Adição, 2-Subtração, 3-Multiplicação, 4-Divisão, 5-Potênciação, 6-Radiciação.")
d = int(d)

if d == 1:

	a = input("Entre com o 1º valor: ")
	a = int(a)

	b = input("Entre com o 2º valor: ")
	b = int(b)
	
	c = a + b
	print("A soma: ", a, "+", b, "=", c)

	input()

elif d == 2:

	a = input("Entre com o 1º valor: ")
	a = int(a)

	b = input("Entre com o 2º valor: ")
	b = int(b)
	
	c = a - b
	print("A subtração: ", a, "-", b, "=", c)

	input()

elif d == 3:

	a = input("Entre com o 1º valor: ")
	a = int(a)

	b = input("Entre com o 2º valor: ")
	b = int(b)
	
	c = a * b
	print("A multiplicação: ", a, "vezes ", b, "=", c)

	input()

elif d == 4:

	a = input("Entre com o 1º valor: ")
	a = float(a)

	b = input("Entre com o 2º valor: ")
	b = float(b)
	
	c = a / b
	print("A divisão: ", a, "dividido por ", b, "=", c)

	input()

elif d == 5:

	a = input("Entre com o 1º valor: ")
	a = int(a)

	b = input("Entre com o valor a elevar: ")
	b = int(b)
	
	c = a ** b
	print("A potênciação: ", a, "elevado a ", b, "=", c)

	input()

elif d == 6:

	a = input("Entre com o valor para tirar a raiz: ")
	a = int(a)
	
	c = math.sqrt(a)

	print("A raiz de: ", a, "=", c)

	input()

else:
	print("Você não selecionou nenhum número válido, só por conta disso, você será obrigado a reiniciar o sistema, parabéns! Seus pais devem estar orgulhosos!")
	
	input()





# -*- coding: utf-8 -*-
"""Olá, este é o Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

#func saudação.

def saudacao(nome):
  print(f"Olá {nome}")

nome = input("Digite seu nome:")

saudacao(nome)

#func alternar

def alternar(n):
  cont = 0

  while cont != n:
    if cont % 2 == 0:
      print(cont)
      cont = cont + 1
    else:
      print(f"{cont}-")
      cont = cont + 1

n = int(input("insira o numero:"))

alternar(n)

#Medida do quadrado

def calQuadrado():
  nome = input("Olá, digite seu nome: ")

  altura = int(input(f"{nome}, digite a altura do quadrado: "))

  largura = int(input(f"{nome}, digite a largura do quadrado: "))

  quadrado = (largura * 2) + (altura * 2)

  print(f"{nome} seu quadrado tem altura de {altura} e largura de {largura}, tendo como area {quadrado} !")

calQuadrado()

#func saudação 2

def saudacao (nome, mensagem="Bom dia !"):
  print(f"Olá {nome}, {mensagem}")

saudacao("Felipe", "Boa tarde.")

#multiplos valores

def calcular_valores(numero):
  dobro = numero * 2
  triplo = numero * 3
  quadruoplo = numero * 4
  quinta_potencia = numero ** 5
  return dobro, triplo, quadruoplo, quinta_potencia

numero = int(input("Digite o nuemro: "))

resultado = calcular_valores(numero)

print(resultado)

def soma_pn(valores):
  soma_p = 0
  soma_n = 0

  for n in valores:
    if n > 0:
      soma_p += n
    else:
      soma_n += n

  return soma_p, soma_n

valores = [2, 3, -1, -4]
soma_p, soma_n = soma_pn(valores)

print(f"soma positivos: {soma_p} / soma negativos: {soma_n}")

lista = [1,2,3]

soma = sum(lista)
quadrado = []

for n in lista:
  quadrado.append(n ** 2)

quadrado = sum(quadrado)

print(soma, quadrado)
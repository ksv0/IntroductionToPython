﻿# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

import random


def main():

	firstElement =	123		#input("enter first element: ")
	diff =	20				#input("enter difference: ")
	numberOfElements =  20	#input("enter number of elements: ")

	#result = []
	#print ([firstElement + (i - 1) * diff for i in range(firstElement, (numberOfElements*diff+firstElement), diff)])

	result = lambda a1, d, quantity: print ([a1 + (n - 1) * d for n in range(a1, (quantity * d + a1), d)])
	result(firstElement, diff, numberOfElements)

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)


	def FillArrayRandom(startRand, powRand, stop ):

		for i in stop:
			arrayOfRandom.append(random.randint(startRand, startRand + powRand))
		return arrayOfRandom

	def IndexesInRange ():
		pass

	minValue =	-40			#input("enter min value: ")
	maxValue =	5000		#input("enter max value: ")

	arrayOfRandom = []
	resultStr = ""

	stop = "Problem 32: Determine the indexes of array (list) elements whose values ​​belong to a given range (i.e. not less than a given minimum and not more than a given maximum)"
	startRand = -10000
	powRand = 20000

	


	try:
		print (f"list of indexes and values, with value from {minValue} to {maxValue} ")
		i = 0
		while i < len(arrayOfRandom):
			if minValue <= arrayOfRandom[i] <= maxValue:
				resultStr += f" [{i} = {arrayOfRandom[i]}]  \n"
			i += 1

		print(resultStr)
	except:
		pass
#print(arrayOfRandom)







	
﻿

##Задача 4: 
##Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
##Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
##а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

#S = int(input("Введите количество сделанных журавликов: "))

#x = S / 6 

#print("Петя и Сережа сделали по", x, "журавлика(ов)")
#print("Катя сделала", S/3, "журавлика(ов)")



##Задача 6: 
##Вы пользуетесь общественным транспортом? 
##Вероятно, вы расплачивались за проезд и получали билет с номером. 
##Счастливым билетом называют такой билет с шестизначным номером, 
##где сумма первых трех цифр равна сумме последних трех. 
##Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
##Вам требуется написать программу, которая проверяет счастливость билета.

#num = input("Введите номер билета: ")
#sum1 = int(num[0]) + int(num[1]) + int(num[2])
#sum2 = int(num[3]) + int(num[4]) + int(num[5])

#if sum1 == sum2:
#    print("У вас счастливый билет!")
#else:
#    print("К сожалению, ваш билет несчастливый.")




##Задача 8: 
##Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника)

#n = int(input("Введите количество долек шоколадки по вертикали: "))
#m = int(input("Введите количество долек шоколадки по горизонтали: "))
#k = int(input("Введите количество долек, которые нужно отложить: "))

#if k > n * m:
#    print("Количество отложенных долек превышает число долек в шоколадке!")
#else:
#    if k % n == 0 or k % m == 0:
#        print("Можно отложить все дольки за один раз!")
#    else:
#        print("Нельзя отложить все дольки за один раз!")


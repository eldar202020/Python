num_1 = int(input("Напишите первую цифру: "))
num_2 = int(input("Напишите вторую цифру: "))
znac = input("Напишите математическую операцию которую хотите выполнить (+, -, *, /, )") 
if znac == '+':
    otvet = num_1 + num_2
elif znac == '-':
    otvet = num_1 - num_2
elif znac == '*':
    otvet = num_1 * num_2
elif znac == '/':
    if num_2 == 0:
        print("Незьзя делить на ноль")
    else:
        otvet = num_1 / num_2
else:
    print("Нет такой операции")
print("Ответ на пример", num_1, znac, num_2, '=', otvet)
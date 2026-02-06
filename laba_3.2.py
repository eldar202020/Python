a = input("Напишите пример ")
if a.find('+')>0:
    znac = '+'
elif a.find('-')>0:
    znac = '-'
elif a.find('*')>0:
    znac = '*'
elif a.find('/')>0:
    znac = '/'
else:
    print("В базе нет таких операций")

print(znac) 
num_1 = int((a.split(znac))[0])
num_2 = int((a.split(znac))[1])
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

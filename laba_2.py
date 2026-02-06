data = int(input('Введите число: '))
mes = input('Введите название месяца: ')
day = 0
month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь','Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
index_month = month.index(mes)
Data_mes = {'Январь': 31, 'Февраль': 28, 'Март': 31, 'Апрель': 30, 'Май': 31, 'Июнь': 30, 'Июль': 31, 'Август': 31, 'Сентябрь': 30, 'Октябрь': 31, 'Ноябрь': 30, 'Декабрь': 31}
if Data_mes[mes] >= data:
        if (index_month == (0 or 1 or 11)):
              sezon = "Зима"
        elif(index_month == (2 or 3 or 4)):
              sezon = "Весна"
        elif(index_month == (5 or 6 or 7)):
              sezon = "Лето"
        else:
              sezon = "Осень"
        
        for i in  range(0,index_month):
            day += Data_mes[month[i]]
        day += data
        
        print(f"{data} {mes} это {sezon}, {day} день года")

else:
    print("Дата неверна")
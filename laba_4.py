def razbienie(primer):
    elem_prim = ''
    stek = []
    znaki = ['+','-','*','/','^','(',')','=']
    for i in range(len(primer)):
        if primer[i] in znaki:
            try:
                stek.append(int(elem_prim)) 
                elem_prim = ''
                stek.append((primer[i]))
            except ValueError:
                stek.append((elem_prim)) 
                elem_prim = ''
                stek.append((primer[i]))
        else:
            elem_prim += primer[i]
    for _ in range(stek.count('')):
        stek.remove('')
    stek.remove('=')
        
    return stek[::-1]
#-----------------------------------------------------------------------------
def bazoper(num_1, num_2, znac):
    if znac == '+':
        otvet = num_1 + num_2
    if znac == '^':
        otvet = num_1 ** num_2
    elif znac == '-':
        otvet = num_1 - num_2
    elif znac == '*':
        otvet = num_1 * num_2
    elif znac == '/':
        if num_2 == 0:
            print("Незьзя делить на ноль")
        else:
            otvet = num_1 / num_2
    return otvet
#--------------------------------------------------------------------
a = input('Введите пример: ')
primer = razbienie(a)
simvol = None
chisla = []
znaki = []
znak_obj = {'+':1,'-':1,'*':2,'/':2,'^':3}  
while True:
    try:
        simvol = primer.pop()
        if type(simvol) == int or type(simvol) == float:
            chisla.append(simvol)
        else:
            if len(znaki) == 0 or znaki[-1] == "(":
                znaki.append(simvol)
            elif simvol == "(":
                znaki.append(simvol)
            elif simvol == ")":
                while True:
                    zn =  znaki.pop()
                    if zn == "(":
                        break
                    else:
                        ch_2 = chisla.pop()
                        ch_1 = chisla.pop()
                        chisla.append(bazoper(ch_1, ch_2, zn))
            else:
                if znak_obj[znaki[-1]] < znak_obj[simvol]:
                    znaki.append(simvol)
                    print(znaki)
                else:
                    while  len(znaki) != 0  and znaki[-1] != "(" and (znak_obj[znaki[-1]] >= znak_obj[simvol])  :
                        ch_2 = chisla.pop()
                        ch_1 = chisla.pop()
                        zn =  znaki.pop()
                        chisla.append(bazoper(ch_1, ch_2, zn))
                    znaki.append(simvol)
    except IndexError:
        for _ in range(len(znaki)):
            zn =  znaki.pop()
            ch_2 = chisla.pop()
            ch_1 = chisla.pop()
            chisla.append(bazoper(ch_1, ch_2, zn))
        print(f"Ответ: {chisla[0]}")
        break
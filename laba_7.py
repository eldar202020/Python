def ymnoz_pri_pom_sum(a, b):
    if a < 0 or  b < 0:
        return 'ошибка'
    if b == 0:
        return 0
    else:
        return a + ymnoz_pri_pom_sum(a, b-1)
   

print(ymnoz_pri_pom_sum(100, 3))
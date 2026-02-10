string  = input()
dlina = len(string)
nev_string = ''
print(dlina)
for i in range(dlina-1,-1 , -1):
    nev_string = nev_string + string[i]
print(nev_string)
    

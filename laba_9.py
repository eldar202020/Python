znak_prepin = {".":0, "?":0, "!":0, ",":0, ";":0, ":":0, "—":0}
f_1 = open('9_1.txt','r', encoding='utf-8')
f_2 = open('9_2.txt', 'w', encoding='utf-8')
count_strock = 0
with f_1 :
    for line in f_1:  # Читает файл построчно, не загружая в память целиком
        count_strock+= 1
        for key in line:
            if key in znak_prepin:
                znak_prepin[key] +=1
with f_2:
    f_2.write(f"количество строк  = {count_strock} \n")
    for key in znak_prepin:
        f_2.write(f"количество {key}  = {znak_prepin[key]} \n")
f_1.close()
f_2.close()
    
                
        
        
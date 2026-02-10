def add_numbers (a, b):
    return a+b
def average_value(a):
    length = len(a)
    amount = sum(a)
    return amount/length
def febonachi(n):
    n -=1
    if n <= 0:
        prev = 0
        seit = 1
        return [seit , prev]
    else:
        return [sum(febonachi(n)), febonachi(n)[0]]
         
def multiply(*arg):
    dlina = len(arg)
    proizved = 1
    for i in range(0, dlina):
        proizved *= arg[i]
    return proizved

global_var = 5
def modify_global_var():
    return global_var*5-8*3


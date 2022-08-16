#Verificando quais os núemros primos menores ou iguais a 'a'

def primos(a):
    primos = [2]
    i = 3

    while i<= a:
        primo = True
        for j in range(2,i):
            if j >= a**(1/2):
                break
            elif i%j == 0:
                primo = False
                break
        if primo:
            primos.append(i)
            print(primos)
        i += 1
    return primos 

while True:

    a = int(input())
    if a == 0:
        break
    elif a == 1:
        print(0)
    elif a == 2:
        print(0)
    else:
        primos_totais = primos(a)
        
    maneiras = 0
    for i in range(len(primos_totais)):
        if primos_totais[i] == a:
            maneiras += 1
        for j in range(i+1, len(primos_totais)):
            if primos_totais[i]+primos_totais[j] <= a:
                maneiras += 1
    print(maneiras)
            



    

    


def primos(a):
    primos = [2]
    for i in range(3, a+1):
        primo = True
        for j in range(2,i):
            if i%j == 0:
                primo = False
                break
        if primo:
            primos.append(i)
    return primos 

print(primos(11))

while True:

    a = int(input())
    if a == 0:
        break
    elif a == 1:
        print(0)
    elif a == 2:
        print(0)
    else:
        pass
    #Verificando quais os núemros primos menores ou iguais a 'a'

    


def primos(a):
    primos = []
    primo = 2
    for i in range(2, a+1):
        if primo/i != 0:
            primos.append(primo)


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

    

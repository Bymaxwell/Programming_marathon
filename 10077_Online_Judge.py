def matriz_soma_fracoes(a,b):
  #matriz m que conterá na primeira linha, os numeradores e na segunda linha os denominadores
  m = [[0,1],[1,1]]
  encontrado = True
  while encontrado:
    soma_temporario = [[],[]]
    #Adiciona as somas dos elementos subjacentes em uma matriz n
    for l in range(len(m[0])-1):
      soma_temporario[0].append(m[0][l]+m[0][l+1])
      soma_temporario[1].append(m[1][l]+m[1][l+1])
    indice = 1
    #Adiciciona as somas que foram inseridas na matriz n na matriz m
    for k in range(len(soma_temporario[0])):
      m[0].insert(indice, soma_temporario[0][k])
      m[1].insert(indice, soma_temporario[1][k])
      indice+=2
    #Ao final vericamos se a fração desejada já existe na nossa matriz m, se sim, podemos parar o processor de somar e retornar essa matriz.
    for f in range(len(m[0])):
      if (m[0][f] == a and m[1][f] == b)or(m[0][f] == b and m[0][f] == a):
        encontrado = False
  return m

#Busca binária 

def busca_binaria(numerador,denominador, a, b, direcao):
  
  if len(numerador) <= 3:
    return direcao
  
  if (numerador[len(numerador)//2])/(denominador[len(denominador)//2])> a/b:
    direcao.append(0)
  if (numerador[len(numerador)//2])/(denominador[len(denominador)//2])< a/b:
    direcao.append(1)

  if direcao[-1] == 1:
    numerador   = numerador[len(numerador)//2:]
    denominador = denominador[len(denominador)//2:]
  else:
    numerador   = numerador[:len(numerador)//2]
    denominador = denominador[:len(denominador)//2]

  return busca_binaria(numerador, denominador, a, b, direcao)


while True:
  a, b = map(int, input().split())
  if a == 1 and b == 1:
    break
  direcao_primeira = [0]
  if a < b:
    matriz_fracoes = matriz_soma_fracoes(a,b)
    direcoes = busca_binaria(matriz_fracoes[0],matriz_fracoes[1], a, b, direcao_primeira)
  else:
    matriz_fracoes = matriz_soma_fracoes(b,a)
    direcoes = busca_binaria(matriz_fracoes[0],matriz_fracoes[1], b, a, direcao_primeira)
  
  if a>b:
    for i in range(len(direcoes)):
      if direcoes[i] == 0:
        direcoes[i] = 1
      else:
        direcoes[i] = 0
 
  for g in range(len(direcoes)):
    if direcoes[g] == 1:
      print('R', end ='')
    else:
      print('L', end ='')
  print()
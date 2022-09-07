def Transposta(matriz):
    matriz_transposta = []
    for i in range(len(matriz[0])):
        matriz_transposta_linha = []
        for j in range(len(matriz)):
            matriz_transposta_linha.append(matriz[j][i])
        matriz_transposta.append(matriz_transposta_linha)
    return matriz_transposta

vetor = []
def spirallyTraverse(matriz, r, c):
    #Serão 4 interações: Linha para direita, Coluna para baixo, Linha para esquerda, Coluna para cima.
    #A ideia é ir adicionando os elementos ao vetor que deve ser retornado e ir deletando esses elementos da matriz, evitando as repetições.

    #Linha para a direita
    for j in range(c):
        vetor.append(matriz[0][j])

    matriz.pop(0)
    r = r-1

    if r == 0:
        return vetor

    #Coluna para baixo
    for k in range(r):
        vetor.append(matriz[k][c-1])

    matriz = Transposta(matriz)
    matriz.pop(c-1)
    matriz = Transposta(matriz)
    c = c-1
    

    if c == 0:
        return vetor

    #Linha para esquerda
    for l in range(c-1, -1, -1):
        vetor.append(matriz[r-1][l])
    
    matriz.pop(r-1)
    r = r-1
    

    if r == 0:
        return vetor

    #Coluna para cima
    for m in range(r-1, -1, -1):
        vetor.append(matriz[m][0])
    
    matriz = Transposta(matriz)
    matriz.pop(0)
    matriz = Transposta(matriz)
    c = c-1
    

    if c == 0:
        return vetor

    return spirallyTraverse(matriz, r, c)

    

matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

print(spirallyTraverse(matriz,4,4))

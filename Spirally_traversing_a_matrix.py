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
    for j in range(len(matriz[0])):
        vetor.append(matriz[0][j])

    matriz.pop(0)

    if len(matriz) == 0:
        return vetor

    for k in range(len(matriz)):
        vetor.append(matriz[k][len(matriz[0])-1])

    matriz = Transposta(matriz)
    matriz.pop(len(matriz)-1)
    matriz = Transposta(matriz)

    if len(matriz) == 0:
        return vetor

    for l in range(len(matriz[0])-1, -1, -1):
        vetor.append(matriz[len(matriz)-1][l])
    
    matriz.pop(len(matriz)-1)

    if len(matriz) == 0:
        return vetor

    for m in range(len(matriz)-1, -1, -1):
        vetor.append(matriz[m][0])
    
    matriz = Transposta(matriz)
    matriz.pop(0)
    matriz = Transposta(matriz)

    if len(matriz) == 0:
        return vetor

    return spirallyTraverse(matriz)

    

matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(spirallyTraverse(matriz))

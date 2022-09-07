image_coordenates = [[],[]]

def floodFill(image, sr, sc, newColor):

    #A ideia é verificar se existe algum semelhante à esquerda, direita, em cima ou em baixo do starting pixel.

    #À direita
    direito_repetido = False
    for i in range(len(image_coordenates[0])):
        if image_coordenates[0][i] == sr and image_coordenates[1][i] == sc+1:
            direito_repetido = True
    if sc+1 < len(image[0]) and image[sr][sc+1] == image[sr][sc] and not(direito_repetido):
        image_coordenates[0].append(sr)
        image_coordenates[1].append(sc+1)


    #À esquerda
    esquerdo_repetido = False
    for i in range(len(image_coordenates[0])):
        if image_coordenates[0][i] == sr and image_coordenates[1][i] == sc-1:
            esquerdo_repetido = True
    if sc-1 > -1 and image[sr][sc-1] == image[sr][sc] and not(esquerdo_repetido):
        image_coordenates[0].append(sr)
        image_coordenates[1].append(sc-1)


    #Em cima
    cima_repetido = False
    for i in range(len(image_coordenates[0])):
        if image_coordenates[0][i] == sr-1 and image_coordenates[1][i] == sc:
            cima_repetido = True
    if sr-1 > -1 and image[sr-1][sc] == image[sr][sc] and not(cima_repetido):
        image_coordenates[0].append(sr-1)
        image_coordenates[1].append(sc)


    #Em baixo
    baixo_repetido = False
    for i in range(len(image_coordenates[0])):
        if image_coordenates[0][i] == sr+1 and image_coordenates[0][i] == sc:
            baixo_repetido = True
    if sr+1 < len(image) and image[sr+1][sc] == image[sr][sc] and not(baixo_repetido):
        image_coordenates[0].append(sr+1)
        image_coordenates[1].append(sc)

    return image_coordenates


image_example = [[0,0,0],[0,0,0],[0,0,0,]]

print(floodFill(image_example, 1, 1, 4))
def floodFill(image, sr, sc, newColor):

    #A ideia é verificar se existe algum semelhante à esquerda, direita, em cima ou em baixo do starting pixel.
    image_fill = image.copy()
    #À direita
    if sc+1 < len(image[0]) and image[sr][sc+1] == image[sr][sc]:
        pass
    #À esquerda
    if sc-1 > -1 and image[sr][sc-1] == image[sr][sc]:
        pass
    #Em cima
    if sr-1 > -1 and image[sr-1][sc] == image[sr][sc]:
        pass
    #Em baixo
    if sr+1 < len(image) and image[sr+1][sc] == image[sr][sc]:
        pass


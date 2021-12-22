matriz = [[1, 2], [3, 4], [5, 6], [7]]
i = 0
x = 0
while i < len(matriz):
    try:
        print(matriz[i][x])
        x = x + 1
    except IndexError:
        print("O valor mais alto da lista {i} é: {max}".format(i=i, max=max(matriz[i])))
        i = i + 1
        x = 0


# Algoritmo de Dijkstra que funciona
def dijkstra(matriz, vOrigem, vDestino):
    n = len(matriz)
    custo = [float('inf')] * n
    rota = [None] * n
    visitado = [False] * n

    custo[vOrigem] = 0

    for _ in range(n):
        minCusto = float('inf')
        paraVisitar = -1
        for i in range(n):
            if not visitado[i] and custo[i] < minCusto:
                minCusto = custo[i]
                paraVisitar = i

        if paraVisitar == -1:
            break

        visitado[paraVisitar] = True

        for i in range(n):
            if matriz[paraVisitar][i] != -1 and custo[i] > custo[paraVisitar] + matriz[paraVisitar][i]:
                custo[i] = custo[paraVisitar] + matriz[paraVisitar][i]
                rota[i] = paraVisitar

    rotaMinimo = []
    i = vDestino
    while i is not None:
        rotaMinimo.append(i)
        i = rota[i]
    rotaMinimo.reverse()

    print(rotaMinimo, custo[vDestino])


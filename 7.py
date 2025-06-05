def imprimir(altura=7):
    for i in range(altura - 2, -1, -1):
        for j in range(altura):
            if i == altura//2 or j == altura//2 or j == i  or j == altura - i - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
imprimir(9)
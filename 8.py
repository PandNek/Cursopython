print("Tienes las siguientes opciones: 1 genera una extrella, 2 usa una calculadora, 3 imprime un mensaje,  4 imprime numeros primos, 5 imprime una lista, 6 contar")
opcion = input("Ingresa tu opcion: ")
if opcion == "1":
    def imprimir(altura=7):
        for i in range(altura - 2, -1, -1):
            for j in range(altura):
                if i == altura//2 or j == altura//2 or j == i  or j == altura - i - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    imprimir(int(input("Ingresa un numero: ")))
if opcion == "2":
    print("Ingresa la operacion que deseas realizar, ejemplo: 2+2")
    operacion = input("Ingresa tu operacion: ")
    if "+" in operacion:
        print(eval(operacion))
    if "-" in operacion:
        print(eval(operacion))
    if "*" in operacion:
        print(eval(operacion))
    if "/" in operacion:
        print(eval(operacion))
if opcion == "3":
    print("Ingresa el mensaje que quieras que este: ")
    mensaje = input("Ingresa tu mensaje: ")
    print(mensaje)
if opcion == "4":
    print("Estos son los numeros primos entre 1 y 100: ")
    print([n for n in range(1, 101) if all(n % d != 0 for d in range(2, int(n*0.5) + 1)) and n > 1])
if opcion == "5":
    print("Por que quieres imprimir una lista?")
    list = input("Ingresa el nombre de la lista: ")
    contenido = input("Ingresa el contenido de la lista: ")
    contenido = contenido.split(",")
    print("La lista {list} contiene: {contenido}".format(list=list, contenido=contenido))
if opcion == "6":
    contador = input("Ingresa el numero que deseas contar: ")
    contador2 = input("Ingresa el numero que deseas contar hasta: ")
    for i in range(int(contador), int(contador2)):
        print(i)
""" numero = 1
while numero <=100:
    contador =1
    x=0
    while contador <= numero:
        if numero % contador == 0:
            x += 1
        contador = contador + 1
    if x == 2:
        print(numero)
    numero = numero + 1
 """
""" for i in range(1, 100):
    if i > 1 and all(i % j != 0 for j in range(2, i)):
        print(i) """
print([n for n in range(1, 101) if all(n % d != 0 for d in range(2, int(n*0.5) + 1)) and n > 1])
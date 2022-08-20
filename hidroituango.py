#ENTRADA DEL PROBLEMA
nivelAgua=int(input("Digite el nivel del agua de la presa: "))

#PROSESO DEL PROBLEMA
if (nivelAgua >= 0 and nivelAgua < 20):
    print(f'El nivel del agua {nivelAgua} esta muy bajo ')
    print("Peligro!")
elif(nivelAgua >=20 and nivelAgua <400):
    print(f'El nivel del agua {nivelAgua} esta dentro del estimado')
elif(nivelAgua >= 400):
    print(f'PELIGRO!!! el nivel del agua {nivelAgua} supero el maximo')
else:
    print("Digite una opcio valida")
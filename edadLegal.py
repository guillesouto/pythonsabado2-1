#ENTRADA DEL PROBLEMA
edad=int(input("Digite la edad del individuo: "))

#PROSESO DEL PROBLEMA
if (edad <=0 or edad >= 130):
    print("papi no ande inventado que no existe")
elif(edad > 0 and edad <= 14):
    print(f'El individuo tiene {edad} es considerado un niño niño vaya pal parque')
elif(edad >=15 and edad <=28):
    print(f'El individuo tiene {edad} es considerado un joven aproveche mientras pueda y estudie')
elif(edad >=29 and edad <=60):
    print(f'El individuo tiene {edad} es un adulto ... nosjo a que hora trabajas? que vas tarde')
elif(edad >= 61 and edad <130):
    print(f'El individuo tiene {edad} ya considerado un adulto mayor  cuide del abuelito')
else:
    print("Digite una edad valida")
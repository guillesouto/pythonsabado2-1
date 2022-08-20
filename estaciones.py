#ENTRADA DEL PROBLEMA
from tokenize import String


meses= input("Digite un mes del año : ")

#PROSESO DEL PROBLEMA
if (meses == 'enero' or meses == 'febrero' or meses == 'marzo'):
    print(f'En el mes de {meses} estaras en invierno ')
    print("abrigate mucho")
elif(meses == 'abril' or meses == 'mayo' or meses == 'junio'):
    print(f'En el mes de {meses} estaras en Primavera ')
    print("disfruta del clima ¬0-0 ")
elif(meses == 'julio' or meses == 'agosto' or meses == 'septiembre'):
    print(f'En el mes de {meses} estaras en verano ')
    print("toco ir pa' la playita o prender el ventilado")
elif(meses == 'octubre' or meses == 'noviembre' or meses == 'diciembre'):
    print(f'En el mes de {meses} estaras en otoño ')
    print("limpia la casa y preparate para el frio  ...winter is coming")
else:
    print("Digite una opcio valida")
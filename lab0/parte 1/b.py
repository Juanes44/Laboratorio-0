import os
import time

def Indice(precipitacion,temperatura):
    return precipitacion/(temperatura+10)

os.system("cls")


print("-----------------------------------------------------")
print("\t\tIndice de aridez")
print("-----------------------------------------------------")

aridez=[]

entrada=(input("Digite primero precipitacion y después temperatura separadas por coma(,)"))
datos=tuple(entrada.split(','))
precipitacion=float(datos[0])
temperatura=float(datos[1])
indice=Indice(precipitacion,temperatura)
print(f"el indice de aridez es\t{indice}\n")
aridez.append(indice)
time.sleep(2)
print("los indices de aridez fueron:",aridez)
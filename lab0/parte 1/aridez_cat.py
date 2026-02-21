import os

os.system("cls")
print("--------------------------------------------------------------------------------")
print("\t\t\t\tIndice de aridez")
print("--------------------------------------------------------------------------------")
precipitacion,temperatura=map(float,input("ingresar la precipitación y temperatura total anual separada por espacios\n").split( ))

Indice=precipitacion/(temperatura+10)
a="la categoria climatica es:"
print("El indice de aridez es:",Indice)
if Indice<5:print(a,"desierto")
elif 5<Indice<10:print(a,"semiárido")
elif 10<Indice<20:print(a,"Subhúmedo")
elif 20<Indice<30:print(a,"Húmedo")
else:print(a,"Húmedo")

#120,26=3.3,desierto
#280,24=8.2,semiarido
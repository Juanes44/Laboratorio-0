import os

os.system("cls")
print("--------------------------------------------------------------------------------")
print("\t\t\t\tIndice de aridez")
print("--------------------------------------------------------------------------------")

aridez=[]
categoria=[]

arida=0
semiarida=0
semihumeda=0
humeda=0
perhumeda=0

x=int(input("¿De cuantos municipios desea recolectar el indice de aridez\t?"))

for i in range(x):
    os.system("cls")

    print("--------------------------------------------------------------------------------")
    print("\t\t\t\tIndice de aridez")
    print("--------------------------------------------------------------------------------")

    precipitacion,temperatura=map(float,input("ingresar la precipitación y temperatura total anual separada por espacios\n").split( ))

    Indice=precipitacion/(temperatura+10)
    aridez.append(Indice)



    if 0<Indice<5:
        a="Arida"
        categoria.append(a)
        arida+=1
    elif 5<Indice<10:
        a="semiárida"
        categoria.append(a)
        semiarida+=1
    elif 10<Indice<20:
        a="Semihúmeda"
        categoria.append(a)
        semihumeda+=1
    elif 20<Indice<30:
        a="Húmeda"
        categoria.append(a)
        humeda+=1
    else:
        a="Perhúmeda"
        categoria.append(a)
        perhumeda+=1

p_arida=(arida/x)*100
p_semiarida=(semiarida/x)*100
p_semihumeda=(semihumeda/x)*100
p_humeda=(humeda/x)*100
p_perhumeda=(perhumeda/x)*100

for i in range(x):
    print("\nEl indice de aridez del municipio",[i+1],"es:",aridez[i])
    print("la categoria climatica del municipio",[i+1],"es",categoria[i])

print(f"el porcentaje de zonas aridas son:{p_arida}%")
print(f"el porcentaje de zonas semiaridas:{p_semiarida}%")
print(f"el porcentaje de zonas semihumedas son:{p_semihumeda}%")
print(f"el porcentaje de zonas humedas es:{p_humeda}%")
print(f"el porcentaje de zonas perhumedas es:{p_perhumeda}%")
#120,26=3.3,desierto
#280,24=8.2,semiarido
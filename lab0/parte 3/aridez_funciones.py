#Importa la biblioteca del sistema para ejecutar un comando en especifico
import os

#Define si el municipio esta por encima o por debajo del rango de referencia
def rango(aridez,x,minimo,maximo):
    
    inRange=[]
    for i in range(x):
        if aridez[i]>maximo:
            inRange.append("esta por encima del rango de referencia")
        elif aridez[i]<minimo:
            inRange.append("esta por debajo del rango de referencia")
        else:
            inRange.append("esta en el rango de referencia")
    return inRange
    
#Define el rango de referencia
def limites_semihumedo(indice_semihumeda,aridez,x):
    if indice_semihumeda: 
        minimo = min(indice_semihumeda)
        maximo = max(indice_semihumeda)
        print("Indices semihúmedos:", indice_semihumeda)
        print("Mínimo:", minimo)
        print("Máximo:", maximo)
        inRange=rango(aridez,x,minimo,maximo)
    else:
        print("No hay zonas semihúmedas, no se puede calcular mínimo ni máximo.")
        inRange=rango(aridez,x,minimo=10,maximo=20)
    return inRange
    
#Comando que limpia la consola
os.system("cls")
print("--------------------------------------------------------------------------------")
print("\t\t\t\tIndice de aridez")
print("--------------------------------------------------------------------------------")

#Crea listas para su posterior llenado
aridez=[]
categoria=[]

#crea variables y se igualan a 0 para despues ir sumandoles los municipios a cada categoria
arida=0
semiarida=0
semihumeda=0
humeda=0
perhumeda=0

#Pide al usuario el numero de municipios
x=int(input("¿De cuantos municipios desea recolectar el indice de aridez\t?"))
while x<=0:
    x=int(input("¿De cuantos municipios desea recolectar el indice de aridez\t?"))

#Mide el indice de aridez
for i in range(x):
    os.system("cls")

    print("--------------------------------------------------------------------------------")
    print("\t\t\t\tIndice de aridez")
    print("--------------------------------------------------------------------------------")



    while True:
        datos = input("Ingresar la precipitación y temperatura total anual separadas por espacio:\n").split()
        
        if len(datos) != 2:
            print("Error: Debe ingresar exactamente 2 valores.")
            continue
        
        else:
            precipitacion = float(datos[0])
            temperatura = float(datos[1])
            break

    Indice=precipitacion/(temperatura+10)
    aridez.append(Indice)


#Clasifica a cada municipio por categoria
    if 0<=Indice<5:
        a="Arida"
        categoria.append(a)
        arida+=1
    elif 5<=Indice<10:
        a="semiárida"
        categoria.append(a)
        semiarida+=1
    elif 10<=Indice<20:
        a="Semihúmeda"
        categoria.append(a)
        semihumeda+=1
    elif 20<=Indice<30:
        a="Húmeda"
        categoria.append(a)
        humeda+=1
    else:
        a="Perhúmeda"
        categoria.append(a)
        perhumeda+=1

#Calcula los porcentajes
p_arida=(arida/x)*100
p_semiarida=(semiarida/x)*100
p_semihumeda=(semihumeda/x)*100
p_humeda=(humeda/x)*100
p_perhumeda=(perhumeda/x)*100
    
indice_semihumeda=[x for x in aridez if 10<=x<=20]

#Ejecuta la funcion para determinar rango
inRange=limites_semihumedo(indice_semihumeda,aridez,x)

#Muestra en consola la aridez,categoria y si esta por encima o por debajo del rango de referencia
for i in range(x):
    print("\nEl indice de aridez del municipio",[i+1],"es:",aridez[i])
    print("la categoria climatica del municipio",[i+1],"es",categoria[i])
    print("El municipio",[i+1],inRange[i])

#Muestra los porcentajes en consola
print(f"\nel porcentaje de zonas aridas son:{p_arida}%")
print(f"el porcentaje de zonas semiaridas:{p_semiarida}%")
print(f"el porcentaje de zonas semihumedas son:{p_semihumeda}%")
print(f"el porcentaje de zonas humedas es:{p_humeda}%")
print(f"el porcentaje de zonas perhumedas es:{p_perhumeda}%")
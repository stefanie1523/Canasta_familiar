
"""
proyecto algebra 2023b
codigo que da lo que se puede comprar de la canasta familiar de colombia 2023 para un mes de un adulto 
con un valor determinado

"""
print("La siguiente lista muestra los alimentos que puede comprar con un monto indicado segun la cansta familiar de colombia 2023 para un mes")
#primero le pedimos cuanto dinero tiene para el mercado y asi calcular cuanto puede comprar
print("Ingrese cuanto dinero tiene presupuestado para el mercado: ")
dinero=float(input())
if(dinero<32530):
    #si el dinero es menor a este valor va a salir que es insuficiente, ya que lo primero en la lista cuesta 32530
    print("no tiene fondos suficientes")
else:
    #entra aqui si el valor es mayor al indicado
    #la lista de lo que contiene la canasta familiar basica con sus nombres, cantitades,unidades y valores
    #cada una de ellas en una lista
    listaNombres=["Frutas", "Verduras", "Carnes","Leche", "Queso",  "Huevos", "Pan", "Arroz"]
    listaCantidades=[6,8,6,10,1,20,5,1.5]
    listaUnidadMedidas=["kg", "kg","kg", "L", "kg",  "unidades", "kg", "kg"]
    listaPrecios=[32530,29670,118310,37990,15260,12000,41330,5560]
    #usamos un diccionario en los cuales ponemos las listas
    canastaBasica = {
        'nombre': listaNombres,
        'cantidad': listaCantidades,
        'unidadMedida': listaUnidadMedidas,
        'precio': listaPrecios
    }
    #se crea una lista temporal para ir sumando para lo que alcanza
    listaCantidadesTemp=[0,0,0,0,0,0,0,0]
    #para que todo este correcto y todos los datos esten incluidos 
    longitudListas=(len(listaCantidades)+len(listaNombres)+len(listaUnidadMedidas)+len(listaPrecios))/4
    #son 8 los articulos inlcuidos en la canasta familiar
    if (longitudListas==8):
        while dinero>=0:
            #mientras que el dinero no sea menor que cero se ejecutara esta accion
            for i in range(int(longitudListas)):
                #este For va pasar por cada uno de los articulos e ira restando el precio de cada uno de ellos 
                temp=dinero
                #se guarda temporalmente el dinero antes de restarlo 
                dinero=dinero-canastaBasica["precio"][i]
                if dinero>=0:
                    #solo si el dinero es mayor a 0 se agrega a la lista temporal
                    listaCantidadesTemp[i]+=canastaBasica["cantidad"][i] 
                else:
                    break     
                #si no lo es no pasa nada    
            #este ciclo se repetira hasta que el dinero sea 0 o sea menor a 0, todas las cosas compradas se agregan en la lista temporal y se suman
    else:
        pass
    #para cada uno de los objetos se imprimira un mensaje 

    for j in range(int(longitudListas)):
        #se pasa la cantidad comprada a la lista de cantidad de la canasta 
        canastaBasica["cantidad"][j]=listaCantidadesTemp[j]
        if canastaBasica["cantidad"][j]==0:
            #si en alguna casilla la cantidad es cero (es decir no alcanzo a comprar )no se imprimira
            pass
        else:
            #si existe algun dato este se imprimira 
            print(f"Usted puede comprar {canastaBasica['cantidad'][j]} {canastaBasica['unidadMedida'][j]} de {canastaBasica['nombre'][j]}")
    #como guardamos el dinero siempre antes que se reste y quede negativo podemos imprimir lo que sobraria 
    print("Le sobrarian: ", temp)

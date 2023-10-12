#proyecto algebra 2023b
"""
codigo que da lo que se puede comprar de la canasta familiar de colombia 2023 
con un valor determinado

"""
print("Lista de cosas que puede comprar de la canasta familiar 2023(son en total 8 objetos) con el monto de dinero preferible ")
print("Ingrese cuanto dinero tiene para el mercado : ")
dinero=float(input())
if(dinero==0):
    print("no tiene fondos suficientes")

#la lista de lo que contiene la canasta familiar basica con sus unidades y valores
listaNombres=["Frutas", "Verduras", "Leche", "Queso", "Carnes", "Huevos", "Pan", "Arroz"]
listaCantidades=[6,8,10,1,6,20,5,1.5]
listaUnidadMedidas=["kg", "kg", "L", "kg", "kg", "unidades", "kg", "kg"]
listaPrecios=[32530,29670,37990,15260,118310,12000,41330,5560]
canastaBasica = {
    'nombre': listaNombres,
    'cantidad': listaCantidades,
    'unidadMedida': listaUnidadMedidas,
    'precio': listaPrecios
}

listaCantidadesTemp=[0,0,0,0,0,0,0,0]

longitudListas=(len(listaCantidades)+len(listaNombres)+len(listaUnidadMedidas)+len(listaPrecios))/4
if (longitudListas==8):
    while dinero>=0:
        for i in range(int(longitudListas)):
            temp=dinero
            dinero=dinero-canastaBasica["precio"][i]
            if dinero>=0:
                listaCantidadesTemp[i]+=canastaBasica["cantidad"][i] 
            else:
                break        
else:
    pass

for j in range(int(longitudListas)):
    canastaBasica["cantidad"][j]=listaCantidadesTemp[j]
    if canastaBasica["cantidad"][j]==0:
        pass
    else:
        print(f"Usted puede comprar {canastaBasica['cantidad'][j]} {canastaBasica['unidadMedida'][j]} de {canastaBasica['nombre'][j]}")
print("Le sobrarian: ", temp)

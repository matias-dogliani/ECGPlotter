import pandas as pd     #Depende de xlrd también 

archivo = pd.read_excel("./Datos.xlsx") 

lis_archivo = archivo.to_dict("list")  # Diccionario con Key ="Columna" : [filas de esa columna]
records = archivo.to_dict("records")   # Lista de diccionarios por fila 

#Se puede trabajar directamente con dataFrame de pandas

INDICE = 0 
#print(archivo['Quimica'])       #Una columna    
#print(archivo.loc[INDICE])      #Toda una fila

print(archivo.loc[INDICE]['Quimica'])  #Un único elemento de toda una fila


#Las operaciones se realizan con elementos de la misma fila. 
promedio = archivo['Quimica'] + archivo['Matematica'] + archivo['Fisica'] 
promedio /= 3 

print(promedio) 

print("El promedio máxima", promedio.max() )









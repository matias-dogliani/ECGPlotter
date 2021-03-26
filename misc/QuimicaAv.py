import pandas as pd 


def indAv(data, i): 
    alumno= data.loc[i]
    prom = (alumno['Quimica'] + alumno['Matematica'] +  alumno['Fisica'])  / 3 
    return prom  





def Showpass(data,materia): 
    aprobados = data[data[materia] >= 4] 
    return aprobados




data = pd.read_excel("Datos.xlsx") 
promedio= sum(data['Quimica']) / len(data['Quimica']) 



print("El promedio de todos los alumno de Química es ", promedio) 
print("El promedio del alumno 0 es", indAv(data,0)) 
print("Los aprobados en Quimica son: ", Showpass(data,'Quimica')) 
































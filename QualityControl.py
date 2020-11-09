import pandas as pd 
import numpy as np 



data = pd.read_csv("ControlCalidadBotellas.csv") 


media = sum(data['Fallas']) / len(data) 

muestras = ((data['Fallas'] - media)**2) 
varianza = sum(muestras) / len(data) 

if (media != varianza): 
    print("Las fallas no tienen una distribución de Poisson") 
else: 
    print("Las fallas tienen una distribución de Poisson") 





'''
ECG Processing - Dogliani Matias, Toth Lautaro.

*Calcular los picos de la frecuencia cardiaca (signal.find_peaks)
*Calcular la frecuencia cardiaca bpm
*Determinar si dormia, reposaba o hacia actividad física
*Pedir sexo, edad
*Almacenar resultado en un archivo de texto.txt

'''


import pandas as pd
import numpy as np



data = read_excel('electrocardiograma.xlsx')
print(data)


'''
ECG Processing - Dogliani Matias, Toth Lautaro.

*Calcular los picos de la frecuencia cardiaca (signal.find_peaks)
*Calcular la frecuencia cardiaca bpm
*Determinar si dormia, reposaba o hacia actividad física
*Pedir sexo, edad
*Almacenar resultado en un archivo de texto.txt

'''
#Scipy puede generar un ECG arbitrariamente para probar con otros scipy.misc.electrocardiograma()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

data = pd.read_excel('electrocardiograma.xlsx')

TimeAxe = data['tiempo']
SignalAxe = data['señal']
picos,_ = find_peaks(SignalAxe, height=0.5, width = 10)


#Como el eje x son segundos, el periodo es la cantidad de
#segundos entre dos picos consecutivos
#La frecuencia es la inversa. 1 Hz es un pulso en un segundo, que equivale
#a 60 pulsos (latidos) en un minuto

T = TimeAxe[picos[1]] -TimeAxe[picos[0]]
freq = (1/T) * 60
lpm = str(freq) + 'bpm'


plt.plot(TimeAxe,SignalAxe,'g')
plt.plot(TimeAxe[picos], SignalAxe[picos],'o', color = 'red')
plt.grid()
texto1 = plt.text(0.5,max(SignalAxe), lpm, fontsize=20)

plt.title('ECG')
plt.savefig('ECGSignal',dpi=300)
plt.show()

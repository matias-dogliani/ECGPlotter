
'''
ECG Processing - Dogliani Matias, Toth Lautaro.

*Calcular los picos de la frecuencia cardiaca (signal.find_peaks)
*Calcular la frecuencia cardiaca bpm
*Determinar si dormia, reposaba o hacia actividad física
*Pedir sexo, Edad
*Almacenar resultado en un archivo de texto.txt

'''
#Scipy puede generar un ECG arbitrariamente para probar con otros scipy.misc.electrocardiograma()
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from scipy.signal import find_peaks



#Datos requeridos para el calculo de la frecuencia ideal y clasificacion de estado
#Ingreso de datos y comprobacion

Edad = 0
Sexo = 'AA'
Peso = 0

while(Edad <= 0):
    try:
        Edad = int(input('Edad del paciente: ')) #Al utilizar try no se rompe
                                                 # si no se ingresa un numero de base10
    except:
        Edad = 0
    if Edad <= 0 or  Edad >= 120:
        Edad = 0
        print('Edad ingresada incorrecta, vuelva a ingresar')

while(Peso <= 0):
    try:
        Peso = int(input('Ingreso el Peso del paciente (Kg): '))
    except:
        Peso = 0
    if Peso <= 0 or Peso >= 500:
        Peso = 0
        print('Edad ingresada incorrecta, vuelva a ingresar')

while Sexo[0] != 'M' and  Sexo[0] != 'F':
    Sexo = input('Ingrese el sexo del paciente (M)asculino, (F)emenino: ')
    Sexo.upper()
    if Sexo[0] != 'M' and Sexo[0] != 'F':
        Sexo = 'AA'
        print('Sexo ingresado incorrecto, vuelva a ingresar')


#Calculo de frecuencia maxima  y clasificaicon de estados

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
texto = 'Bpm = ' + str(round(freq, 2)) + '\n Estado: '
FreqReposo = 80  #Promedio segun Wikipedia


if Sexo[0] == 'M':
    FreqMax = (210 - (0.5*Edad)) - (0.01*Peso) +4
else:
    FreqMax= (210 - (0.5*Edad)) - (0.01*Peso)


#Me fijo de cual esta mas cerca para definir el estado.
if abs(freq - FreqReposo) < abs(freq - FreqMax*0.7):
    estado = 'Reposo'
else:
    estado = 'Ejercitando'

texto += estado


#Guardo informacion del paciente

Paciente = 'Edad: ' + str(Edad) + '\n'
Paciente += 'Peso: ' + str(Peso) + '\n'
Paciente += 'Sexo: ' + Sexo[0] + '\n'
Paciente += 'Estado: ' + estado +  '\n'

fd = open('Pacientes.txt', 'a')
fd.write(Paciente)

fd.close()

plt.text(0.25,max(SignalAxe),
     texto, ha="center", va="center", size=15,
    bbox=dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9))

plt.plot(TimeAxe,SignalAxe,'g')
plt.plot(TimeAxe[picos], SignalAxe[picos],'o', color = 'red')
plt.grid()
plt.title('ECG')
plt.savefig('ECGSignal',dpi=300)
plt.show()

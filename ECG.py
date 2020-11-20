
'''
ECG Processing - Dogliani Matias, Toth Lautaro.

*Calcular los picos de la frecuencia cardiaca (signal.find_peaks)
*Calcular la frecuencia cardiaca bpm
*Determinar si dormia, reposaba o hacia actividad física
*Pedir sexo, Edad
*Almacenar resultado en un archivo de texto.txt

'''
#Scipy puede generar un ECG arbitrariamente para probar con otros scipy.misc.electrocardiograma()
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from scipy.signal import find_peaks


def DataReq():

    Edad = 0
    Sexo = 'AA'
    Peso = 0
    Nombre =""

    while(len(Nombre) <= 1):
        Nombre  = input("Nombre del paciente: ")
        for caracter in Nombre:
            if ((caracter < 'A' or caracter >'z') ):   #Codigo ASCII. Espacios permitidos
                if caracter != " ":
                    Nombre =""

        if (Nombre == ""):
            print("No se permiten caracteres especiales o numeros en el nombre")

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
        Sexo = Sexo.upper()
        if Sexo[0] != 'M' and Sexo[0] != 'F':
            Sexo = 'AA'
            print('Sexo ingresado incorrecto, vuelva a ingresar')

    Edad = int(Edad)
    Peso = int(Peso)
    return (Sexo[0],Edad,Peso,Nombre)

def calcFreq(ecg):

    TimeAxe = ecg['tiempo']
    SignalAxe = ecg['señal']
    picos, _ = find_peaks(SignalAxe, height=0.5, width = 10)

    #La frecuencia es el inverso entre el tiempo de dos picos consecutivos.
    #1 Hz es un pulso en un segundo, que equivale
    #a 60 pulsos (latidos) en un minuto

    T = TimeAxe[picos[1]] -TimeAxe[picos[0]]
    freq = (1/T) * 60
    return freq, picos  #Devuelvo picos porque lo uso despues, así no lo calculo 2 veces

def CalcFreqMax(Sexo,Edad,Peso):
    Edad = int(Edad)
    Peso = int(Peso)
    if Sexo == 'M':
        FreqMax = (210 - (0.5*Edad)) - (0.01*Peso) +4
    else:
        FreqMax= (210 - (0.5*Edad)) - (0.01*Peso)
    return FreqMax

def SaveData(Sexo,Edad,Peso,Nombre, estado):

    Paciente = '\n Nombre: ' + str(Nombre) + '\n'
    Paciente += 'Edad: ' + str(Edad) + '\n'
    Paciente += 'Peso: ' + str(Peso) + '\n'
    Paciente += 'Sexo: ' + Sexo + '\n'
    Paciente += 'Estado: ' + estado +  '\n'

    fd = open('Pacientes.txt', 'a')
    fd.write(Paciente)
    fd.close()

def EstadoDef(freq, FreqMax):

    #Valores umbrales aproximados según articulo brindado
    FreqEjercicio =FreqMax
    FreqDurmiendo =60
    FreqReposo = 80

    if freq < 60:
        return 'Durmiendo'

    #Como no es un umbral estricto definido, se define segun cercanía
    if abs(freq - FreqReposo) < abs(freq - FreqMax*0.7):
        return 'Reposo'
    else:
        return 'Ejercitando'



def PlotEcg(ecg, picos, texto,Nombre):

    TimeAxe = ecg['tiempo']
    SignalAxe = ecg['señal']

    plt.text(0.25,max(SignalAxe)+0.,
         texto, ha="center", va="center", size=15,
        bbox=dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9))

    plt.plot(TimeAxe,SignalAxe,'g')
    plt.plot(TimeAxe[picos], SignalAxe[picos],'o', color = 'red')
    plt.grid()
    plt.title('ECG')
    plt.savefig('ECGSignal'+ "_" + Nombre +".png",dpi=300)
    plt.show()

def main():

    Sexo,Edad,Peso,Nombre = DataReq()
    data = pd.read_excel('electrocardiograma.xlsx')
    freq, picos  = calcFreq(data)
    freqMax = CalcFreqMax(Sexo,Edad,Peso)
    texto = 'Bpm = ' + str(round(freq, 2)) + '\n Estado: '
    estado = EstadoDef(freq,freqMax)
    texto +=str(estado)
    PlotEcg(data,picos,texto,Nombre)
    SaveData(Sexo,Edad,Peso,Nombre, estado)

if __name__ == "__main__":
    main()


import pygame
import numpy as np 
import time 
#Medidas y config del tablero 
WIDHT,HEIGHT = 800,800 
DEAD_COLOR = (128,128,128) 
LIVE_COLOR = (255,255,255) 
BG_COLOR = (25,25,25) 
nX, nY = 80,80
dimX =  WIDHT / nX
dimY = HEIGHT / nY


def inicializar_celdas(): 
    pass     

def contar_vecinos(x,y,estadoCelda):
 #Numero de vecinos cercanos, tratando al tablero como sin bordes (un toroide)
 #La ultima celda es adyacente con la primera de la misma fila 
    n_vec = (estadoCelda[(x-1) % nX, (y-1) % nY] +  
                estadoCelda[(x)   % nX, (y-1) % nY] + 
                estadoCelda[(x+1) % nX, (y-1) % nY] + 
                estadoCelda[(x-1) % nX, (y)   % nY] + 
                estadoCelda[(x+1) % nX, (y)   % nY] + 
                estadoCelda[(x-1) % nX, (y+1) % nY] + 
                estadoCelda[(x)   % nX, (y+1) % nY] + 
                estadoCelda[(x+1) % nX, (y+1) % nY] ) 
                                                            
    return n_vec 
                                                               
def dibujar_celda(wnd, x, y, LINE_COLOR,w):                    
    lii= (x*dimX, y*dimY)                                      
    lid= ((x+1)*dimX, y*dimY)
    lsi= (x*dimX, (y+1)*dimY)
    lsd= ((x+1)*dimX, (y+1)*dimY)
    celda = [lii,lid,lsd,lsi]
    pygame.draw.polygon(wnd,(LINE_COLOR),celda, width=w)  


def main (): 

    pygame.init() 
    #Configuración de la pantalla del juego 
    wnd = pygame.display.set_mode((HEIGHT,WIDHT)) 
    wnd.fill(BG_COLOR) 
    #Estado de la celda 
    estadoCelda = np.zeros((nX,nY)) 
   
    

    while True:

        wnd.fill(BG_COLOR) 
        nuevo_estadoCelda = np.copy(estadoCelda)
        
        #Patron de palo 
        nuevo_estadoCelda[5, 3] = 1
        nuevo_estadoCelda[5, 4] = 1
        nuevo_estadoCelda[5, 5] = 1

        
        for y in range(0,nY): 
            for x in range(0,nX):

                num_vecinos = contar_vecinos(x,y,estadoCelda) 
                print(num_vecinos)  
                
                #Regla 1 : Celda muerta con 3 vecinas revive 
                if estadoCelda[x,y] == 0 and num_vecinos ==3:
                    nuevo_estadoCelda[x,y] =1 

                #Regla 2: Celula vica con mas de 3 vecinos o menos de 2 muere: 
                if estadoCelda[x,y] ==1 and (num_vecinos < 2 or num_vecinos >3): 
                    nuevo_estadoCelda[x,y] = 0 

                if estadoCelda[x,y] == 0 : 
                    dibujar_celda(wnd,x,y,DEAD_COLOR,1) 
                else:
                    dibujar_celda(wnd,x,y,LIVE_COLOR,0) 


        estadoCelda = np.copy(nuevo_estadoCelda) 
        time.sleep(0.1)     
        pygame.display.flip()   











if __name__ == '__main__': 
    main() 

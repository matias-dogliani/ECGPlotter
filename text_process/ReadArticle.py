

def countWords(texto,word): 
    
    noticia = open(texto)
    noneed = ['\ufeff', '—', '\n', '’s', ',', '.']
    palabras= [] 
    contador = 0 
    lineas = noticia.readlines()   #Cada renglon un elemento de una lisa 
    
    for linea in lineas: 

        for caracter in noneed: #borro el caracter de toda la linea 
            linea = linea.replace(caracter,'') 
       
        palabras_linea = linea.split(' ') #el método split es de cadenas de texto  
        
        for palabra in palabras_linea:
           if (palabra != ''): 
                  palabras.append(palabra.upper()) 
    for palabra in palabras: 
        if palabra == word.upper(): 
            contador +=1
    
    return contador    

def findMaxWord(texto): 

    noticia = open(texto)
    noneed = ['\ufeff', '—', '\n', '’s', ',', '.']
    palabras= [] 
    contador = 0 
    Max = 0
    MaxWord = 0
    lineas = noticia.readlines()   #Cada renglon un elemento de una lisa 
    
    for linea in lineas: 

        for caracter in noneed: #borro el caracter de toda la linea 
            linea = linea.replace(caracter,'') 
       
        palabras_linea = linea.split(' ') #el método split es de cadenas de texto  
        
        for palabra in palabras_linea:
           if (palabra != ''): 
                  palabras.append(palabra.upper()) 


    for palabra in palabras: 
        for i in palabras: 
            if palabra == i: 
                contador +=1 
        
        if contador > Max:
            MaxWord = palabra
    
    return MaxWord

noticia = 'noticia.txt'
print("La palabra Trump aparece",countWords(noticia,'Trump'),"veces")  
print("La palabra the aparece",countWords(noticia,'the'),"veces")  
print("La palabra Trump aparece",countWords(noticia,'Trump'),"veces")  
print("La palabra que más aparece es", findMaxWord(noticia)) 













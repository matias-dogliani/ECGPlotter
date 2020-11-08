brackets = {')':'(', ']':'[', '}':'{'}
acum = [] 

inp = input() 

#Guardo todos los que abren en la pila 
for i in inp: 
    if i in brackets.values():
        acum.append(i)


for i in inp: 
    if i in brackets.keys(): 
        if brackets.get(i) == acum[len(acum) - 1]:  
            acum.pop() 
        else: 
            break; 
if len(acum) ==0 :  
    print('True') 
else:   
    print('False')

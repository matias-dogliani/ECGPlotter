openers = ['(', '{', '[']
closers = [')', '}', ']']

acum = [] 

inp = input() 
inp = "{print(#hola)}" 
#Guardo todos los que abren en la pila 
for i in inp: 
    if i in openers:
        print(i)
        acum.append(i)

print(acum) 

for i in inp: 
    if i in closers: 
        if i == acum[len(acum) - 1]:  
            acum.pop() 
        else: 
            break; 
print(acum) 
if len(acum) ==0 :  
    print('True') 
else:   
    print('False')

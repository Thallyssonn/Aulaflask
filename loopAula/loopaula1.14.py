# imprimir apenas numeros pares de 1 a 10
# que sao maiores que 4 ou menores que 8

for i in range (1, 11): 
    if i % 2 == 0 and (i > 4 or i < 8):
        print(i)
        
print ('--------------')
        
    #imprimir apenas numeros imapares de 1 a 10
    # que sao menores que 3 ou maiores que 7
    
for i in range(1, 11):
        if i % 2 != 0 and (i < 3 or i > 7):
            print(i)
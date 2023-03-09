# armazenar um numero pquieno

maior_numero = -999999999
# entra com o primeiro

number = int(input('entre com um numero ou digite -1 para parar: '))
# se o numero nao for igual a -1 continua

while number != -1: 
# o numero e maior que o maior_numero
    if number > maior_numero:
# sim, atualiza maior_numero.
        maior_numero = number
    # Entre com o proximo numero
    number = int(input('entre com um numero ou digite -1 para parar: '))
    
    #imprime o maior numero.
print('o numero e: ', maior_numero)


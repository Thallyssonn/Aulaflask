numero_secreto = 42
tentativa = 1  

while tentativa <= 3:
    palpite = int(input('Adivinhe o numero secreto: '))
    if palpite == numero_secreto:
        print('parabens, voce acertou')
        break
    else:
        if palpite > numero_secreto:
            print('o numero secreto e meneor do que', palpite)
        else:
            print('o numero secreto e maior do que', palpite)
    tentativa += 1
if tentativa > 3:
    print('suas tenattivas acabaram. o numero secreto era', numero_secreto)
    
           
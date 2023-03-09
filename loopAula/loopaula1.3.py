tentativas = 0 
while tentativas <3:
    senha = input('digite a senha')
    if senha == 'senha123':
        print('acesso concedido')
        break
    else:
        print('senha incorreta. tente novamente')
        tentativas += 1
else:
    print('voce excedeu o numero maximo de tentativas')
    
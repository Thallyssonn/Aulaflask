x = int(input("digite o primeiro numero"))
y = int(input("digite o segundo numero"))
z = int(input("digite o terceiro numero"))

if x > y and x > z:
    result = "x é o maior numero"
elif y > x and y > z:
    result = "y é o maior numero"
elif z > x and z > y:
    result = "z é o maior numero"
else: 
    result = "ha numeros iguais"
print(result)

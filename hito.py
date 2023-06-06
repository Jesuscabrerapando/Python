import random
numeros=[random.randint(1,10)] 
i=1
while i<10:
  numero=random.randint(1,10)
  if numero not in numeros:
    numeros.append(numero)
    i=i+1
print(numeros)
print(sorted(numeros))



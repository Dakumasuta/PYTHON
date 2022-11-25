#quadratica :)

from cmath import sqrt


print ('Ingrese sus datos')

a = int(input('Ingrese el valor de "a":'))
b = int(input('Ingrese el valor de "b":'))
c = int(input('Ingrese el valor de "c":'))

raiz1 = (-b + sqrt( (b**2) - 4*a*c ))/(2*a)
raiz2 = (-b - sqrt( (b**2) - 4*a*c ))/(2*a)

print ('Tus resultados son: ')
print (raiz1)
print (raiz2)

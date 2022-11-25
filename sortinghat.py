#sorting hat 

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('Which Hogwarts School of Witchcraft and Wizardry suits you best?')

print ('Q1) Do you like Dawn or Dusk? \n1) Dawn \n2) Dusk')

ans1 = int(input('Your answer is... \n'))

if ans1 == 1:
    Gryffindor +=1
    Ravenclaw +=1
elif ans1 == 2:
    Hufflepuff +=1
    Slytherin +=1
else:
    print('Wrong input bb...\n')

print ('Q2) When Im dead, I want people to remember me as: \n1) The Good \n2) The Great \n3) The Wise \n4) The Bold')

ans2 = int(input('Your answer is... \n'))

if ans2 == 1:
    Gryffindor +=1
elif ans2 == 2:
    Ravenclaw +=1
elif ans2 == 3:
    Hufflepuff +=1
elif ans2 == 4:
    Slytherin +=1
else:
    print('Wrong input bb...\n')


print('Q3) Which kind of instrument most pleases your ear? \n1) The violin \n2) The trumpet \n3) The piano \n4) The drum')

ans3 = int(input('Your answer is... \n'))

if ans3 == 4:
    Gryffindor +=1
elif ans3 == 3:
    Ravenclaw +=1
elif ans3 == 2:
    Hufflepuff +=1
elif ans3 == 1:
    Slytherin +=1
else:
    print('Wrong input bb... \n')



houses = ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']
housesint = [Gryffindor, Ravenclaw, Hufflepuff, Slytherin]

mayor = max(housesint)
ubicacion = housesint.index(mayor)

print('\n Congrats!!!! \nYou are part of the ' + houses[ubicacion] + ' house!!!')






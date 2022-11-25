#currency

yuan = int(input('How much do you have in YUAN: '))
yen = int(input('How much do you have in YEN: '))
won = int(input('How much do you have in WON: '))

total = (yuan / 7.14) + (yen / 138.77) + (won / 1327.78)

print ('You have ' + str(total) + ' dollars available.')



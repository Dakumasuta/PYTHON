#magic8

import random

magic8ball = ['Yes - definitely.','It is decidedly so.','Without a doubt.','Reply hazy, try again.','Ask again later.',
'Better not tell you now.' ,'My sources say no.', 'Outlook not so good.', 'Very doubtful.']

question = input('Ask me anyting bb: ')

response = random.choice(magic8ball)
print('Magic 8 Ball: ' + response)
import re


# numero = '01 34 54 89 09'
#numero = '05-34-54-89-09'
numero = '01 02 34 54 89'
reg = re.compile('(07|01|05)(?P<debut> ([-_ ]?\d{2}){4})')
# reg2 = re.compile('\d{2}([-_ ]?\d{2}){3}')
# operator = {'05': 'MTN', '01': 'MOOV', '07': 'ORANGE'}
# validator = reg.match(numero)

print(reg.sub('02\g<debut>', numero))

# if validator:
#     print(operator[validator.groups()[0]])
# elif reg2.match(numero):
#     print('Passez à dix chiffres')
# else:
#     print('le numero invalide')

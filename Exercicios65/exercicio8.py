# 8. Desenvolva um algoritmo que pergunte ao usuário o estado civil (solteiro, casado, divorciado, viúvo) e exiba uma mensagem correspondente.

estado = str(input('Qual o seu estado Civil? casado, solteiro, divorciado ou viuvo? \n'))

if estado == 'casado':
    print(f'Seu estado civil é {estado}' )
elif estado == 'solteiro':
    print(f'Seu estado civil é {estado}' )
elif estado == 'divorciado':
    print(f'Seu estado civil é {estado}' )
elif estado == 'viuvo':
    print(f'Seu estado civil é {estado}' )
else:
    print('Estado Civil não enontrado')

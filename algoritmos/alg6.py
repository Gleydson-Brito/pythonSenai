
numero1 = int(input("Escolha o primeiro número: "))
operacao = input('Escolha a operação + - * /')
numero2 = int(input("Escolha o segundo número: "))

match operacao:
    case '+':
        print(f'numero {numero1} {operacao} {numero2}, é: {numero1 + numero2}')
    case '-':
        print(f'numero {numero1} {operacao} {numero2}, é: {numero1 - numero2}')
    case '*':
        print(f'numero {numero1} {operacao} {numero2}, é: {numero1 * numero2}')
    case '/':
        print(f'numero {numero1} {operacao} {numero2}, é: {numero1 / numero2}')
    case _:
         print('Equação inválida')   
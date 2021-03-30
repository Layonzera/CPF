while True:  # Loop infinito
    #cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]             # Elimina os dois últimos digitos do CPF
    reverse = 10                    # Contador reverso
    total = 0

    for index in range(19):
        if index > 8:               # Primeiro índice vai de 0 a 9,
            index -= 9              # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverse  # Valor total da multiplicação

        reverse -= 1                # Decrementa o contador reverso
        if reverse < 2:
            reverse = 11
            digit = 11 - (total % 11)

            if digit > 9:           # Se o digito for > que 9 o valor é 0
                digit = 0
            total = 0
            novo_cpf += str(digit)

    if cpf == novo_cpf:
        print('Válido.')
    else:
        print('Inválido.')
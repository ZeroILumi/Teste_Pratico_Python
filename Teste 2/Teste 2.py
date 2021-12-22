# Sequência de Fibonacci

# Criase a var "numero_Fn1_anterior"
# para ser o primeiro numero da Sequência de Fibonacci ou anterior"
numero_Fn1_anterior = 1
# Criase a var "numero_Fn1_atual"
# para ser o segundo numero da Sequência de Fibonacci ou atual"
numero_Fn2_atual = 1
# Criase n para ser o valor máximo do numero atual
# ou "numero_Fn2_atual" na Sequência de Fibonacci
# Sendo seu valor digitado pelo usuario da aplicação no terminal
n = int(input("Digite o valor de n \n"))
# Criase uma var chamada "soma_do_numeros_pares_Fn"
# cujo o intuito e guardar o resultado da soma dos valores contidos
# em uma lista chamada "numeros_pares_Fn"
soma_do_numeros_pares_Fn = 0
# Criase um loop que vai se repitir enquanto/while o valor do numero atual
# ou "numero_Fn2_atual" da Sequência de Fibonacci for menor ou igual ao valor
# de n que e o valor digitado pelo usuario para ser o valor máximo da
# Sequência de Fibonacci
while numero_Fn2_atual <= n:
    # Imprime o valor atual da Sequência de Fibonacci
    print(numero_Fn2_atual)
    # Verifica se o numero atual da Sequência de Fibonacci ou "numero_Fn2_atual"
    # e um numero par pois se o mod dele por 2 for exato ou seja 0 ele e par
    if numero_Fn2_atual % 2 == 0:
        # Criase um lista chamada "numeros_pares_Fn" para guardar os valores pares
        # da Sequência de Fibonacci
        numeros_pares_Fn = []
        # Acrecenta na lista "numeros_pares_Fn" os valores pares da
        # Sequência de Fibonacci atraves da coleta dos atuais(numero_Fn2_atual) pares
        # pelo if
        numeros_pares_Fn.append(numero_Fn2_atual)
        # Pegando valor por valor da lista "numeros_pares_Fn" para poder
        # acresentalos ao valor da soma de "soma_do_numeros_pares_Fn"
        for numero_par in numeros_pares_Fn:
            # Acrescenta ao valor da "soma_do_numeros_pares_Fn" os valores da
            # lista "numeros_pares_Fn"
            soma_do_numeros_pares_Fn += numero_par
    # Torna o valor atual da Sequência de Fibonacci ou "numero_Fn2_atual"
    # no resultado da soma de seu valor atual - o seu valor anterior ou "numero_Fn1_anterior"
    # para tornar o numero atual o proximo numero da Sequência de Fibonacci
    numero_Fn2_atual = numero_Fn2_atual + numero_Fn1_anterior
    # Torna o valor anterior da Sequência de Fibonacci ou "numero_Fn1_anterior"
    # no resultado da subtração do valor atual ou numero_Fn2_atual pelo seu valor
    # ou "numero_Fn1_anterior" sendo sempre o antigo valor atual
    numero_Fn1_anterior = numero_Fn2_atual - numero_Fn1_anterior
    # Verifica se o limite de n foi alcançado
    if numero_Fn2_atual > n:
        # Imprime a soma dos numero pares da Sequência de Fibonacci
        print("A soma dos pares "
              "da Sequência de Fibonacci "
              "é:{soma_dos_pares}".format(soma_dos_pares=soma_do_numeros_pares_Fn))

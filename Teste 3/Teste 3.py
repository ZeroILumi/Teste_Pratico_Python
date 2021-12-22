if __name__ == "__main__":
    # Criase um var "n" que recebe o valor que o usuario digitar
    n = int(input("Digite o valor de n \n"))
    # Criase um var "soma" dos valor para armazenar a soma dos valores
    # de n fatorial
    soma_dos_valores = 0
    # Criase um var que representa n! ou n_fatorial começando do 1
    n_fatorial = 1
    # Criase um i para ser o primeiro valor a qual n_fatorial sera multiplicado
    i = 2
    # Enquanto i for menor ou igual a n
    while i <= n:
        # n! ou n_fatorial acrescenta ao troca seu valor para o valor seu valor atual
        # multiplicado pelo valor de i
        n_fatorial = n_fatorial * i
        # i aumenta seu valor em 1 para parar o loop
        i = i + 1
    # Imprime o valor do n! ou n_fatorial
    print("O valor de %d! eh:{fatorial}".format(fatorial=n_fatorial) % n)
    # Criase uma lista que recebe cada digito do valor do n! ou n_fatorial
    lista_de_fatoriais = [int(numero) for numero in str(n_fatorial)]
    # Para cada valor/numero na lista de fatoriais
    for valor in lista_de_fatoriais:
        # A var soma dos valores soma seu valor atual com os valores da lista de fatoriais
        soma_dos_valores += valor
    # Imprime a soma dos valores do n! ou n_fatorial
    print("A soma dos valores de %d! eh:{soma}".format(soma=soma_dos_valores) %n)
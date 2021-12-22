if __name__ == "__main__":
    # Criase a var "n_times_de_futebol" para representar o numero de times
    n_times_de_futebol = int(input("Digite o numero de times de futebol \n"))
    # Criase a var "ranking_de_gols_de_cada_time" para representar o numero
    # de gols de cada time
    ranking_de_gols_de_cada_time = []
    # Criase i para limitar o loop
    i = 1
    # Criase um loop que se repetira enquanto i for menor ou igual ao numero de times de futebol
    while i <= n_times_de_futebol:
        # Coleta o numero de gols atual de cada time
        ranking_do_time_atual_do_loop = int(input("Digite o "
                                                  "ranking de gols do time {i} \n".format(i=i)))
        # Acrescenta numa lista a quantidade de gols de cada time em ordem crescente
        ranking_de_gols_de_cada_time.append(ranking_do_time_atual_do_loop)
        # Serve para parar o loop
        i = i + 1
    # Criase a var "k_novos_times_futebol" para representar o numero de times
    # novos a serem criados a partir do times antigos
    k_novos_times_futebol = int(input("Digite a quantidade de novos times a serem criados\n"))
    # Os novos times devem ser metade ou menos dos totais para não faltar times
    metade_dos_times = n_times_de_futebol-k_novos_times_futebol
    # Se a quantidade de times for maior que a metade
    if k_novos_times_futebol > metade_dos_times:
        # Enquanto a quantidade for maior que a metade
        while k_novos_times_futebol > metade_dos_times:
            # Troca o valor da var "k_novos_times_futebol" para um valor que seja a metade
            # dos times totais ou menor
            k_novos_times_futebol = int(input("Digite a "
                                              "quantidade de "
                                              "novos times a serem criados"
                                              "tem que ser metade ou menos do times "
                                              "totais\n"))
    # Pega o maior time do ranking de gols
    melhor_time = max(ranking_de_gols_de_cada_time)
    # Pega o menor time do ranking de gols
    pior_time = min(ranking_de_gols_de_cada_time)
    # Gera i para controlar o loop
    i = 1
    # Enquando i for menor ou igual ao total de novos times
    while i <= k_novos_times_futebol:
        # Imprime o numero do time novo e o numero dos times que o compõem
        print("O time {i} deve ser formado pelos times"
              " {melhor_time} e "
              "{pior_time}".format(melhor_time=melhor_time,
                                   pior_time=pior_time,
                                   i=i))
        # Remove o melhor time ja utilizado
        ranking_de_gols_de_cada_time.remove(melhor_time)
        # Remove o pior time ja utilizado
        ranking_de_gols_de_cada_time.remove(pior_time)
        # Se o lista de rankings de gols "ranking_de_gols_de_cada_time" não estiver
        # vazia
        if len(ranking_de_gols_de_cada_time) > 0:
            # Troca o valor do melhor time
            melhor_time = max(ranking_de_gols_de_cada_time)
            # Troca o valor do pior time
            pior_time = min(ranking_de_gols_de_cada_time)
        # Finaliza o loop
        i = i + 1
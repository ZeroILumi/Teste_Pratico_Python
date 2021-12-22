import numpy as np

def calcular_luckBalance():
    n_numero_de_concursos, \
    k_disputas_perdiveis = input("Digite o valor de "
                                 "numero de concursos "
                                 "e numero maximo de disputas perdiveis "
                                 "separados por espaço:\n").split(" ")
    n_numero_de_concursos = int(n_numero_de_concursos)
    k_disputas_perdiveis = int(k_disputas_perdiveis)
    if n_numero_de_concursos <= k_disputas_perdiveis:
        while n_numero_de_concursos <= k_disputas_perdiveis:
            print("O numero de disputas perdiveis deve ser menor que o numero de"
                  "concursos maximos")
            n_numero_de_concursos, \
            k_disputas_perdiveis = input("Digite o valor de "
                                         "numero de concursos "
                                         "e numero maximo de disputas perdiveis "
                                         "separados por espaço:\n").split(" ")
            n_numero_de_concursos = int(n_numero_de_concursos)
            k_disputas_perdiveis = int(k_disputas_perdiveis)
    sorte = 0
    T_importancia_do_concurso = []
    L_pontos_de_sorte = []
    concursos = []
    linha = []
    i = 1
    while i <= n_numero_de_concursos:
        quantidade_de_pontos_de_sorte_do_concurso, nivel_de_importancia = input("Digite "
                                                                                "a "
                                                                                "quantidade "
                                                                                "de "
                                                                                "Pontos "
                                                                                "de "
                                                                                "sorte e "
                                                                                "nivel de "
                                                                                "importancia "
                                                                                "associados "
                                                                                "ao "
                                                                                "concurso "
                                                                                "de "
                                                                                "numero {i} "
                                                                                "separando os por "
                                                                                "espaço:\n".format(i=i)).split(" ")
        quantidade_de_pontos_de_sorte_do_concurso = int(quantidade_de_pontos_de_sorte_do_concurso)
        nivel_de_importancia = int(nivel_de_importancia)
        L_pontos_de_sorte.append(quantidade_de_pontos_de_sorte_do_concurso)
        T_importancia_do_concurso.append(nivel_de_importancia)
        linha = [quantidade_de_pontos_de_sorte_do_concurso, nivel_de_importancia]
        concursos.append([linha])
        if nivel_de_importancia == 0:
            sorte += quantidade_de_pontos_de_sorte_do_concurso
            L_pontos_de_sorte.remove(quantidade_de_pontos_de_sorte_do_concurso)
            T_importancia_do_concurso.remove(0)
            k_disputas_perdiveis = k_disputas_perdiveis - 1
        i = i + 1
    i = 0
    while i <= k_disputas_perdiveis:
        sorte = sorte - L_pontos_de_sorte.index(min(L_pontos_de_sorte))
        i = i + 1
    for ponto in L_pontos_de_sorte:
        sorte += ponto
    print(sorte)

if __name__ == "__main__":
    calcular_luckBalance()


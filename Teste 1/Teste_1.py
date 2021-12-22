# Criando o var do tipo int(inteiro) "numero" e ja que a função range(alcance) conta por
# numero de indices ele começa do 0 e vai ate o var final -1 pois o 0 e um indice então ja
# que queremos de 1 a 101 presisamos começar pulando o 0 mais lembrese mesmo pulando o 0 ele
# ainda faz parte da conta do range então para chegarmos no 100 presimos passar o fim do loop
# como 100+1 para ignorar o 0.
for numero in range(1, 100+1):
    # Estamos dizendo o seguinte se o valor atual de "numero" no loop quando dividido por 3
    # resulta em 0 pois 3 multiplicado por algum numero gera aquele numero exemplo 3 * 33 = 99
    # então isso significa que o resto/mod de 99 por 3 e 0 pois 3 multiplicado
    # pois algo gera 99
    # de maneira exata
    if numero % 3 == 0:
        #Imprime/Mostra no terminal Fizz
        print("Fizz")
    # Estamos dizendo o seguinte se o valor atual de "numero" no loop quando dividido por 5
    # resulta em 0 pois 5 multiplicado por algum numero gera aquele numero exemplo 5 * 20 = 100
    # então isso significa que o resto/mod de 100 por 5 e 0 pois 5 multiplicado
    # pois algo gera 100
    # de maneira exata
    elif numero % 5 == 0:
        # Imprime/Mostra no terminal Buzz
        print("Buzz")
    elif numero % 3 and numero % 5:
        print("FizzBuzz")
    else:
        # Imprimi/Mostra no terminal de 1 a 100
        print(numero)
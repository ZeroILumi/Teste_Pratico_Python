* #### Lena está se preparando para uma importante competição de codificação que é precedida por uma série de competições preliminares sequenciais. Inicialmente, seu saldo de sorte é 0. Ela acredita em "poupar sorte" e quer verificar sua teoria. Cada concurso é descrito por dois inteiros, L [i] e T [i]:
	* #### L [i] é a quantidade de sorte associada a um concurso. Se Lena ganhar o concurso, seu saldo de sorte diminuirá em L [i]; se ela perder, seu saldo de sorte aumentará em L [i].
	* #### T [i] denota a classificação de importância do concurso. É igual a 1 se o concurso for importante e é igual a 0 se não for importante.
	
* #### Se Lena perder não mais do que k disputas importantes, qual é a quantidade máxima de sorte que ela pode ter depois de competir em todas as disputas preliminares? Este valor pode ser negativo.

* #### Exemplo

* #### k = 2

* #### L = [5, 1, 4]

* #### T = [1, 2, 0]

* #### Contexto		 L[i] 		T[i]                                 

* #### 1		                 5		    1		

* #### 2		                 1		    1

* #### 3		                 4		    0

* #### Se Lena perder todas as disputas, ela será 5 + 1 + 4 = 10. Como ela pode perder 2 disputas importantes e há apenas 2 disputas importantes, ela pode perder todas as disputas para maximizar sua sorte em 10.

* #### Se k = 1, ela deve vencer pelo menos 1 das 2 competições importantes. Ela escolheria ganhar o concurso importante de menor valor no valor de 1. Sua sorte final será 5 + 4 - 1 = 8.

* #### Descrição da função

* #### Conclua a função luckBalance no editor abaixo.

* #### luckBalance tem o (s) seguinte (s) parâmetro (s):
	* #### int k: o número de competições importantes que Lena pode perder
	* #### int concursos [n] [2]: um array 2D de inteiros onde cada concurso [i] contém dois inteiros que representam o equilíbrio da sorte e a importância do i<sup>th</sup> concurso.
	
* #### Retornos
	* #### int sorte : o equilíbrio máximo de sorte alcançável
	
* #### Formato de entrada dos dados

* #### A primeira linha contém dois inteiros separados por espaço n e k, o número de disputas preliminares e o número máximo de disputas importantes que Lena pode perder.

* #### Cada uma das próximas n linhas contém dois inteiros separados por espaço, L [i] e T [i], o saldo da sorte do concurso e sua classificação de importância.

* #### Restrições
	* #### 1 < n < 100
	
	* ####  0 < k < N
	
	* ####  1 < L[i] < 10<sup>4</sup>
	
	* ####  T[i] = {0, 1}

* #### Exemplo de entrada de dados

* #### STDIN/Input                    		   Function

* #### -------------------	---------------------------------------------------------------------

* #### 6	       3	        n = 6, k = 3

* #### 5	       1	        concursos = [[5,1], [2,1], [1,1], [8,1], [10, 0] [5, 0]]

* #### 2	       1

* #### 1	       1

* #### 8	       1

* #### 10	       0

* #### 5	       0

* #### Exemplo de saida de dados

* #### 29

* #### Explicação

* #### Existem n = 6 concursos. Destas competições, 4 são importantes e ela não pode perder mais do que k = 3 delas. Lena maximiza sua sorte se ela ganhar o  3<sup>rd</sup> importante concurso (onde L [i] = 1) e perder todos os outros cinco concursos para um saldo de sorte total de 5 + 2 + 8 + 10 + 5 - 1 = 29.
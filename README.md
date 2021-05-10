# Rede-Neural-Artificial
Trabalho envolve o desenvolvimento de um rede neural artificial (RNA) para a disciplina EMB5617 - Sistemas Inteligentes ministrada na UFSC Joinville.

# Enunciado do trabalho:
Para o trabalho utilize os dados disponíveis no arquivo "Dados para o trabalho sobre RNA". O arquivo consiste de uma planilha eletrônica com dados de entrada (uma sequência numérica) e saída (resultado de funções). O comportamento da entrada e saída é mostrado em um gráfico disponível no arquivo.  O objetivo do trabalho consiste em treinar uma rede neural artificial (RNA) para estimar os valores de "Saída" a partir dos valores de "Entrada".

Cada equipe (dupla ou individual) pode utilizar um framework escolhido (na disciplina disponibilizei material do Pybrain).

Para o trabalho é necessário:

Proponha pelo menos 3 topografias de rede e indique qual é considerada a melhor.
Utilize 80-90% dos dados para treinamento e 20-10% dos dados para avaliação da rede.
Quando o usuário digitar um valor dentro do intervalo de treinamento, mostre o valor estimado pela RNA.
Faça um vídeo de até 10 minutos para apresentar o trabalho.

# Equipe:
- Danilo Jose da Silva
- Acir Marconato Junior

# Bibliotecas Necessarias:
Instalar as seguintes bibliotecas urilizando o pip:
- pip install openpyxl
- pip install xlrd
- pip install pandas
- pip install pybrain

# Treinamento:

No treinamento da RNA temos 3 variaveis que precisam ser achados seus valores "ideais" para que tenhamos um equilibrio entre tempo de simulação x processamento. As quais são:
1. Número de Épocas;
2. Número de neurônios na camada oculta;
3. Número de camadas oculta.

Para investigar em como chegar em valores "ideais" adotamos valores iniciais para as duas variáveis sendo:<br>
- Número de neurônios na camada oculta = 100
- Número de camadas oculta = 1

Para o Número de Épocas foi feito um estudo com relacao ao erro, esse erro serve como base para saber até quanto é necessario para se treinar a RNA sem a necessidade de se treinar pouco ou muito.

#### Estudo de Erro
Foi realizado um estudo de erro e como ele varia de acordo com o numero de épocas.

###### Grafico de Erro: ÉPOCAS x %:
![Grafico 01](https://i.postimg.cc/cCPxc2cm/Erro01.png "Grafico 01")
![Grafico 02](https://i.postimg.cc/kMHg9Rdb/Erro02.png "Grafico 02")
![Grafico 03](https://i.postimg.cc/bN2NvYzF/Erro03.png "Grafico 03")
![Grafico 04](https://i.postimg.cc/RZ5CJrhC/Erro04.png "Grafico 04")

De acordo com o gráfico acima, para os dados entregues um numero de 100 épocas já são suficientes para se ter um erro que tenda a um comportamento assintótico, ou seja, tendendo a um valor tendendo a zero com pouca oscilação de valor.

#### Topologias:
Nesse teste o objetivo foi descobrir três topologias que atendesse ao desafio proposto, as topologias depois de varios testes obtidos foram:<br>

##### Topologia 01: Épocas = 10.000; Camadas = 10 e Número de neurônios = 100
Nessa topologia estudamos o caso de ter varias camadas com a mesma quantidade de neurônios e um número grande de épocas para ver justamente se haveria uma influencia na RNA.<br>
![Num. Camadas = 1](https://i.postimg.cc/659GmfJx/E1x1-C10x100-S1x1-EP10000.png "Num. Camadas = 1")<br>
Foi observando diminuindo o número de épocas que tem um impacto significativo no aprendizado da RNA mas não é algo que tenha um alto impacto.

##### Topologia 02: Épocas = 2.000; Camadas e Neurônios com a configuração = [100, 500, 1000, 500, 100]
Nesta topologia o objetivo foi realizar um estudo da interferência de criar camadas com diferentes numeros de neurônios. No segundo estudo diminuimos o número de épocas visto que um número muito grande seria desnecessário e só comprometeria o tempo de treinamento.<br>
![Num. Camadas = 1](https://i.postimg.cc/BZ5KpwzC/E1x1-C1x100-C1x500-C1x1000-C1x500-C1x100-S1x1-EP2000.png "Num. Camadas = 1")<br>
É observado que não houve perda no aprendizado diminuindo o numero de épocas e que variando o numero de camadas com diferentes numeros de neurônios foi obtido um resultado mais positivo que em comparação com o primeiro estudo.

##### Topologia 03: Épocas = 100; Camadas e Neurônios com a configuração = [100, 150, 200, 300, 400, 500, 400, 300, 200, 100]
Nesse ultimo estudo é colocado em xeque se o numero mínimo de épocas para treino da RNA realmente é suficiente, para tanto é aumentado o numero de camadas e variado o numero de neurônios.<br> 
![Num. Camadas = 1](https://i.postimg.cc/7hNJLfzR/E1x1-C1x100-C1x150-C1x200-C1x300-C1x400-C1x500-C1x400-C1x300-C1x200-C1x100-S1x1-EP100.png "Num. Camadas = 1")<br>
Conforme se observa usando o numero mínimo de épocas e variando o numero de neurônios e camadas se obteve um resultado positivo em comparação aos demais estudos. 

### Conclusões
No estudo das 3 Topologias se pode observar que com base no gráfico de erro do treinamento da RNA podemos tirar um numero mínimo de epocas que podemos submeter a RNA para aprendizado. No entanto ao utilizar esse numero minimo de épocas para treino é necessário se atentar ao numero de camadas e neurônios pois eles tem forte influencia no aprendizado.<br>
Nos estudos se pode observar que quanto maior e variada a sua topologia em relação ao numero de camadas e neurônios temos resultados no aprendizado mais satisfatórios. Nos nossos testes dispunhamos de um computador com baixo processamento e portanto limitou as simulações.
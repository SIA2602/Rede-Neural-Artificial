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

Para investigar em como chegar em valores "ideais" adotamos valores iniciais para as três variáveis sendo:<br>
- Número de Épocas = 10000
- Número de neurônios na camada oculta = 100
- Número de camadas oculta = 1

###### Variando Número de Camadas:
Nesse teste o objetivo foi **variar o número de camadas** e os demais estarem fixados afim de ver o seu impacto frente as outras variaveis.
![Num. Camadas = 1](https://i.postimg.cc/L4nvQVjy/E1x1-C1x100-S1x1-EP10000.png "Num. Camadas = 1")

![Num. Camadas = 2](https://i.postimg.cc/XJhK6T9s/E1x1-C2x100-S1x1-EP10000.png "Num. Camadas = 2")

![Num. Camadas = 3](https://i.postimg.cc/BbHF9tSv/E1x1-C3x100-S1x1-EP10000.png "Num. Camadas = 3")

![Num. Camadas = 4](https://i.postimg.cc/QMCWNf8w/E1x1-C4x100-S1x1-EP10000.png "Num. Camadas = 4")

![Num. Camadas = 5](https://i.postimg.cc/L5KqTRtF/E1x1-C5x100-S1x1-EP10000.png "Num. Camadas = 5")

###### Variando Número de Neurônios:
Como no teste anterior foi verificado que uma configuração de 5 camadas tem um impacto significativo na resposta de saída, **então fixamos o número de camadas em 5** e também **fixamos a número de épocas** e **variamos apenas os numeros de neurônios**.

![Num. Neurônios = 100](https://i.postimg.cc/L5KqTRtF/E1x1-C5x100-S1x1-EP10000.png "Num. Camadas = 5")
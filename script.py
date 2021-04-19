import pandas as pd #Usado para ler os dados da planilha Excel

from pybrain.tools.shortcuts import buildNetwork #usada para criar a rede neural
from pybrain.datasets import SupervisedDataSet #usado para ler os dados para a rede neural
from pybrain.supervised.trainers import BackpropTrainer #usado para treinar a rede neural

#Carregando dados da planilha excel
df = pd.read_excel("assets/dadoLeitura/dadosTrabalhoRNA.xlsx",  engine='openpyxl', dtype={'Entrada':int, 'Saída':int})

#Setando dados
RNAdata = SupervisedDataSet(1, 1) #entra 1 dado e sai 1 dado
for i in range(len(df['Entrada'])):
    RNAdata.addSample(float(df['Entrada'][i]/max(df['Entrada'])), float(df['Saída'][i]/max(df['Saída']))) #normalizando dados de 0 a 1

#Inicializando rede Neural
RNA = buildNetwork(1, 5, 5, 1, bias=True) #buildNetwork(num Neuronios na entrada, num neuronio na camada oculta, num neuronio na saida)

#Treinamento
trainer = BackpropTrainer(RNA, RNAdata)
for i in range(50): #treinando a rede neural com numero de epocas
    trainer.train()

#Simulando saida de dados     
saida = RNA.activate([0.40])*max(df['Saída']) #convetendo valor normalizado para mesma escala dos dados de saida
print(saida)
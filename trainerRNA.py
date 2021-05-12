import pandas as pd #Usado para ler os dados da planilha Excel

from pybrain.tools.shortcuts import buildNetwork #usada para criar a rede neural
from pybrain.datasets import SupervisedDataSet #usado para ler os dados para a rede neural
from pybrain.supervised.trainers import BackpropTrainer #usado para treinar a rede neural
from pybrain.tools.customxml import NetworkWriter #usado para salvar RNA treinada

#Para Impressao dos dados
import matplotlib
import matplotlib.pyplot as plt

#Para geracao de numeros aleatorios
from random import random
from random import sample

#Carregando dados da planilha excel
df = pd.read_excel("assets/dadoLeitura/dadosTrabalhoRNA.xlsx",  engine='openpyxl', dtype={'Entrada':int, 'Saída':int})

#Selecionando os 20% dos dados para testar a RNA
listDadosEntrada = sample(list(df['Entrada']), int(len(df['Entrada'])*0.2)) #armazena os 20% dos dados das listas de entrada
listDadosSaida = []
for j in range(len(listDadosEntrada)):    
    for i in range(len(df['Entrada'])):    
        if(df['Entrada'][i] == listDadosEntrada[j]):
            listDadosSaida.append(df['Saída'][i])

#Setando dados
RNAdata = SupervisedDataSet(1, 1) #entra 1 dado e sai 1 dado
for i in range(len(df['Entrada'])):
    RNAdata.addSample(float(df['Entrada'][i]/max(df['Entrada'])), float(df['Saída'][i]/max(df['Saída']))) #normalizando dados de 0 a 1

#Inicializando rede Neural
RNA = buildNetwork(1, 100, 500, 1000, 500, 100, 1, bias=True) #buildNetwork(num Neuronios na entrada, num neuronio na camada oculta, num neuronio na saida)
#print(RNA['in'])
#print(RNA['hidden0'])
#print(RNA['out'])
#print(RNA['bias'])

#Treinamento
trainer = BackpropTrainer(RNA, RNAdata)
x_err = [] #lista que vai armazenar o range de epocas
y_err = [] #lista que vai armazenar o erro em %
for i in range(2000): #treinando a rede neural com numero de epocas
    y_err.append(trainer.train()*100)
    x_err.append(i+1)

NetworkWriter.writeToFile(RNA, 'assets/treinoRNA/topologia02.xml') #Salvando RNA Treinada

#Simulando saida de dados     
#saida = RNA.activate([0.40])*max(df['Saída']) #convetendo valor normalizado para mesma escala dos dados de saida
#print(saida)

#Criando variavel de entrada e saida para plotar o grafico com a rede neural treinada
entrada = sorted([random() for x in range(100)])
saida = []
for i in range(len(entrada)):
    saida.append(RNA.activate([entrada[i]])*max(df['Saída']))    
    entrada[i] = entrada[i]*max(df['Entrada'])

listDadosSaidaRNA = []
for i in range(len(listDadosEntrada)):
    listDadosSaidaRNA.append(RNA.activate([listDadosEntrada[i]/max(df['Entrada'])])*max(df['Saída']))

#Plotando Graficos
fig, ax = plt.subplots()
ax.plot(df['Entrada'], df['Saída'])
ax.plot(entrada, saida, '-')
ax.plot(listDadosEntrada, listDadosSaida, 'o')
ax.plot(listDadosEntrada, listDadosSaidaRNA, 'o')
ax.grid()

fig, ax1 = plt.subplots()
ax1.plot(x_err, y_err, '-')
ax1.grid()

plt.show()
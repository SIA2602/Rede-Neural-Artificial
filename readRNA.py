import pandas as pd #Usado para ler os dados da planilha Excel

from pybrain.tools.customxml import NetworkReader #usado para ler a RNA treinada

#Para Impressao dos dados
import matplotlib.pyplot as plt

#Carregando dados da planilha excel
df = pd.read_excel("assets/dadoLeitura/dadosTrabalhoRNA.xlsx",  engine='openpyxl', dtype={'Entrada':int, 'Saída':int})

RNA = NetworkReader.readFrom('name.xml') #lendo RNA Treinada

#Esperando entrada de 0-1 para visualizar no grafico
while(True):
    entrada = float(input("Digite o valor de entrada entre 0-1: "))    
    saida = RNA.activate([entrada])*max(df['Saída'])
    entrada = entrada*max(df['Entrada'])
    print(entrada, saida)
    #Plotando Graficos
    fig, ax = plt.subplots()
    ax.plot(df['Entrada'], df['Saída'])
    ax.plot(entrada, saida, 'o')    
    ax.grid()
    plt.show()
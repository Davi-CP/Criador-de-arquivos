import os

#Função que coleta os dados dos sensores(substituir aqui)
def coleta_sensores():
    #Simulação de leitura de dados de sensores
    return "Struct1: \nSensor1: 25.5 \nSensor2:23.0 \nSensor3: 150,\nStruct2: Sensor1: 25.5 \nSensor2:23.0 \nSensor3: 150, \nStruct3: Sensor1: 25.5 \nSensor2:23.0 \nSensor3: 150 "

dados_sensor = coleta_sensores()
#obtém diretorio
diretorio_atual = os.getcwd()
#se um arquivo com esse nome ja existe, sobrescreve
nome_arquivo = "dados_sensores.txt"

caminho_completo = os.path.join(diretorio_atual, nome_arquivo)
print(f"O arquivo será criado em : {caminho_completo} ")

with open(nome_arquivo, 'a') as arquivo:
    arquivo.write(dados_sensor + '\n')
import os

file = open('emd.csv', 'r')
next(file)

data = []
modalidade = []
escalao = [0] * 20
federados = 0
nratletas = 0

def calc_posicao(idade):
    return idade // 5


for line in file:
    nratletas += 1
    dados = line.split(',')
    if dados[11] == "true":
        federados += 1
    pos = calc_posicao(int(dados[5]))
    if dados[8] not in modalidade:
        modalidade.append(dados[8])
    escalao[pos] += 1
    data.append(line)


def aptidao_atletas():
    aptos = 0
    if federados != 0:
        aptos = (federados / nratletas) * 100
    inaptos = 100 - aptos

    return aptos, inaptos


output = open("outputs.txt", "w")


def gerar_output():
    
    output.write("Modalidades: \n")
    modalidade.sort()
    for linha in modalidade:
        output.write(f' - {linha}\n')
        
    output.write("\n")
    
    perc = aptidao_atletas()
    output.write(f'Atletas Aptos = {perc[0]:.2f}%\n')
    output.write(f'Atletas Inaptos = {perc[1]:.2f}%\n\n')

    output.write("Escalões: \n")
    idade = 0
    for esc in escalao:
        if esc != 0:
            output.write(f'{idade}-{idade + 4} = {(esc / nratletas) * 100:.2f}%\n')
        idade += 5
    


gerar_output()
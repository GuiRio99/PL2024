import ply.lex as lex
import json
import sys

tokens = (
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'ADICIONAR',
    'SAIR'
)

def t_LISTAR(t):
    r'(?i)LISTAR'
    return t

def t_MOEDA(t):
    r'(?i)MOEDA[ ]+([1c|2c|5c|10c|20c|50c|1e|2e],?)+'
    return t

def t_SELECIONAR(t):
    r'(?i)SELECIONAR[ ]\d+'
    return t

def t_ADICIONAR(t):
    r'(?i)ADICIONAR[ ]\w+[ ]\d+[ ]?(\d+e\d+c|\d+c|\d+e)?'

    return t

def t_SAIR(t):
    r'(?i)SAIR'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print("Carácter Inválido: '%s'" % t.value[0])
    t.lexer.skip(1)

def vending_machine(data):
    lexer = lex.lex()
    saldo = 0

    for line in sys.stdin:
        lexer.input(line)
        for token in lexer:
            if(token.type == "LISTAR"):
                print('     Número       |            Nome                           |       Stock        |   Preço    ')
                for id, p in data.items():
                    print(f"        {id: <5}     |        {p['nome']: <30}      |        {p['stock']: <5}       |       {p['preço']: <5}")

            elif(token.type == "MOEDA"):
                moedas = token.value.split()[1].split(",")
                for m in moedas:
                    if m.endswith('e'):
                        saldo += int(coin[:-1]) * 100
                    elif m.endswith('c'):
                        saldo += int(coin[:-1])

                print(f"maq: Saldo: {saldo}€")

            elif token.type == "SELECIONAR":
                id = int(token.value.split()[1])

                if data[id]['stock'] == 0:
                    print("Produto esgotado!")
                if id not in data:
                    print("Produto não existe!")

                p = data[id]['preço']

                if 'e' in p:
                    eu, cnt = p.split('e')
                    centimos = int(cnt[:-1]) if cnt else 0
                    preco = int(eu) * 100 + centimos
                    
                else:
                    preco = int(p[:-1])
                    
                if saldo >= preco:
                    saldo -= preco
                    print("Produto comprado com sucesoo!")
                    print(f"Troco: {saldo}€")
                    data[id]['stock'] -= 1
                else:
                    print("Saldo insuficiente!")

            elif token.type == "ADICIONAR":
                nome = token.value.split()[1]
                stock = int(token.value.split()[2])
                existe = False
                for id, p in data.items():
                    if p['nome'] == nome:
                        p['stock'] += stock
                        existe = True
                        break
                if not existe:
                    id = len(data) + 1
                    data[id] = {'nome': nome, 'stock': stock, 'preço': token.value.split()[3]}
                print(f"O produto {nome} foi adicionado!")

            elif token.type == "SAIR":
                
                print(f"{saldo}€")
                troco = []
                for coin in [200, 100, 50, 20, 10, 5, 2, 1]:
                    while saldo >= coin:
                        if coin >= 100:
                            troco.append(f"{coin//100}e")
                        else:
                            troco.append(f"{coin}c")
                        saldo -= coin
                print(" ".join(troco))




def main(argv):
    
    if(len(argv) < 2):
        return 1
    input_file = argv[1]
    
    with open(input_file, 'r') as file:
        data = json.load(file)

    produtos = data['vending_machine']
    vendingMachine = {p["id"]: p for p in produtos}
    print("Máquina de venda automática!!!")
    vending_machine(vendingMachine)
    
if __name__ == "__main__":
    main(sys.argv)
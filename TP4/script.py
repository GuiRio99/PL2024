from ply import lex, yacc
import sys


comandos = {
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE',
    'in' : 'IN',
    'and': 'AND',
    'or': 'OR',
    'create' : 'CREATE',
    'drop' : 'DROP',
    'show' : 'SHOW',
    'use' : 'USE',
    'alter' : 'ALTER',
    'grant' : 'GRANT',
    'group by' : 'GROUP_BY' 
}

tokens = [
    "COMMAND",
    "OPERATOR",
    "DELIMITER",
    "ATTRIBUTE",
    "NUMBER",
    "ENDCMD"
] + list(comandos.values())


t_DELIMITER = r","
t_NUMBER = r'\d+'
t_ENDCMD = r";"

    #r"\b[a-zA-Z]+\b"
def t_COMMAND(token):
    r"\b\w+(\s+(?i:by|join))?\b"
    val = token.value.lower()
    if val in comandos:
        token.type = comandos[val]
    else:
        token.type = "ATTRIBUTE"
    return token

def t_OPERATOR(token):
    r"\+|-|\*|>=|<=|>|<|="
    return token


def t_newline(token):
    r'\n+'
    token.lexer.lineno += len(token.value)

t_ignore = ' \t'

def t_error(token):
    print("Caracter inválido --> '%s'" % token.value[0])
    token.lexer.skip(1)

lexer = lex.lex()

def main (args):
    if len(args) < 2:
        return
    with open(args[1], 'r') as file:
        data = file.read()
        lexer = lex.lex() 
        lexer.input(data)
        for t in lexer:
            print(t) 

if __name__ == '__main__':
    main(args=sys.argv)
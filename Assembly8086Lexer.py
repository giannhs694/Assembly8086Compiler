import os

import ply.lex as lex

symbolTable = {}

registers = {
    'AX': 'AX',
    'BX': 'BX',
    'CX': 'CX',
    'DX': 'DX',
    'AH': 'AH',
    'AL': 'AL',
    'BH': 'BH',
    'BL': 'BL',
    'CH': 'CH',
    'CL': 'CL',
    'DH': 'DH',
    'DL': 'DL',
    'DI': 'DI',
    'SI': 'SI',
    'BP': 'BP',
    'SP': 'SP',
    'DS': 'DS',
    'ES': 'ES',
    'SS': 'SS',
    'CS': 'CS'
}

reserved = {
               'MOV': 'MOV',
               'ADD': 'ADD',
               'SEGMENT': 'SEGMENT_START',
               'INT': 'INT',
               'ENDS': 'SEGMENT_ENDS',
               'END': 'END_LABEL',
               'DB': 'DB',
               'LOOPNE': 'LOOPNE',
               'LOOP': 'LOOP',
               'LEA': 'LEA',
               'SHL': 'SHL',
               'CMP': 'CMP',
               'SHR': 'SHR',
               'INC': 'INC',
               'DUP': 'DUP',
               'RET': 'RET'
           } | registers

tokens = [
             'SUB',
             'SEPARATOR',
             'DECIMALNUMBER',
             'BINARYNUMBER',
             'OCTALNUMBER',
             'HEXNUMBER',
             'ID',
             'PLUS',
             'MINUS',
             'COLON',
             'ASSUME',
             'LBRACKET',
             'RBRACKET',
             'AND',
             'DQUOTE',
             'SQUOTE',
             'STRING',
             'LPAREN',
             'RPAREN'
         ] + list(reserved.values())

t_DQUOTE = r'"'
t_SQUOTE = r'\''
t_SEPARATOR = r','
t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_COLON = r':'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_HEXNUMBER = r'(0[xXhH][ABCDEFabcdef0-9]+)|([ABCDEFabcdef0-9]+[hH])'
t_DECIMALNUMBER = r'(0[dD]\d+)|(\d+[dD]?)'
t_OCTALNUMBER = r'(0[qQoO][0-7]+)|([0-7]+[qQoO])'
t_BINARYNUMBER = r'([01]+[bByY])|(0[bByY][01]+)'


def t_RET(t):
    r'(?i)RET'
    return t


def t_DUP(t):
    r'(?i)DUP'
    return


def t_STRING(t):
    r'(".+")|(\'.+\')'
    return t


def t_ADD(t):
    r'(?i)ADD'
    return t


def t_SUB(t):
    r'(?i)SUB'
    return t


def t_SHL(t):
    r'(?i)SHL'
    return t


def t_CMP(t):
    r'(?i)CMP'
    return t


def t_INC(t):
    r'(?i)INC'
    return t


def t_LEA(t):
    r'(?i)LEA'
    return t


def t_INT(t):
    r'(?i)INT'
    return t


def t_MOV(t):
    r'(?i)MOV'
    return t


def t_LOOPNE(t):
    r'(?i)LOOPNE'
    return t


def t_LOOP(t):
    r'(?i)LOOP'
    return t


def t_ASSUME(t):
    r'(?i)ASSUME'
    return t


def t_ignore_TITLE(t):
    r'(?i)TITLE.*'


def t_COMMENT(t):
    r';.*'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


fileName = input("Enter filepath:")
with open(fileName, 'r') as f:
    data = f.read()

lexer = lex.lex()
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)

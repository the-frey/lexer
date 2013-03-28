import ply.lex as lex
  
tokens = (
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        'ELSE',         # else
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        'FALSE',        # false
        'FUNCTION',     # function
        'GE',           # >=
        'GT',           # >
        'IDENTIFIER',   #### 
        'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
        'NUMBER',       #### 
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
        'STRING',       #### 
        'TIMES',        # *
        'TRUE',         # true
        'VAR',          # var
)

states = (
    ('singlelinecomment','exclusive'),
    ('delimitedcomment','exclusive'),
)

t_ignore = ' \t\v\r' # whitespace 

def t_delimitedcomment(token):
    r'\/\*'
    token.lexer.begin('delimitedcomment') #begin this state

def t_delimitedcomment_end(token):
    r'\*\/'
    token.lexer.lineno += token.value.count('\n') #add to whatever the current line number is
    token.lexer.begin('INITIAL') #return to initial (normal) operation

def t_delimitedcomment_error(token):
    token.lexer.skip(1)

def t_singlelinecomment(token):
    r'\/\/'
    token.lexer.begin('singlelinecomment')

def t_singlelinecomment_end(token):
    r'\n'
    token.lexer.begin('INITIAL')

def t_singlelinecomment_error(token):
    token.lexer.skip(1)

def t_newline(token):
        r'\n'
        token.lexer.lineno += 1

def t_error(token):
        print "JavaScript Lexer: Illegal character " + token.value[0]
        token.lexer.skip(1)

def t_NUMBER(token):
    r'-?[0-9]+[.0-9+]*'
    token.value = float(token.value)
    return token

def t_ANDAND(token):
    r'&&'
    return token

def t_COMMA(token):
    r'\,'
    return token

def t_DIVIDE(token):
    r'\/'
    return token

def t_ELSE(token):
    r'else'
    return token

def t_EQUALEQUAL(token):
    r'=='
    return token

def t_EQUAL(token):
    r'='
    return token

def t_FALSE(token):
    r'false'
    return token

def t_FUNCTION(token):
    r'function'
    return token

def t_GE(token):
    r'>='
    return token

def t_GT(token):
    r'>'
    return token

def t_IF(token):
    r'if'
    return token

def t_LBRACE(token):
    r'\{'
    return token

def t_LE(token):
    r'<='
    return token

def t_LPAREN(token):
    r'\('
    return token

def t_LT(token):
    r'<'
    return token

def t_MINUS(token):
    r'\-'
    return token

def t_NOT(token):
    r'\!'
    return token

def t_OROR(token):
    r'\|\|'
    return token

def t_PLUS(token):
    r'\+'
    return token

def t_RBRACE(token):
    r'\}'
    return token

def t_RETURN(token):
    r'return'
    return token

def t_RPAREN(token):
    r'\)'
    return token

def t_SEMICOLON(token):
    r';'
    return token

def t_TIMES(token):
    r'\*'
    return token

def t_TRUE(token):
    r'true'
    return token

def t_VAR(token):
    r'var'
    return token

def t_IDENTIFIER(token):
    r'[a-zA-z]+'
    return token

def t_STRING(token):
    r'"[a-zA-z \\"]*"'
    token.value = token.value[1:-1]
    return token

#three test cases

lexer = lex.lex() 

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ] 
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type]
  return result

input1 = """ - !  && () * , / ; { || } + < <= = == > >= else false function
if return true var """

output1 = ['MINUS', 'NOT', 'ANDAND', 'LPAREN', 'RPAREN', 'TIMES', 'COMMA',
'DIVIDE', 'SEMICOLON', 'LBRACE', 'OROR', 'RBRACE', 'PLUS', 'LT', 'LE',
'EQUAL', 'EQUALEQUAL', 'GT', 'GE', 'ELSE', 'FALSE', 'FUNCTION', 'IF',
'RETURN', 'TRUE', 'VAR']

print test_lexer(input1) == output1

input2 = """
if // else mystery  
=/*=*/= 
true /* false 
*/ return"""

output2 = ['IF', 'EQUAL', 'EQUAL', 'TRUE', 'RETURN']

print test_lexer(input2) == output2

input3 = 'some_identifier -12.34 "a \\"escape\\" b"'

output3 = ['IDENTIFIER', 'NUMBER', 'STRING']

print test_lexer(input3) == output3
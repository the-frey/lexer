import ply.lex as lex
import re

tokens = (
	'LANGLE', # <
	'LANGLESLASH', # </
	'RANGLE', # >
	'EQUAL', # =
	'STRING', # "hello"
	'WORD', # Welcome!
	)

states = (
	('htmlcomment','exclusive'),
)

t_ignore = ' ' #shortcut for whitespace 

def t_htmlcomment(token):
	r'<!-{2}'
	token.lexer.begin('htmlcomment') #begin this state

def t_htmlcomment_end(token):
	r'-{2}>'
	token.lexer.lineno += token.value.count('\n') #add to whatever the current line number is
	token.lexer.begin('INITIAL') #return to initial (normal) operation

def t_htmlcomment_error(token):
	token.lexer.skip(1) #while in html comment, skip all tokens not defined that will cause an error

#if we wanted to display the comment or collect it, we could use something like r'<!-{2}.+-{2}>' 
#then trim it with token.value = token.value[3:-3]

#give us an indication of line number
def t_newline(token):
	r'\n'
	token.lexer.lineno += 1
	pass

#LANGLESLASH takes priority so that closing tags are not misinterpreted
def t_LANGLESLASH(token):
	r'</'
	return token

def t_LANGLE(token):
	r'<'
	return token

def t_RANGLE(token):
	r'>'
	return token

def t_EQUAL(token):
	r'='
	return token

def t_STRING(token):
	r'"[^"]*"'
	token.value = token.value[1:-1]
	return token

def t_WORD(token):
	r'[^ <>\n]+'
	return token

webpage = """"This" is 
<!-- my comment -->
<b>my</b> webpage!
"""

htmllexer = lex.lex()
htmllexer.input(webpage)
while True:
	tok = htmllexer.token() #returns next token available
	if not tok: break #break when there are no more tokens
	print tok #otherwise print the token


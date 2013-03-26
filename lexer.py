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

t_ignore = ' ' #shortcut for whitespace

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
	r'[^ <>]+'
	return token

webpage = "This is <b>my</b> webpage!"

htmllexer = lex.lex()
htmllexer.input(webpage)
while True:
	tok = htmllexer.token() #returns next token available
	if not tok: break #break when there are no more tokens
	print tok #otherwise print the token


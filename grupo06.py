import sys
import ply.lex as lex

#Definicion de Plabras reservadas 
Palabras_Reservadas = {
'SELECT' : 'SELECT',
'DISTINCT' : 'DISTINCT',
'FROM' : 'FROM',
'WHERE': 'WHERE',
'JOIN': 'JOIN',
'INNER': 'INNER',
'LEFT': 'LEFT',	
'AS': 'AS',
'FUNCION': 'FUNCION',
'MIN': 'MIN',
'MAX': 'MAX',
'GROUP': 'GROUP',
'ORDER': 'ORDER',
'BY': 'BY',
'ON': 'ON',
'IN': 'IN',
'NOT': 'NOT',
'COUNT': 'COUNT',
'HAVING': 'HAVING',
'ASC': 'ASC',
'DESC': 'DESC',
'AND': 'AND',
'OR' : 'OR'
}

#Definicion de tokens
tokens = ['MENOR', 'MAYOR', 'IGUAL', 'MAYOR_IGUAL', 'MENOR_IGUAL', 'DIFERENTE', 'R_PARENT', 'L_PARENT','L_CORCH','R_CORCH','PUNTO', 'COMA', 'COMILLA', 'ID', 'NUMBER'] + list(Palabras_Reservadas.values())

#Definicion de expresiones regulares simples
t_MENOR = r'\<'
t_MAYOR = r'\>'
t_IGUAL= r'\='
t_MAYOR_IGUAL= r'\>='
t_MENOR_IGUAL= r'\<='
t_DIFERENTE= r'\<>'
t_R_PARENT= r'\)'
t_L_PARENT= r'\('
t_L_CORCH= r'\['
t_R_CORCH= r'\]'
t_PUNTO= r'\.'
t_COMA = r'\,'
t_COMILLA = r'\''

#Regla de expresión regular con código de acción
def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = Palabras_Reservadas.get(t.value,'ID')   # Busca palabras reservadas 
     return t


def t_NUMBER(t):
     r'\d+'
     t.value = int(t.value)
     return t

#Funcion para ignorar los saltos de linea
def t_newline (t): 
     r'\ n+' 
     t.lexer.lineno += len (t.value)
      

#Regla de manejo de errores
def t_error (t): 
     print ("Carácter no valido '% s'"% t.value [0]) 
     t.lexer.skip (1) 

# Ignora los espacios en blanco     
t_ignore = ' \t'    

# Construye el lexer
lexer = lex.lex ()

cons = "SELECT p.edad FROM personas AS 'p'"
lexer.input(cons)

#Prueba. Devuelve el tipo de token y el valor
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

# Diccionarios para almacenar datos
tablas = {}
columnas = {}

#Funciones por cada NT de la gramatica
def p_Consulta(p):
    'CONSULTA: SELECT_ FROM_ JOIN_ WHERE_ GROUP_ ORDER_' 

def p_SELECT_(p):
    '''SELECT_ : SELECT CAMPO
        |SELECT DISTINCT CAMPO'''

def p_CAMPO(p):
    ''' CAMPO : COL COMA CAMPO
        | COL'''

def p_COL(p): #diccionario
    ''' COL : ID PUNTO ID 
	    | ID PUNTO ID AS COMILLA ID COMILLA
	    | FUNCION AS COMILLA ID COMILLA'''
    

def p_FUNCION (p): #diccionario
    ''' FUNCION : COUNT L_PARENT ID PUNTO ID R_PARENT
	    | COUNT DISTINCT L_PARENT ID PUNTO ID R_PARENT
	    | MIN DISTINCT L_PARENT ID PUNTO ID R_PARENT
	    | MAX DISTINCT L_PARENT ID PUNTO ID R_PARENT '''

def p_FROM_(p):
    ' FROM_ : FROM TABLA' 

def p_TABLA(p):
    ''' TABLA : TAB
	    | TAB COMA TABLA ''' 

def p_TAB(p): #diccionario
    ''' TAB : ID 
	    | ID AS COMILLA ID COMILLA'''

def p_JOIN_(p):
    ''' JOIN_ : INNER JOIN J 
	    | LEFT JOIN J
	    | '''

def p_J(p):
    'J : TAB ON W'

def p_WHERE_(p):
    ''' WHERE_ : WHERE W 
	    | '''

def p_W(p): #diccionario
    ''' W : ID PUNTO ID SIM ID PUNTO ID
	    | ID PUNTO ID SIM VALOR 
	    | ID PUNTO ID SUB 
	    | W AND W 
	    | W OR W ''' 

def p_SIM(p):
    ''' SIM : IGUAL
	    | MAYOR_IGUAL
	    | MENOR_IGUAL
	    | MAYOR
	    | MENOR
	    | DIFERENTE '''

def p_SUB (p):
    ''' SUB : IN L_PARENT CONSULTA R_PARENT
	    | NOT IN L_PARENT CONSULTA R_PARENT '''

def p_VALOR (p): 
    ''' VALOR : COMILLA ID COMILLA 
	    | NUMBER'''

def p_GROUP_ (p):
    ''' GROUP_ : GROUP BY CAMPO_G HAV
	    | ''' 

def p_CAMPO_G (p): #diccionario
    ''' CAMPO_G : ID PUNTO ID 
	    | ID PUNTO ID COMA CAMPO_G '''

def p_HAV(p):
    ''' HAV : HAVING FUNCION SIM VALOR
	    | '''

def p_ORDER_(p): 
    ''' ORDER_ : ORDER BY CAMPO_O
	    | '''

def p_CAMPO_O (p): #diccionario
    ''' CAMPO_O : ID PUNTO ID TIPO_O
	    | ID PUNTO ID TIPO_O COMA CAMPO_O '''

def p_TIPO_O (p):
    ''' TIPO_O : ASC 
	    | DESC '''


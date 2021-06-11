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
     r'\n+' 
     t.lexer.lineno += len (t.value)
      
#Regla de manejo de errores
def t_error (t): 
     print ("Carácter no valido '% s'"% t.value [0]) 
     t.lexer.skip (1) 

# Ignora los espacios en blanco     
t_ignore = ' \t'    

# Construye el lexer
lexer = lex.lex ()

#s = '''SELECT c.first_name,
#               c.last_name
#        FROM customers AS c'''
#lexer.input(s)

#Prueba. Devuelve el tipo de token y el valor
#while True:
#    tok = lexer.token()
#    if not tok:
#        break
#    print(tok)

# Diccionarios para almacenar datos
tablas = {}
columnas = {}

#Funciones por cada NT de la gramatica
def p_Consulta(p):
    '''CONSULTA : SELECT_ FROM_ JOIN_ WHERE_ GROUP_ ORDER_'''

def p_SELECT_(p):
    '''SELECT_ : SELECT CAMPO
        | SELECT DISTINCT CAMPO'''

def p_CAMPO(p):
    ''' CAMPO : COL COMA CAMPO
        | COL'''

def p_COL(p): #diccionario
    ''' COL : ID PUNTO ID 
	    | ID PUNTO ID AS COMILLA ID COMILLA
	    | FUNCION AS COMILLA ID COMILLA'''
    indice = p[1]
    if indice in columnas:
        if len(p) == 4 or len(p) == 7:
            aux = p[3]
            if aux not in columnas[indice]:
                columnas[indice].append(aux)
    elif len(p) == 4 or len(p) == 7:
        columnas[indice] = [p[3]]
    

def p_FUNCION (p): #diccionario
    ''' FUNCION : COUNT L_PARENT ID PUNTO ID R_PARENT
	    | COUNT DISTINCT L_PARENT ID PUNTO ID R_PARENT
	    | MIN L_PARENT ID PUNTO ID R_PARENT
	    | MAX L_PARENT ID PUNTO ID R_PARENT '''
    indice = ''
    if len(p) == 7:
        indice = p[3]
    else:
        indice = p[4]
    if indice in columnas:
        if len(p) == 7:
            aux = p[5]
            if aux not in columnas[indice]:
                columnas[indice].append(aux)
        elif len(p) == 8:
            aux = p[6]
            if aux not in columnas[indice]:
                columnas[indice].append(aux)
    else:
        if len(p) == 7:
            columnas[indice] = [p[5]]
        elif len(p) == 8:
            columnas[indice] = [p[6]]


def p_FROM_(p):
    ''' FROM_ : FROM TABLA''' 

def p_TABLA(p):
    ''' TABLA : TAB
	    | TAB COMA TABLA ''' 

def p_TAB(p): #diccionario
    ''' TAB : ID 
	    | ID AS ID'''
    if len(p) == 2:
        tablas.setdefault(p[1])
    else:
        tablas[p[1]] = [p[3]]      


def p_JOIN_(p):
    ''' JOIN_ : INNER JOIN J 
	    | LEFT JOIN J
	    | '''


def p_J(p):
    '''J : TAB ON W'''


def p_WHERE_(p):
    ''' WHERE_ : WHERE W 
	    | '''


def p_W(p): #diccionario
    ''' W : ID PUNTO ID SIM ID PUNTO ID
	    | ID PUNTO ID SIM VALOR 
	    | ID PUNTO ID SUB 
	    | W AND W 
	    | W OR W ''' 
    if len (p) == 8:
        indice1 = p[1]
        indice2 = p[5]
        if indice1 in columnas:
            aux = p[3]
            if aux not in columnas[indice1]:
                columnas[indice1].append(aux)
        else:
            columnas[indice1] = p[3]
        if indice2 in columnas:
            aux = p[3]
            if aux not in columnas[indice2]:
                columnas[indice2].append(aux)
        else:
            columnas[indice2] = [p[3]]
    elif len(p) == 6 or len(p) == 5:
        indice = p[1]
        if indice in columnas:
            aux = p[3]
            if aux not in columnas[indice]:
                columnas[indice].append(aux)
        else:
            columnas[indice] = [p[3]]


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
    indice = p[1]
    if indice in columnas:
        aux = p[3]
        if aux not in columnas[indice]:
            columnas[indice].append(aux)
    else:
        columnas[indice] = [p[3]]

def p_HAV(p):
    ''' HAV : HAVING FUNCION SIM VALOR
	    | '''

def p_ORDER_(p): 
    ''' ORDER_ : ORDER BY CAMPO_O
	    | '''

def p_CAMPO_O (p): #diccionario
    ''' CAMPO_O : ID PUNTO ID TIPO_O
	    | ID PUNTO ID TIPO_O COMA CAMPO_O '''
    indice = p[1]
    if indice in columnas:
        aux = p[3]
        if aux not in columnas[indice]:
            columnas[indice].append(aux)
    else:
        columnas[indice] = [p[3]]

def p_TIPO_O (p):
    ''' TIPO_O : ASC 
	    | DESC '''

import ply.yacc as yacc

def parse_select_statement(s):
    #Vaciar valores de los diccionarios
    columnas.clear()
    tablas.clear()
    contador= 0
    yacc.yacc()
    yacc.parse(s)
   
    resultado = {}

    for indice_tablas in tablas:
        control=''
        if tablas.get(indice_tablas)!=None:
            control=tablas.get(indice_tablas)
        else:
            control=indice_tablas
        for indice_columnas in columnas:
            if control==indice_columnas:
                resultado[indice_tablas]=sorted(columnas.get(indice_columnas))
                contador+=1
    if len(columnas.keys())>contador:
        raise Exception('Error de cadena inválida.')
    return resultado


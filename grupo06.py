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

#Prueba. Devuelve el tipo de token y el valor
'''
s = 'SELECT c.first_name,
               c.last_name
        FROM customers AS c'
lexer.input(s)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
'''

# Diccionarios para almacenar datos
tablas = {}
columnas = {}

#Funciones por cada NT de la gramatica
def p_Consulta(p):
    '''consulta : select from join where group order'''

def p_select(p):
    '''select : SELECT campo
        | SELECT DISTINCT campo'''

def p_campo(p):
    '''campo : col COMA campo
        | col'''

def p_col(p): #Diccionario columnas
    '''col : ID PUNTO ID AS ID
	    | ID PUNTO ID
	    | funcion AS ID'''
    if len(p) == 4 or len(p) == 6:
        if p[1] in columnas:
            if p[3] not in columnas[p[1]]:
                columnas[p[1]].append (p[3]) #Guardamos las columnas de cada clave (tabla)
        else:
            columnas[p[1]] = [p[3]] #Agregamos la tabla o el alias como clave

def p_funcion(p): #Diccionario columnas
    '''funcion : COUNT L_PARENT ID PUNTO ID R_PARENT
	    | COUNT DISTINCT L_PARENT ID PUNTO ID R_PARENT
	    | MIN L_PARENT ID PUNTO ID R_PARENT
	    | MAX L_PARENT ID PUNTO ID R_PARENT'''

    if len(p) == 7:
        indice = p[3]
    else:
        indice = p[4]
    if indice in columnas:
        #Guardamos columnas de la clave
        if len(p) == 7:
            if p[5] not in columnas[indice]:
                columnas[indice].append(p[5])
        else:
            if p[6] not in columnas[indice]:
                columnas[indice].append(p[6])
    else:
        #Agregamos la tabla o alias como clave
        if len(p) == 7:
            columnas[indice] = [p[5]]
        else:
            columnas[indice] = [p[6]]

def p_from(p):    
    '''from : FROM tabla'''

def p_tabla(p):
    '''tabla : tab
	    | tab COMA tabla'''

def p_tab(p): #Diccionario tablas
    '''tab : ID
        | ID ID
	    | ID AS ID'''
    if len(p) == 2:
        tablas.setdefault(p[1]) # Agrega el nombre de la tabla como clave al diccionario 
    elif len(p) == 3:
        tablas[p[1]] = p[2] # Guarda el alias de la tabla
    else:
        tablas[p[1]] = p[3]

def p_join(p):
    '''join : INNER JOIN j
	    | LEFT JOIN j
	    | '''

def p_j(p):
    '''j : tab ON w'''

def p_where(p):
    '''where : WHERE w 
	    | '''

def p_w(p): #Diccionario columnas
    '''w : ID PUNTO ID sim ID PUNTO ID
	    | ID PUNTO ID sim valor 
	    | ID PUNTO ID sub 
	    | w AND w 
	    | w OR w'''
    if len(p) == 6 or len(p) == 5:
        if p[1] in columnas:
            if p[3] not in columnas[p[1]]:
                columnas[p[1]].append(p[3]) #Guardamos columnas de la clave
        else:
            columnas[p[1]] = [p[3]] #Agregamos la tabla o alias como clave
    elif len(p) == 8:
        if p[1] in columnas:
            if p[3] not in columnas[p[1]]:
                columnas[p[1]].append(p[3]) #Guardamos columnas de la clave
        else:
            columnas[p[1]] = [p[3]] #Agregamos la tabla o alias como clave
        if p[5] in columnas:
            if p[7] not in columnas[p[5]]:
                columnas[p[5]].append(p[7]) #Guardamos columnas de la clave
        else:
            columnas[p[5]] = [p[7]] #Agregamos la tabla o alias como clave

def p_sim(p):
    '''sim : IGUAL
	    | MAYOR_IGUAL
	    | MENOR_IGUAL
	    | MAYOR
	    | MENOR
	    | DIFERENTE'''

def p_sub(p):
    '''sub : IN L_PARENT consulta R_PARENT
	    | NOT IN L_PARENT consulta R_PARENT'''

def p_valor(p):
    '''valor : COMILLA ID COMILLA 
	    | NUMBER'''

def p_group(p): 
    '''group : GROUP BY campo_g hav
	    | '''

def p_campo_g(p): #Diccionario columnas
    '''campo_g : ID PUNTO ID 
	    | ID PUNTO ID COMA campo_g'''
    if p[1] in columnas:
        if p[3] not in columnas[p[1]]:
            columnas[p[1]].append(p[3]) #Guardamos columnas de la clave
    else:
        columnas[p[1]] = [p[3]] #Agregamos la tabla o alias como clave

def p_hav(p):
    '''hav : HAVING funcion sim valor
	    | '''

def p_order(p):
    '''order : ORDER BY campo_o
	    | '''

def p_campo_o(p): #Diccionario columnas
    '''campo_o : ID PUNTO ID tipo_o
	    | ID PUNTO ID tipo_o COMA campo_o'''
    if p[1] in columnas:
        if p[3] not in columnas[p[1]]:
            columnas[p[1]].append(p[3]) #Guardamos columnas de la clave
    else:
        columnas[p[1]] = [p[3]] #Agregamos la tabla o alias como clave

def p_tipo_o(p):
    '''tipo_o : ASC 
	    | DESC'''

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc

#Analizador de prueba
'''
parser = yacc.yacc()

while True:
    try:
        s = input('analizador >')
        columnas.clear()
        tablas.clear()
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)
    items1 = columnas.items()
    items2 = tablas.items()
    for x in items1:
        print(x)
    for y in items2:
        print(y)
'''

def parse_select_statement(s):
    #Vaciar valores de los diccionarios
    columnas.clear()
    tablas.clear()
    contador= 0
    yacc.yacc()
    yacc.parse(s)
   
    resultado = {}

    for indice_tablas in tablas:
        control = ''
        if tablas.get(indice_tablas) != None:
            control = tablas.get(indice_tablas)
        else:
            control = indice_tablas
        for indice_columnas in columnas:
            if control == indice_columnas:
                resultado[indice_tablas] = sorted(columnas.get(indice_columnas))
                contador += 1
    if len(columnas.keys()) > contador:
        raise Exception('Error de cadena inválida.')
    return resultado

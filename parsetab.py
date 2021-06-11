
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS ASC BY COMA COMILLA COUNT DESC DIFERENTE DISTINCT FROM GROUP HAVING ID IGUAL IN INNER JOIN LEFT L_CORCH L_PARENT MAX MAYOR MAYOR_IGUAL MENOR MENOR_IGUAL MIN NOT NUMBER ON OR ORDER PUNTO R_CORCH R_PARENT SELECT WHEREconsulta : select from join where group orderselect : SELECT campo\n        | SELECT DISTINCT campocampo : col COMA campo\n        | colcol : ID PUNTO ID AS ID\n\t    | ID PUNTO ID\n\t    | funcion AS IDfuncion : COUNT L_PARENT ID PUNTO ID R_PARENT\n\t    | COUNT DISTINCT L_PARENT ID PUNTO ID R_PARENT\n\t    | MIN L_PARENT ID PUNTO ID R_PARENT\n\t    | MAX L_PARENT ID PUNTO ID R_PARENTfrom : FROM tablatabla : tab\n\t    | tab COMA tablatab : ID\n        | ID ID\n\t    | ID AS IDjoin : INNER JOIN j\n\t    | LEFT JOIN j\n\t    | j : tab ON wwhere : WHERE w \n\t    | w : ID PUNTO ID sim ID PUNTO ID\n\t    | ID PUNTO ID sim valor \n\t    | ID PUNTO ID sub \n\t    | w AND w \n\t    | w OR wsim : IGUAL\n\t    | MAYOR_IGUAL\n\t    | MENOR_IGUAL\n\t    | MAYOR\n\t    | MENOR\n\t    | DIFERENTEsub : IN L_PARENT consulta R_PARENT\n\t    | NOT IN L_PARENT consulta R_PARENTvalor : COMILLA ID COMILLA \n\t    | NUMBERgroup : GROUP BY campo_g hav\n\t    | campo_g : ID PUNTO ID \n\t    | ID PUNTO ID COMA campo_ghav : HAVING funcion sim valor\n\t    | order : ORDER BY campo_o\n\t    | campo_o : ID PUNTO ID tipo_o\n\t    | ID PUNTO ID tipo_o COMA campo_otipo_o : ASC \n\t    | DESC'
    
_lr_action_items = {'SELECT':([0,102,110,],[3,3,3,]),'$end':([1,4,14,17,18,19,28,33,42,44,46,48,49,50,56,69,71,72,74,79,81,85,97,99,101,111,112,113,114,115,116,117,118,121,122,],[0,-21,-24,-13,-14,-16,-41,-17,-47,-23,-19,-20,-15,-18,-1,-45,-28,-29,-22,-46,-40,-27,-42,-26,-39,-48,-50,-51,-44,-43,-25,-38,-36,-37,-49,]),'FROM':([2,6,8,20,35,36,37,63,],[5,-2,-5,-3,-4,-7,-8,-6,]),'DISTINCT':([3,11,],[7,25,]),'ID':([3,5,7,19,21,22,23,24,26,27,29,30,31,32,34,39,51,52,54,55,58,59,60,61,62,65,68,83,84,86,87,88,89,90,91,95,100,106,107,120,],[9,19,9,33,9,36,37,38,40,41,45,19,19,19,50,53,63,64,66,67,70,45,45,73,45,76,80,97,98,-30,-31,-32,-33,-34,-35,104,108,70,116,80,]),'COUNT':([3,7,21,82,],[11,11,11,11,]),'MIN':([3,7,21,82,],[12,12,12,12,]),'MAX':([3,7,21,82,],[13,13,13,13,]),'INNER':([4,17,18,19,33,49,50,],[15,-13,-14,-16,-17,-15,-18,]),'LEFT':([4,17,18,19,33,49,50,],[16,-13,-14,-16,-17,-15,-18,]),'WHERE':([4,14,17,18,19,33,46,48,49,50,71,72,74,85,99,101,116,117,118,121,],[-21,29,-13,-14,-16,-17,-19,-20,-15,-18,-28,-29,-22,-27,-26,-39,-25,-38,-36,-37,]),'GROUP':([4,14,17,18,19,28,33,44,46,48,49,50,71,72,74,85,99,101,116,117,118,121,],[-21,-24,-13,-14,-16,43,-17,-23,-19,-20,-15,-18,-28,-29,-22,-27,-26,-39,-25,-38,-36,-37,]),'ORDER':([4,14,17,18,19,28,33,42,44,46,48,49,50,69,71,72,74,81,85,97,99,101,114,115,116,117,118,121,],[-21,-24,-13,-14,-16,-41,-17,57,-23,-19,-20,-15,-18,-45,-28,-29,-22,-40,-27,-42,-26,-39,-44,-43,-25,-38,-36,-37,]),'R_PARENT':([4,14,17,18,19,28,33,42,44,46,48,49,50,56,64,66,67,69,71,72,74,76,79,81,85,97,99,101,109,111,112,113,114,115,116,117,118,119,121,122,],[-21,-24,-13,-14,-16,-41,-17,-47,-23,-19,-20,-15,-18,-1,75,77,78,-45,-28,-29,-22,94,-46,-40,-27,-42,-26,-39,118,-48,-50,-51,-44,-43,-25,-38,-36,121,-37,-49,]),'COMA':([8,18,19,33,36,37,50,63,97,111,112,113,],[21,32,-16,-17,-7,-8,-18,-6,106,120,-50,-51,]),'PUNTO':([9,38,40,41,45,53,70,80,98,],[22,52,54,55,61,65,83,95,107,]),'AS':([10,19,36,75,77,78,94,],[23,34,51,-9,-11,-12,-10,]),'L_PARENT':([11,12,13,25,92,103,],[24,26,27,39,102,110,]),'JOIN':([15,16,],[30,31,]),'ON':([19,33,47,50,],[-16,-17,62,-18,]),'BY':([43,57,],[58,68,]),'AND':([44,71,72,74,85,99,101,116,117,118,121,],[59,59,59,59,-27,-26,-39,-25,-38,-36,-37,]),'OR':([44,71,72,74,85,99,101,116,117,118,121,],[60,60,60,60,-27,-26,-39,-25,-38,-36,-37,]),'HAVING':([69,97,115,],[82,-42,-43,]),'IGUAL':([73,75,77,78,94,96,],[86,-9,-11,-12,-10,86,]),'MAYOR_IGUAL':([73,75,77,78,94,96,],[87,-9,-11,-12,-10,87,]),'MENOR_IGUAL':([73,75,77,78,94,96,],[88,-9,-11,-12,-10,88,]),'MAYOR':([73,75,77,78,94,96,],[89,-9,-11,-12,-10,89,]),'MENOR':([73,75,77,78,94,96,],[90,-9,-11,-12,-10,90,]),'DIFERENTE':([73,75,77,78,94,96,],[91,-9,-11,-12,-10,91,]),'IN':([73,93,],[92,103,]),'NOT':([73,],[93,]),'COMILLA':([84,86,87,88,89,90,91,105,108,],[100,-30,-31,-32,-33,-34,-35,100,117,]),'NUMBER':([84,86,87,88,89,90,91,105,],[101,-30,-31,-32,-33,-34,-35,101,]),'ASC':([104,],[112,]),'DESC':([104,],[113,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'consulta':([0,102,110,],[1,109,119,]),'select':([0,102,110,],[2,2,2,]),'from':([2,],[4,]),'campo':([3,7,21,],[6,20,35,]),'col':([3,7,21,],[8,8,8,]),'funcion':([3,7,21,82,],[10,10,10,96,]),'join':([4,],[14,]),'tabla':([5,32,],[17,49,]),'tab':([5,30,31,32,],[18,47,47,18,]),'where':([14,],[28,]),'group':([28,],[42,]),'w':([29,59,60,62,],[44,71,72,74,]),'j':([30,31,],[46,48,]),'order':([42,],[56,]),'campo_g':([58,106,],[69,115,]),'campo_o':([68,120,],[79,122,]),'hav':([69,],[81,]),'sim':([73,96,],[84,105,]),'sub':([73,],[85,]),'valor':([84,105,],[99,114,]),'tipo_o':([104,],[111,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> consulta","S'",1,None,None,None),
  ('consulta -> select from join where group order','consulta',6,'p_Consulta','grupo06.py',94),
  ('select -> SELECT campo','select',2,'p_select','grupo06.py',97),
  ('select -> SELECT DISTINCT campo','select',3,'p_select','grupo06.py',98),
  ('campo -> col COMA campo','campo',3,'p_campo','grupo06.py',101),
  ('campo -> col','campo',1,'p_campo','grupo06.py',102),
  ('col -> ID PUNTO ID AS ID','col',5,'p_col','grupo06.py',105),
  ('col -> ID PUNTO ID','col',3,'p_col','grupo06.py',106),
  ('col -> funcion AS ID','col',3,'p_col','grupo06.py',107),
  ('funcion -> COUNT L_PARENT ID PUNTO ID R_PARENT','funcion',6,'p_funcion','grupo06.py',121),
  ('funcion -> COUNT DISTINCT L_PARENT ID PUNTO ID R_PARENT','funcion',7,'p_funcion','grupo06.py',122),
  ('funcion -> MIN L_PARENT ID PUNTO ID R_PARENT','funcion',6,'p_funcion','grupo06.py',123),
  ('funcion -> MAX L_PARENT ID PUNTO ID R_PARENT','funcion',6,'p_funcion','grupo06.py',124),
  ('from -> FROM tabla','from',2,'p_from','grupo06.py',149),
  ('tabla -> tab','tabla',1,'p_tabla','grupo06.py',152),
  ('tabla -> tab COMA tabla','tabla',3,'p_tabla','grupo06.py',153),
  ('tab -> ID','tab',1,'p_tab','grupo06.py',156),
  ('tab -> ID ID','tab',2,'p_tab','grupo06.py',157),
  ('tab -> ID AS ID','tab',3,'p_tab','grupo06.py',158),
  ('join -> INNER JOIN j','join',3,'p_join','grupo06.py',170),
  ('join -> LEFT JOIN j','join',3,'p_join','grupo06.py',171),
  ('join -> <empty>','join',0,'p_join','grupo06.py',172),
  ('j -> tab ON w','j',3,'p_j','grupo06.py',175),
  ('where -> WHERE w','where',2,'p_where','grupo06.py',178),
  ('where -> <empty>','where',0,'p_where','grupo06.py',179),
  ('w -> ID PUNTO ID sim ID PUNTO ID','w',7,'p_w','grupo06.py',182),
  ('w -> ID PUNTO ID sim valor','w',5,'p_w','grupo06.py',183),
  ('w -> ID PUNTO ID sub','w',4,'p_w','grupo06.py',184),
  ('w -> w AND w','w',3,'p_w','grupo06.py',185),
  ('w -> w OR w','w',3,'p_w','grupo06.py',186),
  ('sim -> IGUAL','sim',1,'p_sim','grupo06.py',215),
  ('sim -> MAYOR_IGUAL','sim',1,'p_sim','grupo06.py',216),
  ('sim -> MENOR_IGUAL','sim',1,'p_sim','grupo06.py',217),
  ('sim -> MAYOR','sim',1,'p_sim','grupo06.py',218),
  ('sim -> MENOR','sim',1,'p_sim','grupo06.py',219),
  ('sim -> DIFERENTE','sim',1,'p_sim','grupo06.py',220),
  ('sub -> IN L_PARENT consulta R_PARENT','sub',4,'p_sub','grupo06.py',223),
  ('sub -> NOT IN L_PARENT consulta R_PARENT','sub',5,'p_sub','grupo06.py',224),
  ('valor -> COMILLA ID COMILLA','valor',3,'p_valor','grupo06.py',227),
  ('valor -> NUMBER','valor',1,'p_valor','grupo06.py',228),
  ('group -> GROUP BY campo_g hav','group',4,'p_group','grupo06.py',231),
  ('group -> <empty>','group',0,'p_group','grupo06.py',232),
  ('campo_g -> ID PUNTO ID','campo_g',3,'p_campo_g','grupo06.py',235),
  ('campo_g -> ID PUNTO ID COMA campo_g','campo_g',5,'p_campo_g','grupo06.py',236),
  ('hav -> HAVING funcion sim valor','hav',4,'p_hav','grupo06.py',249),
  ('hav -> <empty>','hav',0,'p_hav','grupo06.py',250),
  ('order -> ORDER BY campo_o','order',3,'p_order','grupo06.py',253),
  ('order -> <empty>','order',0,'p_order','grupo06.py',254),
  ('campo_o -> ID PUNTO ID tipo_o','campo_o',4,'p_campo_o','grupo06.py',257),
  ('campo_o -> ID PUNTO ID tipo_o COMA campo_o','campo_o',6,'p_campo_o','grupo06.py',258),
  ('tipo_o -> ASC','tipo_o',1,'p_tipo_o','grupo06.py',271),
  ('tipo_o -> DESC','tipo_o',1,'p_tipo_o','grupo06.py',272),
]

#!/usr/local/bin/python
 
#import cgi
#import MySQLdb
import simplejson
 
print "Content-Type: application/json"
print



result = {'records' : [{'Giacienza_iniziale':'12' , 'Prodotto':'Tela' , 'Descrizione': 'Bianco' , 'Giacienza': '2' , 'Scarico': '10' , 'Carico': '12' , 'Prezzo': '12'} ,
					   {'Giacienza_iniziale':'13' , 'Prodotto':'Post' , 'Descrizione': 'Nero' , 'Giacienza': '4' , 'Scarico': '14' , 'Carico': '10' , 'Prezzo': '5'},
					   {'Giacienza_iniziale':'23' , 'Prodotto':'fff' , 'Descrizione': 'Neferfro' , 'Giacienza': '44' , 'Scarico': '514' , 'Carico': '150' , 'Prezzo': '65'}
					   ]}

json_string = simplejson.dumps(result)
print json_string
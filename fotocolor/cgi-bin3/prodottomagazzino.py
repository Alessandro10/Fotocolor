import os
import sys
import cgi, cgitb 
import MySQLdb
import simplejson
#import json

if __name__ == '__main__':
	cgitb.enable()  # for troubleshooting
	#the cgi library gets vars from html
	data = cgi.FieldStorage()

	idprodotto = data["idprodotto"].value
	idmagazzino = data["idmagazzino"].value
	quantita = data["quantita"].value
	idvariante = data["idvariante"].value
	risultato = 0
	#print "Content-Type: text/html\n"
	#print idprodotto
	#print idmagazzino
	#print idvariante
	#print quantita

	db2 = MySQLdb.connect("127.0.0.1","root","admin","myDB" )
	cursor2 = db2.cursor()

	cursor2.execute("INSERT INTO prodottomagazzino(idprodotto , idmagazzino , quantita , idvariante) VALUES("+ str(idprodotto) +" , " + str(idmagazzino) + " , " + str(quantita) + " , " + str(idvariante) + ")")

	db2.commit()
	db2.close()
	risultato = 1
	print "Content-Type: application/json"
	print


	result = {'records' : [{"risultato":risultato}
						   ]}

	json_string = simplejson.dumps(result)
	print json_string
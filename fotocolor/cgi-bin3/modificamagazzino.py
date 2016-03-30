import os
import sys
import cgi, cgitb 
import MySQLdb
#import json


if __name__ == '__main__':
	
	cgitb.enable()  # for troubleshooting
	#the cgi library gets vars from html
	data = cgi.FieldStorage()
	
	db = MySQLdb.connect("127.0.0.1","root","admin","myDB" )
	
	cursor = db.cursor()
	print "Content-Type: text/html\n"
	idmagazzino = str(data["idmagazzino"].value)
	descrizione = str(data["descrizione"].value)
	giacenza_iniziale = str(data["giacenza_iniziale"].value)
	carico = str(data["carico"].value)
	scarico = str(data["scarico"].value)
	prezzo = str(data["prezzo"].value)
	
	first = 'update magazzino set nome="' + descrizione + '" , ultimo_prezzo="' + prezzo + '" , carico="' + carico + '" , scarico="' + scarico + '" where idmagazzino = ' + idmagazzino
	#print first
	cursor.execute(first)
	
	db.commit()
	db.close()
	
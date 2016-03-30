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
	cursor.execute('SELECT count(*)+1 from magazzino;')
	for i in cursor:
		idmagazzino = i[0]
	descrizione = str(data["descrizione"].value)
	giacenza_iniziale = str(data["giacenza_iniziale"].value)
	carico = giacenza_iniziale
	scarico = "0"
	prezzo = str(data["prezzo"].value)
	if(giacenza_iniziale == ""):
		giacenza_iniziale = "0"
	if(carico == ""):
		carico = "0"
	if(scarico == ""):
		scarico = "0"
	
	first = 'INSERT INTO mydb.magazzino(idmagazzino ,nome , ultimo_prezzo , carico , scarico) VALUES (' + str(idmagazzino) + ' ,"' + str(descrizione) + '" , ' + str(prezzo) + ' , ' + str(carico) + ' , ' + str(scarico) + ');'
	second = 'INSERT INTO mydb.storico( idmagazzino , data , giacenza , prezzo) VALUES(' + str(idmagazzino) + ' , curdate() , ' + giacenza_iniziale + ' , ' + str(prezzo) + ');'
	#print first
	cursor.execute(first)
	#print second
	cursor.execute(second)
	
	db.commit()
	db.close()
	
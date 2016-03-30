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
	#this is the actual output

	#outdir="C:\inetpub\wwwroot\cgi-bin3"
	#print "Content-Type: text/html\n"
	id_del_prodotto = -1
	risultato = 1
	name_product = ""	
	idvariante = 0
	nomevariante =""
	#db = MySQLdb.connect(host="192.168.4.145",user="root",passwd="admin",db="mylabdb" )
	db = MySQLdb.connect(host="192.168.4.33",user="root",passwd="admin",db="mylabdb" )
	db2 = MySQLdb.connect("127.0.0.1","root","admin","myDB" )
	
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	#dict_cursor = db.cursor(MySQLdb.cursors.DictCursor)
	
	cursor2 = db2.cursor()
	
	barcode_id = data["barcode_id"].value
	#print barcode_id
	
	#query su MyLabDB per prendere l'id prodotto , quantita e descrizione
	cursor.execute('SELECT PRODUCT_ID , QUANTITY , FINAL_NOTES FROM myorder where BARCODE_ID=' + str(barcode_id))

	
	for i in cursor:
		product_id = i[0]
		quantita = i[1]
		final_notes = i[2]
	#print "product_id = " + str(product_id)
	
	#vedo se il prodotto esiste nel mio db
		cursor2.execute('SELECT * FROM prodotto where idprodotto=' + str(product_id))
		for i in cursor2:
			id_del_prodotto = i[0]
			name_product = i[1]
		righe = cursor2.rowcount
		
		if(righe == 0):
			#se non esiste lo creo prendendo il nome dal MyLabDB
			cursor.execute('SELECT id , descr FROM mylabdb.product where id=' + str(product_id))
			for i in cursor:
				id_del_prodotto = i[0]
				name_product = i[1]
			
			#prendo il gruppo
			cursor.execute('SELECT ID_GROUP from group_product where ID_PRODUCT = ' + str(product_id))
			for i in cursor:
				group_id = i[0]
				#print "group_id = " + str(group_id)
				#prendo l'associazione	
				cursor.execute('SELECT GROUP_DESC , REP_GROUPNAME from print_group WHERE id = ' + str(group_id))
				
				for i in cursor:
					group_desc = i[0]
					rep_groupname = i[1]
				#print "group_desc = " + str(group_desc)
				#print "rep_groupname = " + str(rep_groupname)
				
				cursor2.execute('SELECT * FROM gruppo WHERE idgruppo=' + str(group_id))
				if(cursor2.rowcount == 0):
					#print 'INSERT INTO gruppo(idgruppo , nome , rep_groupname) VALUES(' + str(group_id) + ' , "' + str(group_desc) + '", "' + str(rep_groupname) + '")'
					cursor2.execute('INSERT INTO gruppo(idgruppo , nome , rep_groupname) VALUES(' + str(group_id) + ' , "' + str(group_desc) + '", "' + str(rep_groupname) + '")')
			
				#print 'INSERT INTO prodotto(idprodotto , nome) VALUES(' + str(product_id) + ' , "' + str(name_product) + '")'
				cursor2.execute('INSERT INTO prodotto(idprodotto , nome) VALUES(' + str(product_id) + ' , "' + str(name_product) + '")')
				
				#print 'INSERT INTO prodottogruppo(idprodotto , idgruppo) VALUES(' + str(product_id) + ' , "' + str(group_id) + '")'
				cursor2.execute('INSERT INTO prodottogruppo(idprodotto , idgruppo) VALUES(' + str(product_id) + ' , "' + str(group_id) + '")')
		#vedo se ho la descrizione nel mio DB
		cursor2.execute('SELECT idvariante,descrizione from variante where descrizione LIKE "' + str(final_notes) + '"')
		for i in cursor2:
			idvariante = i[0]
			nomevariante = i[1]
		righe = cursor2.rowcount
		if(righe == 0):
			#se non esiste lo creo
			cursor2.execute('SELECT count(*)+1 from variante;')
			for i in cursor2:
				idvariante = i[0]
			nomevariante = final_notes
			#print 'INSERT INTO variante(idvariante , descrizione) VALUES(' + str(idvariante) + ' , ' + str(final_notes) + ')'
			cursor2.execute('INSERT INTO variante(idvariante , descrizione) VALUES(' + str(idvariante_insert) + ' , ' + str(final_notes) + ')')
		#trovo l'id magazzino nel mio db sapendo prodotto e variante
		cursor2.execute('SELECT idmagazzino , quantita FROM prodottomagazzino where idprodotto=' + str(product_id) + ' and idvariante=' + str(idvariante))
		righe = cursor2.rowcount
		if(righe != 0):
			for i in cursor2:
				idmagazzino = i[0]
				quantita = i[1]
				#se esiste un associazione prendo lo scarico e lo incremento di quantita
				cursor2.execute('SELECT scarico FROM magazzino where idmagazzino=' + str(idmagazzino))
				for i in cursor2:
					scarico = i[0]
				scarico = scarico + quantita
				#print 'UPDATE magazzino SET scarico=' + str(scarico) + ' WHERE idmagazzino=' + str(idmagazzino)
				cursor2.execute('UPDATE magazzino SET scarico=' + str(scarico) + ' WHERE idmagazzino=' + str(idmagazzino))
				risultato=2
			#print "devi creare nuova entita prodottomagazzino " + str(product_id) + " , " + str(idvariante)
		# disconnect from server
		else:
			risultato = 0
		
	db.close()
	db2.commit()
	db2.close()
	
	print "Content-Type: application/json"
	print

	
	result = {'records' : [{"risultato":risultato , "nome":name_product , "id":id_del_prodotto , "idvariante":idvariante , "nomevariante":nomevariante}
						   ]}

	json_string = simplejson.dumps(result)
	print json_string
	
	
	"""db = MySQLdb.connect("127.0.0.1","root","admin","myDB" )
	
	cursor = db.cursor()
	
	cursor.execute('INSERT INTO gruppo values (25 , 252 , 52);')
	
	db.commit()
	db.close()"""
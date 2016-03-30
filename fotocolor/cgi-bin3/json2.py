#!/usr/local/bin/python
 
#import cgi
import MySQLdb
import simplejson
 
if __name__ == '__main__':
	db = MySQLdb.connect("127.0.0.1","root","admin","myDB" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	#cursor.execute('SELECT m.nome , m.ultimo_prezzo ,  s.giacenza , s.giacenza + m.carico - m.scarico as giacenzafinale , m.scarico , m.carico , sum(quantita) as quantita , m.idmagazzino FROM storico s , magazzino m , prodottomagazzino pm WHERE s.idmagazzino = m.idmagazzino and m.idmagazzino = pm.idmagazzino group by m.nome;')
	cursor.execute('SELECT m.nome , m.ultimo_prezzo ,  s.giacenza , s.giacenza + m.carico - m.scarico as giacenzafinale , m.scarico , m.carico , sum(quantita) as quantita , m.idmagazzino , g.nome FROM storico s , magazzino m , prodottomagazzino pm , prodotto p , prodottogruppo pg , gruppo g WHERE p.idprodotto = pm.idprodotto and p.idprodotto = pg.idprodotto and pg.idgruppo = g.idgruppo and s.idmagazzino = m.idmagazzino and m.idmagazzino = pm.idmagazzino group by m.nome;')
	
	dict = {}
	list = []
	dict2 = {}
	for i in cursor:
		dict["Prodotto"] = i[0]
		dict["Prezzo"] = i[1]
		dict["giacenza"] = i[2]
		dict["giacenza_iniziale"] = i[3]
		dict["Scarico"] = i[4]
		dict["Carico"] = i[5]
		dict["Quantita"] = i[6]
		dict["idmagazzino"] = i[7]
		dict['Gruppo'] = i[8]
		#print i
		list.append(dict)
		dict = {}
	#print list
	dict2["records"] = list
	
	cursor.execute('SELECT idmagazzino , nome FROM mydb.magazzino;')
	
	dict1 = {}
	list2 = []
	
	for i in cursor:
		dict1["idmagazzino"] = i[0]
		dict1["Prodotto"] = i[1]
		
		#print i
		list2.append(dict1)
		dict1 = {}
	dict2["magazzino"] = list2
	
	#print dict2
	print "Content-Type: application/json"
	print
	
	"""result = {'records' : [{'giacenza_iniziale':'12' , 'Prodotto':'Tela' , 'Descrizione': 'Bianco' , 'giacenza': '2' , 'Scarico': '10' , 'Carico': '12' , 'Prezzo': '12'} ,
						   {'giacenza_iniziale':'13' , 'Prodotto':'Post' , 'Descrizione': 'Nero' , 'giacenza': '4' , 'Scarico': '14' , 'Carico': '10' , 'Prezzo': '5'},
						   {'giacenza_iniziale':'23' , 'Prodotto':'fff' , 'Descrizione': 'Neferfro' , 'giacenza': '44' , 'Scarico': '514' , 'Carico': '150' , 'Prezzo': '65'}
						   ]}"""

	json_string = simplejson.dumps(dict2)
	print json_string
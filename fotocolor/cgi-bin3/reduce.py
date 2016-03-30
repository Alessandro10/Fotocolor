#!/usr/bin/python

""""import cgi, cgitb 
cgitb.enable()  # for troubleshooting

#the cgi library gets vars from html
data = cgi.FieldStorage()
#this is the actual output
print "Content-Type: text/html\n"
print "YOOO"
#print data["image"].value
#print "The foo data is: " + data["foo"].value
print "<br />"
#print "The bar data is: " + data["bar"].value
print "<br />"
#print data"""


import cgi, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
#if len(form) == None:
	#print "None"
    #fileitem = form["img"].value
v = "Ok"
if form == None:
	v = "None"
#v = form["bar"].value
from PIL import Image, ImageFilter
print "Content-Type: text/html\n"
print("<html><head><title>Python</title></head><body>"+ v +"<body>")
#print("<h5>"+str(len(form))+"</h5>")
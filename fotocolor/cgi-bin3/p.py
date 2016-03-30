#!/usr/bin/python
from __future__ import division
import Image
import math
import os
import sys
import cgi, cgitb 
import urllib
import cStringIO
import PIL.Image
import os
from PIL import Image

def tagliaImg10(image_path , out_name , outdir , left_html , top_html , base_html , altezza_html , base_cm_fine , altezza_cm_fine , base_riquadro , altezza_riquadro , angolo):
	"""slice an image into parts slice_size tall2"""
	img = Image.open(image_path)
	img2 = img.convert('RGBA')
	
	print "LEFT_HTML: " + str(left_html) + " - TOP_HTML: " + str(top_html)
	print "BASE_HTML: " + str(base_html) + "ALTEZZA_HTML: " + str(altezza_html)
	print "BASE_RIQUADRO: " + str(base_riquadro) + "ALTEZZA_RIQUADRO: " + str(altezza_riquadro)

	
	img2 = img2.rotate(-angolo , resample=Image.AFFINE , expand=True)
	base_originale, altezza_originale = img2.size
	#base_girata, altezza_girata = img2.size

	print "B.O. = " + str(base_originale)  + " -A.O. = " + str(altezza_originale)
	img2.save(os.path.join(outdir, "anteprimataglio3" + out_name + ".jpeg") , "JPEG" , dpi=(200,200) , quality=85)
	
	left_originale = (base_originale*left_html)/base_html
	top_originale = (altezza_originale*top_html)/altezza_html

	altezza_fuoriesce_html = altezza_html - altezza_riquadro
	base_fuoriesce_html = base_html - base_riquadro
	altezza_fuoriesce_originale = (altezza_originale*altezza_fuoriesce_html)/altezza_html
	base_fuoriesce_originale = (base_originale*base_fuoriesce_html)/base_html
	altezza_riquadro_originale = (altezza_originale*altezza_riquadro)/altezza_html
	base_riquadro_originale = (base_originale*base_riquadro)/base_html
	l , t , x , y = 0 , 0 , 0 , 0
	top_bianco_html = 0
	top_fine = 0
	left_bianco_html = 0
	left_fine = 0
	top_bianco_originale = 0
	left_bianco_originale = 0
	l_f = 0
	t_f = 0
	dpi = 200
	base_fine = int((base_cm_fine*dpi)/2.54)
	altezza_fine = int((altezza_cm_fine*dpi)/2.54)
	bottom_bianco_fine = 0
	right_bianco_fine = 0

	if(top_html > 0):
		t = 0 
		top_bianco_html =  int(top_html)
		top_bianco_originale = (altezza_originale*top_bianco_html)/altezza_html
		bottom_bianco_html = altezza_riquadro - altezza_html
		top_fine = (top_bianco_originale*altezza_fine)/altezza_originale
		t_f = (altezza_fine*top_bianco_originale)/altezza_riquadro_originale
		
		if(altezza_originale < altezza_riquadro_originale):
			y = altezza_originale
			#y = altezza_girata
			altezza_riquadro_fine = (altezza_fine*y)/altezza_originale
			bottom_bianco_originale = (bottom_bianco_html*altezza_riquadro_originale)/altezza_riquadro		
			bottom_bianco_fine = (bottom_bianco_originale*altezza_riquadro_fine)/altezza_riquadro_originale
		else:
			y = int(altezza_riquadro_originale-top_bianco_originale) 
			altezza_riquadro_fine = (altezza_fine*y)/altezza_originale
			bottom_bianco_fine = t_f
		t_b_f = (altezza_riquadro_fine*top_bianco_originale)/altezza_riquadro_originale
		
	else:
		t = int(top_originale)
		y = int(altezza_riquadro_originale - t)  
		bottom_bianco_html = altezza_riquadro - altezza_html
		altezza_riquadro_fine = (altezza_fine*y)/altezza_originale
		if(-top_html > altezza_fuoriesce_html):
			y = altezza_originale
			top_bianco_html = int(-top_html - altezza_fuoriesce_html)
		else:
			top_bianco_html = 0
		top_bianco_originale = (altezza_originale*top_bianco_html)/altezza_html
		bottom_bianco_html = top_bianco_html
		bottom_bianco_originale = (bottom_bianco_html*altezza_riquadro_originale)/altezza_riquadro		
		bottom_bianco_fine = (bottom_bianco_originale*altezza_riquadro_fine)/altezza_riquadro_originale	
	
	if(left_html > 0):
		l = 0 
		left_bianco_html =  int(left_html)
		left_bianco_originale = (base_originale*left_bianco_html)/base_html
		right_bianco_html = base_riquadro - base_html
		left_fine = (left_bianco_originale*base_fine)/base_originale
		l_f = (base_fine*left_bianco_originale)/base_riquadro_originale
		
		if(base_originale < base_riquadro_originale):
			x = base_originale
			#x = base_girata
			base_riquadro_fine = (base_fine*x)/base_originale
			right_bianco_originale = (right_bianco_html*base_riquadro_originale)/base_riquadro		
			right_bianco_fine = (right_bianco_originale*base_riquadro_fine)/base_riquadro_originale
		else:
			x = int(base_riquadro_originale-left_bianco_originale) 
			base_riquadro_fine = (base_fine*x)/base_originale
			right_bianco_fine = l_f
		l_b_f = (base_riquadro_fine*left_bianco_originale)/base_riquadro_originale
		
	else:
		l = int(left_originale)
		x = int(base_riquadro_originale - l)  
		right_bianco_html = base_riquadro - base_html
		base_riquadro_fine = (base_fine*x)/base_originale
		if(-left_html > base_fuoriesce_html):
			x = base_originale
			left_bianco_html = int(-left_html - base_fuoriesce_html)
		else:
			left_bianco_html = 0
		left_bianco_originale = (base_originale*left_bianco_html)/base_html
		right_bianco_html = left_bianco_html
		right_bianco_originale = (right_bianco_html*base_riquadro_originale)/base_riquadro		
		right_bianco_fine = (right_bianco_originale*base_riquadro_fine)/base_riquadro_originale
	
	
	bbox = (int(-l), int(-t) , int(x) , int(y))
	diff_altezza_originale = altezza_originale - (y+t)
	diff_base_originale = base_originale - (x+l)
	
	print "BASE_RIQUADRO_fine: " + str(base_riquadro_fine) + " left_bianco_originale: " + str(left_bianco_originale)
	
	diff_base_fine = (base_fine*diff_base_originale)/base_originale
	diff_altezza_fine = (altezza_fine*diff_altezza_originale)/altezza_originale
	
	base_originale2 = base_originale + 700
	altezza_originale2 = altezza_originale + 700

	working_slice = img2.crop(bbox)	
	working_slice.save(os.path.join(outdir, "anteprimataglio" + out_name + ".jpeg") , "JPEG" , dpi=(dpi,dpi) , quality=85)

	print "BASE_ORIGINALE: " + str(base_originale) + " ALTEZZA_ORIGINALE: " + str(altezza_originale)
	
	top_bianco_fine = (altezza_fine*top_bianco_originale)/altezza_originale
	left_bianco_fine = (base_fine*left_bianco_originale)/base_originale	
	new_img = Image.new('RGBA', (base_fine , altezza_fine) , "red")
	base_fuoriesce_fine = (base_fine*base_fuoriesce_originale)/base_originale
	altezza_fuoriesce_fine = (altezza_fine*altezza_fuoriesce_originale)/altezza_originale
	size = int((base_fine-(right_bianco_fine))) , int((altezza_fine-(bottom_bianco_fine)))

	working_slice = working_slice.resize(size, Image.ANTIALIAS)
	print "angolo ==> " + str(angolo)
	new_img.paste(working_slice, (int(l_f) , int(t_f)) , working_slice)
	print  base_originale , altezza_originale
	print "size = " + str(size)
	print top_html , left_html
	print top_originale , left_originale
	print "L_F = " + str(l_f) + " T_F" + str(t_f)
	print "--------------------"
	print top_bianco_html , left_bianco_html
	print top_bianco_originale , left_bianco_originale
	print top_bianco_fine , left_bianco_fine
	print "_________________________"
	print altezza_html , base_html
	print altezza_fine , base_fine
	quality_val = 85
	new_img.save(os.path.join(outdir + "/img", "slice_12" + out_name + ".jpeg") , "JPEG" , dpi=(dpi,dpi) , quality=quality_val)
	
	
	
	
if __name__ == '__main__':
	cgitb.enable()  # for troubleshooting
	#the cgi library gets vars from html
	data = cgi.FieldStorage()
	#this is the actual output

	outdir="C:\inetpub\wwwroot\cgi-bin3"
	print "Content-Type: text/html\n"
	print "YOOO"
	nome = data["name"].value #+ ".jpg"
	top2 = data["top"].value
	left2 = data["left"].value
	width2 = data["width"].value
	height2 = data["height"].value
	base2 = data["base"].value
	altezza2 = data["altezza"].value
	base_riquadro = data["base_riquadro"].value 
	altezza_riquadro = data["altezza_riquadro"].value 
	angolo = data["angolo"].value 
	print width2
	print height2
	urllib.urlretrieve(data["src"].value , nome)
	urllib.urlcleanup()
	img = PIL.Image.open(nome);
	dpi = 200
	quality_val = 85
	img.save(os.path.join(outdir, nome) , "JPEG" , dpi=(dpi,dpi) , quality=quality_val)
	tagliaImg10(nome , "longcat" , os.getcwd() , int(left2) , int(top2) , int(width2) , int(height2) , int(base2) , int(altezza2) , int(base_riquadro) , int(altezza_riquadro) , int(angolo));
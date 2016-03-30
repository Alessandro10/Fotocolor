import urllib
urllib.urlretrieve("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAATOUAAAxNCAIAAADNFtWeAAAACXBIW…DAgQMHDhw4cODAgQMHDhw4cODAgQMHDhw4cODAgb8J/v9JOKyKfmYvIAAAAABJRU5ErkJggg==", "00000001.jpg")

def tagliaImg(image_path , out_name , outdir , left , upper , right , lower , width_p , height_p):
    """slice an image into parts slice_size tall"""
    img = Image.open(image_path)
    #print(img.info['dpi'])
    width, height = img.size
    print width , height
    #upper = 20
    #left = 20
    bbox = (left, upper, right, lower)
    working_slice = img.crop(bbox)
    #size = 250 , 40
    dpi = 200
    new_img = Image.new('RGB', (int((width_p*dpi)/2.54) , int((height_p*dpi)/2.54)) , "white")
    size = int((width_p*dpi)/2.54) , int((height_p*dpi)/2.54)
    #working_slice.thumbnail(size, Image.ANTIALIAS)
    working_slice = working_slice.resize(size, Image.ANTIALIAS)
    #box = (0, 0 ,int((250*dpi)/2.54) , int((40*dpi)/2.54))
    #new_img.paste(img , box)
    new_img.paste(working_slice, (0,0))
    quality_val = 85
    new_img.save(os.path.join(outdir, "slice_" + out_name + "_" + str(1)+".jpeg") , "JPEG" , dpi=(dpi,dpi) , quality=quality_val)
    #working_slice.save(os.path.join(outdir, "slice_" + out_name + "_" + str(1)+".png") , dpi=(dpi,dpi))
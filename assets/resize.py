from PIL import Image
import os, sys

cwd = os.getcwd()
path= os.path.join(cwd,"images")
print(path)
dirs = os.walk( path )
final_size = 244;

def resize_aspect_fit():

    for root,dired,items in dirs:
    	for item in items:
	    	if os.path.isfile(os.path.join(root,item)):
	             print(item,flush=True)
	             try:
	             	im = Image.open(os.path.join(root,item))
	             	f, e = os.path.splitext(os.path.join(root,item))
	             	size = im.size
	             	ratio = float(final_size) / max(size)
	             	new_image_size = tuple([int(x*ratio) for x in size])
	             	im = im.resize(new_image_size, Image.ANTIALIAS)
	             	new_im = Image.new("RGB", (final_size, final_size))
	             	new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
	             	new_im.save(os.path.join(root,item) , 'JPEG', quality=85)
	             except Exception as e:
	             	pass

resize_aspect_fit()
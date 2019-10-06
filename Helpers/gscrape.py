from bs4 import BeautifulSoup
import requests
import re
import urllib
import os
import argparse
import sys
import json
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
	
# adapted from http://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search

def get_soup(url,header):
    return BeautifulSoup(urlopen(urllib.request(url,headers=header)),'html.parser')

def main(search,num_images,directory):

	query = search
	max_images = num_images
	save_directory = directory
	image_type="Action"
	query= query.split()
	query='+'.join(query)
	url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
	header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
	soup = get_soup(url,header)
	ActualImages=[]# contains the link for Large original images, type of  image
	for a in soup.find_all("div",{"class":"rg_meta"}):
	    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
	    ActualImages.append((link,Type))
	for i , (img , Type) in enumerate( ActualImages[0:max_images]):
	    try:
	        req = urllib.request(img, headers={'User-Agent' : header})
	        raw_img = urlopen(req).read()
	        if len(Type)==0:
	            f = open(os.path.join(save_directory , "img" + "_"+ str(i)+".jpg"), 'wb')
	        else :
	            f = open(os.path.join(save_directory , "img" + "_"+ str(i)+"."+Type), 'wb')
	        f.write(raw_img)
	        f.close()
	    except Exception as e:
	        print("could not load : "+img)
	        print(e)

if __name__ == '__main__':
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        pass
    sys.exit()

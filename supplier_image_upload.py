#! /usr/bin/env python3
import requests
import os

path = "./supplier-data/images/"
url = "http://localhost/upload/"

for img in os.listdir(path):
  if not img.endswith(".jpeg"):
    continue
  image = open(path+img, 'rb')
  r = requests.post(url, files={'file': image})
  image.close()
 

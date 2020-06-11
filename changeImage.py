#!/usr/bin/env python3
from PIL import Image 
import os 
import glob 

path = "./supplier-data/images"
imgDir = os.listdir(path)

for img in imgDir:
  if not img.endswith(".tiff"):
    continue
  image = Image.open(path+"/"+img)
  image = image.convert("RGB")
  image = image.resize((600,400))
  image.save(path + "/" + img[:-4] + "jpeg")


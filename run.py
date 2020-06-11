#! /usr/bin/env python3

import os
import requests

path = "./supplier-data/descriptions/"
url = "http://localhost/fruits/"

for file in os.listdir(path):
  txt = open(path + file)
  info = txt.read().split("\n")

  fruit_dict = {}
  fruit_dict["name"] = info[0]
  fruit_dict["weight"] = int(info[1][:-4])
  fruit_dict["description"] = info[2]
  fruit_dict["image_name"] = file[:-3] + "jpeg"
  
  r = requests.post(url,json = fruit_dict)
  print(r)
  txt.close()


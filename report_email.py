#!/usr/bin/env python3
import os
import reports
import datetime

def process_data(filepath):
  report = ""
  for txt in os.listdir(filepath):
    desc = open(filepath + txt)
    info = desc.read().split("\n")
    report += "\nname: " + info[0] + "\nweight: " + info[1] + "\n"
  return report 



if __name__ == "__main__":
  path = "./supplier-data/descriptions/"
  print(process_data(path))
  print("Processed Update on " + str(datetime.datetime.today()))

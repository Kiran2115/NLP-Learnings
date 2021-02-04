import json 
import csv

js = open('breast_cancer.json',) 
  

data = json.load(js) 
  

#for i in data['cancer']: 
#    print(i) 
file = "test.csv"
with open(file, "w") as test:
	csv_file = csv.writer(test)
	csv_file.writerow(["DiseaseName","Indication","RegimenName"])

	for item in data:
		csv_file.writerow([item["DiseaseName"],item["Indication"],item["RegimenName"]])



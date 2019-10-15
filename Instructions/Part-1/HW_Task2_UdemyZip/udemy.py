##################################
#Need to account for minutes?
#currently created output already a tuple?



import os
import csv

udemy_csv = os.path.join("web_starter.csv")

title = []
price = []
subscribers = []
reviews = []
length = []
p100subrevd = []
length_string = []

with open(udemy_csv, encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # loop through
    for row in csvreader:
            
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])
        length_string = (row[9].split())
        
        if "mins" in length_string:
            length.append(round(int(int(length_string[0])/60)))
        else: length.append((round(int(round(float(length_string[0]))))))
            
        p100subrevd.append((round(((int(row[6])/int(row[5]))*100), 2)))
        
    
zipped_data = zip(title, price, subscribers, reviews, length, p100subrevd)

output_file = os.path.join("zach_web_final.csv")

with open(output_file, "w", newline='') as datafile:
        writer = csv.writer(datafile)
        
        writer.writerow(["Title","Price","Subscribers","Reviews","Length","Reviewed by n% Subscribers"])
        writer.writerows(zipped_data)
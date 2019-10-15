# =============================================================================
# -tell python to use csv library to open the file "employees.csv"
# -use csv.DictReader function to "process"(take in and present) the contents of 
#   "employees.csv" as though it were a list of dictionary-rows, 
#   with each row containing the keys first_name, last_name, and ssn
#   along with the corresponding values, for one employee per row
# -make lists for each key and an email list
# -fill each list with the correspond information value for each employee
# -fill the email list with concatonated strings from first_name, last_name,
#   "@", and domain
# -use csv.DictWriter to make a new dictionary with keys based on the 
#   list names and values based on the list entries
# -add the newly written dictionaries to a new list, "new_employee_data" 
#   such that each element of the list is a dictionary for each employee
# =============================================================================

# -*- coding: UTF-8 -*-
"""Employee Email Script.

This module allows us to create an email address using employee data from
a csv file.

Example:
    $ python employee_email.py

"""
import os
import csv

filepath = os.path.join("Resources", "employees.csv")

new_employee_data = []


# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        first_name = row['first_name']
        last_name = row['last_name']
        email = f"{first_name}.{last_name}@spookyboys.cia.gov"
        
        new_employee_data.append(
                {
                     'first_name': row['first_name'],
                     'last_name': row['last_name'],
                     'ssn': row['ssn'],
                     'email': email
                }
            )
        
#        first_name.append(row['first_name'])
#        new_employee_data[0].append(row['first_name'])
#        last_name.append(row['last_name'])
#        new_employee_data[1].append(row['last_name'])
#        ssn.append(row['ssn'])
#        new_employee_data[2].append(row['ssn'])
#        emailaddresses.append(email)
#        new_employee_data[3].append(email)     
_, filename = os.path.split(filepath)
csvpath = os.path.join("output", filename)
with open(csvpath, "w") as csvfile:
        fieldnames = ["last_name", "first_name", "ssn", "email"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_employee_data)
        
        
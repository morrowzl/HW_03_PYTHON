# -*- coding: UTF-8 -*-
"""PyBoss Homework Solution."""

import csv
import os

file_to_load = os.path.join("employee_data.csv")
file_to_output = os.path.join("employee_data_reformatted.csv")

us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

#emp_ids = []
#emp_first_names =[]
#emp_last_names = []
#emp_dobs = []
#emp_ssns = []
#emp_states = []
employees = []

with open(file_to_load) as emp_data:
    reader = csv.reader(emp_data)

    header = next(reader)

    for row in reader:
                
        emp_ids = (row[0])
        
        split_name = row[1].split(" ")
        emp_first_names = (split_name[0])
        emp_last_names = (split_name[1])
        
        emp_dobs = (row[2])
        
        split_ssn = row[3].split("-")
        emp_ssns = (f"***-**-{split_ssn[2]}")
        
        emp_states = (us_state_abbrev[row[4]])
        
        employees.append({"Emp ID": emp_ids, 
                          "First Name": emp_first_names, 
                          "Last Name": emp_last_names, 
                          "DOB": emp_dobs, 
                          "SSN": emp_ssns, 
                          "State": emp_states})

with open(file_to_output, "w", newline="") as csvfile:
        fieldnames = ["Emp ID", "First Name",  "Last Name", "DOB", "SSN", "State"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(employees)
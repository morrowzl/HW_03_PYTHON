#Read the resume file as text using the with statement.
#Create a list containing all words in the resume.
#Convert each word to lowercase to normalize the data.
#Use split to remove and trailing punctuation so only words remain.
#Create a set of unique words from the resume using set().
#Use set operations to filter out all remaining punctuation from the set of words.
#Create a set from string.punctuation to use in the difference operation.
#Use the cleaned set (no punctuation) to find all of the words from the resume that match the required skills.
#Use the cleaned set (no punctuation) to find all of the words that match the desired skills.
#Count the number of occurrences for each word in the resume and print the top 10 occurring words in the resume.
#Use a dictionary data structure to hold the counts for each word.
#Make sure to remove punctuation and stop words
#
#Hints
#Carefully consider when to use a Dictionary data structure vs. a Set data structure when operating on Unique and Non-unique elements.

# -*- coding: UTF-8 -*-
"""Resume Analysis Module."""

import os
import string

# Counter is used later in the program
from collections import Counter

# Paths
resume_path = os.path.join("Resources", "resume.md")

# Skills to match
REQUIRED_SKILLS = {"excel", "python", "mysql", "statistics"}
DESIRED_SKILLS = {"r", "git", "html", "css", "leaflet"}

# function to load a file
def load_file(resume_path):
#    """Helper function to read a file and return the data."""
    with open(resume_path, "r") as resume_file_handler:
        
        return resume_file_handler.read().lower().split()

# Grab the text for a Resume
word_list = load_file(resume_path)

# Create a set of unique words from the resume
resume = set(word_list)



# Remove trailing punctuation from words
for token in word_list:
    resume.add(token.split(',')[0].split('.')[0])

# Remove Punctuation that were read as whole words
stop_words = ["and", "with", "using", "##", "working", "in", "to"]
punctuation = set(string.punctuation)
resume = resume - punctuation
print(resume)
print("")
    
# Calculate the Required Skills Match using Set Intersection
print("REQUIRED SKILLS")
print("=============")
print(resume & REQUIRED_SKILLS)
print("")
#
#
# Calculate the Desired Skills Match using Set Intersection
print("DESIRED SKILLS")
print("=============")
print(resume & DESIRED_SKILLS)
print("")
#
# Resume Word Count
# ==========================
# Initialize a dictionary with default values equal to zero
word_count = {}.fromkeys(word_list, 0)

## Loop through the word list and count each word.
for word in word_list:
    word_count[word] += 1
    
word_count = [word for word in word_count if word not in string.punctuation]
word_count = [word for word in word_count if word not in stop_words]

print("WORD COUNT")
print("==============")
print(word_count)
print("")

#
## Using collections.Counter
word_counter = Counter(word_list)
print("WORD COUNTER COUNT")
print("==============")
print(word_counter)
print("")
## Comparing both word count solutions
print(word_count == word_counter)
print("")

## Top 10 Words
print("Top 10 Words")
print("=============")

#print(word_counter[0:10])

#    #print(word_count[word])
#    if len(top10) < 10:
#        
#        top10.append(word)
#    
#    else:
#        
#        for topslot in top10:
#            
#            if word_count[topslot] > word_count[word]:
#                
#                break
#
#            else:
#                
#                top10.remove(topslot)
#                top10.append(word)                
#            
#print(top10)            
    
#    print("fuck this I'm out")
#        for topword in top10:
#            if word_count[topword] > word_count[word]:
#                print(top10)
#                top10.pop(topword)
#                top10.append(word)
#            else:
#            
#                break
#        
#
#        print(top10)        
        
## Don't worry about the underscore in front of _word_count
## It is just convention for internal use only
## More info here: https://dbader.org/blog/meaning-of-underscores-in-python
#
## Clean Punctuation
#_word_count = resume
## Hint: return only words that are not in string.punctuaton
## Hint: consider using a list comprehension
#
## Clean Stop Words
#stop_words = ["and", "with", "using", "##", "working", "in", "to"]
#word_count = word_count - punctuation
#
## Sort words by count and print the top 10
##sorted_words = []
##YOUR CODE HERE#
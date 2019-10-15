# -*- coding: UTF-8 -*-
"""PyParagraph Homework Solution."""

import re
import os

file_to_load = os.path.join("raw_data", "paragraph_1.txt")
file_to_output = os.path.join("paragraph_analysis.txt")

paragraph = ""

# Read the text file
with open(file_to_load) as txt_data:

    paragraph = txt_data.read().replace("\n", " ")

word_split = paragraph.split(" ")
print(word_split)
word_count = len(word_split)

letter_counts = []

for word in word_split:

    letter_counts.append(len(word))

avg_letter_count = sum(letter_counts) / float(len(letter_counts))

sentence_split = re.split("(?<=[.!?]) +", paragraph)
print(sentence_split)
sentence_count = len(sentence_split)

words_per_sentence = []

for sentence in sentence_split:

    words_per_sentence.append(len(sentence))
    
avg_word_sentence = sum(words_per_sentence) / float(len(words_per_sentence))
output = (
f"-------------------------\n"
f"Paragraph Analysis\n"
f"-------------------------\n"
f"Word Count: {word_count}\n"
f"Sentence Count: {sentence_count}\n"
f"Avg Word Length: {avg_letter_count} letters per word\n"
f"Avg Sentence Length: {avg_word_sentence} words per sentence\n"
f"-------------------------\n"
)

print(output)

with open(file_to_output, "w") as text_file:
    print(output, file=text_file)
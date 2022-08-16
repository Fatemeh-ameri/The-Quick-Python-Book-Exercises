"""LAB 8: REFACTOR WORD_COUNT Rewrite the word-count program from section
8.7 to make it shorter. You may want to look at the string and list operations
already discussed, as well as think about different ways to organize the code.
You may also want to make the program smarter so that only alphabetic
strings (not symbols or punctuation) count as words."""

import string
line_count = 0
word_count = 0
char_count = 0

infile = open('word_count.tst')
lines = infile.read().split("\n")
line_count = len(lines)   
for line in lines:
     lines =line.translate(str.maketrans('', '', string.punctuation))
     word_count += len(line.split())
     char_count += len(line)

print("this string has {0} lines and {1} words and {2} characters".format
(line_count, word_count, char_count))

   
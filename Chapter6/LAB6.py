import re
import string

with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        # make all one case
        line=line.lower()

        # remove punctuation
        line = re.sub(r'[^\w\s]', ' ', line)
        #line1 = line.translate(str.maketrans('', '', string.punctuation))

        # split into words
        line = line.split()

        # write all words for line
        line = "\n".join(line)
        print(line)
        outfile.write(line)
        
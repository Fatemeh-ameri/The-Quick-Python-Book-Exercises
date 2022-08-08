"""LAB 7: WORD COUNTING In the previous lab, you took the text of the first chap-
ter of Moby Dick, normalized the case, removed punctuation, and wrote the
separated words to a file. In this lab, you read that file, use a dictionary to
count the number of times each word occurs, and then report the most com-
mon and least common words."""

dic = {}
lis = []

with open("moby_01_clean.txt") as infile:
    for line in infile:
       lis.append(line.strip())
    for word in lis:
        dic[word] = dic.get(word, 0) + 1

most = max(dic, key=dic.get)
print(most)
#output: the

least = min(dic, key=dic.get)
print(least)
#output: call
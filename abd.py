from collections import Counter
def word_count(fname):
        with open(fname) as f:
            return Counter(f.read().split())

print("no. of words in a file:", word_count("abd.txt")) 

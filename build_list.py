from chemistrable import *

with open('words.txt','r') as words:
    with open('new_words.txt','w') as nw:
        for i,line in enumerate(words):
            combinations = chemistrable(line.strip())
            for combination in combinations:
                nw.write(stick_list(combination[0])+'\n')

from copy import deepcopy

CHEM_PATH = 'mendeleev.txt'

def get_elements():
    elements  = []
    with open(CHEM_PATH,'r') as mendv:
        for i,line in enumerate(mendv):
            elements.append(line.strip().upper())
    return elements


CHEM_ELEMENTS = get_elements()

def duplicate_combination(combinations,index):
    combinations.append(deepcopy(combinations[index]))
    return combinations

def explore(combinations,main_index,word):
    index = combinations[main_index][1]
    mendv = CHEM_ELEMENTS
    sym_one = False
    deadend_1 = False
    deadend_2 = False
    if word[index].upper() in mendv:
        combinations[main_index][0].append(word[index])
        combinations[main_index][1]+=1
        sym_one = True
    else:
       deadend_1 = True
    if index<len(word)-1 and word[index:index+2].upper() in mendv:
        if sym_one:
            combinations = duplicate_combination(combinations,main_index)
            combinations[-1][0][-1] = word[index:index+2]
            combinations[-1][1]+=1
        else:
            combinations[main_index][0].append(word[index:index+2])
            combinations[main_index][1]+=2
    else:
        deadend_2 = True
    if deadend_1 and deadend_2:
        try:
            del combinations[main_index]
        except:
            pass
    return combinations
    

def chemistrable(word):
    combinations = []
    combinations.append([[],0])

    end = False
    i = 0
 
    while i<len(combinations):
        if combinations[i][1]!=len(word):
            combinations = explore(combinations,i,word)
        else:
            i+=1
    i = 0
    while i<len(combinations):
        if len(combinations)==0:
            break
        if combinations[i][1]!=len(word):
            del combinations[i]
            i-=1
        i+=1
            
    return combinations  
            
        
if __name__=='__main__':

    word = input()
    combinations = chemistrable(word)
    if len(combinations) == 0:
        print("'"+word+"'"+' is not chemistrable!')
    else:
        for combination in combinations:
            print(combination[0])


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
    #print(combinations)
    return combinations

def explore(combinations,main_index,word):
    index = combinations[main_index][1]
    mendv = CHEM_ELEMENTS
    sym_one = False
    if word[index].upper() in mendv:
        combinations[main_index][0].append(word[index])
        combinations[main_index][1]+=1
        sym_one = True
        print(word[index]+' added to '+str(combinations)+' with '+str(sym_one))
    if index<len(word)-1 and word[index:index+2].upper() in mendv:
        if sym_one:
            combinations = duplicate_combination(combinations,main_index)
            combinations[main_index+1][0][-1] = word[index:index+2]
            combinations[main_index+1][1]+=1
            print(word[index:index+2]+' added to '+str(combinations))
        else:
            combinations[main_index][0].append(word[index:index+2])
            combinations[main_index][1]+=2
            print(word[index:index+2]+' added to '+str(combinations))
    return combinations
    

def chemistrable(word):
    combinations = []
    combinations.append([[],0])

    end = False
    i = 0
 
    while i<len(combinations):
        #print(i)
        if combinations[i][1]!=len(word):
            combinations = explore(combinations,i,word)
            '''
            if new_combinations == combinations:
                print('in')
                i+=1
            '''
        else:
            i+=1
    #print(combinations)
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
    #print(get_elements())
    '''combinations = []
    combinations.append([[],0])

    print(explore(combinations,0,'sarmg'.upper()))
    print(explore(combinations,0,'sarmg'.upper()))
    print(explore(combinations,0,'sarmg'.upper()))'''

    word = 'carbine'
    combinations = chemistrable(word)
    '''
    if len(combinations) == 0:
        print("'"+word+"'"+' is not chemistrable!')
    else:
        for combination in combinations:
            print(combination[0])
    
    '''

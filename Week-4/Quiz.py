# 1) Consider the following Python function.What does mystery([22,14,19,65,82,55]) return?

def mystery(l):
    if l == []:
        return(l)
    else:
        return(mystery(l[1:])+l[:1])


# Elements are moved from the beginning of the list to the end, so the list gets reversed.
# Accepted Answers:
# [55, 82, 65, 19, 14, 22]

# 2) What is the value of pairs after the following assignment?
pairs = [ (x,y) for x in range(4,1,-1) for y in range(5,1,-1) if (x+y)%3 == 0 ]

# All pairs (i,j) with i ∈ {4,3,2}, j ∈ {5,4.3,2} such that i + j is a multiple of 3,
# Accepted Answers:
# [(4, 5), (4, 2), (3, 3), (2, 4)]

# 3) Consider the following dictionary. Which of the following statements does not generate an error?
wickets = {"Tests":{"Kumble":[3,5,2,3],"Srinath":[4,4,1,0],"Prasad":[2,1,7,4]},"ODI":{"Kumble":[2,0],"Srinath":[1,2]}}
# wickets["ODI"]["Prasad"][0:] = [4,4],                         KeyError: 'Prasad'
# wickets["ODI"]["Prasad"] = wickets["ODI"]["Prasad"] + [4,4],  KeyError: 'Prasad'
# wickets["ODI"]["Prasad"].extend([4,4]),                       KeyError: 'Prasad'

# wickets["ODI"]["Prasad"] = [4,4], 
# {'Tests': {'Kumble': [3, 5, 2, 3], 'Srinath': [4, 4, 1, 0], 'Prasad': [2, 1, 7, 4]}, 'ODI': {'Kumble': [2, 0], 'Srinath': [1, 2], 'Prasad': [4, 4]}}

# Direct assignment to a new key adds a value. All other updates result in KeyError.
# Accepted Answers:
# wickets["ODI"]["Prasad"] = [4,4]

# 4) Assume that hundreds has been initialized as an empty dictionary:
hundreds = {}
# Which of the following generates an error?
# hundreds["Tendulkar, international"] = 100,        {'Tendulkar, international': 100}
# hundreds["Tendulkar"] = {"international":100},     {'Tendulkar':{'international':100}}
# hundreds[("Tendulkar","international")] = 100,     {('Tendulkar', 'international'): 100}
# hundreds[["Tendulkar","international"]] = 100,     Error

# Dictionary keys must be immutable values.
# Accepted Answers:
# hundreds[["Tendulkar","international"]] = 100
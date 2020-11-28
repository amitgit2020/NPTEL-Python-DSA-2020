# 1) Write a Python function frequency(l) that takes as input a list of integers and returns a pair of the form (minfreqlist,maxfreqlist) where

# minfreqlist is a list of numbers with minimum frequency in l, sorted in ascending order
# maxfreqlist is a list of numbers with maximum frequency in l, sorted in ascending order
# Here are some examples of how your function should work.

# >>> frequency([13,12,11,13,14,13,7,11,13,14,12])
# ([7], [13])

# >>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14])
# ([7], [13, 14])

# >>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7])
# ([7, 11, 12], [13, 14])

def frequency(l):
    dl1=set(l)
    dl=list(dl1)    
    newl=[]
    for i in dl:
        newl.append(l.count(i))
    mi=min(newl)
    ma=max(newl)
    mil=[]
    mal=[]
    for j in range(len(newl)):
        if newl[j]==mi:
            
            mil.append(dl[j])
        if newl[j]==ma:
           
            mal.append(dl[j])
    mil.sort()
    mal.sort()
    return(mil,mal)

# Instructor Solution
# def frequency(l):
#     count = {}
#     for n in l:
#         if n in count.keys():
#             count[n] = count[n]+1
#         else:
#             count[n] = 1
#     minlist = findmin(count)
#     maxlist = findmax(count)
#     return((minlist,maxlist))

# def findmin(d):
#     upperbound = 0
#     for n in d.keys():
#         if d[n] > upperbound:
#             upperbound = d[n]

#     minlist = []
#     mincount = upperbound

#     for n in d.keys():
#         if d[n] < mincount:
#             minlist = [n]
#             mincount = d[n]
#         elif d[n] == mincount:
#             minlist.append(n)
#     return(sorted(minlist))

            
# def findmax(d):
#     maxlist = []
#     maxcount = 0

#     for n in d.keys():
#         if d[n] > maxcount:
#             maxlist = [n]
#             maxcount = d[n]
#         elif d[n] == maxcount:
#             maxlist.append(n)
#     return(sorted(maxlist))

# 2) An airline has assigned each city that it serves a unique numeric code. It has collected information about all the direct flights it operates, represented as a list of pairs of the form (i,j), where i is the code of the starting city and j is the code of the destination.

# It now wants to compute all pairs of cities connected by one intermediate hope — city i is connected to city j by one intermediate hop if there are direct flights of the form (i,k) and (k,j) for some other city k. The airline is only interested in one hop flights between different cities — pairs of the form (i,i) are not useful.

# Write a Python function onehop(l) that takes as input a list of pairs representing direct flights, as described above, and returns a list of all pairs (i,j), where i != j, such that i and j are connected by one hop. Note that it may already be the case that there is a direct flight from i to j. So long as there is an intermediate k with a flight from i to k and from k to j, the list returned by the function should include (i,j). The input list may be in any order. The pairs in the output list should be in lexicographic (dictionary) order. Each pair should be listed exactly once.

# Here are some examples of how your function should work.

 
# >>> onehop([(2,3),(1,2)])
# [(1, 3)]

# >>> onehop([(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)])
# [(1, 2), (1, 3), (1, 4), (2, 1), (3, 2), (3, 4), (4, 2), (4, 3)]

# >>> onehop([(1,2),(3,4),(5,6)])
# []

# def onehop(l):
#     new=[]
#     l.sort()
#     for i in range(len(l)):
#         for j in range(len(l)):
#                 if l[i]!=l[j]:
#                     if l[i][1]==l[j][0]:
#                         q=l[i][0]
#                         w=l[j][1]
#                         if q!=w:
#                             t=[q,w]
#                             t=tuple(t)
#                             if t not in new:
#                                 new.append(tuple(t))
#     new.sort()
#     return (new)

# Instructor Solution

def onehop(l):
    direct = {}
    for (i,j) in l:
        if i in direct.keys():
            direct[i].append(j)
        else:
            direct[i] = [j]

    hopping = []

    for src in direct.keys():
        for dest in direct[src]:
            if dest in direct.keys():
                for remote in direct[dest]:
                    if src != remote:
                        hopping.append((src,remote))

    return(remdup(sorted(hopping)))
            
def remdup(l):
    if len(l) < 2:
        return(l)

    if l[0] != l[1]:
        return(l[0:1]+remdup(l[1:]))
    else:
        return(remdup(l[1:]))
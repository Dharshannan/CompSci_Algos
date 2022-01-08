strs = ["eat","tea","tan","ate","nat","bat"]
strs2 = []
for i in strs:
    a = "".join(sorted(i))
    strs2.append(a)
    
list1 = list(zip(strs,strs2))

fuck = []
for i in range(0,len(list1)):
    grps = [list1[i][0]]
    for j in range(i+1,len(list1)):
        if list1[i][1] == list1[j][1]:
            grps.append(list1[j][0])
            
    fuck.append(grps)

rem = []
for i in range(0,len(fuck)):
    for j in range(i+1,len(fuck)):
        for let in fuck[j]:
            if let in fuck[i]:
                rem.append(fuck[fuck.index(fuck[j])])
groups = [i for i in fuck if i not in rem]
print(groups)                




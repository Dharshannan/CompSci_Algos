strs = ["eat","tea","tan","ate","nat","bat"]  
dic = {}

for i in range(len(strs)):
    alphabetical = sorted(strs[i])
    joined = "".join(alphabetical)
    if joined in dic:
        dic[joined].append(strs[i])
    else:
        dic[joined] = [strs[i]]
print(dic)
final_lst = []
for lst in dic:
    final_lst.append(dic[lst])
    #print(dic[lst])
    
print(final_lst)
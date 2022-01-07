list1 = [1,2,3,4,4,3,2,1,3,4,5,6,1,1,2,3,4,5,4,3,2,9,10,11] # can work for both integer or string lists
n = len(list1)
list2 = []
for i in range(0,n):
    for j in range(i+1,n):
        if list1[i] == list1[j]:
            list2.append(list1[i:j+1])
            

anal = []
for item in list2:
    pali = []
    karma = []
    if (len(item)) % 2 != 0:
        mid = int((len(item)-1)/2)
        for (i,j) in zip(range(mid-1,-1,-1), range(mid+1,len(item))):
            if item[i] == item[j]:
                pali.append('true')
            else:
                pali.append('false')
    
    elif (len(item)) % 2 == 0:
        lmid = int(len(item)/2) - 1
        rmid = int(len(item)/2)
        for (i,j) in zip(range(lmid,-1,-1), range(rmid,len(item))):
            if item[i] == item[j]:
                pali.append('true')
            else:
                pali.append('false')
            
    for k in range(len(pali)):
        karma.append('true')
    if karma == pali:
        anal.append(item)

# Longest Palindrome possible in the list1

lenitem = []
for item in anal:
    lenitem.append(len(item))
if anal != []:
    for items in anal:
        maxlen = max(lenitem)
        if len(items) == maxlen:
            print(items)
else:
    print(anal)



                

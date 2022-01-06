import numpy as np
# 1st define the list of integers representing the poles
poles = [0,1,0,2,1,0,1,3,2,1,2,1]
rev_poles = poles[::-1] # reverse the poles list
# find the indexes of the maximum height of the poles
max_index = np.argmax(poles) 
max_index2 = np.argmax(rev_poles)
max2 = len(poles) - 1 - max_index2
list2 = poles[max_index:max2 + 1]

maxh = max(poles)
water = 0 # water unit
temp = 0 # temp to hold water unit
for i in range(0,len(poles)): #iterate through 1st list poles
    if poles[i] == maxh:
        break #if the value reaches the max height break the iteration
    else:
        if (poles[i] + temp) > poles[i+1]: # taking the fact, if the temp(previous water level) + current pole height is greater than the next pole height, add the water unit 
            water += poles[i] - poles[i+1] + temp # add water unit (simple maths right ;)
            temp = poles[i] - poles[i+1] + temp # update the temp
        else:
            temp = 0 # if pole current pole height < next pole, set temp back to 0
# Repeat for reversed list
temp1 = 0
for i in range(0,len(poles)):
    if rev_poles[i] == maxh:
        break
    else:
        if (rev_poles[i] + temp1) > rev_poles[i+1]:
            water += rev_poles[i] - rev_poles[i+1] + temp1
            temp1 = rev_poles[i] - rev_poles[i+1] + temp1
        else:
            temp1 = 0
# if the max height repeats, the water is collected between these highest poles using simple maths         
btw = 0
if len(list2) > 1:
    for i in range(1,len(list2)-1):
        btw += list2[i]
    water += maxh*(len(list2)-2) - btw
    
print(water)    



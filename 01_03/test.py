list_1 = [7,8,9,4,5,6,1,2,3]
temp = 0


for i in range(0,len(list_1)):
    for j in range(1+i,len(list_1)):
        if list_1[i] > list_1[j]:
            temp = list_1[j]
            list_1[j] = list_1[i]
            list_1[i] = temp

for i in list_1:
    print(i)
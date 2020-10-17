
list = [12,20,1,23,2,50,11,45]

for i in range(len(list)):
    j=i+1
    for j in range(len(list)):
        if list[i]>list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp

print(list)
'''for iter_num in range(len(list) - 1, 0, -1):
    for idx in range(iter_num):
        if list[idx] < list[idx + 1]:
            temp = list[idx]
            list[idx] = list[idx + 1]
            list[idx + 1] = temp
print(list)'''

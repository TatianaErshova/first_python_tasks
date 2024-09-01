
n1 = int(input("Enter lengh list1: "))
n2= int(input("Enter lengh list2: "))
list1= []
i = 0
while i < n1:
    list1.append(int(input("Enter data1: ")))
    i += 1
list2 = []
j = 0
while j < n2:
    list2.append(int(input("Enter data2: ")))
    j += 1
for i in list2:
    list1.append (i)
list1.sort()
print(list1)
list1 = list()
input1 = int(input())
integers = input().split()
for i in integers:
    list1.append(int(i))
print(hash(tuple(list1)))

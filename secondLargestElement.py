def secondLargestElement(arr):
    return sorted(set(arr))[-2]

array = []
n = int(input())
for i in range(0,n):
    ele = int(input())
    array.append(ele)

print(array)

print(secondLargestElement(array))
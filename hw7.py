import random
from random import shuffle
unsort_list = []
for i in range(1,21):
    unsort_list.append(i)

random.shuffle(unsort_list)
print(unsort_list)

def bubble_sort(unsort_list):
    length = len(unsort_list)
    for i in range(length):
        for j in range(0, length-i-1):
            if unsort_list[j] > unsort_list[j+1]:
                temp = unsort_list[j]
                unsort_list[j] = unsort_list[j+1]
                unsort_list[j+1] = temp
    return unsort_list

print(bubble_sort(unsort_list))

  #  2 part
val = int(input())
def binary_search(val,unsort_list):
    n = max(unsort_list)
    result = False
    first = 0
    last = n - 1
    while(first<last):
        middle = (first + last) // 2
        if val == unsort_list[middle]:
            first = middle
            last = first
            result = True
            pos = middle
        else:
            if val > unsort_list[middle]:
                first = middle + 1
            else:
                last = middle - 1
    else:
        if result == True:
            print(f'Элемент найден!\n{pos}')
        else:
            print(f'Элемент не найден!')

binary_search(val, unsort_list)
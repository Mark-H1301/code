import random
unsorted_array = [0]*1000

size = len(unsorted_array)

for x in range (0,size):
    unsorted_array [x] = random.randint(0,100000)
    print (unsorted_array [x])

notsort = 1

while(notsort == 1):
    notsort = 0
    for i in range (0,size-1):
        if (unsorted_array[i] > unsorted_array[i+1]):
            temp = unsorted_array[i]
            unsorted_array[i] = unsorted_array[i+1]
            unsorted_array[i+1] = temp
            notsort = 1

for x in range (0,size):
    print (unsorted_array [x])
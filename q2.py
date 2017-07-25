def binary(array,target,low,high):
    mid = (low + high) // 2
    if low > high:
        return "Not Found"
    elif array[mid] == target:
        return "Found"
    
    # array in NUMBERS.TXT is sorted according to descending order
    elif target < array[mid]:
        return binary(array,target,mid + 1,high)
    
    # target > array[mid]
    else:
        return binary(array,target,low,mid - 1)

def quicksort(array):
    if array == []:
        return []
    else:
        pivot = array[0]

        less = []
        equal = []
        more = []

        # allocating data into arrays by comparing to pivot
        for i in range(1,len(array)):
            if array[i] < pivot:
                less.append(array[i])
            elif array[i] == pivot:
                equal.append(array[i])
            else:
                more.append(array[i])

        less = quicksort(less)
        more = quicksort(more)

        # concatenate lists
        return less + [pivot] + equal + more
                
try:
    # open file
    infile = open("NUMBERS.TXT",'r')

    # read file
    lines = infile.readlines()

    # close file
    infile.close()

    array = []

    for line in range(len(lines)):
        lines[line] = lines[line].split()
        array.append(int(lines[line][2]))
    
    #2.1
    print(binary(array,500,0,19))
    #2.2
    print(quicksort(array))

except FileNotFoundError:
    print("NUMBERS.TXT not found.")
    

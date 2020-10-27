array = [5,7,9,0,3,1,6,2,4,8]

# Not In Place Sort
def notinplace_quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    temp = array[1:]

    left_array = [x for x in temp if x <= pivot]
    right_array = [x for x in temp if x > pivot]

    return notinplace_quick_sort(left_array) + [pivot] + notinplace_quick_sort(right_array)

# In Place Sort
def inplace_quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        #왼쪽에서부터 피벗보다 큰 데이터를 찾을때까지 반복
        while left <= end and array[pivot] >= array[left]:
            left += 1
        #오른쪽에서부터 피벗보다 작은 데이터를 찾을때까지 반복
        while right > start and array[pivot] <= array[right]:
            right -= 1
        #
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    inplace_quick_sort(array, start, right - 1)
    inplace_quick_sort(array, right + 1, end)

print("not in place :", notinplace_quick_sort(array))
inplace_quick_sort(array, 0, len(array)-1)
print("in place :",array)

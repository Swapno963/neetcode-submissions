def heepify(arr, n, i):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right


    if i != largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        heepify(arr, n, largest)

def heep_sort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heepify(arr, n, i)

    for end in range(n-1, -1, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heepify(arr, end, 0)
    return arr
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sorted_list = heep_sort(nums.copy())
        return sorted_list
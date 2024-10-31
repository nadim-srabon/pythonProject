def binary_search(arr,low,high,tar):
    if high < low:
        return -1

    mid = (low + high) // 2

    if arr[mid] == tar:
        return mid
    elif arr[mid] > tar:
        return binary_search(arr, low, mid - 1, tar)
    else:
        return binary_search(arr, mid + 1, high, tar)


arr = [2, 4, 6, 3, 8, 9]

n = len(arr)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array:", arr)

low = 0
high = n - 1
tar = 3

result = binary_search(arr, low, high, tar)

if result != -1:
    print(f"Target {tar} found at index {result}")
else:
    print("Target {tar} not found in any index")

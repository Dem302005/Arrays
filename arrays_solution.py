def findMaxConsecutiveOnes(nums):
    max_count = 0
    current_count = 0
    for num in nums:
        if num == 1:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    return max_count


def findNumbers(nums):
    count = 0
    for num in nums:
        digits = len(str(num))
        if digits % 2 == 0:
            count += 1
    return count


def sortedSquares(nums):
    return sorted([x * x for x in nums])


def duplicateZeros(arr):
    i = 0
    length = len(arr)
    while i < length:
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 2
        else:
            i += 1


def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
        
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


def removeDuplicates(nums):
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k


def checkIfExist(arr):
    seen = set()
    for num in arr:
        if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
            return True
        seen.add(num)
    return False


def validMountainArray(arr):
    if len(arr) < 3:
        return False
    i = 0
    n = len(arr)
    
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1
        
    if i == 0 or i == n - 1:
        return False
        
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1
        
    return i == n - 1


def replaceElements(arr):
    max_right = -1
    for i in range(len(arr) - 1, -1, -1):
        temp = arr[i]
        arr[i] = max_right
        if temp > max_right:
            max_right = temp
    return arr


def sortArrayByParity(nums):
    return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 != 0]


if __name__ == "__main__":
    print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
    print(findNumbers([12, 345, 2, 6, 7896]))
    print(sortedSquares([-4, -1, 0, 3, 10]))
    
    arr4 = [1, 0, 2, 3, 0, 4, 5, 0]
    duplicateZeros(arr4)
    print(arr4)
    
    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, 3, [2, 5, 6], 3)
    print(nums1)
    
    nums6 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k6 = removeDuplicates(nums6)
    print(k6, nums6[:k6])
    
    print(checkIfExist([10, 2, 5, 3]))
    print(validMountainArray([0, 3, 2, 1]))
    print(replaceElements([17, 18, 5, 4, 6, 1]))
    print(sortArrayByParity([3, 1, 2, 4]))
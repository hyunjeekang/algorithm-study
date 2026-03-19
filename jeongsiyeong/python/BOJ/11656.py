# 백준 11656번 - 접미사 배열
# https://www.acmicpc.net/problem/11656


def merge(left, right):
    merged = []
    l_idx, r_idx = 0, 0

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            merged.append(left[l_idx])
            l_idx += 1
        else:
            merged.append(right[r_idx])
            r_idx += 1
    merged.extend(left[l_idx:])
    merged.extend(right[r_idx:])

    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

s = input().strip()
strings = []

for i in range(len(s)):
    suffix = s[i:]
    strings.append(suffix)

strings = merge_sort(strings)

for string in strings:
    print(string)
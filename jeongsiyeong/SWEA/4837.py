# SWEA 4837 - 부분집합의 합
t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    numbers = list(range(1, 13))  # 1부터 12까지의 숫자 리스트
    count = 0
    length = len(numbers)

    # 모든 부분집합을 비트마스크로 생성
    for bitmask in range(1 << length):
        subset_sum = 0
        subset_size = 0
        
        for j in range(length):
            if bitmask & (1 << j):
                subset_sum += numbers[j]
                subset_size += 1
                
        if subset_size == n and subset_sum == k:
            count += 1
    print(f"#{test_case} {count}")
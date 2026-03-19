T = int(input())

def insert_heap(heap, num):
    heap.append(num)
    idx = len(heap) - 1

    while idx > 1:
        parent_idx = idx // 2

        if heap[parent_idx] > heap[idx]:
            heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
            idx = parent_idx
        else:
            break

for test_case in range(1, T+1):
    N = int(input())

    numbers = list(map(int, input().split()))
    
    heap = [0]

    for num in numbers:
        insert_heap(heap, num)

    ancestor_num = 0
    cur_node = N//2

    while cur_node > 0:
        ancestor_num +=heap[cur_node]
        cur_node //= 2
    
    print(f'#{test_case} {ancestor_num}')

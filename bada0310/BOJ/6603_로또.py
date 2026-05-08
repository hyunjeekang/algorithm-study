while True:
    try:
        arr = list(map(int,input().split()))

        N = arr[0]
        num_arr = arr[1:]
        res = []
        def comb(depth, start):
            if depth == 6:
                print(' '.join(map(str,res)))
                return
            
            for i in range(start,N):
                res.append(num_arr[i])
                comb(depth+1,i+1)
                res.pop()
        comb(0,0)
    except EOFError:
        break
    print()
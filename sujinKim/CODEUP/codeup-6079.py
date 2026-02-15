# n = int(input()) 
# total = 0 
# for i in range(n): 
#     total = total + i 
#     if total <= n: 
#         print(i-1)
      
            
      ###########사실 틀림....... 나 잘 모르겠삼      
		
	

n = int(input())
i = 0
total = 0

while total <= n:
    i = i + 1
    total = total + i
    

print(i)	


#즉, i=0이고 total=0이었는데 
#i = i+1 -> 0+1 =1 이 되고, 
# #total=0에서 0+1 =1이 되고,
# #1+1=2 < 10 이런식으로 하다가
# i=1+1=2, total=1+1 = 2 , 2+2 < 10
# i = 2+1 3 , total = 2+3 , 5+3<10
# i = 3+1 = 4 ,  total = 5+4 <10 그래서 i가 4번째 
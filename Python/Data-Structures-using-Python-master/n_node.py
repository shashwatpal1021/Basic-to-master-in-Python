

N = int(input("enter the value of N : ")) 
k1 = 1 - pow(N,N+1)
k2 = 1 - N
total = k1 / k2

res = total - (N+1)

res1 = res * 3

res2 = N * 10

final_result = res1 + res2

print(final_result)





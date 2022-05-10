N = int(input())

if N % 6 == 0:

    stairs = N // 6
    
    print("No of stairs : ", 22*stairs)

elif N % 2 == 0:

    print("No of stairs : " ,10*2 + N)

else:

    print("No of stairs : ",10*2+10+1)
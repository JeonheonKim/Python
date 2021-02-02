def solution(n):
    a0 = 0
    a1 = 1
    num = 1234567
    fibo = [a0,a1]
    if n < 2:
        return fibo % num
    else:
        for i in range(2,n+1):
            fibo.append(fibo[i-1] + fibo[i-2])
    
    return fibo[n] % num

n = int(input("N을 입력하세요 : "))
print(solution(n))
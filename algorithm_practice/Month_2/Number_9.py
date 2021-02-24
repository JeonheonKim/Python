def solution(n):
    ans = 0
    while True:
        m = n % 2
        if m == 0:
            n = n/2
        else:
            n -= 1
            ans += 1
        
        if n == 0: break


    return ans

n = 5
print(solution(n))
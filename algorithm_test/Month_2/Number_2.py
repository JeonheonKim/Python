def solution(n):

    cnt = 1
    if n == 1:
        return cnt
    else:
        for i in range(int(n/2+1),0,-1):
            sum_n = i
            for j in range(i-1,0,-1):
                sum_n += j 
                if sum_n == n:
                    cnt += 1
                    break
                elif sum_n > n:
                    break

    return cnt

n = 15
print(solution(n))
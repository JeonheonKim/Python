def solution(A,B):
   
    tot = 0

    while True:
        A.sort()
        B.sort(reverse=True)
        tot += A.pop(0)*B.pop(0)
        if len(A) == 0: break

    return tot


A = [1, 2]; B = [3, 4]
print(solution(A,B))

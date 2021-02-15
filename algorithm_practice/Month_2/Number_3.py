def solution(arr):
    div_n = max(arr)
    for i in range(div_n,0,-1):
        lst = [j % i for j in arr]        
        num = set(lst)
        if (len(num) == 1) & (list(num)[0] == 0):
            lst = [j // i for j in arr]
            a = 1
            for k in lst:
                a = a*k
            answer = i*a
            break         
    return answer


arr = [2,6,8,12]
print(solution(arr)) 
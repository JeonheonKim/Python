# 순열&조합 활용한 풀이
# 계산량이 많아 효율성 테스트 실패 
import itertools

def solution(n):
    result = 0
    num2 = 0
    while True:
        num1 = n- num2*2

        if num1 < 0: break

        jp1 = [1]*num1 + [2]*num2
        result += len(list(itertools.combinations(jp1,num2)))

        num2 += 1

    answer = result % 1234567
    return answer

# 피보나치 수열
def solution2(n):
    answer = 0
    lst = [0 for i in range(n + 1)]
    lst[0] = 1
    lst[1] = 2
    for i in range(2, n + 1) :
        lst[i] = (lst[i - 1] + lst[i - 2]) % 1234567
    answer = lst[n - 1] % 1234567
    return answer

n = 100
print(solution2(n))
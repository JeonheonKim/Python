def solution(s):
    s = s.split(" ")
    lst = list(map(int,s))
    answer = '{} {}'.format(min(lst),max(lst))
    return answer

s = "-1 -2 -3 -4"
print(solution(s))
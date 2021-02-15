def solution(brown, yellow):
    
    for i in range(1,yellow+1):
        if yellow % i == 0:
            edge = ((yellow // i) + i)*2 + 4
            if edge == brown:
                ga = (yellow // i) + 2
                se = i + 2
                break

    answer = [ga,se]

    return answer

brown = 24
yellow = 24
print(solution(brown, yellow))
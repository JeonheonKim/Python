def solution(genres, plays):
    d = {}
    for ger, play in zip(genres,plays):
        if ger in d:
            d[ger] += play
        else:
            d[ger] = play
    
    ger_max = sorted(d.items(),key = lambda x:x[1],reverse = True)
    ger_1st = []    
    ger_2nd = []
    for j,p in enumerate(plays):
        if genres[j] == ger_max[0][0]:
            ger_1st.append((j,p))
        elif genres[j] == ger_max[1][0]:
            ger_2nd.append((j,p))
        else:
            continue
    return list(map(lambda x:x[0],sorted(ger_1st,key = lambda x:x[1],reverse = True)))[:2] + list(map(lambda x:x[0],sorted(ger_2nd,key = lambda x:x[1],reverse = True)))[:2]


genres = ["jazz","classic", "pop", "classic", "classic", "pop","pop"]
plays = [500000, 500, 2500, 150, 600, 2500,2500]

print(solution(genres,plays))


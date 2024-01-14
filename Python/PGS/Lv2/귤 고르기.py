def solution(k, tangerine):
    answer = 0
    
    # 귤 개수 세기
    arr = {}
    for i in range(len(tangerine)):
        if tangerine[i] in arr:
            arr[tangerine[i]] += 1
        else:
            arr[tangerine[i]] = 1
    
    # 귤 개수 내림차순으로 정렬
    s_tangerine = sorted(arr.items(), key=lambda x: x[1], reverse=True)
    for t in s_tangerine:
        if k <= 0:
            break
        # 귤 개수 많은 것부터 가능한 종류 개수 더해주기    
        k -= t[1]
        answer += 1
    
    return answer
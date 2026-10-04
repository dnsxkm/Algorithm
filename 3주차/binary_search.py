def location(low, high, x, S) :
    if low > high :
        return -1

    mid = floor((low + high)/2) # 중간 인덱스 계산

    if x == S[mid]:
        return mid # 원소를 찾음
    elif x < S[mid]:
        return location(low, mid-1, x, S) # 중간 값보다 작으면 왼쪽 절반 탐색
    else :
        return location(mid+1, high, x, S) # 중간 값보다 크면 오른쪽 절반 탐색
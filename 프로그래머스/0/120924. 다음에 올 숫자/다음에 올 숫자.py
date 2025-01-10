def solution(common):
    if len(common) == 2:
        # 길이가 2일 경우, 두 값을 기반으로 공차 또는 공비를 구해서 다음 값 계산
        if common[1] - common[0] == common[0] - common[1]:
            # 등차수열
            return common[1] + (common[1] - common[0])
        else:
            # 등비수열
            return common[1] * (common[1] // common[0])
    else:
        if common[1] - common[0] == common[2] - common[1]:
            # 등차수열
            return common[-1] + (common[1] - common[0])
        else:
            # 등비수열
            return common[-1] * (common[1] // common[0])

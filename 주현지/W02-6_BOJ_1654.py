# https://www.acmicpc.net/problem/1654
# 1654 랜선 자르기
# 알고리즘: 이분탐색
# 핵심: 재귀 범위 설정 유의

import sys


def binary_search(start, end, target):  # target은 필요한 랜선 개수
    global max_len
    if start > end:
        return None
    mid = (start + end) // 2
    if mid == 0:  # 0으로 나누기 방지
        binary_search(mid + 1, end, target)
        return None

    cable_count = cut_cable(mid)
    if cable_count < target:
        binary_search(start, mid - 1, target)
    if cable_count >= target:
        if mid >= max_len:
            max_len = mid
        binary_search(mid + 1, end, target)


# 개수 파악
def cut_cable(a):
    count = 0
    # a는 자를 길이, 개수가 맞는지 확인해야할듯?
    for cable in cables:
        count += cable // a
    return count


input = sys.stdin.readline

k, n = map(int, input().split())

cables = []
for _ in range(k):
    cables.append(int(input()))

cables_total = sum(cables)
avg = cables_total // n

max_len = 0

low = 1
high = avg

binary_search(low, high, n)
print(max_len)

"""
N개 랜선
K개 랜선 가지고있음
길이 제각각
N개의 같은 길이의 랜선으로 -> K개 랜선 잘라서 만들어
길이는 상관없지만 N개를 만들어야돼
이미 가지고 있는 랜선의 길이 -> 센티미터 단위의 정수


최소값...

1. 최소막대기로 나눌수 있니?
2. 제일 큰 값을 반으로 나누고
아니 개수가 맞는지는 어떻게 알아야하지?
내가 어떻게 알아!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
딱 보면 모르나

우선 그 준 막대기 개수랑
필요한 막대기 수를 비교하는게 중요할 듯
아니 근데.. 어케알지..4322

막대기를 다 합해봐
합해서 필요한 필요한 막대기수만큼으로 나눠
그리고..?

아니 이것도 이분탐색인듯!!!!!
"""

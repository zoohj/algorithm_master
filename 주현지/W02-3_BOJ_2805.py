# https://www.acmicpc.net/problem/2805
# 2805 나무 자르기
# 알고리즘: 이분 탐색
# 핵심:

"""
n 나무의 수
m 필요한 나무 길이

나무 길이가 m보다 길때만 (나무길이 - m)만큼의 나무를 얻을 수 있음
최대값을 기준으로 하는게 나은지..
모든 나무들의 합 나누기 개수 /  평균을 구하고
settings: 평균 - (m / 나무 개수)
초기값일때 계산한 값 = cut_timber
if cut_timber < m:
    더 잘라야함
if cut_timber > n:
    설정값을 줄여야함 -> 하나씩 ->

    나무 정렬하고
    큰거랑 다음 작은거의 차만큼 잘라

    이분 탐색
언제 멈춰야할지를 모르겠는데..
종료조건이 개 어려움.. 생각이 안나

<흐름>
크면 올리고 작으면 내리자
하나씩 내릴까?
오래걸림
이분탐색으로 할까?
종료를 어떻게 하지?
종료말고 그냥 한바퀴 다 돌고 최댓값을 출력하자
"""

import sys

input = sys.stdin.readline

# n: 나무의 수 m: 목표 나무 길이
n, m = map(int, input().split())
trees = list(map(int, input().split()))


def cal_cut(mid) -> int:
    # 자른 나무 계산
    global trees
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    return total


def binary_search(target, start, end):
    global cutter_height
    if start > end:
        return None
    mid = (start + end) // 2
    cal = cal_cut(mid)
    if cal < target:
        binary_search(target, start, mid - 1)
    if cal >= target:
        cutter_height = mid
        binary_search(target, mid + 1, end)


low = 0
high = max(trees)
cutter_height = 0

binary_search(m, low, high)
print(cutter_height)

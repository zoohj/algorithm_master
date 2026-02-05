# https://www.acmicpc.net/problem/2805
# 2805 나무 자르기
# 알고리즘: 이분 탐색

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

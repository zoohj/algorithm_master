# https://www.acmicpc.net/problem/1463
# 1463 1로 만들기
# 알고리즘: DP
# 핵심: 점화식 규칙성 찾기, 조건부 갱신

'''
그리디 ❌ → DP ⭕

dp[i] = i를 1로 만드는 최소 연산 횟수
기본: dp[i] = dp[i-1] + 1
조건부 갱신:
i % 2 == 0 → dp[i//2] + 1
i % 3 == 0 → dp[i//3] + 1
'''

import sys
input = sys.stdin.readline

n = int(input()) 

dp = [0]* max(4, (n+1))  

dp[2]=1
dp[3]=1
for i in range(4,n+1):
    dp[i]= dp[i-1] + 1
    if i%3==0:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i%2==0:        
        dp[i] = min(dp[i],dp[i//2]+1)

print(dp[n])

# 3으로 나누기
# 2로 나누기
# 1 빼기

# count = 0
# n=o_n2

# while n != 1:
#     if n % 3 == 0:
#         count +=1
#         n = n//3
#     elif n % 2 == 0:
#         count +=1
#         n = n//2
#     else:
#         count +=1
#         n -= 1

# b_n= o_n-1
# before_count=0
# while b_n != 1:
#     if b_n % 3 == 0:
#         before_count +=1
#         b_n = b_n//3
#     elif b_n % 2 == 0:
#         before_count +=1
#         b_n = b_n//2
#     else:
#         before_count +=1
#         b_n -= 1


# print(max(before_count+1, count))



'''
X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.

연산을 사용하는 횟수의 최솟값

그냥 다해보고 최소값을 해야하나..??
dp 써야하나..?

1. 3으로 나눠떨어지면 나눠
2. 2로 나눠떨어지면 나눠

vs
dp[i-1]값 +1이랑 비교..?
'''

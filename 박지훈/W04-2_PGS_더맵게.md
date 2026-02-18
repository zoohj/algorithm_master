## pgs 더맵게 문제
https://school.programmers.co.kr/learn/courses/30/lessons/42626/solution_groups?language=python3&type=my

```
import heapq

def solution(scoville, K):
    answer = 0
    # 1. 기존 리스트를 '힙' 구조로 변환 (한 번만 하면 됨!)
    heapq.heapify(scoville)

    # 2. 가장 작은 값이 K보다 작고, 음식이 2개 이상일 때만 반복
    while scoville[0] < K:
        if len(scoville) < 2:
            break

        # 3. heappop으로 가장 작은 값 2개를 효율적으로 추출
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        answer += 1

    # 4. 루프가 끝났는데도 가장 작은 값이 K 미만이면 -1 반환
    return answer if scoville[0] >= K else -1
```

### 배운점
---
로직이 맞더라도 sort()를 사용하면 효율성 테스트를 통과하지 못함
## 문제 주소
* https://school.programmers.co.kr/learn/courses/30/lessons/132266?language=python3

## 문제 설명
* 스토리가 있는 다익스트라 문제.

## 풀이 과정
* 다익스트라를 구현하고 시작점은 강철부대의 지역으로 설정.
* 다익스트라 실행한 후에 강철부대의 지역에서 부대원 위치까지의 최단 경로를 각각 출력하면 끝.

## 로직
1. roads 값을 그래프에 입력.
2. destination = 강철부대의 지역(복귀 지점). 해당 변수를 다익스트라의 시작점으로 설정.
3. 다익스트라를 통해 시작점에서 모든 정점의 최단 경로를 구한 후 원하는 정점들의 거리를 하나 씩 확인.
4. 최단 경로를 리스트에 저장. 도달할 수 없으면 -1로 치환해서 저장 후 출력.

## 코드

```python
# https://school.programmers.co.kr/learn/courses/30/lessons/132266?language=python3
from collections import defaultdict
import heapq # 다익스트라는 힙큐를 써야 좀 더 빠르게 동작

def dijkstra(start, n, graph):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    
    pq = [(0, start)]
    
    while pq:
        cost, now = heapq.heappop(pq)
        
        if cost > dist[now]:
            continue
        for w, nxt in graph[now]:
            new_cost = cost + w
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))
    
    return dist

def solution(n, roads, sources, destination):
    answer = []
    
    # 그래프 양방향
    graph = defaultdict(list)
    
    for u, v in roads:
        graph[u].append((1, v))
        graph[v].append((1, u))
    
    dist = dijkstra(destination, n, graph)
    for target in sources:
        num = dist[target]
        
        if num == float('inf'):
            num = -1
            
        answer.append(num)
    return answer

```

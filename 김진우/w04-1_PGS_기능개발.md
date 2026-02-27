## 문제 주소
* https://school.programmers.co.kr/learn/courses/30/lessons/42586

## 문제 설명
* 작업과 작업이 진행되는 속도가 리스트 형태로 주어짐.
* 작업은 반드시 순서에 따라서 완료될 수 있음.
* 앞에 있는 작업이 배포되고, 뒤에 있는 작업도 배포될 수 있다면 한꺼번에 같이 배포한다.
* 각 배포마다 몇 개의 작업이 배포되는지 구해보자.
* 앞의 데이터가 나가기 전에는 뒤의 데이터는 아무 것도 못한다! queue를 활용하면 좋을 듯!

## 로직
1. 주어진 작업 리스트와 작업이 진행되는 속도 값을 가진 리스트를 deque로 변환.
2. 반복문에서는 queue의 맨 앞에 있는 데이터와 (현재 지난 시간 * 데이터의 작업 속도)를 더해서 작업이 완료되었는지 확인.
3. 작업이 완료된 경우, 맨 앞의 데이터를 큐에서 pop하고, complete_cnt 값을 + 1
4. 이러면 다음 반복에서 time 값이 +1 되기 전에 다시 2번부터 반복을 시작한다.
5. 그래서 다음에 queue의 가장 앞에 있는 데이터를 똑같이 확인하고, 이 데이터도 작업이 완료된 경우 다시 pop하고 complete_cnt 값에 + 1.
6. 작업이 마무리 되지 않은 데이터가 나오거나, 모든 데이터를 다 검사해서 while문이 끝날 때까지 반복하고, 맨 왼쪽의 데이터가 작업이 완료되지 않은 경우, 누적된 complete_cnt 값을 정답 리스트에 append 한 뒤에 0으로 초기화.
7. 이후 반복문이 종료되면 마지막으로 complete_cnt 값을 정답 리스트에 추가해주면 끝.

## 코드

```python
# https://school.programmers.co.kr/learn/courses/30/lessons/42586
from collections import deque

def solution(progresses, speeds):
    answer = []
    time = 1
    queue = deque(progresses)
    speed_queue = deque(speeds)
    # 기능이 몇 개가 한번에 배포될 것인지 저장.
    complete_cnt = 0
    # queue가 빌 때까지 반복.
    while queue:
        cur_data = queue[0]
        cur_speed = time * speed_queue[0]
        # 맨 앞의 작업이 완료된 경우.
        if cur_data + cur_speed >= 100:
            queue.popleft()
            speed_queue.popleft()
            complete_cnt += 1
        # 맨 앞의 작업이 완료되지 않은 경우
        else:
            time += 1
            # 만약, 앞에서 완료된 작업들이 있다면 answer에 추가하고 complete 값 초기화.
            if complete_cnt > 0:
                answer.append(complete_cnt)
                complete_cnt = 0
    
    # 맨 마지막 값은 queue가 비면 반복문이 종료됨.
    # 그래서 반복문 끝난 후 남아있을 마지막 complete 값을 추가해주자.
    answer.append(complete_cnt)
    
    return answer


```

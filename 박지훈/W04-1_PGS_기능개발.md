## pgs 기능개발 문제
https://school.programmers.co.kr/learn/courses/30/lessons/42586

```
def solution(progresses, speeds):
    answer = []
    days = []
    day = 0
    for i, j in zip(progresses, speeds):
        day = 0
        while i < 100:
            i += j
            day += 1
        days.append(day)

    max_day = days[0]
    count = 0

    for date in days:
        if date <= max_day:
            count += 1
        else:
            answer.append(count)
            count = 1
            max_day = date

    answer.append(count)
    return answer
```

다른 사람들의 풀이법
```
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
```

### 제미나이가 제시한 각 코드별 장단점
첫 번째 코드: 직관적 단계별 접근 (Iterative Approach)  
장점 :  
- 가독성(Readability): 로직이 사람이 생각하는 순서와 일치하여 코드를 처음 보는 사람도 바로 이해할 수 있음  
- 디버깅 용이성: days 리스트에 중간 결과값이 저장되므로, 어느 부분에서 계산이 틀렸는지 확인하기 쉬움  
- 유지보수성: 작업일 계산 방식이나 배포 조건을 수정해야 할 때 해당 부분만 골라 고치기 편함  

단점:  
- 시간 효율성: while 루프를 사용하기 때문에 진행률이 낮고 속도가 느린 경우 불필요한 연산이 반복  
- 공간 효율성: 모든 작업의 완료일을 담는 days 리스트를 추가로 생성하므로 메모리를 더 사용  

두 번째 코드: 수학적 압축 접근 (Mathematical & Compact Approach)  
장점:  
- 계산 효율성: while문 대신 음수 나눗셈(//)을 이용한 올림 테크닉을 써서 작업일을 한 번에 계산  
- 공간 효율성: 별도의 완료일 리스트를 만들지 않고 결과 리스트 Q에 직접 데이터를 쌓아 공간 낭비가 적음  
- 간결함: 코드가 짧고 파이썬의 리스트 컴프리헨션을 활용해 세련된 느낌을 줌  

단점:  
- 가독성 저하: -((p-100)//s) 같은 수학적 트릭은 직관적으로 무엇을 계산하는지 한눈에 알기 어려움  
- 데이터 구조의 복잡성: Q[-1][0] 처럼 중첩된 리스트 인덱스를 사용하므로 구조가 복잡해지면 실수가 생길 수 있음  
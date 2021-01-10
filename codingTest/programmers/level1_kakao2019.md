# 코테연습 2021-01-09

* https://programmers.co.kr/learn/courses/30/lessons/64061
* 2019 카카오 개발자 겨울 인턴십>크레인 인형뽑기 게임



* 

```python
def solution(board, moves):
    answer = 0
    busket = []
    
    for i in moves:
        for j in board:
            if j[i-1] == 0:
                continue
            else:
                busket.append(j[i-1])
                j[i-1] = 0 #여기에서 for문을 이용해서 j에 board의 값을 넣어도 j가 같은 주소를 가리키기 때문에 board의 값을 바꿀 수 있다.
                break
                
        if len(busket) >=2:
            if busket[-1] == busket[-2]: #busket리스트의 뒤쪽부터 참조할 때 리스트 범위를 넘어가면 에러가 발생하므로 len(busket)>=2를 if문 조건으로 주어서 에러를 막았다.
                busket.pop()
                busket.pop() #pop은 리스트의 마지막부터 터뜨려준다.
                answer += 2
                
                
    return answer
```


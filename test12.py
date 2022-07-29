#7월 28일 추가 실습 Q3

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        cnt = 0
        for j in range(1,i+1):
            if i%j == 0:
                cnt += 1
        if cnt%2:
            answer -= i
        else :
            answer += i
    return answer

left = 24
right = 27
answer = solution(left, right)
print(answer)
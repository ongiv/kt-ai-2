#7월 28일 추가 실습 Q6

def solution(n):
    for i in range(1,n+1):
        if i*i == n:
            return i+1
    return -1

n = int(input())
a = solution(n)
a*=a
print(a)
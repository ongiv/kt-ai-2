#7월 28일 추가 실습 Q2

n = int(input('입력 : '))

a = n//10
b = n%10

cnt = 0

while 1:
    temp = (b%10)*10+(a+b)%10
    cnt += 1
    if temp == n:
        print(cnt)
        break
    a = temp//10
    b = temp%10
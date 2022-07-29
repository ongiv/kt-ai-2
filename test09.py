#7월 28일 추가 실습 Q0

a= int(input('입력 : '))
b= int(input('입력 : '))

for i in range(min(a,b),1,-1):
    if a%i==0 and b%i==0:
        print(i)
        break
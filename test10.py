#7월 28일 추가 실습 Q1


a= int(input('입력 : '))
b= int(input('입력 : '))
i = max(a,b)
while 1:
    if i%a==0 and i%b==0:
        print(i)
        break
    i+=1
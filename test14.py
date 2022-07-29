#7월 28일 추가 실습 Q5
import re

score = input()
lenth = len(score)
numbers = re.findall(r'\d', score)
a=0
b=0
cnt=0

for j in numbers:
    i = int(j)
    cnt+=1
    if cnt<=lenth/2:
        a += i
    else :
        b += i
        
if a==b:
    print('LUCKY')
else :
    print('READY')
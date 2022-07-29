#7월 28일 추가 실습 Q4
import re
data = input('숫자로 이루어진 문자열을 입력하세요. ')

numbers = re.findall(r'\d', data)

flag = 1
for i in numbers:
    j = int(i)
    if flag:
        print(f'{j} ', end='') 
        result = j
        flag = 0
        continue
    if (j+result) > (j*result):
        print(f'+ {j} ', end='') 
        result += j
    else :
        print(f'* {j} ', end='') 
        result *= j
print(f'= {result}')
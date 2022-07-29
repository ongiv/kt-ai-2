#7월 28일 실습 4
from code import interact
import math

integer = int(input('입력 : '))
root_int = int(math.sqrt(integer))
              

for i in range(2,root_int+1):
    target = integer
    count = 0
    while target%i == 0 and target:
        target /= i
        count += 1
        if target == i:
            print(f'{i}**{count+1}')
            
            
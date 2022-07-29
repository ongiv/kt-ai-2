#7월 28일 실습 2

count = int(input('입력 : '))

for i in range(count):
    if i%2:
        print(f'+', end='')
    else :
        print(f'-', end='')
        
print()
        
for _ in range(count // 2): 
    print('+-', end='') 
rest = count % 2
if rest: 
    print('+', end='') # rest 값만큼 * 반복 출력
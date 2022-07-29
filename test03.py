#7월 28일 미니 실습 3
print('a부터 b까지 정수의 합을 구합니다.')

a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b:
    a, b = b, a #튜플로 취급되어 한번에 바뀜
    
sum = 0

for i in range(a, b): #리스트로 만들어 주는 함수
    print(f'{i} + ', end='') #줄바꿈 안하기 위함
    sum +=i
print(f'{b} = ', end='')
print(sum+b)
#7월 28일 미니 실습 1
def max4(a, b, c, d): 
    maxi = a
    if b > maxi:
        maxi = b 
    if c > maxi:
        maxi = c
    if d > maxi:
        maxi = d
    return maxi

a = int(input('정수 a의 값을 입력하세요.:'))
b = int(input('정수 b의 값을 입력하세요.:'))
c = int(input('정수 c의 값을 입력하세요.:'))
d = int(input('정수 d의 값을 입력하세요.:'))
print(f'최댓값은 {max4(a, b, c, d)}입니다')

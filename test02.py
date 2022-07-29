#7월 28일 미니 실습 2

def A_waterPay(litre):
    return litre*100

def B_waterPay(litre):
    if litre <= 50:
        return litre * 150
    elif litre >50:
        return 50*150+(litre-50)*75
    else:
        return 0
    
company = str(input('회사를 입력하시오.:'))
litre = int(input('수도 사용량을 입력하시오.:'))

if company == 'A':
     print(f'요금 : {A_waterPay(litre)}')
elif company == 'B':
    print(f'요금 : {B_waterPay(litre)}')
else :
    print('등록되지 않은 회사입니다.')
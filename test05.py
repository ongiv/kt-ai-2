#7월 28일 실습 1

def electricPay( kWh ):
    if kWh < 100:
        pay=410 + kWh*60.7
    elif kWh<=200:
        pay=910 + 100*60.7 + (kWh-100)*125.9
    else:
        pay=1600+100*60.7+100*125.9+(kWh-200)*187.9
        
    pay *= 1.137
    return int(pay)

kWh = int(input('입력 : '))
print(f'요금 : {electricPay(kWh)}')
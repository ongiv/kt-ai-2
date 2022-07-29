#7월 29일 미니 실습 1

def min_of(x):
    mini = x[0]
    for i in range(1, len(x)):
       if x[i]<mini:
           mini = x[i]
    return mini

t = (4,7,5.6,2,3.14,1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(min_of(t))
print(min_of(s))
print(min_of(a))

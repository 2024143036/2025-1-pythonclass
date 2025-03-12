#2025.03.12
#파이썬 수업 - 변수, 타입, 출력
#타입 (형) - 정수 :   int (intager)
#           실수 :   float (floating point)
#           문자열 : str (string)
#           논리값 : bool (boolean)

title="시간계산"
sec=3700
min=sec / 60
min=min>sec
print(sec, min)
print(type(title), type(sec), type(min))

a=int(10.999989)
b=float(10.3)
c=str (10.3)
print(type(a), type(b), type(c))
print(a)

sec1 = 3100;sec2=120

tf=100
tc=(tf-21)*5/9
print(f'{tf=} ===> {tc=}')

tc=37.7
tf=tc*9/5+32
print(f'{tc=} ===> {tf=}')

print(2**3,2**(1/2),2**(-1/2))

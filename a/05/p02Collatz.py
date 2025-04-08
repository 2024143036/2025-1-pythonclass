#2025.04.02 파이썬수업 프로젝트2
#콜라츠 추측, 또는 우박수
#1부터 1000까지 숫자 중 가장 많은 단계를 거쳐서 1로 가는 수는 무엇인가, 가장 많은 단계는 몇단계인가
#규칙 : n이 짝수 -> n/2
#      n이 홀수 -> 3n+1
#      예) 5 -> 16 -> 8 -> 4 -> 2 -> 1 (5단계)
# import random
#
# n=random.randint(1,100)
# a=1
#
# print('n : ',n)
# while n != 1:
#     if n%2==1:
#         print(a, '단계 n은 홀수 ', n)
#         n=3*n+1
#         a=a+1
#     else:
#         print(a,'단계 n은 짝수 ',n)
#         n=n/2
#         a=a+1
# print(a,'단계')

i=0
max=0
b=0
c=0
d=1

#while i<=100:

#   while n != 1:
#        if i%2==1:
#            d=3*d+1
#            b=b+1
#        else:
#            d=d/2
#            b=b+1
#        d=i
#        if max<b:
#            max=b
#            c=d
#print(d)

# 단계의 횟수를 셀것
# n을 1부터 99까지 변화하면서 각각의 단계수를 출력할것
# 그중 가장 큰 수를 찾을것
# n=97 : 118번만에 1로 도달
maxvalue=0
maxvaluen=0
thvalue=0
thvaluen=0
svalue=0
svaluen=0
a=0
for n in range(1,100):
    a=n
#    print(f'{n = }')
    ncount=0
    while n!=1:
        if n%2==1:
            n=3*n+1
        else:
            n=n/2
        ncount=ncount+1

#    print(f'{ncount}번 만에 1로 도착')
    if maxvalue<ncount:
        thvalue, thvaluen=svalue,svaluen
        svalue, svaluen=maxvalue,maxvaluen
        maxvalue,maxvaluen=ncount,a
    elif svalue<ncount:
        thvalue, thvaluen=svalue,svaluen
        svalue,svaluen=ncount,a
    elif thvalue<ncount:
        thvalue,thvaluen=ncount,a

print(f'{maxvalue = },{maxvaluen = }')
print(f'{svalue = },{svaluen = }')
print(f'{thvalue = },{thvaluen = }')



maxvalue1=-100
maxvalue2=-100
maxvaluen1=0
maxvaluen2=0

for n in range(1,100):
    a=n
#    print(f'{n = }')
    ncount=0
    while n!=1:
        if n%2==1:
            n=3*n+1
        else:
            n=n/2

        ncount=ncount+1

#    print(f'{ncount}번 만에 1로 도착')
    if maxvalue1 < ncount:
        maxvalue2, maxvalue1 = maxvalue1,ncount
        maxvaluen2,maxvaluen1=maxvaluen1,n
    elif maxvalue2<ncount:
        maxvalue2=ncount
        maxvaluen2=n

print(f'{maxvalue1 = },{maxvaluen1 = }')
print(f'{maxvalue2 = },{maxvaluen2 = }')



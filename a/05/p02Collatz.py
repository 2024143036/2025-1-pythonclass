#2025.04.02 파이썬수업 프로젝트2
#콜라츠 추측, 또는 우박수
#1부터 1000까지 숫자 중 가장 많은 단계를 거쳐서 1로 가는 수는 무엇인가, 가장 많은 단계는 몇단계인가
#규칙 : n이 짝수 -> n/2
#      n이 홀수 -> 3n+1
#      예) 5 -> 16 -> 8 -> 4 -> 2 -> 1 (5단계)
import random

n=random.randint(1,100)
a=1
m=0
b=0

print('n : ',n)
while n != 1:
    if n%2==1:
        print(a, '단계 n은 홀수 ', n)
        n=3*n+1
        a=a+1
    else:
        print(a,'단계 n은 짝수 ',n)
        n=n/2
        a=a+1
print(a,'단계')

i=0
while i<=100:
    if i%2==1:
        i=3*i+1
        b=b+1

    else:
        print(a,'단계 n은 짝수 ',n)
        i=i/2
        b=b+1




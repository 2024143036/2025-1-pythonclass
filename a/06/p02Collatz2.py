#2025.04.02 파이썬수업 프로젝트2
#콜라츠 추측, 또는 우박수
#1부터 1000까지 숫자 중 가장 많은 단계를 거쳐서 1로 가는 수는 무엇인가, 가장 많은 단계는 몇단계인가
#규칙 : n이 짝수 -> n/2
#      n이 홀수 -> 3n+1
#      예) 5 -> 16 -> 8 -> 4 -> 2 -> 1 (5단계)

#2025.04.09 우박수 프로젝트 2번째 : 기본 통계량 구하기
#numpy 배열, list 두가지 방식으로 시험
#구하는 통계량 : 평균, 중앙값, 표준편차
import numpy as np
import statistics
import time
maxnum=1000

from po2Collatzfunc import collatz

ncountl=[]
#
# for n in range(1,100):
#     i=n
#     ncount=0
#     while i!=1:
#         if i%2==1:
#             i=3*i+1
#         else:
#             i=i/2
#         ncount=ncount+1
#     print(f'{ncount}')
#     ncountl.append(ncount)
#
# print(ncountl)
# print(sum(ncountl)/len(ncountl))

#최대값, 평균, 중앙값, 표준편차, 최빈값
from collections import Counter

# def calculate_stats(ncountl):
#     if not ncountl:
#         return None
#
#     max_val = max(ncountl)
#     mean_val = round(statistics.mean(ncountl),5)
#     median_val = round(statistics.median(ncountl),5)
#     stdev_val = round(statistics.stdev(ncountl),5) if len(ncountl) > 1 else 0
#     mode_val = statistics.multimode(ncountl)  # 여러 개일 경우 모두 반환
#
#     return {
#         '최대값': max_val,
#         '평균': mean_val,
#         '중앙값': median_val,
#         '표준편차': stdev_val,
#         '최빈값': mode_val
#     }
# data = [1, 2, 2, 3, 4, 5, 5, 5]
#
# stats = calculate_stats(ncountl)
# for key, value in stats.items():
#     print(f"{key}: {value}")
#
# print(f'최대값 : {max(ncountl):.5f}')
# print(f'평균 : {statistics.mean(ncountl):.5f}')
# print(f'중앙값 : {statistics.median(ncountl):.5f}')
# print(f'최빈값 : {statistics.stdev(ncountl):.5f}')
# print(f'표준편차 : {statistics.mode(ncountl):.5f}')

start=time.time()

#numpy
ncounta=np.zeros(maxnum-1)

for n in range(1,maxnum):
    ncount=collatz(n)
    ncounta[n-1]=ncount

print(ncounta)

print(f'최대값 : {np.max(ncounta)}')
print(f'평균 : {np.mean(ncounta):.5f}')
print(f'중앙값 : {np.median(ncounta)}')
# print(f'최빈값 : {np.stdev(ncounta):.5f}')
# print(f'표준편차 : {np.mode(ncounta):.5f}')


end=time.time()
print(f'{end-start:.5f}초')


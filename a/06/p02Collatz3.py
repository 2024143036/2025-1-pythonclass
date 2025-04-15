
# 2025.04.02 파이썬수업 프로젝트2
# 콜라츠 추측, 또는 우박수
# 규칙 : n이 짝수 -> n/2, n이 홀수 -> 3n+1

# 2025.04.09 우박수 프로젝트 2번째 : 기본 통계량 구하기
# numpy 배열, list 두가지 방식으로 시험
# 구하는 통계량 : 평균, 중앙값, 표준편차, 최빈값
# 추가기능: 1~100 우박수 단계수 상위 3개 값과 해당 숫자 출력
# 커밋메시지: 빅3구하기

import numpy as np
import statistics
import time
from collections import Counter

def collatz(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

maxnum = 1000
ncountl = []

# 리스트 방식 계산
for n in range(1, maxnum):
    ncount = collatz(n)
    ncountl.append(ncount)

# 리스트 방식 통계량 계산
def calculate_stats(ncountl):
    if not ncountl:
        return None
    max_val = max(ncountl)
    mean_val = round(statistics.mean(ncountl), 5)
    median_val = round(statistics.median(ncountl), 5)
    stdev_val = round(statistics.stdev(ncountl), 5) if len(ncountl) > 1 else 0
    mode_val = statistics.multimode(ncountl)
    return {
        '최대값': max_val,
        '평균': mean_val,
        '중앙값': median_val,
        '표준편차': stdev_val,
        '최빈값': mode_val
    }

# 리스트 결과 출력
print("=== 리스트 방식 통계량 ===")
stats = calculate_stats(ncountl)
for key, value in stats.items():
    print(f"{key}: {value}")

# 리스트 방식 빅3
print("\n=== 리스트 방식 빅3 (1~100) ===")
big3_list = sorted([(n, collatz(n)) for n in range(1, 101)], key=lambda x: x[1], reverse=True)[:3]
for i, (num, steps) in enumerate(big3_list, 1):
    print(f'{i}위: 숫자 {num}, 단계수 {steps}')

# numpy 방식 시간 측정
start = time.time()

# numpy 배열 계산
ncounta = np.zeros(maxnum - 1)
for n in range(1, maxnum):
    ncount = collatz(n)
    ncounta[n - 1] = ncount

print("\n=== numpy 방식 통계량 ===")
print(f'최대값 : {np.max(ncounta)}')
print(f'평균 : {np.mean(ncounta):.5f}')
print(f'중앙값 : {np.median(ncounta)}')
print(f'표준편차 : {np.std(ncounta):.5f}')

most_common = Counter(ncounta).most_common()
max_count = most_common[0][1]
modes = [val for val, count in most_common if count == max_count]
print(f'최빈값 : {modes}')

# numpy 방식 빅3
print("\n=== numpy 방식 빅3 (1~100) ===")
temp_arr = np.array([collatz(n) for n in range(1, 101)])
big3_np_idx = temp_arr.argsort()[::-1][:3]
for i, idx in enumerate(big3_np_idx, 1):
    print(f'{i}위: 숫자 {idx+1}, 단계수 {int(temp_arr[idx])}')

end = time.time()
print(f'\n실행 시간: {end - start:.5f}초')

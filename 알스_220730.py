# 220730
# SWEA_D2
# 1984. 중간 평균값 구하기

# 10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램
# 소수점 첫째 자리에서 반올림한 정수 출력

for t in range(1, int(input())+1):
    N = sorted(map(int, input().split()))       # 숫자 받아서 정렬
    ans = N[1:9]                                # 최대 수, 최소 수 제외한 수들 모음
    
    print(f'#{t} {round(sum(ans)/len(ans))}')   # 평균값 구하고 소수점 첫째 자리에서 반올림
        

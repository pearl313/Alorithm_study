# 220801
# SWEA_D3
# 113229. 일요일

# 문자열 S는 오늘의 요일을 나타냄
# S는 “MON”(월), “TUE”(화), “WED”(수), “THU”(목), “FRI”(금), “SAT”(토), “SUN”(일) 중 하나
# 내일 이후의 가장 빠른, 다음 일요일까지 며칠 남았는지 출력

for t in range(1, int(input())+1):
    S = input()     # S 입력
    day_dict = {'MON': 1, 'TUE': 2, 'WED': 3, 'THU': 4, 'FRI': 5, 'SAT': 6, 'SUN': 7} # 각 요일별로 숫자 지정
    
    if S == 'SUN':          # SUN만 다음 일요일까지 7
        print(f'#{t} 7')
    else:
        ans = day_dict['SUN'] - day_dict[S]     # 입력받은 S에 해당하는 숫자 가져와서 계산
        print(f'#{t} {ans}')
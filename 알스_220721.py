# 220721
# SWEA_D1
# 2056. 연월일 달력

# 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어짐.
# 22220228 -> 2222/02/28
# 해당 날짜의유효성 판단 후, 날짜가 유효하면 YYYY/MM/DD 형식으로 출력
# 유효하지 않으면, -1을 출력하는 프로그램 작성.

# 연월일로 구성된 입력에서 월은 1~12 사이의 값
# 일은 1일 ~ 각 달에 해당하는 날짜까지의 값을 가져야함.

#31 : 1,3,5,7,8,10,12
#30 : 4,6,9,11
#28 : 2

T = int(input())        #날짜 입력할 횟수 입력

date = []       #빈 리스트 만들기
for tt in range(1, T+1):
    num = input()       #날짜 입력
    
    if (int(num[4:6]) in [1,3,5,7,8,10,12]) and (int(num[6:8]) in range(1,32)):
        date.append(f'#{tt} {num[:4]}/{num[4:6]}/{num[6:8]}')       #빈 리스트에 넣기

    elif (int(num[4:6]) in [4,6,9,11]) and (int(num[6:8]) in range(1,31)):
        date.append(f'#{tt} {num[:4]}/{num[4:6]}/{num[6:8]}')

    elif (int(num[4:6]) == 2) and (int(num[6:8]) in range(1,29)):
        date.append(f'#{tt} {num[:4]}/{num[4:6]}/{num[6:8]}')

    else:
        date.append(f'#{tt} -1')

for i in date:
    print(i) #한꺼번에 주르륵 출력


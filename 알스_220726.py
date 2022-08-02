# 220726
# SWEA_D2
# 1945. 간단한 소인수분해

# 숫자 N이 주어질 때,
# N=2a x 3b x 5c x 7d x 11e
# 여기서 a,b,c,d,e를 출력하라.

# 가장 첫줄에는 테스트 케이스 개수 T가 주어지고
# 그 아래로 각 테스트 케이스가 주어진다.


T = int(input())                        # 테스트 케이스 입력
#ls_1 = []                     
for t in range(1, T+1):     
    N = int(input())                    # 각 테스트에서 실행할 값 입력
    a, b, c, d, e = 0, 0, 0, 0, 0
    ls_2 =[]

    #if N % 2 == 0:
    while N % 2 == 0:
        N = N // 2
        a += 1
    ls_2.append(a)

    #if N % 3 == 0:
    while N % 3 == 0:
        N = N // 3
        b += 1
    ls_2.append(b)

    #if N % 5 == 0:
    while N % 5 == 0:
        N = N // 5
        c += 1
    ls_2.append(c)        

    #if N % 7 == 0:
    while N % 7 == 0:
        N = N // 7
        d += 1
    ls_2.append(d)     
   
    #if N % 11 == 0:
    while N % 11 == 0:
        N = N // 11
        e += 1
    ls_2.append(e)

    print('#{t}', end=' ')
    print(*ls_2)        
    #ls_1.append(ls_2)    

#for j in range(len(ls_1)):
    #print(f'#{j + 1}', end=' ')
    #print(*ls_1[j])
# for j in ls_1:                            # 리스트에 넣어준 결과값
    # print(f'#{}', end = ' ')
    # print(*j)                           # 하나씩 출력   
        

    #print('#{t}', end=' ')
    print('#{t}', *ls_2)
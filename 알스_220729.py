# 220729
# SWEA_D2
# 2005. 파스칼의 삼각형

# 크기가 N인 파스칼의 삼각형을 만들어야함
# 첫 번째 줄은 항상 숫자 1
# 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성
# N을 입력 받아 크기가 N인 파스탈의 삼각형을 출력하는 프로그램 작성

'''
for t in range(1, int(input())+1):
    ans = []
    for n in range(1, int(input())+1):
        if n >= 3:
            for i in range(n-1):  
                ans.insert(1, (str(ans[i] + ans[i+1])*(n-2)))
            print(*ans)
        else:
            ans.append(1)
            print(*ans)
'''






for t in range(1, int(input())+1):  # 테스트 케이스 입력
    ans = []                            # 전체 결과 담을 리스트
    for n in range(int(input())):           # 입력한 숫자만큼 반복
        change = []                             # n을
        for i in range(n+1):                    # 0부터 n까지 반복
            if i == 0 or i == n:                # 앞과 뒤는 무조건 1
                change.append(1)
            else:
                change.append(ans[n-1][i-1] + ans[n-1][i])  # 맨 앞, 뒤가 아닌 수는 위의 두 수의 합
        ans.append(change)          # 리스트 change를 다시 ans에 넣어줌
    print(f'#{t}')
    for j in ans:           # ans에 담겨있는 change를 하나씩 출력 (리스트 안에 리스트)
        print(*j)
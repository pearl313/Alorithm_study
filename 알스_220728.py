# 220728
# SWEA_D1
# 14553. Game Money

# N명의 사람이 게임을 하는데, 한 판에 두 사람이 참여함
# 두 사람은 각자 1원씩 게임 머니를 내야함
# 주어진 게임 머니를 통해 최대 몇 게임을 할 수 있는지 계산하기

# N은 최대 20, 초기 게임 머니는 최대 100



T = int(input())

for t in range(1, T+1):
    N = int(input())
    N_ls = sorted(map(int, input().split()))    # 숫자 받아서 정렬
    game_n = 0
    while N_ls[-1] > 0 and N_ls[-2] > 0:        # 큰 수 두 개끼리 먼저 게임 시작, 둘 다 돈이 있어야 가능
        N_ls[-1] -= 1                           # 1원씩 사용
        N_ls[-2] -= 1
        game_n += 1                             # 둘 다 1원씩 사용하면 게임 수 증가
        N_ls.sort()                             # 다시 정렬해서 큰 수 갱신
    print(f'#{t} {game_n}')

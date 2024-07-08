import sys
input = sys.stdin.readline

n, m = int(input().split())
graph = [list(map(int, input().split())) for _ in range]
# 한 턴에 하나 또는 두 명의 플레이어 움직일 수 있음
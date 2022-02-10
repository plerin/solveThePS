from collections import deque


def bfs(i, j, k):
    q = deque([(i, j, k)])

    if box[i][j][k] != 1:
        return

    while q:
        i, j, k = q.popleft()

        for r in range(6):
            dh, dn, dm = dz[r]+i, dy[r]+j, dx[r]+k
            if dh < 0 or dh >= h or dn < 0 or dn >= n or dm < 0 or dm >= m:
                continue
            if box[dh][dn][dm] == 0:
                box[dh][dn][dm] = box[i][j][k]+1
                q.append((dh, dn, dm))
    return


box = []
ret = 0
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [-1, 1, 0, 0, 0, 0]

m, n, h = map(int, input().split())

for i in range(h):
    tray = [list(map(int, input().split())) for _ in range(n)]
    box.append(tray)

for i in range(h):
    for j in range(n):
        for z in range(m):
            bfs(i, j, z)

max_v = 0
for i in range(h):
    for j in range(n):
        for z in range(m):
            if box[i][j][z] == 0:
                print(-1)
                exit()
            max_v = max(box[i][j][z], max_v)

print(max_v-1) if max_v != 1 else print(0)
# max_v = max(map(max, map(max, box)))

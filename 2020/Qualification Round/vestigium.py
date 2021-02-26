T = int(input())

for t in range(1, T+1):
    N = int(input())
    k, r, c = 0, 0, 0
    matrix = [[e for e in map(int, input().split())] for _ in range(N)]

    for n in range(N):
        k += matrix[n][n]
        r += len(matrix[n]) != len(set(matrix[n]))
        column = [matrix[j][n] for j in range(N)]
        c += len(column) != len(set(column))
    
    print(f"Case #{t}: {k} {r} {c}")
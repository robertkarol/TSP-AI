def find(x, tree):
    if tree[x] == x:
        return x
    tree[x] = find(tree[x], tree)
    return tree[x]

def merge(x, y, tree):
    tree[find(x, tree)] = find(y, tree)

def mst(dist):
    ms_tree = []
    dist.sort(key=lambda x : x[2])
    tree = [i for i in range(0, N+1)]
    for e in dist:
        x = e[0]
        y = e[1]
        if not find(x, tree) == find(y, tree):
            ms_tree.append(e)
            merge(x, y, tree)
    return ms_tree

def bfs_mst(start, mst):
    queue = [start]
    #print(mst)
    visited = []
    while len(queue):
        curr = queue.pop()
        visited.append(curr)
        for i in range(N, 0, -1):
            if ((curr, i, V[curr - 1][i - 1]) in mst or (i, curr, V[i - 1][curr - 1])in mst)  and i not in visited:
                queue.append(i)
    return visited

def tsp():
    dist = [(i + 1, j + 1, V[i][j]) for i in range(N) for j in range(N) if not i == j]
    ms_tree = mst(dist)
    return bfs_mst(1, ms_tree)

def tsp2():
    sol = [1]
    while len(sol) < N:
        cand = -1
        Min = 2**64
        for i in range(0, N):
            if (V[sol[len(sol) - 1] - 1][i] < Min and i + 1 not in sol):
                Min = V[sol[len(sol) - 1] - 1][i]
                cand = i + 1
        sol.append(cand)
    return sol

def cost(sol):
    if len(sol) == 0:
        return 0
    s = 0
    for i in range(1,len(sol)):
        s += V[sol[i]-1][sol[i-1]-1]
    return s + V[sol[len(sol)-1]-1][sol[0]-1]

def solve():
    global N, V
    N = 0
    V = dist = []
    with open("input.txt", "r") as f:
        N = int(f.readline())
        for i in range(N):
            try:
                V.append(list(map(float, f.readline().strip().split(','))))
            except ValueError:
                pass

    solution1 = tsp()
    solution = solution2 = tsp2()
    if cost(solution1) < cost(solution2):
        solution = solution1
    with open("output.txt", "w") as f:
        out = ",".join(map(str, solution))
        f.write(str(len(solution)) + "\n")
        f.write(out + "\n")
        f.write(str(cost(solution)))

solve()
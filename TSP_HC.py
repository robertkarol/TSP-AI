import random

def neighbours(sol, j):
    '''
    l = [sol[0:j-1] + sol[j:i] + [sol[j-1]] + sol[i:] for i in range(j, N+1) if sol[0:j-1] + sol[j:i] + [sol[j-1]] + sol[i:] not in used]
    used.extend(l)
    print(sol)
    '''
    l = []
    for i in range(2, N):
        c = [] + sol
        c[j], c[i] = c[i], c[j]
        if c not in used:
            l.append(c)
    used.extend(l)

    return l

def cost(sol):
    if len(sol) == 0:
        return 0
    s = 0
    for i in range(1,len(sol)):
        s += V[sol[i]-1][sol[i-1]-1]
    return s + V[sol[len(sol)-1]-1][sol[0]-1]

def tsp():
    x = [i for i in range(1, N + 1)]
    k = 0
    j = 1
    while j < N:
        print(cost(x))
        k += 1
        n = neighbours(x, j)
        if len(n) == 0:
            j += 1
            continue
        min_n = min(n, key = lambda a : cost(a))
        if cost(min_n) >= cost(x):
            j += 1
            continue
        x = min_n
    print(k)
    return x


def solve():
    global N
    N = 0
    global V
    V = []
    global used
    used = []
    with open("input.txt", "r") as f:
        N = int(f.readline())
        for i in range(N):
            try:
                V.append(list(map(float, f.readline().strip().split(','))))
            except ValueError:
                pass
    solution = tsp()
    with open("output.txt", "w") as f:
        out = ",".join(map(str, solution))
        f.write(str(len(solution)) + "\n")
        f.write(out + "\n")
        f.write(str(cost(solution)))

solve()

def neighbours(sol):
    l = [sol + [i] for i in range(1, N+1) if i not in sol]
    return l

def cost(sol):
    if len(sol) == 0:
        return 0
    s = 0
    for i in range(1,len(sol)):
        s += V[sol[i]-1][sol[i-1]-1]
    return s + V[sol[len(sol)-1]-1][sol[0]-1]

def tsp():
    S = []
    sol = [1]
    q = [sol]
    while(len(q) > 0):
        curr = q.pop()
        if len(curr) == N and (cost(curr) < cost(S) or len(S) == 0):
            S = curr
            #print(S)
        n = neighbours(curr)
        q.extend(n)
    return S

def solve():
    global N
    N = 0
    global V
    V = []
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



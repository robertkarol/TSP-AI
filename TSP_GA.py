import numpy

def cost(sol):
    if len(sol) == 0:
        return 0
    s = 0
    for i in range(1,len(sol)):
        s += V[sol[i]-1][sol[i-1]-1]
    return s + V[sol[len(sol)-1]-1][sol[0]-1]

def init_population(popSize):
    p = [i for i in range(2, N+1)]
    pop = []
    for i in range(0, popSize):
        pp = numpy.random.permutation(p)
        pop.append([[1] + pp.tolist(), 0])
    return pop


def eval_population(population, popSize):
    for i in population:
        i[1] = cost(i[0])
    population.sort(key = lambda i : i[1])
    #print("aa", population, population[0:popSize], popSize)
    return population[0:popSize]


def select_parent(population):

    totalCost = 0
    for i in population:
        totalCost += i[1]
    selection = [i[1] / totalCost for i in population]
    selection.reverse()
    selection = numpy.cumsum(selection)
    p = numpy.random.random()
    i = 0
    while i < len(selection) and p > selection[i]:
        i += 1
    #print(selection, p, i)
    return population[i - 1]


def crossover(parent1, parent2):
    child = [parent2[0][i - 1] for i in parent1[0]]
    return [child, 0]


def mutate(child):
    pos1 = numpy.random.randint(1, len(child[0]))
    pos2 = numpy.random.randint(1, len(child[0]))
    child[0][pos1], child[0][pos2] = child[0][pos2], child[0][pos1]


def best_individual(population):
    return population[0][0]


def tsp(noGenerations, popSize):
    #print(initPopulation(10))
    population = init_population(popSize)
    while noGenerations > 0:
        population = eval_population(population, popSize)
        #print(population)
        #print(cost(best_individual(population)))
        children = []
        size = popSize
        while size > 0:
            parent1 = select_parent(population)
            parent2 = select_parent(population)
            child = crossover(parent1, parent2)
            #print(child)
            mutate(child)
            #print(child)
            #print(parent1, parent2, child)
            children.append(child)
            size -= 1
        #print(children)
        population.extend(children)
        noGenerations -= 1
    eval_population(population, popSize)
    return best_individual(population)

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
    solution = tsp(5000,25)
    with open("output.txt", "w") as f:
        out = ",".join(map(str, solution))
        f.write(str(len(solution)) + "\n")
        f.write(out + "\n")
        f.write(str(cost(solution)))

solve()
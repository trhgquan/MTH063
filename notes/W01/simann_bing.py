from numpy import arange
from numpy.random import rand
from numpy.random import choice
from numpy import exp
from numpy import log
from numpy import argmin
from numpy import asarray

# objective function
def objective(x, coeffs):
    return coeffs.dot([x**i for i in range(len(coeffs))])

# simulated annealing algorithm
def simulated_annealing(objective, bounds, n_iterations, step_size, temp):
    # generate an initial point
    best = None
    for i in range(100):
        x = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
        score = objective(x)
        if best is None or score < best[1]:
            best = [x, score]
    # run the algorithm
    scores = list()
    solutions = list()
    current = best
    for i in range(n_iterations):
        # take a step
        candidate = None
        while candidate is None or any(candidate < bounds[:, 0]) or any(candidate > bounds[:, 1]):
            candidate = current[0] + rand(len(bounds)) * step_size - step_size / 2.0
        # evaluate candidate point
        candidate_score = objective(candidate)
        scores.append(candidate_score)
        solutions.append(candidate)
        # check if we should keep it
        diff = candidate_score - current[1]
        if exp(-diff / temp) > rand():
            current = [candidate, candidate_score]
        # cool temperature
        temp *= 0.9999
    # return the best solution found
    ix = argmin(scores)
    return [solutions[ix], scores[ix]]

# define range for input
bounds = asarray([[-5.0, 5.0]])

# define the problem
coeffs = asarray([1, -3, 2])
n_iterations = 10000
step_size = 0.1
temp = 10

# solve the problem using simulated annealing
best, score = simulated_annealing(objective, bounds, n_iterations, step_size, temp)

# report solution
print('f(%s) = %f' % (best, score))
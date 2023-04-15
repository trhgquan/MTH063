import math
import random

def simulated_annealing():
    # Define initial state
    x = 0.0
    y = x ** 2 - 4 * x + 5
    
    # Define initial temperature and cooling rate
    temp = 1000.0
    cooling_rate = 0.03
    
    # Define minimum temperature to stop annealing
    min_temp = 0.001
    
    # Loop until minimum temperature is reached
    while temp > min_temp:
        # Choose a new candidate state
        x_new = x + random.uniform(-1, 1)
        y_new = x_new ** 2 - 4 * x_new + 5
        
        # Calculate energy difference between current and new state
        delta_e = y_new - y
        
        # If new state is better, accept it
        if delta_e < 0:
            x = x_new
            y = y_new
        # If new state is worse, accept it with a probability based on temperature
        else:
            acceptance_prob = math.exp(-delta_e / temp)
            if random.random() < acceptance_prob:
                x = x_new
                y = y_new
        
        # Reduce temperature
        temp *= 1 - cooling_rate
    
    return x, y

if __name__ == "__main__":
    x, y = simulated_annealing()
    print(f"f({x}) = {y}")
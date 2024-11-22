import numpy as np

# Define probabilities
P_A = {True: 0.8, False: 0.2}
P_C = {True: 0.5, False: 0.5}
P_G_given_A_C = {
    (True, True): {True: 0.9, False: 0.1},
    (True, False): {True: 0.7, False: 0.3},
    (False, True): {True: 0.6, False: 0.4},
    (False, False): {True: 0.3, False: 0.7}
}

P_J_given_G = {
    True: {True: 0.8, False: 0.2},
    False: {True: 0.2, False: 0.8}
}

P_S_given_G = {
    True: {True: 0.7, False: 0.3},
    False: {True: 0.3, False: 0.7}
}

# Monte Carlo simulation to estimate P(J=True | A, C)
def monte_carlo_simulation(num_samples=5):
    count_job_given_aptitude_coding = 0
    count_aptitude_coding = 0
    
    for _ in range(num_samples):
        A = np.random.rand() < P_A[True]
        
        C = np.random.rand() < P_C[True]
        
        G = np.random.rand() < P_G_given_A_C[(A, C)][True]
        
        J = np.random.rand() < P_J_given_G[G][True] 
        if A and C:
            count_aptitude_coding += 1
            if J:
                count_job_given_aptitude_coding += 1
    
    # Calculate conditional probability
    if count_aptitude_coding == 0:
        return 0  # Avoid division by zero
    return count_job_given_aptitude_coding / count_aptitude_coding

# Run simulation
num_samples = 5  # You can adjust the number of samples here
estimated_probability = monte_carlo_simulation(num_samples)
print(f"Estimated P(J=True | A=True, C=True): {estimated_probability:.4f}")
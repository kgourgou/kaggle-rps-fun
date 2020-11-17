
from numpy import zeros
from numpy.random import choice

e_minus_2 = None
e_minus_1 = None
A = zeros([3,3]) # P(e_minus_1 | e_minus_2) = A[e1,e2]

def markov_agent(observation, configuration):
    global A
    global e_minus_2
    global e_minus_1

    STEPS = 100
    
    if observation.step > 0:
        e_minus_1 = observation.lastOpponentAction
    
    if observation.step < STEPS:
        answer = int(choice([0,1,2]))
        if observation.step > 1:
            A[e_minus_1, e_minus_2] = A[e_minus_1, e_minus_2] + 1
            
        e_minus_2 = e_minus_1 
    else:
        if sum(A[e_minus_1,:]) == 0:
            return int(choice([0,1,2]))
        
        probs = A[e_minus_1,:]/sum(A[e_minus_1,:])
        next_move_prediction = int(choice([0,1,2],p = probs))
        answer = ((next_move_prediction + 1) % configuration.signs)
    
    return answer

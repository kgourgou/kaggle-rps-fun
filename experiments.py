from kaggle_environments import make, evaluate

env = make("rps")

standard_agents = [k for k in env.agents]
standard_agents.append('shift_agent.py')
standard_agents.append('random_agent.py')

target_agent = "markov_agent.py"
print(f'target_agent = {target_agent}')
for k in standard_agents:
    print(f'versus {k}')
    print(evaluate("rps",[target_agent,k], 
        configuration={"episodeSteps": 1000}))


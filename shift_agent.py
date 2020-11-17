
from kaggle_environments.envs.rps.utils import get_score
last_react_action = 0

def shift_agent(observation, configuration):
    global last_react_action
    if observation.step < 100:
        last_react_action = 0
    else:
        if get_score(last_react_action, observation.lastOpponentAction) <= 1:
            last_react_action = (observation.lastOpponentAction + 1)  % configuration.signs

    return last_react_action

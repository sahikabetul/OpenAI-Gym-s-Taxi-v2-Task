import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6, epsilon=0.003, alpha=0.35, gamma=0.99):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
       
    def update_Q_expsarsa(self, Q, nA, state, action, reward, next_state, i_episode):
        """Returns updated Q-value for the most recent experience."""
        
        policy_s = np.ones(nA) * self.epsilon / nA  
        policy_s[np.argmax(self.Q[state])] += 1 - self.epsilon 
 
        return self.alpha * (reward + self.gamma * np.sum(self.Q[next_state] * policy_s)  - self.Q[state][action])

    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        policy_s = np.ones(self.nA) * self.epsilon /self.nA
        policy_s[np.argmax(self.Q[state])] += 1 - self.epsilon
        
        return np.random.choice(self.nA, p = policy_s)

    def step(self, state, action, reward, next_state, done, i_episode):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        self.Q[state][action] += self.update_Q_expsarsa(self.Q, self.nA, state, action, reward, next_state, i_episode)
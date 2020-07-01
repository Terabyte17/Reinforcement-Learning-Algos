import gym
import itertools
import matplotlib
import numpy as np
import pandas as pd
import sys
if "../" not in sys.path:
	sys.path.append("../")
from collections import defaultdict
from windy_gridworld import WindyGridworldEnv
import plotting

matplotlib.style.use('ggplot')

env=WindyGridworldEnv()

def make_epsilon_greedy_policy(Q,epsilon,nA):
	def policy_fn(observation):
		policy=(np.ones(nA,dtype=float)/nA)*epsilon
		best_action=np.argmax(Q[observation])
		policy[best_action]+=1-epsilon			#defining epsilon-greedy policy
		return policy
	return policy_fn
	
def sarsa(env, num_episodes, discount_factor=1.0, alpha=0.5, epsilon=0.1):
	
	Q=defaultdict(lambda: np.zeros(env.action_space.n))	
	
	policy=make_epsilon_greedy_policy(Q,epsilon,env.action_space.n)
	
	stats = plotting.EpisodeStats(episode_lengths=np.zeros(num_episodes),episode_rewards=np.zeros(num_episodes))
	
	for episode in range(num_episodes):
		done=False
		state=env.reset()
		probs=policy(state)
		action=np.random.choice(np.arange(len(probs)),p=probs)
		while done is False:
			next_state,reward,done,_=env.step(action)
			probs=policy(next_state)
			next_action=np.random.choice(np.arange(len(probs)),p=probs) #choosing next action by using our policy
			Q[state][action]+=alpha*(reward+discount_factor*Q[next_state][next_action]-Q[state][action])  #SARSA(0)
			#Backward Sarsa(lambda) can also be implemented for better results
			state=next_state
			action=next_action
			stats.episode_rewards[episode]+=reward      
			stats.episode_lengths[episode]+=1
	return Q,stats
	
Q,stats=sarsa(env, 200)
plotting.plot_episode_stats(stats)

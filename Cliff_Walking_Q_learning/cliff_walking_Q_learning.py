import gym
import numpy as np
import sys
import matplotlib
if "../" not in sys.path:
	sys.path.append("../")
from collections import defaultdict
from cliff_walking import CliffWalkingEnv
import plotting

matplotlib.style.use('ggplot')

env=CliffWalkingEnv()

def make_epsilon_greedy_policy(Q,epsilon,nA):
	def policy_fn(observation):
		policy=(np.ones(nA,dtype=float)/nA)*epsilon
		best_action=np.argmax(Q[observation])
		policy[best_action]+=1-epsilon  #defining epsilon-greedy policy
		return policy
	return policy_fn
	
def greedy_policy(Q,observation):
	return np.argmax(Q[observation])  #choosing best action as our alternate action
	
def q_learning(env, num_episodes, discount_factor=1.0, alpha=0.5, epsilon=0.1):
	
	Q=defaultdict(lambda: np.zeros(env.action_space.n))
	
	stats=plotting.EpisodeStats(episode_lengths=np.zeros(num_episodes),episode_rewards=np.zeros(num_episodes))
	
	mu_policy=make_epsilon_greedy_policy(Q,epsilon,env.action_space.n)
	
	for episode in range(num_episodes):
		done=False
		state=env.reset()
		probs=mu_policy(state)
		action=np.random.choice(np.arange(len(probs)),p=probs)
		while done is False:
			next_state,reward,done,_=env.step(action)
			probs=mu_policy(next_state)
			next_action=np.random.choice(np.arange(len(probs)),p=probs) #next action to take
			alternate_action=greedy_policy(Q,next_state) #finding alternate action which gives best action value function
			Q[state][action]+=alpha*(reward+discount_factor*Q[next_state][alternate_action] - Q[state][action])
			#off-policy learning
			state=next_state
			action=next_action
			stats.episode_rewards[episode]+=reward
			stats.episode_lengths[episode]+=1
		
	return Q,stats
	
Q,stats=q_learning(env,500)
plotting.plot_episode_stats(stats)

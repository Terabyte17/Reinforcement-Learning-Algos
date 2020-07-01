import gym
import matplotlib
import numpy as np
import sys
if "../" not in sys.path:
	sys.path.append("../")
from collections import defaultdict
from blackjack import BlackJackEnv
import plotting
matplotlib.style.use('ggplot')

env=BlackJackEnv()

def sample_policy(observation):
	score,dealer_score,usable_ace=observation
	return 0 if score>=20 else 1

def mc_prediction(policy,env,num_episodes,discount_factor=1.0):
	
	returns_sum=defaultdict(float)   
	returns_count=defaultdict(float)
	
	V=defaultdict(float)
	
	for episode in range(num_episodes):
		episodes=[]
		state=env.reset()
		for t in range(100):
			action=sample_policy(state)
			next_state,reward,done,_=env.step(action)
			episodes.append((state,action,reward))    #for each episode we store, the state-action-reward for each timestep
			state=next_state
			if done:
				break
				
		states_in_episode=set(tuple(x[0]) for x in episodes)  #set of unique states in episode
		for state in states_in_episode:
			for i in range(len(episodes)):
				if episodes[i][0]==state:
					first_occurence=i	#finding first occurrence of each state in episode
					break
			a=0	
			G=0 #First Visit Monte Carlo Return for each state in the episode
			for j in range(first_occurence,len(episodes)):
				G+=(discount_factor**a)*episodes[j][2]
				a+=1
			returns_sum[state]+=G
			returns_count[state]+=1.0
			V[state]=returns_sum[state]/returns_count[state]   #calculating value function
			
	return V
	
V_10k=mc_prediction(sample_policy,env,num_episodes=10000) 
plotting.plot_value_function(V_10k,title="10,000 steps")
 #running large number of episodes gives approximate value function when following sample policy
 
 
			
			
	

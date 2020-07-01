import gym 
import numpy as np
import sys
import matplotlib
if "../" not in sys.path:
	sys.path.append("../")
import plotting
from blackjack import BlackJackEnv
from collections import defaultdict

env=BlackJackEnv()

#in model-free control, we don't have model of the environment and hence have to use action value function instead of value function

def make_epsilon_greedy_policy(Q,epsilon,nA):    
	def policy_fn(observation):
		policy=(np.ones(nA,dtype=float)/nA)*epsilon     
		best_action=np.argmax(Q[observation])
		policy[best_action]+=1-epsilon       #defining epsilon-greedy policy
		return policy
	return policy_fn
	
def MC_control_epsilon_greedy_policy(env, num_episodes, discount_factor=1.0, epsilon=0.1):
	
	returns_count=defaultdict(float)
	
	Q=defaultdict(lambda: np.zeros(env.action_space.n))
	
	policy=make_epsilon_greedy_policy(Q,epsilon,env.action_space.n)
	
	for episode in range(num_episodes):
		episodes=[]
		state=env.reset()
		for t in range(100):
			probs=policy(state)
			action=np.random.choice(np.arange(len(probs)),p=probs)  #randomly choosing an action based on the probabilities
			next_state,reward,done,_=env.step(action)
			episodes.append((state,action,reward))
			if done is True:
				break
			state=next_state
		
		sa_pair_in_episode=set([(tuple(x[0]),x[1]) for x in episodes])  #set of all unique - state-action pairs
		for state,action in sa_pair_in_episode:
			sa_pair=(state,action)
			for i in range(len(episodes)):
				if episodes[i][0]==state and episodes[i][1]==action:
					first_occurrence=i				#finding first occurrence in episode
					break
			G=0
			a=0
			for j in range(first_occurrence,len(episodes)):     #finding total return
				G+=(discount_factor**a)*episodes[j][2]
				a+=1
			
			returns_count[sa_pair]+=1	
			
			Q[state][action]+=(G-Q[state][action])/returns_count[sa_pair]	#incremental update in Q after every episode
			#incremental updates help in decreasing storage complexity			
			
	return	Q,policy
	
Q, policy= MC_control_epsilon_greedy_policy(env, num_episodes=500000, epsilon=0.1)

V=defaultdict(float)
for state,actions in Q.items():     #creating value function from action-value function by assigning the greedy action value
	action_value=np.max(actions)
	V[state]=action_value
	
plotting.plot_value_function(V,title='optimal_value_function')

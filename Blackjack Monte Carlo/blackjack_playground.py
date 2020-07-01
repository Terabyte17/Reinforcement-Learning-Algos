import numpy as np
import sys
if "../" not in sys.path:
	sys.path.append("../")
from blackjack import BlackJackEnv

env=BlackJackEnv()

def print_observation(observation):
	score,dealer_score,usable_ace=observation
	print("Score: - " + str(score))
	print("Dealer Score: - " + str(dealer_score))
	print("Usable Ace " + str(usable_ace))

def policy(observation):
	score,dealer_score,usable_ace=observation
	return 0 if score>=20 else 1
	
for episode in range(20):		#number of episodes
	observation=env.reset()
	for t in range(100):		#100 is set to ensure that enough steps take place and each episode terminates
		print_observation(observation)
		action=policy(observation)
		print("Taking action: {}\n".format(["Stick","Hit"][action]))
		observation,reward,done,_=env.step(action)
		if done:
			print_observation(observation)
			print("Game end. Reward: " + str(reward))
			break

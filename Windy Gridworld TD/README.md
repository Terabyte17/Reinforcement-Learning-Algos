# Solving Windy-GridWorld via SARSA(0)
## SARSA(0)
SARSA is a control algorithm based on Temporal Difference Learning. There are variations to SARSA - SARSA(0), Forward-View SARSA(lambda), Backward-View SARSA(lambda). In this repo, SARSA(0) has been used to solve the Windy GridWorld Environment. SARSA(lambda) can also be implemented to give better results.

## Windy GridWorld Environment
				. 	. 	. 	. 	. 	. 	. 	. 	. 	.

				. 	. 	. 	. 	. 	. 	. 	. 	. 	.

				. 	. 	. 	. 	. 	. 	. 	. 	. 	.

				S 	. 	. 	. 	. 	. 	. 	G 	. 	.

				. 	. 	. 	. 	. 	. 	. 	. 	. 	.

				. 	. 	. 	. 	. 	. 	. 	. 	. 	.

				. 	. 	. 	. 	. 	. 	. 	. 	. 	.

				. 	. 	. 	. 	. 	. 	. 	. 	. 	.

				. 	. 	. 	. 	. 	. 	. 	. 	. 	.

				. 	. 	. 	. 	. 	. 	. 	. 	. 	.

				0 	0 	0 	1 	1 	1 	2 	2 	1 	0
The Windy GridWorld environment is a variation of the GridWorld Environment, and in this there are 2 points S-starting and G-goal. The aim is to move the player/agent from the starting to the goal in the least number of timesteps possible. However, in each of the columns there is a wind factor involved. i.e. when moving to a new column, the position will be affected by the wind in that column(mentioned in the last row of the grid). This wind is acting upwards in the gridworld affecting the movement of the agent.

## Results
Episode Length (number of timsteps it takes) - This shows that as the algorithm sees more episodes it starts converging to an optimal value function and hence the timesteps required to complete the task decreases
<p align="center">
 <img  width="800" height="400" src="https://github.com/Terabyte17/Reinforcement-Learning-Algos/blob/master/Windy%20Gridworld%20TD/Media/Episode_length.png">
</p>

Episode Reward - This shows that as the algorithm sees more episodes it starts converging to an optimal value function and hence the reward the agent get increases
<p align="center">
 <img  width="800" height="400" src="https://github.com/Terabyte17/Reinforcement-Learning-Algos/blob/master/Windy%20Gridworld%20TD/Media/Episode_Reward.png">
</p>

Episodes per TimeStep - This shows that as the algorithm sees more episodes it starts converging to an optimal value function and hence later epsiodes take lesser timsteps
<p align="center">
 <img  width="800" height="400" src="https://github.com/Terabyte17/Reinforcement-Learning-Algos/blob/master/Windy%20Gridworld%20TD/Media/Ep_timesteps.png">
</p>


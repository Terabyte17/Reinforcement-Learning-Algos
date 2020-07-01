# Solving Cliff Walking via Q-learning
## Q-learning
Q-learning is an efficient off-policy control algorithm in Reinforcement Learning. It is a form of SARSA(0) but the target is a little bit different. It is the basis of the deep reinforcemenent learning algorithm DQN which has been widely used in this field.

## Cliff Walking Environment
<p align="center">
 <img  width="800" height="250" src="https://github.com/Terabyte17/Reinforcement-Learning-Algos/blob/master/Cliff_Walking_Q_learning/Media/cliff_walking.png">
</p>
The Cliff Walking Environment problem consists of a grid with some grid cells defined as Cliffs and hence walking into them will cause termination of the episode. The goal of the agent is to reach from the starting point to the target point without going into the cliff and accomplishing this task in the minimum timesteps possible. 

## Results
Episode Length (number of timsteps it takes) - This shows that as the algorithm sees more episodes it starts converging to an optimal value function and hence the timesteps required to complete the task decreases
<p align="center">
 <img  width="800" height="400" src="https://github.com/Terabyte17/Reinforcement-Learning-Algos/blob/master/Cliff_Walking_Q_learning/Media/episode_length.png">
</p>

Episode Reward - This shows that as the algorithm sees more episodes it starts converging to an optimal value function and hence the reward the agent get increases
<p align="center">
 <img  width="800" height="400" src="https://github.com/Terabyte17/Reinforcement-Learning-Algos/blob/master/Cliff_Walking_Q_learning/Media/episode_reward.png">
</p>

Episodes per TimeStep - This shows that as the algorithm sees more episodes it starts converging to an optimal value function and hence later epsiodes take lesser timsteps
<p align="center">
 <img  width="800" height="400" src="https://github.com/Terabyte17/Reinforcement-Learning-Algos/blob/master/Cliff_Walking_Q_learning/Media/ep_timesteps.png">
</p>

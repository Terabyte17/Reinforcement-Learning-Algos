# Solving BlackJack Environment via First Visit Monte Carlo
## First Visit Monte Carlo
The First Visit Monte Carlo is a model free prediction and control algorithm that can be used for solving many reinforcement learning problems. Another implementation of the Monte Carlo is the Every Visit Monte Carlo. Here, the blackjack environment has been solved using the first visit Monte Carlo approach.

## BlackJack Environment
The BlackJack environment is a classic implementation of the famous game BlackJack. In it, there are 2 players - a player and a dealer, and both of them draw cards from a shuffled deck. The main motive of the game is to get a higher sum on the cards than the opponent, but keeping the total sum less than 21. The player can see only 1 card of the dealer and can decide to stick(stop taking cards) or twist(take another card). If the sum of the player's cards goes above 21, the player is busted and the dealer wins. Same goes for the dealer. The one with the highest sum at the end wins. There is also the case of having a Usable Ace, that is the Ace can be used as 1 or 11 by the player.
In our implementation, the dealer always follows the policy of twisting if his sum is less than 17, and sticking otherwise. This is obviously not apparent to the player/agent as we our implementing a model free problem.

## Policy Evaluation (Prediction)
The First Visit Monte Carlo prediction algorithm has been implemented in the MC_prediction.py script and it evaluates the value function for a given policy. The policy that the agent/player follows in this script is: - Twist if sum < 20; stick otherwise


## Results
#### Value Function Prediction (No Usable Ace)                                                   
<p align="center">
 <img  width="800" height="400" src="https://github.com/Terabyte17/Reinforcement-Learning-Algos/blob/master/Blackjack%20Monte%20Carlo/Media/MC_eval_1.png">
</p>

#### Value Function Prediction (Usable Ace)                                                   
<p align="center">
 <img  width="800" height="400" src="https://github.com/Terabyte17/Reinforcement-Learning-Algos/blob/master/Blackjack%20Monte%20Carlo/Media/MC_eval_2.png">
</p>

#### Optimal Value Function (No Usable Ace)                                                   
<p align="center">
 <img  width="800" height="400" src="https://github.com/Terabyte17/Reinforcement-Learning-Algos/blob/master/Blackjack%20Monte%20Carlo/Media/MC_optimal_1.png">
</p>

#### Optimal Value Function (Usable Ace)                                                   
<p align="center">
 <img  width="800" height="400" src="https://github.com/Terabyte17/Reinforcement-Learning-Algos/blob/master/Blackjack%20Monte%20Carlo/Media/MC_optimal_2.png">
</p>
                                  

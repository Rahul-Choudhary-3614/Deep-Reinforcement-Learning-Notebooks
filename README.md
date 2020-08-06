![Alt Text](https://j.gifs.com/OMBMLr.gif)          ![Alt Text](https://j.gifs.com/r848Vp.gif)


# Deep-Reinforcement-Learning-Notebooks
This Repository contains a series of google colab notebooks which I created to help people dive into deep reinforcement learning.This notebooks contains both theory and implementation of different algorithms. 

Following is the content of the Notebooks of till now:
1) The first Notebook provides with the introduction of Deep Reinforcement Learning. 

2) The second Notebook is most basic policy based algorithm called REINFORCE.The Notebook is about the theory behind the REINFORCE algorithm, disadvantages of using Reinforce Algorithm and its few remedies. Environment used  here is CartPole-v1

3) The third Notebook is most basic value based algorithm called SARSA. The Notebook starts with providing the definitions about value functions, temporal difference learning. Then we talk about Epsilon- greedy policy. Using all these we talk SARSA and its implementation.Environment used  here is CliffWalking

4) The fourth Notebook is another value based algorithm called Deep Q-Networks algorithm(DQN). The Notebook starts with providing how DQN is better than SARSA. Then we talk about a Boltzmann exploration which is bit better than epsilon- greedy policy. At last we talk how DQN improves on the sample efficiency of SARSA with the help of experience replay memory. Combining all these we implement DQN.Environment used  here is Assault-v0

5) The fifth Notebook is a bit advance value based algorithm called Double DQN with Prioritized Experience Replay(PER) and target networks.This Notebook talks about some problems we have while using the Deep Q-Networks algorithm (DQN) and how we can improve DQN. This Notebook introduces concept of target network, double dqn and Prioritized Experience Replay and how we can combine them to make DQN more stable and efficient.Environment used  here is KungFuMaster-v0

6) The sixth Notebook is an algorithm called Advantage Actor-Critic (A2C) which elegantly combine the policy gradient and a learned value function. This Notebook starts with providing the concept of advantage function and various methods of estimating advantage. Then we discuss the implementation of A2C. In the code I have also written about how add regularisation in Actor model with the help of entropy of policy

![Alt Text](https://j.gifs.com/OMBMLr.gif)          ![Alt Text](https://j.gifs.com/r848Vp.gif)

![Alt Text](https://github.com/Rahul-Choudhary-3614/Deep-Reinforcement-Learning-Notebooks/blob/master/Demos/pusher.gif)

![Alt Text](https://github.com/Rahul-Choudhary-3614/Deep-Reinforcement-Learning-Notebooks/blob/master/Demos/cartpole.gif)

![Alt Text](https://github.com/Rahul-Choudhary-3614/Deep-Reinforcement-Learning-Notebooks/blob/master/Demos/Pendulum-v0.gif)

![Alt Text](https://github.com/Rahul-Choudhary-3614/Deep-Reinforcement-Learning-Notebooks/blob/master/Demos/Ant.gif)

![Alt Text](https://github.com/Rahul-Choudhary-3614/Deep-Reinforcement-Learning-Notebooks/blob/master/Demos/Half-Cheetah.gif)

![Alt Text](https://github.com/Rahul-Choudhary-3614/Deep-Reinforcement-Learning-Notebooks/blob/master/Demos/Car.gif)

![Alt Text](https://github.com/Rahul-Choudhary-3614/Deep-Reinforcement-Learning-Notebooks/blob/master/Demos/Doom_Death_Match.gif)

![Alt Text](https://github.com/Rahul-Choudhary-3614/Deep-Reinforcement-Learning-Notebooks/blob/master/Demos/bowling_result.gif)

# Deep-Reinforcement-Learning-Notebooks
This Repository contains a series of google colab notebooks which I created to help people dive into deep reinforcement learning.This notebooks contains both theory and implementation of different algorithms. 

Following is the content of the Notebooks of till now:
1) The first Notebook provides with the introduction of Deep Reinforcement Learning. 

2) The second Notebook contains the most basic policy based algorithm called REINFORCE.The Notebook is about the theory behind the REINFORCE algorithm, disadvantages of using Reinforce Algorithm and its few remedies. Environment used  here is CartPole-v1

3) The third Notebook contains the most basic value based algorithm called SARSA. The Notebook starts with providing the definitions about value functions, temporal difference learning. Then we talk about Epsilon- greedy policy. Using all these we talk SARSA and its implementation.Environment used  here is CliffWalking

4) The fourth Notebook contains another value based algorithm called Deep Q-Networks algorithm(DQN). The Notebook starts with providing how DQN is better than SARSA. Then we talk about a Boltzmann exploration which is bit better than epsilon- greedy policy. At last we talk how DQN improves on the sample efficiency of SARSA with the help of experience replay memory. Combining all these we implement DQN.Environment used  here is Assault-v0

5) The fifth Notebook contains a bit advance value based algorithm called Double DQN with Prioritized Experience Replay(PER) and target networks.This Notebook talks about some problems we have while using the Deep Q-Networks algorithm (DQN) and how we can improve DQN. This Notebook introduces concept of target network, double dqn and Prioritized Experience Replay and how we can combine them to make DQN more stable and efficient.Environment used  here is KungFuMaster-v0

6) The sixth Notebook contains an algorithm called Advantage Actor-Critic (A2C) which elegantly combine the policy gradient and a learned value function. This Notebook starts with providing the concept of advantage function and various methods of estimating advantage. Then we discuss the implementation of A2C. In the code I have also written about how add regularisation in Actor model with the help of entropy of policy

7) The seventh Notebook contains an algorithm called Deep Deterministic Policy Gradients(DDPG).Deep Deterministic Policy Gradient (DDPG) is a model-free off-policy algorithm for learning continous actions.
It combines ideas from DPG (Deterministic Policy Gradient) and DQN (Deep Q-Network). It uses Experience Replay and slow-learning target networks from DQN, and it is based on DPG, which can operate over continuous action spaces.

8) The Eighth Notebook contains an algorithm called Proximal Policy Optimization (PPO) extending Actor- Critic Algorithm.It is a another family of policy gradient methods for reinforcement learning, which alternate between sampling data through interaction with the environment, and optimizing a "surrogate" objective function using stochastic gradient ascent.

9) The Ninth Notebook contains an algorithm called Soft Actor-Critic (SAC): Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. It is policy maximum entropy actor-critic algorithm which provides for both sample- efficient learning and stability. This algorithm extends readily to very complex, high-dimensional tasks. 

10) The Tenth Notebook contains an algorithm called Asynchronous Advantage Actor Critic (A3C): A3C is an algorithm similar to A2C but differs in a way that it is  Asynchronous i.e. multiple independent agents(networks) with their own weights interact with a different copy of the environment in parallel and  thus explore a bigger part of the state-action space in much less time.

11) The Eleventh Notebook contains an algorithm called Noisy Nets: Noisy Nets are way to improve exploration in the environment by adding noise to network parameters

12) The Twelfth Notebook contains an algorithm called Rainbow: Rainbow takes the standard DQN algorithm and adds the 6 variants of DQN to it.

Credits: A lot of theory part for initial few notebooks is taken from Book:Foundations of Deep Reinforcement Learning By Graesser Laura and  Keng Wah Loon.


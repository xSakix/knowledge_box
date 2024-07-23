## DeepMind x UCL RL Lecture Series - Introduction to Reinforcement Learning [1/13]

URL: [https://www.youtube.com/watch?v=TCCjZe0y4Qc](https://www.youtube.com/watch?v=TCCjZe0y4Qc)

 * The speaker, Harvan Husselt, is a research scientist at DeepMind in London, teaching a course on reinforcement learning at UCL.
* He explains that the course is being delivered online due to the pandemic situation and goes into depth about reinforcement learning.
* Reinforcement learning is a type of machine learning where an agent learns to make decisions by interacting with its environment to maximize reward.
* It's related to artificial intelligence, which automates mental solutions, starting from the industrial revolution and continuing with the digital revolution.
* The main goal in reinforcement learning is to find a policy that maximizes cumulative reward.
* The speaker recommends the book "Reinforcement Learning: An Introduction" by Richard Sutton and Andrew Barto for further reading.
* The course covers different concepts and algorithms, with lectures available online on UCL's Moodle platform.
* Students can ask questions in the forum for interaction and collaboration.
* The speaker discusses the difference between active and passive learning and the importance of specifying a clear goal and reward function.
* He mentions various examples of reinforcement learning applications, including flying helicopters, managing investment portfolios, controlling power stations, making robots walk, and playing video games.
* The speaker emphasizes the importance of adaptive algorithms that can learn online and generalize to new situations.
* Reinforcement learning is a science framework for making decisions based on interaction, with reinforcement planning being a specific algorithm.
* The speaker mentions that reinforcement learning has synergy with deep learning and neural networks.
* He provides an example of an Atari game called Beam Rider to illustrate the concepts.
* The speaker discusses the concept of Markov property and its use in formulating reinforcement problems. * The case observation in reinforcement learning can be Markovian, meaning the probability of the next state depends only on the current state and action, not the entire history.
* Markov Decision Process (MDP) is a useful mathematical framework for formulating and solving decision problems with the Markov property.
* A Markovian state might not equal the full environment state, as some information might be thrown away due to the Markov property.
* The observation might not be Markovian if it contains uninformative data or depends on past observations.
* Partial Observable Markov Decision Process (POMDP) is an extension of MDP that deals with environments where the agent cannot observe the full state, and instead observes only a part of it.
* The update function in reinforcement learning can depend on the observation stream and the agent's actions, as well as the current state.
* A suitable state representation is important for dealing with partial observability, and using observation might be enough or might require full history depending on the problem size.
* The value function defines the optimal policy, which picks the action that maximizes the expected reward given the current state and policy.
* Planning involves computing the optimal policy given a model of the environment, which can be done in a model-free or model-based way.
* Prediction and control are related problems in reinforcement learning, with prediction focusing on estimating future rewards and control optimizing policies to find the best actions.
* Deep learning is a popular tool for learning functions in reinforcement learning, but it can violate assumptions such as stationarity and supervision.
* The Atari game example shows how an agent learns a value function from pixel observations and joystick inputs, and uses this information to select actions based on the current state and policy. * The speaker discusses a mean value state and a prime value state in a dynamic world
* Discount factor is used to see desirable states, with state b being somewhat desirable but the bottom left corner being quite undesirable
* Optimal policy involves not bumping the wall anymore and getting the best possible state through transitions
* The speaker mentions the optimal value function problem and the optimal policy, which are positive and result in no wall bumping
* There is a figure (c) showing the optimal policy and how to move between states
* The speaker discusses going around state b and the potential for getting stuck in a loop
* Learning planning algorithm is discussed as a way to find the optimal solution without bumping the wall
* The lecture touched upon various concepts like Q-learning, deep Q network (DQN), and policy gradient method
* Deep reinforcement learning with a neural network was mentioned
* The speaker mentions exploration and the concept of a bandit problem in the next lecture
* A simple example of a reinforcement learning problem involving controlling a body part to move in a certain direction is given.


## DeepMind x UCL RL Lecture Series - Exploration & Control [2/13]

URL: [https://www.youtube.com/watch?v=aQJP3Z2Ho8U](https://www.youtube.com/watch?v=aQJP3Z2Ho8U)

 * Adolf Hussels discussing exploration and exploitation in reinforcement learning
* Recommend reading chapter 2 of Sutton and Barto's "Reinforcement Learning" book for background
* Topic is bandit algorithms, specifically the UCB algorithm
* Previous lecture discussed RL and the interaction loop between agent and environment
* Agent interacts with environment, which can change based on its actions and observations
* Reward function defines agent's goal, which it tries to optimize by selecting actions
* Exploration is trying new actions to gather information, while exploitation is maximizing performance based on current knowledge
* Multiarmed bandit problem: set of actions with unknown rewards, need to determine optimal one
* Greedy policy: always select action with highest estimated value
* Epsilon-greedy algorithm: explore by randomly selecting other actions with probability epsilon
* UCB (Upper Confidence Bound) algorithm: explores and exploits by balancing exploration and exploitation using confidence intervals
* Gradient bandit algorithms: update policy parameters using gradient ascent to optimize expected reward
* Softmax policy: select action based on probabilities derived from preferences
* Stochastic gradient descent (SGD): optimization algorithm for finding minimum of a function, used in machine learning and deep learning.
* The speaker mentions the Reinforce algorithm, which is an early reinforce learning algorithm proposed by Williams and Peng in 1992. It's an on-policy algorithm that uses temporal difference methods to learn Q-values and policy parameters using stochastic gradient ascent. It also introduces the idea of eligibility traces to efficiently estimate gradients.
* The speaker mentions the concept of exploration vs exploitation tradeoff, where exploration involves trying new actions to gather information and exploitation involves taking actions based on current knowledge to maximize reward. In the context of multi-armed bandits, this means balancing between trying out new arms (exploration) and pulling the arm with the highest estimated reward (exploitation).
* The UCB algorithm is a popular approach for solving the exploration-exploitation dilemma in multi-armed bandit problems. It uses an upper confidence bound to balance exploration and exploitation by calculating an exploration bonus term based on the uncertainty of the estimates. This bonus term encourages the algorithm to explore actions with higher uncertainty, while still exploiting the ones with known high rewards.
* The speaker mentions that in a multi-armed bandit setting, there is no explicit environment state to observe, only rewards. Therefore, the agent needs to learn the distribution of rewards for each action based on past observations and use this information to make decisions.
* The speaker also mentions that in some cases, it might be more efficient to model the environment as a single state, even if it's complicated, rather than trying to model every possible state. This simplifies the problem and makes it easier to reason about.
* The speaker briefly touches on the concept of regret, which is the difference between the maximum expected reward that could have been obtained and the actual reward obtained by an algorithm. Minimizing regret is a common goal in reinforce learning and multi-armed bandit problems.
* The speaker mentions that the UCB algorithm can be used to minimize regret by balancing exploration and exploitation, but other algorithms like Thompson Sampling and Upper Confidence Bound 1 (UCB1) have also been proposed for this purpose.
* The speaker briefly discusses the concept of epsilon-greedy policy, which is a simple exploration strategy that selects an action with high probability based on current estimates, but with a small probability explores randomly. This strategy balances exploration and exploitation by allowing the agent to explore new actions while still exploiting known good ones.
* The speaker mentions that in some cases, it might be more efficient to learn the policy directly instead of learning the value function first. This is known as policy gradient methods or policy optimization, where the policy parameters are updated directly using gradient ascent.
* The speaker briefly discusses the concept of softmax policy, which is a probability distribution over actions that can be used to make decisions based on preferences or utilities assigned to each action. Softmax policies are commonly used in reinforce learning and deep reinforce learning.
* The speaker mentions that in some cases, it might be more efficient to use a constant step size for gradient descent instead of adaptive step sizes. This can lead to tracking behavior, where the algorithm converges to a local optimum faster but might not find the global optimum if the environment is nonstationary.
* The speaker mentions that in some cases, it might be more efficient to learn the value function directly using methods like Q-learning or SARSA instead of learning the policy directly. This can lead to better performance and easier convergence in certain environments.
* The * The speaker discusses the concept of preference action and how it relates to reward in reinforcement learning.
* Preference action with higher reward increases, while preference action with lower reward decreases.
* Policy gradient algorithm is used to learn the policy through exploration, but it can get stuck at local optima and suffer from linear increasing regret over time.
* The speaker mentions the importance of baseline in policy gradient algorithms and discusses the effect of different state values on variance reduction.
* UCB (Upper Confidence Bound) algorithm is introduced as a way to balance exploration and exploitation by using an uncertainty bound.
* Hoeffding's inequality is used to derive a bound for the estimate, which ensures that the probability of selecting a suboptimal action decreases over time.
* The speaker mentions the importance of considering different cases in the derivation and simplifying notation for clarity.
* The UCB algorithm picks the action with the highest estimated value plus uncertainty bound to ensure exploration while keeping the total regret logarithmic.
* The speaker mentions that they will prove the logarithmic regret bound later in the lecture.
* They also mention that there are other techniques that could be used instead of UCB, such as Thompson sampling and Bayesian optimization.
* The speaker encourages the audience to refer to the paper for more details on the proof. * The speaker discusses probability theory and its application to selecting actions in a bounded one-step decision-making problem.
* They mention using Huffman's inequality and the concept of regret.
* The speaker suggests that the left-hand side of an equation should be random variable minus q, while the right-hand side should be expectation.
* They propose the idea of a property larger than 2u to replace probability.
* The speaker mentions the logarithmic case and the need for a precise proof.
* They discuss the use of UCB (Upper Confidence Bound) and Thompson Sampling algorithms for bandit problems.
* The speaker explains the concept of probability matching, which is different from UCB.
* They describe the idea of optimism in the face of uncertainty and its relationship to UCB.
* The speaker mentions the challenges of computing probabilities analytically and the use of POMDPs (Partially Observable Markov Decision Processes).
* They discuss planning, explore-exploit tradeoff, and the idea of learning a Bayesian reward distribution.
* The speaker mentions the difficulty of scaling reinforcement learning techniques for large problems.
* The speaker provides an example problem and asks the audience to select the next action based on probability.
* They compare the answers given by a greedy algorithm and UCB, and explain the difference between them.
* The speaker assumes a beta distribution for the posterior distribution in Thompson Sampling and explains how it looks like the optimal action.
* They discuss the similarities and differences between UCB and Thompson Sampling algorithms.
* The speaker mentions that UCB does not always select the exact action, while Thompson Sampling might select it 25% of the time on average.
* They suggest tweaking exploration parameters to change the behavior of UCB and Thompson Sampling.


## DeepMind x UCL RL Lecture Series - MDPs and Dynamic Programming [3/13]

URL: [https://www.youtube.com/watch?v=zSOMeug_i_M](https://www.youtube.com/watch?v=zSOMeug_i_M)

 * The speaker is Diana, a research scientist at DeepMind, discussing Markov Decision Processes (MDPs) in the context of Reinforcement Learning.
* She has been involved with the UCL machine learning master's course and has taught the RL course for three years.
* Today's lecture will cover formalizing the interaction loop in RL using MDPs.
* Recap: RL problem, agent-environment interaction, Markov property.
* Formalizing RL interaction with Markov Decision Processes (MDPs):
  * Assumes fully observable environment where current observation contains all relevant information.
  * Defines MDP as a tuple: state space, action space, transition probabilities, reward function, discount factor.
  * Bellman equation and dynamic programming for solving MDPs.
* Differences between MDP and other definitions in literature.
* Example of a cleaning robot problem from Sutton & Barto's book.
* Computing the value function using the Bellman equation and dynamic programming.
* Bellman expectation equation, matrix formulation, linear equation solution, convergence, and complexity.
* Policy iteration methods: value iteration and policy evaluation.
* Dynamic Programming (DP) history and meaning.
* Solving MDPs with dynamic programming methods.
* Policy Evaluation:
  * Initializing values, iteratively updating values according to the Bellman equation, convergence, and stopping criterion.
* Example of iterative policy evaluation in a grid world environment.
* Acting greedily respects the value function after each iteration.
* General principle of reinforcement learning with dynamic programming: evaluating policies, taking a step, getting gratification, and improving based on the new policy. * The speaker discusses the concept of reinforcement learning, specifically policy iteration and dynamic programming
* Policy iteration involves evaluating a policy, improving it, and repeating the process until an optimal policy is obtained
* Dynamic programming is a method for finding the optimal value function, which can then be used to determine the optimal policy
* Bellman equation and Bellman optimality equation are mentioned as important concepts in reinforcement learning
* Policy iteration algorithm consists of policy evaluation, policy improvement, and policy iteration steps
* Asynchronous dynamic programming is mentioned as a way to reduce computational overhead in dynamic programming
* Real-time dynamic programming is another method that makes updates efficiently by maintaining a priority queue
* The speaker mentions the importance of understanding the structure of value functions and the role of state, action, and reward in reinforcement learning.


## DeepMind x UCL RL Lecture Series - Theoretical Fund. of Dynamic Programming Algorithms [4/13]

URL: [https://www.youtube.com/watch?v=XpbLq7rIJAA](https://www.youtube.com/watch?v=XpbLq7rIJAA)

 * Recap of Markov Decision Process (MDP) and dynamic programming
* Bellman operator introduction
* Property 1: Star contraction mapping in L∞ norm
* Property 2: Monotonicity of Bellman operator
* Value Iteration algorithm and its convergence
* Approximate Dynamic Programming overview
* Challenges with perfect knowledge assumption, large state and action spaces, and function approximation
* Sampling methods and estimation errors
* Sample-based methods vs. Function approximation methods
* Computational considerations in approximate dynamic programming
* Example of a divergent sequence using linear approximator in a small MDP
* Greedy policy derivation using the Quality Policy Theorem
* Proof of the Quality Policy Theorem
* Importance of understanding edge cases and potential losses in approximate dynamic programming. * The speaker discusses the gamma value in reinforce learning and its potential large impact on performance
* Small gamma values make the problem easier, but when gamma equals zero, the term goes to zero
* Q-value function is derived to obtain a greedy policy, which is bounded by Q\*, implying moving towards the optimal policy
* Policy iteration paradigm and its relation to approximation methods are discussed
* The convergence of the value function and optimal policy is questioned, even if the value function converges
* Approximate policies may not guarantee the optimal policy, but can still provide good results
* The nature of approximation quality and its impact on policy quality is mentioned
* The target policy in evaluating the previous iteration's policy is discussed, with no assumption made about greedy improvement
* The speaker mentions that evaluation policy improvement is guaranteed to improve the policy, but not necessarily converge to the optimal policy
* Approximate value functions may not converge to the optimal value function
* The approximate dynamic programming paradigm is summarized and the next lecture will cover the picture and map algorithms.


## DeepMind x UCL RL Lecture Series - Model-free Prediction [5/13]

URL: [https://www.youtube.com/watch?v=eaWfWoVUTEw](https://www.youtube.com/watch?v=eaWfWoVUTEw)

 * Lecture on model-free prediction in reinforcement learning by Advan Hasselt
* Recap of background material from previous lectures, feel free to defer reading
* Model-free prediction vs. model-based prediction
* Monte Carlo algorithm for estimation without a model
* Monte Carlo method used in reinforcement learning
* Monte Carlo sampling and its usage
* Linear function approximation for value functions
* Q-learning as an alternative to Monte Carlo methods
* Temporal difference learning and the Bellman equation
* Bootstrapping in temporal difference learning
* Advantages of Monte Carlo methods over dynamic programming
* Recap of upcoming lecture: policy learning and prediction tasks. * The speaker discusses the difference between Monte Carlo and Temporal Difference (TD) learning in the context of estimating state values.
* TD learning updates value estimates based on the current state and the next state's estimated value, while Monte Carlo learning waits for the end of an episode to update the value estimate with the actual reward.
* TD learning allows for online learning, as each transition is used to update the value estimate, whereas Monte Carlo learning requires the entire episode to be completed before updating.
* TD learning can handle incomplete sequences and corrupted data better than Monte Carlo learning, but it may have a higher computational complexity due to the need to store and update separate tables for each state.
* Monte Carlo learning has a lower memory requirement as it only needs to store the current estimate for each state, while TD learning requires storing the estimated value for each state-action pair.
* TD learning can suffer from bias variance tradeoff, as the target value may be biased if the prediction is not accurate, leading to higher error.
* Monte Carlo learning returns an unbiased estimate of the true value, but it may take longer to converge to the true value due to the need for more samples.
* TD learning can handle partially observable environments by using an implicit target update and exploiting the Markov property, while Monte Carlo learning assumes a fully observable environment and does not make this assumption explicitly.
* TD learning can propagate information slowly, leading to slow credit assignment, whereas Monte Carlo learning updates the previous state visited, allowing for faster propagation of information.
* TD learning can look ahead multiple steps to update the value estimate, while Monte Carlo learning takes exactly one step at a time.
* The speaker mentions that the choice between Monte Carlo and TD learning depends on the specific problem and the tradeoffs involved, such as computational complexity, memory requirement, and convergence rate. * The speaker discusses the relationship between Temporal Difference (TD) learning and Monte Carlo methods, focusing on the differences and similarities between one-step TD, n-step TD, and various other algorithms.
* TD algorithms update value functions based on the temporal difference error, while Monte Carlo methods use the return from a single trajectory to estimate values.
* One-step TD corresponds to TD(0) algorithm, which always chooses one time step for bootstrapping, while n-step TD uses n timestamps for bootstrapping.
* The curves of TD and Monte Carlo methods look similar but are not exactly the same due to differences in how they handle instances and the number of steps taken.
* The benefits of using mixed multistep returns include independence from temporal span prediction and computational efficiency.
* Monte Carlo learning has issues with bias and variance, while TD learning has advantages in terms of information propagation and simplicity.
* Linear function approximation is used to approximate value functions, which are defined as the inner product of a weight vector and feature vector.
* The update rule for linear function approximation involves taking the difference between the current estimate and the target value, multiplying it by the learning rate, and adding the product of the feature vector and the weight vector.
* Eligibility traces are used to efficiently update past states in TD learning, which helps in accounting for new temporal difference errors without recomputing values or storing individual features.
* The speaker discusses the equivalence between Monte Carlo updates and TD updates, and mentions that both methods can be applied online or offline.
* Mixed multistep returns combine the benefits of both TD and Monte Carlo learning by using a weighted average of n-step returns and one-step returns.
* The speaker also touches upon the importance of considering computational properties and the independence of span prediction when choosing between TD and Monte Carlo methods.


## DeepMind x UCL RL Lecture Series - Model-free Control [6/13]

URL: [https://www.youtube.com/watch?v=t9uf9cuogBo](https://www.youtube.com/watch?v=t9uf9cuogBo)

 * The lecture is about advanced topics in model-free control, specifically focusing on value functions and policy improvement in reinforcement learning.
* Model-free control tries to optimize the value function first in policy evaluation.
* Policy iteration involves interleaving two steps: policy evaluation and policy improvement.
* In policy evaluation, an arbitrary initial value function is used, which is then updated based on the current policy's evaluations.
* In policy improvement, a new policy is found by making the policy greedy with respect to the current value function.
* Policy iteration can be seen as a way to replace V(Q) in model three estimation.
* Monte Carlo control uses the full return, including the reward from the current state and all future discounted rewards.
* Temporal difference learning (TD) methods use bootstrapping, which involves taking one step and updating the estimate based on the current value function.
* Q-Learning is a popular algorithm for policy learning, which learns the optimal policy by estimating the state-action values using the Bellman equation.
* Off-policy TD (Q) Learning is an extension of Q-Learning where the policy used to evaluate the state-action value is different from the policy used to select actions. * The speaker discusses Q-learning and SARSA, two popular reinforce learning algorithms
* Q-learning uses the maximum expected value of the next state as the target for updating the action value function
* SARSA uses the actual next state and reward to update the action value function
* Q-learning can explore by using an epsilon-greedy policy, which randomly selects actions with a small probability
* The speaker discusses the difference between on-policy and off-policy learning, with Q-learning being an on-policy algorithm
* The speaker mentions that Q-learning can suffer from overestimation of action values due to exploration and function approximation errors
* Double Q-Learning is a variation of Q-learning that addresses the overestimation issue by using two separate target value functions
* DQN (Deep Q-Network) is another popular reinforce learning algorithm that uses a deep neural network to approximate the Q-value function.
* The speaker mentions the importance of exploration in RL, and how it can be achieved through various methods such as epsilon-greedy or UCB1.
* The speaker discusses the concept of convergence, which refers to when an algorithm reaches a stable solution. In the context of RL, this means that the Q-values have converged to their optimal values.
* The speaker mentions the importance of exploration in RL, and how it can be achieved through various methods such as epsilon-greedy or UCB1.
* The speaker discusses the concept of exploration vs exploitation, which is a fundamental tradeoff in RL. Exploration refers to trying out new actions to gather more information about the environment, while exploitation refers to taking the action with the highest expected reward based on current knowledge.
* The speaker mentions the importance of function approximation in RL, and how it allows us to handle large state and action spaces. However, it also introduces errors due to finite sample size and approximation errors.
* The speaker discusses the concept of temporal difference learning, which is a key component of Q-learning and SARSA algorithms. It involves estimating the error in the Q-value function at each time step and using that error to update the Q-values.
* The speaker mentions the importance of exploration in RL, and how it can be achieved through various methods such as epsilon-greedy or UCB1.
* The speaker discusses the concept of convergence, which refers to when an algorithm reaches a stable solution. In the context of RL, this means that the Q-values have converged to their optimal values.
* The speaker mentions the importance of exploration in RL, and how it can be achieved through various methods such as epsilon-greedy or UCB1.
* The speaker discusses the concept of exploration vs exploitation, which is a fundamental tradeoff in RL. Exploration refers to trying out new actions to gather more information about the environment, while exploitation refers to taking the action with the highest expected reward based on current knowledge.
* The speaker mentions the importance of function approximation in RL, and how it allows us to handle large state and action spaces. However, it also introduces errors due to finite sample size and approximation errors.
* The speaker discusses the concept of exploration vs exploitation, which is a fundamental tradeoff in RL. Exploration refers to trying out new actions to gather more information about the environment, while exploitation refers to taking the action with the highest expected reward based on current knowledge.
* The speaker mentions the importance of exploration in RL, and how it can be achieved through various methods such as epsilon-greedy or UCB1.
* The speaker discusses the concept of convergence, which refers to when an algorithm reaches a stable solution. In the context of RL, this means that the Q-values have converged to their optimal values.
* The speaker mentions the importance of exploration in RL, and how it can be achieved through various methods such as epsilon-greedy or UCB1.
* The speaker discusses the concept of exploration vs exploitation, which is a fundamental tradeoff in RL. Exploration refers to trying out new actions to gather more information about the environment, while exploitation refers to taking the action with the highest expected reward based on current knowledge.
* The speaker mentions the importance of function approximation in RL, and how it allows us to handle large state and action spaces. However, it also introduces errors due to finite sample size and approximation errors.
* The speaker discusses the concept of exploration vs exploitation, which is a fundamental tradeoff in RL. Exploration refers to trying out new actions to gather more information about the environment, while exploitation refers to taking the action with the highest expected reward based on current knowledge * The speaker begins by discussing Onestep Reward and Policy Evaluation in the context of Bandit problems.
* They explain how to calculate expected rewards using value functions, behavior policies, and reweighted samples.
* The importance of sampling distributions and unbiased estimates is emphasized.
* The speaker discusses the use of Monte Carlo methods, Temporal Difference Learning, and Importance Sampling for estimating value functions.
* They mention the advantages of using Temporal Difference Learning over Monte Carlo methods in certain cases.
* The speaker introduces Q-Learning as a special case of SARSA and discusses its relationship to Value Iteration.
* They touch on the concept of Double Q-Learning and its use in mitigating bias in action value estimates.
* The lecture concludes with a summary of the key points covered.


## DeepMind x UCL RL Lecture Series - Function Approximation [7/13]

URL: [https://www.youtube.com/watch?v=ook46h2Jfb4](https://www.youtube.com/watch?v=ook46h2Jfb4)

 * The lecture is about Function Approximation in Reinforcement Learning.
* The background material includes Saturn Embargo and covers material from chapters 9 to 11.
* Function approximation is important for dealing with large state spaces, which cannot be stored in a tabular form.
* Different function classes can be used for function approximation, including neural networks, which is often called deep reinforcement learning.
* Value prediction and policy learning will be discussed in upcoming lectures.
* The motivation for using function approximation is to make the algorithm more flexible and efficient.
* Linear function approximation was mentioned earlier as a special case of the tabular case.
* Deep neural networks can be used for nonlinear function approximation, which allows for richer representations.
* Gradient-based algorithms, such as gradient descent, can be used to optimize the parameters in function approximation methods.
* The lecture mentions some challenges in reinforcement learning, including nonstationary environments and partially observable states.
* The lecture also discusses the importance of understanding the reward function and choosing appropriate features for representation. * The speaker discusses different methods for estimating the value function in Markov Decision Processes (MDPs), specifically focusing on Monte Carlo and Temporal Difference (TD) learning.
* Monte Carlo method involves taking random samples from the environment to estimate state-value functions, while TD learning updates the value function based on the difference between the predicted and actual rewards at each time step.
* The speaker discusses the advantages and disadvantages of both methods, including their convergence properties and computational efficiency.
* They also mention the use of function approximation techniques, such as linear function approximation and neural networks, to handle large state spaces.
* The speaker touches on the concept of Q-learning and the importance of exploration vs exploitation in reinforce learning algorithms.
* They briefly discuss the idea of using different step sizes and discount factors in TD learning, and the tradeoff between convergence speed and variance.
* The speaker mentions the concept of bootstrapping and its role in TD learning.
* They also touch on the difference between Monte Carlo and TD solutions, and the fact that Monte Carlo solutions are typically more biased but converge faster than TD solutions.
* The speaker briefly discusses the idea of using different feature representations for state-value functions and their impact on convergence properties.
* They mention the importance of handling non-stationary environments in reinforce learning algorithms.
* They touch on the concept of policy iteration and its relationship to value iteration.
* The speaker mentions the use of off-policy TD learning, which allows for learning a policy while following a different policy than the one being optimized.
* They briefly discuss the idea of using eligibility traces in TD learning to improve convergence properties.
* They mention the importance of handling continuous state and action spaces in reinforce learning algorithms, and the use of function approximation techniques to handle these spaces.
* The speaker briefly touches on the concept of deep Q-learning and its ability to learn complex policies from raw pixel inputs using neural networks.
* They mention the importance of exploration strategies, such as epsilon-greedy, in reinforce learning algorithms.
* They touch on the idea of using value iteration with function approximation, which is known as Q-learning.
* They briefly discuss the concept of policy gradients and their use in reinforce learning algorithms.
* They mention the importance of handling non-Markovian environments in reinforce learning algorithms and the use of methods such as Monte Carlo control to handle these environments.
* They touch on the idea of using actor-critic methods, which combine the estimation of the value function and the policy in a single algorithm.
* They briefly discuss the concept of deep deterministic policy gradients (DDPG) and its ability to learn continuous policies using neural networks.
* They mention the importance of handling partial observability in reinforce learning algorithms and the use of methods such as Monte Carlo control with eligibility traces to handle these environments.
* They touch on the idea of using deep reinforce learning techniques, such as deep Q-learning and policy gradients, to learn complex policies from raw pixel inputs using neural networks.
* They mention the importance of handling continuous state and action spaces in deep reinforce learning algorithms and the use of methods such as softmax actions and Gaussian policies to handle these spaces.
* They briefly discuss the concept of trust regions and their use in optimization algorithms, including reinforce learning algorithms.
* They touch on the idea of using Monte Carlo tree search (MCTS) for games with large state spaces and the ability of MCTS to explore the state space efficiently.
* They mention the importance of handling multi-agent environments in reinforce learning algorithms and the use of methods such as Q-learning with separate Q-values for each agent to handle these environments.
* They briefly discuss the concept of cooperative and competitive multi-agent environments and the challenges of learning policies in these environments.
* They touch on the idea of using deep reinforce learning techniques, such as actor-critic methods and deep Q-learning, to learn complex policies for multi-agent systems.
* They mention the importance of handling uncertainty in reinforce learning algorithms and the use of methods such as Bayesian reinforce learning to handle these environments.
* They touch on the idea of using hierarchical reinforce learning to learn high-level abstractions of complex tasks.
* They briefly discuss the concept of transfer learning and its ability to leverage knowledge learned in one task to improve performance in a related task.
* They mention the importance of handling real-world constraints, such as safety and resource limitations, in reinforce learning algorithms.
* They touch on the idea of using model-based methods, such as dynamic programming and Monte Carlo control, to learn optimal policies in complex environments with known dynamics.
* They briefly discuss the concept of online learning and its ability to adapt to changing environments in real-time.
* They mention the importance of handling high-dimensional state spaces and the * The speaker discusses Temporal Difference (TD) learning and its potential issues, specifically the "deadly triad" of bootstrapping, function approximation, and policy learning
* TD learning involves updating the value function based on the difference between the current estimated state value and the expected future state value
* Bootstrapping is used to estimate the expected future state value using the current policy and the current state's value function
* Function approximation is used to approximate the value function with a finite set of parameters, such as weights in a neural network
* Policy learning involves updating the policy based on the estimated Q-values or policy gradients
* The combination of these three techniques can lead to divergent dynamics, known as the "deadly triad"
* The speaker mentions that TD learning ignores bootstrapping value and instead tries to update the state value towards something closer to the next state's value, which can result in chasing a moving target and divergence
* Alternative approaches include minimizing the expected temporal difference error or using Bellman residual minimization
* The speaker also mentions the importance of understanding convergence properties of different reinforce learning algorithms. * Deep learning explanation: computing gradients, neural networks, backpropagation
* Deep learning vs traditional machine learning: deep neural networks, nonlinear functions, optimization methods
* Reinforcement learning: agent update function, Q-learning, double Q-learning, target network
* Deep reinforcement learning: combining deep learning and reinforcement learning
* Deep learning aware reinforcement learning: changing reinforcement updates, using experience replay, deliberate use of deep networks
* Importance of deep learning in reinforcement learning research.



## DeepMind x UCL RL Lecture Series - Planning & models [8/13]

URL: [https://www.youtube.com/watch?v=FKl8kM4finE](https://www.youtube.com/watch?v=FKl8kM4finE)

 * Matthew Hassell introducing Reinforcement Learning module with Hado Diana
* Discussing model-based and model-free algorithms in RL
* Dynamic Programming (DP) and Model 3 algorithm differences
* DP assumes complete specification of the environment, Model 3 relies on learned models
* Function approximation for scaling up RL, especially in large state spaces
* Introducing different types of learned models: table lookup model, linear expectation model, stochastic generative model
* Linear Expectation Model (LEM) advantages and disadvantages
* Comparing LEM with the Dyna algorithm
* Combining model-based and model-free methods in RL
* Dyna algorithm's strengths and limitations. * The speaker discusses the difference between like algorithm and Dyna, focusing on the ability of Dyna to train models with jumpy predictions in a true native time scale environment.
* Parametric models have lower memory requirements than big neural networks but may not be the best fit for every problem.
* Planning involves selecting actions based on current state and estimating future rewards, with planning value functions being used to make accurate local value functions that can approximate global functions.
* Simulation-based search algorithms allow selecting the best action given a state by constructing an entire search tree or using forward search approaches like Monte Carlo Tree Search (MCTS).
* MCTS uses a fixed simulation policy and navigates the tree based on previous simulations to guide learning and improve exploration.
* The speaker discusses the advantages of simulation-based search, including its computational efficiency and parallelizability, but notes that it may still feel fuzzy in certain situations.
* Monte Carlo research is a simulation-based approach used to learn values and policies, with the AlphaZero system being an example of its success in learning to play world champion games like Go, Chess, and Shogi.
* The speaker provides a concrete example of how simulation-based search works and discusses the advantages of using a fixed simulation policy instead of a tree policy for building the search tree.
* The speaker notes that Monte Carlo research is essentially a table lookup approach but can be more efficient than forward search due to its ability to allocate computational resources effectively.
* The speaker mentions that monte carlo research is not naive as it can handle large search spaces and combines ideas with MCTS instance value function approximation.
* The speaker concludes by emphasizing the importance of understanding these algorithms for building intelligent agents and realizing that simulation-based approaches are essential for creating efficient and effective AI systems.


## DeepMind x UCL RL Lecture Series - Policy-Gradient and Actor-Critic methods [9/13]

URL: [https://www.youtube.com/watch?v=y3oqOjHilio](https://www.youtube.com/watch?v=y3oqOjHilio)

 * Welcome to ninth lecture on marine enforcement, discussing policy gradient extra credit term
* Comparing approach of AI and reinforcement learning (RL)
* Policy gradient RL benefits: relatively easy to learn model in supervised learning, can extract data and structure from transitions
* Downside: might spend significant computation capacity on irrelevant details
* Value-based RL: easier to generate policy values, but might focus on irrelevant details
* Pros and cons of value-based RL: easier to generate policy values, less planning required, but might not learn values well and could focus on irrelevant details
* Policy-based RL: directly optimizes the policy instead of learning a value function
* Comparing different approaches in general: they generalize differently, and policy-based RL might be easier to learn in some cases
* Formalizing policy learning objective: finding the policy parameter (theta) that maximizes the expected return
* Episodic environment: use average total return per episode as objective
* Policy gradient methods: optimizing the policy using a gradient-based algorithm, such as stochastic gradient descent or advanced optimizers like RMS prop, Adam, and AdaGrad. * The speaker is discussing policy gradient methods in reinforce learning.
* They start by deriving the expected reward gradient equation.
* They mention the importance of understanding the equality proven in the previous slide.
* They discuss the sample stochastic policy gradient update and its unbiasedness.
* They introduce the inverse log-likelihood trick to reduce variance.
* They explain how the policy parameter and state depend on each other in the context of the Bellman equation.
* They mention the difference between episodic and nonepisodic tasks and their respective objectives.
* They provide an example of a maze problem and discuss why using average reward as the objective is not appropriate for episodic tasks.
* They discuss the policy gradient theorem in the context of Markov decision processes (MDPs) and multistep transitions.
* They mention the use of baselines to reduce variance and improve estimation efficiency.
* They discuss the difference between discounted and undiscounted returns, and their respective advantages and disadvantages.
* They introduce the concept of eligibility traces and their relationship to policy gradient methods.
* They briefly touch on the ectocritic algorithm as an alternative to traditional actor-critic methods.
* They mention some practical considerations when implementing policy gradient algorithms, such as regularization and stability.
* They discuss various extensions and modifications to policy gradient algorithms, including TRPO, PPO, and MPO. * Function parameters in RL: keep policy moving, avoid bad updates, understand technicalities
* Regularization: use objective term, hyperparameter eta determines level of regularization
* Modern algorithms: TRPO, PPO, MPO, etc.
* Continuous action space: extend value-based RL, parameterize policy with gaussian distribution
* High dimensional continuous space: challenging to explore, use Monte Carlo or bootstrapping returns
* Policy improvement: perform gradient ascent on value function, using policy and critic gradients
* Action-dependent heuristic dynamic programming: policy improvement with gradient ascent
* Continuous Active Critic Learning Automaton (CACL): define action space instead of error parameter space
* Temporal difference error: update value function using TD error, positive updates towards action taken
* Gradient descent ascent algorithm: move towards maximum value in value space
* Cache algorithm: extend simulated annealing with caching and exploration strategies
* Different algorithms: Q-learning, SARSA, etc.
* Reducing variance in policy learning: multistep learning, reducing exploration noise
* No context: 'let look example moment first' and 'im going talk continuous action space'.


## DeepMind x UCL RL Lecture Series - Approximate Dynamic Programming [10/13]

URL: [https://www.youtube.com/watch?v=AJejcug2brU](https://www.youtube.com/watch?v=AJejcug2brU)

 * The lecture is about Approximate Dynamic Programming and Reinforcement Learning.
* Model 3 of reinforcement learning is being discussed, which involves removing the perfect knowledge assumption and using function approximation instead.
* Approximate dynamic programming involves estimating value functions and policies iteratively.
* Belmont optimality operator and Bellman optimality equation are introduced.
* Value iteration and policy iteration algorithms are explained in approximate setting.
* Approximation error is discussed, which can be incurred due to imperfect knowledge of the underlying MDP or function approximation limitations.
* Backup value iteration is introduced as a way to handle approximation error.
* The lecture covers the convergence of approximate dynamic programming algorithms and the relationship between performance policy and optimal policy.
* Linear function approximators, such as neural networks, are mentioned as a popular choice for function approximation.
* DQN (Deep Q-Network) and Batch RL (Batch Reinforce Learning) are given as examples of instantiation of approximate dynamic programming algorithms.
* The lecture covers the relationship between control and policy iteration, and the concept of policy improvement.
* The lecture discusses the convergence of approximate dynamic programming algorithms to optimal value functions and policies.
* The importance of understanding the relationship between performance policy and optimal policy is emphasized.
* The lecture covers the use of matrices to represent transition probabilities and Bellman equations in matrix form.
* The proof of the convergence of approximate dynamic programming algorithms is discussed, using the concept of gain and the relationship between consecutive policies. * The speaker is discussing the application of an equation in policy optimization, specifically a particular inequality.
* They want to convince the audience that they have proven a statement about the quality of policies derived from iteration to iteration.
* They discuss the definition of approximation error and how it relates to the quality of a policy.
* They give an example of a simple MDP (Markov Decision Process) to illustrate the concept.
* Instead of using full evaluation policy, they suggest considering approximation methods based on functional classes or samples.
* Approximation methods maintain the relationship between action values within the action space and allow taking greedy actions respecting the approximation.
* The speaker discusses the concept of a Bellman operator and fixed point evaluation expectation evaluator in relation to optimal policy.
* They introduce the term "lk" as the difference between the optimal value function and the quality policy iteration k.
* They bound the term using various operators, simplify it, and discuss the behavior of the error in the limit as k tends to infinity.
* They mention a concrete instance algorithm called TD lambda and its properties related to convergence and optimization.
* They summarize the two paradigms of approximate dynamic programming: approximate value iteration and policy evaluation.
* They emphasize that control error and approximation error have different sources and discuss the importance of efficient optimization methods.
* They mention that convergence is guaranteed in some cases but not always, and there might be intermediate errors during the process.
* They discuss approximate policy iteration and its results, as well as the importance of inner loop procedures in policy evaluation problems.
* They invite questions at the end of the talk.


## DeepMind x UCL RL Lecture Series - Multi-step & Off Policy [11/13]

URL: [https://www.youtube.com/watch?v=u84MFu1nG4g](https://www.youtube.com/watch?v=u84MFu1nG4g)

 * Hardivan Husselt talking about policy learning in reinforcement learning
* Background material: Susan Ambartos chapters 5, 7, 11; recapping and motivating
* Discussed: taking action based on observations, policy gradient, model-based methods, function approximation, importance of policy learning
* Policy learning involves taking account of time consequences and agent internal state
* Multistep update vs. one-step update, importance sampling correction for efficient learning
* Dynamic programming operator in reinforcement learning algorithms
* Discussed policy correction, multistep return, variance, and importance weighting strategies to reduce variance. * Control Variance: a method to reduce variance in Monte Carlo and Temporal Difference (TD) methods
* Control Variance = weighting error rather than return
* Important Sampling Ratio: multiplies reward recursively for each step, reduces variance significantly especially later
* Per-Decision Importance: waiting for adding important sampling ratio earlier in the process to get equivalent term reward
* Bootstrapping: applying temporarily earlier or on a step-by-step basis
* Control Variance vs. Error Weighting: both reduce variance but error weighting might not always reduce variance
* Deadly Triad: divergent learning, bootstrapping, and function approximation can lead to inaccurate estimates
* Adaptive Bootstrapping: mitigating the deadly triad by adapting the bootstrap parameter based on data
* Multistep Error: extending one-step TD error to multistep using initial bootstrap parameter
* Importance Sampling Corrected Multistep Error: correcting multistep error using importance sampling ratio
* Tree Backup: a different algorithm that uses recursive definitions and weighted sums for action value estimation.
* VTraces: an effective algorithm that uses a tree structure to store and update value estimates, allowing for adaptive bootstrapping. * Sampled return is important in unbiased, low variance estimation.
* Importance of sampling ratio and division by n are not crucial in Monte Carlo methods.
* In lab courses, additional problems may require downloading.
* Practical problems can work well with bootstrapping, but careful consideration is needed due to pi behavior.
* Policy method behavior might be different when using bootstrapping; it could take many steps.
* Low probability actions in policy might require more bootstrapping steps.
* Policy mechanism might agree with the greedy policy, causing long trajectories of picking the same action.
* Nongreedy actions would terminate bootstrap process.
* Max Q-learning is similar to bootstrap target Q-learning.
* Policy is fairly greedy in Q-learning, and multistep returns are quite uniform.
* Greedy policy return might be truncated.
* Deadly triad issue: behavior mismatch between target and actual policies.
* Target policy might bootstrap earlier, which could be dangerous.
* Chris Watkins proposed Q-learning algorithm is policy greedy.
* Long-term returns are of interest in the greedy policy.
* Policy target policy could be greedy, but it doesn't eliminate behavior mismatch issue.
* Ongoing research is being done to find the best solution for dealing with deadly triad.


## DeepMind x UCL RL Lecture Series - Deep Reinforcement Learning #1 [12/13]

URL: [https://www.youtube.com/watch?v=cVzvNZOBaJ4](https://www.youtube.com/watch?v=cVzvNZOBaJ4)

 * Discussing the combination of deep reinforcement learning and function approximation
* Function approximation allows generalizing value estimation for large, complex problems
* Automatic differentiation (autodiff) is a tool used in deeper enforcement learning to efficiently compute gradients
* Q-Learning agent example using neural network function approximator and autodiff (Jax framework)
* DPQ learning update using pseudoloss function and Jax's gradient function
* Deep reinforcement learning challenges: combining RL and deep learning, making RL aware of specific choices in function approximation, and keeping the learning process stable.
* Deadly triad issues: divergence, time complexity, and instability
* DQN algorithm: target network idea, bootstrapping, and periodically updating parameters to reduce interference with feedback loop
* Double Q-learning: separate evaluation and selection networks, reducing overestimation and improving stability
* Prioritization in reinforcement learning: making efficient use of resources by prioritizing transitions based on error
* Deep learning side design: neural network architecture for enforcement learning, optimizing the neural network target constructed via bootstrapping, and increasing instance capacity to improve performance.
* Recent successes in deep learning: encoding inductive bias, building tailored representations for specific tasks, and applying deep learning to various domains (computer vision, NLP).
* Dueling Network Architecture: introduced to improve performance of deep Q-learning agents by separating state value estimation and action-dependent advantage estimation.
* Larger networks tend to perform better in reinforcement learning due to increased capacity and ability to learn complex representations.
* Smoothness and stability issues in deep learning architectures can be addressed using techniques like double queue estimators and multistep target updates. * Large empirical study found that Q-learning with instance different network capacity can lead to unreasonable estimate growth and inappropriate generalization
* Smoothness is a problematic property in deep learning architecture for approximating sharp discontinuities
* Monte Carlo update in function approximator can result in high variance errors in the bottom half of the value estimation, while TD update has lower variance and less noise
* The smoothness property might introduce error, but this could be expected
* Double Q-learning with a double queue estimator can help alleviate the issue of leakage propagation
* Certain architectural choices can improve function approximator performance in deep reinforcement learning (DRL) research
* Inappropriate generalization, smoothness, and leakage propagation are major issues in DRL
* Deep learning architecture is important but not a complete solution to RL, as better representation training methods are needed
* Multitask instance could share representations to predict values for different policies, discounts, and cumulative rewards, potentially alleviating many discussed issues.


## DeepMind x UCL RL Lecture Series - Deep Reinforcement Learning #2 [13/13]

URL: [https://www.youtube.com/watch?v=siDtNqlPoLk](https://www.youtube.com/watch?v=siDtNqlPoLk)

 * Discussion on deep neural networks used for function approximation in RL and automatic differentiation
* Issues with using deep learning for function approximation, such as the deadly triad phenomenon
* Idea of optimized representation learning in RL to address fundamental problems
* Overview of recent research on general value functions and distributional value prediction
* Discussion on the use of general value functions for prediction and their relationship to standard value functions
* Comparison of different approaches to prediction, including GVF (Generalized Value Function) and TD (Temporal Difference) algorithms
* Importance of understanding the effect of cumulative discounting on representation learning
* Discussion on using auxiliary tasks in RL for representation learning, such as self-supervised learning and feature control
* Comparison of different approaches to representation learning, including GBFs (Gradient-based Function Approximation) and GDFS (Gradient Descent with Function Smoothing)
* Overview of recent research on using auxiliary tasks for representation learning, such as the unreal agent and PCR (Policy Gradient with Importance Rescaling)
* Discussion on the importance of understanding the effect of different target policies and discount factors on representation learning
* Comparison of different approaches to handling non-stationarity in RL, including adaptive normalization and merging distributions
* Overview of recent research on distributional reinforcement learning as an alternative to traditional value-based methods.


## DeepMind x UCL | Deep Learning Lectures | 1/12 | Intro to Machine Learning & AI

URL: [https://www.youtube.com/watch?v=7R52wiUgxZI](https://www.youtube.com/watch?v=7R52wiUgxZI)

 * DeepMind UCL connection: Thomas Hassabis, founder of DeepMind, met a postdoctoral fellow at UCL and started the company.
* Lecture series: Sharing thoughts on deep learning, with several lecturers in the series getting to know people.
* Case studies: Three successful applications of deep learning will be discussed to motivate the study of intelligence.
* AlphaGo AlphaZero: A master of chess, shogi, and Go through self-play learning.
* AlphaFold: A deep learning-based system for protein folding in biology.
* Reinforcement Learning: A general-purpose framework for AI, with applications in deep learning.
* Reward function: The policy determines the action based on the state, and the intelligence is measured by the environment's response to the agent's actions.
* Complexity: Environment complexity impacts the success of a policy, with low complexity environments being easier to learn from.
* Alphago vs. Lee Sedol: A historic match between AlphaGo and a professional Go player in 2016.
* AlphaZero manager: Playing two games and using less human knowledge compared to AlphaGo.
* AlphaZero approach: Learning through self-play and improving over time.
* AlphaZero vs. Stockfish: Surpassing the skills of traditional chess programs.
* Alpha Zero architecture: Using a combination of policy and value networks.
* Automatic curriculum: A system that starts with weak opponents and gradually improves them to create stronger learning agents.
* Procedural generation: Creating varied environments for training AI agents.
* Population agent: Connecting multiple agents in an arena for decentralized multi-agent learning.
* Collaborative learning: Human players can work together with AI agents.
* Understanding trained agents: Agents may behave in clever ways, and understanding their internal representations is important.
* Protein folding: A complex problem that involves predicting the 3D structure of a protein from its amino acid sequence.
* AlphaFold: An improved protein structure prediction system using deep learning.
* Deep search space: The vast number of possible configurations in protein folding makes it a challenging problem for AI to solve.
* AlphaFold architecture: Using a combination of convolutional and recurrent neural networks.
* CASP assessment: A competition that provides benchmarks for evaluating the performance of protein folding systems.
* Deep learning in protein folding: Experimental methods can be used to determine the structure of a protein using deep learning.
* AlphaFold system: Generating features from raw data and using distance prediction and angle prediction to produce a score function.
* Deep dilated convolution: A component of AlphaFold's architecture that helps capture short-term and long-range interactions. * AlphaFold system work sequence: generate feature database, distance prediction, angle prediction, score function, gradient descent optimization
* Deep learning used for protein folding prediction, captures short and long-range interactions
* Gradient descent optimization of potential energy function
* Convolutional neural network (CNN) architecture with dilated convolutions and residual connections
* Self-supervised learning in deep learning for protein structure prediction
* Deep learning systems have limitations, especially in accuracy and handling large datasets
* Unsupervised learning used in deep learning for generating latent variables from data
* Generative adversarial networks (GANs) generate data that can fool discriminators into thinking they are real
* Ethical considerations of building AI systems, including the potential consequences and responsibility
* Lack of data efficiency and energy consumption as limitations of deep learning
* Flexibility and adaptability needed for AI to understand and act appropriately in various situations
* Reinforcement learning exploration problem: balancing exploration and exploitation to maximize long-term rewards
* AlphaGo and AlphaZero used to improve understanding of game playing and strategy development
* Measuring and optimizing performance in deep learning through experimentation and feedback.


## DeepMind x UCL | Deep Learning Lectures | 2/12 |  Neural Networks Foundations

URL: [https://www.youtube.com/watch?v=FBggC-XVF4M](https://www.youtube.com/watch?v=FBggC-XVF4M)

 * The speaker will talk about neural networks, focusing on motivation and history
* They will cover various types of neural nets: RBMs, DBNs, Hopfield nets, Kohonen maps
* They will discuss biologically inspired neural nets and physical simulators
* They will touch upon capsule networks and graph networks
* The talk will cover the modularity of deep learning systems
* The first part will be about the motivation and high-level ideas behind deep learning
* The second part will delve into the biological intuition and mathematical foundations
* They will discuss the importance of understanding the inner workings of neural networks
* They will provide an overview of the history of neural networks and their properties
* They will explain how neural networks have become increasingly popular due to advances in hardware and data availability
* They will discuss the modularity and composition of deep learning models, using examples such as convolutional neural networks and recurrent neural networks
* They will mention the importance of understanding the mathematical reasoning behind deep learning models
* They will provide an overview of the biological intuition behind neurons and neural networks, comparing them to complex distributed computation systems. * The speaker discusses the derivative of a neuron function and how it can vanish or not matter in deep learning models
* They mention the importance of initializing models correctly and keeping track of dead units for debugging
* Deep learning models have many layers that represent different features, from simple line detection to complex shape recognition
* The speaker mentions the exponential growth of the number of neurons as more layers are added
* Computational graphs are used in deep learning to represent the relations between inputs and outputs and allow for efficient computation
* Backpropagation is a technique used to compute gradients in neural networks
* The speaker discusses the importance of handling non-differentiable functions and regularization techniques
* They mention the challenges of training large, complex models with a finite amount of data
* The speaker mentions the importance of monitoring loss during training and the use of initializations, shape assertions, and debugging techniques.


## DeepMind x UCL | Deep Learning Lectures | 3/12 | Convolutional Neural Networks for Image Recognition

URL: [https://www.youtube.com/watch?v=shVKhOmT0HE](https://www.youtube.com/watch?v=shVKhOmT0HE)

 * Convolutional Neural Network (ConvNet) for image recognition
* Background: developed in the past decade, based on convolution operation and pooling layers
* History: ImageNet Challenge competition (2010-2017), large datasets led to major innovations in computer vision
* Building Blocks of ConvNet:
  + Convolution Operation: filters image, preserves topology, reduces parameters with weight sharing
  + Locally Connected Layers: connects local regions instead of individual pixels
  + Pooling Layer: reduces resolution, computes aggregation function (max or average)
* Recent Successful Architectures: VGGNet (2014), ResNet (2015)
* Image Data Modality: similar properties to images like translation invariance and locality
* Weight Sharing and Model Hierarchy: important concepts for efficient and effective ConvNets
* Challenges in Image Recognition: large datasets, imbalance data sets, multiple objects, varying scales, object detection
* Variants of Convolution: valid convolution, strided convolution, dilated convolution, depth-wise convolution
* Pooling Operations: max pooling, average pooling
* Building Blocks Fit Together in a Neural Network: computational graph representation, fully connected layers, loss function
* Recent Architectures: LeNet-5 (early handwritten digit recognition), AlexNet (2012), VGGNet (2014), ResNet (2015)
* Innovations: large datasets, regularization strategies, value functions, dropout, batch normalization. * The use of multiple convolutional layers and pooling layers in deep neural networks was realized to be important for better performance.
* VGG Net, introduced in 2014, doubled the depth of Alex Net by adding more convolutional layers and controlling resolution reduction using pooling layers.
* PGD Net, another architecture, used different kernel sizes for different convolutional layers to create larger receptive fields.
* Batch normalization was introduced in 2015 to make optimization easier by standardizing activations across batches.
* ResNet, also from 2015, added residual connections to facilitate training of deeper networks.
* Dense Net, another architecture, connects every layer to the previous one to make backpropagation easier.
* Global context convolution was introduced in 2017 to capture both local and global patterns in an image.
* Data augmentation is used to make models robust to variations such as translation, rotation, and brightness.
* Transfer learning is an effective strategy for using pre-trained models for new tasks with limited data.
* Recurrent attention models can incorporate topological structure into input network architecture.
* Convolutional neural networks have replaced handcrafted features due to their ability to learn hierarchical representations automatically.
* Prior knowledge and higher level abstractions are still being incorporated into deep learning architectures for better performance.


## DeepMind x UCL | Deep Learning Lectures | 4/12 |  Advanced Models for Computer Vision

URL: [https://www.youtube.com/watch?v=_aUq7lmMfxo](https://www.youtube.com/watch?v=_aUq7lmMfxo)

 * Speaker discusses going beyond image classification in computer vision
* Classification models can only identify objects in specific images, not understand the scene as a whole
* Scene understanding is important for various applications: visually impaired people, AR/VR, robotics, autonomous vehicles
* Challenges include different tasks (object detection, pose estimation), input and output structures, prior knowledge
* Classification vs regression: classification maps input to predefined classes, regression maps input to continuous values
* Object detection involves detecting and localizing objects in images, often using a bounding box prediction
* Bounding box prediction can be done through regression instead of classification for continuous output
* Two-stage object detection: first rough classification, then refinement through regression
* RetinaNet is an example of a one-stage object detector that performs both classification and regression in a single pass
* Semantic segmentation involves assigning class labels to every pixel in an image
* Evaluation methods for object detection and semantic segmentation differ: object detection uses accuracy, intersection over union (IoU), while semantic segmentation may use different measures like Jaccard index or Dice coefficient. * Speaker discusses using networks for image recognition, specifically in the context of recovering blindness and object recognition
* Mentioned experiment with patients recovering sight after surgery and testing their visual ability using images
* Discussed importance of understanding two separate objects in a scene and how motion can help learning
* Mentioned challenges of using single image input for models and benefits of pair image input, specifically optical flow estimation
* Talked about generating labels automatically and the importance of motion in object recognition
* Discussed using video input instead of static images and the need for parallel processing and efficient algorithms
* Mentioned the challenge of obtaining labels for large datasets and the use of transfer learning
* Discussed the energy consumption of models and the need to improve efficiency
* Talked about going beyond strong supervision in training models
* Mentioned using triplet loss for training systems and the importance of selective sampling.


## DeepMind x UCL | Deep Learning Lectures | 5/12 |  Optimization for Machine Learning

URL: [https://www.youtube.com/watch?v=kVU8zTI-Od0](https://www.youtube.com/watch?v=kVU8zTI-Od0)

 * Lecture on optimization methods for machine learning, specifically neural networks
* Divided into five sections: introduction, basic methods, stochastic optimization, second order methods, and advanced techniques
* Motivation: optimization methods enable models to learn from data by adapting parameters to minimize objective functions
* Basic methods: gradient descent, momentum method, and other modifications
* Gradient descent: simple optimization algorithm that updates parameters based on negative gradients of the objective function
* Momentum method: modification of gradient descent that uses previous velocity to accelerate convergence along low curvature directions
* Stochastic optimization: optimization algorithms for large datasets where only a subset of data is used at each iteration
* Second order methods: optimization algorithms that use information about the Hessian matrix to improve convergence rate
* Advanced techniques: Nesterov momentum, trust region methods, and others.  * The speaker discusses optimization methods in machine learning, specifically comparing deterministic and stochastic methods.
* Deterministic method minimizes the objective function locally using gradient descent or its variants (steepest descent, momentum method).
* Stochastic method uses mini-batches to estimate gradients and converges more slowly than deterministic method.
* Kronecker product method is a way to approximate large matrices and improve optimization in neural networks.
* The speaker mentions the importance of initializing weights carefully in deep learning and the role of batch normalization and skip connections.
* Regularization methods are used to prevent overfitting and improve optimization performance, but there is disagreement on their effectiveness.
* The loss surface in deep learning is often assumed to be convex quadratic within a vicinity of a good initialization point.
* Stochastic method converges to a solution more slowly than deterministic method, which may not find the minimum in every case.
* The speaker mentions the importance of variance and its relationship to learning rate and batch size in optimization.
* Variance reduction techniques can help reduce the variance of gradient estimates in stochastic methods.
* Data processing in machine learning models can be complex and detrimental, but there may be potential benefits to exploring new methods.


## DeepMind x UCL | Deep Learning Lectures | 6/12 | Sequences and Recurrent Networks

URL: [https://www.youtube.com/watch?v=87kLfzmYBy8](https://www.youtube.com/watch?v=87kLfzmYBy8)

 * Speaker is discussing sequential data and its importance in machine learning
* Sequential data deals with variable length, order-dependent data
* Feedforward neural networks deal with fixed size vectors, not well suited for sequential data
* Convolutional neural networks can handle non-fixed size inputs but don't take structure into account
* Modeling sequence probability is difficult and time-consuming
* Engram models are a way to preserve long term dependencies in language modeling
* Recurrent Neural Networks (RNNs) are used for sequence modeling, they store information in hidden states and update them based on the current input
* RNNs have the vanishing gradient problem, making it difficult to learn long-term dependencies
* Long Short-Term Memory (LSTM) networks are a type of RNN that can keep multiple internal states and forget or add new information based on the current input
* LSTMs use gates to regulate the flow of information and prevent the vanishing gradient problem.
* LSTMs have been used for sequence learning tasks such as language modeling, speech recognition, and machine translation. * Long Short-Term Memory (LSTM) is a type of Recurrent Neural Network (RNN) used for dealing with sequential data
* LSTM has the capacity to remember information for longer periods without the vanishing gradient problem
* LSTM has gating mechanisms: input gate, output gate, and forget gate
* GRU (Gated Recurrent Unit) is a simplified version of LSTM
* LSTM can learn and store relevant information for later use
* LSTM models are used in machine learning research to overcome the vanishing gradient problem
* Auto-regressive models generate sequences by predicting next word based on previous words
* Image sequence models, such as pixel RNN, model probability of a pixel given previous pixels using chain rule
* Google Neural Machine Translation (GNMT) is an example of a successful application of LSTM in machine translation
* Wavenet is another successful application of RNN and convolution for generating audio text
* Transformer models focus on attending to a subset of the input instead of processing it sequentially like RNNs
* GPT-2 is a large transformer-based language model that generates good language and adapts style and content
* LSTM and transformer models are important in machine learning for natural language generation and audio text generation tasks.


## DeepMind x UCL | Deep Learning Lectures | 7/12 |  Deep Learning for Natural Language Processing

URL: [https://www.youtube.com/watch?v=8zAP2qWAsKg](https://www.youtube.com/watch?v=8zAP2qWAsKg)

 * The speaker is discussing deep learning and language understanding, focusing on the Transformer model
* Neural computation and deep learning have been producing impressive results in natural language processing (NLP)
* Transformer model, released in 2018, has been particularly successful in NLP applications like machine translation and speech synthesis
* The Bird model demonstrates the unsupervised learning ability of neural language models
* DeepMind is working on grounded language learning to enable a language model to interact with a simulated environment
* Language processing depends on context, as shown by examples like "Jack Jill went up the hill"
* Early perceptual processes inform how symbols are mapped and processed in the brain
* Interaction between words can be complex and may require considering wider context
* The Transformer model uses self-attention to process language effectively
* The Transformer model contains a distributed representation of words, with each word having its own vector representation
* Self-attention operation applies weights equally to every word input
* Multihead attention allows the model to attend to different aspects of the input simultaneously
* Skip connections allow the model to bypass computation in certain cases for efficiency
* The Transformer model is expressive and can handle a wide range of applications. * The speaker discusses the Transformer model and its ability to understand language context, with a focus on positional encoding and self-attention mechanisms.
* Transformers have strong awareness of word order and can learn word meaning based on context, but they don't allow developers to transformer input directly like recurrent neural networks (RNNs).
* Positional encoding is a trick used to determine the position of words in a sentence, allowing the model to pay attention to relationships between certain wave lengths and distances across the input.
* Transformers perform better than LSTM models for language tasks because they don't require the gradient path to connect two word units directly, resulting in shorter average recurrent neural network computations.
* The speaker discusses BERT (Bidirectional Encoder Representations from Transformers), a pre-trained transformer model that can understand different types of language tasks and improve performance when fine-tuned on specific tasks.
* Transfer learning is an important aspect of BERT, as it allows the model to transfer knowledge learned from one task to another, making it more effective at understanding language in general.
* The speaker also discusses the importance of balancing existing knowledge with new information and the role of unsupervised knowledge extraction in language understanding.
* They mention Helmholtz's influential paper on predicting an agent's perception of its environment, which is relevant to understanding how language models can learn from experience and interact with their surroundings.


## DeepMind x UCL | Deep Learning Lectures | 8/12 |  Attention and Memory in Deep Learning

URL: [https://www.youtube.com/watch?v=AIiwuClvH6k](https://www.youtube.com/watch?v=AIiwuClvH6k)

 * Attention is a mechanism in deep learning that allows selective focus on specific parts of data
* It is useful for human cognition, allowing us to focus on one thing while ignoring others in our environment
* In neural networks, attention can be implicit or explicitly defined
* Implicit attention is learned from the network's internal representations and can be analyzed using the Jacobian matrix
* External memory is used to provide selective recall of information based on attention
* Transformer models use variable computation time for attention mechanisms
* Attention allows neural networks to focus on specific parts of data, ignoring irrelevant details
* Implicit attention is present in all neural networks but can be made explicit for analysis and training purposes
* Explicit attention requires making hard decisions about which parts of the data to focus on and ignore
* Softmax function can be used to make these decisions probabilistically
* Attention can be applied to recurrent neural networks as well as feedforward networks
* Neural attention models use an extra output vector to represent attention, which can be used to define a distribution over the input data
* Attention mechanisms have been shown to improve performance in various applications, including image classification and handwriting recognition. * Attention mechanism helps make decisions by focusing on specific parts of data
* Recurrent neural networks (RNNs) and attention mechanisms are commonly used together
* Soft attention mechanism is a popular attention mechanism that gives weight to different parts of data based on relevance
* Introspective attention is a type of attention mechanism that focuses on internal memory and cognitive processes
* Neural Turing machines (NTMs) use attention mechanisms to read, write, and modify memory in a controllable way
* Location-based attention is a type of attention mechanism used in handwriting synthesis and other tasks
* Content-based attention is another form of attention mechanism that uses the meaning or context of data to focus on specific parts
* Transformers are a type of deep learning model that use self-attention mechanisms to process sequences of data
* Adaptive computation time is an idea that allows neural networks to spend more time processing difficult decisions
* Recursive transforms are a way of dividing and enacting transformations on data in a recurrent manner
* The universal transformer is a model that applies self-attention mechanisms across all levels of the network
* Adaptive computation time can help neural networks learn long sequences and make better predictions. * The speaker discussed time processing context prediction using Transformer model
* Idea is to build an information network for making predictions
* Adaptive computation time is a nice combination for the Universal Transformer model
* Case study: baby dataset with series of sentences entered along x-axis
* Input and context networks need to know the question being asked (e.g., "Apple, bathroom?")
* Example sentences: Apple went to office, John dropped Apple, etc.
* Important parts of sequence are identified via adaptive computation time in Bhayya transformer model
* Lecture selective attention is useful in deep learning and can be learned implicitly or explicitly
* Different types of attention mechanisms defined (stochastic hard attention, soft attention)
* Attention mechanism allows the network to attend to memory internal state
* Last year, excellent results were achieved in sequence learning using attention with transformer models.


## DeepMind x UCL | Deep Learning Lectures | 9/12 |  Generative Adversarial Networks

URL: [https://www.youtube.com/watch?v=wFsI2WqUfdA](https://www.youtube.com/watch?v=wFsI2WqUfdA)

 * Generative Adversarial Networks (GANs) are a type of generative model that learn the underlying data distribution and generate new samples by training two models: a generator and a discriminator.
* The generator learns to generate new samples, while the discriminator learns to distinguish between real and generated samples.
* GANs can learn statistical properties of the original data without explicitly modeling its probability distribution.
* Implicit generative models like GANs generate new samples without giving access to the underlying model or distribution.
* GANs have been successful in generating high-quality images, such as photorealistic faces and high-resolution images.
* The generator and discriminator are trained using a min-max game, where the generator aims to maximize the probability of the discriminator misclassifying generated samples as real, and the discriminator aims to maximize its ability to correctly classify real and generated samples.
* GANs have been used for various tasks such as image synthesis, style transfer, and data augmentation.
* The training process involves updating both the generator and discriminator in alternating steps using stochastic gradient descent.
* The loss function for GANs is based on the difference between the probability distribution of real and generated samples.
* GANs have been shown to be able to learn complex data distributions, but they can also suffer from issues such as mode collapse and instability during training.
* There are various extensions and modifications to GANs, such as using different loss functions, adding regularization terms, and using different architectures for the generator and discriminator.
* GANs have been shown to be effective in various applications, including image generation, video synthesis, and text generation.
* The talk also discusses related concepts such as maximum likelihood estimation, KL divergence, and optimization methods used in training GANs. * GANZ people discussed metrics for evaluating GANs, specifically Inception Score
* Inception Score measures model's ability to generate realistic samples by comparing output distribution with known data distribution
* Model preserving class ratio is important to avoid mode collapse and ensure diversity in generated samples
* Laplacian Pyramid method was mentioned as an approach to improve sample quality
* Single generator, single discriminator model (Spectrally Normalized GANs) was proposed to stabilize training by clamping singular value discriminator weights
* Projection Discriminator was introduced to handle conditioning and train classifier directly on class embeddings
* Self-attention technique was mentioned for global reasoning in the image domain
* Truncation trick was discussed as a tradeoff between variety and fidelity, allowing control over sample generation
* BigGAN architecture was presented with deeper yet efficient architecture and onebyone convolution to lower channel count
* StyleGAN was introduced as capable of generating remarkably photorealistic face images using a structured latent input and spatial noise input. * The speaker discusses unsupervised representation learning using GANs (Generative Adversarial Networks)
* InfoGAN was an interesting paper from the previous year that added inference network to recover latent codes
* InfoGAN maximizes information content between latent variable and image output, allowing for meaningful order and variation of style, size, rotation, etc.
* Disadvantage: representation learning doesn't have ground truth latent associated with real images like generated images
* Adversarial approaches like adversarial E-learning and bidirectional GANs compare to regular GAN setup
* Eve network learns inverse mapping of generator's output to image data
* Generative models suffer from domain shift, but encoders never suffer since they don't explicitly communicate with the generator during training
* Feature learning is a benefit of using encoders in GANs
* Discriminator's job is to figure out which process generated the input tuples (encoder or generator)
* Global optimum model doesn't hold perfectly, as reconstructions may capture semantics but not every pixel value exactly
* Nearest neighbor data set validation shows that reconstructions are semantically relevant even if they don't look identical to inputs
* GANs have been used for image-to-image translation (satellite images to maps, horse to zebra, etc.)
* CycleGAN enforces cycle consistency to translate between two domains without paired samples
* GANs are being applied to various domains like audio synthesis, text-to-speech, video prediction, image editing, program synthesis, and human-machine collaborative art.


## DeepMind x UCL | Deep Learning Lectures | 10/12 |  Unsupervised Representation Learning

URL: [https://www.youtube.com/watch?v=f0s-uvvXvWg](https://www.youtube.com/watch?v=f0s-uvvXvWg)

 * Irina and Mihaela discuss the role of unsupervised representation learning in deep learning.
* Unsupervised learning is important for solving various tasks, especially when external supervision is not available.
* Historical background: machine learning has relied on handcrafted feature engineering since the 1940s, but deep unsupervised representation learning became popular around 2006 with the rise of deep neural networks.
* Unsupervised learning can be used for preprocessing to improve interpretability and solve subsequent supervised tasks.
* Major techniques in unsupervised representation learning include clustering, dimensionality reduction, and self-supervised learning.
* Challenges in unsupervised learning include evaluating the quality of the learned representations, generalization across different tasks, and robustness to adversarial attacks.
* Current deep supervised reinforcement learning algorithms lack the ability to generalize across irrelevant variations and have poor transferability.
* Future research directions include developing more efficient and robust unsupervised representation learning methods, such as semisupervised learning and transfer learning.
* Representation learning is crucial for machine learning success since it allows adapting to new challenges with minimal data and observation.
* Neuroscience and physics provide inspiration for designing good representations, emphasizing the importance of compositionality and symmetry.
* Generative modeling is a popular representation learning technique that preserves temporal and spatial data consistency.
* Self-supervised learning uses information from the data modality (e.g., image or audio) to learn representations without labels.
* Semisupervised learning can be used when only unlabeled data is available, and it often involves training a simple classifier on top of the learned representation.
* A standard benchmark for evaluating semisupervised learning is the ImageNet dataset.
* Representation learning allows adapting to new experiences and tasks, making it essential in reinforcement learning and continual learning.
* Disentangled representations aim to separate latent variables that correspond to different aspects of the data.
* Interpretable models are desirable for understanding and deploying machine learning systems in production. * Representation learning: encoding information from data for various tasks
* Generative modeling: generating new data based on a probability distribution
* Latent variable models: assuming generative process looks like high-dimensional data, using deep neural networks to learn mapping to low-dimensional space
* Variational inference: optimizing lower bound objective instead of original maximum likelihood objective for complex models
* Disentangled representation: separating latent variables for different aspects of data
* Transfer learning: applying learned representations to new tasks or domains
* Unsupervised learning: learning from raw data without labeled examples
* Reinforcement learning: learning through interactions with an environment to maximize rewards
* Downstream tasks: using learned representations for specific tasks, such as classification or generation
* Data efficiency: making the most of limited training data
* Discrete vs continuous representation: trade-offs between compressibility and expressiveness
* Neural scene representation: encoding information about 3D scenes and objects
* Adversarial learning: training models to generate realistic data that can fool other models
* Contrastive learning: maximizing agreement between representations of similar examples and minimizing agreement between dissimilar ones
* CPC (Contrastive Predictive Coding): a type of contrastive learning method for unsupervised representation learning
* Architectural perspective: using different neural network architectures and training methods to learn representations
* Spatial data: handling spatial relationships in images or other data types
* Temporal coherence: preserving consistency over time in learned representations
* Self-supervised learning: learning from unlabeled data through pretext tasks
* Classification vs regression: choosing the appropriate task for a particular dataset and representation learning method
* Adversarial attacks: using adversarial examples to test model robustness and improve model defenses. * The speaker discusses various topics in image and text representation learning using deep learning models
* Gaussian noise, blur, and color distortion techniques are used to improve model performance
* Large models with hundreds of millions to billions of parameters have been seen to perform better than smaller ones
* Self-supervised learning is a powerful approach for encoding information from unlabeled data
* Representational learning using semisupervised learning and temporal coherence has been effective in downstream tasks such as classification, object recognition, and action recognition
* Long term temporal coherence and structure are important for representation learning in both image and text domains
* Transformers have been used to learn local and global structure from text data
* The importance of task design and using advanced neural networks for presentation learning is emphasized.
* Self-supervised learning allows the use of domain knowledge to build useful representations
* Contrastive loss has been an important data modality in representation learning, especially in image domains
* Latent variable models and generative models have been used to learn high-dimensional representations
* Posterior methods and auto-regressive posteriors have been effective in improving model performance
* The importance of prior knowledge and causal coherence is discussed.


## DeepMind x UCL | Deep Learning Lectures | 11/12 | Modern Latent Variable Models

URL: [https://www.youtube.com/watch?v=7Pcvdo4EJeo](https://www.youtube.com/watch?v=7Pcvdo4EJeo)

 * Andrea Nick, research scientist at DeepMind, discusses generative modeling and latent variable models
* Generative modeling vs. discriminative modeling: generative modeling deals with high-dimensional distributions and generates data points based on a probabilistic process
* Latent variable models: model the joint distribution of input data and hidden variables, can be used for various applications like text, image, video generation, denoising, and compression
* Variational Inference (VI): a modern approach to approximate inference for latent variable models, allows for efficient training and inference
* VI involves estimating the gradient of the expected log likelihood with respect to model parameters
* Popular generative models: Gaussian Mixture Models (GMMs), Hidden Markov Models (HMMs), Naive Bayes, Variational Autoencoders (VAEs)
* Intractable latent variable models: require approximate inference methods like Variational Inference or Markov Chain Monte Carlo (MCMC) to make inference tractable
* Invertible models: allow for exact inference and are gaining popularity due to their ability to retain inverterability while being powerful and expressive
* Exact inference is important for understanding the generative process and making predictions, but can be computationally expensive or intractable for high-dimensional data
* Variational Inference provides a way to approximate the true posterior distribution using an approximating distribution (variational posterior) and optimizing it to minimize the KL divergence between the variational posterior and the true posterior.
* The variational lower bound is used to train the model by maximizing the lower bound on the marginal log likelihood, which is a simplified form of the original objective function that can be computed efficiently.
* Variational Inference allows for approximating marginal log likelihoods intractable models and optimizing them using gradient-based optimization methods like stochastic gradient descent (SGD) or Adam.
* VI provides a way to train generative models with complex structures, such as deep neural networks, by approximating the intractable integral over latent variables using variational distributions.
* VI has been successfully applied to various tasks, including image generation, text generation, and speech recognition.
* VI can be combined with other techniques like MCMC or importance sampling for better performance and accuracy.
* VI is an active area of research, with new methods and applications being developed constantly. * Variational Inference: optimizing lower bound using variational parameters and the concept of back-Leibler divergence
* Two terms in variational lower bound: marginal log likelihood and KL divergence between true and approximate posterior distributions
* Variational Lower Bound (VLB): maximize ELBO respecting variational parameters to get closer approximation to true posterior
* Importance of Joint Distribution in VLB derivation
* Variational Inference concepts: Back-Leibler Divergence, KL divergence, and its properties
* Optimizing variational lower bound using variational parameters and minimizing KL divergence
* Variational Pruning: reducing complexity by pruning variables, making model simpler and easier to perform variational inference
* Choices for modeling variational posterior: mixture models, multimodal distributions, rich covariance structures, or invertible models
* Amortized Inference: training a neural network to compute the variational lower bound for multiple data points efficiently
* Variational Inference techniques: reinforce likelihood ratio estimator, reparameterization trick, and Riemannian manifold optimization
* Variational Autoencoders (VAEs): generative model using continuous latent variables, trained with amortized inference and the upper motorisation trick.


## DeepMind x UCL | Deep Learning Lectures | 12/12 |  Responsible Innovation

URL: [https://www.youtube.com/watch?v=MhNcWxUs-PQ](https://www.youtube.com/watch?v=MhNcWxUs-PQ)

 * Tony Chen speaks about the importance of responsible innovation in artificial intelligence (AI)
* Discusses recent breakthroughs in machine learning, including image classification and protein folding
* Highlights ethical implications of machine learning algorithms and the need to mitigate risks
* Gives example of bias in neural networks and adversarial attacks
* Introduces specification-driven machine learning as a solution to ensure robustness and reliability
* Describes methods for evaluating adversarial robustness, including projected gradient descent and adversarial evaluation
* Emphasizes the importance of strong adversarial evaluation to ensure satisfaction of specifications
* Mentions the danger of weak adversarial evaluations giving a false sense of security
* Talks about gradient obfuscation as a way to evaluate algorithms more effectively
* Yasmin Gabriel speaks about ethics in machine learning and the importance of considering ethical implications from the start
* Discusses challenges in AI ethics, including data collection, labeling, and bias
* Emphasizes the need for transparency and accountability in machine learning systems
* Talks about responsible innovation as a paradigm for developing machine learning technology. * The speaker discusses the socially beneficial use of technology, considering both potential benefits and risks
* Technologically socially beneficial in various ways: contributes to human health and wellbeing, enhances autonomy and freedom, produces fairer outcomes, etc.
* However, technology might also harm human health and wellbeing, restrict autonomy, infringe on human rights, and lead to addictive content or algorithmic bias
* It's important to consider the ethical implications of technology use and potential mitigation strategies
* The speaker mentions specific examples like Wavenet and deep learning algorithms for synthetic audio
* Risks include voice mimicry deception, rogue public trust, and infringement on human rights
* Mitigation strategies include technical solutions, policy solutions, and mindful technology development
* It's important to consider the potential consequences of technology use and act responsibly
* Machine learning research presents tremendous opportunities but also requires constant vigilance for ethical concerns
* New norms and standards are emerging in machine learning to address safety, fairness, and accountability
* The speaker encourages responsible innovation in machine learning and creating a bias bounty to discover and address bias in models.

## RL Course by David Silver - Lecture 3: Planning by Dynamic Programming

URL: [https://www.youtube.com/watch?v=Nd1-UUMVfz4](https://www.youtube.com/watch?v=Nd1-UUMVfz4)

 * The speaker started by discussing the understanding of Markov Decision Processes (MDPs) and dynamic programming as a solution method.
* Dynamic programming is a mathematical optimization technique used to solve sequential decision-making problems.
* Policy evaluation was introduced as the first application of dynamic programming in MDPs, where an agent evaluates a given policy to determine its expected reward.
* Value iteration was presented as another approach related to policy evaluation, which directly optimizes the value function using the Bellman equation.
* The speaker mentioned that dynamic programming can be extended to handle various problems and lead to subsequent lectures on planning in MDPs.
* Dynamic programming is used to solve complex problems by breaking them down into smaller sub-problems and solving each one efficiently.
* The optimal substructure principle and optimality property were discussed as essential concepts in dynamic programming.
* The speaker planned to use dynamic programming to try and solve an MDP problem later in the course.
* Dynamic programming is widely used in various fields, including scheduling algorithms, string algorithms, graph algorithms, and machine learning models like LTI and bioinformatics.
* The speaker then focused on planning in MDPs and introduced the concept of a planning problem, which involves finding an optimal policy given full knowledge of the environment.
* Planning in MDPs can be addressed through prediction control, where the goal is to predict the reward achieved by different policies and choose the best one.
* The speaker mentioned that they would consider two special cases of planning in MDPs: prediction and control.
* In prediction, the goal is to determine the expected reward given a policy, while in control, the goal is to find the optimal policy that maximizes long-term reward.
* The speaker then provided an example of a simple grid world problem to illustrate dynamic programming concepts.
* They discussed how to use iterative policy evaluation to compute the value function for a given policy and improve it by applying the Bellman equation iteratively.
* The speaker also mentioned that there is a formal proof of the uniqueness property of the solution in MDPs, which they would cover later. * The speaker discusses policy evaluation and improvement in the context of Markov Decision Processes (MDPs)
* Jack's Car Rental is used as a real-world example to illustrate the concepts
* MDP: Markov Decision Process, state space, action space, reward function, transition probability
* Policy Evaluation: estimate value function using iterative method, Bellman Expectation Equation
* Policy Improvement: acting greedily respecting current value function, shifting cars to maximize income
* Optimal policy and value function: fundamental theorem of MDPs, convergence rate independent of initial value
* Policy Iteration: evaluate policy, improve policy, repeat until convergence
* Contraction mapping argument for understanding the algorithm's working
* Value iteration vs Policy Iteration: both methods to find optimal policy in MDPs. * The speaker is discussing methods for solving Markov Decision Processes (MDPs)
* Two types of planning problems: prediction and control
* Prediction problem: find optimal value function using Bellman expectation equation
* Control problem: find optimal policy using value iteration or policy iteration
* Value iteration: iteratively improve value function using Bellman optimality equation
* Policy iteration: iteratively improve policy using the best policy given the current value function
* Asynchronous dynamic programming: update value function in any order, not waiting for every state to be updated before moving on
* Place dynamic programming: store and use old and new value functions efficiently
* Realtime dynamic programming: use real-world experience to guide state updates
* Contraction mapping: a theoretical result showing that value iteration converges to the optimal value function.


## RL Course by David Silver - Lecture 4: Model-Free Prediction

URL: [https://www.youtube.com/watch?v=PnHCvfgC_ZA](https://www.youtube.com/watch?v=PnHCvfgC_ZA)

 * The speaker is discussing model-free prediction methods in reinforcement learning.
* Monte Carlo Learning (MCL) and Temporal Difference Learning (TD) are two major methods for model-free prediction.
* MCL uses sample returns to estimate value functions by taking the average of returns from multiple episodes. It requires the assumption that the environment is stationary, which may not hold in reality.
* TD learning looks one step ahead to estimate the return and updates the value function iteratively. It unifies the approach towards solving the value function problem.
* MCL and TD are related, but there is a distinction between planning and prediction in reinforcement learning.
* Model-free methods aim to find the optimal policy without knowing the environment dynamics or reward function.
* Monte Carlo policy evaluation uses empirical mean returns to estimate the expected return of a policy. It requires visiting each state multiple times to reduce variance.
* TD learning updates the value function based on the difference between estimated and observed returns, which is called the TD error. It can converge faster than Monte Carlo methods but may require more computational resources.
* The speaker mentions an example of Blackjack as a simplified MDP problem and explains how to represent it using state variables.
* Monte Carlo policy evaluation involves running many episodes of the game, evaluating each state based on the policy, and updating the value function accordingly. The algorithm converges to the true value function as the number of episodes increases but may be noisy for rare states or when the number of episodes is not large enough.
* The speaker mentions that Monte Carlo methods can be extended to online algorithms, where estimates are updated after each step instead of waiting for the end of an episode.
* TD learning uses bootstrapping, which involves estimating the value function based on the current estimate and the observed return, to make more efficient updates.
* The speaker mentions that both MCL and TD methods have advantages and disadvantages, with MCL being simpler but less efficient for large state spaces and TD being more complex but more efficient for smaller state spaces.
* The speaker also mentions that reinforcement learning algorithms can be developed towards online algorithms, where statistics are not maintained incrementally, and the estimates are updated after each step. * TD learning: Temporal Difference (TD) method for estimating value function
* TD0: Simplest version of TD, uses estimated return one step instead of real return
* Bellman equation: Value function equals expected reward plus discounted value next step
* TD Target: Estimate taking a step, difference between estimated and actual value
* Monte Carlo learning: Wait for end of episode to observe entire trajectory and compute return
* Advantages of TD over Monte Carlo:
  + Faster convergence as it updates at every step instead of waiting for an episode to finish
  + Can handle incomplete sequences, unlike Monte Carlo which requires the full sequence to estimate the value function
* Bias-Variance tradeoff: TD introduces bias by using an estimate for the next step's value instead of the true value, but this reduces variance compared to Monte Carlo
* TD Lambda: A variant of TD that allows choosing between shallow and deep backups according to a parameter lambda.
* Shallow vs Deep Backup:
  + Shallow backup: One-step update towards estimated value function
  + Deep backup: Full width update considering every possibility exhaustively
* Methods in reinforcement learning: Policy evaluation, policy control
* Bootstrapping: Using an estimate for the next step's value instead of the true value to update the current value estimate. * TD Lambda is a unifying algorithm for temporal difference (TD) learning, which lets us pick the best place to update values based on depth or shallowness
* TD Lambda uses a Lambda return, which is a geometrically weighted average of returns from different steps
* TD Lambda works by looking at the value function one step ahead and updating it based on the observed reward and the next estimated value
* TD Lambda can give incorrect answers in some cases, such as in stochastic MDPs where we may get the wrong answer due to the Markov property
* The intuition behind TD Lambda is that taking one step in reality always gives us a more accurate estimate than looking backwards from the current state
* TD Lambda converges like contraction math and brings us closer to the ground truth with each step
* TD Lambda can be compared to Monte Carlo learning, which uses random sampling to estimate returns, but TD Lambda is more efficient and exploits the market property of lower variance
* TD Lambda has a sweet spot around 3-5 steps for the Lambda return, where it performs best
* TD Lambda can be used in both online and offline learning, and it is robust to changes in the environment
* TD Lambda uses eligibility traces to efficiently assign credit for errors and update the value function
* TD Lambda has a forward view and a backward view, which are equivalent but have different advantages: the forward view computes end-of-episode returns and averages them, while the backward view accumulates eligibility traces and updates them efficiently
* Recent work has shown that TD Lambda can even achieve equivalence with online updating.


## RL Course by David Silver - Lecture 5: Model Free Control

URL: [https://www.youtube.com/watch?v=0g4j2k_Ggc4](https://www.youtube.com/watch?v=0g4j2k_Ggc4)

 * The speaker is discussing reinforcement learning and control in unknown environments
* Policy means learning while following behavior, while policy learning means learning while following someone else's behavior
* Starting with simpler cases, the goal is to estimate value functions and optimize policies
* Monte Carlo control and Temporal Difference Learning are methods used for policy evaluation and improvement
* Model-free control involves using tools like state value functions and Q-learning to estimate and optimize policies without knowing the underlying dynamics of the environment
* The speaker mentions various applications of reinforcement learning, including controlling elevators, self-driving cars, and playing games
* In an unknown MDP (Markov Decision Process), model-free control can be useful when sampling is the only way to access the model
* Real-world examples of complex systems that could benefit from model-free control include atomic-level simulations and controlling a bioreactor
* The speaker discusses the dichotomy between policy learning and policy improvement, and how they are related
* Policy iteration involves alternating between evaluating and improving policies
* Monte Carlo methods can be used for policy evaluation and improvement in a model-free setting
* Epsilon-greedy exploration is a simple way to ensure exploration while making progress towards finding the best policy. * The speaker discusses various reinforcement learning algorithms, focusing on Q-learning and SARSA
* Q-learning estimates the value of a state-action pair by taking actions and observing rewards and next states
* SARSA (State-Action-Reward-State-Action) is an extension of Q-learning that uses eligibility traces to estimate the value of a state-action pair based on the most recent reward received
* Eligibility traces keep track of how recently each state-action pair has been visited and decay over time
* The speaker discusses the advantages of online learning, which allows for immediate updates as new data becomes available
* TD(Lambda) is a variant of Q-learning that uses eligibility traces with discounting to estimate the value of a state-action pair based on the sum of rewards received along a trajectory
* The speaker discusses the importance of choosing an appropriate Lambda parameter, which determines how far back in the trajectory to consider rewards when updating the Q-value
* The speaker mentions that using a large Lambda parameter allows for faster information flow backwards along the trajectory and can help overcome the "tyranny of the time step"
* The speaker also discusses the importance of tuning the Lambda parameter to balance control bias, variance, and the SU effect (bootstrapping error)
* The speaker mentions that in online learning, updates are made every single step based on the most recent reward received, even if the episode is not yet finished. * The speaker discusses forming estimates of expected reward in reinforcement learning
* Two methods mentioned: Monte Carlo and Temporal Difference (TD) learning
* Monte Carlo learning forms true mean by using the count of number of times a state-action pair has been visited
* TD learning uses bootstrapping to form an estimate of the expected reward based on the current value estimation
* Importance sampling is mentioned as a mechanism for estimating expectations in Monte Carlo learning
* The speaker mentions the equivalence between backward and forward views in reinforcement learning
* Discusses the use of eligibility traces and Q matrices in reinforcement learning
* Mentioned the need to treat behavior generated data like human experience in policy learning
* Discussed the importance of exploring state space effectively in reinforcement learning
* Importance sampling mentioned as a problem in reinforcement learning due to its high variance
* TD learning recommended as an alternative to Monte Carlo learning for efficiency
* Q Learning, specifically Q(TD)0 algorithm, mentioned as an example of an efficient policy learning method that doesn't require importance sampling.


## RL Course by David Silver - Lecture 6: Value Function Approximation

URL: [https://www.youtube.com/watch?v=UoPei5o4fps](https://www.youtube.com/watch?v=UoPei5o4fps)

 * Welcome to lecture on scaling reinforcement learning
* Goal: Understand how to build efficient methods for representing value functions in large state spaces
* Two approaches: Incremental method and Data-efficient method
* Incremental method: Update value function online as new data comes in using a function approximator like a neural network
* Data-efficient method: Use all available data to fit the value function exactly
* Value function approximation methods: State-value function, Policy-space methods
* State-value function: Estimate the value of taking a specific action in a given state
* Policy-space methods: Evaluate policies directly instead of estimating values for every state-action pair
* Incremental method challenges: Memory requirements, slow learning with large data spaces
* Data-efficient method challenges: Need to store and process all available data, memory usage, potential overfitting
* Function approximators: Linear combination feature neural network, nonlinear function approximators (neural networks)
* Gradient-based methods for training function approximators
* Stochastic gradient descent (SGD) for incremental value function approximation
* Batch methods (Least Squares Method) vs Online methods in reinforcement learning
* Linear combination feature representation: Simplifies the learning problem, makes it easier to represent value functions
* Nonlinear function approximators: More sophisticated but require more computational resources
* Quadratic objective function for linear value function approximation
* Update rule: Change weights based on the error between estimated and true values
* Linear combination feature optimization: Easy to optimize using standard optimization methods, less likely to get stuck in local optima
* Cheating with an Oracle: Imagining the existence of an oracle that provides the correct answers is not practical in reinforcement learning
* Monte Carlo temporal difference learning method: Estimates value functions by using returns from random trajectories
* Target estimation: Use function approximator to estimate target values instead of relying on an oracle
* TD Learning: Use different targets for estimating value functions and update the approximator towards the estimated target
* TD Lambda: Interpolates between TD(0) and Monte Carlo learning, treats the target as a function approximator
* Stochastic gradient descent converges to the optimum in reinforcement learning, but may be slow with nonlinear value function approximation. * The speaker discusses various methods for reinforcement learning, including Monte Carlo learning, TD (Temporal Difference) learning, and Q-learning.
* Linear function approximation is used in these methods to estimate value functions.
* Monte Carlo learning involves generating data from the environment and using it to estimate values. It provides an unbiased estimator but may be slow.
* TD learning estimates the difference between predicted and actual rewards to update the value function. It can converge to the optimal value even with bias.
* Q-learning is a variant of TD learning that uses action-value functions instead of value functions. It requires exploration strategies to ensure adequate sampling of the state-action space.
* The speaker mentions various techniques for improving convergence and reducing bias, such as using eligibility traces, gradient methods, and function approximation with neural networks.
* The speaker also discusses challenges in reinforce learning, such as catastrophic divergence and chattering policies.
* Batch methods are mentioned as an alternative to online methods, where the agent collects a large dataset of experiences before updating its policy.
* The speaker emphasizes the importance of understanding the underlying theory and practice of reinforcement learning algorithms.

No context. * The speaker discusses minimizing sum squared error using least squares solution and experience replay method
* Experience replay involves making the dataset explicit, sampling experiences, and optimizing with stochastic gradient descent
* Least squares solution is simple but can be unstable, while experience replay stabilizes neural networks by decorrelating trajectories
* Recent work in Atari used experience replay for Q-learning and policy improvement
* Experience replay helps stabilize the algorithm and improve performance in various games
* Linear function approximation with a big neural network is used to estimate Q values and make decisions greedily
* The speaker discusses the importance of experience replay in RL, particularly in using a big convolutional neural network for Atari games.


## RL Course by David Silver - Lecture 7: Policy Gradient Methods

URL: [https://www.youtube.com/watch?v=KHZVXao4qXs](https://www.youtube.com/watch?v=KHZVXao4qXs)

 * The speaker is discussing reinforcement learning, specifically the policy gradient method.
* Policy gradient method optimizes policy directly instead of working with value functions.
* It adjusts policy direction by following the gradient in the direction that makes the policy better.
* Different methods for policy gradient include Nieve, numerical approach using finite difference, and act-critic method.
* The speaker discusses the advantages of policy gradient over value based methods like Q-learning.
* Policy gradient can handle continuous action spaces and high dimensional state spaces more effectively than value based methods.
* It is useful for learning stochastic policies and handling partial observability in Markov Decision Processes (MDPs).
* The speaker mentions the importance of feature representation in policy gradient methods.
* He discusses the use of likelihood ratio trick to compute policy gradients analytically.
* Policy gradient methods can be used for optimization problems, not just reinforcement learning.
* The speaker provides an example of using policy gradient to optimize a robot's gate opening speed in Robocop soccer.
* He mentions the challenges of implementing policy gradient methods and the importance of efficient computation. * The speaker discusses the policy gradient method and its use in reinforcement learning
* Policy gradient involves adjusting the policy to maximize the expected reward
* Score function tells us how much better an action is compared to the current policy
* Policy gradient update involves taking a step in the direction of the gradient of the expected reward with respect to the policy parameters
* The likelihood ratio trick can be used to recover the gradient of the objective function
* Monte Carlo policy gradient is a simple algorithm that uses samples to estimate the gradient
* Actor-critic methods combine value function approximation and policy gradient methods
* Advantage functions are used in actor-critic methods to estimate the advantage of taking a particular action in a given state
* TD error is used to estimate the advantage function, which can be plugged into the policy gradient theorem to update the policy
* Eligibility traces can be used to make the algorithm more efficient by remembering past rewards and actions.
* The speaker discusses eligibility traces and their role in making the critic effective in actor-critic methods
* Eligibility traces help update the policy direction based on the largest recent reward frequently
* They are a way to understand analogy between eligibility trace value and update in value-based reinforcement learning
* Eligibility traces make the actor make use of the critic in many different ways
* The idea is to build a toolkit to help make the critic effective
* Eligibility traces can be used with various types of function approximators without introducing bias
* The speaker mentions the importance of compatible function approximation and using features and score functions
* They guarantee that the policy still follows the true gradient direction
* The speaker briefly touches on the idea of noisy policies and the challenges of estimating policy gradients in such cases
* Deterministic policy gradients are an alternative to traditional policy gradient methods
* Different manipulations of actor-critic algorithms include using different approximation techniques, score functions, and value functions
* The speaker mentions various algorithms from the Monte Carlo, Temporal Difference (TD), and lambda families as alternatives considered in previous lectures.


## RL Course by David Silver - Lecture 9: Exploration and Exploitation

URL: [https://www.youtube.com/watch?v=sGuiWX07sKw](https://www.youtube.com/watch?v=sGuiWX07sKw)

 * Lecture on exploration and exploitation in reinforcement learning
* Balancing exploration and exploitation: figuring what's best in the world while learning effectively
* Simplified version of reinforcement learning problem: multi-armed Bandit problem
* Multi-armed Bandit: pick one action, get one reward, explore to find the best action
* Exploration vs. exploitation dilemma
* Three approaches to exploration: random, systematic, and careful
* Random exploration: Epsilon greedy, randomly choose an action with a certain probability
* Systematic exploration: optimism face uncertainty, prefer the action with the highest estimated value
* Careful exploration: explore systematically, figure out which part of the state-action space hasn't been explored yet
* Multi-armed Bandit setup: simplified MDP framework, set action reward function R, estimate Q value for each arm
* Regret: difference between the amount of reward we got and the maximum possible reward
* Gap: difference in value between the best and second-best arm
* Exploration-exploitation tradeoff: keeping a balance between exploring new arms and exploiting known good arms
* Importance of exploration: identifying the best arm and minimizing regret
* Optimistic initialization: initialize all values to be maximum possible, then update as data comes in
* Epsilon-greedy algorithm: pick the action with the highest estimated value most of the time, randomly explore the rest of the time
* Softmax policy: use a probability distribution over actions based on their estimated values
* Decaying Epsilon: gradually decrease the exploration rate over time
* Exploration schedule: explore more when the gap between the best and second-best arms is large, and less when it's small. * The speaker introduces the Epsilon-greedy algorithm and its properties, mentioning that it achieves a nice property called the lower bound in the context of bandit problems
* They discuss the concept of regret and how algorithms try to minimize it
* The speaker mentions that the hardest problem is when arms have similar distributions
* They introduce the Upper Confidence Bound (UCB) algorithm as an approach that achieves logarithmic regret
* UCB uses optimism in the face of uncertainty principle, which suggests not taking the currently believed best arm and instead trying potential best arms
* The speaker compares UCB to Epsilon-greedy with a decaying schedule and mentions that UCB performs better without requiring knowledge of the problem schedule
* They mention that UCB is difficult to tune but performs well in practice
* The speaker briefly touches on Thompson Sampling, another algorithm for exploration in bandits
* They discuss the concept of probability matching, which selects actions according to their probability based on the current belief
* They introduce Thompson Sampling as a method that uses probability distributions and updates them with new data
* The speaker mentions that Thompson Sampling is parameter-free and achieves optimal performance in some cases
* They discuss the impact of situation change, specifically budget constraints, on bandit problems and algorithms
* They mention that Bayesian Bandits are good at utilizing prior knowledge but may not deal well with sequential information in full MDP cases. * The speaker discusses the concept of Bandit problems and MDPs (Markov Decision Processes)
* Bandits: different possible information states, explore vs. exploit, example: pharmaceutical drug testing
* Information state: summarized statistics of past actions and outcomes
* Dynamic programming solution for Bandit problem using look-ahead tree search
* Base adaptive reinforcement learning: characterizing posterior distribution, Bayesian approach
* Monte Carlo Tree Search as a tractable approach for large state spaces
* Contextual Bandits: extending multi-arm Bandit problem with contextual information
* Upper Confidence Bound (UCB) approach for exploration in MDPs and RL
* Importance of considering uncertainty in RL, optimism face uncertainty principle
* Extending full MDP case to include uncertainty, internal methods
* ARAX algorithm: systematic exploration, EB variant
* Augmented state space: combining information to create bigger, more complicated MDPs
* Solving augmented MDPs using various methods (Monte Carlo tree search)
* Exploration-exploitation dilemma and its progression from random to systematic approaches
* Multi-arm Bandits, contextual Bandits, and their combination in reinforcement learning
* Final lecture notice: non-examinable material, taking place next week, check website for details.


## Deep Learning 1: Introduction to Machine Learning Based AI

URL: [https://www.youtube.com/watch?v=iOh7QUZGyiU](https://www.youtube.com/watch?v=iOh7QUZGyiU)

 * Torie Grable from DeepMind UCL discusses machine learning course collaboration between UCL and DeepMind
* Course covers deep learning and reinforcement learning, with a focus on general artificial intelligence
* Team includes Cora Hado, Alex Davies, Deana Borsa, Marie, and others
* Format includes assessments in two streams: deep learning and reinforcement learning
* Course materials include assignments, programming problems, and collab notebooks
* Collaborative Jupyter Notebook environment provided with pre-configured cloud resources for students
* Schedule includes guest lectures on Tuesdays for deep learning topics and Thursdays for reinforcement learning
* Coursework consists of four deep learning and four reinforcement learning assignments spread across the module, with equal weighting towards final grade
* Assessments include written exams and programming assignments, with a focus on practical problem-solving rather than theoretical exams
* Students need to order collaborative resources through a whitelisted email address provided by UCL
* Support is available through Moodle forum and lecturer/TA office hours. * Breakthrough in reducing error rate with large convolutional neural networks (CNNs)
* Human performance surpassed on ImageNet dataset
* CNNs applied to text data using one-dimensional grids and shift invariance
* Deep learning viewed as a new programming paradigm with building blocks like convolutional, memory, attentional, and fully connected modules
* Recent advances in reinforcement learning for human-level control
* Reinforcement learning challenge: rich visual domain, many different games, and unified family problem
* Q-learning and deep Q networks (DQNs) used to learn optimal policies for Atari games
* DeepMind's AlphaGo project, which uses deep learning and reinforcement learning, has been successful in various domains including Go and chess
* Lifelong learning is a challenging problem in AI, especially protecting learned weights when transferring concepts between domains
* Deep learning approaches to computer vision and natural language processing have led to significant progress in these areas.


## Deep Learning 2: Introduction to TensorFlow

URL: [https://www.youtube.com/watch?v=JO0LwmIlWw0](https://www.youtube.com/watch?v=JO0LwmIlWw0)

 * Tense Flow: a test flow framework for executing computational graphs across various hardware
* Computational graph: an abstract representation of computation, consisting of a collection of primitive operations and their dependencies
* Advantages: dependency-driven scheduling, efficient use of hardware resources, and support for general forms of computation including stateful, conditional, iterative, and synchronous computations
* Declarative vs imperative programming: declarative programming describes the desired result, while imperative programming specifies the order in which operations should be executed
* Computational graph declaration and execution: using TensorFlow's TF graph object and Python utility functions to define and execute a subset of a dense flow program within the TensorFlow framework
* Variables and tensors: defining variables and their initial values, updating them within computational graphs, and reading them using within compositional graphs
* Session initialization and execution: manually initializing variables before executing a session, and using TensorFlow's monitor session to automatically initialize variables without boilerplate code
* Data feeding: using placeholders in the graph declaration to inject data during execution, and specifying feed dictionaries to provide different input values for each execution. * The speaker discusses implementing a Fibonacci sequence using TensorFlow, focusing on core functionality and computational graph
* TensorFlow is powerful for handling complex computations and supports multithreaded execution, distributed execution, and automatic placement of operations across devices
* The speaker mentions the importance of defining the core equation in TensorFlow and the use of higher-level abstractions like dynamic RNNs
* TensorFlow provides built-in functions for various situations, such as handling sequential data, time series predictions, and reinforcement learning
* The speaker discusses the benefits of using TensorFlow for deep learning applications, including its flexibility and support for a wide range of use cases
* They also mention the importance of understanding TensorFlow's lower-level functionality and how to use it effectively
* The speaker mentions some popular libraries like SONET and Karis that work with TensorFlow and provide additional features
* They discuss the benefits of using TensorFlow for research and development, including its ease of use and integration with Google Cloud services like Colab.

Some key points:

* TensorFlow is a powerful library for handling complex computations, especially in deep learning applications
* It supports multithreaded execution, distributed execution, and automatic placement of operations across devices
* Its declarative approach to defining computational graphs makes it easy to understand and debug complex functions
* Higher-level abstractions like dynamic RNNs make it easier to build complex models with less boilerplate code
* TensorFlow's built-in functions support a wide range of use cases, from handling sequential data to reinforcement learning. * The speaker mentions that resetting the default graph in TensorFlow is a useful debugging mechanism when things don't get executed
* They demonstrate a simple linear regression model and explain that generating random data with noise can make the graph complicated
* They suggest making sure everything is set up correctly before trying to debug, as debugging can be notoriously hard
* They show how to view operations within the TensorFlow graph by double-clicking on entities
* They mention using TensorBoard for visualization, but it requires proper setup and an internet connection
* Opening a playground in Google Colab allows playing around without saving variables, which can help with debugging
* Using named scopes and commenting code is good practice for debugging in Python
* Long-running jobs in Collab should be monitored to ensure nothing fails and progress is being made
* Losing an internet connection can cause issues with running a kernel and losing state, so it's important to be careful
* They apologize for not being able to provide code examples for some topics and express hope that UCL (University College London) has good internet connection.


## Deep Learning 3: Neural Networks Foundations

URL: [https://www.youtube.com/watch?v=5eAXoPSBgnE](https://www.youtube.com/watch?v=5eAXoPSBgnE)

 * Simon Senderos lecture on neural networks and deep learning
* Backpropagation and training a network
* Neural networks are simple, composed of linear transforms and nonlinear functions
* Training involves optimizing the loss function with various gradient optimization methods (e.g., stochastic gradient descent)
* Deep learning has led to impressive advancements in computer vision, speech recognition, machine translation, etc.
* Single layer neural networks are a foundation, with modern deep networks being complex software compositions
* Sigmoid functions and logistic regression are related
* Softmax layers extend binary classification to multiclass classification
* Gaussian processes are another type of neural network model
* Universal approximation property: one hidden layer can approximate any continuous function
* Adding depth to the network makes it more powerful but also more complex
* Modern deep learning research focuses on efficient methods for training large networks (e.g., Inception, automated ways of plugging things together) * The speaker discusses deep learning, focusing on reinforcement learning and optimization methods
* Towards the end of the RL course, they will cover optimization techniques like gradient descent and its variants
* They mention 0th order approximation methods and their application in optimization
* Reverse mode automatic differentiation is useful for sensitivity analysis in deep learning
* Forward mode automatic differentiation is also mentioned as a method to compute gradients
* The speaker discusses the chain rule, backpropagation, and vector calculus concepts in the context of neural networks
* They mention the importance of efficient computation and memory management in deep learning
* Various optimization methods are discussed, including momentum, RMSProp, and Adam
* The speaker mentions the importance of choosing a good learning rate and handling hyperparameter optimization. * Benefits of reinforcement learning (RL)
* Non-stationary data distribution is a hallmark of RL problems
* Robot operation in the real world may encounter different distributions
* Locally adaptive methods, like population-based methods, are worth looking into
* Hyperparameter search is important for making the best learning progress
* Google's resource constraints might require sequential methods
* Diagnostic tools such as histograms and large minibatches can be useful
* Heavy-tailed grading distributions can cause numerical issues
* Simplified RL tasks and model versions can help with performance issues
* Decoupled neural interfaces using data gradients are an ongoing research topic
* Predictive models with different architectures might perform better
* Online architecture search is a promising approach for adapting network architecture without restarting training
* Gradient-free methods and evolutionary methods are alternatives to traditional learning algorithms.



## Deep Learning 4: Beyond Image Recognition, End-to-End Learning, Embeddings

URL: [https://www.youtube.com/watch?v=OfKnA91zs9I](https://www.youtube.com/watch?v=OfKnA91zs9I)

 * Ryan Hansel is a researcher at DeepMind, leading the deep learning team with a focus on continual learning and transfer learning.
* He will discuss three topics: end-to-end learning, computer vision, and robotics.
* End-to-end learning is optimizing input and output together, usually using differentiable approaches like gradient descent methods.
* Pre-trained models trained on large datasets like ImageNet are useful for various tasks as they provide feature representations from similar domains.
* Object detection involves more than just classification; it requires object localization, which can be achieved by predicting bounding boxes directly and refining their locations using mean squared error loss.
* Semantic segmentation is labeling each pixel in an image with one of multiple classes, which is challenging as it requires high resolution and accurate representation of objects.
* Convolutional neural networks (CNNs) can be used for semantic segmentation but lose spatial resolution at the higher layers. Reverse pooling or transposed convolutions can be employed to preserve spatial resolution.
* Skip connections help carry information across different layers in a network, making it translation invariant and improving performance.
* In video classification, considering multiple frames instead of individual ones can lead to better results.
* Dilated convolution can provide a broader receptive field without pooling, reducing the need for complex architectures.
* Fusing information from different modalities (e.g., audio and video) can improve performance in various applications like speech recognition or action recognition.
* The brain processes different sensory modalities independently but allows communication between them through feedback connections early in cortical processing.
* Late fusion is a common approach to combining information from different modalities, but other methods like early fusion or using recurrent neural networks can also be effective.
* Max Yata Berg from DeepMind motivated the use of convolutional neural networks with pooling layers for translational invariance and broader feature detection.
* Data augmentation is a common technique to introduce variation into data, making learning harder but more robust to transformations. * Speaker introduces the challenge of dealing with variation data in image recognition
* Discusses the need for rotation invariance and the limitations of Gabor filters
* Proposes a two-layer processing approach, with the first layer handling transformation estimation and the second layer learning the transformation
* Mentions the importance of normalization and bias correction
* Talks about using affine transformations and differentiable functions to learn rotation invariance
* Discusses the use of localization networks and grid generators for sampling input data
* Mentions the importance of backpropagation and bilinear interpolation in the network design
* Compares affine transformations with thin plate splines
* Talks about using a Siamese Network for learning similarity and contrastive loss
* Discusses the use of triplet loss for training an embedding space
* Mentions the challenges of navigation problems and deep reinforcement learning approaches
* Talks about developing a simulator for maze navigation and using LSTM for memory tasks
* Discusses the importance of auxiliary tasks, such as depth prediction, in improving performance.


## Deep Learning 5: Optimization for Machine Learning

URL: [https://www.youtube.com/watch?v=ALdsqfrLieg](https://www.youtube.com/watch?v=ALdsqfrLieg)

 * James Martens is discussing optimization methods, specifically neural implants and the topics of video consent, standard canonical method momentum, and stochastic optimization
* He covers gradient descent, second order methods, and their motivations
* Gradient descent is a simple method for minimizing an objective function by making small incremental changes in the direction of the greatest reduction per unit change
* It relies on the assumption that the objective function is relatively smooth and follows the negative gradient direction
* Second order methods, such as Newton's method, use information about the curvature of the objective function to make larger steps towards the minimum
* Stochastic optimization is used when dealing with large datasets and involves making updates based on noisy estimates of the gradient
* He mentions the importance of Lipschitz smoothness and strong convexity in ensuring convergence
* Momentum methods add a velocity term to the update rule to help overcome oscillations and converge faster
* Nesterov methods use an anticipatory update rule that looks ahead to the next step
* Convergence theory is discussed, including the relationship between learning rate and momentum
* He mentions the importance of understanding the worst case bounds for optimization algorithms and the role of condition number in determining convergence rates. * The speaker discusses approximating curvature matrices for efficient storage and inversion in optimization, specifically in the context of neural networks.
* Diagonal approximation is a popular method to reduce storage cost and computation cost by turning the curvature matrix into a diagonal matrix.
* Generalized Gauss-Newton (GGN) matrix is mentioned as an example of a method that uses a diagonal approximation.
* The speaker mentions that computing exactly can be hard, but unbiased estimation techniques like Carpet Propagation can work efficiently for certain cases.
* Block diagonal approximation is another method to approximate curvature matrices by partitioning the matrix into blocks and approximating each block separately.
* Kronecker product approximation is a technique used in block diagonal approximation.
* Stochastic optimization, which is commonly used in neural networks, is discussed as an extension of deterministic optimization methods.
* Momentum methods are mentioned as a way to address the staleness problem in stochastic optimization.
* The speaker discusses the advantages and disadvantages of different optimization methods, including second-order methods and momentum methods.
* The importance of understanding theory and intuition in optimization is emphasized.
* The speaker mentions some classical optimization techniques and references to relevant papers.


## Deep Learning 6: Deep Learning for NLP

URL: [https://www.youtube.com/watch?v=Y95JwaynE40](https://www.youtube.com/watch?v=Y95JwaynE40)

 * Speaker is giving a lecture on deep learning and natural language processing (NLP), focusing on word embeddings
* Mentioned using Moodle for the lecture, and being an honorary faculty member at DeepMind and Stanford
* Discussed the importance of understanding language fundamentals and solving the problem of artificial general intelligence (AGI)
* Covered topics such as representation building, language modeling, natural language understanding, and application methods in NLP
* Mentioned distributional semantics and its relation to word vectors, using examples like cosine similarity and context modeling
* Discussed the limitations of count-based methods and the need for richer representations to capture semantic similarity
* Introduced neural network models for vector-based machine learning in NLP
* Mentioned the history of distributional semantics, including the idea of word vectors and their use in information retrieval systems
* Discussed the importance of normalization methods for vector representations and the role of context in building effective representations. * The speaker discusses various approaches to learning word embeddings and language modeling, including neural network methods and the use of unsupervised learning
* Discusses the importance of conditioning information in language models and the difference between conditional and unconditional models
* Mentions the challenges of dealing with variable length sequences and the trade-offs between model complexity and data size
* Talks about the role of probability distributions in language modeling and the use of different assumptions, such as Markov assumptions
* Discusses the use of neural networks for language modeling and the advantages of using conditional models over unconditional ones
* Mentions the importance of handling long range dependencies in language models and the use of attention mechanisms to do so
* Talks about the application of language models to various tasks, such as translation and textual entailment
* Discusses the challenges of training large language models and the role of pre-training and transfer learning in addressing these challenges.
* The speaker discusses the use of attention mechanisms in neural sequence modeling, specifically for machine translation and textual entailment.
* Attention allows capturing long range dependencies and makes training easier by passing gradients back to the encoder without much noise.
* Textual entailment is a task that requires complete retraining when using traditional approaches, but attention models can be used as a good starting point for new tasks like parsing or textual entailment.
* The speaker provides examples of how attention can be used in textual entailment to classify the relation between two sentences.
* Attention allows the model to focus on specific parts of the input sequence and distinguish fine-grained differences, making it useful for tasks like textual entailment and parsing.
* The speaker mentions that attention models have been used in translation and have adapted well to large scale supervised learning tasks.
* Attention can be implemented using different architectures such as LSTM, GRU, or neural Turing machines.
* The speaker discusses the importance of compositionality in understanding language and how it relates to neural network models.
* They also mention the use of trees for guiding neural networks and the benefits of jointly learning parsing and composition functions.
* The speaker mentions that shift reduce parsing is a technique used for parsing sequences and reducing the branching structure of the tree.
* They also discuss the use of reinforcement learning in natural language processing and how it can be used to learn both the structure and the meaning of language.
* The speaker encourages further research in natural language processing, particularly in the field of deep learning, and recommends looking into open problems and opportunities for progress.


## Deep Learning 7. Attention and Memory in Deep Learning

URL: [https://www.youtube.com/watch?v=Q57rzaHHO0k](https://www.youtube.com/watch?v=Q57rzaHHO0k)

 * Alex Graf, research scientist at DeepMind, discussing attention memory in deep learning systems
* Attention: ability to focus on one thing while ignoring others, like the cocktail party problem
* Neural networks are parametric nonlinear functions that approximate errors and learn functions from input vectors
* In image classification, a neural network looks at the whole image but implicitly attends to specific parts based on their importance
* The Jacobian matrix shows sensitivity of output to input
* Recurrent neural networks (RNNs) have memory of past events encoded in internal state
* Implicit attention and memory are intimately bound together
* In online handwriting recognition, RNNs interpret decisions made by the network and attend to specific parts of the sequence
* Explicit attention mechanisms allow for focusing on specific parts of data, such as in machine translation or image processing
* Soft attention models take a weighted average of possible glimpses instead of sampling one at a time
* Handwriting recognition requires generating a handwriting sequence from text and aligning it with the text sequence
* Gaussian mixture sets can be used to model handwriting sequences, with each Gaussian representing a different character and its parameters defining its position and variance within the sequence. * The speaker discusses handwriting recognition using associative attention
* Associative attention allows looking at the context of a sequence to attend to specific parts
* It uses a neural network to learn the similarity between vectors representing words or objects
* Cosine similarity is used as a simple similarity function, but learned embeddings can be more powerful
* The speaker mentions the importance of associative recall and lookup in computer science
* Neural machine translation uses associative attention for jointly learning alignment and translation
* Introspective attention allows selectively attending to internal content, such as memory or thoughts
* External data can be modified during introspective attention, but internal content is typically modified iteratively
* The speaker mentions the Turing machine as a computational model and inspiration for neural networks
* Long short-term memory (LSTM) architecture uses attention mechanisms to remember information
* The speaker discusses the difficulty of learning algorithms in neural Turing machines (NTMs) and Engram models
* NTMs can make predictions based on past sequences and use Bayesian methods to update probabilities
* The speaker mentions the importance of memory usage and accessing information differently in neural networks
* Neural phones or annotation machines are mentioned as a potential future development.
* The speaker discusses various machine learning and computer science concepts using associative attention, neural networks, and Turing machines. * The speaker discusses memory architecture based on associative lookup and temporal links
* Memory usage is important, with the ability to access information in multiple ways
* Temporal link matrix is a complicated design for managing large blocks of memory
* Associative recall is important for human cognition and can be used in neural networks
* The speaker suggests that a neural operating system could be useful but it's not yet clear how it would work
* Temporal continuity and concurrent processing are key ideas
* A knowledge graph is an example of a complex graph structure that can be used to represent information
* Traversing a graph to find answers to queries is a challenging problem
* Associative lookup can be used to complete incomplete queries by finding the closest match
* Soft attention mechanisms can be used to focus on specific parts of an image or sequence
* Generative models, such as variational autoencoders, can create realistic images
* Attention mechanisms can be trained using backpropagation and reinforcement learning.


## Deep Learning 8: Unsupervised learning and generative models

URL: [https://www.youtube.com/watch?v=H4VGSYGvJiA](https://www.youtube.com/watch?v=H4VGSYGvJiA)

 * Speaker is Shakir, discussing unsupervised learning and generative models
* Importance of unsupervised learning: understanding the world, abstract reasoning, establishing conceptual basis for decision-making, generating new plans
* Generative models: complementary to other learning systems (supervised, reinforcement, semisupervised), applications include super resolution images, video compression, text-to-speech, scientific research in areas like physics and healthcare
* Five tricks for manipulating probability in generative models using integral, density, and gradient tools
* Importance of probabilistic dexterity in machine learning to effectively solve problems
* Evidence lower bound: computing evidence P(X|Z) using the identity trick and importance sampling
* Density ratio trick: computing the ratio of densities P(X)/Q(X) for classifier building and compression
* Manipulating density and gradient in generative models, including the log derivative trick
* Policy learning in reinforcement learning using the policy gradient framework
* Control variate estimation: knowing the optimal C to minimize variance in a particular problem
* Pathwise estimation and the Reaper amortization trick for gradient computation in continuous spaces. * Urbation analysis and perturbation analysis are used to derive variation gradients
* Five tricks for learning: identity trick, one bounding trick based on Jensen's inequality, density estimation, ratio trick, log derivative trick
* Generative model discussion: densely observed models vs. partially observed models, unsupervised learning, choice of optimization method and penalization
* Latent variable models: undirected graphical models, Markov random fields, Ising models, Hopfield networks, deep latent Gaussian models
* Variational inference and variational free energy
* Likelihood reconstruction term and natural penalty mechanisms
* Structured approximation and designing Q distribution
* Optimization methods: variational calculus, functional gradient descent, doubly stochastic variational inference. * The speaker discussed various methods for estimating probability distributions, focusing on variational inference and amortized inference
* Variational Inference:
  + Use of Gaussian distribution with univariate gaussians as a base model
  + Build richer covariance models using mixture models
  + Use of auto-regressive models for modeling the mean
  + Create posterior approximations using variational bounds
  + Two relations between X and latent variable model
  + Amortized Inference:
    - Variational EM algorithm with stochastic optimization
    - Doubly stochastic variational inference
* Amortized Inference vs. Variational Inference:
  + Both methods deal with optimization and model learning
  + Amortized Inference optimizes for each data point separately, while Variational Inference optimizes globally
  + Amortized Inference uses an inference network to share statistical strength between data points
* Importance of designing appropriate loss functions and optimization techniques
* Comparison of different estimation methods: density ratio versus density difference estimation
* Adversarial Learning: using a discriminator and generator to learn distributions
* Building a generative model with a renderer for computer graphics
* Importance of understanding the underlying principles and choosing appropriate models and techniques based on the problem at hand.



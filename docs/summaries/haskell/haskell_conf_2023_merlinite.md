## [Haskell'23] Welcome

URL: [https://www.youtube.com/watch?v=uTltUa4UOi8](https://www.youtube.com/watch?v=uTltUa4UOi8)


* Speaker is welcoming the audience to the Haskell Symposium
* The speaker will be hosting a lightning talk every year
* The lightning talks are about five minutes long
* Audience members can register for a lightning talk through the symposium's website
* If someone wants to ask a question or share their thoughts during a lightning talk, they should use the `#hcll` hashtag
* The speaker hopes that everyone will enjoy the program and find it helpful

[Please note that this document was generated using an AI. The language may not be perfect. If you notice any errors, please let me know.]


## [Haskell'23] The Evolution of Effects

URL: [https://www.youtube.com/watch?v=m821Vz8N_bo](https://www.youtube.com/watch?v=m821Vz8N_bo)

 
- Mona Talk: Algebraic Effect Handlers - A Historical Perspective
    - Monads as a way to compose programs together (1990)
    - Monad Transformers for combining effects in a modular way (1993)
    - State monad and its general interest (1995)
    - Effect Handlers with algebraic syntax and semantics (2002)
    - Scoped Effects: A new syntactic construct for algebraic effect handling (2014)
- Key Concepts:
    - Monads as a way to compose programs together
    - Monad Transformers for combining effects in a modular way
    - State monad and its general interest
    - Effect Handlers with algebraic syntax and semantics
    - Scoped Effects: A new syntactic construct for algebraic effect handling
- Historical Context:
    - Phil Wadler's work on Monads and Monad Transformers (1990, 1993)
    - John Hughes' work on the Reader monad and the State monad (1992)
    - Mark Jones' work on type classes and the Monad instance (1993)
    - Bill L L's work on the L Theory (1965)
    - Plotkin's work on semantics of algebraic effects (2002)
- Current Challenges:
    - Expressivity: The ability to express a wide range of effects
    - Efficiency: The ability to make efficient implementations
    - Convenience: The ability to use the library in a convenient way
- Future Directions:
    - Unifying framework for effect handlers
    - Scoped Effects: A new syntactic construct for algebraic effect handling
    - Row Types: A way to express effects in a more concise way
- Current State of the Field:
    - Lots of research and excitement around algebraic effects
    - Many libraries and tools available for working with algebraic effects
    - Challenges remain in expressivity, efficiency, and convenience


## [Haskell'23] Effect Handlers for Programmable Inference

URL: [https://www.youtube.com/watch?v=V2vIfgGrr74](https://www.youtube.com/watch?v=V2vIfgGrr74)

 
- Alexa presented on using effect handlers for programmable inference
- Effect handlers provide a way to structure inference programs and reinterpret models in different ways
- The talk focused on two specific algorithms: Metropolis Hastings and particle filter
- Metropolis Hastings is an algorithm that proposes new samples and decides whether to accept them based on a likelihood ratio
- Particle filter is an algorithm that resamples particles (representations of the model) based on their weights and proposes new samples for each observation
- The speaker demonstrated how to derive concrete algorithms from abstract descriptions using effect handlers
- The speaker also discussed a resample move particle filter, which applies Metropolis Hastings to the resampling step of the particle filter
- The talk emphasized the importance of managing side effects and imperative baggage in inference programs
- The speaker mentioned the use of monads as a way to manage side effects and provide type safety
- The speaker acknowledged that haskell's learning curve is steep, but that effect handlers provide an intuitive and explicit interface for building inference algorithms


## [Haskell'23] The Essence of Reactivity

URL: [https://www.youtube.com/watch?v=JCy6YYigsog](https://www.youtube.com/watch?v=JCy6YYigsog)

 
- The speaker discusses functional reactive programming and the Yampa library.
- Functional reactive programming can be used to write systems using ordinary differential equations.
- The Yampa library supports writing differential equations but may not always be able to solve them.
- The speaker mentions a system called Zos that incorporates differential equations.
- Lustre also incorporates differential equations.
- There is a limit to the time in Yampa, which can go to negative values or infinity.
- The speaker suggests that this limit may not be necessary.
- The speaker mentions a problem from 2000 related to functional reactive programming.
- The speaker introduces the notion of number types and classes in their system.
- The speaker is working on a new system that will incorporate mathematical ideas.
- The speaker suggests that they may need to redesign their copilot language.
- The speaker mentions a problem with going back in time in functional reactive programming.
- The speaker suggests that repeating sequences, like sin and cosine, could go back in time.
- The speaker mentions a question about the rule of law for their system.
- The speaker mentions a paper they are working on to explain their framework.
- The speaker mentions a question about how their system handles number types and classes.
- The speaker suggests that they may need to redesign their system to incorporate mathematical ideas.


## [Haskell'23] This Is Driving Me Loopy: Efficient Loops in Arrowized Functional Reactive Pr...

URL: [https://www.youtube.com/watch?v=d3kzZN9asKM](https://www.youtube.com/watch?v=d3kzZN9asKM)

 
- Speaker discusses the challenges and benefits of using Arrowized Functional Reactive Programming (AFRP) in software development.
- AFRP is a programming paradigm that combines functional and reactive programming, allowing for efficient handling of data streams and event-driven systems.
- The speaker presents two case studies: Loop D and Loop M, which are examples of transformations used to optimize and simplify AFRP code.
- Loop D is a strict variant of the Loop transformation, while Loop M is a more flexible variant that allows for reordering of computations.
- The speaker uses diagrams and examples to illustrate how these transformations work and how they can improve performance and simplify code.
- The speaker also discusses the limitations of AFRP and potential future improvements, such as better support for loop transformations and random program generation.


## [Haskell'23] An Exceptional Actor System (Functional Pearl)

URL: [https://www.youtube.com/watch?v=pqTUtTyZZxU](https://www.youtube.com/watch?v=pqTUtTyZZxU)

 
- Patrick Redmond from University of California, Santa Cruz presented a paper on an Actor System using Haskell.
- The Actor System is implemented with ForkIO and KillThread primitives.
- Actors are able to send and receive messages.
- The system is designed to be extensible, allowing for the addition of new message types without changing code.
- A State transition framework is used to encode actor behavior.
- A ring leader election algorithm is demonstrated using the actor framework.
- The algorithm works by passing around a "nominate" message until a leader is elected.
- The paper also includes support for stateful actors and handling asynchronous exceptions.
- The author proposes comparing the performance of channels with STM implementations.
- The talk was humorous and engaging, with the author incorporating Star Trek references and jokes.


## [Haskell'23] HasTEE: Programming Trusted Execution Environments with Haskell

URL: [https://www.youtube.com/watch?v=q-VW1pp1nGk](https://www.youtube.com/watch?v=q-VW1pp1nGk)

 
- The speaker presents a program called Hy, which is a domain specific language for programming trusted execution environments using Haskell.
 	+ Hy relies on a compiler modification to extend the language and enable information flow control.
 	+ The approach involves dividing an application into two projects: a trusted project and an untrusted project.
 	+ The trusted project uses a restricted version of the C standard library, implemented in hardware vendor-specific enclave description language.
 	+ The speaker demonstrates this concept with a simple password checker example using API calls to a monad representing the enclave.
 	+ Hy is designed for automatic partitioning of programs using type systems and compiler modifications.
 	+ The toolchain includes cabal and flag-based compilation for enclave and untrusted side compilation.
 	+ The speaker discusses the future work, including generalization to compartmentalized applications and experimental ideas related to Haskell as a target language.


## [Haskell'23] Haskell Library for Safer Virtual Machine Introspection (Experience Report)

URL: [https://www.youtube.com/watch?v=Xy8loMNknHo](https://www.youtube.com/watch?v=Xy8loMNknHo)

 
- The research focuses on Virtual Machine Introspection (VMI) and its challenges, specifically the use of a Haskell library called HBMI to address two main issues: complicated data retrieval and undetected errors.
	1. HBMI utilizes static type checking and meta programming to detect programmer errors at compile time and generate safe code for accessing guest memory.
	2. The library provides dedicated type accessors, symbol generation functions, and error handling mechanisms to ensure safe and accurate data retrieval.
	3. HBMI's metaprogramming facility and template haskell support simplify the process of building the library and implementing rootkit detection for Linux guests.
- The presenter highlights two main problems in existing VMI libraries and how HBMI addresses them:
	1. Reading/writing guest memory requires complex procedures, leading to potential errors.
	2. Statically undetected fatal errors can occur due to incorrect variable symbol names, calculation mistakes, or using the wrong API data type.
- The presenter discusses the benefits and drawbacks of HBMI:
	1. HBMI's static type checking mechanism effectively detects different types of address value usage.
	2. The library's concise notation simplifies program portions and makes the code clear and easy to understand.
	3. Despite its benefits, HBMI's adaptive generative approach has some drawbacks, such as requiring explicit Declarations for every C name accessed in the program.
- The presenter concludes by emphasizing the practicality of Haskell's metaprogramming facility and template haskell support in building HBMI.


## [Haskell'23] A Haskell Auto-Parallelizer for Distributed Computing

URL: [https://www.youtube.com/watch?v=ahPC7xshN60](https://www.youtube.com/watch?v=ahPC7xshN60)

 
- Presenting a Haskell Auto Parallelizer for Distributed Computing.
- The main issue is side effect management in distributed computing.
- Two semantics are needed: the function and its side effects.
- The goal is to create a monad that can distribute function calls while keeping track of side effects.
- Implemented a prototype using a generic Haskell program, parsing the main function, and building an abstract syntax tree.
- Current implementation has limitations, such as supporting only monadic operations and having difficulty handling higher-order functions.
- The goal is to create a system that can schedule tasks based on data dependency.
- Experimented with different granularity levels for tasks.
- Ideas for the future include implementing full tolerance mechanisms and strategy mitigation techniques.


## [Haskell'23] Verifying Haskell's Rewrite Rules based on Polymorphic Rewriting Theory

URL: [https://www.youtube.com/watch?v=Z68SseWlxT0](https://www.youtube.com/watch?v=Z68SseWlxT0)

 
- Goal: verify Haskell's rewrite rules based on polymorphic rewriting theory
- Problem: current Haskell user-defined rewrite rule optimization lacks formal theory
- Solution: develop a new correctness theme and suitable rewriting semantics for high-scale systems
- Concept: implement a system F extension called System F Omega with prototype in GHC core plugin
- Technique: use polymorphic termination guarantee based on rewriting theory and unification check
- Result: automated checking of correctness rules and strong normalization for map and list functions


## [Haskell'23] Lightning Talks I

URL: [https://www.youtube.com/watch?v=7FX9IuKugKw](https://www.youtube.com/watch?v=7FX9IuKugKw)

 
- Haskell's test coverage for the backend has been improved.
- The talk is based on a role-playing scenario where a compiler engineer receives a ticket about incorrect UTF-8 decoding.
- The engineer faces difficulty in reproducing the issue, and realizes that the current testing infrastructure needs improvement, especially for various backends.
- A test suite package for PrimOps has been implemented to address this issue.
- The C minus minus language, used by GHC, has diverged over time and still requires active effort to define its semantics.
- A pure interpreter for C minus minus expressions has been written as a reference for the compiler.
- The test suite driver compares the interpretation of an expression between the pure interpreter and the compiler, using Quick Check to identify discrepancies.
- Several bugs have been identified and fixed in various GHC backends, particularly in native code generation and foreign calling conventions.
- Contributing to the test PrimOps project on Gitlab is encouraged.


## [Haskell'23] Haskell for choice-based learning

URL: [https://www.youtube.com/watch?v=mo9VGu5gUbU](https://www.youtube.com/watch?v=mo9VGu5gUbU)

 
- Speaker introduced the concept of Choice based learning, a method for combining two programming paradigms (algebraic effect handlers and selection monad) to implement machine learning algorithms in a functional programming language.
- The speaker demonstrated the design using a simple training algorithm (linear regression with one variable) and discussed how the choice made during each iteration affects the loss calculation.
- The speaker then introduced the concept of an algebraic effect interface and explained how it provides a modular, flexible way to support structured control flow abstraction in functional programming languages.
- The speaker provided examples of using effect handlers to implement specific optimization techniques (gradient descent and safe division) and showed how multiple choice can be combined using effect handlers.
- The speaker discussed the challenges of implementing machine learning algorithms in a high school environment, including the need for simplicity and ease of use.
- The speaker introduced the concept of a loss operation and explained how it can be used to encode selection monad in functional programming.
- The speaker provided examples of using effect handlers to implement different optimization techniques (gradient descent and hyperparameter optimization) and discussed the advantages of using an interpreted selection monad in machine learning algorithms.


## [Haskell'23] falsify: Internal Shrinking Reimagined for Haskell

URL: [https://www.youtube.com/watch?v=csKkTas6X58](https://www.youtube.com/watch?v=csKkTas6X58)

 
- The speaker discusses the concept of shrinking in the context of Quick Check and Falsify.
 	+ Shrinking involves reducing the size or complexity of a value to help identify counterexamples.
 	+ The speaker suggests that shrinking can be implemented using either internal or bidirectional parsing.
 	+ Bidirectional parsing, as used in Hedgehog and Falsify, allows for more efficient shrinking by splitting the generator into left and right sides.
 	+ The speaker argues that integrated shrinking, as implemented in Hedgehog, is more effective than manual shrinking.
 	+ Integrated shrinking uses a cut point to determine when to stop shrinking, while manual shrinking requires explicit state management.
- The speaker discusses the idea of using a Sud function to split a random number generator into left and right sides.
 	+ This approach can be used to generate infinite trees with finite representations.
- The speaker also discusses the concept of primitives in generator writing.
 	+ Primitives are building blocks that can be combined to create more complex generators.
 	+ When writing a generator, it's important to consider how the shrinker will behave and whether it will shrink towards a specific value, such as zero or false.
- The speaker mentions the Hedgehog library, which provides a more composable and principled way of generating values for testing.
 	+ The Hedgehog library also guarantees that the shrinking process will terminate and will not cycle.
- The speaker compares Falsify to the Hypothesis library, which uses a different approach to shrinking.
 	+ The Hypothesis library provides more detailed comparisons and examples of how to use its functions.
- The speaker mentions that Python is a popular language for testing and that people have reported good results with Falsify in Python.
 	+ However, the speaker also acknowledges that they are not as familiar with Python as they are with Haskell.
- The speaker answers questions from the audience about shrinking, monotonicity, and bidirectional parsing.
 	+ They discuss how to write generators that are monotonic and how to combine bidirectional parsing with selective functors.
 	+ They also mention that they have not heard the term "monotonic" used in this context before.
- The speaker thanks the audience for their questions and comments.


## [Haskell'23] Don’t Go Down the Rabbit Hole: Reprioritizing Enumeration for Property-Based ...

URL: [https://www.youtube.com/watch?v=-CIyc27MJfw](https://www.youtube.com/watch?v=-CIyc27MJfw)

 
- Speaker discusses the challenges of property-based testing, specifically in relation to enumeration.
 	+ Enumeration can be time-consuming and may require a large input space.
 	+ Blackbox random generation doesn't always solve the problem efficiently.
 	+ Lazy enumeration can create a "rabbit hole" issue, where structural similarities lead to redundant testing.
 	+ The speaker presents a strategy for addressing this issue by splitting the input space into smaller subspaces and using combinatorial coverage.
- The speaker also discusses techniques for finding counterexamples more efficiently, such as:
 	+ Parallel evaluation
 	+ Mutation testing
 	+ Bounded exploration with different timeouts and interaction strengths
 	+ Using a combination of shallow, medium, and deep patterns to cover various types of bugs
- The speaker mentions the importance of understanding interaction strength and how it affects the testing process.
- The talk concludes with a Q&A session where the speaker addresses questions about the implementation and practicality of their proposed methods.
 	+ The speaker acknowledges that an external tool is currently needed to generate coverage arrays, but they are working on a hascal implementation.
 	+ The speaker also discusses potential optimizations for pattern matching and keeping results uniform to improve performance.


## [Haskell'23] Lightning Talks II

URL: [https://www.youtube.com/watch?v=KpaCDZw1KyE](https://www.youtube.com/watch?v=KpaCDZw1KyE)

 
- Speaker: [Haskell 23] Lightning Talks II
- Topics covered: Property based testing, generators, shrinking, type classes, monads, randomness, Hedgehog library
- Challenges with property based testing: Type inference failures, ambiguity, duplication
- Solutions proposed: Extensible effect library, type level traversal, gut type level programming, record label specific examples
- Speaker: Armand Ramirez, Mercury and Game Dev engineer
- Topic: Inference failure situations in Haskell
- Example of a concrete list with two readers causing inference failure
- Proposed solution: Use effect lists with higher kind, bring constraint, and gut type level programming
- Speaker: Richard Eisenberg
- Topic: GHC JavaScript backend
- Current status: Integrated GC, CMM involved, scripton used for basic tool chain
- Missing features: Optimizer, incremental linking, splitting executable into multiple files
- Benefits of using the JavaScript backend: Accessibility, type safety, higher level features
- Speaker: La Stan
- Topic: GHC JavaScript backend and Haskell
- Current state: Everything integrated, merged, cabal simple install, custom script fixed
- Future plans: Optimizer profiling, FFI, platform detection features
- Example of converting existing C code to JavaScript using a few lines of glue code
- Challenges: Memory representation, platform specific features, easy installation and configuration.


## [Haskell'23] Haskell Summer of Code Presentations

URL: [https://www.youtube.com/watch?v=_gpggZ-o0eE](https://www.youtube.com/watch?v=_gpggZ-o0eE)

 
- Greg: Proposing an intermediate representation for Haskell to improve parsing and tooling compatibility.
- Sai: Demonstrating a project that visualizes patterns using Haskell and World Turtle library.
- Lander: Showcasing progress on implementing goto definition in a Haskell language server.


## [Haskell'23] PC Chair Report

URL: [https://www.youtube.com/watch?v=cufcFre5Oc8](https://www.youtube.com/watch?v=cufcFre5Oc8)


- **Husk Symposium PC Chair Report**
    - Thanks to well typed sponsor
    - Thanks to speaker, attendee
    - Thanks to two keynote speakers
    - Appreciation for Trevor, steering committee organizer Nikil Swami, General chair Yanik Foster, organized workshop chair, student volunteer
    - Gratitude for program committee, session chairs
    - Discussion of mission process changes
        + No abstract deadline this year
        + Last year tried artifact submission idea; not another round
        + 15 submissions, 12 regular papers, one demo, one experience report, one functional Pearl
        + Three reviewers per paper; eight papers accepted; six gave suggestions to come present a demo
    - Hope for artifact submission next year
- **Husk Symposium PC Chair Report (Continued)**
    - Discussion of low number submissions this year: 15 last year, 20 Co era, 13 le
    - Suggestion for two page abstract submission next year
    - Awareness that student finds it hard to get papers reviewed
    - Idea to get sponsorship for students to come present their demos
    - Appreciation for Garett attending the symposium



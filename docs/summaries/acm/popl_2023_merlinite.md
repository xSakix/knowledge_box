## [POPL'23] Higher-Order Leak and Deadlock Free Locks

URL: [https://www.youtube.com/watch?v=QJyJNMHkgWY](https://www.youtube.com/watch?v=QJyJNMHkgWY)

 
- Speaker mentions having a higher-order lock that is leak and deadlock free, and will present on this topic.
- Speaker mentions using a higher-order function to solve the problem of memory leaks and deadlocks in concurrent programming.


## [POPL'23] Temporal Verification with Answer-Effect Modification: Dependent Temporal Type-a...

URL: [https://www.youtube.com/watch?v=LZjQyc-yCAA](https://www.youtube.com/watch?v=LZjQyc-yCAA)

 
- The speaker is discussing temporal verification, a technique for verifying the temporal properties of programs.
 	+ They introduce the concept of answer-effect modification and its use in temporal verification.
 	+ They give an example of resource usage and how it can be verified using this technique.
 	+ They discuss the challenge of implementing control operators in the context of temporal verification.
 	+ They mention the need for a type system that can handle type modification and effect propagation.
 	+ They talk about the importance of knowing the types of expressions and effects in a program.
 	+ They give an example of backtracking in a program and how it can be handled using control operators.
 	+ They discuss the need for a flexible control flow mechanism that can handle different control structures.
- The speaker then answers questions from the audience:
 	+ One question is about inferring constraints and generating them in a decidable manner.
 	+ Another question is about the use of limited continuation in the context of multiprompt programs.


## [POPL'23] Recursive Subtyping for All

URL: [https://www.youtube.com/watch?v=1KxcPtak-78](https://www.youtube.com/watch?v=1KxcPtak-78)

 
- Speaker to discuss a new subtyping algorithm for system F.
  - System F with subrecursive types is a classical problem.
  - The talk aims to introduce recursive typing and its importance.
  - Recursive typing has two important features: natural combination and two flavor dependencies.
  - The speaker will discuss combining F Sub with ISO recursive type, but it turns out to be nonconservative.
  - The talk will also cover the difficulty of proving undecidability for subcalculations.
  - The speaker will propose a new solution to combine kernel and executive types to make the system decidable.
  - The speaker will discuss the advantages of using ISO recursive simultaneous calculus.
  - The talk will cover structural rules, annotated types, and polymorphic types.


## [POPL'23] A High-Level Separation Logic for Heap Space under Garbage Collection

URL: [https://www.youtube.com/watch?v=cam6tdwB6YI](https://www.youtube.com/watch?v=cam6tdwB6YI)

 
- The speaker is discussing the concept of a high-level separation logic for managing heap space under garbage collection.
	+ They mention the challenges of verifying program behavior in the presence of garbage collection, and the importance of using formal methods to prove properties about heap space usage.
	+ They describe a system that uses stackable assertions to track the reachability of heap blocks, and how this can help ensure that the heap does not exceed a maximum size.
	+ They also discuss the use of predicates and specification functions to verify the correctness of closures (functions that allocate and deallocate heap space).
- The speaker asks questions about the concept of stackable assertions and their behavior, and receives answers from the audience.
	+ They ask if a stackable assertion can be used like a reference count to track the number of pointers to a heap block.
	+ They also ask if there is a way to prove the reachability of a heap block without using a stackable assertion, and if it would be possible to use pointed assertions instead.
- The speaker mentions some related work, including a verified compiler for Cake ML and a paper on formalizing the semantics of a high-level language with separation logic.


## [POPL'23] CN: Verifying Systems C Code with Separation-Logic Refinement Types

URL: [https://www.youtube.com/watch?v=x7fp-avX_QE](https://www.youtube.com/watch?v=x7fp-avX_QE)

 
- The talk is about verifying systems C code with separation-logic refinement types, specifically in the context of the pkvm project.
- The main challenges include handling complexity in real-world system software and achieving predictable automation.
- The solution involves building a type system that can explicitly manage complex control flow and variable scoping, using concepts like Cerberus and liquid types.
- The goal is to create a predictable automation scheme that can handle complex invariances in low-level system code.
- The team is working on improving the user experience and error messages for the verification tool.
- They are considering adding support for concurrency and function pointers, but have not yet decided on the best approach.
- The ultimate goal is to create a foundational proof for the translation of C semantics to binary level, ensuring correctness and soundness.


## [POPL'23] Conditional Contextual Refinement

URL: [https://www.youtube.com/watch?v=fINgpZeyF_g](https://www.youtube.com/watch?v=fINgpZeyF_g)

 
- The speaker discussed Conditional Contextual Refinement (CCR), a method that allows for the use of separation logic in refinement calculus, which is useful for proving properties of programs.
 	+ CCR is a key idea that enables the integration of separation logic into refinement calculus, providing benefits such as transitivity and the ability to prove properties of programs.
- The speaker used a toy example to illustrate the concept of CCR.
 	+ The toy example involved a simple function that computes the nonnegative integer power of an input number.
- The speaker explained the challenge of operationalizing the notion of ownership transfer in separation logic.
 	+ The challenge is due to the fact that the pure proposition model of separation logic does not allow for the duplication of appending tokens, which can cause issues when trying to operationalize the concept of ownership transfer.
- The speaker introduced the concept of dual nondeterminism technique and how it can be used to implicitly pass resources between modules without changing the type of the argument or return value.
 	+ This technique is used to ensure that the resource is always sequenced properly between modules, which is important for maintaining the correctness of the program.
- The speaker mentioned the use of Iris, a specialized Coq assistant, to perform automatic proofs in the context of separation logic.
 	+ Iris can instantiate proof modes and notions of resources in a custom way without requiring step indexing.
- The speaker discussed the difference between explicit resource passing and implicit resource passing in separation logic.
 	+ Explicit resource passing, such as linear types, ensures that resources are passed systematically, while implicit resource passing, like in traditional notion of contextual refinement, can lead to gaps in the environment and properties.
- The speaker mentioned the challenge of integrating separation logic into a framework that supports nontermination and visual recursion.
 	+ The speaker suggested using step indexing technique and finding a way to operationalize the traditional notion of contextual refinement in the framework.


## [POPL'23] MSWasm: Soundly Enforcing Memory-Safe Execution of Unsafe Code

URL: [https://www.youtube.com/watch?v=uBqi4T0tnd8](https://www.youtube.com/watch?v=uBqi4T0tnd8)

 
- Anita Golamundi presented on MSWasm, a project enforcing memory-safe execution of unsafe code.
- The goal is to compile and run C code safely without memory safety vulnerabilities in webassembly (Wasm).
- Wasm is a new bike core language meant to run native apps at native speed across various platforms.
- WebAssembly Workers are Edge cloud computing resources that allow for safe execution of code from untrusted sources.
- MSWasm aims to compile high-level languages like C++, Rust, and C (with unsafe portions) into Wasm without memory safety vulnerabilities.
- The challenge is to leverage hardware features efficiently while preserving performance and flexibility.
- Three limitations of the current approach:
	1. Inline memory safety checks are not robust enough for linking third-party libraries.
	2. Compiling well-typed, memory-safe C code can still introduce vulnerabilities if the compiler is dumb.
	3. Hardware features may be necessary but not always built into optimizing compilers.
- Future work includes exploring various memory safety policies and compilation techniques.


## [POPL'23] Reconciling Shannon and Scott with a Lattice of Computable Information

URL: [https://www.youtube.com/watch?v=FysnEmdF11s](https://www.youtube.com/watch?v=FysnEmdF11s)

 
- The speaker is discussing the reconciliation of Shannon and Scott's theories of information flow.
    - Shannon's theory is based on electrical engineering and communication, while Scott's is based on logic and theoretical computer science.
    - The speaker aims to combine these two theories into a new model.
- The speaker introduces two superheroes: Reverend Bays (probabilistic dimension) and Claude Shannon (combinatoric probabilistic view).
    - They represent different ways of looking at information flow.
    - The speaker suggests that combining these views may lead to a more comprehensive understanding of information flow.
- The speaker mentions the need for a generalized notion of termination-sensitive noninterference property.
    - This property is used to describe secrecy in computer systems.
    - The speaker wants to study this property in the context of different application domains.
- The speaker thanks Andy Pitts and the University of Cambridge for introducing the two superheroes.


## [POPL'23] A Core Calculus for Equational Proofs of Cryptographic Protocols

URL: [https://www.youtube.com/watch?v=5rQstrKftGE](https://www.youtube.com/watch?v=5rQstrKftGE)

 
- The speaker discusses a core calculus for equational proofs of cryptographic protocols, called LPDL.
  - LPDL is an expressive language that allows for simple compositional proofs of cryptographic security.
  - It is based on the idea of encoding cryptographic protocols as network programs and using equational reasoning to prove their security.
  - The speaker mentions the importance of soundness and completeness in the proof system.
  - LPDL also allows for the use of uninterpreted functions, which can be used to encode replication and other complex behaviors.
  - The speaker mentions the challenge of adjusting the completeness story in LPDL.
- The speaker also discusses a case study of a simple encryption protocol and a more complex secure multiparty computation protocol.
  - The case study demonstrates the power of LPDL for encoding and proving the security of cryptographic protocols.
  - The speaker mentions the use of induction and other proof techniques in the case study.
- The speaker also discusses the relationship between LPDL and the UC (Universally Composable) model of security.
  - The UC model is a common framework for specifying and proving the security of cryptographic protocols.
  - The speaker mentions the need to establish a polynomial time constraint in order to ensure simulatability in the UC framework.
- The speaker also discusses the importance of modeling high level cryptographic protocol design and extracting implementation from the model.
  - The speaker mentions the use of informal definition and abstraction in the modeling process.
  - The speaker also mentions the need to establish a polynomial time constraint in order to ensure simulatability in the UC framework.


## [POPL'23] DimSum: A Decentralized Approach to Multi-language Semantics and Verification

URL: [https://www.youtube.com/watch?v=5IFZaoBdjkQ](https://www.youtube.com/watch?v=5IFZaoBdjkQ)

 
- Michael presented "DimSum: A Decentralized Approach to Multi-language Semantics and Verification" at the first day of the proper conference.
- The talk focused on a new approach for verifying multi-language programs using a decentralized method.
- The main concept is to combine reasonings from different languages in a modular fashion, allowing for easier proofs and more robust code.
- The DimSum framework achieves this by handling translation between different languages, enabling modular reasoning, and performing bulk verification at the rack level using language-local verification.
- The talk also discussed the idea of introducing a common interaction protocol to link many different languages together, as well as the challenge of verifying programs that rely on assembly code.
- Michael highlighted three key ideas from related work: dealing with the fixed notion of linking, allowing for custom linking operators, and enabling language-local reasoning.


## [POPL'23] Formally Verified Native Code Generation in an Effectful JIT: Turning the CompCe...

URL: [https://www.youtube.com/watch?v=KJfViNtQGIk](https://www.youtube.com/watch?v=KJfViNtQGIk)

 
- The speaker discussed the formal verification of a just-in-time (JIT) compiler, specifically focusing on native code generation and execution.
- JIT compilers are used in modern web browsers and other dynamic languages to optimize performance.
- The speaker's work involves formally verifying the correctness of a JIT compiler, which includes proving that the generated native code behaves exactly as the source program.
- The speaker presented a formal model for JIT compilers, including a state machine and an interpretation of the execution.
- The speaker mentioned the challenges of proving the correctness of JIT compilers, including the need to prove the correctness of both the static compiler and the JIT compiler.
- The speaker also discussed the use of formal methods to verify the compilation process, including the use of a proof assistant like Coq.
- The speaker presented a prototype model for native code generation in a JIT compiler, which includes a formal model for the execution stack and memory management.
- The speaker mentioned the need to prove the correctness of the native code generation process, including the need to prove that the generated native code preserves the observable behavior of the source program.
- The speaker discussed the use of custom calling conventions in JIT compilers, which can help to optimize performance.
- The speaker mentioned the need to prove the correctness of the custom calling convention, including the need to prove that the generated native code corresponds to the specified calling convention.
- The speaker presented a simple example of a JIT compiler, including the use of a state machine to monitor the execution and optimize the performance.
- The speaker discussed the challenges of proving the correctness of JIT compilers, including the need to prove the correctness of both the static compiler and the JIT compiler.
- The speaker mentioned the need to prove the correctness of the native code generation process, including the need to prove that the generated native code preserves the observable behavior of the source program.
- The speaker discussed the use of custom calling conventions in JIT compilers, which can help to optimize performance.
- The speaker mentioned the need to prove the correctness of the custom calling convention, including the need to prove that the generated native code corresponds to the specified calling convention.
- The speaker presented a simple example of a JIT compiler, including the use of a state machine to monitor the execution and optimize the performance.
- The speaker discussed the challenges of proving the correctness of JIT compilers, including the need to prove the correctness of both the static compiler and the JIT compiler.
- The speaker mentioned the need to prove the correctness of the native code generation process, including the need to prove that the generated native code preserves the observable behavior of the source program.
- The speaker discussed the use of custom calling conventions in JIT compilers, which can help to optimize performance.
- The speaker mentioned the need to prove the correctness of the custom calling convention, including the need to prove that the generated native code corresponds to the specified calling convention.
- The speaker presented a simple example of a JIT compiler, including the use of a state machine to monitor the execution and optimize the performance.


## [POPL'23] Dargent: A Silver Bullet for Verified Data Layout Refinement

URL: [https://www.youtube.com/watch?v=IsHzO3F0dSI](https://www.youtube.com/watch?v=IsHzO3F0dSI)

 
- The presentation discusses Cogent, a programming language and certifying compiler that allows for the refinement of data layout specifications.
	* Cogent is designed to create higher-level system verification on the specification side, using a purely functional programming language with uniqueness types that eliminates garbage collection.
	* It is suitable for low-level implementation, as it can generate loadable systems and produce C code directly from functional specifications.
	* The compiler generates proof profiles that provide memory safety guarantees and absence of undefined behavior.
	* Cogent supports variable link data types and recursive types, but does not currently support type punning or casting between different layouts.
- The presentation also discusses related work in integrating layout languages with minimum wage support for recursive types and array handling.
	* Collision is an example of a language that allows specifying layouts and providing proofs, but it does not yet support recursive types or arrays.
	* Legends is a language that allows specifying layouts and generating encoders and decoders within the language, but it does not provide formal guarantees like Dodge can.
	* The goal of this research is to create a layout description language that is integrated with an extension of programming and provides customization of low-level behavior through type systems.


## [POPL'23] A Type-Based Approach to Divide-and-Conquer Recursion in Coq

URL: [https://www.youtube.com/watch?v=W38iJhcS9b4](https://www.youtube.com/watch?v=W38iJhcS9b4)

 
- Talk on "A Type-Based Approach to Divide-and-Conquer Recursion in Coq" by Pablo Coito, Aaron Stump, Neil Ghani, and Robert Crabb.
- Focus on using a type-based approach to ensure termination of divide-and-conquer recursive algorithms in Coq proof assistant.
- Introduce the concept of wellfounded recursion and its importance in proving termination.
- Discuss the challenge of implementing dependent index types to track the size of data in recursive functions.
- Show how to use the F algebra framework to build Merge Sort and Quick Sort algorithms with type-based termination proofs.
- Highlight the power of the Coq proof assistant and its support for structural recursion and dependent types.


## [POPL'23] Elements of Quantitative Rewriting

URL: [https://www.youtube.com/watch?v=1hfIA4uug_o](https://www.youtube.com/watch?v=1hfIA4uug_o)

 
- Francesco Gavazzi presented on quantitative rewriting.
  - He focused on extracting and making explicit computational operations and equational deductions in a quantitative setting.
  - Gavazzi discussed the challenge of proving confluence in a quantitative setting.
  - He suggested that quantitative rewriting may not need to look at specific systems, but rather can focus on abstract rewriting systems.
  - Gavazzi mentioned the importance of understanding reduction and distance propagation.
  - He introduced the concept of amplifying distance using functions.
  - Gavazzi also discussed the idea of recovering confluence in a quantitative setting.
  - He provided examples of linear systems and how they can be applied to quantitative rewriting.
  - Gavazzi suggested that future work could involve finding strategies for termination and approximating or computing distances given equations.
-


## [POPL'23] The Geometry of Causality: Multi-token Geometry of Interaction and Its Causal Un...

URL: [https://www.youtube.com/watch?v=C-oCr6ZGxAA](https://www.youtube.com/watch?v=C-oCr6ZGxAA)


* This is a discussion about the geometry of causality, specifically its interaction and its causal consequences.
* There are mentions of various computational methods and models used to understand this concept.
* The importance of understanding the structure and composition of these interactions is emphasized.
* The impact of these interactions on language, sound, and structure is also discussed.
* The role of various techniques and methods in exploring and understanding this concept is highlighted.


## [POPL'23] Deconstructing the Calculus of Relations with Tape Diagrams

URL: [https://www.youtube.com/watch?v=Iz0C0NE4vq8](https://www.youtube.com/watch?v=Iz0C0NE4vq8)

 
- Talk: Deconstructing the Calculus of Relations with Tape Diagrams
- Speaker: Alessandro de Giorgio
- Goal: Present a new diagrammatic language for expressing and constructing calculus relations
- Background: Existing calculus relation syntax can be difficult to understand and work with
- Proposal: A two-layer grammar using tape diagrams, string diagrams, and relational product
  - First layer: One- or three-diagram syntax for monologue products, precomposition, postcomposition, duplicator, complicator
  - Second layer: Construct NDMT (Named Diagrams with Monoidal and Tensor Product) diagrams using identity lines, branching structure, and merging processes
- Example: ZX calculus diagrams can be embedded in tape diagrams, providing a more intuitive representation
- Future work: Explore negation calculation, nondeterministic process form, and generalizing the work to other languages


## [POPL'23] Probabilistic Resource-Aware Session Types

URL: [https://www.youtube.com/watch?v=6J0l8e4g3lE](https://www.youtube.com/watch?v=6J0l8e4g3lE)

 
- Probabilistic Resource-Aware Session Types: A conservative extension of traditional session types that supports probabilistic Choice type, combining probability and nondeterminism.
- The type system is proven to be type-safe using nested Multiverse semantics and linear time type checking.
- Two applications presented: expected cost analysis in distributed protocols and Markov chain performance analysis.
- Distributed protocol example: Boundary Transmission, a simple file transfer protocol with probability of failure for each chunk's acknowledgment.
- Markov chain example: Dice program, a three-state system with equal probability output.
- The language supports amortization and symbolic bound inference for potential data structure usage.
- Nested Multiverse semantics allow keeping the effect of executing a probabilistic flip expression local.
- Two challenges in relaxing restriction: combining probability and nondeterminism, and preserving control flow with value probability annotation different channels.


## [POPL'23] A Calculus for Amortized Expected Runtimes

URL: [https://www.youtube.com/watch?v=CGRYYJ4q5fI](https://www.youtube.com/watch?v=CGRYYJ4q5fI)

 
- The talk is about a calculus for amortized expected runtimes, which enables separation logic style verification and is used to analyze probabilistic data structures.
 	+ It uses a potential method to enable local reasoning and utilizes a quantitative variant of separation logic.
- The goal is to prove that the main procedure's amortized expected runtime is upper bounded by a constant term, even in the presence of randomization.
- An example of a simple probabilistic operation is analyzed, where the amortized expected runtime is shown to be upper bounded by a constant term.
- The calculus is used to prove that a deterministic implementation of a dictionary data structure can run in constant amortized time using randomization.
- The speaker emphasizes the importance of being able to deal with pointer operations and randomization in the calculus.
- The talk also covers how to prove compositional respect for potential functions, which is important for analyzing composed programs.
- An inductive definition of amortized expected runtime (AER) is provided, along with a proof method for recursively defining AER.
- The speaker discusses the importance of continuation passing style and how it can be used to define weakest preconditions.
- The talk concludes by demonstrating how to analyze a loop using the calculus and proving that the amortized expected runtime is constant.


## [POPL'23] A General Noninterference Policy for Polynomial Time

URL: [https://www.youtube.com/watch?v=z_3ZKflQlUQ](https://www.youtube.com/watch?v=z_3ZKflQlUQ)

 
- The speaker presents a general noninterference policy for polynomial time.
- Noninterference is a security property that ensures the actions of a program do not depend on sensitive data.
- The speaker discusses the complexity analysis of noninterfering programs and the challenges in characterizing their complexity.
- A noninterfering type system is introduced as a means to enforce noninterference.
- The speaker provides an example of a toy type system that enforces noninterference by increasing the type level of data that may increase.
- The speaker discusses the problem of representing objects in memory and the challenges in maintaining noninterference while allowing object-oriented programming.
- The speaker introduces the concept of stratification, which is a way to characterize the complexity of programs that follow a noninterfering type system.
- The speaker provides an example of a program that follows the stratification strategy and shows how it can be analyzed using a reduction index.
- The speaker concludes by discussing the potential of using noninterference-based techniques to capture functions that are computable in polynomial time.


## [POPL'23] Admissible Types-to-PERs Relativization in Higher-Order Logic

URL: [https://www.youtube.com/watch?v=trXRnMXlYko](https://www.youtube.com/watch?v=trXRnMXlYko)

 
- The speaker presented a talk on "Admissible Types-to-PERs Relativization in Higher-Order Logic" at the 10th International Conference on Formal Verification (FV 2023).
- The goal of the presentation was to discuss how to relativize higher-order logic without adding new axioms, focusing on desirable properties and optimization.
- The speaker emphasized the importance of understanding the relationship between set-based and type-based approaches in higher logic.
- They introduced concepts such as simple types, individual functions, terms, and the connection between set theory and type theory.
- The speaker also discussed the challenges of relativizing equality and equivalence relations, and proposed a relaxed equality relation as a solution.
- They noted that relativization can be achieved by extending the axiomatic base or using conservative extensions.
- The presentation included examples of relativized terms and theorems, as well as a discussion of implementation and infrastructure.


## [POPL'23] An Order-Theoretic Analysis of Universe Polymorphism

URL: [https://www.youtube.com/watch?v=bp4yvTRM3DQ](https://www.youtube.com/watch?v=bp4yvTRM3DQ)

 
- Presentation about order-theoretic analysis of universe polymorphism
- Identity function and type theory discussed
- Universe represented as a partially ordered set (poset)
- Monad definition based on poset, category theory, and McBride scheme
- Proposed monad structure includes product level context and natural number kind
- Embedding Monad category with partial order preservation
- Discussion of theoretical boundaries and limitations of universe polymorphism
- Slogan: "Crude, effective, universal"
- Vision for a reusable and optimal library
- Mention of proof assistance system and GitHub repository



## [POPL'23] Impredicative Observational Equality

URL: [https://www.youtube.com/watch?v=xNF3okmS4HI](https://www.youtube.com/watch?v=xNF3okmS4HI)

 
- The speaker is discussing the concept of predicativity in mathematical logic and how it relates to computational expressivity.
- Predicative systems are those where quantification is only allowed over sets that have already been defined, while impredicative systems allow quantification over all possible subsets of a set.
- The speaker is working on a proof assistant that implements a computational rule to determine the relevance of a proof, which helps prevent normalization from breaking due to impredicative propositions.
- The goal is to create a system that can handle both predicative and impredicative propositions while maintaining normalization.
- The speaker mentions that Andreas Abel realized that trying to normalize irrelevant parts of a proof can lead to contradictions, and that the key is to inspect the values being compared instead of trying to normalize them.
- The speaker also discusses the idea of observational type theory, which is a way to model impredicative systems while maintaining normalization.
- The speaker thanks the audience for their questions and engagement, and says they are open to discussing the topic further offline.


## [POPL'23] A Bowtie for a Beast: Overloading, Eta Expansion, and Extensible Data Types in F...

URL: [https://www.youtube.com/watch?v=j1zLZ9Rap1o](https://www.youtube.com/watch?v=j1zLZ9Rap1o)

 
- Speaker discusses a bowtie for a beast, likely referring to a data type that can hold two different values.
 	+ Overloading and eta expansion are mentioned as ways to handle the data type.
- Speaker mentions the need for extensible data types in F, a programming language.
	+ They propose using a merge operator and a power merge operator to achieve this.
- Speaker discusses the challenges of ensuring determinism and distinguishability in the presence of overloading and eta expansion.
	+ They suggest using pattern matching and type annotations to help with this.
- Speaker mentions the need for a way to automatically calculate certain types of expressions, possibly using a theory or algorithm.
	+ They also mention the need to handle missing functions and values in the language.
- Speaker discusses the idea of a quantum computing system that can learn and make decisions based on probabilities.
	+ They suggest that such a system could be used to model certain types of mutations and behavior.


## [POPL'23] Making a Type Difference: Subtraction on Intersection Types as Generalized Recor...

URL: [https://www.youtube.com/watch?v=tXYMbCS8iVU](https://www.youtube.com/watch?v=tXYMbCS8iVU)

 
- Speaker discusses the concept of type difference and its importance in programming.
- He proposes a generalized record registration operator to calculate type differences.
- The speaker mentions the need for a language that can express type difference and prevent implementation issues.
- He also talks about the difficulty of implementing type difference in some lower level languages.
- The speaker suggests that type difference can be used to solve certain problems, such as interpreting text or accessing contacts in an app.
- He gives examples of how type difference can be applied in practice, such as subtracting single field records or interpreting substances.
- The speaker proposes a language that can carry type difference and provides algorithms to calculate it.


## [POPL'23] Quantitative Inhabitation for Different Lambda Calculi in a Unifying Framework

URL: [https://www.youtube.com/watch?v=UuXDPb_O8rQ](https://www.youtube.com/watch?v=UuXDPb_O8rQ)

 
- Speaker presented on quantitative inhabitation for different lambda calculi in a unifying framework.
- Inhabitation is the process of building a program that demonstrates the existence of a value of a certain type in a system.
- The speaker discussed the importance of understanding the context and constitutional type of inhabitation.
- Three new constructors were introduced: one for values, one for communication, and one for practical meaning.
- The speaker highlighted the significance of finding a unified framework for solving navigation problems in different systems.


## [POPL'23] Step-Indexed Logical Relations for Countable Nondeterminism and Probabilistic Ch...

URL: [https://www.youtube.com/watch?v=xz7J5pVeku0](https://www.youtube.com/watch?v=xz7J5pVeku0)

 
- The speaker introduces the concept of a step-indexed logical relation for modeling countable nondeterminism and probabilistic choice.
- This relation is used to express the equivalence between two programs with different probabilistic choices.
- The speaker mentions that this relation is an extension of the recursive type, which is a fundamental concept in functional programming.
- The relation is defined as a sequence of smaller relations, each of which is reflexive, transitive, and compatible.
- The speaker also discusses the importance of contextual equivalence and how it can be used to prove the correctness of a program.


## [POPL'23] Choice Trees: Representing Nondeterministic, Recursive, and Impure Programs in C...

URL: [https://www.youtube.com/watch?v=Zt3THGB-egQ](https://www.youtube.com/watch?v=Zt3THGB-egQ)

 
- The presentation is about representing nondeterministic, recursive, and impure programs in C using choice trees.
- The choice tree is a data structure that represents the possible choices made by a program at each step.
- Choice trees can be used to model nondeterministic and recursive programs, as well as programs with side effects.
- The presentation discusses how to use choice trees to reason about the behavior of these types of programs.
- The presenter mentions that choice trees can be used to model asynchronous awaiting frameworks in C.
- The presentation also touches on the concept of trace responsibility and the difficulty of understanding computation with redundant representation.


## [POPL'23] Hefty Algebras: Modular Elaboration of Higher-Order Algebraic Effects

URL: [https://www.youtube.com/watch?v=9S41-ntyZCY](https://www.youtube.com/watch?v=9S41-ntyZCY)

 
- The speaker presents a technique called 'Hefty Algebras' for modularly elaborating higher-order algebraic effects.
- This technique is a solution to the problem of modifying behavior when using higher order operations.
- An example of this problem is when a higher order operation breaks modularity by changing the behavior of a program without modifying its text.
- The speaker uses the example of sensor operations, which are higher order effects that can be either primitive or composed from other effects.
- A workaround for this problem is to use a nonmodular sensor Prime workaround function, but this function may not provide the desired modularity.
- The Hefty Algebras technique provides a simple and general solution to this problem by using algebraic effect handlers to model higher order effects.
- This technique ensures that the behavior of a program can be modified without changing its text, making it more modular and easier to maintain.


## [POPL'23] Tail Recursion Modulo Context: An Equational Approach

URL: [https://www.youtube.com/watch?v=TbTdEW3Zkk0](https://www.youtube.com/watch?v=TbTdEW3Zkk0)

 
- Dan Licata presented on "Tail Recursion Modulo Context: An Equational Approach"
- The talk focused on tail recursion and its optimization using contexts, which are a way to abstract over control flow
- Contexts can be used to create an equational theory that allows for optimizations like tail recursion modulo cons (TRMC)
- TRMC is a technique that transforms tail recursive functions into non-recursive ones by introducing a context that holds the state of the recursion
- Licata discussed how to implement TRMC in a functional language using continuation passing style (CPS) and delimited control
- He also mentioned the importance of ensuring that updates to shared data structures are safe and linear
- Licata provided examples and benchmarks showing the performance improvements achieved by using TRMC
- The talk was based on a paper written in 1986 by John Hughes, which is one of the foundational works in this area


## [POPL'23] Taking Back Control in an Intermediate Representation for GPU Computing

URL: [https://www.youtube.com/watch?v=0joevDrRWP8](https://www.youtube.com/watch?v=0joevDrRWP8)

 
- The speaker discusses taking back control in an intermediate representation for GPU computing.
- They mention using a formal modeling approach to rectify problems with control flow specifications.
- A novel fuzzing technique is introduced to find bugs in compiler translators.
- The speaker highlights the importance of having a clear and concise control flow rule.
- They talk about the validation process, crosschecking models, and establishing truthfulness.
- An example of a control flow graph is provided, with different types of edges representing various aspects of program execution.
- The speaker proposes a structural dominance concept to simplify the analysis of control flow graphs.
- They mention the importance of having a well-defined specification for encoding and decoding rules.
- The speaker thanks Vaseleos Clemus for their contributions to the project.


## [POPL'23] Executing Microservice Applications on Serverless, Correctly

URL: [https://www.youtube.com/watch?v=oUJvBL4U_W8](https://www.youtube.com/watch?v=oUJvBL4U_W8)

 
- Constants Call discussed microservices framework and executing them correctly on serverless platforms.
- Randy Sebastian, Vincent Penn started by deconstructing the title of the paper, explaining the difference between microservices and serverless.
- The talk focused on the interaction between microservices and serverless, benefits, challenges, and execution models.
- The speaker mentioned that moving to a serverless model can help with scaling and reduce responsibility for deployment and operation.
- They also discussed the challenge of ensuring correct execution in a serverless environment.
- The presentation included an overview of cloud computing platforms and their role in serverless computing.
- The speaker introduced the Mutor SLS open-source framework, which generates a correct serverless implementation from a given application implemented using a service model.
- The talk also covered related work, formal foundation for serverless computing fault tolerance, and transactional stateful serverless workflows.
- The presentation concluded with an evaluation of real microservice applications and the Mutor SLS framework.


## [POPL'23] An Operational Approach to Library Abstraction under Relaxed Memory Concurrency

URL: [https://www.youtube.com/watch?v=AOjfBC3bfKU](https://www.youtube.com/watch?v=AOjfBC3bfKU)

 
- The talk discusses an operational approach to library abstraction under relaxed memory concurrency.
 	+ The goal is to ensure correctness of client programs developed based on a specification given by the library, even with relaxed memory programming.
 	+ A new definition of history is proposed, which includes propagation of call and return information in library functions, and is necessary to explain behavior induced by internal communication.
 	+ A counterexample is presented, showing that standard history cannot reflect synchronization-induced call and return information in library functions.
 	+ New semantics are introduced, which ensure that earlier events are propagated before later events can happen, and are proven equivalent to RC11 declarative semantics using a library extraction theorem.
 	+ The talk also discusses the importance of choosing the right mgcdrf library call to reduce race conditions and ensure strong semantics in location accessed nonracy access.
 	+ An example implementation of a concurrent queue is given, specifying partial release and acquire access mode using relaxed memory model RCU synchronization mechanism.
 	+ The FDR refinement Checker is used to verify the implementation, which is adapted using release and record semantics.
 	+ The talk concludes with the library abstraction theorem co11 style memory model correctness condition and operational semantics based on totally ordered history, which supports library calling policy and introduces new access modes like partial release acquire access mode in the language.


## [POPL'23] The Path to Durable Linearizability

URL: [https://www.youtube.com/watch?v=yaApl0TAiBk](https://www.youtube.com/watch?v=yaApl0TAiBk)

 
- The talk is about durable linearizability, a concept in programming that ensures a data structure's correctness even in the presence of crashes.
- The speaker, Emmanuel, presents work done in cooperation with Azalea Victor.
- The goal is to create a concurrent set implementation that can survive crashes and maintain correctness.
- The challenge lies in managing nonvolatile RAM (NVRAM), which can persist data even after a crash.
- The speaker introduces the concept of linearizability, which ensures that a data structure appears to be accessed atomically, even if it is not.
- The talk covers proof techniques and optimization strategies for creating high-performance concurrent algorithms that work correctly with NVRAM.
- The speaker emphasizes the importance of understanding memory models and weak memory models in managing NVRAM.
- The presentation also discusses the concept of durable linearizability, which is a stronger notion of linearizability that can handle crashes.
- The speaker proposes a methodology for linking reset procedures to ensure data structure correctness in the presence of crashes.
- The talk concludes with an overview of techniques used to prove the correctness of concurrent algorithms and data structures in the context of NVRAM.


## [POPL'23] A Compositional Theory of Linearizability

URL: [https://www.youtube.com/watch?v=8daiHZvL1Vk](https://www.youtube.com/watch?v=8daiHZvL1Vk)

 
- The talk is about a compositional theory of linearizability in computer science.
- Linearizability is a property that ensures concurrent operations on shared data appear to be executed in some total order, even when they are not.
- The speaker discusses the benefits of using a compositional approach to verify linearizability, as it simplifies the verification process.
- They also mention the challenges of verifying linearizability, particularly in complex systems with many concurrent operations.
- The speaker refers to an early paper on linearizability and compares it to their own work.
- They explain how their theory can be used to verify the linearizability of complex systems, using program logic and sound formalization.
- The speaker also mentions the importance of locality in linearizability and how it interacts with other properties.


## [POPL'23] Locally Nameless Sets

URL: [https://www.youtube.com/watch?v=t0NDXVN_ZJA](https://www.youtube.com/watch?v=t0NDXVN_ZJA)

 
- Andy Pitts presented on locally nameless sets, a representation method for abstract syntax trees.
- The talk discussed the benefits of using this method, including its ability to avoid clashing names and simplify reasoning about properties.
- An example was given of using a de Bruijn index to represent terms without names.
- The concept of freshness was introduced, which is used to ensure that variables do not collide.
- A locally closed term is one where the index of a bound variable is strictly less than the index of a free variable.
- The talk mentioned the paper "Locally Nameless Terms in Engineering Meta Theory" (2008) and its impact on mechanized meta theory.
- The presenter also discussed the role of cofinite quantification in developing meta theory using locally nameless representation.
- An example was given of defining a freshness relation and using it to prove properties about terms.
- The talk concluded by mentioning the potential for automation in type class style and the importance of syntactic situations in gaining abstract algebraic views.


## [POPL'23] Why Are Proofs Relevant in Proof-Relevant Models?

URL: [https://www.youtube.com/watch?v=NhuZwxy4jeU](https://www.youtube.com/watch?v=NhuZwxy4jeU)

 
- Federico Ugolini presented on "Proof-Relevant Models"
- The talk focused on the relevance of proofs in understanding and working with mathematical models
- He discussed the need for a more comprehensive understanding of computational behavior in different models
- The goal is to develop a categorical theory that can capture both extensional and nonextensional aspects of these models
- The talk emphasized the importance of studying different Notions, such as intersection types and category theories
- Federico Ugolini mentioned the need for better understanding of the extensional case, as well as the study of possible isomorphisms
- He also discussed the idea of a twodimensional Lambda Theory, which would capture different aspects of mathematical models
- The talk concluded with an invitation to think about different Notions and how they can be related through structural isomorphisms
- Federico Ugolini mentioned the importance of understanding normal forms and spelling trees in the context of these models
- He also discussed the idea of Confluence, or the ability to collapse parallel reductions, and the role of categorical Insight in proving this property
- The talk concluded with a question about pro functor semantics and set typing derivation terms
- Federico Ugolini mentioned the need for a more comprehensive understanding of reduction inside category relations
- He also discussed the difficulty of getting soundness results directly, and the importance of considering invertible two-cell structures in the proof
- The talk emphasized the need for a more systematic approach to studying different mathematical models and their properties


## [POPL'23] Towards a Higher-Order Mathematical Operational Semantics

URL: [https://www.youtube.com/watch?v=POSj6Z3zVm8](https://www.youtube.com/watch?v=POSj6Z3zVm8)

 
- Speaker Stelios Popple discusses his research on higher-order mathematical operational semantics.
- He emphasizes the importance of understanding the relationship between syntax, behavior, and denotational models in language design.
- The speaker introduces the concept of natural transformation and its role in parametric polymorphism.
- He highlights the challenges in applying higher-order languages and the need for a better framework to describe their behavior.
- The speaker presents a simple format for specifying rules, consisting of premise and conclusion, with labeled terms and reduction rules.
- He compares Lambda calculus and combinator calculus, emphasizing the differences in their rule formats and the role of labels.
- The speaker discusses the importance of dinaturality as a suitable notion for parametric polymorphism.
- He introduces the concept of bifunctorial contravariant and covariant ideas and the use of end functors for financial transformation.
- The speaker suggests that the framework should be able to specify rules in a generic manner, using type rules and matching.
- He presents an example of how to model higher behavior functors using dinatural transformations.
- The speaker concludes by discussing the challenges of achieving proper call value semantics and environmental biosimilarity support.


## [POPL'23] Welcome to POPL'23

URL: [https://www.youtube.com/watch?v=A4fdGAvdPwE](https://www.youtube.com/watch?v=A4fdGAvdPwE)

 
- The Popl'23 conference is celebrating its 50th anniversary, which was first held in 1973.
- Despite the challenges of dealing with COVID-19, this year's conference has seen over 500 in-person attendees and 700 registered participants for a colocated event.
- Health and safety measures are in place, following CDC guidelines, including requiring masks and asking those who test positive for COVID-19 to isolate.
- The conference features a strong technical program and serves as a community building event.
- There are various social activities planned, such as board game nights and dinners.
- Registration is full, but those interested can be added to a waitlist if they mention they are mentoring someone or being mentored.
- The conference has generous sponsors who have contributed significantly this year.
- The program includes the Milner Award talk by Victor Vipadis and a panel discussing the last 50 years of Popl'23.
- There will be session previews, introducing ideas from selected papers in a short, accessible format.
- The goal is to make problems and solutions presented at the conference understandable, especially for students.
- The conference schedule includes two parallel tracks, with sessions taking place on the fourth floor.


## [POPL'23] Principles of Persistent Programming

URL: [https://www.youtube.com/watch?v=DwzFdrgpZao](https://www.youtube.com/watch?v=DwzFdrgpZao)

 
- Victor Rafia presented a talk on "Principles of Persistent Programming" at the PopL conference.
- The talk focused on principles and techniques for ensuring data persistence in concurrent, weakly memory-ordered systems.
- Weak memory consistency models like TSO and x86 were discussed, along with their limitations and potential improvements.
- The speaker also mentioned the importance of model checking and formal verification in establishing correctness and safety properties of persistent programs.
- The talk included a demonstration of weak memory benchmarks and the impact of different modeling approaches on performance.
- Intel's discontinuation of nonvolatile memory production was noted as a potential loss for the field, despite its academic significance and relevance to persistent programming.


## [POPL'23] Kater: Automating Weak Memory Model Metatheory and Consistency Checking

URL: [https://www.youtube.com/watch?v=5efg4ryUibs](https://www.youtube.com/watch?v=5efg4ryUibs)

 
- The speaker discusses automating the verification of weak memory models.
- An example is given of a program with shared variables and flags, and how to reason about its behavior using operational semantics.
- The speaker also talks about using cleaning algebra to express declarative axiomatic semantics.
- They mention the need for a tool that can handle irreflexivity in memory models and provide a soundness theorem.
- The goal is to reduce the memory model query language to a decidable set of expressions.
- The speaker demonstrates the tool, which generates code to check consistency based on an execution graph.
- They mention the challenges of working with large term size and linear size product.
- The speaker discusses the need for multiple irreflexivity checks in memory models and how to handle them.
- They also talk about the importance of handling reflexivity constraints in memory models.


## [POPL'23] Stratified Commutativity in Verification Algorithms for Concurrent Programs

URL: [https://www.youtube.com/watch?v=64jcmculty0](https://www.youtube.com/watch?v=64jcmculty0)

 
- Dominic Plum discussed commutativity in verification algorithms for concurrent programs.
	+ He introduced the idea of stratified commutativity, a proof rule that allows combining multiple commutativity relations.
	+ This can help simplify proofs and improve verification efficiency.
	+ A key challenge is selecting the right representative from an infinite number of equivalence classes.
	+ Stratified commutativity was inspired by trace theory and lexicographic normal form.
	+ It has applications in formal methods, programming languages, and hardware design.


## [POPL'23] A Partial Order View of Message-Passing Communication Models

URL: [https://www.youtube.com/watch?v=-PY2OYrMvtU](https://www.youtube.com/watch?v=-PY2OYrMvtU)

 
- David is presenting on message-passing communication models.
- There are two main types of communication: synchronous and asynchronous.
- Synchronous communication involves messages being sent and received at the same time, while asynchronous communication does not have a fixed order.
- David has introduced seven different communication models, ranging from fully asynchronous to restrictive synchronous.
- He is trying to formalize and compare these models using partial orders and linearizations.
- The goal is to understand which properties are decidable for each model and how they can be used for model checking.
- David has also discussed the relationship between communication models and distributed systems, and how they can be used to represent different computational scenarios.


## [POPL'23] On the Expressive Power of String Constraints

URL: [https://www.youtube.com/watch?v=DQZD5UL13No](https://www.youtube.com/watch?v=DQZD5UL13No)

 
- The speaker discussed the expressive power of string constraints.
	+ He defined three classes of string constraints: word equation, language membership, and linear arithmetic with string length allowed.
	+ Word equation and regular constraint are well-studied topics in the theory of formal logic.
	+ Membership in a formal language is an example of a language membership constraint.
	+ Decidability and undecidability are important concepts in studying constraints.
	+ The speaker mentioned that the satisfiability problem for string equations is an open problem.
	+ A string solver is a tool used to solve string-related problems, and there are both general and dedicated string solvers.
	+ The speaker discussed three key takeaways from a recent survey on string constraint solving: word equation, concatenation operation, and membership constraints.
	+ He defined Logics as formulas that are Boolean combinations of general classes of string constraints.
	+ He considered three types of formulas: word equation, length constraint, and regular membership constraint.
- The speaker then discussed the decidability status of various problems involving string constraints.
	+ The satisfiability problem for word equations with additional linear arithmetic constraints is unknown.
	+ The problem becomes undecidable if string lengths are allowed to be quadratic in an arithmetic expression.
- The speaker mentioned that understanding the solution set of a formula in a different theory can help solve string solving problems.
	+ He discussed the concept of expressive power, which is the ability to express a language using a particular logic.
- The speaker then described his main result, which characterizes Logics based on their expressive power.
	+ He showed that the class of recursively enumerable languages can be characterized by two classes of Logics: one for word equations and visibly pushdown languages, and another for regular languages with length constraints.
	+ This result provides a stronger characterization than previous results.
- The speaker mentioned that stringy quality is important for expressing certain languages using string constraints.
	+ He mentioned that the satisfiability problem for string equations with linear arithmetic constraints might also be undecidable.
	+ He mentioned that the concept of inexpressibility can be used to separate classes of Logics.
- The speaker briefly discussed the pumping lemma and its application to string constraint solving problems.
	+ He mentioned that the pumping lemma is a standard tool for proving results in formal language theory.
	+ He mentioned that the pumping lemma can be used to show that certain languages are not expressible using word equations.
- The speaker briefly discussed the concept of unanchored factors and their role in string constraint solving problems.
	+ He mentioned that understanding the behavior of unanchored factors can help solve certain string constraint problems.
	+ He mentioned that the number of unanchored factors in a word equation might be relevant to its expressibility.
- The speaker mentioned that the growth rate of languages is an important property in string constraint solving.
	+ He mentioned that certain language classes have specific growth rates, and understanding these growth rates can help solve certain problems.
	+ He mentioned that the pumping lemma can be used to study the growth rate of languages.


## [POPL'23] A Robust Theory of Series Parallel Graphs

URL: [https://www.youtube.com/watch?v=3pwxGqmr9N8](https://www.youtube.com/watch?v=3pwxGqmr9N8)

 
- Chris Watson presented a robust theory of series parallel graphs (SSPG) in the context of distributed stream processing.
- The talk focused on a formalism based on automata and regular languages to define temporal integrity constraints.
- SSPGs are used to express data streams and ensure their properties, such as taxi ride events occurring in the correct order or not overloading taxis.
- Automata models were introduced to decide whether a data stream satisfies the specified constraints, with both deterministic and nondeterministic versions having equal expressiveness.
- Nondeterministic automata can be determinized with an exponential blow in state complexity but a linear blowup in counting complexity, making them easier to construct for some applications.
- The talk also discussed the relationship between SSPGs and monadic second-order logic, as well as the potential for subtyping constraints in stream processing.


## [POPL'23] Inductive Synthesis of Structurally Recursive Functional Programs from Non-recur...

URL: [https://www.youtube.com/watch?v=misd2VGQJ3w](https://www.youtube.com/watch?v=misd2VGQJ3w)

 
- The speaker discusses inductive synthesis of structurally recursive functional programs from non-recursive examples.
- The challenge is to find a recursive function given a custom data type and example input/output pairs.
- A two-phase method is proposed: first, synthesize a non-recursive conditional free simple expression, then perform top-down search for a recursive functional program.
- Block-based pruning and library sampling are used to handle recursion and improve performance.
- The Trio system is mentioned, which includes a library of reusable functions and an efficient data structure called version space.
- A specific example of synthesizing a double function is given, with partial evaluation and block-based pruning used to check consistency.
- The speaker discusses the challenges of efficiently synthesizing billion-block programs and the use of version space to compactly represent large sets of expressions.


## [POPL'23] FlashFill++: Scaling Programming by Example by Cutting to the Chase

URL: [https://www.youtube.com/watch?v=X2CH76Luy2w](https://www.youtube.com/watch?v=X2CH76Luy2w)

 
- Arjun Radhakrishna presented FlashFill++, a tool for scaling programming by example using Flash Fill.
- The tool was inspired by user feedback and the need to translate code between different languages.
- FlashFill++ uses a small, expressive DSL (Domain Specific Language) and a middle synthesis approach to simplify translation.
- The middle synthesis approach breaks down tasks into smaller subtasks and determines intermediate values using a cut function.
- The cut function helps break problems into smaller parts and eliminates bad branches quickly.
- FlashFill++ was able to solve 92% of benchmark tasks compared to 65% for the baseline, with better performance on harder tasks.
- The tool produced programs that were around 70% shorter than Flash Fill and easier to understand.
- A user study showed that 98% of participants agreed that variable renaming in FlashFill++ made the program more readable.
- FlashFill++ is available in Excel online, PowerApps, and Power Automate and has received positive reviews.


## [POPL'23] Unrealizability Logic

URL: [https://www.youtube.com/watch?v=K9yiG1TX5kQ](https://www.youtube.com/watch?v=K9yiG1TX5kQ)

 
- Jin Wu presented on "Unrealizability Logic" in the context of program synthesis.
- The talk focused on a new technique called "unrealizability logic" to prove unrealizable synthesis problems using a new proof system.
- Unrealizability logic is built upon horror logic, which provides a basis for reasoning about correctness in verification tools.
- The motivation behind unrealizability logic is to develop a general proof system for proving synthesis problems unrealizable.
- An example of a simplified bitwise problem was used to illustrate the concept of unrealizability logic.
- The challenge of synchronizing multiple input examples was discussed, and a vectorization solution was proposed.
- Realizability logic, which focuses on synthesizing optimal solutions, was mentioned as an application of unrealizability logic.
- The talk concluded with a teaser about the potential applications of unrealizability logic in program analysis.


## [POPL'23] Affine Monads and Lazy Structures for Bayesian Programming

URL: [https://www.youtube.com/watch?v=eFGxJ3E_pEE](https://www.youtube.com/watch?v=eFGxJ3E_pEE)

 
- Christophe Pouyanne presented on "Affine Monads and Lazy Structures for Bayesian Programming" at the International Conference on Probabilistic Programming.
- The talk focused on using monadic meta language and lazy structures to implement Bayesian programming.
- Affine monads are used to represent probability distributions, while measure monads are used to build general measures (possibly unnormalized).
- Lazy programming style is used to handle infinite dimensional settings, such as the Poisson process example.
- The goal is to keep separate contexts for probability and affine structures.
- The meta language is designed with denotational semantics and implemented in Haskell, using a quasibarrel space and category space.
- The Variational Inference algorithm was mentioned as a potential application of this approach.


## [POPL'23] Type-Preserving, Dependence-Aware Guide Generation for Sound, Effective Amortize...

URL: [https://www.youtube.com/watch?v=6thkydOei9w](https://www.youtube.com/watch?v=6thkydOei9w)

 
- The speaker, Tim, will present on type-preserving, dependence-aware guide generation for sound, effective amortized probabilistic inference.
- The goal is to create a guide program that can accurately model and make predictions about complex systems with many dependencies.
- The presentation will cover the basics of sampling, observing, and inference, and how to use these concepts to build a probabilistic context-free grammar (PCFG) model.
- The speaker will also discuss the importance of preserving types and ensuring absolute continuity in the model.
- The presentation will include examples of benchmark tests and experimental results, and will explain the implications of these findings for machine learning and artificial intelligence research.


## [POPL'23] Smoothness Analysis for Probabilistic Programs with Application to Optimised Var...

URL: [https://www.youtube.com/watch?v=pZTv0Kz5WQo](https://www.youtube.com/watch?v=pZTv0Kz5WQo)

 
- The speaker is presenting on smoothness analysis for probabilistic programs with application to optimized variational inference.
- They introduce the concept of smoothness and its importance in ensuring efficient algorithms.
- The speaker discusses the differentiability property of probability models and how it affects algorithm performance.
- They present a paper that analyzes the smoothness of Prologix programs and applies this analysis to optimized variational inference.
- The speaker highlights the challenges of smoothness analysis, including the need for differentiability and the impact of program composition.
- They introduce the concept of a joint differentiability property and how it can be used to ensure soundness in analysis.
- The speaker discusses the importance of estimating gradients in variational inference and the challenges of computing them exactly.
- They present an optimized estimator that can estimate gradients more efficiently than basic estimators.
- The speaker mentions the Pyro library, which uses optimized estimators by default, but may not always guarantee soundness.
- They discuss a bug in Pyro that affects nondifferential models and how it can lead to biased or incorrect results.
- The speaker mentions a 2018 paper that extends the pathway gradient estimator with a correction term for nondifferential cases.
- They express curiosity about using smoothness analysis to automatically choose an inference algorithm in a way that is both sound and precise.


## [POPL'23] Panel: Next 50 Years of POPL

URL: [https://www.youtube.com/watch?v=m9eQCZ6bCEA](https://www.youtube.com/watch?v=m9eQCZ6bCEA)

 
- Nate: POPL has been a place for exploring new ideas, and it should continue to be.
	+ The panelists mentioned the importance of practical work and its impact on theory.
	+ They also emphasized the need for a balance between theoretical and practical contributions in POPL.
	+ The panelists discussed the importance of the review process in POPL, and they suggested that the community should focus on nurturing ideas rather than dismissing them too quickly.
- Xavier: He published a paper on compiler optimization in 1984, which was influential.
	+ He suggested that the POPL community should be more welcoming to practical work.
	+ He also mentioned the importance of understanding both the theory and practice of programming languages.
- Ben: He published a paper on differentiable programming in 2017, which has had a significant impact.
	+ He suggested that the POPL community should be more welcoming to practical work.
	+ He also mentioned the importance of understanding both the theory and practice of programming languages.
- Azalea: She published a paper on program synthesis in 2019, which has had a significant impact.
	+ She suggested that the POPL community should be more welcoming to practical work.
	+ She also mentioned the importance of understanding both the theory and practice of programming languages.
- Michael: He published a paper on type systems in 1985, which was influential.
	+ He suggested that the POPL community should be more welcoming to practical work.
	+ He also mentioned the importance of understanding both the theory and practice of programming languages.
- Nadia: She published a paper on formal verification in 2014, which has had a significant impact.
	+ She suggested that the POPL community should be more welcoming to practical work.
	+ She also mentioned the importance of understanding both the theory and practice of programming languages.
- Bens: He published a paper on machine learning in 2016, which has had a significant impact.
	+ He suggested that the POPL community should be more welcoming to practical work.
	+ He also mentioned the importance of understanding both the theory and practice of programming languages.
- Uri: He published a paper on differentiable programming in 2017, which has had a significant impact.
	+ He suggested that the POPL community should be more welcoming to practical work.
	+ He also mentioned the importance of understanding both the theory and practice of programming languages.
- Benjamin: He published a paper on compiler optimization in 1984, which was influential.
	+ He suggested that the POPL community should be more welcoming to practical work.
	+ He also mentioned the importance of understanding both the theory and practice of programming languages.


## [POPL'23] babble: Learning Better Abstractions with E-Graphs and Anti-unification

URL: [https://www.youtube.com/watch?v=ogGiKdhDmhU](https://www.youtube.com/watch?v=ogGiKdhDmhU)

 
- The presentation discusses a library learning algorithm that compresses code size by finding common abstractions in a given input corpus.
- The library uses e-graphs (equivalence graphs) and anti-unification to efficiently represent and find equivalent program versions.
- Targeted common subexpression elimination (TCSE) is used to select the best possible subset of abstractions from the original input program.
- The algorithm was tested on two datasets: a library learning dataset and a dreamcoder dataset containing complex programs with nested terms.
- The results show that Babel, the library learning tool, significantly outperforms dreamcoder in compression ratio and speed.
- The performance improvement is due to the use of e-graphs, anti-unification, and TCSE, which enable the library to learn and reuse shared structure more effectively.
- The dataset was divided into multiple domains, each representing a particular language type or program domain.
- The results show that Babel achieves near 12 compression ratio for compressive sets and clustered results closer to 100 for the dreamcoder dataset.
- Ignoring equivalence in the library learning procedure results in slightly better performance but lower compression ratio.
- The presentation highlights the importance of considering equivalence when designing library learning algorithms.


## [POPL'23] Combining Functional and Automata Synthesis to Discover Causal Reactive Programs

URL: [https://www.youtube.com/watch?v=Avq2qsYGIvw](https://www.youtube.com/watch?v=Avq2qsYGIvw)

 
- The talk is about combining functional and automata synthesis to discover causal reactive programs.
- The goal is to find the underlying model that generates the data, rather than just fitting a model to the data.
- The method involves encoding the system as a finite state automaton, which can describe the dynamics of the scene.
- The talk mentions the challenge of generalizing beyond the specific dataset used for training.
- The approach combines functional synthesis and automata synthesis in an error-driven way, with iterative refinement based on feedback.


## [POPL'23] Comparative Synthesis: Learning Near-Optimal Network Designs by Query

URL: [https://www.youtube.com/watch?v=GsRW5b9iYTg](https://www.youtube.com/watch?v=GsRW5b9iYTg)

 
- The speaker introduces a comparative synthesis framework for learning near-optimal network designs by query.
- This framework is used to solve traffic engineering problems and is a joint work with Sanjay Purdue University.
- The goal is to formulate optimization problems with well-defined objective functions and find corresponding optimal programs.
- The speaker mentions the difficulty of finding random solutions and the challenge of finding an optimal solution without specifying the objective function.
- An interactive synthesis approach is proposed, called comparative synthesis, which solves quantitative sens problems without specifying the objective function.
- The learner asks the teacher to compare two programs, and the teacher either approves or declines the proposed program based on whether it is strictly better than the previous running best.
- The learner's goal is to find a perfect objective function by spending a budget of number Q risk producing a near-optimal program.
- The speaker defines the quality of a solution intuitively as its relative rank among possible solutions.
- An example is given where the target function is the objective function, and the learner proposes programs based on teacher feedback until a quality solution is achieved.
- The key insight behind the algorithm is that neither program alone is ideal, and there are many Target functions corresponding to optimal programs.
- The learner picks informative queries and prunes the search space based on teacher response and the number of remaining candidates.
- The learning algorithm is straightforward, with the learner starting by sampling a moderate-sized candidate set and iteratively picking informative queries and pruning the search space based on teacher response.
- The goal of the voting guided algorithm is to minimize the number of queries and approve convergence rate.
- The algorithm is proven to guarantee logarithmic rate convergence.
- A comparative census framework tool called netting queue is introduced, which interacts with the user to produce near-optimal network design.
- An experimental result is shown where netting Q performs consistently better than a baseline version.
- A small-scale user study is conducted involving 17 participants, and the results indicate that netting Q produces quality recommendations and has an acceptable response time.
- The speaker concludes by presenting a new formal framework for learning neural optimal network design queries without a given objective function and proposing a new algorithm framework combining program search, objective learning, and goal achievement.
- The experimental result shows promise for the framework.


## [POPL'23] Top-Down Synthesis for Library Learning

URL: [https://www.youtube.com/watch?v=vMbhqxWrAZU](https://www.youtube.com/watch?v=vMbhqxWrAZU)

 
- The presentation discusses top-down synthesis for library learning in computer science.
- The goal is to create a more efficient and scalable abstraction learning process.
- The approach involves finding common structures in problems and reusing them.
- Aggressive pruning and branch bound search strategies are used to balance exploration and exploitation.
- The Stitch algorithm, an implementation of this approach, has shown significant improvements in efficiency and scalability.
- The utility function in the Stitch algorithm is based on minimum description length principles.
- The algorithm aims to find the smallest program that can solve a problem while considering readability and runtime performance.
- The presentation also discusses the importance of incorporating new abstractions and regularizing the learning process.
- The Stitch algorithm has been implemented in Rust and Python, with documentation and tutorials available.


## [POPL'23] SSA Translation Is an Abstract Interpretation

URL: [https://www.youtube.com/watch?v=wkIfcN3Ipd4](https://www.youtube.com/watch?v=wkIfcN3Ipd4)

 
- The talk is about SSA (Static Single Assignment) translation and its abstract interpretation.
 	+ SSA translation takes a program transformation and translates it into another program with an affected operation.
 	+ Abstract interpretation is used to produce an SSC (Static Single Assignment) form, which provides simple syntax semantics and a new algorithm.
 	+ The global value graph adds control flow information to the top of the SSA representation.
 	+ Control flow information is crucial for handling recursion in the SSA form.
 	+ The talk also discusses the use of an interpretation to produce a cyclic time graph, which can be applied to other compilation techniques.
- The speaker argues that SSA translation and abstract interpretation are sound and complete.
 	+ They use simple data flow analysis and a proof system to demonstrate this.
 	+ The process is based on operational semantics of the SST (Static Single Assignment) graph.
 	+ The speaker shows how the initial state, corresponding initial state, original program, and translated program can be related.
- The talk mentions the potential for future work in incorporating GCC (GNU Compiler Collection) to improve performance.
 	+ They suggest that heavily optimizing the implementation could lead to a level of performance comparable to traditional approaches.
- The speaker concludes with key takeaways:
 	+ SSA translation and abstract interpretation are sound and complete.
 	+ The global value graph adds control flow information to the SSA representation, providing simple syntax semantics.
 	+ Interpretation can be used to produce a cyclic time graph, which can be applied to other compilation techniques.


## [POPL'23] Dynamic Race Detection with O(1) Samples

URL: [https://www.youtube.com/watch?v=uJAADF-2i6c](https://www.youtube.com/watch?v=uJAADF-2i6c)

 
- Presented sound Epsilon Delta Property Tester that samples constantly many events to detect data races.
- Designed experiment to understand performance and show tool's running time is low and adds constant overhead.
- Compared rpt property tester with Fast Track and Pacer, showing rpt behaves well in most benchmarks.
- Mentioned observation supported by a detailed experiment section, encouraging readers to look at the paper for more information.


## [POPL'23] Statically Resolvable Ambiguity

URL: [https://www.youtube.com/watch?v=BQf0K1WBNI0](https://www.youtube.com/watch?v=BQf0K1WBNI0)

 
- The speaker's talk focuses on the concept of statically resolvable ambiguity in programming languages.
    - He uses a simplified example involving camel notation to illustrate the issue.
    - A formalism is introduced to express and handle ambiguity, with the goal of avoiding combinatorial explosion in parsing algorithms.
- The speaker proposes an approach for combining expressiveness and efficiency in programming languages.
    - He argues that embeddable formalisms can be beneficial when combined with efficient implementations.
    - He presents a benchmark showing the performance impact of introducing ambiguity to a language.
- The speaker discusses the trade-off between ambiguity and efficiency, and the importance of having a clear definition of what constitutes an operator level and grouping specification.
- The speaker mentions the challenge of proving that a formalism is complete and correct, but suggests that it is possible with careful design and implementation.
- The talk concludes with a question-and-answer session where the speaker addresses various aspects of his approach, including its applicability to real-world applications and its impact on type checking.


## [POPL'23] You Only Linearize Once: Tangents Transpose to Gradients

URL: [https://www.youtube.com/watch?v=6YGG7lWNUnM](https://www.youtube.com/watch?v=6YGG7lWNUnM)

 
- The speaker is discussing automatic differentiation and the process of linearizing functions.
- Forward mode differentiation involves performing the differentiation within the original function, while reverse mode differentiation involves computing the derivative of the output with respect to the input.
- Reverse mode differentiation can be more complicated than forward mode differentiation.
- The speaker mentions a project they are working on that involves building a system for automatic differentiation.
- They also discuss the idea of transposing expressions, which means applying the linear part of a computation first and then the nonlinear part.
- The speaker highlights the benefits of using a well-typed language for automatic differentiation, as it can help ensure correctness and simplify the implementation.
- They also mention the challenge of efficiently differentiating projections and transposing expressions.
- The speaker thanks the audience for their questions and engagement.


## [POPL'23] Efficient Dual-Numbers Reverse AD via Well-Known Program Transformations

URL: [https://www.youtube.com/watch?v=Ard3SL2JDxI](https://www.youtube.com/watch?v=Ard3SL2JDxI)

 
- Explains 'Efficient Dual-Numbers Reverse AD via Well-Known Program Transformations' presentation
    - Automatic Differentiation (AD) is reverse mode and forward mode
    - Forward mode: one input, many outputs; reverse mode: many inputs, one output
    - Dual numbers are a way to represent sensitivity information in a program
    - Reverse AD can be made more efficient using well-known program transformations
        - Structurally recursive transformations don't do anything interesting
        - Linear type transformations can be used to factor out expensive operations
        - Sparse vectors can be used to avoid allocating large amounts of memory
    - The presentation focuses on optimization techniques for reverse AD
- Background and motivation
    - Reverse AD is useful for machine learning and statistical inference
    - Exponential explosion of computation can occur in reverse AD
    - Linear algebra and distributive laws can be used to make reverse AD more efficient
- Presentation slides
    - Overview of the presentation
    - Naive transformation of reverse AD
        - Operational semantics are given, allowing the transformation to produce efficient code
        - Different semantics can be given to produce different results
    - Background slide: forward mode AD
        - Computes derivative of a function by adding extra arguments to track sensitivity information
        - Can be used for optimization and machine learning
    - Background slide: reverse mode AD
        - Computes derivative of a function by modifying the program to backpropagate sensitivity information
        - Can be used for optimization and machine learning
    - Reverse mode AD can be made more efficient using well-known transformations
        - Structurally recursive transformations don't do anything interesting
        - Linear type transformations can be used to factor out expensive operations
        - Sparse vectors can be used to avoid allocating large amounts of memory
    - The presentation focuses on optimization techniques for reverse AD
- Presentation content
    - Overview of the presentation
    - Naive transformation of reverse AD
        - Operational semantics are given, allowing the transformation to produce efficient code
        - Different semantics can be given to produce different results
    - Background slide: forward mode AD
        - Computes derivative of a function by adding extra arguments to track sensitivity information
        - Can be used for optimization and machine learning


## [POPL'23] ADEV: Sound Automatic Differentiation of Expected Values of Probabilistic Progra...

URL: [https://www.youtube.com/watch?v=4ifhXVmV_RM](https://www.youtube.com/watch?v=4ifhXVmV_RM)

 
- The talk presented a natural extension of forward mode automatic differentiation (AD) to handle expressive probabilistic programs.
- The goal is to automate the construction of unbiased derivative estimators for various objective functions, especially those with specific properties like parameterized computation or low variance.
- The proposed framework, called Adam, aims to make it easier for users to experiment with different tradeoffs between variance and speed when implementing gradient estimation strategies.
- Adev is a user-friendly interface for automatic differentiation that handles probabilistic programs using forward mode AD.
- The talk mentioned the challenge of propagating derivative information in probabilistic primitives and the need for correctness specifications to ensure unbiasedness.
- The authors explored the use of higher order functions, measure theory, and continuation monads to represent probability distributions and compute derivatives.
- A Phantom estimator was introduced as a way to consider paths that are not typically explored by existing methods.
- The talk concluded with a recap of the main points and an invitation for questions.


## [POPL'23] When Less Is More: Consequence-Finding in a Weak Theory of Arithmetic

URL: [https://www.youtube.com/watch?v=ToqlbSOFn_E](https://www.youtube.com/watch?v=ToqlbSOFn_E)

 
- The speaker presented a talk about finding stronger consequences in a weak theory of arithmetic, using a monophone generation scheme and linear case theory.
- They discussed the concept of a consequence-finding algorithm that takes a formula as input and outputs a stronger consequence formula.
- The talk included examples of linear inequalities and polynomials, with the goal of extracting consequences from these expressions.
- The speaker mentioned the importance of effective satisfiability, which is the ability to determine whether a formula is satisfiable within a given time or resource limit.
- They also discussed the concept of a linear restriction, which is a way to restrict the domain of a polynomial or other mathematical expression.
- The talk concluded with a discussion of monotonicity and experimental results from running the consequence-finding algorithm on various benchmarks.


## [POPL'23] Higher-Order MSL Horn Constraints

URL: [https://www.youtube.com/watch?v=buiJs-0iCKk](https://www.youtube.com/watch?v=buiJs-0iCKk)

 
- Presentation about higher-order MSL (Monadic Second-Order Logic) and its horn constraints.
- MSL is a logic that allows quantification over monadic predicates, which are predicates taking one argument.
- The talk focuses on the first-order fragment of MSL, which does not allow quantification over variables or terms.
- Higher-order MSL can express more complex properties than first-order logic, but it also makes decidability and automation more challenging.
- The presentation discusses a verification approach using high-order automata and proof concepts implemented in verified silver programming in Haskell.
- High-order MSL can be used to characterize and solve safety problems in a vertical way, contributing to establishing a foundation for high-order logic.
- The talk also mentions the challenge of grasping high-order logic and the need for a common framework to understand specific problems.
- High-order logic can provide an accessible representation for model checking problems.
- There is a connection between MSL's first-order fragment and regular languages, which can be functionalized using high-order bit.
- The talk suggests that higher-order MSL can correspond to regular automata, but this may involve an exponential blowup in complexity.
- High-order MSL can be used to easily express satisfiable automata.


## [POPL'23] Fast Coalgebraic Bisimilarity Minimization

URL: [https://www.youtube.com/watch?v=9F0dVBF1hnc](https://www.youtube.com/watch?v=9F0dVBF1hnc)

 
- The speaker is presenting a fast general algorithm for minimizing bisimilarity in coalgebras.
- This work is an improvement over previous algorithms, which had limitations such as only handling certain types of automata and requiring extra factors to be computed.
- The new algorithm can handle various types of automata and has better complexity, making it more efficient and scalable.
- The speaker also mentions the challenges of implementing this algorithm in practice, including the need to efficiently track changes and handle large memory requirements.
- The presentation concludes with a comparison between the new algorithm and other tools, showing that the new algorithm is faster and can handle larger input sizes.
- The speaker also discusses potential future work, including exploring how to further optimize the algorithm and integrate it into existing tools.


## [POPL'23] Qunity: A Unified Language for Quantum and Classical Computing

URL: [https://www.youtube.com/watch?v=E2yMPeD1jHQ](https://www.youtube.com/watch?v=E2yMPeD1jHQ)

 
- Qunity is a unified language for both quantum and classical computing
- It aims to make it easier to express quantum algorithms in a more general way
- The language is designed to be expressive enough to describe various types of quantum algorithms
- Qunity provides a reversible type system, which is useful for quantum computing
- It also offers features like pattern management, variable reuse, and customization choices
- Qunity can compile classical programs into lower level quantum circuits
- The language is motivated by the need to make large scale quantum algorithms more efficient
- It is currently targeting super efficient compilation


## [POPL'23] Proto-Quipper with Dynamic Lifting

URL: [https://www.youtube.com/watch?v=aNFjxkZRT9g](https://www.youtube.com/watch?v=aNFjxkZRT9g)

 
- Presentation about Proto-Quipper with Dynamic Lifting, a technology that compiles high-level programming content into low-level circuits for quantum computers.
 	+ The system consists of two runtimes: circuit generation time and runtime call circuit execution time.
 	+ Circuit generation time is responsible for compiling the high-level program, while runtime call circuit execution time is responsible for sending and executing the generated circuit.
 	+ Proto-Quipper uses Dynamic lifting to handle content, which allows for more efficient processing of quantum information.
 	+ The presentation covers a categorical model for dynamic lifting and typing judgments associated with modality.
 	+ The system aims to provide a general categorical model for dynamic lifting and demonstrate operational semantics that respect categorical semantics.


## [POPL'23] CoqQ: Foundational Verification of Quantum Programs

URL: [https://www.youtube.com/watch?v=RjKCP8U-1Zg](https://www.youtube.com/watch?v=RjKCP8U-1Zg)

 
- The speaker discussed their work on formally verifying the correctness of Quantum programs using the Coq proof assistant.
- They mentioned the challenge of expressing Quantum States and operations in a formal system.
- Coq's support for arbitrary data types and direct notation for Quantum operators simplifies equation reasoning and formalization.
- The speaker emphasized the importance of human readable statements and local parallel reasoning in Quantum program formalization.
- They also discussed the need for a library of classical analysis objects compatible with the Quantum framework.
- The Arcadian subgroup problem was used as an example of a Quantum algorithm that could be formally verified.
- The speaker mentioned the potential for using a cloud-based toolchain to verify Quantum programs and the need for a formally verified compiler.


## [POPL'23] Modular Primal-Dual Fixpoint Logic Solving for Temporal Verification

URL: [https://www.youtube.com/watch?v=GdNs9ZILuVw](https://www.youtube.com/watch?v=GdNs9ZILuVw)

 
- Hiroshi introduced the Modular Primal-Dual Fixpoint Logic Solving for Temporal Verification, which uses a modular approach to constraint-based verification.
 	+ The method involves using exponent logic and joint work with Eric.
 	+ The goal is to identify foreign properties and express them in a way that can be used for verification.
 	+ The method consists of three steps: eliminating existential quantifiers, replacing inductive practices with guarded induction, and using well-founded relations for determination.
 	+ The presentation won the distinguished paper award.
- Questions from the audience included:
 	+ How important is modular encoding?
 	+ Does complement property always need a fact?
 	+ What language logic is used for closed complement?
 	+ How does one express relative completeness and validity in procedure?



## [POPL'23] Optimal CHC Solving via Termination Proofs

URL: [https://www.youtube.com/watch?v=hrIL0FYLMKY](https://www.youtube.com/watch?v=hrIL0FYLMKY)

 
- The speaker introduced a new method for optimal CHC solving via termination proofs.
  - The method uses a termination proof to verify the safety of a program.
  - The speaker demonstrated how to use a ranking function and a strategy synthesis engine to check maximality.
  - The method was applied to a maximum specification synthesis problem and shown to be sound.
  - The speaker also discussed the difficulty of solving optimization problems and the importance of termination analysis.
  - The method was compared to other existing methods and shown to be practical and useful.


## [POPL'23] From SMT to ASP: Solver-Based Approaches to Solving Datalog Synthesis-as-Rule-Se...

URL: [https://www.youtube.com/watch?v=DQ40UBmsQ9k](https://www.youtube.com/watch?v=DQ40UBmsQ9k)

 
- Speaker discusses the use of AI technology to solve the data log synthesis problem.
 	+ The approach consists of two main parts: generating candidate data log rules and filtering them to find a subset that fits the input/output example.
 	+ The second part of the problem, rule selection, is considered a synthesis real selection problem.
 	+ The speaker mentions two tools used in their progression algorithm: monosynth and loopsynth.
 	+ Monosynth has a disadvantage in that it makes uneducated guesses for candidate rules, while loopsynth encodes the candidate rule and sat formula to reiterate the idea.
 	+ The speaker then introduces ASP synth, an off-the-shelf ASP solving tool that encodes the problem as an answer set program.
 	+ ASP solvers can choose whether a rule is part of the answer set, making them effective for data log synthesis.
 	+ The speaker highlights two main flavors of ASP solving: translating sets and native custom solvers using satlike techniques.
- The speaker mentions some limitations and potential improvements for their approach:
 	+ Encoding negation in ASP can be challenging.
 	+ The current Benchmark Suite is small, which may affect scalability.
 	+ The approach may need to generate rules instead of preselecting them.
- Question from the audience about scaling the approach and preselected rule sets:
 	+ The speaker acknowledges that their approach may not scale well and suggests exploring existing data log programs that can be mutated for future work.
 	+ The speaker agrees with the assumption that starting with a preselected rule set is a limitation and mentions it as a potential area for improvement.


## [POPL'23] The Fine-Grained Complexity of CFL Reachability

URL: [https://www.youtube.com/watch?v=PNg5JeXL7us](https://www.youtube.com/watch?v=PNg5JeXL7us)

 
- Researcher presents recent work on understanding fine-grained complexity of CFL reachability, a problem with wide application in areas like interprocess data flow analysis and program slicing.
  - The talk highlights two specific contributions: a better n^(25/8) algorithm for the pair reachability problem and an n^3 lower bound for the on-demand reachability problem.
  - The research also discusses the K language, a set of well-matched parentheses that requires fine-grained complexity analysis.
  - The talk addresses the complexity of CFL reachability in specific languages, aiming to find an exact expression for the running time function based on input size.
  - The research considers two variants of the CF reachability problem: a pair production problem and an on-demand problem.
  - The talk highlights the K language and its relevance to the fine-grained complexity problem, aiming to identify an exact expression for the running time function based on input size in specific cfgs.
  - The research discusses the complexities of CFL reachability in specific languages, aiming to find an exact expression for the running time function based on input size and the number of edges in the graph.
  - The research also considers the complexity of CFL reachability in terms of the database size, aiming to find a complexity result bound for the term n (number of vertices) and M (number of edges).
  - The talk highlights the author's two main results: a pair reachability problem with an interesting CSG running time of n^Omega + 3/2 and an n^3 lower bound for the on-demand reachability problem.
  - The research also discusses Anderson's pointer analysis, showing a subcubic algorithm for the term M (number of edges).
  - The talk highlights three contributions: presenting a flavor idea of key reductions, discussing CFL reachability in sparse and dense graphs, and addressing the on-demand reachability problem.


## [POPL'23] Single-Source-Single-Target Interleaved-Dyck Reachability via Integer Linear Pro...

URL: [https://www.youtube.com/watch?v=fkB1j3lTEYM](https://www.youtube.com/watch?v=fkB1j3lTEYM)

 
- The presentation discusses a new algorithm for the interleaved Dyck reachability problem, which is a generalization of the context-free grammar reachability problem.
- The traditional approach to solving this problem suffers from two major sources of imprecision: multipass precision issues and final summary approximation.
- The proposed algorithm addresses these issues by breaking the graph into individual passes and using a more precise formulation, avoiding the need for multiple summaries.
- The algorithm is evaluated using two benchmarks: the contact sensitivity benchmark and the concurrent program benchmark.
- The new algorithm performs slightly better than the traditional summary-based algorithm in terms of running time, with around a 5-10% reduction in false positives.
- The presentation also compares the performance of the new algorithm to that of the SPDs reachability algorithm and a CUDA approximation algorithm.
- The domain-specific tool used in the experiment shows a slight improvement in precision compared to the ECC algorithm, with around a 7% reduction in false positives.
- The presentation concludes that the single-Source-single-Target interleaved diagram algorithm provides a new perspective on the problem and demonstrates improved precision and efficient routing time.


## [POPL'23] Context-Bounded Verification of Context-Free Specifications

URL: [https://www.youtube.com/watch?v=WihiMdcouWg](https://www.youtube.com/watch?v=WihiMdcouWg)

 
- Speaker discusses the "context bounded refinement verification problem" for multithreaded programs with shared memory.
- The problem is reduced to a reachability question in a context-free specification, which is shown to be NP-complete.
- A refinement verification algorithm is presented, which checks whether a fixed number of thread context switches result in a specific shared state.
- The speaker mentions that the problem is related to the "reference counting" problem, where shared resources are accessed by multiple threads.
- An example of reference counting is given, where a counter is used to keep track of the number of threads accessing a resource.
- The speaker discusses the challenge of ensuring that the counter is updated correctly when threads access and release the resource.
- A model checking approach is proposed to prove that the program behaves as expected.
- The speaker mentions that the problem is not easily algorithmic and requires manual intervention.
- The talk concludes with a reference to a paper by Shahbazian and Kadiry, which discusses the "context bounded reachability" problem.


## [POPL'23] An Algebra of Alignment for Relational Verification

URL: [https://www.youtube.com/watch?v=_H299Iy4Rlc](https://www.youtube.com/watch?v=_H299Iy4Rlc)

 
- Speaker presents an algebraic approach to relational verification using a new concept called alignment.
- Alignment is used to establish a relationship between two programs that compute the same function in different ways.
- The speaker uses a Relational Judgment to express this equivalence.
- The talk covers the following topics:
  - Introduction
  - Ramana's algebra of alignment
  - Relational verification
  - Example: factorial computation
  - Algebraic techniques for relational verification
  - Soundness and completeness
  - Discussion on related work and future directions
- The speaker mentions the importance of finding a new proof principle that respects the relational horror logic.


## [POPL'23] Grisette: Symbolic Compilation as a Functional Programming Library

URL: [https://www.youtube.com/watch?v=E_gNz0XLw1o](https://www.youtube.com/watch?v=E_gNz0XLw1o)

 
- The speaker introduced Grisette, a functional programming library for symbolic compilation.
- Symbolic compilation is a technique used to build a program reasoner or solver.
- Grisette is written in Haskell and uses a purely functional approach.
- The library provides a typed, higher-order interface for building synthesizers.
- The speaker discussed the design goals of Grisette, including efficiency, usability, and performance.
- Grisette includes a built-in benchmarking tool to evaluate solving time and formula size.
- The speaker mentioned that Grisette is part of a larger project to make symbolic compilation more accessible to the wider community.
- The speaker encouraged people to try building their own symbolic compilers with Grisette and provided resources for getting started.
- The speaker also discussed the benefits of using a functional programming approach and the challenges of implementing symbolic compilation in an imperative language.


## [POPL'23] HFL(Z) Validity Checking for Automated Program Verification

URL: [https://www.youtube.com/watch?v=aRBLGZ7_iXQ](https://www.youtube.com/watch?v=aRBLGZ7_iXQ)

 
- The presentation is about HFL(Z) Validity Checking for Automated Program Verification.
- The goal is to provide a uniform approach to automated verification of high order programs with various properties.
- The method involves transforming the given HIV formula into an atmc formula using a greatest fixed point operator.
- New HFC checking is done by considering special cases and applying equivalence preserving transformations.
- The main challenge is encoding arbitrary regular temporal property in high order program detection problem.
- The presentation focuses on the method overview, HF divided checking, and the idea of approximating HIV formula with an emulative Z formula.
- The idea is to transform the formula into a form that can be verified using existing tools.
- The presentation also discusses the power verification method and the tool's performance compared to previous automated tools.
- The tool outperforms previous tools in most cases, except when dealing with certain properties like fairness.
- The tool is designed for common backends and is a general approach for automated high order program verification.


## [POPL'23] Witnessability of Undecidable Problems

URL: [https://www.youtube.com/watch?v=3SPNPfA049I](https://www.youtube.com/watch?v=3SPNPfA049I)

 
- The talk is about the witnessability of undecidable problems in computability theory and programming languages.
- A decidable problem has an algorithm that always terminates with a correct answer, while an undecidable problem does not.
- Witnessability refers to the ability to construct a proof or certificate for a problem's solution.
- The speaker presents a theorem that reduces the holding problem to the witnessability problem, implying that the witnessability problem is also undecidable.
- Different approximation methods can be used to improve the quality of an approximation, but they may not always converge to the exact solution.
- Counterexample-guided abstraction refinement is a technique used to refine an abstraction based on counterexamples.
- The speaker mentions that some problems are unstable or have weaknesses that can affect their solvability.
- The talk covers the concept of reducibility, which is the ability to transform one problem into another with similar properties.
- Witness functions are used to verify whether a program's output is correct.
- The speaker discusses the importance of implementing admissible approximation methods in programming languages and compilers.
- The talk concludes that witnessability is a general property that applies to most practical programming languages.



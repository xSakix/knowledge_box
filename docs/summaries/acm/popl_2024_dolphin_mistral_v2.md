## [POPL'24]  Welcome To POPL 2024

URL: [https://www.youtube.com/watch?v=E-plTaqhBfE](https://www.youtube.com/watch?v=E-plTaqhBfE)


- Philippa Gartner is chairing the conference
- London winter season bubbling
- Partner Christmas went conference in California
- Covid-19 affecting attendance
- Hand sanitizers available around the spot
- Lunch on first and third floor, entertainment provided
- Dei lunch and receptions happening
- Experimenting with a different schedule for lunch
- Organizing committee acknowledgment and thanks
- Ninga, the artist, responsible for signage and T-shirt design
- Nat, PhD student, saved the day with screen issues
- Modern font design used in the conference material
- Derek, enthusiastic organizing committee member, praised for his help
- Conference location and schedule overview
- Popple chair's name mentioned
- No context or information available for some parts of the transcript


## [POPL'24] A New Perspective on Commutativity in Verification

URL: [https://www.youtube.com/watch?v=S_lYmWWZD2w](https://www.youtube.com/watch?v=S_lYmWWZD2w)


- AZ Fan introduces the topic of commutativity verification, discussing its historical context, impact on programming language research, and its various applications in verification and testing.
- The speaker explains the concept of commutativity and how it applies to concurrent programs. They also discuss program reduction and the use of commutativity reasoning in partial order reduction methods.
- AZ Fan presents a new perspective on commutativity verification, focusing on the search for alternative programs and proof methods. They discuss the use of logical reasoning engines and the benefits of operational proof over traditional proof methods.
- The speaker highlights the importance of algorithmic verification schemes and the role of commutativity reasoning in program verification. They discuss the challenges and opportunities in this area and present a unified framework for combining proof search and program search.
- AZ Fan discusses the concept of abstract commutativity and how it can be used to leverage commutativity in different contexts. They provide examples and insights into the use of commutativity in message passing and distributed systems.
- The speaker introduces the idea of stratified commutativity and its application in the verification of concurrent programs. They discuss the potential challenges and opportunities in extending this concept to larger and more complex systems.
- AZ Fan emphasizes the need for further research in the field of commutativity verification, highlighting the Grand challenge of enabling the movement of program parts and the formation of alliances. They also mention the need to bridge the gap between theory and practice for successful application in industry.
- The speaker addresses a question about using property language to get commutativity relations in different programming languages, acknowledging the complexity of dealing with sophisticated abstractions and semantics statements.
- AZ Fan provides an insight into the successful practices and techniques used in the industry, emphasizing the need for a balance between search strategies and performance considerations.
- The speaker takes a question about the connection between Tre automata, graph quality, and saturation techniques. They acknowledge the potential for further research in this area and the ongoing exploration of machine learning and logical reasoning engines in program verification.


## [POPL'24] Implementation and Synthesis of Math Library Functions

URL: [https://www.youtube.com/watch?v=sFtnd9eWt8g](https://www.youtube.com/watch?v=sFtnd9eWt8g)


- The speaker discusses the implementation of elementary functions using primitive arithmetic operations.
- The talk highlights the trade-off between speed and accuracy in function implementation.
- They present their work on implementing the cosine function using primitive arithmetic, focusing on the error bound and tradeoffs.
- The speaker mentions the importance of catching typos and the use of a megal lab workbench for safe and modular function implementation.
- They introduce the concept of range reduction and reconstruction in function implementation.
- The speaker emphasizes the need for type-level tracking of error bounds and the integration of verification tools like Gappa and Herby.
- They briefly discuss the use of a DSL to implement arbitrary computable functions and the potential for implementing Newton's method.


## [POPL'24] Enhanced Enumeration Techniques for Syntax-Guided Synthesis of Bit-Vector Manipu...

URL: [https://www.youtube.com/watch?v=lbDxCZ7wh80](https://www.youtube.com/watch?v=lbDxCZ7wh80)


- The speaker discussed the importance of syntax guides and the role of semantic specification in reducing the search space for synthesis.
- They provided an example of a challenging problem represented using bit vector expressions from Hacker's Delight.
- The speaker emphasized the need for both semantic and syntactic specifications to guide the synthesis process.
- They discussed two major approaches to syntax synthesis: bottom enumeration and top deduction.
- The bottom enumeration approach searches an infinite space of candidate solutions, while the top deduction approach starts with a small solution and expands it.
- The speaker also highlighted the challenges of combining different ideas and techniques in syntax synthesis.
- They mentioned using large language models as guidance for syntax synthesis.
- The speaker shared their experience in evaluating bit vector synthesis and the challenges faced in the process.
- They expressed confidence in the general usefulness of the techniques presented.
- The speaker acknowledged the importance of context in applying these techniques effectively.
- They thanked the audience for their attention and invited questions.


## [POPL'24] Efficient Bottom-Up Synthesis for Programs with Local Variables

URL: [https://www.youtube.com/watch?v=a_dvy9s44G4](https://www.youtube.com/watch?v=a_dvy9s44G4)


- Introduced a new efficient synthesis algorithm for programming local variable start
- Example program is fold common high-order function
- Challenges in synthesizing programs like fold are tackled using either bottom or top synthesis approach
- Observational equivalence work program like fold is challenging
- Proposed idea is "lifted interpretation" combining top interpretation with program grammar and bottom enumeration operation with observational equivalence
- Example of two fold programs x 2 1 and x uh X Plus LM 2 is used to explain the method
- The method is applicable to complex domains like web automation
- The fold function example is used to solve a web automation problem
- Lifted interpretation is used to efficiently reduce space in the program local variable domain
- The approach outperforms C technique for solving benchmark problems
- The main takeaway is the proposed lifted interpretation for interpreting programs and reducing space using equivalent classes in local variable domain.


## [POPL'24] Optimal Program Synthesis via Abstract Interpretation

URL: [https://www.youtube.com/watch?v=OlFnav1sm4A](https://www.youtube.com/watch?v=OlFnav1sm4A)


- Steve Sanwick presented work on optimal program synthesis by abstract interpretation.
- He discussed the use of program synthesis in data science and user programming tasks.
- Examples of tasks include identifying specific behaviors in animal interactions or detecting suspicious behavior in vessel tracking.
- The goal is to find the optimal synthesis, rather than perfect classification, focusing on maximizing accuracy.
- The speaker introduced the concept of abstract interpretation and how it can be used for optimization.
- He also introduced generalized partial programs and their use in constructing search juristics.
- The speaker demonstrated an example of synthesis for car trajectory analysis.
- He mentioned the use of regular expressions, temporal logic, and parameterized units for representing programs.
- The speaker emphasized the importance of reducing branching factor by using structured spaces and partitioning.
- He discussed the implementation of two different domain-specific languages, QUVER and NEAR.
- The speaker compared the performance of their approach with SMT-based optimal synthesis and meta sketch.
- He also considered using breadth-first search for finding heuristics in the search space.
- The speaker addressed limitations of abstract abstraction and internal domain and suggested possible ways to improve it.


## [POPL'24] Generating Well-Typed Terms that are not "Useless"

URL: [https://www.youtube.com/watch?v=KkE-wVqUbVQ](https://www.youtube.com/watch?v=KkE-wVqUbVQ)


- Speaker: Justin Frank
- Topic: Generating Well-Typed Terms
- Key Points:
  - Differential testing - generating random programs and comparing their outputs
  - Explanation of generating well-typed terms
  - Discussion of the need for a recursive generation algorithm
  - Example of generating a function with a recursive generation problem
  - Overview of the process of expanding typed holes
  - Use of extension variables to delay the choice of argument type
  - Discussion of the limitations of choosing the type function early
  - The need for a method to easily identify location changes
  - The introduction of the call extension variable to identify location changes
  - Example of using extensible Lambda application rule
  - Discussion of the need for an efficient implementation
  - Evaluation of the effectiveness of the method
  - Discussion of the need for a standalone implementation
  - Mention of the O Camel standalone implementation
  - Questions about the implementation and testing type checkers


## [POPL'24] Indexed Types for a Statically Safe WebAssembly

URL: [https://www.youtube.com/watch?v=mkTgnFrv7lI](https://www.youtube.com/watch?v=mkTgnFrv7lI)


- Introduces WebAssembly (WM) and its design goals, including speed, safety, portability, and small binary footprint.
- Explains WM's dynamic check mechanism for memory access, which ensures safety by denying access to anything outside the allocated memory region.
- Describes the challenges of applying WM to embedded systems, where virtual memory becomes expensive and the dynamic check mechanism may not be applicable.
- Highlights the need for static safety and introduces the WUM precheck system, which uses a type system to ensure safety without dynamic checks.
- Explains the WUM precheck system's type system, which includes a stack-based language and annotations to enforce constraints and safety guarantees.
- Demonstrates the performance benefits of the WUM precheck system compared to WM with dynamic checks, including a 171x speed improvement for memory-intensive benchmarks.
- Discusses the potential of applying the type system to security-critical applications and the need for further research in this area.


## [POPL'24] The Essence of Generalized Algebraic Data Types

URL: [https://www.youtube.com/watch?v=8l7JAmMh3v4](https://www.youtube.com/watch?v=8l7JAmMh3v4)


- The speaker introduces GDs (Generalized Algebraic Data Types) and their usefulness.
- Examples include JDS Express vector, fixed length without usage dependent type and vector natural number.
- The presentation discusses the extension of the calculus system, recursive types, equality, injectivity rule, and calculus expressiveness.
- The speaker presents two additional judgments: provability rule and class judgment (discriminability judgment).
- Static semantic rules and dynamics semantics are also covered.
- The speaker explains how their work aims to extend data systems and define two additional judgments.
- They argue that the calculus is expressive enough to represent JTS.
- The speaker presents the idea of model division into two stages and constructing both a syntactic and semantic model.
- They discuss the interpretation of type and how to maintain information while avoiding using purely semantic relations.
- The speaker presents the new calculus and its study of GDTS.
- They mention future work, including extending the calculus and the relational approach to quantified kind.


## [POPL'24] Ill-Typed Programs Don't Evaluate

URL: [https://www.youtube.com/watch?v=B-CPdJIK-60](https://www.youtube.com/watch?v=B-CPdJIK-60)


- The talk focuses on well-typed programs and their guarantees
- Free certain class exception runtime program could be wrong
- Well-typed untypable guarantee could be incorrect
- The type system cannot see type system, expressive enough to prove correctness properties
- Mainstream type systems might be a problem due to complexity
- Incorrectness logic reasoning could be inspired by type systems
- A new view of type systems could be seen as a proof system
- Type systems can provide a foundation for incorrectness reasoning
- Two-sided judgment allows for assumptions and conclusions involving arbitrary typing
- Expressive power of two-sided system gives a new kind of type theory
- The talk introduces a new view of type systems as sequin calculus formulas
- The rule justifying a formula can be categorized into left or right rules depending on formula occurrence
- The talk discusses the need for left rule refutation in certain cases
- Function type term is introduced to allow expressing new kind dependencies
- The talk presents an example of a new kind of semantics: Call-value semantics
- The talk introduces a new function type term for liveness safety verification
- The talk presents a version of type systems with syntactic twosidedness
- The talk discusses automatic type inference and constraint generation




## [POPL'24] An Infinite Needle in a Finite Haystack: Finding Infinite Counter-Models in Dedu...

URL: [https://www.youtube.com/watch?v=_gMQxhqmOgA](https://www.youtube.com/watch?v=_gMQxhqmOgA)


- The talk focuses on infinite counter examples and deductive verification.
- It discusses an approach to find even though they are infinite.
- The setting is SMT-based deductive verification, where the goal is to verify that a property is satisfied.
- The talk presents a finite representation of an infinite model, enabling symbolic model checking.
- An efficient search procedure is presented to find a satisfying infinite model given a formula.
- The talk identifies a new decidable fragment of first-order logic called "Osc" and demonstrates its applicability.
- It introduces a tool called Fast Stand to find infinite models with symbolic encoding and searching using templates.
- The speaker concludes by discussing the applicability of symbolic models in various domains and future work.


## [POPL'24] Mostly Automated Verification of Liveness Properties for Distributed Protocols w...

URL: [https://www.youtube.com/watch?v=v4Kx0UkVbKw](https://www.youtube.com/watch?v=v4Kx0UkVbKw)


- Speaker introduces the topic of automated verification of the liveness property in distributed protocols
- They mention the challenge of nondeterminism and synchrony in system formal verification
- The speaker discusses the use of ranking functions for safety property verification
- They highlight the importance of collaboration in the development of such verification tools
- The speaker notes that while safety property verification has seen significant progress, verifying liveness is much harder
- The presentation covers existing tools and their limitations
- The speaker introduces a new method for verifying liveness using ranking functions and static analysis
- They discuss the use of linear polynomial ranking functions and the need to find valid assignments of coefficients
- The speaker demonstrates the effectiveness of their method on practical distributed protocols like the Mutual Exclusion Lock protocol
- They emphasize the need for user guidance in the process of verifying liveness properties
- The speaker concludes by highlighting the effectiveness and practicality of their method


## [POPL'24] Decision and Complexity of Dolev-Yao Hyperproperties

URL: [https://www.youtube.com/watch?v=7_EdecEJHM4](https://www.youtube.com/watch?v=7_EdecEJHM4)


- The talk focuses on decision complexity and hyperproperties.
- It explores two different types of properties: functional and security.
- The speaker presents a simple example of a server holding a monetary prize and solving a challenge to obtain it.
- The talk discusses the concept of fairness in rewarding the person with a correct solution.
- It highlights the distinction between functional and security properties.
- The speaker introduces the concept of Doio hyperproperty, which studies the behavior of a concurrent system and security properties in an adversarial environment.
- They propose a theoretical foundation and decision complexity result for Doio hyperproperty.
- The speaker outlines the challenges of implementing the proposed framework and the potential future work.
- The talk concludes with a complexity overview of nonrelational hyperproperties and a discussion of the limitations of the current approach.


## [POPL'24] Soundly Handling Linearity

URL: [https://www.youtube.com/watch?v=sHGrKEoWtm8](https://www.youtube.com/watch?v=sHGrKEoWtm8)


- PhD student L from University of Edinburgh discusses handling linearity in programming
- L type ensures something is used exactly
- Sound handling of linearity involves understanding control flow linearity
- Linearity guarantees something is used exactly
- L type can be hard to implement and handle
- Linearity can be used to manipulate control flow
- Control flow linearity restricts the use of values and characterizes whether a value contains a linear source
- Linearity can also be used to track rarity exactly
- L type ensures that linear variables are only used once
- Linearity can be used to handle control flow linear operations using Multi-Shot handlers
- Tracking control linearity can help in making programming more precise
- A paper was presented that formalizes the concept of control flow linearity
- The paper also introduces the concept of an annotated control flow linear operation
- Continuation context operations are also annotated with control linearity
- Control flow linearity can be used to track the control flow of linear configurations
- The concept of control flow linearity is related to continuation functions
- The concept of control flow linearity can be extended to advantage types
- The speaker mentions that there are ongoing discussions on this topic
- The speaker also mentions that there are no mic problems and invites questions via Discord


## [POPL'24] Answer Refinement Modification: Refinement Type System for Algebraic Effects and...

URL: [https://www.youtube.com/watch?v=S4XojkWuEtY](https://www.youtube.com/watch?v=S4XojkWuEtY)


- Introduced algebraic effect handlers and refinement types
- Algebraic effect handlers represent effects in a modular way, with special terms called operations and handlers
- Refinement types represent specific properties of types
- The main contribution is the development of a type system for effect handlers and refinement types
- The type system provides precise verification and ensures that programs written with effect handlers and refinement types are type-checked
- Two approaches are introduced: one-level approach and nested approach for handling types
- Answer type modification is presented as a way to handle requirement changes
- The author argues that refinement type verification can be achieved through CPS transformation
- The implementation of the type system is shown using the OK library and type requirements
- The speaker answers a question about the effect of type inference on implementation
- The speaker discusses the difference between deep and shallow handler variants, and the need for an adapted variant handler for OCaml
- The speaker shares an example of a non-deterministic choice handler
- The speaker repeats a question about CPS translation and OCaml
- The speaker discusses the potential challenges of reflecting type answer modification with different implementation versions
- The speaker thanks the audience


## [POPL'24] Effectful Software Contracts

URL: [https://www.youtube.com/watch?v=__F3ML62xd8](https://www.youtube.com/watch?v=__F3ML62xd8)


- The talk discussed contract-based programming approach using the philosophy of specification and code.
- An example was given for generating RSA public-private key pairs using a function that takes a thunk to produce a random prime number.
- A contract-based approach allows for easy expressive specifications compared to type systems.
- Contract checking is typically done at runtime, but the speaker assumes it is performed at runtime as well.
- Contract use effect means that contracts should be implemented in a reasonable manner.
- A literature review found that there were many papers on the use of effects in contracts.
- An example contract that uses effect intentionally was provided from a paper that ensures value flow in ordinary ML doesn't violate invariance.
- The speaker discussed a theoretical model and implementation details using mutable references and effect handlers.
- The goal is to unify the model and satisfy the eraser theory, making it more expressive and implementable.
- A contract-based approach allows for easier implementation of sophisticated contracts.
- The speaker mentioned that there is still room for improvement and relaxation of restrictions on handlers.
- The use of effect handlers in concurrency and their impact on the model were discussed.
- The speaker highlighted the importance of proving properties using the system practice approach.


## [POPL'24] Algebraic Effects Meet Hoare Logic in Cubical Agda

URL: [https://www.youtube.com/watch?v=seMLbt0Rdx8](https://www.youtube.com/watch?v=seMLbt0Rdx8)


- The speaker discusses formalizing a program language, focusing on syntax and semantics.
- Operational semantics is introduced as one approach to modeling programs, treating them like symbolic Abacus machines or Universal CH machines.
- Formalizing language involves not only formalizing syntax but also the intended derivational meaning.
- The speaker introduces the concept of a first-order language framework, where a user can specify set operations and an operation library provides a general definition model and a free model.
- The speaker demonstrates how to use the framework to model a program and write programs in the language.
- The speaker introduces the concept of whole logic and explains how it can be used for reasoning about programs and proving program correctness.
- The speaker discusses the use of cubical actors and C type function extensionality in formalization.
- The speaker emphasizes that whole logic reasoning can coexist with other reasoning styles, such as computation reasoning, and that they can be beneficial together.
- The speaker thanks the audience for their questions and ends the talk.


## [POPL'24] An Iris Instance for Verifying CompCert C Programs

URL: [https://www.youtube.com/watch?v=xr5ecmtJ25U](https://www.youtube.com/watch?v=xr5ecmtJ25U)


- Separation logic session with William Mansky discussing Iris instance verification
- Comet C program verified using Iris instance
- Key takeaways include:
  - Iris instance language like Rust and Go
  - Connection to existing semantics in WebAssembly
  - Tool chain integration and language work
  - Adding list C in Comet verified C compiler
  - Verifying software tool chain using Iris and VST
  - Focus on proving correctness in the program logic
  - Use of the Floyd tactic library for user-guided proofs
  - Significant reduction in proof size
  - Extending and adding new features to the library
  - Rebuilding VST top Iris for semiautomatic verification system
- Future plans and goals:
  - Release of the VST-based entirely on Iris support
  - Spurring interest in the Iris community and research for C program verification
  - Developing a verified compiler for realistic languages


## [POPL'24] The Logical Essence of Well-Bracketed Control Flow

URL: [https://www.youtube.com/watch?v=00aqaUXNC4w](https://www.youtube.com/watch?v=00aqaUXNC4w)


- The speaker discussed well-bracketed control flow, which ensures that every function call has a corresponding return statement.
- The speaker used an example to demonstrate how concurrent execution can break the property of well-bracketed control flow.
- The speaker introduced the concept of ghost stacks, which are used to reason about the behavior of well-bracketed control flow in a concurrent setting.
- The speaker presented a proof that demonstrates the correctness of the well-bracketed control flow program logic.
- The speaker discussed the potential applications of their work in real-world scenarios, such as supporting unstructured language constructs.
- The speaker responded to questions about the tension between proving well-bracketed control flow and the complexity of reasoning about concurrent programs.
- The speaker expressed interest in exploring further examples, such as a single-threaded scheduler, to verify the correctness of well-bracketed control flow programs.


## [POPL'24] Asynchronous Probabilistic Couplings in Higher-Order Separation Logic

URL: [https://www.youtube.com/watch?v=pWbixzvXcLU](https://www.youtube.com/watch?v=pWbixzvXcLU)


- Simon Gregerson presented on asynchronous probabilistic coupling and higher-order separation logic
- He demonstrated the concept using an example program that flips a coin and returns the result
- The example program is observationally equivalent to another program that uses a different approach to flip the coin
- He discussed how this pattern is seen in various places, such as cryptographic security and hash functions
- The key enabler for this reasoning is the coupling rule in probabilistic program equivalence
- He explained how a synchronous probabilistic coupling rule allows for reasoning about the synchronization of two flip instructions
- The talk focused on developing an expressive programming language using high-order separation logic and a small principle called synchronous probabilistic coupling
- It mentioned the use of a well-typed context-sensitive language called Mik, which supports higher-order functions, recursive functions, and recursive polymorphism
- The presentation emphasized the use of a probabilistic uniform sampling primitive and the reduction of probabilities
- Gregerson introduced a relational probabilistic separation logic called Clutch to prove contextual refinement in probabilistic programs
- He showed how to use a deterministic probability observation predicate to express contextual refinement using a type well-formedness judgment
- The talk also covered the evaluation of an expression in a context using the symbolic execution rule
- Gregerson demonstrated how to use the resource primitives in the relational logic to reason about program behavior
- He provided a detailed definition of the relational logic and used the logical relation to show contextual refinement
- The talk included an example of a lazy coin that refines an eager coin, showing how to inject intermediate program differences and use synchronous coupling to relate the sampling process
- Gregerson discussed the use of pre-sampling tapes in operational logic, which extends the execution state and supports the synchronous PRL-style coupling rule
- He emphasized the importance of using high-order logic to reason about programs in an expressive language
- The talk provided a sketch proof method for asynchronous coupling and highlighted the use of probabilistic coupling to relate tricky examples
- Gregerson mentioned that his work on high-order probabilistic relational separation logic, called Clutch, has been used to verify the security of several cryptographic protocols, including Elgamal encryption and ECP
- He also discussed the potential for using his approach to reason about lazy versus eager evaluation in shuffling programs
- Gregerson acknowledged the need for more work in measuring the performance of his approach with continuous variables and non-Markovian processes.


## [POPL'24] Thunks and Debits in Separation Logic with Time Credits

URL: [https://www.youtube.com/watch?v=FraK4NRL4Io](https://www.youtube.com/watch?v=FraK4NRL4Io)


- Introduced the concept of data structures that use the credit-debit system for time complexity analysis
- Explained the intuition behind credit-debit but pointed out its unsoundness
- Proposed a new perspective, where debt is duplicated to approximate true time complexity
- Formally reasoned about term credit-debit using separation logic
- Presented an overview of the paper, discussing the need for a deep payment rule
- Provided examples and explanations of how to apply term credit-debit in practice
- Introduced the concept of a piggy bank as a building block for reasoning about credit-debit
- Discussed the need for ghost data structures in the separation logic setting
- Mentioned the importance of independent views in debit-based reasoning
- Explained the deep payment rule and its justification using a piggy bank example
- Presented the concept of a stream sequence and how it allows sharing and debit shifting
- Highlighted the need for a conceptual view of shifting debit without runtime cost
- Discussed the use of a banker's queue as an example of a data structure with constant amortized time complexity
- Suggested that the term "ghost piggy bank" could be used to refer to code instrumented with tick instructions for verification purposes
- Acknowledged the need for engineering work to make Iris more user-friendly
- Mentioned that the work on Iris time credit involves a kind of translation between Iris and the logic programming language
- Discussed the open problem of unbounded waiting in a concurrent setting
- Highlighted that the use of THS (Tarjan-Hoare-Strecker) logic in this context allows for multithreaded programs
- Reiterated the importance of synchronizing access in a concurrent setting as a precautionary measure


## [POPL'24] Parikh's Theorem Made Symbolic

URL: [https://www.youtube.com/watch?v=-3RPsLRWPN8](https://www.youtube.com/watch?v=-3RPsLRWPN8)


- The transcript discusses symbolic automata complexity and how it relates to context-free grammar.
- It introduces the concept of a parametric context-free grammar and explains its equivalence to a parametric push system.
- The presentation also demonstrates how to encode paric image small existential formulas using an abstract context-free language.
- The speaker highlights the benefits of using abstract context-free languages, such as faster string constraint solving and the ability to characterize paric image using constraint solvers.
- They also mention the challenges of dealing with a large alphabet and propose using symbolic automata as a solution.
- The speaker provides an example of how symbolic automata can be used to solve string constraint problems and shares their vision for future work in integrating this technique into solvers and applying it to various areas.


## [POPL'24] Efficient Matching of Regular Expressions with Lookaround Assertions

URL: [https://www.youtube.com/watch?v=ZfdAkJNNK_I](https://www.youtube.com/watch?v=ZfdAkJNNK_I)


- The talk presented joint work on regular expressions (regexes) with a focus on lookaround assertions.
- Lookaround assertions are used to extract specific patterns from unstructured data and have various applications, including network intrusion detection and malware detection.
- The main challenge with existing regex engines is that they rely on backtracking, which results in an inefficient algorithm with exponential running time.
- The proposed algorithm, which is based on aom (automata), significantly improves the efficiency of regex matching with lookaround assertions.
- The algorithm performs multiple passes over the input text, evaluating both look behind and look ahead assertions, while storing the output in a tape data structure.
- The talk also discussed the importance of performance optimization and presented an example of an optimized algorithm that performed better than existing regx engines like PCRE and Java's RE2.
- The optimized algorithm had linear running time and was much faster than the base version, especially for larger input texts.


## [POPL'24] The Complex(ity) Landscape of Checking Infinite Descent

URL: [https://www.youtube.com/watch?v=rcV3EgTVtNM](https://www.youtube.com/watch?v=rcV3EgTVtNM)


- The speaker discusses complexity landscape, checking progress proof, and circular proof.
- They mention their work with Leon, Israel, and Andre colleagues.
- They propose two new algorithms for deciding infinite descent property.
- The speaker talks about the infinite descent property, core aspects, and size change approach.
- They introduce the concept of a sloped relation, abstract graph, and the underlying sloped graph.
- The speaker discusses the infinite descent property in terms of graphs and sloped relations.
- They mention the existing algorithm and a new algorithm for checking infinite descent property.
- They compare the performance of different algorithms in a practical setting.
- The speaker acknowledges the complexity landscape and its relation to different algorithms.


## [POPL'24] Positive Almost-Sure Termination – Complexity and Proof Rules

URL: [https://www.youtube.com/watch?v=1GvYDMI9zrY](https://www.youtube.com/watch?v=1GvYDMI9zrY)


- The speaker is discussing positive almost termination and its complexity in a programming language.
- The concept involves a probabilistic nondeterministic choice operator that resolves nondeterminism using a scheduler.
- There are three notions of termination studied: almost sure termination, termination probability, and bounding the deterministic expected runtime.
- The speaker mentions the arithmetical hierarchy and its role in determining the complexity of termination.
- They introduce a canonical complete problem set for the Pi11 class and a recursive well-founded Omega tree.
- The speaker presents a ranking function and its role in certifying termination, as well as its generalization to the probabilistic case called "ranking super Martin Gs".
- They discuss the challenges of applying the ranking function to programs and the need for a sound complete proof rule.
- The speaker highlights the combination of probabilistic and non-deterministic computing as a challenging area of research, where nondeterminism can make problems undecidable.


## [POPL'24] EasyBC: A Cryptography-Specific Language for Security Analysis of Block Ciphers ...

URL: [https://www.youtube.com/watch?v=EsPNHYSY0UM](https://www.youtube.com/watch?v=EsPNHYSY0UM)


- EBC cryptographic specification language security analysis
- Block cipher differential crypto analysis
- P takeaway: Develop a generic automatic approach for evaluating security of block CER using a domain-specific language (DSL)
- Proposed approach: EDBC- a DSL for evaluating security of block CER
- Key features: Generic, automatic, evaluating security
- EDBC based on SSA (Single Static Assignment) approach
- EDBC can automatically analyze block CER's security based on specific operations and generate corresponding C code
- EDBC can handle various cryptographic algorithms, including block ciphers
- EDBC can generate C code, assembly code, or an interpreter for running the program
- EDBC provides security results, different C analysis reports, and evaluates running time
- EDBC can handle both translating and executing code, focusing on analyzing feature-based design
- EDBC can improve resistance against different cryptographic attacks


## [POPL'24] A Core Calculus for Documents: Or, Lambda: The Ultimate Document

URL: [https://www.youtube.com/watch?v=yC4ja0Zines](https://www.youtube.com/watch?v=yC4ja0Zines)


- Presenter's name is Kraton Im Post Brown, Joint work advisor
- Paper discusses the evolution of document languages over time
- Last time someone published anything related to document languages was in 1980
- Brian Reed wrote a paper on a language called Scribe
- The presenter proposes revisiting the concept of document languages and providing a theoretical foundation for reasoning about sophisticated trade-offs in document development
- The presenter introduces the concept of document calculus as an extension of core calculus
- Document calculus provides a formal model for documents, highlighting their structure, reference reforestation, and reactivity
- The presenter suggests that document languages should be designed to respect documents and provide meaningful theories that correspond to human perception
- The presenter discusses the importance of defining semantics for document languages and how it impacts performance, correctness, expressiveness, and ergonomics
- The presenter talks about interoperability and how it affects the exchange of data representation between different languages and frameworks
- The presenter expresses a preference for using a general-purpose language instead of a specialized template notation, suggesting that syntactic sugar should be used to make it easier to write documents


## [POPL'24] Validation of Modern JSON Schema: Formalization and Complexity

URL: [https://www.youtube.com/watch?v=ZLIekqPCy80](https://www.youtube.com/watch?v=ZLIekqPCy80)


- Modern Jason schema formalization: Complexity and validation
- New draft: Notation dependent validation, dynamic reference added
- Dynamic reference: Context dependent, can cause side effects
- Formalization of Modern J schema: Algebra formalization, syntax formalization
- Formalization complexity: Exponential time and space complexity
- P space hard problem: Due to dynamic variable use
- JavaScript scope resolution mechanism: Famous feature of JavaScript
- User level requirement: Composition of GL structures
- Parametric polymorphism: Considered as a potential solution


## [POPL'24] Shoggoth - A Formal Foundation for Strategic Rewriting

URL: [https://www.youtube.com/watch?v=HRFiCObmVeQ](https://www.youtube.com/watch?v=HRFiCObmVeQ)


- Strategic Writing Language: A language designed for strategic rewriting, aiming to perform synthetic transformations without formal understanding
- Overview: The talk covers the strategic writing language, its core language, and its system, adapted from previous work, such as Elevate
- Strategic Language: It includes atomic strategies like single rewrite rules (e.g., addition with commutativity) and composed strategies composed of strategy combinators (e.g., sequential composition, choice)
- Programmer Combinators: Provide control application for rules and allow reuse of strategies
- Application Areas: Program optimization, writing interpreters, compilers, and DSLs
- Challenges: Understanding formal understanding of strategic rewriting language
- Example: Big step operational semantics force system without modeling divergence, and sketching Wiest precondition calculus system for making use of CTL expressive enough for nondeterminism
- Denotational Operational Model: It includes nondeterminism, error, and divergence, especially Angelic and Demonic nondeterminism errors
- Fixed Point Operator: Ensures repeated strategy applications until no further changes occur
- Semantics: Defined using denotational semantics and execution strategies, considering Divergence in sequential composition
- Weakest Precondition Calculus: Introduces the concept of weakest precondition calculus to characterize good and bad strategies, and to model successful and unsuccessful executions
- Successful Execution: If the input expression meets the post-condition, it is considered successful
- Bad Strategy: It never leads to successful execution
- Good Strategy: May lead to unsuccessful execution, but still characterized by the Wiest precondition calculus
- Formal Semantics: Mechanized proof using Isabel Hall for computational soundness and adequacy
- Future Works: Considering reasoning expressing, using rewriting tree, extending the system, and formalizing the pragmatic calculus
- Question: How to apply strategic rewriting language to optimize programs and represent bad strategy examples effectively
- Example: Music inise paper from ICFP 2020, which uses rewrite language to express when a compile optimization is successful
- Extension of System: Like instance strategy, comput value, pass value later, and sequential composition without passing value


## [POPL'24] A Universal, Sound, and Complete Forward Reasoning Technique for Machine-Verifie...

URL: [https://www.youtube.com/watch?v=rOGmRSPHQsU](https://www.youtube.com/watch?v=rOGmRSPHQsU)


- Concurrency is pervasive in computing, and its applicability is widening, making concurrent algorithms and data structures crucial for many applications.
- A concurrency bug in NASA's Mars Rover mission caused three deaths, emphasizing the importance of rigorous machine-verified guarantees for critical concurrent data structures.
- Linearizability is a standard for concurrent object correctness, ensuring that a concurrent system's operation appears to occur atomically in a specific interval of time.
- The talk presented a universal, sound, and complete forward reasoning technique for machine-verified proof of linearizability, which is more intuitive than other existing techniques.
- The technique, called possibility tracking, allows for a simple way to prove concurrent objects.
- Possibility tracking works by maintaining possible atomic reference objects corresponding to possible linearizations of a current run, ensuring that all operations appear to occur atomically in the linearization.
- The paper demonstrates the effectiveness of possibility tracking by providing machine-verified proofs for several concurrent data structures, including the Hurley-Hing Q and a snapshot object.


## [POPL'24] Predictive Monitoring against Pattern Regular Languages

URL: [https://www.youtube.com/watch?v=apf5afr0eEc](https://www.youtube.com/watch?v=apf5afr0eEc)


- Introduces the topic of concurrent code and the problem of detecting and predicting bugs.
- Discusses the use of static and dynamic analysis techniques for bug detection.
- Focuses on Dynamic Analysis and proposes the membership problem, asking whether an execution trace belongs to a set of buggy traces.
- Introduces the idea of predictive monitoring to anticipate buggy executions.
- Presents the challenge of finding an efficient algorithm for predictive monitoring in regular languages.
- Explains the need for a pattern language that captures execution events in a certain order, using the example of a file open/write/close operation.
- Suggests a conditional lower bound for the predictive monitoring problem and proposes a pattern language to solve it efficiently.
- Mentions the need to evaluate the algorithm's scalability and performance in real-world scenarios.
- Highlights the importance of finding practical boxes that can be solved in constant space and linear time, using a streaming algorithm.
- Discusses the possibility of extending the pattern language to handle critical sections and incorporating LTL properties.
- Asks questions about the efficiency of the predictive monitoring algorithm and the importance of good instrumentation tools.
- Ends with a question about how to express the property of an argument.


## [POPL'24] Commutativity Simplifies Proofs of Parameterized Programs

URL: [https://www.youtube.com/watch?v=nHHaMcteNI8](https://www.youtube.com/watch?v=nHHaMcteNI8)


- The speaker introduces the topic of commutativity and its role in simplifying proofs in parameterized programs.
- They explain the concept of contextual commutativity and its implications for verification.
- The speaker discusses the challenges of automated verification and the use of ghost variables to simplify the proof process.
- They introduce the idea of using commutativity to prove the correctness of parameterized programs, using an example to illustrate the concept.
- The speaker explains the advantages of using commutativity in the verification process and highlights the simplicity of the resulting invariants.
- They mention the challenge of representing reductions in a parameterized program and introduce the idea of encoding reductions in parameterized programs.
- The speaker discusses the translation of Fret templates into constrainted Horn Clauses and the use of a CHC solver to prove programs correct.
- They present the results of applying their approach to a benchmark parameterized program and highlight the significant increase in expressivity achieved.
- The speaker concludes by summarizing their contributions and discussing the future direction of their work.
- The speaker answers questions from the audience, covering topics such as commutativity with fixed-size integers, the encoding of reductions, and the effectiveness of their approach for different types of programs.


## [POPL'24] Coarser Equivalences for Causal Concurrency

URL: [https://www.youtube.com/watch?v=mvEfZI7ApNA](https://www.youtube.com/watch?v=mvEfZI7ApNA)


- The speaker discusses equivalence relations and their impact on program runs, focusing on causal concurrency and decision problems.
- They introduce the concept of read equivalence and its definition in a specific alphabet, emphasizing the importance of preserving recent values in equivalent runs.
- The speaker talks about the hardness of studying causal concurrency and decision problems, and introduces the idea of a streaming algorithm for monitoring it.
- They explore the complexity of monitoring a large log system and the importance of constant space algorithms for efficient runtime monitoring.
- The speaker explains the core problem of causal concurrency and the decision problem associated with it, mentioning the need for a solution that can handle scattered grain and constant space algorithms.
- They introduce the concept of grain-based notions and describe how they can be used to build a graph called the grain graph to analyze causal concurrency.
- The speaker highlights the challenge of resolving nondeterminism in a constant space algorithm and the need for a careful implementation of the grain-based approach.
- They mention the potential application of their grain-based Notions to decision problems related to testing and verification, as well as their connection to contextual Petri nets.
- The speaker briefly addresses an intriguing idea about grain closure and the potential connection to future events, mentioning the need for careful management of memory.

Please note that the provided transcript contains a lot of technical and domain-specific terminologies, which may not be fully understood without additional context.


## [POPL'24] On Model-Checking Higher-Order Effectful Programs

URL: [https://www.youtube.com/watch?v=8g2PqP7Q2uo](https://www.youtube.com/watch?v=8g2PqP7Q2uo)


- The talk discusses higher order model checking of effectful programs
- A decidable model checking problem is demonstrated for a specific case scenario involving a higher order model checking problem
- The complexity of the problem is relatively high, with a complexity of K exp time complete
- The talk extends to the realm of pure higher-order programs and their model checking
- A concrete example of a program with two references is presented, along with a description of how exceptions are handled in the program
- The speaker discusses the possibility of verifying the program using higher-order model checking techniques
- The speaker also considers the presence of a global store and how it affects the model checking problem
- The speaker considers a general case involving global states and how they can be modeled using MSO
- The speaker presents an example of a program with global states and how it can be verified using MSO
- The talk also addresses the case of probabilistic effects and how they can be modeled using MSO
- The speaker discusses the challenges of model checking programs with endlers and how they can be verified using MSO
- The speaker considers the case of preinterpreted effects and how they affect the model checking problem
- The speaker presents an example of a program with endlers and how it can be verified using MSO
- The speaker discusses the possibility of using a restricted notion of the handler call to make the model checking problem decidable
- The speaker mentions the need for first-order path quantification to model certain problems
- The speaker briefly touches on the concept of runners in the context of higher-order model checking
- The speaker asks a question about the difference between generic effect handlers and runners, and how they impact expressivity
- The speaker acknowledges that the talk may not cover all possible cases and encourages further exploration and research in the field

Note: The provided transcript has many technical terms and concepts, so this summary only captures the overall structure and topics discussed in the talk.


## [POPL'24] Explicit Effects and Effect Constraints in ReML

URL: [https://www.youtube.com/watch?v=447M7267JQE](https://www.youtube.com/watch?v=447M7267JQE)


- Explicit effect constraint
- Reasoning in high-order effect programs
- Efficient memory management and multi-threading in ML functional languages, including OCaml and Milton
- Work looking at world without reference tracing garbage collectors, instead relying on safe allocation and deallocation based on static analysis
- Region-based memory management: explicit versions allow programmers to explicitly manage memory
- Non-annotated programs and inference algorithms insert allocation and deallocation primitives at compile time
- Stack-based region organization, with stack growth determined by the first region allocated
- Segmented region-page allocation and deallocation using free lists
- Proposal of the language RML that allows combining efficient memory management, multi-threading, and ML functional languages
- Gradual information provision to programmers, making sure small changes to the program source code still provide results from previous runs
- RML program annotations expressing region instances and expressions specifying values
- Data type scoping and region programs, usually called lead region
- Possibility of annotating functions with their type schemes and function types
- Backward compatibility using constraints and effect reasoning
- Region inference and analysis for input analysis and annotation of intermediate representations
- Allowing region parameters in functions and handling the allocation of new regions
- Explicit region support in RML, with annotations and local regions
- Example of a polymorphic function taking a region parameter and specifying a type for that parameter
- Gradually typed sense, where programmers can add annotations to get desired behavior
- Copying and endomorphic functions that specify regions for their arguments and results
- Parallelism support and merging region-entered polymorphic recursion
- Proof of type effect system constraint soundness based on assertion feature language guarded by constraints and effect annotations
- The status of region runtime erasure, adding reference tracing garbage collectors, and the bootstrapping of ANL kit
- The use of region influence in list-type control and the potential for optimization by joining regions for cheaper allocation


## [POPL'24] Decalf: A Directed, Effectful Cost-Aware Logical Framework

URL: [https://www.youtube.com/watch?v=JQNL0NQbaiE](https://www.youtube.com/watch?v=JQNL0NQbaiE)


- Presented an overview of the full story, discussing motivation, core language components, and program inequality.
- Highlighted the importance of understanding cost behavior and utilizing cost models.
- Explained the use of computation types and effect types in analyzing program cost.
- Discussed the Calf notation and its role in cost analysis.
- Described the importance of understanding equality and inequality in reasoning about program cost.
- Introduced the concept of exact cost bounds and their use in verifying cost behavior.
- Presented an example of merge sort and how it can be analyzed using cost models and inequality reasoning.
- Explained the extension of the Calf framework to handle probabilistic effects and randomized algorithms.
- Gave an example of a randomized parallel quick sort algorithm.
- Explained the use of the Eliminator and its role in the top semantics of the Calf framework.
- Discussed the limitations of the Eliminator and the challenges of working with higher-order programs.
- Introduced the concept of topological semantics based on directed type theory and synthetic domain theory.
- Provided an overview of the practical example of embedding the Calf framework in Agda.
- Highlighted the importance of cost analysis and its role in analyzing algorithm behavior.
- Discussed future work and potential improvements to the Calf framework, including support for data abstraction, separate cost proofs, and a deeper understanding of effect analysis.


## [POPL'24] Modular Denotational Semantics for Effects with Guarded Interaction Trees

URL: [https://www.youtube.com/watch?v=3F0VsFR0wxM](https://www.youtube.com/watch?v=3F0VsFR0wxM)


- The talk discusses modular denotational semantics with guarded interaction tree.
- The goal is to represent different effects separately and combine them.
- The framework G interaction tree is introduced and formalized.
- Several case studies are applied to demonstrate the framework.
- The talk also covers high-order computation and effect.
- Guarded interaction tree is mentioned as a way to model high-order computation.
- The talk emphasizes the importance of interpreting effects and using separation logic.
- The Aris system is used to derive different domain-specific logics and effect-specific rules.
- The case study of cross-language interaction is presented to showcase modularity.
- The talk highlights the importance of extracting an executable program from the interaction tree.
- The speaker addresses a question about extracting higher-order constructors and the need for representing higher-order computation.
- The speaker answers a question about relaxing restrictions and the possibility of introducing change logic for reasoning.
- The speaker discusses domain interpretation and adding an error domain for fixed example settings.


## [POPL'24] Semantic Code Refactoring for Abstract Data Types

URL: [https://www.youtube.com/watch?v=OMvGITAUQOs](https://www.youtube.com/watch?v=OMvGITAUQOs)


- Abstract Data Type (ADT) refactoring is a challenge due to the semantics underlying data representation.
- Refactoring involves changing the data representation of an ADT implementation, which can require significant modifications to the codebase.
- The main challenge is ensuring that the semantics of the original method implementation are preserved in the new implementation.
- Manual refactoring can introduce new bugs, making it essential to automate the process.
- Revamp, a tool developed for this purpose, uses a three-step approach:
  1. Reducing the synthesis problem instance to PBE (Pretty Big Example).
  2. Leveraging symbolic reasoning to infer useful code snippets.
  3. Accelerating the search through partial equivalence and component-based synthesis.
- Revamp was evaluated using real-world refactoring tasks and demonstrated effectiveness.
- The key takeaway is that Revamp can automatically refactor ADT implementations, preserving the observational equivalence of the original method.
- The speaker emphasized the importance of providing precise rri (relational representation invariant) specifications to avoid potential errors during refactoring.


## [POPL'24] API-driven Program Synthesis for Testing Static Typing Implementations

URL: [https://www.youtube.com/watch?v=lZws2_bhL58](https://www.youtube.com/watch?v=lZws2_bhL58)


- Thoris presented work on API-driven program synthesis for stress testing type systems.
- He mentioned the importance of type checker components in compilers and shared motivating examples in Scala and Groovy.
- The approach involves leveraging existing APIs to generate small client programs for stress testing type system implementations.
- Thalia, a system for synthesizing test cases, was introduced, which utilizes an API graph to generate typing sequences and expressions.
- The presentation demonstrated the efficiency of Thalia in synthesizing compact test cases and stress testing type systems.
- The talk also compared Thalia with other testing frameworks, highlighting its advantages in terms of synthesis compilation time and code coverage.
- Questions from the audience included inquiries about hole filling examples, the potential for Thalia to find bugs in simple programs, and the ability to generate test cases for specific features.


## [POPL'24] Programmatic Strategy Synthesis: Resolving Nondeterminism in Probabilistic Progr...

URL: [https://www.youtube.com/watch?v=Jh0YZDHAbOw](https://www.youtube.com/watch?v=Jh0YZDHAbOw)


- Programmatic strategy synthesis for resolving nondeterminism in probabilistic programs
- Goal is to maximize the probability of winning in a Gamble game
- Uses a simple game as an example
- Encodes the objective using post-conditions and a predicate system
- Uses weakest precondition to encode the strategy and find the optimal solution
- Weakest precondition maps from initial states to the truth value of the post-condition
- Probabilistic weakest precondition is a generalized version for probabilistic programs
- Extended probabilistic programs handle nondeterministic choices
- The approach involves a semi-automatic technique, with user-provided invariants and classical program verification
- The technique helps in computing the strategy and ensures termination
- Future work includes considering stochastic two-player games and Markov decision process theory
- A question about keeping local variables and if the approach still works in case of programs with a positive probability of termination is raised


## [POPL'24] A Case for Synthesis of Recursive Quantum Unitary Programs

URL: [https://www.youtube.com/watch?v=Hc6e8DP-xb4](https://www.youtube.com/watch?v=Hc6e8DP-xb4)


- The talk focuses on the synthesis of recursive Quantum unitary programs.
- Existing circuit synthesis techniques can help generate sequences of quantum operations but face challenges with loop recursive structures and fixed-size circuits.
- The goal is to develop a program synthesis framework that supports loop recursive structures and enables large-scale quantum program synthesis.
- Three main challenges are identified: designing a new representation specification for quantum programs, creating a new program language that includes loop recursive structures, and developing a new verification mechanism for quantum programs.
- Qims, a corner unit reprogram synthesis framework, is introduced, which includes recursion structure support.
- The framework consists of three main parts: specification, candidate program generation, and verification.
- Qims uses a trival searcher to generate candidate programs based on syntax iteration.
- Qims verifier is designed to automatically verify quantum progress and includes two parts: a new language called induced Squares and an encoding part to encode the verification process.
- The framework employs a new input-output style specification, new language called square, and a new representation called permiss size pas amplitude form.
- Qims supports automatic verification using the SMP Music solver.
- The speaker provides an evaluation of the framework through six additional case studies.
- The synthesis time of Qims is compared with QAST Qsync, and the results show that QAST Qsync stops synthesis after running time exceeds 1 hour, while Qims successfully generates synthesis programs in constant time.


## [POPL'24] Quotient Haskell: Lightweight Quotient Types for All

URL: [https://www.youtube.com/watch?v=ox9nIF2jt8M](https://www.youtube.com/watch?v=ox9nIF2jt8M)


- Quotient type in Liquid Haskell
- Extends refinement type system
- Provides support for quotient type
- Lightweight meaning that manual proof obligations are automatically verified
- Introduces quotient type to extend the existing type system
- Example: Natural numbers defined using quotient type
- Motivation for quotient type:
  - Adds expressivity to the type system
  - Allows for a wider range of properties to be checked statically
- Duality of quotient type and subtypes
- Discussion of quotient type implementation
- Quotient equality back refinement logic
- Subtyping rule for quotient type
- Introduces a new subtyping rule for quotient type
- Example: Mobile type extended with quotient type
- Quotient type respects functions
- Summation function respecting swap equality constructor
- Liquid Haskell automatically verifies the function
- Introduction of quotient equality back refinement logic
- Example: Map function respecting swap equality constructor
- Quotient type in Lambda Haskell
- Future work:
  - Support for quotient gadts
  - Improved reasoning for quotient type
  - Specification type class for quotient type
  - Manual proof obligation feature
  - Improved error reporting


## [POPL'24] Focusing on Refinement Typing (TOPLAS)

URL: [https://www.youtube.com/watch?v=dKd-7hQwbkY](https://www.youtube.com/watch?v=dKd-7hQwbkY)


- Discussed dependent type refinement in ML style
- Refining types for specialized data structures, such as Nat list
- Proposed using measure to refine types for natural numbers
- Provided examples of refinement types and measure refinements
- Highlighted challenges in implementing fancy types and ensuring soundness
- Mentioned the use of liquid type, which uses measures to refine types
- Discussed the need for an algorithmic system to infer and solve indices
- Described the importance of value determinism in the liquid typing algorithm
- Discussed the role of proof theory in the liquid typing system
- Outlined the process of proving typing soundness in the system
- Mentioned the use of term progress preservation and Lima's key step
- Concluded by mentioning the importance of proving total correctness and pattern cover


## [POPL'24] Polymorphic Reachability Types: Tracking Freshness, Aliasing, and Separation in ...

URL: [https://www.youtube.com/watch?v=cMBuYviwtIE](https://www.youtube.com/watch?v=cMBuYviwtIE)


- Guan presents work on a polymorphic reachability type system
- Focuses on memory safety and performance, with examples from Rust and Scala
- Proposes a new notion of freshness to handle sharing in higher-order languages
- Freshness is a qualifier that tracks sharing and separation, preventing interference
- The system allows for precise tracking of resource usage without explicit quantification
- The Diamond Language prototype implements this system and is being developed further
- Freshness notion can be used to reason about concurrency and non-interference in a practical way
- Current work involves syntactic mechanization using logical relation formalization

In summary, the speaker discussed the importance of memory safety and performance in programming languages, presenting a novel approach to handle sharing in higher-order languages using a polymorphic reachability type system with the notion of freshness. This system allows for precise tracking of resource usage and can be used to reason about concurrency and non-interference. The work is being further developed with a prototype implementation called The Diamond Language.


## [POPL'24] Capturing Types (TOPLAS)

URL: [https://www.youtube.com/watch?v=EBS8wiH4khU](https://www.youtube.com/watch?v=EBS8wiH4khU)


- Introduces the concept of capturing types in relation to object capabilities and effectful operations
- Suggests that the use of capturing types can make it easier for developers to adopt these approaches in their code
- Compares the use of capturing types to the classical effect system, showing how it can provide a more concise and precise way of expressing effects
- Describes how capturing types can help control and mediate effects in code, providing an alternative way of structuring object-oriented code
- Introduces the concept of subcapturing, which integrates capability derivation and subtyping in a capturing type
- Discusses the potential implementation challenges of capturing calculus, particularly in relation to variable-dependent types and subtyping relations
- Highlights the use of lightweight annotations to migrate parts of the Scala collection library to a capturing type-based approach
- Explains the need for explicit type annotations to restrict capabilities and ensure safety in the code


## [POPL'24] Probabilistic programming interfaces for random graphs: Markov categories, graph...

URL: [https://www.youtube.com/watch?v=GdxIDp_-84E](https://www.youtube.com/watch?v=GdxIDp_-84E)


- The talk focuses on the connection between probabilistic programming and statistical modeling using random graphs.
- The speaker discusses three methods of using Markov categories for graph modeling.
- The main theorem states that given data and a well-behaved implementation of a graph, it is equivalent to a particular implementation.
- The speaker introduces the concept of a probabilistic programming language called Lazy Probabilistic Programming.
- They discuss an example of implementing a random graph on a sphere.
- The talk also covers the concept of a probabilistic interface, which can be applied to other statistical problems, such as linear regression.
- The speaker highlights the importance of understanding the structure of probabilistic programming and how it corresponds to important statistical structures.
- The talk also touches on the concept of graphons and their connection to combinatorics and graph theory.
- The speaker mentions that they are developing a library called Lazy People for probabilistic programming.
- The talk concludes with a question-and-answer session.


## [POPL'24] Inference of Probabilistic Programs with Moment-Matching Gaussian Mixtures

URL: [https://www.youtube.com/watch?v=suSV6_NQvXQ](https://www.youtube.com/watch?v=suSV6_NQvXQ)


- Presented work on approximating output distributions using Gaussian mixture distributions.
- Introduced a method based on moment matching for approximating the output distribution of a probabilistic program.
- Developed a second-order Gaussian semantics (SOA) tool that provides an efficient and accurate method for computing moments of the output distribution.
- Compared the performance of SOA with other methods such as Monte Carlo Markov Chain sampling, Stan, Pyro, and Aqua.
- Demonstrated the applicability of the method in scaling efficiently with the number of variables in a model.
- Mentioned plans to improve the stability and extend the syntax of the tool and aim to integrate the method with existing probabilistic programming languages like Spyro.


## [POPL'24] Higher Order Bayesian Networks, Exactly

URL: [https://www.youtube.com/watch?v=ESfLesM315A](https://www.youtube.com/watch?v=ESfLesM315A)


- Introduced simple graphical model: Ban Network
- Exemplified with a Boolean random variable (rain) and its associated conditional probability table
- Described a more complex model using a directed acyclic graph (DAG)
- Discussed the limitations of standard Bayesian networks and their expressiveness
- Introduced a higher-order probabilistic programming language (Ban) for encoding complex Bayesian models
- Elaborated on the first-order Bayesian network encoding and the rewriting process to obtain a standard Bayesian network
- Emphasized the role of type systems in providing notational semantics for Ban programming language
- Mentioned the use of a data flow analysis approach to extract the graph structure and compute the type derivation
- Explained the use of cost-aware denotational semantics, including cost inference and type derivation computation
- Discussed the importance of representing probability distributions and inference algorithms in the Ban programming language
- Highlighted the need for a sound and complete higher-order probabilistic programming language with efficient computation
- Discussed the complexity of inference based on the result DAGum-Luby and the need for efficient approximation algorithms
- Concluded with a discussion on variable elimination and its impact on cost awareness


## [POPL'24] Strong Invariants Are Hard: On the Hardness of Strongest Polynomial Invariants f...

URL: [https://www.youtube.com/watch?v=XkuegDpPn4A](https://www.youtube.com/watch?v=XkuegDpPn4A)


- Polynomial invariance and classical program
- Probabilistic program and loop invariant
- Polynomial question: finding an invariant automatically
- Computing the basis for the strongest polynomial invariant
- Deterministic unguarded Loops
- Nondeterminism and the T-complete problem
- Polynomial assignment and loop body
- Discrete time and polinomial dynamical systems
- Classical program and the computation of the strongest polynomial invariant
- Undecidability proof for the reachability problem
- Scolum problem and reachability invariance
- Linear recurrent sequence and the scolum problem
- The status of the scolum problem as unknown
- Polynomial loop invariant and the reachability problem
- Probabilistic session and focusing on the moment invariant
- Polynomial invariance among the moments
- Infinite set of moments and ideal
- Generalization of the classical invariant
- Moment invariant ideal and the tool algorithm
- Polar computing the moment invariant ideal
- Classical program and the necessity of the invariant
- Moment invariant ideal and the automation of program verification
- Probabilistic program and the sequence of increasingly high order moments
- The case of probability distribution and the determined full set of moments
- Moment invariance ideal and the undecidable problem
- Computing the moment variant ideal
- Undesirability proof and the replacement of nondeterministic prolistic choice
- Discussion paper and the open problem
- Acknowledgment of the speaker.


## [POPL'24] With a Few Square Roots, Quantum Computing is as Easy as Pi

URL: [https://www.youtube.com/watch?v=OQRxlqrZC5g](https://www.youtube.com/watch?v=OQRxlqrZC5g)


- Robin Hell talks about square root Quantum Computing and its relation to reversible classical Computing.
- He discusses the idea of quantum computation as a complete system with a mathematically classical component, drawing parallels to complex number algebraic closure.
- Robin explains the concept of unitary matrices and their relation to classical and quantum computation.
- He introduces the programming language Pi, designed for reversible classical Computing, and discusses its extension to represent quantum permutation.
- Robin describes a model, called screw P, that can represent both classical and quantum computing circuits and provides a sound complete equational theory.
- He discusses the challenges of formalizing and proving the completeness of the equational theory for quantum circuit models, especially for Clifford plus T circuits.
- The speaker acknowledges the limitations of the current understanding and invites further research on the topic.


## [POPL'24] Quantum Bisimilarity via Barbs and Contexts: Curbing the Power of Non-Determinis...

URL: [https://www.youtube.com/watch?v=-xLEnLZ5GHI](https://www.youtube.com/watch?v=-xLEnLZ5GHI)


- The speaker discusses Quantum similarity via Barb context curbing.
- They focus on communicating systems protocols via process algebra and a similarity relation.
- Existing proposals use syntax calculus and the Cas discat notation, but the speaker proposes an alternative approach.
- The speaker's approach uses finite support probability distributions and a bar notation for point distributions.
- They work in finite-dimensional space and adopt direct notation for column vector products.
- The speaker highlights two important properties of quantum states: superposition and entanglement.
- They use a density operator as a generalization of quantum states, representing probability distributions instead of simple quantum states.
- The speaker defines the Linear Quantum CCS (LCCS) and its two-operator structure for value passing and communication.
- They evaluate process configurations using a label transition system and the probabilistic outcome of a measurement.
- The speaker introduces the concept of behavioral equivalence and explains how it applies to the evaluation of processes.
- They propose a context-based approach to build exact context relations and address the issue of non-determinism.
- The speaker presents an extended configuration semantics for non-choice examples and the use of an arrow index to represent location.
- They define a refinement relation and demonstrate how it can be used to constrain non-deterministic choices.
- The speaker discusses the need to quantify over all possible quantum states and the challenge of verifying such similarity.
- They mention the potential for extending syntax examples, such as recursive processes or pending issues.
- The speaker acknowledges the limitations of the previous proposal and the need for additional research to investigate inconsistencies.


## [POPL'24] SimuQ: A Framework for Programming Quantum Hamiltonian Simulation with Analog Co...

URL: [https://www.youtube.com/watch?v=X2cDCqUfWg0](https://www.youtube.com/watch?v=X2cDCqUfWg0)


- Introduction of SimQ framework for programming quantum Hamiltonian simulation and analog compilation
- Overview of quantum Hamiltonian simulation and the challenges it presents for classical computers
- Emphasis on the need for software tools to aid in computing tasks related to quantum systems
- SQ framework's anal compilation scheme and its potential application in quantum computing research
- Discussion on the importance of programming languages in the development of quantum computing tools
- Explanation of the Forun language and its influence on the development of abstraction models in programming languages
- Proposal of the SQ framework as a direct abstraction for quantum computing, leveraging existing analog quantum simulators
- Introduction to the AIS instruction, which represents a partial analog quantum device
- Presentation of the Simi Cube framework and its competencies
- Overview of the Simi Cube compiler design and its ability to generate executable policies for analog quantum simulators
- Mention of the interdisciplinary collaboration between researchers and the expansion of SQ's functionality
- Demonstration of SQ's practical application in real quantum devices
- Discussion on the future direction of quantum computing programming languages and the potential for low-level pulse compilation techniques
- Comparison of the abstraction levels used in SQ and other quantum computing devices
- Emphasis on the importance of APIs and control development in quantum computing
- Discussion on the challenges of developing a high-level quantum programming language and compiling it to a lower level language
- Mention of the integration of Dynamical Decoupling Technology and the addition of support for DW-recat devices
- Conclusion with a recap of the talk's key points and a focus on the practical application of SQ in real quantum devices
- Question and answer session at the end of the talk


## [POPL'24] Enriched Presheaf Model of Quantum FPC

URL: [https://www.youtube.com/watch?v=C-BpyfyWLl0](https://www.youtube.com/watch?v=C-BpyfyWLl0)


- Introduction to the Denotational Model and High-Order Quantum Programming Language
- Overview of the Quantum FPC (Fully Polynomial Time Computable) model
- Challenge: dealing with entanglement in quantum systems
- Primary Goal: developing an enriched pre-shift model for quantum systems
- Key Concepts: module operator, enriched presheaf, and fully abstract model
- Technical Development: referring to the paper "Quantum FPC Extension"
- Probabilistic Mixture: using subn and Psubn to represent mixture of pure states
- Superoperator: linear function that preserves positive semi-definite matrices and trace
- CER 2004 and Deal LDA: remarkable results in developing quantum languages
- Quantum Programming Language LLY: obtaining the Q model by ignoring probabilistic features
- Two Issues in Q Model: interpretation function type and natural course function type
- Singer's Proposal: extending the Q model by adding space Norms
- Proposal for Probabilistic Coherent Space: a promising approach to treating entanglement
- Entanglement: a crucial concept in Quantum Information Theory
- State Entanglement: state composed of two quantum systems cannot be expressed as a mixture of pure states
- Primary Goal of the Project: fixing the problem using the notion of enriched pre-shift
- Enrichment Development: motivated by the connection between linear algebra and linear logic
- Cap Model: a unified framework capturing the difference between models
- Semi Ring and Sigma Semi Ring: generalization of the modu theory
- Q Module Model: interpret arbitrary leip type Omega CPO as an enriched pre-shift structure
- Obstruction Result: applying the Q module model to obtain full obstruction
- Q Prime Model: fully faithful strong monomorphism

(an empty string)

- Quantum Inductive Type: using V algebra to relate to previous work on Quantum Inductive Type
- Quantum Inductive Type and V Algebra: understanding the connection between the two
- Connection between Quant and Category: currently unsure about the relationship

(an empty string)

- The speaker thanks the audience for their attention and applauds the great session.


## [POPL'24] How Hard is Weak-Memory Testing?

URL: [https://www.youtube.com/watch?v=nj6V5mMHGBw](https://www.youtube.com/watch?v=nj6V5mMHGBw)


- Introduction to weak memory testing
- Hard weak memory testing: motivation and examples
- Formal specification and memory models
- Testing and verification models
- Limits of testing and hardness results in weak memory models
- Challenges and future research directions
- Complexity of testing in weak memory models and potential parameterizations
- Scaling up testing with a large number of threads and memory locations
- Separating models and the impact of partial RF Co change
- Read testing and the complexity landscape
- Possible bounding of input size in testing

Note: The summary provided above is based on the content of the transcript and does not include any additional context or information.


## [POPL'24] An Axiomatic Basis for Computer Programming on the Relaxed Arm-A Architecture: T...

URL: [https://www.youtube.com/watch?v=c_Te-E79teY](https://www.youtube.com/watch?v=c_Te-E79teY)


- Relaxed R architecture and modern programming languages exhibit weak behavior.
- The focus is on relaxed user mode setting in ARM architecture.
- Challenges in reasoning about whole programs in a relaxed setting.
- The need for a compositional reasoning tool to reason about large programs in the ARM model.
- The importance of bit-level reasoning in the ARM model.
- The Global consistency check is a challenging issue.
- The use of Iris operational semantics model for the ARM architecture.
- The need to develop a new AR assertion to support the ARM memory event graph.
- The introduction of a new AR assertion to support register point2 and TI assertions.
- The use of Iris logic to support the ARM memory event graph.
- The need for a protocol to support resource transfer using invariance.
- The development of a protocol to hide invariance closures and reliance on VAR annotations.
- The similarities between Iris and the proposed approach for handling memory settings in the ARM model.
- The importance of considering infinite execution settings.
- The use of incremental guessing and graph building approaches in the OPAC semantics model.
- The need to develop a protocol that guarantees resource transfer using invariance.


## [POPL'24] Trillium: Higher-Order Concurrent and Distributed Separation Logic for Intension...

URL: [https://www.youtube.com/watch?v=eYgDMkHwfco](https://www.youtube.com/watch?v=eYgDMkHwfco)


- The speaker introduces a simple example to illustrate the concept of termination in concurrent programs.
- They discuss the idea of fairness in scheduling threads and its impact on program termination.
- The speaker proposes a new logic called Trum, which is designed to build refinement programs and prove termination in concurrent systems.
- Trum aims to provide a formal way of setting arguments and proving program behavior.
- They explain the use of the Trillium proof method and how it helps to prove termination in concurrent programs.
- The speaker highlights the importance of refinement models and their role in proving program correctness.
- They discuss the limitations of existing logics and the need for a new approach to handle safety properties and infinite traces.
- The speaker mentions the possibility of using Trillium to prove termination in concurrent programs and addresses the limitations of existing methods.


## [POPL'24] Deadlock-Free Separation Logic: Linearity Yields Progress for Dependent Higher-O...

URL: [https://www.youtube.com/watch?v=Tt28Z-3OM7A](https://www.youtube.com/watch?v=Tt28Z-3OM7A)


- The main goal is to make separation Logic message passing more free and easier to prove
- Iris is an existing separation Logic message passing system
- The talk discusses combining two linear session types to create a more powerful system
- The key difference between separation logic and traditional ownership-based type systems is that separation logic deals with separate resources and ownership assertions
- Adequacy theorems are used to prove the correctness of programs in separation logic
- The talk mentions challenges in verifying deadlock-free programs and proposes a solution for handling them
- The talk also discusses future work and the potential for automating proofs using a diaphragm-like approach
- The speaker is asked about the possibility of using a probabilistic programming system and responds positively
- The speaker is asked about the feasibility of using cancelable invariance in a linear course, and they suggest it could work
- The speaker is asked about the possibility of allowing users to write programs and evaluate the second aspect, and they express uncertainty about what kind of program people want to write


## [POPL'24] Polyregular functions on unordered trees of bounded height

URL: [https://www.youtube.com/watch?v=w5aaxBgabHY](https://www.youtube.com/watch?v=w5aaxBgabHY)


- The speaker discusses decidability problems for two functions, specifically focusing on determining if two functions are equal.
- The speaker provides examples and context, mentioning decidability in theoretical computer science and the undecidability of some problems.
- The speaker presents a nontrivial example of deciding two regular languages and discusses the building of products and checking appropriate properties.
- The speaker introduces the concept of a function with a graph output and its relation to graph isomorphism problems.
- The speaker highlights the importance of tree structures and their representation in decidability problems.
- The speaker introduces the concept of first-order interpretations and explains how they can be used in decidability problems.
- The speaker presents a theorem and discusses the decidability of equivalence for functions that transform graphs with bounded tree depth.
- The speaker mentions that the decidability of equivalence for string-based functions can be considered a special case of the tree-based problem.
- The speaker acknowledges the limitations of the decidability problem and the challenges it poses when dealing with tree structures.
- The speaker discusses the potential use of the decidability problem in the field of graph theory and the development of algorithms for checking equivalence.


## [POPL'24] Solving Infinite-State Games via Acceleration

URL: [https://www.youtube.com/watch?v=3G0WaerPZpQ](https://www.youtube.com/watch?v=3G0WaerPZpQ)


- Introduction to infinite State game solving via acceleration
- Overview of the problem: Synthesis of systems with specification systems
- Two main directions: Program synthesis and finite state reactive synthesis
- Approach: Two-player game played between system and environment
- Existing methods: Method-based abstraction and classical algorithm examples
- Acceleration method: Loop game and iterative decrement of variables
- LMA (Loop-Making-Acceleration): Uninterpreted Lamas and non-terminating attractor computation
- Evaluation: Comparison with existing methods and benchmarking with infinite State Games
- Tool: Use of SMT solvers and constraints for encoding and solving problems


## [POPL'24] Ramsey Quantifiers in Linear Arithmetics

URL: [https://www.youtube.com/watch?v=tdbKUovVMlY](https://www.youtube.com/watch?v=tdbKUovVMlY)


- Three-variable program example given
- Termination of the program discussed
- Reality relation and its expression in real-integer linear arithmetic formula
- Remsey quantifier introduced and its role in the problem-solving process
- Non-terminating program example provided
- Use of the SMT (Satisfiability Modulo Theories) server to check satisfiability of the formula
- Main result: eliminating Ramsey quantifier by constructing a polinomial time formula of linear size
- Example of a system with linear liveness and reachability relation
- Application of the theory to continuous V reversal bonded counter machine par automaton, Su one counter automaton
- Discussion of integer linear loops and linear arithmetic
- Use of matrix to represent linear transformation
- Acknowledgement of the limitations of the theory


## [POPL'24] Reachability in Continuous Pushdown VASS

URL: [https://www.youtube.com/watch?v=z9Bp17F5ovQ](https://www.youtube.com/watch?v=z9Bp17F5ovQ)


- Ramanam presented a problem related to reachability in continuous pushdown systems
- The presentation focused on modeling regular threads with asynchronous calls
- He discussed the concept of a vector addition system with states represented by a finite set of counters
- The reachability problem was defined in the context of a central model of computation
- The speaker discussed the notion of coverability and its relationship to reachability
- He presented an example to illustrate the concepts and mentioned that the reachability problem for vector addition systems with states is a complete problem
- He briefly mentioned the decidability of the reachability problem for one counter, one stack theory, and the community's interest in studying it
- Ramanam discussed the concept of continuous approximation, introduced by David Allah in 1987
- He mentioned that Petri Nets reachability is shown to be P-complete
- The speaker presented a lower bound for the reachability problem in continuous pushdown systems, which is non-deterministic exponential time complete
- He also mentioned the possibility of studying a restricted model of continuous approximation and hoped to achieve better complexity, like in P-space NP
- Ramanam briefly touched upon the relation between asynchronous programs and continuous pushdown systems, mentioning that there is no direct mapping except for the approximation aspect
- He shared his interest in the bounded counter detection problem, which is a known problem with a bound and the continuous aspect
- The speaker mentioned that the reachability problem in a branching push Vector Edition system would be an interesting point for further research
- Ramanam also touched upon the concept of Zeno runs and their relationship with complexity
- He briefly mentioned the work of Blonda and Hassa, who studied the case without a stack and provided a characterization of runs in their model
- Ramanam concluded by expressing his interest in studying the upper bound of the problem.


## [POPL'24] Pipelines and Beyond: Graph Types for ADTs with Futures

URL: [https://www.youtube.com/watch?v=YqCyyaBiwqg](https://www.youtube.com/watch?v=YqCyyaBiwqg)


- The transcript is about graph type, a representation of the dependency graph of a program.
- Graph type system can be used for static analysis and scheduling.
- The graph type system can be used for visualizing programs, allowing programmers to analyze parallelism.
- The transcript introduces a new work called Lambda G mu, a parallel calculus that introduces second iteration graph type system with a new vertex structure.
- Lambda G mu has a prototype implementation and a verification algorithm that can prove every data structure represented by a corresponding vertex structure.
- The graph type system can be used for type checking and program visualization.
- The future work mentioned in the transcript is related to theorizing possible applications of the graph type system.


## [POPL'24] Disentanglement with Futures, State, and Interaction

URL: [https://www.youtube.com/watch?v=m8-EnnteBg8](https://www.youtube.com/watch?v=m8-EnnteBg8)


- Disentanglement property allows efficient management of memory in parallel functional programs
- Disentanglement ensures program disentanglement holds even when limited to purely functional programs and when considering determinacy race
- Disentanglement property holds true for programs with Fork-Join parallelism and IO effects
- Disentanglement can help prove a program's deadlock freedom using calculus and intermediate language
- Disentanglement ensures a program remains free from determinacy race even when participating in determinacy race with Futures
- Disentanglement property helps prevent the creation of deadlock conditions in programs with Futures and mutable state
- Disentanglement system provides synchronization primitives, including barriers and locks, to ensure race-free and deadlock-free execution


## [POPL'24] DisLog: A Separation Logic for Disentanglement

URL: [https://www.youtube.com/watch?v=PhIHAlgHd7g](https://www.youtube.com/watch?v=PhIHAlgHd7g)


- Presenter: Alexandra Mo
- Topic: Dislog Separation Logic - Disentanglement
- Disentanglement property generally occurs in pure programs, exchange allocation, and Race-Free programs.
- Disentanglement guarantees locality, which makes memory management tasks faster and easier to synchronize.
- The MPL compiler, developed by CMU, heavily uses disentanglement for fast memory management.
- DisLodge Separation Logic is proposed to ensure program disentanglement.
- DisLodge Separation Logic uses time stamping to guarantee unique access to resources, preventing entanglement.
- DisLodge Plus Separation Logic extends DisLodge Separation Logic with standard separation logic to handle race-free programs without invariance.
- DisLodge Plus Separation Logic provides a mechanism to verify race-free programs and offers an extension, Bing Disentanglement, for race-read right.
- The speaker presented a roadmap for future work, which includes devising a type system and proving sound semantic typing for DisLodge.


## [POPL'24] Automatic Parallelism Management

URL: [https://www.youtube.com/watch?v=G87sgOdDLTw](https://www.youtube.com/watch?v=G87sgOdDLTw)


- The speaker is Sam Westrick, presenting on automatic parallelism management.
- The concept focuses on fine-grained task parallelism, specifically Fork-Join parallelism.
- The speaker addresses the challenge of granularity control in parallelism.
- The speaker explains the need for a general solution that guarantees efficiency and can be implemented effectively.
- The speaker introduces the concept of PE call, a nearly zero-cost calling convention for parallelism.
- PE call uses two additional return addresses to achieve sequential execution or expose parallelism.
- The speaker discusses the promotion of parallelism and its associated cost, and how it is amortized in the heartbeat scheduling algorithm.
- The speaker highlights the work efficiency and span efficiency properties of the proposed technique.
- The speaker mentions the implementation of the automatic parallelism management technique in the Maple compiler.
- The speaker emphasizes the importance of collaboration between the middle end and runtime systems in achieving effective parallelism.


## [POPL'24] SIGPLAN Awards, PC Chair's Report, and Business Meeting

URL: [https://www.youtube.com/watch?v=up7OJgLL5uo](https://www.youtube.com/watch?v=up7OJgLL5uo)


- Industrial sponsorship of 80K
- Platinum sponsor: Amazon Web Services
- Carbon offset support from Jane Street, Platinum Sponsor
- Conference registration cost: 600 USD for students
- Total number of accepted papers: 319
- Program Committee: Ilia, Michael, Aliser, John, Kristoff, Anders, Leo, Calb, Neil, Den Fang, Costas, Marco Shada, Sasha, Zavier, Aov, Baki, Daniel, Aim, Ohad, Nat, Clement, Comrad, Ninga
- Distinguished Paper Awards and Winners
- Influential Paper Awards and Winners
- Sponsorship challenges: Late confirmation from sponsors
- 2024 conference will be held in Denver, Colorado, with a similar date to previous years
- Next year's conference will have an in-person element with a hybrid option for those who cannot attend
- The Milner Young Researcher Award winner: Nate Foster
- The Ocaml Language Award winner: Zavier D.
- Student Research Competition winners announced
- Discussion on conference budget and registration costs
- Proposal to create an endowment for the conference
- Need for a better understanding of the trade-offs involved in conference size and location
- Discussion on carbon offsets and venue selection for future conferences
- Suggestion to add a registration form option for vegetarians
- Closing remarks and thanks to everyone involved in the conference


## [POPL'24] Extraordinary Meeting: The Publicity Chairs Reflect on the Peer-Review Process

URL: [https://www.youtube.com/watch?v=8621PLkdpSc](https://www.youtube.com/watch?v=8621PLkdpSc)


- The speaker discusses the peer-review process in programming language and music publications
- They mention reviewing a manuscript, noting that they have made a quick decision and lack an important reference
- The speaker asks for help with writing the review and receives no response from their companion
- They mention that the publication is prestigious and well-known
- The speaker expresses frustration with the typo in the manuscript and considers accepting the work despite its flaws
- They mention that they have reviewed 70 manuscripts but have not started writing this review
- They wonder if they will ever finish reviewing manuscripts
- The speaker receives applause for their speech
- The speaker says they better think about the review, implying a lack of clarity or understanding.


## [POPL'24] The Network is the Computer: A Programming Language Perspective

URL: [https://www.youtube.com/watch?v=tUh1mrnjSoQ](https://www.youtube.com/watch?v=tUh1mrnjSoQ)


- Nate Foster discusses the principles of programming and their application in networking, including abstraction, modularity, and precision.
- He highlights the importance of precision in networking, citing the example of informal methods in the early days of the Internet.
- Foster talks about the evolution of programming languages and networking, mentioning the Active Networking project and Software Defined Networking (SDN).
- He introduces P4, a language specifically designed for programming network devices, and discusses its impact on the industry.
- Foster presents an example of how P4 can be used to implement a new forwarding abstraction in a network, demonstrating the advantages of using a programmable data plane.
- He discusses the challenges of designing a network topology that minimizes congestion and the role of programming languages in addressing these issues.
- Foster introduces the concept of micro P4, a language designed for composing small, modular pipeline mini-programs to decouple the pipeline hardware from the software implementation.
- He provides an example of building an abstract model of a switch using micro P4 and shows the potential performance improvement.
- Foster introduces the concept of P4a, a language designed for writing packet parsers, and discusses the use of symbolic simulation techniques to verify the correctness of these parsers.
- He highlights the importance of precise modeling and verification in networking and mentions the need for new tools and techniques to address the challenges of performance and network verification.


## [POPL'24] Solvable Polynomial Ideals: The Ideal Reflection for Program Analysis

URL: [https://www.youtube.com/watch?v=J2biQREB-Eg](https://www.youtube.com/watch?v=J2biQREB-Eg)


- Talk title: Solvable Polynomial Ideal
- Approach: Model Solvable Polynomial Map
- Goal: Characterize Works using model
- Key features:
  - Generalization of Solvable Polynomial Maps
  - Complete method utilizing new model
  - Solvable Polynomial Ideal generalization
  - Method producing best solvable polinomial ideal given transition formula
  - Invariance view
- Application:
  - Loop analysis
  - Producing monotonicity results
- Advantages:
  - Completeness
  - Abstraction method providing the best approximation
- Results:
  - Benchmarking: Competitive compared to other methods
  - Time Complexity: Practical and theoretical execution time
- Questions:
  - Bounding technique in classical analysis
  - Extended UKLs algorithm and proven properties
  - Long take and runtime
- Summary:
  - The Loop: Starts with no knowledge and ends with no knowledge, making no changes to the input
  - General Summary: The Loop summarizes states and transformations, making use of contextual information


## [POPL'24] On-The-Fly Static Analysis via Dynamic Bidirected Dyck Reachability

URL: [https://www.youtube.com/watch?v=y-RoVA1Qr4Y](https://www.youtube.com/watch?v=y-RoVA1Qr4Y)


- Static analysis in a continuous development setting requires fast solutions to avoid redundant analysis costs and potential overlap.
- Dyke CFL reachability is a graph reachability problem used in static analysis, providing a running time guarantee.
- The algorithm typically runs in cubic time, with the number of nodes being a good reason to believe this is a tight bound.
- A model commonly used in formulating the problem is the context-sensitive data dependence graph, which represents variables, program instructions, and labeled edges.
- The algorithm captures reachability through a properly balanced parenthesis string, which witnesses the blue path between two variables.
- The approach aims to maintain the Dyke strongly connected component (DSC) in linear time, with the inverse Ackermann function providing a quadratic worst-case complexity.
- Field-sensitive alias analysis is an example of a context-sensitive data dependence analysis that uses parentheses to model field accesses and calling conventions.
- The algorithm can efficiently handle inserting and deleting edges, maintaining the DSC in constant time, with the Union-Find data structure used for efficient computation.
- The talk discusses the potential benefits of context sensitivity in static analysis and how it can provide quick approximations for refinement later on.


## [POPL'24] Monotonicity and the Precision of Program Analysis

URL: [https://www.youtube.com/watch?v=m06wlLISzx0](https://www.youtube.com/watch?v=m06wlLISzx0)


- Marco introduces the idea of Precision Program Analysis
- He discusses false alarm problems in program analysis
- The speaker proposes the idea of ABS interpretation as a way to deal with false alarms
- He talks about monotonicity and its application to program analysis
- The speaker provides examples of program monotonicity and its implications
- Marco discusses the concept of always terminating programs and their relation to program analysis
- He explains the idea of a widening operator and its role in program analysis
- The speaker mentions the possibility of building precise program analysis tools
- He gives examples of monotonically behaving variables in a program
- Marco briefly discusses the concept of a proof system and its potential application in program analysis
- The speaker mentions the possibility of classifying programs based on their behavior
- He talks about the completeness of program analysis and its impact on program behavior
- Marco concludes by discussing the importance of precision in program analysis and the need for always terminating programs.


## [POPL'24] Flan: An Expressive and Efficient Datalog Compiler for Program Analysis

URL: [https://www.youtube.com/watch?v=Ioe3F_Z5_60](https://www.youtube.com/watch?v=Ioe3F_Z5_60)


- Presented work on Flan, an efficient excessive deadlock compiler for program analysis
- Discussed deadlock and its use in declarative programming languages
- Explained the Prive algorithm for evaluating data log rules
- Highlighted the power of data log using program analysis in a declarative manner
- Mentioned the need for extension and support for a wider range of program analysis
- Discussed the limitations of the existing data log compiler landscape and the need for a specialized core generation approach
- Shared work on building an interpreter using a high-level Scala-like textbook implementation
- Demonstrated the connection between the interpreter and compiler specifically, using specialization via the LMS framework
- Discussed the benefits of specialized index structures and multiple joint strategy optimization
- Highlighted the embedding of Scala within the data log system for interoperability and use of Scala infrastructure
- Discussed the performance of the system, with benchmark results showing the efficiency of the approach
- Noted the limitations of the current system, such as query planning and the need for a proper query planning mechanism
- Acknowledged the need to improve performance and maintain flexibility and developer productivity
- Discussed future work, including the need for a native data log garbage collector interface

Summary:
- Flan: Efficient excessive deadlock compiler for program analysis
- Prive algorithm for evaluating data log rules
- Power of data log in declarative program analysis
- Need for extension and support for a wider range of program analysis
- Limitations of existing data log compiler landscape
- Specialization via the LMS framework
- Benefits of specialized index structures and optimization
- Embedding of Scala within data log system for interoperability and use of Scala infrastructure
- Performance benchmarks showcasing efficiency
- Future work includes improving performance, maintaining flexibility, and developing a native data log garbage collector interface


## [POPL'24] Internal parametricity, without an interval

URL: [https://www.youtube.com/watch?v=bcazvJr8bjc](https://www.youtube.com/watch?v=bcazvJr8bjc)


- The speaker introduced internal parametricity without intervals.
- They discussed the identity type used to express equality in different ways.
- They mentioned the general identity type for every type and the computational rule for identity type.
- They discussed the identity universe type and the univalence axiom in higher observational type theory.
- The speaker described the computational univalence definition using identity type.
- They also presented the internal parametricity model and explained the syntax and structure of the type theory model.
- The speaker mentioned the obstacle of implementing Real in the type theory and the technique of neutral term.


## [POPL'24] Internal and Observational Parametricity for Cubical Agda

URL: [https://www.youtube.com/watch?v=dP2WH14nLvw](https://www.youtube.com/watch?v=dP2WH14nLvw)


- Introducing Online People
- Explanation of Free Theorem
- Two Solutions for Free Theorem
- Parametric Translation
- Internal Parametric Dependent Type Theory (DTS)
- Bridge Type
- Cartesian Cubical Type Theory (CCTT)
- Proof Assistant: ACTA Bridges
- Primitives of AGA Bridges
- Bridge Interval
- Bridge Type
- Gel Primitive
- Relativity: Gel Isomorphism
- Redesigned Trans Comp Operation in CCTT
- Three Theorems Proved within Proof Assistant
- Internal Quantification in Proof
- RAL's Definition of Parametricity Preservation
- Logical Relation Preservation in Dependent Programs
- Equivalence and Structural Reless Principle
- U Rot: Modular Library for Equivalence
- Equivalence Modularly Built Using Type Equipped Horizontal Equivalence
- Type Bit: A Low-level Proof for Equivalence
- Implementation of NE Bridge
- Questions and Answers
- Naive Translation of Internal Parametricity Construction
- Church Encoding Booleans
- Ral's Substitution Theorem
- Predictive System Time
- Subset Type Expressibility in R
- Contextual Limitations


## [POPL'24] Internalizing Indistinguishability with Dependent Types

URL: [https://www.youtube.com/watch?v=cgTrzJ1yVSA](https://www.youtube.com/watch?v=cgTrzJ1yVSA)


- The speaker presents a paper on internalizing indistinguishability dependent type.
- The goal is to combine dependent type theory and dependency tracking.
- Dependent type theory allows internalizing reasoning about program equivalence.
- Dependency tracking system tracks the dependency parameterized latest structure type system prevents flow of information from higher level to lower level.
- Latest structure is instantiated in concrete applications, such as security type systems and runtime erasers.
- The typing context and typing judgment are augmented with levels representing the Observer level.
- Low-level variables cannot be used in high-level computations, preventing information flow from lower levels to higher levels.
- The concept of a "box type" is introduced, which allows storing secret computations at low observer levels.
- High-level box construction ensures that low-level computations cannot extract content from the box without access from the high-level observer.
- Two letters with different contents delivered to different recipients can have different effects on the recipient, even if the letters appear identical from the outside.
- The concept of indistinguishability is introduced to capture the notion of program equivalence in the back-end language.
- The system uses dependency tracking to reason about program equivalence, focusing on indistinguishability.
- The speaker presents an extension of the Baron type system, incorporating indistinguishability and level index into the identity type.
- The type soundness and non-interference proofs are provided using a proof assistant.
- The speaker emphasizes the design of the Decoy language, which integrates indistinguishability reasoning into a dependently typed language.
- The contribution of the paper focuses on making type conversion using indistinguishability work consistently.
- The speaker discusses related work and frameworks in modal dependent type theory, such as model types and quantitative type theory.
- The speaker addresses the issue of handling PT moments, which involves obtaining inductive types, and clarifies that the example of natural numbers is specific.


## [POPL'24] Polynomial Time and Dependent types

URL: [https://www.youtube.com/watch?v=u2UcApiJA1Q](https://www.youtube.com/watch?v=u2UcApiJA1Q)


- Discussing an approach to combine programming and proof languages with linear typing
- Linear typing allows explicit accounting of resource usage
- Proposes a type system for implicit polinomial time, which is sound and complete
- Linear typing prevents duplication of natural numbers and allows for control over iteration
- Demonstrates the system through examples of sorting and touring machine simulation
- Suggests that this system could lead to a new field of computational complexity theory
- Mentioned the concept of NP mightiness and the Simplex algorithm
- Expresses interest in exploring the use of linear functional programming language (LFPL) in practical programming applications
- Refers to the Criterion soundness and completeness proof, and the potential to simulate touring machines with LFPL
- Implies that the linear functional programming language (LFPL) could have a library for polinomial time algorithms
- Encourages the audience to consider using LFPL for practical programming tasks


## [POPL'24] Guided Equality Saturation

URL: [https://www.youtube.com/watch?v=ZLkHl7YmpIY](https://www.youtube.com/watch?v=ZLkHl7YmpIY)


- Presented a method for guided equality saturation
- Demonstrated its application to various optimization problems such as memory usage reduction and tiling
- Suggested that guided equality saturation can be used to find optimizations automatically in specific domains
- Discussed the potential of implementing equality saturation using a database theory approach
- Highlighted the possibility of reusing guide sketles for similar problems and the potential for sketch abstraction composition
- Mentioned the use of a quy rewriting system with backtracking in the context of a scheduling problem


## [POPL'24] Fusing Direct Manipulations into Functional Programs

URL: [https://www.youtube.com/watch?v=uNAMe1RHde4](https://www.youtube.com/watch?v=uNAMe1RHde4)


- Introducing a new operation-based framework, BLP System (Fusion Direct Manipulation)
- FDM combines direct manipulation and functional programming
- Live programming enables developers to see real-time output changes without reexecuting the program
- BLP System offers two types of bidirectional live programming: state-based and operation-based
- The state-based system focuses on the updated output snapshot
- The operation-based system allows developers to control program modification by performing hardcoded program modifications
- Direct manipulation is defined in a simple and expressive Delta language
- Fusion algorithm propagates direct manipulation in a general-purpose functional program
- An application prototype of the SVG editor was successfully implemented
- The Delta language subset includes identity, arithmetic, and data structures like lists
- The Delta language allows for expressing common direct manipulation tasks
- Constraint introduction is used to encode relationships between sub-values
- The paper presents a detailed explanation of the Delta language and its implementation
- FDM proves correctness by ensuring that the program fused with direct manipulation gives the correct output
- The effectiveness of the fusion algorithm is demonstrated with a 14-benchmark example
- The presentation outlines three key contributions of FDM: a simple and expressive Delta language, fusion algorithm, and application design for 14 non-trivial benchmark examples
- The speaker briefly touches on the topic of minimality and the need for incremental change
- The speaker answers questions about inferring Deltas from user manipulation and the correctness algorithm

No contextual limitations apply, as the transcript provides sufficient information to formulate a summary.


## [POPL'24] Inference of Robust Reachability Constraints

URL: [https://www.youtube.com/watch?v=4DT5XZQNUSE](https://www.youtube.com/watch?v=4DT5XZQNUSE)


- Presented work on influence, Rob switch ability, and constraint
- Focused on program verification, identifying bugs, and automating the process
- Explained symbolic execution as an example technique for finding bugs
- Discussed the need for a methodology to evaluate practical replicability
- Proposed a methodology for evaluating practical replicability in CES
- Introduced the concept of robust reachability and its importance in vulnerability detection
- Discussed the challenges and limitations of characterizing case
- Presented the idea of simple reachability and complete probabilistic reachability
- Proposed the use of abduction for generating predicates
- Discussed the base generation procedure and its applicability in various languages
- Demonstrated the efficiency of the proposed algorithm in finding vulnerabilities
- Presented the task idea of fault injection for security evaluation
- Discussed the use of symbolic execution in finding potential formal vulnerabilities
- Emphasized the importance of characterizing vulnerabilities and understanding their impact

(Note: The last part of the transcript was not included in the summary, as it contains information on additional work and open questions, which are beyond the scope of this task.)


## [POPL'24] Nominal Recursors as Epi-Recursors

URL: [https://www.youtube.com/watch?v=IqSubNUOWWg](https://www.youtube.com/watch?v=IqSubNUOWWg)


- The speaker discusses U nominal recursor and its importance in proof assistant infrastructure
- The speaker compares different approaches to syntax binding and explains the nominal approach
- They introduce the concept of nominal recursion principle and its significance in defining functions recursively
- The speaker outlines the process of creating a nominal recursor and provides examples
- They mention the relationship between nominal recursion and qu inductive types, and discuss the expressiveness of different recursors
- The speaker discusses the advantages of using a definitional package for proof assistants
- The speaker concludes by stating that the best recursor depends on the specific use case and expressiveness requirements


## [POPL'24] When Subtyping Constraints Liberate: A Novel Type Inference Approach for First-C...

URL: [https://www.youtube.com/watch?v=jDhSUuvxomY](https://www.youtube.com/watch?v=jDhSUuvxomY)


- Leonel talks about subtyping constraint and liberate a novel type inference approach for first-class polymorphism
- First, he discusses classical prex polymorphism in ML and compares it to first-class polymorphism
- He presents an example of a function with a type identity function and how it can be used in a list
- The speaker then highlights the importance of first-class polymorphism in data structure fusion, encapsulation, and existential types
- He introduces the concept of the Bar function and demonstrates how it can be used with type subtyping
- The speaker discusses the challenges of type inference using subtyping relationships and how it can be used to infer intersection types
- He presents a new type inference system using subtyping and shows how it can handle multiple function positions
- The speaker also explains the concept of multi-bounded polymorphism and how it can be used with union and intersection types
- He talks about the limitations of the superf type inference system and how it can lead to non-termination and polymorphism extrusion
- The speaker concludes by discussing the future work and the conclusion of the talk.


## [POPL'24] Parametric Subtyping for Structural Parametric Polymorphism

URL: [https://www.youtube.com/watch?v=tl-DWLjVw-o](https://www.youtube.com/watch?v=tl-DWLjVw-o)


- Discussed parametric subtyping, structural parametric polymorphism, and recursive type parametric polymorphism.
- Provided examples using stack type Alpha.
- Proposed an alternative notion of parametric subtyping and a decision procedure for it.
- Discussed the limitations of structural subtyping and the need for a decidable notion.
- Highlighted the advantages of parametric subtyping, such as designability, intuitive simplicity, and a declarative characterization.
- Explained the saturation-based decision procedure and the forward and backward inference phases.
- Demonstrated the use of the decision procedure on a binary tree example.
- Provided an overview of the main contributions and future work.


## [POPL'24] Unboxed data constructors -- or, how cpp decides a halting problem

URL: [https://www.youtube.com/watch?v=YWEcslvNuKc](https://www.youtube.com/watch?v=YWEcslvNuKc)


- Constructor unboxing is a feature in C++ that decides the halting problem
- The feature is designed to support low-level data representation and is influenced by work from Stephen and other researchers
- The feature allows for a single Constructor record field to be unboxed
- A microbenchmark shows a 20x speedup when unboxing annotations, which can be used to speed up programs with large amounts of memory usage
- The compiler can be extended to support multiple type IDs and error cases, and to automatically unbox certain types
- A two-step process is proposed for designing the feature, involving abstraction and implementation
- The approach could be used in languages within the ML family, such as OCaml, Rust, and JavaScript
- The transcript includes a discussion on type checking and termination, showing that the algorithm is sound and complete for the first-order fragment
- The speaker concludes by mentioning ongoing work on high-order model checking and related research areas


## [POPL'24] Polymorphic Type Inference for Dynamic Languages

URL: [https://www.youtube.com/watch?v=dYJ9DB5ySwU](https://www.youtube.com/watch?v=dYJ9DB5ySwU)


- The speaker presents a type system inference algorithm for dynamic languages.
- The goal is to infer the most specific type for expressions.
- The algorithm incorporates polymorphism, overloading, and genericity.
- It uses type case, type decomposition, and union elimination rules.
- The system supports Union and intersection types, allowing for flexible and precise type inference.
- The speaker discusses the complexity of the algorithm and the importance of performance optimization.
- They mention the use of a specialized set solver and prototype implementation for better efficiency.
- The speaker also touches upon the concept of type principality, where every expression has the smallest type.
- They provide an example of a type map function for a list of tuples, illustrating the inference process.
- They discuss the impact of order on performance and the need for control over semantics.
- They mention the use of a library for subtyping and the importance of optimizing the implementation.
- The speaker explains the difference between typing values and typing expressions, emphasizing the need for a basic type system.


## [POPL'24] Efficient CHAD

URL: [https://www.youtube.com/watch?v=HUoUap7nO2U](https://www.youtube.com/watch?v=HUoUap7nO2U)


- The speaker discussed the idea of automatic differentiation, particularly Reverse Mode AD.
- The algorithm aims to efficiently produce a program that computes the derivative.
- The speaker mentioned that the reverse ID algorithm is useful in various disciplines.
- They also talked about computational complexity, time complexity, and the need for practical efficiency.
- The speaker introduced a list of operations that need to be made relatively efficient.
- They discussed the need to make environment derivative addition and state passing cost-effective.
- The speaker mentioned that the algorithm is still being worked on, and there might be ongoing efforts to extend the proof.
- The speaker mentioned that the algorithm is essential to preserve complexity, especially in the case of reversible algorithms.


## [POPL'24] ReLU Hull Approximation

URL: [https://www.youtube.com/watch?v=Dn4y4PqhvgI](https://www.youtube.com/watch?v=Dn4y4PqhvgI)


- The speaker discussed the RLU whole approximation technique and its importance in high-performance computing.
- They highlighted the need for model verification, which involves ensuring the correctness of the model.
- They talked about the challenges of network verification, including non-enumerable actions and non-linearities.
- The speaker introduced the concept of a "ripping RLU hole," which involves constructing a convex hull RLU function.
- They demonstrated the use of this approach in a 3D space with two input variables and one output variable.
- They discussed the limitations of this technique in high-dimensional cases and mentioned future work on generalizing the function.
- They mentioned that the SODA framework, a tool for deep learning, can be used to integrate the approach.
- They addressed the practical challenges of scaling deep learning with heterogeneous hardware, specifically GPUs.
- They concluded by mentioning the need for sequential optimization and possible issues with parallelization in calculating the convex SC operation.


## [POPL'24] On Learning Polynomial Recursive Programs

URL: [https://www.youtube.com/watch?v=IiYXHqzYuYo](https://www.youtube.com/watch?v=IiYXHqzYuYo)


- Introduction to learning framework
- Fibonacci sequence and number involution comparison
- Polynomial representation of Fibonacci sequence
- Explanation of automata and their roles in learning framework
- Overview of automata equivalence problem and exact learning problem
- Anglin's results on the exact learning problem for finite automata
- Discussion of the Z-weighted automaton exact learning problem
- The concept of the P-finite automaton equivalence problem
- Brief explanation of the P-finite automaton learning problem
- Highlighting the practicality of the presented approach for certain instances
- Discussion on the potential extension of Anglin's algorithm to infinite or symbolic alphabets
- Closing remarks and last-minute questions about the learning framework.


## [POPL'24] Programming-by-Demonstration for Long-Horizon Robot Tasks

URL: [https://www.youtube.com/watch?v=b2iN3keWUgk](https://www.youtube.com/watch?v=b2iN3keWUgk)


- Noah presented a paper on programming demonstration for long-horizon robot tasks.
- The main contribution is a novel algorithm that synthesizes programmatic robotic policies.
- The paper aims to enable long-horizon tasks, such as household chores and restaurant work.
- The program must be capable of executing in large environments with various object types and locations.
- The algorithm uses a large language model to guide the generation of a program based on a demonstration provided by the end user.
- The algorithm consists of sketch inference, pruning, and completion steps.
- The sketch inference step uses regular expression learning to generalize the demonstration.
- The pruning step uses an approximation-based approach to eliminate non-feasible partial programs.
- The completion step uses a large language model to guide the search for a complete program.
- The paper evaluates the algorithm on a benchmark consisting of 40 tasks with varying difficulty levels.
- The algorithm was able to find ground truth programs for most tasks within the time limit.
- The paper compares the algorithm with other approaches, such as the SAA solver, CVC 5, and GPT 35.
- The speaker mentioned that they are working on implementing the algorithm to evaluate its performance on actual robots.


## [POPL'24] Mechanizing Refinement Types

URL: [https://www.youtube.com/watch?v=UXA7SRArBj8](https://www.youtube.com/watch?v=UXA7SRArBj8)


- Presentation on mechanizing refinement type in joint work with Nikki Vazou, Md. Rana Jalal, and UC San Diego
- Discussion of refinement type system, its representation, and its applications
- Emphasis on the prevention of runtime errors and the importance of functional correctness
- Overview of the project's goal to create a practical refinement type engineering system
- Explanation of the challenges faced in formalizing meta-theory, semantic subtyping, and polymorphism
- Introduction of the Lambda RF calculus, which combines semantic subtyping and parametric polymorphism with a supplied meta-theory
- Discussion of the implementation system's features, including semantic subtyping and automatic verification of function calls
- Overview of three challenges faced during the formalization process: implicit semantic subtyping, logical implication, and polymorphism
- Description of the stratified calculus approach to breaking circularity
- Explanation of how the implication challenge was addressed by formalizing the refinement implication relationship and supplying a mechanization denotation proof
- Discussion of the ant solver challenge and its relation to the difficulty of polymorphism
- Introduction of a simple kind system to handle refinement parametric polymorphism
- Explanation of the type safety and soundness implication reduction and its benefits
- Mention of the use of liquid HCLL for mechanization and the incorporation of a positivity Checker to address the equation walk around issue
- Conclusion by presenting the Lambda RF calculus and expressing interest in extending it to include GHC Primitives and data type literals
- Discussion of the requirement for coercion in system FR and its difference from system F


## [POPL'24] VST-A: A Foundationally Sound Annotation Verifier

URL: [https://www.youtube.com/watch?v=f1PkaDlf6Eo](https://www.youtube.com/watch?v=f1PkaDlf6Eo)


- J Jin talks about foundationally sound annotation verifier
- VST verifies three program respect comp semantics based separation logic
- Interactive verifier requires expertise compared to annotation verifier
- VST supports nonstructural proof
- VST proposes control flow splitting algorithm
- VST improves proof effort and automates updates
- VST is more efficient for small programs with complex structures
- VST's future improvements focus on better solutions for conjunction rules and annotation ghost updates
- VST supports partial assertion and frame inference
- VST improves verification time and performance during interactive development


## [POPL'24] Fully Composable and Adequate Verified Compilation with Direct Refinements betwe...

URL: [https://www.youtube.com/watch?v=AS5wHIjHYMc](https://www.youtube.com/watch?v=AS5wHIjHYMc)


- Speaker discusses verified compilation and direct refinement in the context of open module support.
- The speaker highlights the importance of direct refinement and compiling open modules, including vertical and horizontal composition, equivalence, and semantic linking.
- The speaker emphasizes the difficulty of compiler-like multiple passes and the need to vertically compose refinements.
- They mention the challenges of protecting private states and ensuring that the user does not know the compiler-implemented changes.
- The speaker outlines their approach, which includes applying the full comparison chain concept and providing answers to questions like developing an approach that directly supports direct refinement.
- They discuss the challenges of creating a high-level user specification for assembling programs.
- The speaker provides a running example of a communication protocol and highlights the non-trivial aspects, such as passing pointers between different modules.
- They explain the three-step proof process for direct refinement, focusing on the adequacy property, horizontal competitions, and vertical composition.
- The speaker discusses the challenge of ensuring the transitivity of cryptical memory relations and the need to split involved injections.
- They introduce the concept of conert direct refinement and its left table showing Rel guarantee conditions and individual compiler pass conditions.
- The speaker mentions their work's key discoveries, such as the cepic relation and memory protection being transitive, and its application to the compilation verification project artifact online.
- The speaker also mentions ongoing future works, including reducing the connecting direct refinement back to the whole program correctness concept and connecting user-level program verification.


## [POPL'24] A Formalization of Core Why3 in Coq

URL: [https://www.youtube.com/watch?v=c4QHpY5GhWU](https://www.youtube.com/watch?v=c4QHpY5GhWU)


- Deductive verifier building
- Challenges of deductive verifier
- Program takes input, annotated specification, and produces output set of logical formula
- SMT solver used for solving the formula
- Existing real-world deductive verifier tool chains
- Foundational approach to building a tool
- VST, CML, formalizing semantics, proof assistant
- Verified implementation of Y3
- Y3 logic formalization
- Expressive Y3 logic with automation via translation to SMT solver
- Challenges of verified implementation
- Y3's future extensions
- Verifying intermediate verification languages
- Formalization of Y3 typing rules and termination checks
- Reusability approach and framework specification
- Potential for generalizing the framework for semantics and logics


## [POPL'24] Securing Verified IO Programs Against Unverified Code in F*

URL: [https://www.youtube.com/watch?v=7jCChuyZHR4](https://www.youtube.com/watch?v=7jCChuyZHR4)


- Presenter: Chesar Andrii
- Purpose: Introduce the Scio verified secure compilation framework
- Key Points:
  - Scio allows linking verified code with unverified code securely
  - Two-pronged approach: enforce assumptions and access control policies
  - High-order contracts enforce assumptions made by unverified code
  - Reference monitors enforce access control policies, preventing bad behavior
  - The framework verifies the global safety property of the program
  - The framework supports terminating IO programs
  - The framework is proven to be secure with a strong compilation criterion
  - The framework can be used for mutually distrusting programs

Please note that the summary above is based solely on the transcript provided and may not capture all nuances or intricacies of the original presentation.


## [POPL'24] Sound Gradual Verification with Symbolic Execution

URL: [https://www.youtube.com/watch?v=BB1D6R9U-rs](https://www.youtube.com/watch?v=BB1D6R9U-rs)


- The speaker presents an approach to sound gradual verification using symbolic execution and collaboration with Jonathan Aldrich.
- They introduce Wy Coyote as a character who wants to catch Road Runner using verification methods.
- The speaker explains the concept of gradual verification, which allows for the incremental building of specifications and receiving feedback about behavior.
- They discuss the problems of formalizing state proofs, ensuring soundness, and dealing with unsoundness issues in gradual verification.
- The speaker provides an example of a method called "catch RoadRunner" and its verification process.
- They highlight the importance of symbolic execution in the gradual verification process and the challenges of ensuring soundness.
- The speaker outlines a strategy for fixing unsoundness issues by defining dynamic semantics and language-specific proofs of soundness.
- They mention that the technique of symbolic execution is used to make the verification process more predictable and efficient.
- The speaker briefly discusses the performance implications of using symbolic execution and the need for further evaluation.


## [POPL'24] Type-based Gradual Typing Performance Optimization

URL: [https://www.youtube.com/watch?v=YHUadoP9ZFg](https://www.youtube.com/watch?v=YHUadoP9ZFg)


- Gradual typing is important for developer speed and fast programs
- Performance issues can arise from unnecessary casts and runtime type checks
- Gradual typing involves adding type annotations at different levels: module, function, and variable
- Soundness is crucial in gradual typing to ensure annotations are not completely erased
- A case study on transitioning a Quantum compiler codebase from untyped Python to a type system demonstrates the need for gradual typing and avoiding unnecessary casts
- Discriminative typing can help speed up programs and provide blame labels for optimization
- Subtyping and constraint solving are key components of discriminative typing
- Gradual subtyping allows for incremental type migration in a gradually typed language
- The Reticulated Python project found significant speedup in some programs using discriminative typing, but also slower compilation times for some programs
- Gradual subtyping can be challenging in practice and may not work well for all types of languages, especially those with complex, dynamic structures
- The speaker acknowledges that the core of the type system should be kept small and that inference specialization can be used to avoid slow Dynamic versions
- The speaker provides an example of using the plus operator with different objects to illustrate the need for careful handling of type inference in certain cases


## [POPL'24] Total Type Error Localization and Recovery with Holes

URL: [https://www.youtube.com/watch?v=j1Xyuu4kVwQ](https://www.youtube.com/watch?v=j1Xyuu4kVwQ)


- Eric discusses the challenges of handling ill-typed code in various programming languages.
- He introduces the concept of a "marked lambda calculus" for localizing and recovering from type errors in a gradual typing system.
- Eric presents a framework for type error localization and recovery, including the use of unknown types, marking syntax, and handling inconsistent types.
- He demonstrates how his approach can be applied to different programming languages, such as Rust and Hazel.
- Eric discusses the potential for automating some aspects of the process and mentions ongoing research in the field.
- He briefly touches on the complexity of adding instrumentation and the potential trade-offs between performance and ease of use.
- Eric acknowledges the challenges of developing a unified framework for various type systems and suggests gradual dependent typing as a possible solution.
- He concludes by emphasizing the importance of incorporating tooling support for these techniques in language development.


## [POPL'24] Orthologic with Axioms

URL: [https://www.youtube.com/watch?v=uW39tCEqfUU](https://www.youtube.com/watch?v=uW39tCEqfUU)


- The speaker discussed the use of Oric Logic in helping with formal reasoning, proposing the design of an algorithm that is guaranteed efficient, predictable, and respects the theoretical foundations of the logic.
- The speaker mentioned the AIC property, which allows for solving problems efficiently with an algorithmic proof, logical proof system, and polynomial time proof search procedure.
- They discussed the potential application of Oric Logic in type systems, decision procedures for type inhabitation, and subtyping in refinement type systems.
- The speaker also introduced the concept of Oric Variable Predicate, which extends the scope of Oric Logic to include predicate variables and propositional logic functions.
- They mentioned the use of Oric Logic in the Liquid Type system and its potential to improve efficiency and reproducibility across machines and versions.
- The speaker demonstrated the use of Oric Logic in a data log application, extending the logic to support axioms and proving theorems in the classical sequent calculus.
- They discussed the possibility of extending Oric Logic to support predicate variables and propositional logic functions, allowing for the encoding of more complex statements and expressing congruence relations.
- The speaker addressed the question of whether Oric Logic can be used as a model in the same way as classical logic, emphasizing the importance of understanding distributivity and intuitionistic logic.
- They answered questions about the implication connective in Oric Logic and the generalization of restrictions in the number of formulae.
- The speaker mentioned the potential use of Oric Logic in solving external solvers and the possibility of reusing axioms in the decision procedure.


## [POPL'24] Deciding Asynchronous Hyperproperties for Recursive Programs

URL: [https://www.youtube.com/watch?v=RL-gKSxvzfI](https://www.youtube.com/watch?v=RL-gKSxvzfI)


- The research focuses on the combination of asynchronous hyperproperties and pushdown models for better fit of recursive programs.
- The work introduces a new asynchronous hyperlogic and a pushdown model checking algorithm.
- The presentation covers the differences between classical and hyper properties, and the advantages of using hyper LTL and stuttering hyper LTL for modeling asynchronous systems.
- The talk highlights the challenges of pushdown model checking, the introduction of well-aligned restrictions, and the use of the well-aligned next operator.
- The speaker discusses the complexity of quantifier alternation and the need for future work in implementing the proposed algorithms and generalizing the criterion beyond stuttering and mumbling.


## [POPL'24] Calculational Design of [In]Correctness Transformational Program Logics by Abstr...

URL: [https://www.youtube.com/watch?v=e2F0Y_LIhV4](https://www.youtube.com/watch?v=e2F0Y_LIhV4)


- Discussed natural relational semantics
- Introduced transformational semantics
- Explained structural properties
- Defined abstraction Alpha and collecting semantic precise hyper property
- Presented theory logic and fixed Point form
- Applied AEL correspondence and logic approximation
- Discussed fixed Point set order deductive system
- Introduced fixed Point induction and approximation
- Mentioned the need for precise approximate results
- Highlighted the importance of least fixed points and complete ltis
- Discussed the concept of a complete X
- Described the difference between fix Point induction and approximate logic
- Presented the idea of a variant function for loop invariants
- Noted the need for different induction proof rules for approximate and complete cases
- Mentioned the use of well-foundedness in total correctness proofs
- Emphasized the importance of sound approximate logic and its relation to induction principles
- Discussed the need for a precise induction principle for total correctness
- Expressed the desire to survive Peters question


## [POPL'24] Concluding Remarks

URL: [https://www.youtube.com/watch?v=XML7bRPv7P4](https://www.youtube.com/watch?v=XML7bRPv7P4)


- Transcript speaker expresses gratitude to various individuals and teams for their work during the conference
- They specifically thank the PC chair, AV team, student volunteers, IET team, and IATS team
- The IATS team received an award for the best venue in London with 500 people
- The speaker mentions it being a positive memory and a vibrant spirit within the community
- They hope attendees continue their enthusiasm in the next decade



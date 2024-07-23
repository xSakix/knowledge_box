## Simplifying Systems with Elixir • Sasa Juric • YOW! 2020

URL: [https://www.youtube.com/watch?v=EDfm2fVS4Bo](https://www.youtube.com/watch?v=EDfm2fVS4Bo)

 * The speaker explores simplifying implementation of software systems using Elixir, focusing on web servers and databases
* Elixir is a lightweight, concurrent programming language with the BEAM runtime
* Elixir processes run inside a single OS process, allowing for efficient communication and shared memory without the need for external components like load balancers or service managers
* The speaker discusses the benefits of using Elixir in a software system: multicore capability, vertical scalability, separation failure, and separation latency
* In the case study of the Earl Angeles blog site, the speaker demonstrates how the system is organized with separate processes for handling incoming requests and serving static files
* The speaker discusss how Elixir simplifies handling errors and failures in a concurrent environment, allowing for independent processes to handle different tasks
* The Earl Angeles blog site uses an embedded database, reducing complexity compared to using a third-party database
* The system is testable with standard Triple A tests, ensuring data is properly cleaned and accessed as desired.
* The speaker discusses serving HTTP traffic and the use of Let's Encrypt for SSL certificates
* The system uses Elixir's supervision tree to organize processes in a hierarchical manner
* The speaker also runs a local Acme server for certificate management, reducing the gap between production and development environments.
* The talk concludes with the benefits of using Elixir in software systems: simplicity, efficiency, and ease of testing.


## How to Improve Developer Productivity • Jez Humble • YOW! 2020

URL: [https://www.youtube.com/watch?v=5_rrQND3lpQ](https://www.youtube.com/watch?v=5_rrQND3lpQ)

 * Jez Humble from Google spoke about improving developer productivity
* Measuring software delivery performance is important, but traditional measures like lines of code or velocity are not reliable
* Continuous Delivery practices can improve both software delivery and organizational performance
* Four metrics for measuring software delivery performance: deploy frequency, lead time, change fail rate, and mean time to restore service
* High performing teams have shorter lead times, frequent deployments, low failure rates, and quick recovery times
* Elite performers deploy multiple times per day with the lowest change fail rate and fastest mean time to restore
* Continuous Delivery helps organizations achieve better security, stability, and quality in addition to faster delivery
* Lean management practices such as visual management, limiting work in progress, and lightweight change approval processes can improve software delivery performance
* Agile Transformations that force exact adherence to agile principles may hinder productivity and innovation
* Psychological safety, trust, and effective communication are key factors in building high performing teams
* Effective leadership and tooling can help reduce technical debt and improve productivity
* Remote work has had little impact on productivity during the pandemic, with flexible tools and processes supporting developers
* Research from Google's Dora research program supports these findings.


## Discontinuous Improvement • Kevlin Henney • YOW! 2020

URL: [https://www.youtube.com/watch?v=q4oGqf8r9P4](https://www.youtube.com/watch?v=q4oGqf8r9P4)

 * The speaker discusses the concept of discontinuous improvement in software development, contrasting it with continuous improvement.
* Discontinuous improvement refers to radical change, while continuous improvement means changing something for the better over time.
* The speaker notes that lean manufacturing and software development borrowed the term "kaizen" from Japanese, which originally meant "improvement" but was repurposed to mean "continuous improvement."
* Elimination of waste is a dominant aspect of lean thinking, but the meaning of waste can be misunderstood. Not all waste is bad, and some waste can be necessary for achieving flow.
* Concurrency, or working on multiple things at once, is another aspect of discontinuous improvement in software development. Set-based concurrent engineering is a contrast to point-based engineering, which can lead to technical debt and discontinuity in the development process.
* Continuous integration, deployment, and refactoring are practices related to continuous improvement in software development. However, these practices can also be seen as disruptive and radical changes when taken to the extreme.
* The speaker discusses the importance of preserving current context and understanding stable intermediate forms in the evolution of complex systems.
* Disruptive innovation is a term often used to describe radical change in business, but it can be overused and misapplied. The speaker encourages embracing discontinuity and dealing with the load of change rather than trying to avoid it.
* The speaker mentions the importance of understanding physics metaphors and concepts like force, work, and acceleration in software development. They also discuss the challenges of dealing with technical debt and optimizing velocity while heading in the wrong direction.
* The speaker encourages embracing discontinuity and dealing with steep parts of the change curve rather than trying to smooth out the process. They also mention the importance of focusing on security issues and staff retention in software development.
* The speaker discusses the importance of design, collective knowledge, and codification in software development. They mention the challenges of dealing with ignorance and uncertainty in the development process.
* The speaker emphasizes that it is impossible to prioritize business value without violating the laws of physics. Instead, they encourage being aware of the limitations of our knowledge and dealing with situations as they come.


## How to be a more Impactful Data Analyst • Claire Carroll • YOW! 2020

URL: [https://www.youtube.com/watch?v=d8H0942c3aQ](https://www.youtube.com/watch?v=d8H0942c3aQ)

 * Claire Carroll, data analyst at Fishtown Analytics, shares her journey from inheriting a BI system as a data analyst to becoming an impactful data analyst
* Started as a data analyst in a startup in Sydney, inherited a Bi system and felt valuable when she could answer business questions
* Felt frustrating when the backlog kept growing and she couldn't keep up with new data questions
* Realized the need to learn SQL and understand business knowledge to express it in code
* Learned version control and build transformation layers to manage changes and automate reports
* Adopted software engineering practices like testing, modularity, and continuous integration
* Changed mindset from being a service provider to building a product
* Learned to train stakeholders and enable self-service reporting
* Transitioned into an analytics engineer role, which is different from a data analyst role but can be complementary
* Shares her experience as a Community manager in the DBT community and how it helped her career growth.


## Apache Pulsar: The Next Gen Messaging & Queuing System • Karthik Ramasamy • YOW! 2020

URL: [https://www.youtube.com/watch?v=_SSFM7FTI8A](https://www.youtube.com/watch?v=_SSFM7FTI8A)

 * Karthik Ramasamy, Senior Director Engineering at Streamlio, introduced Apache Pulsar as a messaging and queuing system that brings together compute, storage, and messaging in a single system.
* Data collection is increasing due to sensors attached to various devices producing high-velocity data streams. Real-time processing of this data is essential for making decisions based on fresh data.
* Apache Pulsar is designed as a cloud-native system with a natural separation of compute and storage, allowing for independent scaling. It provides messaging and queuing functionality, as well as stream data processing capabilities.
* Key concepts of Apache Pulsar include: tenancy, topics, partitions, segment-based architecture, and state management.
* Pulsar is naturally multitenant and supports a hierarchical namespace for topics and namespaces within a tenant. It allows for multiple applications to share the same stream data and process it in parallel.
* Apache Pulsar provides automatic load balancing and fault tolerance through its segment-based architecture, where segments are replicated across multiple nodes. This ensures high availability and reduces the need for expensive rebalancing operations.
* The system uses a distributed log storage to ensure data durability and supports various levels of consistency for different use cases. It also provides a unified messaging model that combines both queuing and streaming paradigms.
* Apache Pulsar is designed to be easier to deploy in Kubernetes environments compared to legacy systems like Kafka, and it supports various authentication, authorization, and rate control plugins for isolation and security.
* The system provides a simple producer and consumer API, as well as schema registry support for type safety and consistency across applications. It also supports various programming languages and integrates with popular data processing frameworks like Spark and Flink.
* Apache Pulsar is used by over 600 companies in production and has grown exponentially in the past six months.


## Scaling Your Architecture With Services & Events • Randy Shoup • YOW! 2020

URL: [https://www.youtube.com/watch?v=Idkz_rOS-ug](https://www.youtube.com/watch?v=Idkz_rOS-ug)

 * Randy Shoup, former engineering leader at eBay, Stitch Fix, WeWork, and currently VP Engineering at Yelp, discusses scaling architecture with services and events
* Monolithic architecture is suitable for small companies with one team, but as the company grows and teams increase in number, monolithic architecture becomes less efficient
* In the optimizing phase, companies tend to consolidate many teams into fewer teams, and architectures get smaller in size
* The scaling phase is where microservices and event-driven communication come in
* Twitter, Amazon, and eBay all went through similar evolutions from monolithic architecture to microservices
* Microservices have well-defined interfaces that allow each team to operate independently and autonomously
* A service architecture provides fault isolation and performance optimization within the service boundary
* Isolated persistence is important to prevent sharing a database between services
* Event-driven communication allows decoupling of different domains and asynchronous interaction between services, ensuring they can scale independently
* Canonical systems record data in their respective services, which produce events that are consumed by other services
* Change data capture and transactional outbox are two methods for producing events from a producer service when state changes occur
* Asynchronous event-driven communication using local caches allows for efficient interaction between services without the need for real-time joins or materialized views.


## Building Adaptive Systems For a Fast Flow of Change • Susanne Kaiser • YOW! 2020

URL: [https://www.youtube.com/watch?v=r2XSTFDsO3Y](https://www.youtube.com/watch?v=r2XSTFDsO3Y)

 * Nokia's market share dropped 90% within six years due to underestimating the increasing importance of software in mobile phones and being slow to adapt to changing market conditions.
* Building adaptive systems for a fast flow of change involves understanding the business strategy, worldly maps, software architecture design, and team organization.
* Business strategy: Understanding the competitive landscape and how it changes (Waltzing Maps).
* Software architecture perspective: Domain-driven design to build better software that aligns with the business domain and strategy.
* Team organization perspective: Small, autonomous cross-functional teams with clear communication and ownership boundaries.
* Nokia's decline was due to inertia from past success, resistance to transitioning to new technologies, and a focus on hardware rather than software.
* Adaptive systems need to be able to evolve and respond to changing landscapes quickly and efficiently.
* The climatic pattern describes external forces that influence the business landscape and can be anticipated to prepare for strategic advantage.
* Domain-driven design involves understanding the problem domain, analyzing it with domain experts, and designing software based on a shared language and model.
* Tactical design patterns support low-level design decisions and architecture implementation.
* Subdomains should be partitioned to reduce complexity and improve situational awareness.
* A team of domain experts and developers collaborate closely to gain domain knowledge and challenge assumptions.
* Use appropriate methods for each subdomain in the evolutionary flow.
* Streamlined teams can produce steady flows of feature delivery, incorporating feedback and reducing cognitive load.
* Autonomous cross-functional teams enable fast flow and minimize handovers between teams.
* Platform teams support infrastructure and self-service tools to ease collaboration between teams.
* Complicated subsystems require specialized knowledge and may need to be streamlined with the rest of the system.
* Use small, long-lived teams that are responsible for end-to-end functionality and minimize cognitive load.
* Coaching and training can facilitate the adoption of new technologies and practices within a team.
* Serverless technology and cloud platforms enable infrastructure to be fully managed and reduce cognitive load in complex subsystems.
* Absorbing change requires a design that is flexible and allows for graceful evolution.


## Cadenza: Building Fast Functional Languages Fast • Edward Kmett • YOW! 2020

URL: [https://www.youtube.com/watch?v=gbmURWs_SaU](https://www.youtube.com/watch?v=gbmURWs_SaU)

 * Speaker is working on a project called Cadenza, a functional language with fast evaluation, type checking, and inference compiler
* Goal is to build a dependently typed language with good performance using a simple Lambda calculus interpreter
* Steps through process of building a simple interpreter for evaluating expressions in Lambda calculus
* Discusses challenges of implementing a type checker without substitution and the benefits of normalization evaluation
* Mentions use of the Truffle framework to implement JIT compilation and optimization techniques like deoptimization, node optimization, and trampolining
* Talks about the importance of efficient memory representation and environment handling in functional languages
* Discusses potential improvements for Cadenza, including better error reporting and more advanced features like dependent types and ETA-expansion.


## Inside Every Calculus Is A Little Algebra Waiting To Get Out • Erik Meijer • YOW! 2020

URL: [https://www.youtube.com/watch?v=k_XHrhaRn3A](https://www.youtube.com/watch?v=k_XHrhaRn3A)

 * Speaker discusses his strange dreams involving mathematics, specifically calculus and algebra
* Mentions using machine learning and differentiable programming in software development
* Distinguishes between discrete value and continuous value software and their relationship to calculus and algebra
* Discusses the history of real numbers and the challenges of defining them
* Introduces dual numbers and their use in mathematics and computer science
* Explains how to calculate derivatives using dual numbers and functional programming concepts
* Mentions the importance of understanding the definition of a real number and the concept of isomorphism
* Discusses applying continuation passing transformation and backpropagation to neural networks
* Talks about the benefits of using a Point-free style in writing code
* Introduces the concept of scholarization and its simplification of complex formulas
* Mentions the importance of understanding the underlying mathematics and avoiding intuition when learning calculus and differentiation.


## Jepsen 13 • Kyle Kingsbury • YOW! 2020

URL: [https://www.youtube.com/watch?v=_TD31etxb_w](https://www.youtube.com/watch?v=_TD31etxb_w)

 * Kyle Kingsbury from Jepsen project discusses distributed systems and common failure conditions
* Database focus: Engines often hide details of database access and versioning, making it challenging to build reliable systems
* Discusses concepts of Discovery Services, coordination primitives, information hiding, and transaction dependencies in distributed systems
* Introduces Jepsen, a library for testing concurrent systems, focusing on the database "black box"
* Covers L Systems and Cycles graph, total order, version dependency, and consistency violation identification
* Discusses PostgreSQL and MongoDB case studies and their claimed data consistency guarantees, including repeatable read and snapshot isolation
* Talks about Redis and its replication system, raft consensus algorithm, and potential issues like infinite loops and lost updates
* Provides insights on choosing a database, the importance of understanding consistency models and failure modes, and testing methodologies.


## Scala Implicits Revisited • Martin Odersky • YOW! 2020

URL: [https://www.youtube.com/watch?v=dr0PUXQhg3M](https://www.youtube.com/watch?v=dr0PUXQhg3M)

 * Implicits are a defining feature of Scala, used extensively but controversial
* Originally intended as implicit conversions to solve the late binding problem in object-oriented languages
* First step towards implicits was implicit conversion, added in 2004
* Late binding problem: extending classes and interfaces is difficult due to the need for wrapper classes or casting
* Implicit conversion cannot extend a class directly and requires creating an automatic wrapper, which has downsides
* Implicit parameters were introduced in 2006 to improve implicit resolution and reduce the need for type classes
* Implicits are used extensively in Scala libraries such as Cats and Shapeless
* Mistakes made during the design of implicits:
  + Implicit names shouldn't matter, but they can cause shadowing problems
  + Nesting of implicit values can lead to ambiguity
  + Coherence issues with implicit values in different scopes
* Implicits have been redesigned in Scala 3 to improve coherence and reduce confusion, making the language more predictable.
* Type class-based approaches are an alternative to implicit conversions but have their own trade-offs.


## Strongly Typed System F in GHC • Stephanie Weirich • YOW! 2020

URL: [https://www.youtube.com/watch?v=rS2mpuwAK4M](https://www.youtube.com/watch?v=rS2mpuwAK4M)

 * Stephanie Weirich talks about strongly typed System F in GHC
* Discusses the challenge of representing data types and abstract syntax for System F with strong typing
* Uses an analogy of representing dragons to illustrate the concept of variable representation and de Bruijn indices
* Describes implementing a simply typed Lambda calculus and extending it to a strongly typed version using a substitution library
* Mentions her inspiration from ancient documents and a fairy tale
* Explains the importance of keeping track of binding levels and variable scopes in substitution implementation
* Discusses the benefits of encapsulating reasoning and creating a reusable library
* Shows examples of implementing a simple evaluator and modifying the data structure for type checking
* Talks about using GADTs to capture type information and represent indexed expressions
* Discusses the importance of precise typing and the role of a type checker in enforcing it
* Mentions extending System F by defining new constructors, type abstraction, and instantiating types
* Talks about using single tense library for dependency-free programming and binding forms
* Discusses the challenges of implementing substitution operations and function application in a strongly typed system
* Concludes by discussing the benefits of strong typing and encouraging the audience to take a closer look at the code available on GitHub.


## Unveiling much Simplified Functional Programming in Scala • Afsal Thaj • YOW! 2020

URL: [https://www.youtube.com/watch?v=t5tMQ0Kcq1Q](https://www.youtube.com/watch?v=t5tMQ0Kcq1Q)

 * The speaker discusses the challenges of implementing functional programming (FP) in Scala for big data problems, focusing on issues with jargon, type inference, and boilerplate code.
* Big data problems involve analyzing large datasets, such as transaction records or customer data from banking apps, requiring efficient handling and processing.
* The speaker introduces the problem of finding attributes (features) in a dataset, using a customer's account transactions as an example. They aim to build a library for generating features quickly with a simple interface.
* The library should allow developers to define business logic without performance optimization concerns and enable adding new features easily.
* A thin layer abstraction over the backend engine is necessary to optimize queries and join data sets efficiently.
* The speaker uses an example of defining a feature based on customer transactions within a specific time window, demonstrating the importance of a simple representation for input and output.
* They also discuss using expression APIs to expose backend engines and combining helper functions for type inference and easier development.
* The goal is to simplify FP programming with Scala by addressing issues such as type inference, boilerplate code, and making feature generation more accessible.


## Scodec for Scala 3 • Michael Pilquist • YOW! 2020

URL: [https://www.youtube.com/watch?v=Uo9S4iKw8NA](https://www.youtube.com/watch?v=Uo9S4iKw8NA)

 * Michael Pilquist talks about Scodec, a binary processing library he built for Scala 3
* He discusses the background of Scodec and how it relates to binary processing and formal specification
* He explains how Scodec works at a bit level and demonstrates decoding a bit string using the library
* Pilquist then focuses on the transition from Scala 2 to Scala 3 and the differences in the macro system
* He discusses new features such as inline keywords, extension methods, and the use of `scala.collection.immutable.Tuple`
* He mentions some challenges in porting code from Scala 2 to Scala 3, including compile time errors related to string literals and hexadecimal numbers
* Pilquist also touches on the new numeric literal feature in Scala 3 and its potential use cases
* Overall, he emphasizes how Scala 3 simplifies library development and reduces dependency on external libraries like Shapeless.



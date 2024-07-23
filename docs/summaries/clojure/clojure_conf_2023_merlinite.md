## "Design in Practice" by Rich Hickey

URL: [https://www.youtube.com/watch?v=c5QF2HjHLSE](https://www.youtube.com/watch?v=c5QF2HjHLSE)

 
- Presenter discusses design process, focusing on problem diagnosis and solution.
- He mentions using a decision matrix spreadsheet to evaluate different approaches and make a choice.
- The presenter emphasizes the importance of clear, concise problem statements and detailed descriptions.
- He also talks about avoiding subjective judgment and predefined sets when evaluating options.
- The presenter encourages introspection, questioning assumptions, and seeking alternative perspectives.
- He mentions the value of diagramming to understand relationships and visualize solutions.
- The presenter highlights the importance of growing a team, sharing knowledge, and giving constructive feedback.
- He also stresses the need for continuous learning, practice, and improvement in design.


## "Vector Symbolic Architectures In Clojure" by Carin Meier

URL: [https://www.youtube.com/watch?v=j7ygjfbBJD0](https://www.youtube.com/watch?v=j7ygjfbBJD0)

 
- Carin Meier discusses Vector Symbolic Architecture (VSA) in Clojure, which is a way to approach AI that is noise tolerant and can ground real-world input.
 	+ VSAs use high-dimensional vectors with at least 10,000 dimensions, allowing for big patterns to be expressed in a small vector space.
 	+ The vectors are orthogonal and nearly orthogonal, making them noise tolerant and able to solve the symbol grounding problem.
 	+ VSAs were first implemented using binary spatter code (BSC), which is an algebraic way of combining and operating on high-dimensional vectors.
 	+ VSAs can bundle, edit, clip, and multiply vectors element-wise, allowing for a variety of operations to be performed on the data.
 	+ A dictionary is used to hold and access the hyperdimensional vectors, with cleanup memory being necessary to remove old or irrelevant data.
 	+ An example of using VSAs is shown in the context of robotics, where hyperdimensional vectors are used to represent and query data structures.
 	+ VSAs can be used as a map-like structure, allowing for multiple values to be searched within a fuzzy probabilistic zone.
 	+ Compound values can be created using VSAs, allowing for complex relationships to be represented and queried.
 	+ The challenge of exploring the human brain intersection with VSAs is presented, with the potential for hyperinventional vectors in Lisp operations.
 	+ The concept of merging the intersection of two worlds (deep learning vs symbolic AI) using VSAs is also discussed.

The summary of Carin Meier's talk on Vector Symbolic Architecture (VSA) in Clojure highlights the potential for high-dimensional vectors to be used in various applications, such as data structuring and querying, and the possibility of exploring complex relationships using VSAs. The challenge of merging deep learning and symbolic AI is also presented as a potential area of exploration.


## "Gaining Constant time Lookup over Unorganized Data" - Ghadi Shayban, Jeb Beich

URL: [https://www.youtube.com/watch?v=8XgY1j1etOI](https://www.youtube.com/watch?v=8XgY1j1etOI)

 
- The speaker discusses the importance of leveraging organized data for efficient lookups, using a certificate revocation list (CRL) as an example.
 	+ Organizing data can be done through sorting or using a hash map.
 	+ Hash maps provide constant time access, but they're not well-suited for updating data sets.
 	+ DynamoDB is a database that provides deterministic low latency and can handle large data sets.
 	+ The speaker suggests using a hybrid approach of organizing data once and then using a database like DynamoDB to handle lookups.
- The speaker mentions the challenge of building solutions for specific use cases, which often require expensive custom solutions.
 	+ He proposes identifying the underlying categorical problem and finding a reusable solution that fits various molded use cases.
 	+ An example is creating an experimentation platform for A/B testing with a unique key and sufficient non-membership test.
- The speaker discusses using hash indexes to improve lookup performance, which can be implemented using a closure data structure like Maps or a hash organized tree.
 	+ Hash indexes are not suitable for updating data sets directly, but they can be used to create an index for disconnected data sets.
 	+ The speaker uses the term "logarithmic time" to describe the performance of lookups in a data set with varying size encoding and data type.
- The speaker suggests using a two-part index for data sets, consisting of the actual data set and the associated content.
 	+ This allows for efficient lookup and record retrieval using a primary method like API calls or SPI program calls.
 	+ Custom behavior can be added to the index implementation to handle different data set instantiations.
- The speaker provides examples of use cases requiring specific data set abstractions, such as CRL data sets and customer Shard maps.
 	+ He suggests using an abstraction layer with a SPI (Service Provider Interface) to provide flexibility in handling various data set types.
- The speaker discusses the importance of understanding schema and encoding when working with data sets, using Avro as an example.
 	+ He suggests using a data set abstraction tool to handle different data set implementations and provide indexing capabilities.
 	+ CSV libraries may not support random access or providing line numbers, making it challenging to implement indexing for CSV data sets.
- The speaker emphasizes the importance of designing systems with specific use cases in mind and using appropriate tools and technologies.
 	+ He mentions the cost of two million dollars for an EC2 instance and the potential savings from using a more efficient design.
 	+ The speaker suggests using EFS (Elastic File System) for storing large data sets, which provides sub-microsecond access times and scales well.
 	+ He encourages designing systems to be stateless whenever possible and making the most of container scheduling and orchestration tools like Kubernetes.


## "State of XTDB" by Jon Pither

URL: [https://www.youtube.com/watch?v=gQV-XrkJj2o](https://www.youtube.com/watch?v=gQV-XrkJj2o)

 
- Jon Pither, CEO of Juxt Consultancy, gave a talk on the state of XTDB, a database designed for temporal data.
 	+ He mentioned that XTDB is written in closure and is known for its simplicity and power.
 	+ The talk focused on three main areas: temporal functionality, columnar SQL, and operational improvements.
- Temporal functionality is a key feature of XTDB, allowing users to query data based on timelines.
 	+ Bitemporality is discussed as a way to give control over time insertion.
 	+ The talk also mentioned the challenges of keeping full timeline databases around and the tradeoffs between nonbiotemporal and bitemporal views.
- Columnar SQL is another feature of XTDB, which allows for efficient querying of large datasets.
 	+ The talk discussed the advantages of columnar storage over traditional row storage.
 	+ Apache Arrow is mentioned as a data format specification that can be used with XTDB.
- Operational improvements have been made to XTDB, including checkpointing and operational hardening.
 	+ The talk also discussed the new Core 2 architecture, which has been replaced by a more scalable and flexible design.
 	+ XTDB now supports first-class SQL functionality, with a focus on temporal capability and compatibility with the latest SQL temporal specification.

Jon Pither thanked the Closure Conch community for their feedback and help in developing XTDB. He also mentioned that an Early Access version is available and encouraged people to provide feedback to help harden the product.


## "Fluree: an Immutable, Verifiable, Shareable Database" - Daniel Petranek

URL: [https://www.youtube.com/watch?v=PV4IUuqblig](https://www.youtube.com/watch?v=PV4IUuqblig)

 
- The speaker, Daniel Petranek, discusses the challenges and benefits of sharing data across trust boundaries.
 	+ He proposes using a new data representation called Json LD to simplify schema and improve data interoperability.
 	+ He also suggests using a graph database like Fluree to store and manage the data.
 	+ The goal is to make data sharing more efficient, secure, and cost-effective.
- The speaker mentions that he has been working on this project for about two months and plans to release it soon.
- He encourages people to check out the website, docs, and repo for more information.
 	+ He also thanks Daniel Higginbotham for helping with the project and giving feedback.
 	+ The speaker has a booth at Closure Camp and is willing to help people learn about the technology in a fun and friendly way.


## "How to Find the Write Rhythm for your Software Composition" by Jordan Miller and Heather Haylett

URL: [https://www.youtube.com/watch?v=_beZ07o91rg](https://www.youtube.com/watch?v=_beZ07o91rg)

 
- The speakers are Jordan Miller and Heather Haylett.
- They discuss the importance of finding the right rhythm for a software composition.
- A good rhythm can help create a shared understanding among team members.
- Documentation should provide context at different levels: outer message, inner message, and closure.
- Closure is an abstraction that helps humans understand code.
- The speakers advocate for using a consistent structure in documentation, like the diataxis model.
- They mention the importance of considering both conventional and bespoke organization in documentation.
- A good documentation strategy can help improve PR reviews and reduce friction within a team.
- The speakers suggest starting with a readme file and prioritizing code readability.
- They recommend creating a shared frame or context for the team to work towards.
- The speakers mention the role models of well-documented open source projects.
- They discuss the importance of organizing code and documentation for different types of projects.
- The speakers highlight the need to balance complexity with readability in documentation and code.
- They recommend using a consistent structure, like the diataxis model, to help readers understand the code base.
- A good documentation strategy can help teams work more efficiently and reduce friction.


## "High Performance Clojure" by Chris Nuernberger

URL: [https://www.youtube.com/watch?v=ralZ4j_ruVg](https://www.youtube.com/watch?v=ralZ4j_ruVg)

 
- The speaker, Chris Nuernberger, discussed high performance Clojure and its optimization techniques.
- He mentioned the importance of understanding the CSV and JSON parsing in Clojure.
- The speaker found a significant performance issue with CSV libraries and implemented a faster method using a canonicalizing map.
- He also talked about the Eden reader, a high-performance Lisp reader, and its benefits.
- The speaker compared various data structures, such as hash tables and bitmap trees, in terms of performance.
- He discussed the importance of reducing computational complexity and optimizing algorithms.
- The speaker mentioned his experience with the Futhark programming language, which is designed for high-performance parallel computing.
- He also talked about the Monte Carlo simulation method and its use in probabilistic programming.


## "Consequential Clojure Architectures" by Janet Carr

URL: [https://www.youtube.com/watch?v=vf1GLAeT6V4](https://www.youtube.com/watch?v=vf1GLAeT6V4)

 
- Speaker's name: Janet Carr
- Occupation: Independent closure consultant
- Experience: Professional experience in DevOps, SRE, and software engineering
- Blogs and tweets about architecture design and closure
- Talks about consequential closure architecture and negative impacts
- Antipatterns in closure-based system design
  - Single namespace problem: information overload and reluctance to find functions
  - Haphazard Handler locality problem: trying to solve locality business logic with APIs and input systems
  - Wishful typing problem: trying to use statically typed programming languages for closure
  - Relational mapping inversion control DB: using a protocol for record protocol can create rigidity
- Proposal for software architecture patterns: Model View Controller (MVC) and the Gang of Four design pattern
  - MVC: decouples state, state change, and state usage using strategy and observer patterns
  - Gang of Four design pattern: achieves separation of concern and allows for easy addition of new watch functions
- Porcelain adapter architecture (Hexagonal architecture): decouples input business logic and output, promoting good mocking dependency testing
  - Driving adapter wraps external libraries or services, while driven adapter wraps application logic core APIs
- Ports adapter architecture: promotes reusable components called bricks and organizes them in a component base workspace
  - Four domains: domain, technical, application logic, and API layer
- Strangler pattern: helps transition to microservices by decoupling dependencies and making software web scale
  - Favor closure for many small code bases in microservices architecture


## "Unmanned Systems Flight Planning with Clojure" by Heow Goodman

URL: [https://www.youtube.com/watch?v=5-IZeGphlhc](https://www.youtube.com/watch?v=5-IZeGphlhc)

 
- Speaker: Hugh Goodman, full stack engineer at ATA
  - Topic: Unmanned Systems Flight Planning with Clojure
  - Goal: Create a software solution for managing and planning flights of unmanned systems
  - Challenges:
    - Different types of hazards to consider (oncoming aircraft, train derailments, hazardous chemical spills)
    - Various rules and regulations from different levels of government (federal, local, state)
    - Integrating data from multiple sources (GIS systems, FAA UAS system, foreign systems)
  - Solution: Airdex Authority, a software platform designed to collect, disseminate, and administer information for public safety and emergency services
  - Features:
    - Real-time advisories based on various data sources
    - Collision detection and prevention
    - Restricted and unrestricted information access
    - User interface for creating and managing advisories
  - Technology Stack:
    - Clojure (for its robustness, simplicity, and consistency)
    - Reagent and Reframe (for building single-page apps and reusing code)
    - Polyleth (for composable blocks of code)
    - Babashka (for development patterns and build automation)
  - Benefits:
    - Allows for quick, simple, and consistent code structure
    - Enables code reuse across different projects and services
    - Simplifies error handling and debugging
    - Accommodates nontrivial problems and complex data structures
  - Use Cases:
    - Public safety and emergency services
    - Aircraft manufacturers and FAA
    - NASA


## "Architecting systems through Engineering Principles" by Bruno Tavares

URL: [https://www.youtube.com/watch?v=WMlPT3ELP9s](https://www.youtube.com/watch?v=WMlPT3ELP9s)

 
- Bruno Tavares presented "Architecting systems through Engineering Principles" at newbank.
- He discussed the Cold Organization Principle and its application in code organization and architecture.
- The presentation aimed to help people understand and write idiomatic code that fits within a system's norms and expectations.
- Tavares emphasized the importance of clear definitions, feedback, and nurturing a growth mindset in a microservice architecture.
- He also shared lessons learned from building systems at newbank, such as the value of consistent syntax, design patterns, and architectural principles.
- The presentation included examples of data set expectations, backfilling information, and the importance of a consistent approach to change management.


## "Operating Datomic at Scale" by João Palharini and Filipe Andrade

URL: [https://www.youtube.com/watch?v=bvEsnJiCs7E](https://www.youtube.com/watch?v=bvEsnJiCs7E)

 
- João Palharini and Filipe Andrade presented on operating Datomic at scale.
- They work for the atomic team, which moved to Datomic eight months ago.
- The presentation focused on tuning techniques and troubleshooting performance issues.
- A key problem they addressed was optimizing query execution for large databases with many customers.
- They discussed how to interpret and adjust queries, focusing on ordering clauses and removing unnecessary memory consumption and computation.
- They also covered caching strategies, transaction management, and using various APIs to optimize performance.
- The presentation included examples of using iostats, caching setup, and documentation to measure and improve performance.
- The speakers shared their experience with indexing and storage, emphasizing the importance of indexing performance and memory usage.
- They provided tips for tuning, such as adjusting GC settings and increasing CPUs to handle more parallel work.
- The presentation concluded with a summary of how Datomic can improve transaction throughput and lower latency.


## "Clojure in the Fintech Ecosystem" by Philip Cooper

URL: [https://www.youtube.com/watch?v=QCxcLsxQeYs](https://www.youtube.com/watch?v=QCxcLsxQeYs)

 
- Presenter's past experience:
  - Worked with Python, numpy, and panda for data analysis in finance.
  - Used Fortran 4 in college, but didn't like it.
  - Began investment management career in the early 2000s.
  - Started using Python again in 2019 due to APL-like features and ecosystem.
  - Has been involved with a large bank project since then.
- Presenter's interest in Scala, Clojure, and other languages.
- Presenter's experience with financial data analysis:
  - Works with stock, bond, and loan data.
  - Deals with dirty, noisy, and obfuscated data.
  - Uses XML libraries for data storage and retrieval.
- Presenter's use of Datomic for scalability and reproducibility in financial analysis:
  - Impressed by Datomic's ability to handle 80 million customer credit card records.
  - Prefers Datomic's self-healing and logging features over traditional databases.
- Presenter's experience with web frameworks:
  - Familiar with Ruby on Rails, Django, and ClojureScript.
  - Preferring Ring Interceptor pattern for routing and database integration.
- Presenter's use of npm packages and React for frontend development:
  - Impressed by the quality and features of Blueprintjs AG Grid.
  - Uses Helix for frontend development, which provides a "last mile" solution.
- Presenter's recommendation for data science tools:
  - Encourages using Python, numpy, and panda for data analysis in finance.
  - Prefers Clojure for its immutable data structures and community support.
- Presenter's use of GitHub and other resources:
  - Follows Chris Nuremberg's talk on Lib Python Clj and Chris Read Buffer.
  - Uses Specter, Exoscale, and Plumatic Graph for data pipeline processing.
- Presenter's use of tooling and infrastructure:
  - Finds tech radar useful for finding the best practices and libraries.
  - Uses Jupyter Notebook and PyCharm for Python development.


## "Four years of Datomic powered ETL in anger with CANDEL" by Ben Kamphaus and Marshall Thompson

URL: [https://www.youtube.com/watch?v=2nIfNxZZhiQ](https://www.youtube.com/watch?v=2nIfNxZZhiQ)

 
- Four years of Datomic powered ETL in anger with CANDEL
- Benefits of using a unified data platform for managing and analyzing data from different sources
- Overview of the Candle ecosystem, including raw sugar, a tool for handling raw data files, and Mantis, a tool for multi-dimensional analysis
- Importance of having a schema that can handle nontrivial relationships and evolving data models
- Challenges in building a system to manage and analyze large and complex datasets
- Use of R tools and visual query builder interface to help scientists build queries
- Need for unified set of processes, validation, and data ingestion analysis
- Example of using Candle in a multiomic profiling study in a clinical trial
- Importance of data harmonization and cleaning in data science workflows
- Use of atomic databases and version control to manage schema changes and handle conflicts


## "How to build a Clojure dialect" by Jeaye Wilkerson

URL: [https://www.youtube.com/watch?v=Yw4IAY4Nx_o](https://www.youtube.com/watch?v=Yw4IAY4Nx_o)

 
- The speaker, Jay Wilkerson, is discussing the process of building a Clojure dialect called Jank.
  - He started working on Jank in 2015 and has been refining it since then.
  - Jank is built on top of C++, C+++, Objective-C, Rust, and LLVM/libc++.
  - The speaker has considered using a tokenizer but decided to write his own regex-based lexer instead.
  - He is struggling with semantic analysis and generating code from the parse tree.
  - Jank's compiler integrates its runtime, which generates code as needed.
  - The speaker has been inspired by Rich Hickey's work on Clojure and is trying to implement a macro system similar to Clojure's.
  - He is also considering adding support for socket programming and interop with Java and JavaScript.
  - The speaker acknowledges the complexity of implementing a closure dialect and the need to figure out how to handle metadata and interop.
  - He plans to implement an object model and class hierarchy in Jank, which will be based on existing Java classes.
  - The speaker is also considering adding support for packed arguments and variadic calls.
  - He is looking for ways to make the closure core more compact and easier to use.
  - The speaker hopes that Jank can be used as a library in C++ applications and as an embedded language in existing applications.
  - He is considering adding support for software transactional memory, linting, editor support, and other features.
  - The speaker acknowledges the challenges of building a closure dialect and the need to get community feedback and support.

(Please note that this summary is based on the provided transcript and may not capture all the nuances or subtleties of the original talk.)


## "Modern Frontend on ClojureScript and React in 2023" by Yuri Khmelevsky

URL: [https://www.youtube.com/watch?v=lvsAqVIeRAQ](https://www.youtube.com/watch?v=lvsAqVIeRAQ)

 
- Presenter is discussing building a UI kit and frontend application using ClojureScript and React.
	* Used design system UI kit for consistency and efficiency.
	* Utilized Figma API to fetch color, typography, and shadow data.
	* Used SVG for icons, automating the process with a script.
	* Implemented a macro to create react components more easily.
	* Organized components into categories and subcategories, with documentation and themes.
- Presenter also discussed building a backend component:
	* Used Helix library for its close React API.
	* Utilized Emotion library for CSS-in-JS styling.
	* Implemented reagent library for building react components.
	* Used preagent to optimize the build process.
	* Discussed using SWR hook and react suspense for data fetching.
- Presenter highlighted the importance of fast refresh, developer experience, and efficient rendering.
- Presented an example of a UI kit built with ClojureScript and React:
	* 600 components in the UI kit.
	* 130 components built for the application.
	* Fast refresh and performance are good.
	* Router and state management are implemented using react context.
- Presented an example of building a solid design system:
	* Used reframe to organize global state.
	* Implemented atomic principles for react context.
	* Discussed migrating from react context to atomics.
	* Highlighted benefits of using Shadowcljs, such as code sharing and lazy loading.
- Presenter concluded by praising ClojureScript's frontend capabilities:
	* Shareable code between frontend and backend.
	* Incredible UI performance.
	* Solid developer experience and excellent performance.


## "Joyful Cross platform Development with ClojureDart" by Christophe Grand and Baptiste Dupuch

URL: [https://www.youtube.com/watch?v=wbUBb09bUnk](https://www.youtube.com/watch?v=wbUBb09bUnk)

 
- The speakers introduce themselves and the subject of their talk, "Joyful Cross Platform Development with ClojureDart".
- They mention that they have been working on ClojureDart for over two years.
- The speakers show a slideshow containing code examples in both Clojure and Dart.
- They discuss the benefits of using ClojureDart, including its simplicity and ease of use.
- The speakers demonstrate how to create a basic UI application using Flutter and ClojureDart.
- They show how to create a todo list application with checkboxes and navigation features.
- The speakers discuss the importance of listening for changes in application state and updating the UI accordingly.
- They mention some challenges they encountered while developing with ClojureDart, such as dealing with global state and creating custom widgets.
- The speakers show how to use Flutter's build system to create a cross-platform application that runs on iOS, Android, and the web.
- They discuss the importance of testing and debugging when developing with ClojureDart.
- The speakers mention some resources for learning more about ClojureDart and Flutter.


## "Growing Data Center networking mgmt UI using ClojureScript, Reagent and re-frame" by Kirill Ishanov

URL: [https://www.youtube.com/watch?v=pTyYH5t1fFo](https://www.youtube.com/watch?v=pTyYH5t1fFo)

 
- The presentation discusses a large application built in the networking domain, with a UI that fetches data from multiple sources and displays it in a single page.
- The application has around 800 API endpoints and almost 400 unique UI screens.
- Data visualization is an important aspect of the application, which led to the creation of Reagent and Reframe frameworks.
- The presentation also touches on the challenges faced during development, such as scalability, data modeling, and integration with existing systems.
- The team had to learn best practices from the industry and adopt a more structured approach over time.
- The application has been integrated with Juniper Networks' internal systems since its acquisition, which brought new challenges related to customer support and documentation.
- The presentation ends with lessons learned during the journey of building and scaling the application.


## "Clojure lsp – One tool to lint them all" by Eric Dallo

URL: [https://www.youtube.com/watch?v=nxcNrjKL2WA](https://www.youtube.com/watch?v=nxcNrjKL2WA)

 
- Speaker introduced himself and his background in software engineering.
  - He discussed the challenges of managing linkers across different projects in a large company.
  - The speaker highlighted the importance of standardization in configuration management.
  - He introduced LSP (Language Server Protocol) as a solution to these problems.
  - LSP is an open-source project that provides a standard for language servers to follow.
  - The speaker encouraged contributing to and sponsoring LSP development.
  - He also mentioned the use of Clojure LSP in the company's projects.
  - The speaker discussed the importance of code style, class path, and analysis in project management.
  - He introduced the concept of a dump feature for analyzing project dependencies.
  - The speaker mentioned the use of external libraries and tools like babashka and pod.
  - He emphasized the importance of exportable configuration features for easier management.
  - The speaker provided examples of macro usage and the need for proper configuration.
  - He discussed the use of Code style and code lanes to improve code quality.
  - The speaker mentioned the importance of handling specific problems in large code bases.
  - He introduced the concept of custom linkers and their impact on configuration management.


## "Real @toms with Clojure!" by Thomas Clark and Daniel Slutsky

URL: [https://www.youtube.com/watch?v=SE5Ge4QP4oY](https://www.youtube.com/watch?v=SE5Ge4QP4oY)

 
- Thomas Clark and Daniel Slutsky presented on using Clojure for scientific programming.
- They discussed the benefits of simplicity, abstraction, and a functional approach in Clojure.
- The talk focused on a project involving laser light and atomic physics.
- They demonstrated how to use Clojure for data analysis, visualization, and experimentation.
- Thomas Clark mentioned the EIT (Electromagnetically Induced Transparency) effect and sculpting shadows with magnetic fields.
- Daniel Slutsky discussed workflow, tooling, and the importance of a namespace notebook in scientific programming.
- The speakers emphasized the value of collaboration, community building, and peer review in scientific research.


## "Comparing protein structures with Clojure" by Blaine Mooers

URL: [https://www.youtube.com/watch?v=vt594qgAc1I](https://www.youtube.com/watch?v=vt594qgAc1I)

 
- Speaker introduces the topic of comparing protein structures using Clojure and the Cyclose community's study group.
    - They discuss their experience working on a textbook Bayesian data analysis process.
    - A protein bioinformatics problem is presented as an example, focusing on overlaying protein structure comparison.
- The speaker provides a basic introduction to protein structure, using simple cartoons and ribbon diagrams.
- Two methods for comparing protein structures are presented: a principal method and a test hypothesis protein structure comparison.
    - An example of a predicted protein structure from artificial intelligence (Alpha fold) is compared to an experimental structure.
- The speaker introduces probabilistic programming, using Python libraries like Dash, clj, and pi MC, to model protein structures.
- The speaker demonstrates the use of enclosure and lib python to create a protein polymer model.
    - Amino acids are represented by different colors: blue for polar and green for nonpolar.
- The speaker explains how the shape of a protein determines its function, using an example of a protein involved in cell growth and tumor development.
- The workflow for comparing protein structures is presented, including crystal preparation, data collection, and electron density map generation.
    - Crystal properties are discussed, such as size, shape, and the importance of rapid cooling.
- The speaker highlights the use of national facilities for high-intensity X-ray diffraction experiments.
- The importance of the Protein Data Bank is emphasized, with over 200,000 protein structures available.
- The speaker discusses the development of cryo methods and their impact on experimental accuracy.
    - They mention a shift from in-house to national facilities for data collection.
- The speaker introduces C Alpha Trace, a molecular representation used for comparing overlay structure.
- The speaker uses conventional and probabilistic programming approaches to superimpose two protein structures.
    - They discuss the assumption of equal variance position along the polypeptide chain in the conventional approach.
- The speaker introduces the Theseus program and the Theseus PP method, which use a probabilistic programming approach.
    - They demonstrate the improvement of the Theseus PP method compared to the conventional approach.
- The speaker discusses the application of the probabilistic programming approach using NMR data and nuclear magnetic resonance techniques.
- The speaker presents an example of superimposing two protein structures, using the Theseus PP method and a NMR technique.
    - They highlight the importance of long-distance information and the challenge of constraining overall shape.
- The speaker discusses the use of Hamiltonian Monte Carlo (HMC) and the Metropolis Hastings algorithm in probabilistic programming.
    - They compare the performance of these methods using probability distribution plots.
- The speaker concludes by thanking the Cyclose community for their collaboration and discussing future directions, including the potential use of deep learning approaches.


## "BI and Reporting for Datomic" by Arne Brasseur

URL: [https://www.youtube.com/watch?v=w9RO8Qb8m8g](https://www.youtube.com/watch?v=w9RO8Qb8m8g)

 
- The speaker introduced the topic of Atomic, a project they've worked on.
	+ Atomic is a cloud-based accounting software built using closure script and database.
	+ It aims to provide business intelligence features, allowing users to get insights from data and make informed decisions.
	+ The speaker mentioned two use cases for Atomic: prebuilt dashboards and self-service querying.
- The speaker discussed the challenges of integrating Atomic with various databases, including PostgreSQL, Google BigQuery, and Google Sheets.
- They introduced embedkit, an open-source project that simplifies integration with Metabase.
	+ It provides a single Eden data structure for storing user logins, query results, and dashboards.
	+ Embedkit can save time by reusing existing dashboards and reducing the need for manual administration.
- The speaker mentioned a potential use case for embedkit in SaaS products that want to offer nicer visualizations.
- They introduced Metabase, an open-source business intelligence tool built using closure script.
	+ It supports various data sources and allows users to create prebuilt dashboards or perform self-service querying.
	+ The speaker mentioned the importance of having a robot named Melvin for automating user management tasks.
- The speaker discussed the challenges of connecting Atomic to Metabase using the driver architecture in Metabase.
	+ They created a custom driver for Atomic using multimethods and resolved data source configuration issues.
- The speaker mentioned the performance benefits of using Atomic's native query format compared to SQL.
- They discussed the potential for Atomic Analytics to use Presto as a SQL engine, which has its own driver and metadata file-based membership attribute.
	+ Presto is an open-source distributed SQL database that can handle large datasets.
	+ The speaker mentioned that Atomic Analytics was based on Presto until it was renamed to Trino in 2019.
	+ They noted that there has been less activity around Atomic Analytics and Trino recently, and they are unsure of future developments.
- The speaker discussed the challenges of optimizing performance in Atomic Analytics when dealing with wide tables and complex queries.
	+ They suggested a simple idea for improving performance by using Atomic's transaction log to process schema changes and data changes.
	+ This approach would require postgres to create a transaction table and an idents table, among other modifications.
- The speaker mentioned that Atomic Analytics currently uses PostgreSQL as its database, which is not typically used for analytics workloads.
	+ They suggested using column store databases like Snowflake for better performance in analytics workloads.
	+ The speaker noted the differences between OLTP and OLAP workloads and the benefits of using different databases for each type of workload.
	+ They mentioned that PostgreSQL is a versatile database that can handle various use cases adequately.
- The speaker concluded by mentioning the importance of understanding SQL dialects, data types, and equivalents when working with different databases.


## "Clojure for Data Science in the Real World" by Kira McLean

URL: [https://www.youtube.com/watch?v=MguatDl5u2Q](https://www.youtube.com/watch?v=MguatDl5u2Q)

 
- The presentation focuses on Clojure for Data Science, with a specific emphasis on its use in the real world.
- Kira McLean, a software engineer at TPX Impact, is the presenter.
- Clojure is a functional programming language that is well-suited for data science tasks.
- The presentation covers various aspects of using Clojure for data science, including its ease of use, interoperability with other languages, and its suitability for reproducible analytical pipelines.
- The presenter highlights the stability and reproducibility benefits of using a functional programming language like Clojure in data science.
- The presentation also discusses the challenges of data science, such as the need for stable and reproducible code, and how Clojure can help mitigate these issues.
- The presenter emphasizes the importance of learnability, discoverability, and polish in the Clojure ecosystem.
- There is a push to integrate Clojure more closely with popular data science tools and workflows.
- The presentation also discusses the potential for tighter integration between Clojure libraries and existing data science ecosystems.
- The presenter highlights the potential of Clojure to make working with data feel familiar and ergonomic for data scientists.
- The presentation concludes by discussing various ways to get involved in the Clojure community, such as contributing to open source projects, attending meetups, and participating in study groups.


## "How to transfer Clojure goodness to other languages" by Elango Cheran and Timothy Pratley

URL: [https://www.youtube.com/watch?v=terdLf0ribg](https://www.youtube.com/watch?v=terdLf0ribg)

 
- Elango Cheran and Timothy Pratley discussed their project, Kalei, which transpiles code from various languages to Rust or Java.
- They mentioned the challenges of handling different syntax, semantics, and mutation between languages.
- The goal of Kalei is to provide a simple, efficient, and flexible solution for transpiling code while preserving its intended meaning.
- They also talked about the importance of immutability, persistent data structures, and type inference in their design.
- Elango shared his experience working with Scala and building a time series database, which led him to adopt Rust and create Kalei.


## "Emmy: Moldable Physics and Lispy Microworlds" by Sam Ritchie

URL: [https://www.youtube.com/watch?v=B9kqD8vBuwU](https://www.youtube.com/watch?v=B9kqD8vBuwU)

 
- The speaker has written a textbook and created a project called Emmy, which is a library for running physics simulations.
- The library uses a build system to integrate equations into the codebase and provides data structure libraries and a notebook environment for working with physics simulations.
- The library was inspired by Sussman's scheme library, which contains a full general relativity implementation written in scheme.
- The speaker has created a web browser-based environment for developing and testing Emmy using Clerk, a closure library that watches the namespace for changes.
- The library includes features such as a D operator for taking derivatives and a Taylor series expansion function.
- The speaker is working on improving the performance of the library and making it more accessible to non-experts.


## "Working With the Machine – A Maker’s Journey into Clojure" by Adam Vermeer

URL: [https://www.youtube.com/watch?v=R_CSO8v1ELs](https://www.youtube.com/watch?v=R_CSO8v1ELs)

 
- Adam Vermeer talks about his journey from a maker to a programmer.
  - He started as a mechanical engineer and learned CAD software like SolidWorks, AutoCAD, and Inventor.
  - He discovered the concept of programmatic CAD and found it compelling.
  - He used Python and open-source libraries to create a 3D model of a chess set and a squat rack.
  - He also helped his brother make a chess set using laser cut parts.
  - During the pandemic, he started working on a portable hydroponic system prototype.
  - He learned about functional programming and open-sourced his code.
  - He started using Emacs and Htmlx for web development and created a solenoid web app prototype.
  - He is currently working on a quilt design tool and a generative art tool using SVG.



## Composing All The Things with Kotlin Multiplatform • Garth Gilmour • GOTO 2023

URL: [https://www.youtube.com/watch?v=iq2tTtG3zs4](https://www.youtube.com/watch?v=iq2tTtG3zs4)

 1. SC Gilmore, a developer advocate at JetBrains, discusses Compose Multiplatform.
2. A framework for creating awesome user interfaces across multiple platforms, built on Kotlin Multiplatform and powered by Google's Jetpack Compose.
3. Supports sharing code across different platforms, simplifying cross-platform projects.
4. iOS support is in Alpha stage with an example using the ImageViewer application.
5. Demos showcasing Compose Multiplatform usage for various tasks.
6. Cotland Multiplatform: A framework with multiple compilers for different platforms.
7. Composed Multiplatform: Built on top of Cotland, allows sharing code across platforms.
8. Ecosystem of libraries for various tasks.
9. Creating UI in Compose using a declarative approach with composable functions.
10. Demos showcasing basic button counter, performance optimization, text input, and microservice integration.
11. Composable functions allow efficient UI rendering by avoiding unnecessary recomposition.
12. View models separate state and event handlers from the UI.
13. State can be derived in composable functions using other states.
14. Private observable state can be modified within event handlers.
15. Composable UI can be used on Android, iOS, and desktop with minimal changes.
16. Multiplatform libraries handle networking, marshalling, and concurrency.
17. Co-routines manage jobs of work and cancel them when needed.
18. State management is done using a single state object for the UI.
19. Compos offers incremental learning, supports multiple platforms, and leverages Kotlin ecosystem.
20. Allows developers to choose their approach based on specific needs.
21. Offers concurrency via co-routines, making it easier to handle user interface events.
22. State management is done using a single state object for the UI.


## The Reflex Architecture • Ben Kolera • YOW! 2019

URL: [https://www.youtube.com/watch?v=5ACqm2ee-XI](https://www.youtube.com/watch?v=5ACqm2ee-XI)

 - Reflex is an FP library with Dom framework, Platform, and Obelis.
- Functional Programming (FP) focuses on dynamic values based on events.
- Dynamic values change over time in response to events.
- Reducer functions handle event and state for new states.
- Reflex uses fold D to manage dynamic values.
- Event Rider is an analog of dispatchers, allowing reusable widgets.
- Widgets are components with specific constraints, building DOM elements and emitting events.
- Reflex centralizes state and simplifies UI development.
- Monad Reader adds time-varying values to context for complex UI behavior.
- Reflex focuses on composable and reusable widgets without a magic store like Redux or Relay.
- Conduit app demonstrates real-world usage of Reflex.
- A functioning Nyx Obelisk environment is required for the workshop.
- Virtual Box setup instructions are provided in the program.


## Scodec for Scala 3 • Michael Pilquist • YOW! 2020

URL: [https://www.youtube.com/watch?v=Uo9S4iKw8NA](https://www.youtube.com/watch?v=Uo9S4iKw8NA)

 1. Sodc is a library for binary processing.
2. Scala 3 macro system revamp: less powerful but more stable.
3. Macro implementation example: hex string literal interpolation.
4. Inline keyword in Scala 3: code gets inlined at call site.
5. Extension method syntax used to support hex followed by a string.
6. Compile time validation via unlift operation.
7. Sodc library transition from Scala 2 to Scala 3 focuses on source and binary compatibility, simplifying established libraries.
8. Introducing the Scy 2 macro system and its impact on library authors.
9. Using Scala 3's inline keyword for compile time execution.
10. Implementing a hex string literal support using custom numeric literals.
11. Sodec at core project: building codecs with simple algebra and combinators.
12. Comparison of three methods to generate nested tuples in Sodec for Scala 2.
13. Using heterogeneous lists from Shapeless directly in the API of the library.
14. Scola 3 introduces new ways to handle codecs and tuples.
15. Tuple arity can be abstracted, allowing generic code that preserves tuple size.
16. Cons operator is right associative in Scala 3.
17. Two generic operations are needed: one for consing a codec of A onto B (Tuple) and another for consing any two arbitrary codics.
18. Extension methods are used to implement these operations, ensuring they're always in implicit scope.
19. Implementation of codic operations in Scola 3 using extension methods.
20. Extension methods for consing two arbitrary types A and B, ensuring right associativity.
21. Simple extensions not used due to issues with eraser and implicit scope.
22. Drop units operation removes unit values from a codec, returning a smaller tupal or the same tupal if no units were present.
23. Match type feature in Scola 3 allows defining type functions at the type level.
24. Implementation: Recursive pattern matching on Tuple structure, removing unit values from the head or tail.
25. Inline definitions: Used to perform these operations at compilation time.
26. Converting codecs: Mapping between Tuple and case class structures using Scala 3's syntax and implicit functions.
27. Compile-time meta programming: Using Scholar.deriving package for reflection and generic programming against product and sum types.
28. Scala 3's type class derivation allows generating coherent codec instances.
29. Derives keyword can be used to derive a single canonical instance for a given type class.
30. Implement derived method in the companion object of the target type class.
31. Require compiler to give a mirror of whatever is being derived.
32. Three abstract methods need implementation: encode, decode, and codecError.
33. Use Scala 3's new syntax for enumerations and adts.
34. Introducing a codec for enumerations in Scala 3.
35. Deriving a codec for ADTs with arbitrary complexity.
36. SizeBound method implementation: Product case - Sum the binary sizes of each element type; Sum case - Use an unsigned 8bit integer to select the Su type member and encode it, followed by the encoded data.
37. Scola 3 compatibility with Scala 2 libraries (no macros).
38. Cats Effect 3 and FS2 support for Dy.
39. Simplified implementation and use of Scala 3.
40. Easier maintenance, less dependencies, and better readability compared to previous approaches.
41. Improving compatibility between Scala 2 and Scala 3.
42. Bidirectional cross-compatibility with no macro usage in Scala 2.
43. Open source ecosystem porting libraries for Scala 3.
44. Encouragement to try Scala 3 and seek help from the community.


## Jakarta EE 10: Modern & Lightweight Cloud Application Development • Ivar Grimstad • GOTO 2023

URL: [https://www.youtube.com/watch?v=2749IF7gAbI](https://www.youtube.com/watch?v=2749IF7gAbI)

 1. Jakar E10 is a comprehensive platform with various specifications and APIs.
2. New core profile targets microservices or headless services, similar to the web profile for traditional web applications.
3. Security updates include standardized OpenID Connect support in Jakar applications.
4. Persistence minor update adds UIDs as basic Java types, simplifying usage.
5. Jakar Restful API 3.1 allows Java SE bootstrapping without an application server.
6. Demonstration of a Jakarta application using S bootstrap for simple web services.
7. Core profile aims to improve runtime performance and compatibility with smaller runtimes.
8. CDI light is designed for restricted environments, resolving dynamic features at build time.
9. Migration from Java EE to Jakarta: Transformation tools can automatically update code without touching it.
10. Demo application showcases a complete Duke application with database, repository, business service layer, and REST API using JSON binding.
11. Upgrade to Jakarta EE by using migration tools like Apache TomEE and Eclipse Transformer.
12. Fix Imports, XML schema namespaces, and property files with changes from Java X to Jakarta.
13. Check for any other Java X dependencies and update them accordingly.
14. Ensure proper bootstrapping files are renamed if needed (e.g., Java X Enterprise Inject SBI extension).
15. Test the updated application and fix any issues that arise.
16. Update XML configurations to persistent XML.
17. Change properties files for Java X to Jakarta.
18. Check for CDI extensions and rename bootstrapping files.
19. Verify dynamic data in applications and update if needed.
20. Upgrade application versions by changing version numbers and fixing compilation errors.
21. Use a trick to make JSON binding work with records.
22. In 10, the issue with getters and setters is fixed, so no coding changes are required for this specific case.
23. Demonstrated a system where a B XML file is required for CDI activation in Spring.
24. Showcased a simple Spring application with dependencies and validation.
25. Upgraded the application to Spring 3, resulting in compilation issues due to missing symbols.
26. Updated the JPA persistence API and Jakar validation versions to fix the issue.
27. Compiled the Spring Boot application successfully after dependency version updates.
1. Upgrade to newer versions of dependencies and frameworks for better compatibility.
2. Use Eclipse Transformer to update libraries with new Jakarta namespace.
3. Publish updated libraries in Maven repository for use in projects.
4. Follow a two-year release cadence for Jakarta, with Java SE LTS version as the base.
5. Discussions on MVC and NoSQL integration are ongoing; contribute if interested.
6. RPC is not likely to be included in Jakarta.
7. Oracle contributes code to RPC project but needs more contributors to move forward.
8. Hope for Jakarta Data, even without NoSQL, to provide data management capabilities.
9. Jakarta release cadence: 6 months after Java SE LTS version
10. Jakarta 11 based on Java 17 or 21 (depending on APIs)
11. Jakarta 11 runtime will be Java SE 21
12. MVC and NoSQL for discussion, but not confirmed for inclusion in Jakarta EE
13. Jakarta RPC not included, join the project if interested
14. Jakarta Data hoped to be included, input needed on repository pattern vs active record
15. Jakarta 9 focused on namespace, 10 added new specifications and bridged 11 and 17
16. Resources: Jakarta website, starter, LinkedIn course (with QR code)


## Concurrency Abstractions for Application Security • Bram Verburg • GOTO 2023

URL: [https://www.youtube.com/watch?v=snCylAGgcxw](https://www.youtube.com/watch?v=snCylAGgcxw)

 - Memory management evolution: From explicit allocation to automatic memory management with garbage collection.
- Concurrency: Dealing with parallelism and asynchronous interactions within an application.
- Automatic concurrency management: Pushing responsibilities into the runtime, providing abstractions for developers.
- Language impact: Functional programming languages often have immutable data structures and pattern matching for message handling.
- Runtime support: Green threads, schedulers, isolated processes with no shared state.
- Automatic concurrency management aims to simplify development by providing abstractions and runtime support.
- Immutable data, isolated processes, and resilience can lead to better security through integrity, confidentiality, and availability.
- The actor model with lightweight green threads helps ensure integrity by making state changes explicit and transactional.
- Confidentiality is improved by shortlived processes with dedicated scopes that limit access to relevant data.
- Resilience provides fault tolerance by allowing for process monitoring and recovery from failures.
- Clarity: Focus on the happy path and avoid handling errors that shouldn't occur.
- Simplicity: Keep code simple to minimize risk of bugs and make it easier for future developers.
- Functional programming: Consider using pure functions for testing purposes as they are easy to test due to their predictable behavior.
- Separate runtime or language for full benefits of concurrency abstractions.
- Airong (Elixir, Erlang) has actor model, lightweight threads, non-blocking IO, and OTP principles.
- Security features like isolation, access controls, code signing, static typing can be improved.
- Other languages like Go have some of the features but not all.
- Discusses the need for better security, integrity, and isolation in applications.
- Mentions various languages and frameworks that address some of these issues but lack complete solutions.
- Encourages awareness and collaboration among developers to improve concurrency and security.


## Genetic Algorithms in Elixir • Sean Moriarity & Bruce Tate • GOTO 2023

URL: [https://www.youtube.com/watch?v=vS1_Z4xaeqQ](https://www.youtube.com/watch?v=vS1_Z4xaeqQ)

 1. Bruce Tate interviews Sean Moriarity, creator of Axon and co-creator of Nx projects.
2. Axon focuses on machine learning in Elixir with competitive performance to Python ecosystem.
3. Nx (Numerical Elixir) is the foundation for the Elixir machine learning ecosystem, providing numerical routines and automatic differentiation.
4. Defn allows for numerical functions in Elixir, similar to JAX's just-in-time compilation behavior.
5. Axon is an Elixir library for creating and training neural networks, inspired by Keras, TensorFlow, and PyTorch.
6. The Elixir ecosystem benefits from the slow and careful approach of building these libraries on top of functional programming languages.
7. Nx and Axon aim to make machine learning more accessible and maintainable while leveraging the strengths of their underlying language.
8. Nx Serving provides an efficient serving abstraction that supports distribution, fault tolerance, and good concurrency.
9. The combination of Elixir's strengths with machine learning capabilities creates exciting opportunities in the ecosystem.
10. Bumblebee library interoperates with Python ecosystem, allowing use of pre-trained models in Elixir applications.
11. ONNX support enables running ONNX models with Nx abstractions.
12. Low code requirements make machine learning accessible to non-experts.
13. Elixir's concurrency and robustness make it potentially better for machine learning than other languages.
14. Elixir ecosystem lacks machine learning experience, but Bumblebee provides easy access.
15. Abstractions in the Elixir ecosystem are good for building robust and concurrent applications.
16. Immutability helps with reasoning about complex data pipelines.
17. Nx's JIT compilation overcomes immutability issues.
18. Initial challenges included GPU compilation, autograd implementation, and numerical correctness issues.
19. Elixir's versatility makes it ideal for machine learning startups as it handles the entire pipeline from application development to model training and deployment.
20. A new book, "Machine Learning in Elixir," teaches the fundamentals of the ML ecosystem in Elixir. The speaker encourages listeners to check out the book and report any issues found during beta testing.


## Problem Solving with Erlang & the BEAM • Robert Virding & Francesco Cesarini • GOTO 2023

URL: [https://www.youtube.com/watch?v=I7A5Y5wHDHI](https://www.youtube.com/watch?v=I7A5Y5wHDHI)

 1. Erlang, a programming language and ecosystem, was developed for telecom applications.
2. Ericsson used Erlang in their products starting from 1994.
3. The language became open-source in 1998, leading to more companies using it.
4. Bluetail was the first company outside of Ericsson to use Erlang in a product.
5. Erlang's success is attributed to its ability to adapt and evolve with new technologies.
6. Mnesia, an early distributed database, provided key-value storage and fault tolerance but lacked strong consistency for transactional use cases.
7. The Erlang ecosystem has spread across various industries such as telecom, banking, and web servers.
8. Elixir emerged as a significant addition to the ecosystem, bringing new tools and frameworks for web development.
9. Nerves is making embedded systems more accessible in production.
10. Phoenix framework is similar to Ruby on Rails but focused on web development.
11. Jose Valim aims to bring Erlang's power to a wide range of communities through Elixir and Phoenix.
12. Nerves is making progress in production and real-world use cases for embedded systems.
13. More languages are expected to emerge in the ecosystem, with statically typed languages gaining traction.
14. The Erlang ecosystem's versatility allows new ideas to be built on top of it.
15. Continuous evolution of the Erlang language, virtual machine (BEAM), and new features contribute to its longevity.
16. Recent changes include the addition of a JIT compiler for performance gains.
17. New languages and packages are being developed on top of existing systems.
18. The system's focus on concurrency, parallelism, and ease of use is appreciated by users.
19. Adaptation to change is necessary for continued growth and improvement.


## Zig Build System & How to Build Software From Source • Andrew Kelley • GOTO 2023

URL: [https://www.youtube.com/watch?v=wFlyUzUVFhw](https://www.youtube.com/watch?v=wFlyUzUVFhw)

 1. Different ways to obtain software: upstream binary distribution, system package manager (e.g., apt, yum), and obtaining from source code.
2. Importance of the configure phase in building software from source.
3. Understand available options and choices during configuration.
4. Respecting the configure phase avoids issues while building software.
5. Choose a prefix for installation within your home directory, maintain consistency across operating systems (if cross-platform), or cater to audience preferences on Windows.
6. During build phase, use make with proper CPU usage and install without sudo if in home directory.
7. Pick stable release versions when building from source.
8. Avoid using Docker or virtual machines for basic tasks; follow normal processes and report issues clearly.
9. Learn basics before attempting advanced techniques.
10. Dependencies are crucial, either build them separately or use prebuilt packages.
11. Troubleshooting tips: check dependencies, test on different OS/compilers, and fix caching issues.
12. Use proper tools for your project's language (e.g., CMake for C++).
13. New build system: Zig Build System - portable, easy installation with binary distribution, compiles C/C++ code without additional tools, uses clang for compilation, parallelism and efficient resource usage, solves caching problems with a hash-based system, improved M time granularity by checking file changes.
14. The Zig build system is featured in the next release of Zig.
15. Donations are encouraged for Zig Software Foundation, a non-profit organization.


## How to Do Embedded Development with Rust • Steve Klabnik • GOTO 2023

URL: [https://www.youtube.com/watch?v=7lHtXkYnip8](https://www.youtube.com/watch?v=7lHtXkYnip8)

 1. Low-level programming skills can be learned by anyone interested in them.
2. Rust is suitable for embedded software development due to its type system, focus on compiler error messages, and well-designed libraries.
3. Learning unfamiliar data structures and algorithms is essential for personal growth.
4. Fashion is a form of communication that impacts how others perceive us; it can be seen as a language constantly evolving.
5. Steve Jobs' fashion choices were deliberate, focusing on meaningful creative decisions in his work.
6. Tech industry fashion can convey opinions about people without conscious awareness.
7. BBC micro:bit is recommended for learning embedded systems.
8. Rust has a cortex M runtime library and high-level APIs for easier development.
9. Cargo embed tool helps build programs and upload code to devices.
10. Low-level programming involves configuring GPIOs, using volatile instructions, and working with hardware.
11. Embedded programming has different levels of abstraction, from high-level APIs to low-level details like pin concepts.
12. Cross compiling is used for compiling code for various architectures.
13. Flash memory and flashing are essential in embedded systems; consider memory usage.
14. Serial ports are an older I/O interface found in various devices.
15. Semi-hosting should be avoided due to timing issues.
16. Pin concept: Memory location for performing actions on a device.
17. Learn through projects, documentation, debugging errors, and successes.
18. i2C protocol is used in embedded systems; master and slave communication via clock and data lines.
19. Interrupts are asynchronous events in hardware, similar to callbacks in JavaScript.
20. Debuggers play a crucial role in embedded development for examining system state while it's running.
21. Embedded documentation is extensive but can have errors like any other documentation.
22. Test-driven development (TDD) is less common in embedded programming, but tools like Rust's CI integration can help.
23. Useful resources for learning embedded programming include The Embedded Rust book, Comprehensive Rust, and various rust books.
24. Digikey and Mouser are popular websites for buying hardware and finding documentation.


## Concurrency Oriented Programming in a Modern World • Robert Virding & Francesco Cesarini • YOW! 2022

URL: [https://www.youtube.com/watch?v=A-f7md5exaE](https://www.youtube.com/watch?v=A-f7md5exaE)

 1. Francesco and Robert are founders of Ireland Solutions, focusing on language expertise.
2. Concurrency-oriented programming (COP) was introduced by Joe Armstrong in 2002, emphasizing concurrent processes, data sharing, and communication through message passing.
3. Erlang was developed to solve Telecom system problems with a focus on fault tolerance and scalability, using processes as its main building block.
4. Beam VM enables fast process creation with minimal memory allocation.
5. Elixir's process-based ecosystem decouples concurrency from the underlying operating system, similar to Erlang.
6. Processes communicate via asynchronous message passing without guarantees on receiving messages.
7. Failure detection in Airline uses two linked processes for crash detection and appropriate actions.
8. The "let it crash" principle allows for a reliable system by detecting issues and handling them efficiently.
9. Co-inventors of the first mobile phone systems focused on reliability, leading to human monitoring and redundancy in processes.
10. Erlang's concurrency model based on no shared memory and message passing enables distribution, scalability, and reliability.
11. Concurrency and parallelism are different concepts: concurrency is about doing things at the same time while parallelism is about executing tasks simultaneously.
12. Erlang focuses on concurrency with no shared memory, making it suitable for distributed systems and scalability.
13. JVM prioritizes speed and parallelism but can achieve concurrency through frameworks like Akka.
14. WhatsApp used concurrency to reduce operational overhead and hardware costs by handling a large number of users simultaneously.
15. Phoenix (Elixir) enabled 2 million socket connections in a stable way, showcasing the language's potential.
16. Elixir's popularity is due to its concurrency features and ease of adoption for new communities.
17. The goal is to solve problems related to running massive things simultaneously without crashing servers.
18. Erlang's web server benchmarks outperformed Apache in 2001 but wasn't packaged as a standalone application.
19. Web servers are examples of similar problems, handling massive connections without crashing.
20. Elixir's syntax is inspired by Ruby for familiarity and reduced psychological barriers.
21. Challenges in orchestration and distribution, containerization, and Kubernetes.
22. Importance of considering concurrency from the start when designing languages.
23. Airline philosophy on handling errors: let processes crash without affecting the whole system.
24. Consistent error handling across programs for various scenarios.
25. Focus on dealing with small chunks of the system, ensuring it keeps running and restarts when necessary.
26. Letting a process crash is about managing software errors in a standardized way across programs.
27. Handling machine crashes is difficult but having two machines can help create a fault-tolerant system.


## Scala Implicits Revisited • Martin Odersky • YOW! 2020

URL: [https://www.youtube.com/watch?v=dr0PUXQhg3M](https://www.youtube.com/watch?v=dr0PUXQhg3M)

 1. Implicits are a key feature in Scala, used in 98% of projects.
2. Implicit conversions led to issues, and later, implicit parameters were introduced with limitations.
3. Contextual implicit resolution caused problems, leading to coherence and locality rules for clarity.
4. Scala 3 aims to improve implicit design decisions by focusing on term inference and introducing given instances (Givens).
5. Givens are synthesized values for specific types, abstracting from how they're produced.
6. Future improvements include better error messages, more explicitness, clearer rules, and support for Scala 3.0 with implicit conversions.
7. Scala 3 introduces improvements in indentation, optional braces, cross-compilation, and uniform syntax.
8. Tools like editors help maintain code reliability through meta properties of indentation.
9. House Color 3 experience shows positive results, including shorter programs with better writing flow.
10. No downsides found for refactoring or large settings.


## Calling Functions Across Languages • Richard Feldman • GOTO 2023

URL: [https://www.youtube.com/watch?v=ZOvxa9aKCCg](https://www.youtube.com/watch?v=ZOvxa9aKCCg)

 1. Calling functions across languages can be achieved using different methods, such as HTTP requests and responses or direct communication between processes.
2. Optimizing the process involves removing HTTP boilerplate, focusing on data transfer, and using localhost and binary encoding instead of JSON.
3. Inter-process communication (IPC) like Unix sockets can further reduce overhead.
4. The goal is to call a Ruby function from JavaScript within a single process with minimal overhead.
5. To achieve this, opcode manipulation is used to combine JavaScript and Ruby in one process by jumping between their instructions.
6. This approach has risks like type mismatches due to lack of type information.
7. C can be used as an intermediate representation between JavaScript and Ruby via Node.js for direct function calling.
8. Ruby linear algebra can be imported into Node.js without inter-process communication or network overhead.
9. CFFI (C Foreign Function Interface) is a tool that can be used in other languages like Python to call functions across different languages.
10. Overhead occurs due to conversions between different number representations, and a Gnome2js library could eliminate the need for C intermediary.
11. Type checking can be challenging with C bindings as they don't support type definitions; Rust has Russ bindgen for this purpose.
12. The programming language Rock aims to make it easy to embed in other languages, focusing on being nice to call from them.
13. Rock Glue generates Rust types and bindings from Rock code, making it easy to call Rock functions from Rust.
14. This approach can be applied to other languages like Node.js for interoperability.
15. The goal is to provide a consistent user experience regardless of the target language.
16. Each approach has trade-offs: network communication offers distribution across multiple machines, while same process ensures minimal overhead and stateful runtime guarantees.
17. Language server protocol uses inter-process communication for editor extensions without affecting the entire editor.
18. WebAssembly provides more control over memory management but doesn't automatically protect against segmentation faults or memory corruption.


## Effective Programming in OCaml • KC Sivaramakrishnan • YOW! 2021

URL: [https://www.youtube.com/watch?v=X28PFYvZ_V8](https://www.youtube.com/watch?v=X28PFYvZ_V8)

 1. Multicolor Camel is a project that adds native support for concurrency and parallelism to OCaml through effect handlers and domains.
2. Effect handlers provide composability, well-behaved libraries, and first-class restartable exceptions using exception handling syntax.
3. The language extension implements lightweight threading with fork and yield effects, managed by a scheduler.
4. Effects are hidden behind signatures, making it look like sequential code for users.
5. Multicolor Camel demonstrates handling continuations and concurrency in a language, including generators for non-continuous traversals.
6. The project maintains backwards compatibility while transforming synchronous code into asynchronous using FX (effects) for handling IO operations.
7. It introduces defensive programming for exceptional behavior, making synchronous code asynchronous with a scheduler queue and discontinue primitive.
8. Performance overhead measurements include stack switching, generators, and web server implementation with effect handlers.
9. OCaml Multi-Core is an open source project that allows users to install and use the techniques discussed.
10. The approach based on effect handlers is comparable in performance to Go and LWT, without relying on monads or sacrificing program pausing capabilities.


## Hashing Modulo Alpha Equivalence • Simon Peyton Jones • YOW! 2021

URL: [https://www.youtube.com/watch?v=PltixgJiRrw](https://www.youtube.com/watch?v=PltixgJiRrw)

 - The problem is finding equivalent sub-expressions in a program and making small rewrites.
- Hashconzing can be used for incremental analysis but doesn't work well with lambdas due to false positives and negatives.
- Using Divine notation removes names from lambdas, but introduces new issues: overheads in the compiler and both false positives and negatives.
- The speaker didn't find a perfect solution for this problem during their talk.
- Dubai notation has issues with false positives and negatives.
- E-summary is a solution to find Alpha equivalent subexpressions.
- E-summary consists of structure and free variable map.
- Hash codes are extracted from e-summaries for efficient comparison.
- Collisions can occur, but should be infrequent.
- The approach focuses on Isamu first, then extracts hash codes and uses a table to save nodes with the same hash code.
- Introducing e-summaries: A pair of a structure and a free variable map.
- Structure: Describes the shape of an expression without mentioning identities or locations of variables.
- Variable Map: Maps variables to their positions in the structure.
- E-summary for single variable: Structure is svar, variable map maps variable to P here.
- Lambdas: Recursively call summarize and extract structure and variable map from summary.
- Application nodes: Use e-summaries of children expressions to create e-summary of application node.
- No two position trees point to the same location.
- E7 concept: Structure and free verbal map.
- S-dam container (Repository) vs. Pository.
- Summarize function: Takes an expression, delivers e-summary.
- Hash summaries: Replace structures with structure hashes, positives with pository hashes for more efficient reconstruction.
- Handling shadowing in e-summaries: No issues as they're anonymous and don't have names.
- Next step: Discussing app nodes.
- E summaries deal with shadowing by treating them as anonymous variables.
- Hash summaries use structure hashes and pository hashes for more efficient reconstruction.
- App nodes require attention to every element of both VAR Maps, leading to O(n^2) work in unbalanced trees.
- Solution: Only adjust items in smaller map, recording depth and bigger map flag in structures.
- This approach allows efficient rebuilding while maintaining perfect inversion.
- Discussed the process of combining and splitting variable maps in a tree structure.
- The complexity is O(n log n) due to work done on smaller trees.
- Considered using hashes for variable maps, but deleting elements from them was problematic.
- Introduced exclusive or (XOR) as a solution: hash of a variable map is the XOR of its key value pairs' hashes.
- Deletion can be achieved by XORing the hash of the deleted element with the available map hash.
- Synthetic benchmarks and real-world tests show that the proposed method outperforms other correct algorithms.
- Synthetic test cases show balanced and unbalanced expressions.
- Green circles algorithm is the best, with faster performance than locally nameless.
- Locally nameless is correct but has worse complexity.
- The speaker found it surprising that there was a gap in literature regarding this issue.
- Algorithm is simple yet efficient, requiring mathematical and formal reasoning for improvements.


## Zig Build System & How to Build Software From Source • Andrew Kelley • GOTO 2023

URL: [https://www.youtube.com/watch?v=vKKTMBoxpS8](https://www.youtube.com/watch?v=vKKTMBoxpS8)

 1. Obtain software through various methods: upstream binary distribution, system package manager (e.g., apt, yum), and source code compilation.
2. Understand the importance of the configure phase in building software from source.
3. Focus on using a custom prefix during configuration to simplify uninstallation and avoid conflicts with other software.
4. For Windows, consider catering to its specific needs while maintaining consistency across platforms.
5. When building from source, use release versions and stick to the system toolchain.
6. Avoid using Docker or virtual machines unless necessary; focus on learning how to build from source.
7. Don't modify header files or perform weird workarounds during the build process.
8. Learn the basics before attempting advanced techniques.
9. Dependencies are crucial for building software from source, so ensure they're installed correctly.
10. Troubleshooting tips: check dependencies, test on different OS/compilers, and fix broken caching issues.
11. Use alternative build systems like Ninja instead of Make to avoid caching problems.
12. Introduce the Zig Build System for efficient and portable compilation.
13. Parallelism is achieved by constructing a build graph in the script.
14. Implement a cache system for better resource usage and avoiding false positives.
15. Create a package manager with manifest files for dependency management.
16. Rebuild Groove Basin music player using Zig.
17. The Zig build system is easy to use, allowing contributors to run it without complex instructions.
18. Support the non-profit Zig Software Foundation through donations.


## An Introduction to Functional Imperative Programming in Flix • Magnus Madsen • GOTO 2023

URL: [https://www.youtube.com/watch?v=2LSOqikNqxM](https://www.youtube.com/watch?v=2LSOqikNqxM)

 1. Flix is a functional programming language with effect systems, which help in understanding programs better and enable optimizations.
2. Type and effect systems characterize values and computational effects respectively.
3. Effect systems allow capturing purity or impurity of functions through effect polymorphism.
4. Libraries can benefit from effect systems by enabling parallel execution without race conditions or deadlocks.
5. Flix forces equals and hash functions to be pure for trustworthy implementations.
6. Region-based memory management allows pure functions to use mutable data structures temporarily within a lexical block.
7. Iterators are efficient ways to iterate through collections, with terminal and non-terminal operations managing suspended effects.
8. Effect systems clarify how code works by managing suspended effects and mutable memory for iterators.
9. Pure functions in languages with type and effect systems are easier to understand and optimize for parallelism.
10. Library authors can use reflection on function purity to enable parallel evaluation safely when needed.


## Concurrency Oriented Programming in a Modern World • Robert Virding & Francesco Cesarini • GOTO 2023

URL: [https://www.youtube.com/watch?v=AvA97AB8cAA](https://www.youtube.com/watch?v=AvA97AB8cAA)

 1. Francesco and Robert, co-inventors of Erlang, discussed their experiences in building a programming language for telecom applications with concurrency, fault tolerance, and upgradability while running.
2. They demonstrated the concept using an electric train simulation at a conference, focusing on concurrency and processes.
3. Key ideas behind Erlang include concepts like concurrent systems, data isolation, and asynchronous communication.
4. Processes in Erlang are lightweight and efficient, allowing millions to interact simultaneously. When a process ends normally or crashes, the memory is freed immediately.
5. Communication between processes happens through messages with PIDs (process identifiers).
6. Asynchronous communication can lead to lost messages, so acknowledgments are used for confirmation. Failure detection is achieved by monitoring processes and linking them together.
7. Early mobile telephony systems had manual error handling, but Erlang's approach allows processes to monitor and link to each other, sending exit signals when a linked process crashes.
8. Trap exits enable processes to handle errors in a custom way, while supervisors monitor other processes and take appropriate actions (restart, terminate).
9. Concurrency models based on notion memory and message passing provide distribution, scalability, and reliability.
10. Three pioneers in concurrency research developed similar solutions for different problems: Carl Hewitt, Tony Hoare, and Joe Armstrong.
11. Concurrency is a property of the problem being solved while parallelism is a property of the underlying system. These models allow efficient distribution and scalability without worrying about hardware architecture.
12. Beam and JVM have differences in focus: Beam emphasizes scalability and resilience, while JVM focuses on speed/parallelism.
13. Concurrency model in Java was implemented through Akka by Jonas Bonér, inspired by Erlang's OTP systems.
14. WhatsApp used Airline for their backend servers with 2 million TCP connections on one machine.
15. Elixir is an ecosystem of languages built on top of the Airline and Beam virtual machine, aiming to bring the power of Airline to new programming communities.
16. Alexa became a first-class citizen in the Airline ecosystem, showcasing its potential as an ecosystem.
17. Statically typed languages like Elixir are important for device security.
18. Jose Valim created Elixir to bring Erlang's power to new programming communities, focusing on runtime and language principles for effective concurrency implementation.


## Why Static Typing Came Back • Richard Feldman • GOTO 2022

URL: [https://www.youtube.com/watch?v=Tml94je2edk](https://www.youtube.com/watch?v=Tml94je2edk)

 1. In the 1950s to 1990s, statically typed languages were more prevalent than dynamically typed ones.
2. The 1990s saw a boom in dynamic languages due to web growth and fast feedback loops.
3. Popular dynamic languages include JavaScript, Ruby, PHP, Python, and R.
4. Statically typed languages had advantages like runtime performance but were less relevant in the 1990s context.
5. Gradual typing systems emerged for dynamic languages, leading to more popularity for statically typed ones.
6. In the 1990s, dynamic languages dominated web use cases due to their fast feedback loops and concise syntax.
7. The LAMP stack became popular for early web needs.
8. Two dynamic languages made the top 20 most popular programming languages: PowerShell and CoffeeScript.
9. Statically typed languages like C#, ActionScript, Go, Rust, Dart, Kotlin, TypeScript, and Swift have gained popularity in recent years.
10. Modern JavaScript has less ceremony than older versions.
11. TypeScript adds minimal static typing without much ceremony.
12. The speaker's view of static typing has evolved over time.
13. Minimal ceremony in JavaScript leads to success.
14. Upgrading to Modern JavaScript involves minor changes.
15. Static typing in TypeScript adds minimal extra code compared to Java's static typing.
16. Advantages of Java implementation include better equals and hashcode implementations, early JSON validation, and useful Getters/Setters.
17. Rock programming language uses type inference for early JSON validation without explicit type annotations.
18. Concise code can be achieved with proper language design and features.
19. Null pointer exceptions are not innate to static typing; some languages have null-aware type checkers.
20. Elm and Haskell have sound type systems, leading to fewer runtime errors.
21. Error messages in modern languages are improving, becoming clearer and more helpful.
22. IDEs can be laggy but performance has improved with multi-core processors.
23. Static typing has improved over time, with better error messages and IDE performance.
24. Feedback loops have also become faster in statically typed languages like Haskell.
25. The main benefit of static typing for many people is the red squiggle (syntax errors) in their IDEs, which helps them catch issues earlier than runtime crashes.
26. Static typing has become more popular with languages like TypeScript and Elm, showing that it can be enjoyable to use.
27. In the past, static typing was seen as slow with feedback loops.
28. Modern languages have improved this by offering faster feedback and non-blocking errors.
29. Three hypothetical futures: 1) Dynamic typing returns, 2) Gradual typing becomes popular, or 3) Static typing without gradual typing grows.
30. The pendulum swinging back to dynamic typing is less likely as statically typed languages can offer the same benefits.
31. Future of static and dynamic typing will depend on how well they adapt to new technologies and user needs.
32. Gradual typing has become more popular by adding static type checking to existing dynamically typed ones.
33. ActionScript and Dart were the only gradually typed languages from the start, but Dart later switched to full static typing.
34. Static typing has a simpler design space compared to gradual typing, which needs to model all dynamic behavior.
35. Gradual typing introduces runtime overhead due to checking types at both compile time and runtime.
36. Historical evidence doesn't support the claim that gradually typed languages will become mainstream in the future.
37. Static typing has become more popular due to improvements in statically typed languages that adopt benefits of dynamically typed ones.
38. Gradual typing is not the best solution as it comes with unavoidable downsides, such as runtime overhead and complexity.
39. Rock language aims for simplicity, performance, and ease of use without sacrificing benefits of statically typed languages.
40. Prediction: Among the next five popular programming languages, most or all will be statically but not gradually typed.


## The Java Agent: Modifying Bytecode at Runtime to Protect Against Log4J • Joe Beeton • GOTO 2022

URL: [https://www.youtube.com/watch?v=ZrGOv44iTC8](https://www.youtube.com/watch?v=ZrGOv44iTC8)

 1. Java instrumentation API enables dynamic and static analysis of running Java applications.
2. Dynamic attachment involves creating a Unix socket, loading the agent jar file, and calling its main method with arguments.
3. Manifest files in agent jars contain pre-main, agent class, native prefix, and permissions for modifying bytecode.
4. JBomb creates a bill of materials for running Java applications by attaching to them at runtime.
5. Static attachment is simpler; add the Java agent flag with jar location on startup.
6. Protect is a tool that detects and blocks potential vulnerabilities like SQL injection or remote code execution.
7. Log4Shell allows remote code execution through specific strings in log files, which can be blocked using tools like Protect.
8. JNDI lookup can lead to remote code execution if an attacker controls the JNDI server.
9. Oracle disabled default remote class loading in Java updates after October 2018.
10. Other ways of exploiting Log4j include Spring Boot Tomcat's Apache Bean Factory and JavaScript engine removal in Java 15.
11. A malicious JNDI server can return a payload that executes commands on the application.
12. Demonstrated a JNDI vulnerability in Spring Boot Tomcat using Apache Bean Factory.
13. Showed how to modify the JNDI lookup class to block the vulnerability using ASM and Java agent.
14. Discussed other security issues and resources available for developers.


## Expert Talk: Zig Programming Language & Linters • Andrew Kelley & Jeroen Engels • GOTO 2022

URL: [https://www.youtube.com/watch?v=zKmZmiOU6qE](https://www.youtube.com/watch?v=zKmZmiOU6qE)

 1. Jeroen and Andrew discuss their experiences with linters, focusing on Elm and Zig languages.
2. They mention the lack of powerful refactoring tools in Elm compared to other languages like Java.
3. Conditional compilation is important for future language development.
4. Code smells can be false positives in linter rules; examples from different languages are provided.
5. Assertions may help reduce false positives, but they might not be possible if type information is missing.
6. Linting fixes can simplify developers' lives, but they need to be trustworthy and provide details about the changes made.
7. Elm-review uses prompts for every error with a suggested fix, allowing users to build trust in the tool.
8. The tradeoff between linting errors and compilation is separating the steps, ensuring code quality while still allowing flexibility in development.
9. In pull requests with green tests, there's a guarantee that all used code has been checked by the linter.
10. Context matters when evaluating the usefulness of linting in different scenarios.
11. Continuous integration is related to linting, as it enforces rules during development.
12. Some projects may not have a separate integration phase or focus on guarantees.
13. Nim language focuses more on flexibility and power rather than guarantees.
14. Zig prioritizes readability and maintainability over other aspects.
15. Elm has referential transparency due to functional programming, ensuring the same input yields the same output.
16. Guarantees can simplify code and make refactoring easier.
17. Referential transparency is an essential aspect of purely functional languages, where the same inputs always result in the same outputs.


## Deno: The JavaScript Runtime for the Serverless Era • Ryan Dahl • GOTO 2022

URL: [https://www.youtube.com/watch?v=VDKJ1rSj-NI](https://www.youtube.com/watch?v=VDKJ1rSj-NI)

 1. The speaker emphasizes the significance of JavaScript in modern software development.
2. He presents an ideal stack consisting of a universal scripting language, serverless architecture, and optimized infrastructure.
3. Dino is introduced as a framework that implements this stack, focusing on simplicity, security, and optimization.
4. Features include TypeScript integration, browser compatibility, and easy dependency management through npm.
5. Dino Deploy builds serverless systems using Dino, hosting at the edge in 34 data centers worldwide with GitHub integration for code deployment.
6. Dino is a local development runtime similar to Node, focusing on serverless systems for JavaScript.
7. Dino Deploy provides a white label serverless system for websites like Netlify Edge functions and Super based Edge functions.
8. A fresh web framework is built for speed, rendering everything just in time on the server, automatically inlines CSS, uses Tailwind, and has TypeScript out of the box with no configuration.
9. Comparison between a fresh app (84KB) and a create react app (339MB) shows significant optimization potential in server-side JavaScript.
10. Efforts are being made to improve frameworks and cloud deployment for better optimization.


## BEAM Concurrency in Action • Sasa Juric • YOW! 2022

URL: [https://www.youtube.com/watch?v=A4x6IfceJCM](https://www.youtube.com/watch?v=A4x6IfceJCM)

 1. Beam concurrency revolves around processes, which are sequential programs that can spawn other processes and communicate through messages.
2. Message passing is the primary way for processes to coordinate or cooperate; each process has a mailbox for received messages.
3. Beam runtime starts with an OS process containing all the processes, encouraging lightweight, independent processes in abundance.
4. Concurrency is essential even for small systems as it allows multiple capabilities and vertical scalability.
5. In the example given, an analyst process handles requests and spawns a query process to run long-running tasks separately, decoupling execution flows.
6. Beam is a framework for concurrent programming using event-driven, reactive style with lightweight processes.
7. Data processing pipelines can be implemented using Beam, making it suitable for event-driven microservices and handling data streams.
8. Concurrent thinking in Beam: Split processes to separate execution flows and failures.
9. Registry pattern maps logical roles to physical addresses for service discovery.
10. Managing load in the pipeline involves batching efficiently to handle high loads without falling behind reality.
11. Cancellation is crucial in concurrency technology, often overlooked; it can involve stopping processes with reasons and cleaning up resources before stopping.
12. Elixir's process hierarchy allows concurrent execution of builds with custom termination for each process in a tree structure.
13. Observability and metrics are essential for understanding distributed systems.
14. Erlang and Elixir have flexible, in-memory standard libraries that aid debugging multi-process Beam programs.
15. Dealing with side effects before process cancellation requires custom termination, such as cleaning up caches or draining commands.
16. Transactions can be handled by closing sockets or using saga patterns for distributed messaging systems.


## Rust in Action • Tim McNamara & Richard Feldman • GOTO 2023

URL: [https://www.youtube.com/watch?v=iYJ6bLITZsI](https://www.youtube.com/watch?v=iYJ6bLITZsI)

 1. Tim McNamara, author of "Rust in Action", shares his background as a Python developer and transition to Rust.
2. The book aims to teach Rust while incorporating concepts from systems programming for people with dynamic or Java backgrounds.
3. Rust offers a different experience compared to languages like C++, with fewer segmentation faults and more developer happiness.
4. "Rust in Action" provides extra context on low-level computer concepts while learning Rust.
5. The Rust community is welcoming and interested in preventing people from feeling excluded, making it more accessible for new entrants.
6. Teaching Rust effectively to beginners can be challenging, with strings being one of the hardest concepts due to its unique handling.
7. Lifetime annotations help manage data access validity in Rust programs.
8. The borrow checker ensures every data access is valid and can never be invalidated.
9. Unsafe code in Rust is intentional and used for low-level tasks, but it's essential to understand its purpose.
10. Atomic clocks and network time protocols help synchronize time across distributed systems, with monotonic ordering crucial for logs or messages to be roughly in order.


## Intro to the Zig Programming Language • Andrew Kelley • GOTO 2022

URL: [https://www.youtube.com/watch?v=YXrb-DqsBNU](https://www.youtube.com/watch?v=YXrb-DqsBNU)

 1. Zig is a general-purpose programming language and toolchain for creating robust, optimal, and reusable software.
2. The project aims to enhance technology by incrementally improving the commons.
3. Zig CC is a drop-in C++ compiler with better defaults, enabling hermetic builds and undefined behavior sanitizer.
4. Real-world applications are using Zig CC, finding bugs, and fixing them.
5. The project focuses on raising standards of software as a craft through tooling, open source libraries, and student education.
6. Use Zig CC for better defaults, cross compilation, and simplified installation.
7. Leverage the Zig build system to create a unified build process for C/C++ projects.
8. Write components in Zig for improved dependency management across different operating systems.
9. Compiler with Zig build system; Level 2: Exploiting C dependencies in Zig build system; Level 3: Integrating Zig code into projects; Mixing C and Zig code seamlessly.
10. Non-profits vs. for-profit companies; Timeline of a typical VC-backed startup: unsustainable product, tight grip on resources, acquisition or failure.
11. Examples of companies with varying fates: Wikipedia, Google, Fitbit, Progressive Roofing, Rad Game Tools, SQLite.
12. Zig Software Foundation's stable and mission-focused approach.
13. Zig language's versatility in various applications: low-level infrastructure (river Window Manager), high-performance applications, resource-constrained environments, webassembly.
14. Arraylist implementation in Zig is simple and easy to understand; Inline loops allow printing any value without complex code; Hash maps from the standard library provide efficient data storage.
15. Zig language focuses on application understanding, not esoteric rules; Inline loops and reflection for convenience; Hash maps with auto array functionality; Multi-array lists for data oriented design.
16. C integration through demos like a roguelike deck builder.
17. Zig is a CT plus compiler toolchain and build system for simplifying maintenance of existing projects, but can be used without the language.
18. The software foundation aims to improve software engineering craft throughout the industry; Cross compilation and C integration are supported, allowing for easier maintenance of existing projects.
19. Sponsorship is encouraged for those who like what they do.


## The Perfect Language • Bodil Stokke • YOW! 2017

URL: [https://www.youtube.com/watch?v=vnv8MGIN7A8](https://www.youtube.com/watch?v=vnv8MGIN7A8)

 1. A perfect language doesn't exist as they are designed for specific purposes.
2. Popular programming languages include JavaScript, Rust, and Esperanto based on GitHub metrics.
3. JavaScript features functional aspects and type handling in Rust.
4. Rust emphasizes ownership and borrowing concepts to avoid memory issues.
5. Consider improving existing languages instead of creating new ones.
6. Ideal language should focus on abstraction, simplicity, garbage collection, immutability, higher-order programming, and FFI for interoperability.
7. Scarlet combines functional programming ideas with familiar syntax.
8. Modular 2 aims to make JavaScript programmers more comfortable with Haskell concepts.
9. Design a language that combines the simplicity of JavaScript with the power of functional programming.
10. Focus on tooling, community, and documentation for language adoption.
11. Explore ideas like transpilers, bridging gaps between existing languages, and dependent types.
12. Build a universal package manager for any language to facilitate code sharing.
13. Consider building a language that combines aspects of PureScript and TypeScript or use a subset of JavaScript for server-side development.
14. Explore dependent types in languages like Idris to make them more accessible.
15. Keep learning new programming languages and tools to improve skills.
16. If you find an interesting idea, consider building your own niche language.


## TypeScript vs KotlinJS • Eamonn Boyle & Garth Gilmour • GOTO 2022

URL: [https://www.youtube.com/watch?v=GlU8ZyJNI7Q](https://www.youtube.com/watch?v=GlU8ZyJNI7Q)

 1. Both Typescript and Kotlin are loved by developers, but Kotlin is more versatile.
2. Creating a Kotlin JS project with IntelliJ wizard and using Gradle for build system integration.
3. Documentation provides clear information on library availability in Kotlin JS.
4. Dependencies can be managed through npm or pre-built wrappers.
5. Kotlin JS projects follow a similar structure to JavaScript, with main() and app creation.
6. Kotlin JS uses low-level DOM API for browser rendering.
7. Kotlin.js allows using existing libraries and integrates with Gradle.
8. Typescript is more popular than Kotlin.js, making it easier to reuse JavaScript assets.
9. Kotlin's community is growing but needs to catch up in comparison.
10. Interoperability with JavaScript is possible through wrappers or automatic generation tools like CAT.
11. Kotlin offers escape hatches for working with untyped objects, similar to JavaScript.
12. Typescript has a larger community and better compatibility with JavaScript.
13. Kotlin's new DSL is nicer but needs updated documentation.
14. Typescript has powerful type systems with features like unions and intersections.
15. Kotlin lacks overloads, a feature that allows multiple functions with the same name to accept different arguments.
16. Typescript has powerful type system with features like unions and intersections.
17. Kotlin has suspending functions for asynchronous tasks.
18. Transitioning from JavaScript to Kotlin requires extra work in some cases.
19. JSX is purpose-built for HTML and easier for designers.
20. Suspending functions can be used for lazy evaluation and have various use cases.
21. Both languages are good, but Typescript might be preferred for stable engineering due to its larger community, bug fixes, and documentation.
22. For building on the JavaScript ecosystem, Typescript solves problems that Kotlin doesn't address.
23. Consider other languages like Kotlin for specific use cases outside of web development.
24. Learning JavaScript/TypeScript is inevitable for developers working in web development.
25. If you have no context, write 'no context'.


## Simplifying Systems with Elixir • Sasa Juric • YOW! 2020

URL: [https://www.youtube.com/watch?v=EDfm2fVS4Bo](https://www.youtube.com/watch?v=EDfm2fVS4Bo)

 - Elixir, a programming language with Erlang runtime (BEAM) benefits, offers embedded support for microservices, multi-core capabilities, and concurrency.
- The Earlangelist is an example of a simple system written in Elixir, organized as independent processes internally but presented as a monolithic project.
- Erlangelist is another example, a blog site built with Elixir showcasing microservices.
- Phoenix web framework provides process organization for multi-core capability, vertical scalability, separation of failures and latencies.
- No need for additional components like nginx, simplifying implementation.
- A custom lightweight database eliminates external dependencies, while a stats collector handles concurrent requests efficiently.
- Separation of failures and latencies through independent processes.
- Periodic jobs are handled by two processes: scheduler and task performer, improving testability compared to third-party components like Cron jobs.
- Serving HTTPS traffic with Let's Encrypt for added security and privacy.
- Certifier process handles certificate renewal without additional dependencies or external tools.
- A dashboard provides insights into the system's usage and state.
- Tests verify various aspects of the system, including HTTP redirects to HTTPS, endpoint certifications, and other features.
- Elixir and Erlang provide a simple, monolithic approach to development.
- Docker simplifies operation by allowing self-contained releases.
- A programmable API allows for user-friendly interfaces on top of the core functionality.
- Start with a single language and expand as needed, reducing technical complexity.
- Utilize databases for proper data persistence.
- Explore other technologies when necessary.
- Benefits include reduced complexity, easier testing, and increased confidence in the system.
- The speaker is a huge fan of Elixir and BEAM languages.


## Streamlining Large-Scale Java Development Using Error Prone • Sander Mak • GOTO 2022

URL: [https://www.youtube.com/watch?v=C5MBsKZHqrY](https://www.youtube.com/watch?v=C5MBsKZHqrY)

 1. Error Prone is an open-source tool by Google, automating Java code improvements through a compiler plugin.
2. Supports various Java versions and offers built-in checks for uniformity and development process improvement.
3. Demonstrated with examples of unused methods and incorrect exception handling.
4. Customizable via enabling/disabling specific checks or suppressing warnings.
5. Can use the far check feature to assume local variables and parameters as final, requiring explicit annotations for mutable ones.
6. Error Prone can be customized by creating your own book Checker implementations to find specific patterns in code.
7. Auto Service from Google simplifies making classes service loadable, used by Error Prone.
8. Refactor is a solution that expresses patterns in concrete Java syntax for ErrorProne to rewrite automatically.
9. Create refaster templates with before and after templates for matching and rewriting code.
10. Use ErrorProne to apply generated rules to the code base, making it easier to migrate between APIs or libraries.


## Interview with Louis Pilfold on Elixir Gleam • YOW! 2022

URL: [https://www.youtube.com/watch?v=kDfa7AVeugw](https://www.youtube.com/watch?v=kDfa7AVeugw)

 1. Gleam is a new functional programming language that combines strengths of Beam and typed functional languages.
2. It offers features like actor model for concurrency, type system, and editor tooling.
3. Inspired by Rust, Go, and Elixir, the goal is to make Gleam accessible for businesses and various applications.
4. Gleam's syntax draws inspiration from Rust and Go, focusing on simplicity with a small set of useful features and an easy learning curve.
5. The weirdness budget concept helps in designing language features.
6. Gleam aims to be used by businesses for diverse tasks.
7. No plans for traits or ad hoc polymorphism due to readability concerns.
8. Gleam is compatible with other Beam languages, ensuring interoperability and access to existing libraries.
9. JavaScript compatibility is slightly more challenging due to differences between both languages.
10. Compiled code maintains human-readable appearance in Erlang and JavaScript runtimes.
11. Gloom is a language that uses immutable data structures and doesn't mutate, with its own mutable list library for use with JavaScript.
12. Gleam's standard library is modular, allowing users to choose which version they want.
13. The latest release focuses on implementing the Language Server Protocol for IDE integration.
14. Future releases will add auto completion, type-directed refactorings, and more features.
15. Community growth is essential, with plans to improve the onboarding process, make it easier to try Gleam in a browser, and foster a welcoming environment through a Discord server for discussion and community.


## Full-Stack Haskell: From Prototype to Production • Ryan Trinkle • YOW! 2018

URL: [https://www.youtube.com/watch?v=guhrVxY63tg](https://www.youtube.com/watch?v=guhrVxY63tg)

 1. Speaker shares experience of using functional programming in a full stack web and mobile app development company.
2. Benefits include improved focus, collaboration, reduced latency, and fun work environment.
3. Functional programming is better at full stack development due to its strong typing and pure functions.
4. Code reusability increases as Haskell forces explicit dependency declaration.
5. Contributing fixes upstream became a habit for the speaker's company, making it easier to maintain dependencies.
6. Haskell makes code more reusable, allowing for different compilation methods.
7. Contributing fixes upstream is easier with functional programming and strong typing.
8. NYX provides a consistent development environment for packages.
9. Fixing bugs upstream saves money and improves teamwork.
10. Obsidian doesn't believe in prototypes, preferring refactoring instead.
11. Haskell's compiler feedback makes writing code easier and more predictable.
12. Avoid prototyping and focus on refactoring, as Haskell code can be easily improved.
13. Recognize the cost-benefit of perfectionism in Haskell, knowing when to stop proving things with types.
14. Use end-to-end solutions instead of breaking down projects into components.
15. Be cautious about using new language extensions and libraries, as they can have a high cognitive overhead.
16. Remember that great software can be built without advanced features like type classes or Singletons.
17. Refactoring is important but can be challenging with new language extensions and libraries.
18. Obelisk helps build a sensible default for web and mobile app development, making it easier to learn and work in the ecosystem.
19. It provides tools for setting up projects, development, and deployment.
20. Demo shows how to use Obelisk to create a simple website and deploy it to production.
21. Plans for improving documentation, support for ghcjs 8.2 and 8.4, and community contributions.
22. Recognition of the Haskell ecosystem's impact on software development.
23. Aiming to move from prototype mentality to production mentality in Haskell.


## Building Your Own Compiler The Slightly Easier Way With LLVM • Erik Corry • YOW! 2016

URL: [https://www.youtube.com/watch?v=_XbOTRunqHk](https://www.youtube.com/watch?v=_XbOTRunqHk)

 1. Speaker discusses creating a language and mentions LVM, an open source compiler framework.
2. Demonstrates building a simple regular expression parser in a new language.
3. Explains the need for data structures to represent abstract syntax trees (AST) in regular expressions.
4. Introduces classes for literal characters, alternatives, disjunctions, and empty alternatives as AST nodes.
5. Shares the importance of passing up the AST to the compiler.
6. Design a recursive descent parser for a simple regular expression language.
7. Create an AST class and data structures for the abstract syntax tree.
8. Use graphviz to visualize the tree by adding unique names for each node.
9. Add dump methods to every class to print ASCII representation of nodes.
10. Include test string methods for regular expressions.
11. Create a makefile with commands to run the program and generate output.
12. Upside down jokes and tree visualization: AST node naming convention (F0, F1), dumping nodes into ASCII file for printing, using visitor pattern for recursive dumping, generating C code with llvm to represent AST nodes, optimizing generated functions using llvm, abstract class and methods for matching input characters.
13. Generated a regular expression parser in C++ using LLVM.
14. Created a driver to test the parser on input lines.
15. Compiled the code into an executable named 'grit'.
16. Tested the program with a sample input, showing efficiency and performance.
17. Generating llvm intermediate code from Dart.
18. Compiling down to assembler using clang.
19. Efficient regular expression language.
20. Comparing grep performance with the generated code.
21. Inlining optimizations in llvm.
22. Code quality of LVM is good, but Dragon book may not be suitable for compiler study.


## Idioms for Building Fault-tolerant Applications with Elixir • José Valim • YOW! 2021

URL: [https://www.youtube.com/watch?v=mkGq1WoEvI4](https://www.youtube.com/watch?v=mkGq1WoEvI4)

 1. Elixir, a functional programming language, combines functional principles with the Erlang VM (BEAM) for efficient distributed applications.
2. Functional programming helps by making state explicit and immutable, improving code clarity and reducing issues with concurrency.
3. BEAM was designed to solve specific use cases like telecommunication systems, enabling high concurrency.
4. Elixir uses lightweight processes that are isolated by default for efficient concurrent applications.
5. Processes communicate through message passing, ensuring fault tolerance as failure in one process doesn't affect others.
6. Phoenix is an Elixir web framework built on these principles, using processes and supervision trees to manage applications.
7. Elixir's accessibility allows libraries like Acto for database interaction and NX for numerical computing on GPUs.
8. Focus on productivity through first-class documentation, tooling, and community support.
9. Hex package manager provides access to various libraries and frameworks like Phoenix for web applications and Nerves for embedded software.
10. Pinterest case study: reduced servers by 95%, improved performance and reliability, saving $2 million annually in server costs.


## A Tour of the Modern Java Platform • James Ward & Ryan Knight • GOTO 2022

URL: [https://www.youtube.com/watch?v=BU_zIpQI5Dg](https://www.youtube.com/watch?v=BU_zIpQI5Dg)

 1. Modern Java includes features like algebraic data types, product types (represented by records), and sum types with sealed interfaces for improved type safety and handling complexity.
2. Testing for records in Java 17 is discussed as an improvement.
3. Algebraic data types (ADTs) and sum types are introduced with sealed interfaces, enabling exhaustive pattern matching.
4. Kotlin handles null values better with explicit nullability and forcing developers to handle null cases.
5. Option types in Scala and Kotlin provide some (value exists) or none (no value).
6. Test containers automatically manage service dependencies for different services like PostgreSQL, providing consistency across environments.
7. R2DBC and Spring support non-blocking database connections with reactive databases like PostgreSQL.
8. Kotlin co-routines allow efficient resource usage by avoiding thread blocking.
9. Reactor Crud repository provides a reactive interface to non-blocking database access.
10. Test containers can be used for local development and integration testing, ensuring consistency across environments.
11. Spring Boot uses build packs to containerize applications for easy deployment on platforms like Kubernetes.
12. Container images are created with layers for operating system, JVM, dependencies, and application.
13. Cloud Native Build Packs can be used to turn any Java application into a container image.
14. Docker is used to run the application and check its performance.
15. GraalVM native image allows ahead of time compilation, reducing memory usage and startup times.
16. Spring Native addresses challenges with reflection in AOT compiling.


## What’s New in F# 5.0 & Beyond • Don Syme • YOW! 2021

URL: [https://www.youtube.com/watch?v=1cqvmiaj6SI](https://www.youtube.com/watch?v=1cqvmiaj6SI)

 1. F# is a functional programming language designed for the .NET ecosystem, bringing benefits to both object-oriented and functional communities.
2. The history of programming languages includes the object-oriented tidal wave, impacting Microsoft and functional programming communities.
3. Reactions to this wave include developing object calculi, integrating functional features into OOP languages, and creating multi-language runtimes.
4. F#'s core remains consistent throughout its evolution, focusing on functional programming experiences for the .NET ecosystem.
5. Object-oriented programming (OOP) has influenced the industry with languages like C++ and Java, while functional programming led to languages like F#, Scala, and C# incorporating functional features.
6. F# is an open source, cross-platform language suitable for JavaScript development using tools like Fable. It offers high performance due to its integration with ASP.NET Core.
7. Functional programming has become more practical, interoperable, reusable, and tooled over time.
8. F# is available on Linux as an open source, cross-platform tool chain with a functional first approach, high performance, and interoperability.
9. Fable allows using F# in the Node.js ecosystem. Functional programming leads to safer languages like F#.
10. The language design process is open for contributions from various communities.
11. F# 4.1 introduced unboxed tuples, records, and union types for better performance. F# 5.0 added span of T, a low-level feature for high-performance code. Tooling updates focused on improving async debugging.
12. F# 4.6 improved record types with anonymous support, while F# 4.7 enhanced computational expressions and syntax for whitespace.
13. F# history focuses on functional programming, interoperability, and performance, combining static typing, succinctness, scalability, explorative libraries, and efficiency.
14. Domain modeling in F# is relevant to areas like theorem proving, with a focus on domain data structures and metalanguage for programming over them.
15. The F# Advent calendar showcases various uses of the language. Functional programming is relevant to user interface development, especially with languages like Elm.
16. Not all functional code is good; Curry and uncurrying can lead to confusing code. Focus on writing clear, debuggable code instead of using advanced functional features.
17. Embrace object programming over full object orientation in F#. Introduce computation expressions for powerful and intuitive code. Prioritize clear, readable, and practical functional code. Learn from the Udemy course to learn F# effectively.


## Spring Boot: Up & Running • Mark Heckler & Thomas Vitale • GOTO 2022

URL: [https://www.youtube.com/watch?v=F0BJiE2LnpQ](https://www.youtube.com/watch?v=F0BJiE2LnpQ)

 1. Mark Heckler, a Principal Engineer at Microsoft, shares his passion for aviation and its relation to software development.
2. The importance of trusting software in critical domains like aviation is discussed, emphasizing the need for reliable and resilient data, hardware, and software.
3. Mark wrote "Spring Boot: Up and Running," a book covering Spring Boot fundamentals and best practices. It serves as a comprehensive guide for developers learning about the framework while also being a reference for experienced users.
4. The challenges of writing a technical book are mentioned, including balancing workload and perspective.
5. Spring Boot is considered a game changer in the Java ecosystem by simplifying development and focusing on business logic.
6. Mark's experience with Spring Boot highlights the importance of perspective when evaluating code and features.
7. Spring Boot was a game changer for developers, allowing them to focus on business logic instead of infrastructure.
8. The transition from Java EE to Spring can be disconcerting initially due to reduced boilerplate code.
9. Spring framework and Spring Boot provide opinionated ways of doing things while still being flexible.
10. Learning about Spring Boot's features, such as dependency management, auto-configuration, and data integration, helps newcomers understand how it works.
11. Technology is the foundation of Spring, a rigorous framework. The book focuses on Spring Boot fundamentals and data integration with various databases.
12. Aviation domain is used for live data examples in the book. Reactive programming is covered, allowing developers to build scalable, resilient, and cost-efficient applications using the same programming model as imperative.
13. Benefits of reactive programming are discussed, including its potential to be more natural for some developers.
14. Spring security is another important topic covered in the book, focusing on abstractions used by the framework. It covers forms-based authentication, OpenID, OAuth2, and authorization concepts.
15. The importance of understanding nonfunctional requirements like security is emphasized.
16. Spring Boot simplifies building production-ready applications with embedded servers and executable standalone Java apps. Native compilation is an important part of the story but not all workloads will go native.
17. Spring Boot offers various deployment options, including executable JARs, container-based applications, and native images in containers. Upgrading to newer versions of Spring framework improves performance even without using native code.
18. Testing is crucial for development life cycle, but balancing testing coverage with the topic being covered can be challenging.
19. Configuration options for Spring Boot applications are discussed. Mark Heckler recommends his book "Spring Boot: Up and Running" as a valuable resource for learning about Spring Boot.
20. Twitter is the best way to reach Mark Heckler online. The conference speakers thank each other and look forward to future discussions.


## The Quick Python Book • Naomi Ceder & Luciano Ramalho • GOTO 2022

URL: [https://www.youtube.com/watch?v=7CwmUmQjvYg](https://www.youtube.com/watch?v=7CwmUmQjvYg)

 1. Naomi Sidder's "The Quick Python Book" covers various aspects of data processing and handling, including ETL, FTP servers, APIs, databases, and data science tools like Pandas and Jupyter.
2. The book is a great starting point for learning Python, with many readers finding success in their careers after using it.
3. The third edition includes an extensive case study involving parsing data.
4. Discussions on the use of functions and classes in programming: Functions are basic concepts, while classes are advanced. Overemphasizing classes can be problematic for beginners.
5. Static typing is not covered in depth in some Python books but is an evolving area within the language.
6. The community's diversity makes it difficult to determine the best approach for everyone; static typing may not be essential for all users.
7. For those who don't need static typing, learning other relevant skills could be more beneficial.
8. Python's success is due to its focus on aesthetics, readability, and community, with a diverse library ecosystem similar to CPAN in the past.
9. Syntactic macros (PEP 638) are an idea that allows easier experimentation with language features without rewriting code; they could be used for implementing new features like sync awaits and match case statements as library keywords instead of deep interpreter changes.


## Growing Together with the BEAM • Stavros Aronis & Hans Nahringbauer • Code BEAM 2022

URL: [https://www.youtube.com/watch?v=OXlC6f8indM](https://www.youtube.com/watch?v=OXlC6f8indM)

 1. Telaes is a Nordic contact center solution provider that uses Erlang for its robustness, cost efficiency, and scalability.
2. Ace has over 96,000 users and handles millions of interactions annually with the help of Erlang-based systems.
3. The company has been using Erlang since 1997 and continues to build new solutions on it.
4. Telaes utilizes natural language understanding and other technologies for their solutions.
5. First system created for Destination Gotland with 70 agents, using Alan on Windows Server and now running in the cloud.
6. Convinced sponsors to use Alan due to lower cost and robustness.
7. Rewrote code in 2000, used Angelo for routing calls and managing states.
8. Introduced virtualization with VMware for better redundancy.
9. Created Ace Clusterware for handling web clients and scaling.
10. Adopted JavaScript and Angular for client structure.
11. Clusterware maintains state, synchronizes, and communicates with existing systems.
12. Telia's journey involved building a new recording solution and IVR system using AWS cloud services.
13. Clusterware remains in the middle, handling routing and connecting to telco systems.
14. Telia's cloud migration involves AWS and integrating with Microsoft Teams.
15. There's a movement back to on-premise data centers due to regulatory issues.
16. Telia is building new modules for IVR and recording, using partners like Avasa.
17. Google Cloud AI Platform (CCAI) helps virtual agents solve customer problems.
18. Agent Assist will coach live agents during calls or chats.
19. Insights feature uses interaction analytics to understand conversations.
20. Global uses Google CCAI platform for natural language processing.
21. Virtual agents empowered by the Google CCAI engine help customers solve issues and transfer to live agents if needed.
22. Agent Assist is added to coach or help agents during interactions.
23. Insights feature provides interaction analytics to improve entire companies' workings in real time.
24. Erlang played a crucial role in the success of their cloud service.
25. Global has offices worldwide, with around 250 employees and 80 developers working on development.


## Expert Talk: What’s Next For .NET? • Hannes Lowette & Martin Thwaites • GOTO 2022

URL: [https://www.youtube.com/watch?v=vzywu1ol-b8](https://www.youtube.com/watch?v=vzywu1ol-b8)

 1. Over the past two decades, .NET has evolved significantly, with notable changes in compatibility and technology.
2. The transition from .NET 1.1 to 2.0 introduced challenges due to compatibility issues.
3. Documentation improvements have made learning easier for newcomers.
4. WebForms had its challenges but helped bridge the gap between desktop developers and web development.
5. MVC and other frameworks simplified workflows, lowering barriers for smaller applications.
6. .NET Core focuses on performance and web development, with a strong emphasis on cross-platform support.
7. Dependency injection is now a first-class citizen in the ecosystem.
8. Minimal APIs make it easier for new developers while still allowing traditional approaches.
9. The language specification remains unchanged throughout .NET's evolution.
10. Maintaining backward compatibility with older frameworks and technologies like Core WCF is crucial.
11. Focusing on the future, leaving past issues behind, is essential for continued growth.
12. MVC's approach with extensibility and dependency injection benefits developers.
13. WCF was overengineered but still useful due to its powerful tools.
14. Core WCF aims to maintain backward compatibility for those who prefer older technologies.
15. Converting from WCF to gRPC can be challenging, requiring significant codebase changes.
16. .NET Core focuses on making the right thing easier and more accessible.
17. Logging frameworks like ILogger are now standardized, reducing custom solutions' need.
18. Containerization has changed how applications are deployed and monitored.
19. Application Insights offers visibility into production code but requires manual instrumentation for better insights.
20. New Relic and similar tools provide out-of-the-box visibility on performance numbers and metrics without log statements.
21. The DevOps movement has pushed developers to care about their production environment and system outputs.
22. Observability is crucial for understanding system performance and debugging issues in complex distributed systems.
23. Instrumentation can help identify problems by monitoring code execution instead of logging everything.
24. Overengineering may occur due to software complexity, but keeping it simple is recommended.
25. OpenTelemetry could revolutionize how we look at code in production with standardized ways of collecting and analyzing data.
26. The .NET ecosystem's rapid evolution makes it an exciting time for developers.


## Life After Business Objects: Confessions of an OOP Veteran • Vagif Abilov • GOTO 2021

URL: [https://www.youtube.com/watch?v=Q2p_iqjfekI](https://www.youtube.com/watch?v=Q2p_iqjfekI)

 1. Object-oriented languages may have insufficient default implementations, causing issues for new developers.
2. Functional programming offers cleaner code and clear intentions, with immutable data structures making concurrency easier.
3. Learning from others' mistakes is crucial for improving code quality; metrics show the importance of considering future developers and readability.
4. Separating data and operations in business objects can solve visibility issues; focus on them as different entities.
5. Real-world examples highlight the need for subjective decisions regarding method placement.
6. Discussions cover handling order processing, organizing classes/data types, and the importance of algebraic data types (ADTs) in functional programming languages like F#.
7. Caution against using optional values in domain models; hybrid approaches combining object-oriented and functional programming are possible, but F# offers a better full functional experience.
8. Consider mutability when choosing a language for specific needs; compare OOP and actor models, highlighting the advantages of the latter.
9. Use types to keep domain models tight, compact, and easy to understand; avoid nulls and options with the principle of making illegal states unrepresentable.
10. Utilize modules for better visibility of operations and avoid exposing unsafe ones; adopt functional programming communication between actor model objects using Akka.net.
11. Observe responsiveness to quick changes, compact code, and strong type checking in F#.
12. Use communication channels to contact the speaker or vote for their session on a conference app.


## Ready for Rust • Erik Doernenburg • GOTO 2021

URL: [https://www.youtube.com/watch?v=WgLlwjZNEtY](https://www.youtube.com/watch?v=WgLlwjZNEtY)

 1. Rust is a modern programming language gaining popularity due to its safety and efficiency, attracting interest from companies like Microsoft.
2. Apple, Google, and Mozilla created their own alternatives to C: Swift, Go, and Rust respectively.
3. Companies struggle with writing secure C code due to memory management issues, leading them to consider languages like Rust for its safety and interoperability.
4. Rust's toolchain installation is simple, and cargo is an effective package manager.
5. The language focuses on keeping dependencies small for security and performance.
6. Rust supports multiple editions to target older versions of the language.
7. A genetic programming simulator was used as a real-world example to demonstrate building something in Rust.
8. Rust is ideal for long-lived, large code bases that require a more complex programming language.
9. The language supports object-oriented and functional programming styles.
10. Macros allow extending the language's functionality.
11. Memory management uses automatic reference counting to avoid memory leaks.
12. Passing references to functions avoids ownership issues.
13. Immutable and mutable references are allowed, preventing data races.
14. Dangling pointers are not allowed in Rust.
15. Functions can be passed as parameters for abstraction.
16. Rust's borrow checker ensures data race avoidance and semantic correctness.
17. Parallelism is easier in Rust compared to other languages due to explicit multi-threading and memory management.
18. The language was used to improve performance of a simulation application, achieving 25 million cycles per second with an optimized build.


## #FAIL • Kevlin Henney • GOTO 2021

URL: [https://www.youtube.com/watch?v=Lc13xKEJZTc](https://www.youtube.com/watch?v=Lc13xKEJZTc)

 - Software development involves time travel, allowing undoing actions and exploring different timelines.
- Facebook's use of user feedback led to political interference.
- C library's time function can cause systems to default to January 1st, 1970, due to generating value zero.
- Nan (not a number) is a feature of IEEE 754 from the '80s; it can be generated by various languages.
- Prototype code vs production-ready code: When to consider it ready for use.
- Failure of state modeling in software development.
- Defect-driven testing (DDT) helps fix bugs and increase traceability.
- Importance of understanding and learning from past successes in software development.
- Testing is crucial for preventing failures, even if not detecting everything in advance.
- DDT helps increase knowledge and traceability.
- Validate data and check it as it comes in to avoid issues like buffer overruns.
- Keep code simple for correctness; focus on attention management during development.
- Importance of clear code and attention management in programming.
- Binary search algorithm issue discovered in 2006, present since 1983.
- Muffet's law: Correcting others' work often leads to errors.
- Avoid being too clever with code; let the compiler optimize.
- Humility is key when writing code.
- Understand the context of your code and how it interacts with other systems.
- Collective intelligence is crucial for software development.
- Consider safety critical aspects when designing systems.
- Review code from different perspectives and learn from past failures.
- 1996 Ariane 5 launch failure due to hardcoded values in code.
- Code reuse from Ariane 4 led to dead code in Ariane 5, causing issues.
- Assumptions are crucial but difficult to identify until contradicted.
- Dead code can lead to significant losses.
- Configuration errors can be latent and go undetected for long periods.
- Configuration is often considered separate from source code, but it's part of the system.
- Flight control system issue due to incorrect settings for mission originating from a new launch site.
- Configuration errors are often not detected until late, and people tend to downplay their significance.
- Spreadsheets can be considered functional programming systems with issues in type systems that invite errors.
- Excel now supports Turing completeness with lambda functions.
- Gene name conversions in scientific literature have caused problems due to automatic conversion by excel.
- Earth's temperature averages are defined using the arithmetic mean, and choosing different methods can lead to varying results.
- Scientific literature has seen issues with gene name conversions in Excel.
- Errors in Excel can lead to significant changes in scientific practices.
- Earth's temperature averages are crucial for understanding climate change.
- A critique of climate deniers showed how incorrect calculations led to misleading results.
- Spreadsheet errors can have major consequences, such as austerity economics and potential deaths due to health budget cuts.
- Learning from past mistakes requires conscious effort and acknowledging the importance of practices.


## Expert Talk: gRPC, Kubernetes & .NET • Mark Rendle & Matt Turner • GOTO 2022

URL: [https://www.youtube.com/watch?v=vzqzLSJWo3k](https://www.youtube.com/watch?v=vzqzLSJWo3k)

 1. Matt shares his recent experience at QCon, focusing on API gateways, service meshes, and shift left tooling for API development.
2. The importance of defining APIs upfront is discussed, along with tools like Swashbuckle and Nswag for generating documentation and client libraries.
3. Matt highlights gRPC as a powerful option in .NET, offering fast implementation and virtual method overriding features.
4. Challenges of load balancing in HTTPClient are mentioned, with potential improvements in future versions of .NET.
5. gRPC implementation in C# offers a base class for service inheritance and virtual methods.
6. Service mesh like Istio provides additional features but can be complicated to set up; Linkerd is more opinionated and easier for most cases.
7. gRPC combines transport, encoding, and HTTP 2 multiplexing with generated stubs for messaging.
8. API built on top of gRPC can be RPC or REST/CRUD style.
9. Discussed the benefits of gRPC, Istio, and Linkerd, along with monitoring and observability tools like Open Telemetry.
10. Tracing is highlighted for visibility into network calls and application performance.
11. The evolution of computing technology from mainframes to cloud services is discussed, including platforms like Kubernetes.
12. Terraform's declarative approach is praised, while Pulumi's logic-based API calls are criticized. Crossplane is introduced as a potential solution for managing cloud resources with reconciliation loops.
13. PolyScale is described as a startup providing cloud database services as a proxy/cache in front of databases to reduce load and improve performance.
14. Kubernetes' evolution from mainframe scheduling systems is mentioned, offering distributed computing capabilities.
15. Different implementations of Kubernetes are discussed, including micro k8s, k3s, k0s, minikube, OpenShift, etc., all based on the same code and API standard.
16. The complexity of Kubernetes can be challenging for some users but provides a wide range of possibilities for various applications.
17. Updating software in a cluster is addressed, with Kubernetes handling complexity well. Smaller distributions like CoreOS or Flatcar are mentioned as alternatives for rolling updates.
18. Microsoft's implementation of gRPC in .NET 7 allows browsers to talk to gRPC services.
19. Discussion on middleware standards in .NET and how it evolved over time, along with comparisons of different languages like Kotlin and Rust.
20. Challenges with Rust's lifetime feature are mentioned. Appreciation for modern compilers providing more helpful error messages is expressed.
21. Discussions on coding standards, syntax highlighting, and IDEs are touched upon.
22. Comparison of different programming languages and their evolution is addressed.
23. DOS's abort, retry, ignore, and cancel options are mentioned.
24. A new comedy project on programming's greatest mistakes is introduced.


## Did We(b Development) Lose the Right Direction? • Stefan Judis • GOTO 2021

URL: [https://www.youtube.com/watch?v=3PmPkZJ22Cc](https://www.youtube.com/watch?v=3PmPkZJ22Cc)

 1. The speaker's journey in web development over the years has seen the emergence of frameworks like Angular 1 and React.
2. A personal blog example highlights the importance of performance, with a high Lighthouse score but slow page load time.
3. Mistakes made by the speaker include shipping too many JavaScript files, large index HTML file, and not considering lazy loading.
4. Lighthouse performance score is calculated based on speed index, accessibility, SEO, and best practices.
5. Optimizing websites for better user experience and search engine ranking is crucial.
6. JavaScript's importance to Google lies in its impact on user experience and website speed.
7. Aim for a simple, pure approach in web development for better performance.
8. Universal Javascript apps can be optimized through code splitting and lazy loading.
9. Static site generators like 11ty help create websites with high Lighthouse scores.
10. Focus on user benefits rather than adding unnecessary features to a website.
11. Complex universal JavaScript apps for content sites can slow down user experience.
12. Progressive enhancement ensures basic functionality works without JavaScript.
13. React's redesign and rebuild may not significantly improve user experience.
14. Sending more data for the same experience can harm user experience in regions with limited mobile contracts.
15. A website called "What does my site cost?" shows how much loading a specific site costs in different parts of the world.
16. Excessive JavaScript usage can harm user experience.
17. Gmail is an example of a site with high JS usage but good experience.
18. Client-side navigation breaks accessibility for assistive technology.
19. New proposals like document transition aim to improve the situation.
20. Astro and Svelte are frameworks that focus on reducing JavaScript usage.
21. React teams are working on improving server-side components.
22. A great site should just work, focusing on HTML, CSS, and JavaScript foundations.
23. Challenges of modern web development include complexity, accessibility, security, and simplicity.
24. Understanding HTML basics and avoiding unnecessary frameworks is crucial.
25. Use tools like Netlify, Vercel, and serverless functions to simplify development.
26. Focus on building sites that just work rather than worrying about the technology powering them.
27. There's a divide between front-end developers who focus on JavaScript frameworks and those who prioritize UX and CSS architecture.
28. Developers should consider the trade-offs of technology choices before using them.


## Expert Talk: Native vs Cross-Platform • Sebastiano Poggi & Carl-Gustaf Harroch • GOTO 2022

URL: [https://www.youtube.com/watch?v=cNXDpl-rfrM](https://www.youtube.com/watch?v=cNXDpl-rfrM)

 1. Choosing between native or cross-platform apps depends on factors like product needs, company capabilities, and organizational structure.
2. Native apps may be better for complex features tied to specific platforms, while cross-platform frameworks can save time and resources.
3. Organizational dysfunction can lead to problems in mobile app development, such as misaligned priorities between tech and product teams.
4. Back-end APIs might not consider mobile app needs, leading to issues like lack of offline support or inefficient data usage.
5. Mobile apps are proactive and event-driven, requiring different API design compared to web applications.
6. Collaboration between teams from the start is crucial to avoid mismatched expectations.
7. Vertical teams that work closely together can help prevent issues caused by disconnected teams.
8. Different approaches to team structure have been tried, with varying success.
9. Vertical teams that work closely together can be more effective than separate back-end and front-end teams.
10. Communication is key for successful collaboration between different teams.
11. Cross-functional teams may not always work well due to individual preferences and skillsets.
12. Microservices can help create structure within cross-functional teams, but they can also lead to fragmentation over time.
13. Teams working together on Android and iOS platforms are possible with constructive collaboration and shared goals.
14. Business models can complicate matters when revenue is involved, as each platform may have different performance metrics.
15. Discussing the challenges of native app development between iOS and Android platforms.
16. Importance of understanding target audience for each platform.
17. Suggestions to improve collaboration include code reviews, shared language, and cross-platform thinking.
18. Cross-platform frameworks allow a single team to target both platforms using a single language and build tools.
19. Flutter is an example of a successful cross-platform framework, with growing usage in the mobile industry.
20. React Native and Xamarin are also mentioned but have different communities and focuses.
21. Declarative UIs are becoming a big trend in native mobile development.
22. Kotlin and Swift UI may bring Android and iOS closer in terms of UI development.
23. It's unlikely for Google to adopt Swift or Apple to adopt Kotlin, but their mindsets could become more similar.


## Programming Language Stereotypes • PJ Hagerty • GOTO 2021

URL: [https://www.youtube.com/watch?v=3o_nCe67wA4](https://www.youtube.com/watch?v=3o_nCe67wA4)

 - Misconceptions about programming languages and identities.
- Ruby is beautiful, not synonymous with Rails; it's used by big companies like Netflix, Zendesk, IBM, etc.
- Perception of open source developers as building trivial apps.
- Ruby on Rails is a framework, not the language itself.
- PHP powers about 70% of the internet despite misconceptions around its speed and security.
- Java remains popular despite being considered dead by some young developers.
- Python has uses beyond academia and analytics.
- Linux has commercial applications and is enterprise ready.
- Pearl's perception of being dead might be due to lack of updates, but it still exists with version 6 released in 2014.
- Don't limit yourself to one programming language; explore various options.
- Importance of communities in tech industry: break out of silos, learn from others, attend meetups, conferences, and online events outside your usual community.
- Understand other developers' needs and incorporate their ideas into your work.
- Build a greater tech community through collaboration.
- Importance of cross-pollination between different tech communities: open source and enterprise developers can learn from each other.
- Recognize and eliminate biases to improve collaboration.
- Focus on teaching, mentoring, and sharing knowledge with others.
- Encourage diversity in hiring and team building.
- Discusses the use of unrealistic job titles like "rock star wizard ninja": focus on work, not myths or legends.
- Mentor people from diverse backgrounds to improve diversity.
- Inclusion of diverse perspectives leads to better products and a more inclusive workplace.


## Expert Talk: Functional Programming • Russ Olsen & Christian Romney • GOTO 2022

URL: [https://www.youtube.com/watch?v=AbCWHZljhkM](https://www.youtube.com/watch?v=AbCWHZljhkM)

 1. Functional programming is a different approach to building programs, making them simpler and easier to understand.
2. Pure functions are the foundation of functional programming; they don't have side effects or depend on external state.
3. The goal is to minimize side effects in a program while achieving desired results.
4. Misconceptions about functional programming include it being overly complex and requiring extensive study before understanding.
5. Functional programming is about producing side effects but using them as little as possible.
6. Misconceptions include the idea that functional programming is complex and requires deep understanding of terminologies from mathematics.
7. To understand functional programming, you only need pure functions, immutable data structures, and efficient ways to handle these concepts.
8. Category theory isn't necessary for understanding functional programming; it may be more relevant in languages with strong typing.
9. The speaker started as a mechanical engineer but found programming more enjoyable and began exploring how programming languages work.
10. Transitioning from object-oriented to functional programming can be liberating, simplifying the process.
11. A disastrous project example: Rewriting a C++ program into a functional style could have made it easier to understand and work with.
12. Functional programming helps avoid getting lost in tools and infrastructure of programs.
13. Functional programming can help avoid certain bugs and simplify code changes.
14. Immutable data structures and pure functions make code more predictable.
15. For new functional programmers, start with a familiar problem and learn by solving it in a functional way.
16. Find an interesting, medium-sized problem and write a functional program to solve it.
17. Understand the details of the problem and focus on solving it in a different way.
18. Learning a new programming style helps in understanding a new language.


## Live-Coding a Dashboard with KSQL, Python & JavaScript • Kris Jenkins • GOTO 2021

URL: [https://www.youtube.com/watch?v=8bPDiuJGGh0](https://www.youtube.com/watch?v=8bPDiuJGGh0)

 1. The speaker is building a live dashboard for streaming sales data using various technologies.
2. He connects to a Kafka database, which acts as an event stream and can be summarized into a static table.
3. A one-row summary table is created from the Kafka database, showing real-time updates.
4. The speaker writes a Python websocket server to connect to the Kafka database and stream data.
5. He uses packages like websockets, simplejson, and confluent kafka drivers for development.
6. The speaker plans to expand the connection handler function to handle more complex tasks.
7. Key features include creating a Python websocket server using the websockets library, connecting to Kafka database, handling different message types, configuring consumer settings, deserializing data with schema registry, and broadcasting updates to clients.
8. The speaker also addresses issues like race conditions, connection messages, and frontend development.
9. He connects the web app to the websocket server, parses JSON data for display on the dashboard, and emphasizes the importance of quick internal tools for easy data access.
10. Suggestions include considering Kafka for real-time data streaming in systems.


## Expert Talk: Web Development & Its Failures • Kevlin Henney & Stefan Judis • GOTO 2021

URL: [https://www.youtube.com/watch?v=jQ0_bIVhkLk](https://www.youtube.com/watch?v=jQ0_bIVhkLk)

 1. Lars introduces Stefan and Kevlin, who discuss the current state of web development.
2. Stefan highlights the increase in complexity and performance issues due to JavaScript dominance.
3. Google's Lighthouse is pushing for better performance, leading to a potential shift towards simpler solutions.
4. Kevlin emphasizes understanding dependencies and their consequences on security, performance, and software agility.
5. Complexity in software development leads to issues like performance, security vulnerabilities, and reduced agility.
6. Dependency management is crucial, but responsibility lies with everyone involved: developers, tool vendors, site providers, etc.
7. Cultural shifts within companies can help improve practices such as reducing dependencies, updating them regularly, and prioritizing good user experiences.
8. Numbers and data are essential for understanding the impact of these issues and driving change.
9. Importance of responsibility in data and software engineering.
10. Need for collective understanding and culture within teams.
11. Learning from past incidents like the Left Pad event.
12. Striving for self-containment and awareness of dependencies.
13. Desire for frameworks to offer simpler solutions for less experienced developers.
14. Maintain simplicity in code and consider trade-offs.
15. Don't always go for the latest technology.
16. Be aware of changing needs over time.
17. Legacy code can be good, but the world around it may change.
18. Slow down and evaluate decisions carefully.
19. Importance of slowing down and being aware when making decisions.
20. Trade-offs change over time, what was good before may not be now.
21. Awareness is key to understanding the context and relevancy of decisions.
22. Responsibility comes with adopting dependencies in code.
23. Balancing between duplication and dependency avoidance.
24. JavaScript ecosystem has evolved rapidly, leading to duplication and reinventing patterns.
25. People tend to copy code from others when learning, which can lead to duplication.
26. Tooling can help with awareness and identifying duplicate code.
27. Communication and group intelligence are crucial for addressing duplication issues.
28. There's no one-size-fits-all solution; it depends on the context and team dynamics.
29. Duplication is not always bad; it can help identify patterns and abstractions.
30. Tools should extend human capabilities, not define the way of working.
31. Learning from observations and iterations is crucial for understanding code.
32. Keep an eye on potential issues without making premature decisions.


## The Ideal Programming Language • Richard Feldman & Erik Doernenburg • GOTO 2021

URL: [https://www.youtube.com/watch?v=MPyUvtPFDSg](https://www.youtube.com/watch?v=MPyUvtPFDSg)

 1. Ideal programming languages depend on the problem domain.
2. Richard and Erik prefer functional programming, but appreciate the benefits of object-oriented programming.
3. They value ergonomic type systems with helpful error messages, automatic memory management, and languages that allow both functional and object-oriented programming.
4. Some people struggle to adapt to new languages due to familiarity with existing patterns.
5. Functional programming can be useful for transforming data between different systems.
6. Humans enjoy classification, but it may not always benefit code productivity.
7. Premature abstraction and overuse of inheritance can lead to inefficiencies.
8. Testability should be considered during language design.
9. Rust's approach to package manager and unit testing integration is an inspiration for other languages.
10. Discussions on language design, focusing on testability and memory management.
11. Rust's package manager and unit testing integration are seen as positive examples.
12. Automatic reference counting (ARC) is considered less appealing than tracing garbage collection due to GC pauses.
13. Compiler time ARC detection in languages like Roc is being explored.
14. Apple's focus on automatic reference counting for Swift, potentially influencing hardware optimization.
15. Cyclical dependencies and their impact on memory management are discussed.
16. Apple's hardware-level optimizations for automatic reference counting could influence other processor makers.
17. Elixir and Erlang have a powerful concurrency model, suitable for distributed systems.
18. SIMD (Single Instruction Multiple Data) is an efficient low-level data parallelism technique used in some languages like SIMD JSON.
19. Rust, Roc, and Zig are upcoming languages with different approaches to solving similar problems.
20. Discussed parallelism, specifically low-level data parallelism on CPUs using SIMD.
21. Zig and Roc languages mentioned as up-and-coming alternatives to Rust for specific niches like game development.
22. WebAssembly's potential impact on web application programming languages is being watched closely.
23. Elm and Roc can compile to WebAssembly, with Roc already doing so.
24. Predictions suggest WebAssembly might mainly affect games in the near future.
25. Discussion on programming languages and web development.
26. WebAssembly is seen as a promising step towards using any language in the browser, but not necessarily improving performance.
27. JavaScript, CoffeeScript, and TypeScript have strong cultural momentum.
28. In-house applications may benefit from WebAssembly and alternative languages like C# (Blazor).
29. Performance is important for web browsers but not the main factor driving change.
30. Large organizations with in-house apps could be more open to new technologies.


## Programming: Now & Then • Eamonn Boyle & Garth Gilmour • GOTO 2021

URL: [https://www.youtube.com/watch?v=52jnUWrO9i8](https://www.youtube.com/watch?v=52jnUWrO9i8)

 1. Three old men discuss changes in the industry over time.
2. Access to open source and community editions has allowed self-education at home, making learning more accessible.
3. Work-life balance varies for individuals; some prefer socializing with colleagues while others enjoy working from home.
4. Learning resources were limited in the late '90s compared to today's online tutorials and community editions.
5. Self-education using open source and community editions is seen as a positive change.
6. The transition from physical documentation to online resources has made self-education easier.
7. Companies value capabilities over paper credentials, with certifications still holding some monetary value.
8. Cloud computing may lead to a shift in learning paradigms, potentially requiring on-site training for serverless learning.
9. Product management becomes increasingly important as users expect quality features and interactivity.
10. Energy consumption could influence future programming languages and platforms.
11. Serverless architecture offers scalability and better resource utilization but may lead to less efficient code execution.
12. Discussions about early programming experiences with different machines and their limitations.
13. Comparison of modern programming languages to older ones, highlighting the importance of understanding memory management for efficiency in certain professions.
14. Nostalgia for the past and appreciation for current advancements in technology.
15. Discussions on the evolution of computer science and industry needs.
16. The importance of understanding memory, algorithms, and mathematics in computer science education.
17. The need for segmentation within the IT industry to cater to different subgroups.
18. Comparison between current programming and early computing methods.
19. How each generation faces different challenges and problems.
20. Discussions on how technology has evolved and the impact it has had on different generations.
21. The importance of being grateful for the privileges in the IT industry, while acknowledging the stresses involved.
22. Philosophy's role in IT as people gain more experience and refine their understanding of fundamental principles.


## Erlang, the Hidden Gem: Solving Problems at Scale for 30+ Years • Francesco Cesarini • GOTO 2021

URL: [https://www.youtube.com/watch?v=-m31ag9z4VY](https://www.youtube.com/watch?v=-m31ag9z4VY)

 - Erlang Solutions' Francesco Cesarini discusses the history and features of Erlang.
- BEAM virtual machine is highly optimized for large-scale concurrency, featuring a JIT compiler.
- OTP abstracts from concurrency models, increasing productivity and ensuring resilience by default.
- Elixir runs on the same VM as Erlang, expanding its reach to more developers.
- Fault tolerance in OTP is achieved through processes not sharing state or memory, allowing termination of faulty processes without affecting others.
- The inventor of Erlang aimed to make it accessible for a wider range of programmers, initially focusing on web developers.
- Attempts to bring Erlang to the web failed due to different requirements and toolings needed for telecom and web development.
- Akka framework was inspired by OTP but lacks full emulation of BEAM semantics.
- BEAM runs a scheduler for every core on a machine, ensuring fair distribution of processes across threads and migration between them.
- Lua framework allowed running Erlang on iPhones but didn't make it into production.
- Elixir is making its way into embedded spaces like IoT devices and cars due to performance improvements in JIT compiler and numerical capabilities.
- The original Erlang language evolves very little, with most changes happening around libraries, frameworks, and the BEAM virtual machine.


## Functional Programming for Pragmatists • Richard Feldman • GOTO 2021

URL: [https://www.youtube.com/watch?v=3n17wHe5wEw](https://www.youtube.com/watch?v=3n17wHe5wEw)

 1. Functional programming is a style that avoids mutation and side effects, focusing on immutability, pure functions, and functional languages.
2. Pure functional languages support only pure functions, which ensure predictable behavior and enable caching techniques like memoization.
3. Performance advantages of functional programming include caching, pre-computing, and parallelization; disadvantages include increased memory usage due to immutability and potential performance issues with recursion.
4. Functional languages focus on immutability, pure functions, and functional programming concepts.
5. Caching strategies include memoization, which is easier to implement with pure functions. Precomputing can be done at build time for known constants or function calls, reducing runtime costs.
6. Parallelization can speed up functional programs but requires thread safety inherent in pure functions.
7. Managed effects offer an alternative to side effects by creating tasks instead of immediately executing actions like promises; this approach improves performance and simplifies code.
8. Pure functional programming offers benefits for development, such as fewer flaky tests due to minimized effects, no need for mocking, and the ability to test effects through simulation.
9. Rearranging code in functional languages is possible without affecting the result. Global mutable variables create implicit dependencies and make debugging difficult; pure functions have explicit dependencies and are easier to debug.
10. Side effects introduce implicit dependencies, increasing search space for bugs. In pure functional programming, explicit dependencies make debugging simpler.
11. Functional programming offers benefits like caching, parallelization, testing, code revision, debugging, and ecosystem advantages. Pure functional languages provide a more reliable experience compared to imperative ones.


## Modernizing Enterprise Java • Markus Eisele, Natale Vinto & Ana-Maria Mihalceanu • GOTO 2021

URL: [https://www.youtube.com/watch?v=tSjCFMSp9oY](https://www.youtube.com/watch?v=tSjCFMSp9oY)

 - Key points for migrating from monolithic to cloud-native applications:
  1. Understand business and non-functional requirements.
  2. Choose the right approach (refactoring is optimal).
  3. Use modern Java frameworks for cloud-native apps.
  4. Monolithic apps can still be useful with well-architected designs.
  5. Pros and cons of monolithic vs microservices architecture discussed.
  6. Kubernetes as a popular operational platform for various workloads, including stateful applications.
  7. Importance of understanding how components work together in cloud native environments.
  8. "Concise Cloud Native Guide" provides practical examples and guidance on migrating Java projects to the cloud.
  9. Readers can choose theory or hands-on experience with examples.
 10. Book focuses on Java migration, rehosting, re-platforming, or complete rewrite decisions.
 11. Challenges in migrating traditional applications include poor architecture, technical limitations, and lack of documentation.
 12. Three approaches to modernization: refactoring, lift and shift, and hybrid (split complexity).
 13. OSGI framework helps build modular monoliths with loose coupling.
 14. Container technology speeds up development and deployment by standardizing application packaging and simplifying infrastructure management.
 15. Three approaches for modernizing applications: refactoring, lift and shift in containers, or hybrid approach.
 16. Container technology brings standardization and portability to application development and deployment.
 17. Challenges in developer productivity with containerized systems.
 18. Improving Java productivity through runtime ecosystems like GraalVM for serverless workloads.
 19. Building and orchestrating apps in containers is a challenge.
 20. The book focuses on being agnostic and open source, improving Java productivity for developers.
 21. GraalVM has advantages for serverless workloads.
 22. Optimization and frameworks are important for Java development.
 23. Containers help with universality and best practices.
 24. Quarkus conserves existing knowledge while scaling.
 25. The book addresses cloud native concepts, focusing on practical aspects rather than theoretical ones.
 26. Authors prefer calling it "Kubernetes native" due to its specific execution environment.
 27. Book aims to provide practical guidance for Java developers in the new era of technology.
 28. Covers various frameworks and technologies while not delving too deeply into each one, offering pointers or links instead.
 29. Authors believe their book is a great starting point for modernizing existing applications and adopting Kubernetes native approaches.


## A TypeScript Fan's KotlinJS Adventures • Eamonn Boyle & Garth Gilmour • GOTO 2021

URL: [https://www.youtube.com/watch?v=9p60bBBpG6A](https://www.youtube.com/watch?v=9p60bBBpG6A)

 1. Evan Boyle and Garth Gilmore, both TypeScript and Kotlin enthusiasts, built a WebGL game in Kotlin JS to compare it with a similar project in TypeScript.
2. IntelliJ provides good support for Kotlin JS development, while Gradle serves as the build system for multi-platform compilation.
3. Dependencies can be managed through regular and npm methods.
4. The speakers found Kotlin JS to be a viable alternative to TypeScript in certain situations.
5. Kotlin's Domain Specific Language (KDSL) is more modern than Groovy, while multi-platform allows compiling common code for various platforms.
6. Integrating with JavaScript libraries is easy using Gradle files and external declarations.
7. TypeScript is popular due to its established nature, easy integration with JavaScript, and automatic generation tool (Ducat).
8. Kotlin's popularity has grown quickly but still needs time to catch up with TypeScript.
9. TypeScript is a superset of JavaScript, making it easier to use and interoperable.
10. Kotlin offers good interop with JavaScript through Gradle files and external declaration files.
11. Ducat tool helps in automatic generation for TypeScript declaration files.
12. Kotlin supports dynamic typing (dynamic) and object creation similar to TypeScript.
13. Kotlin's KDSL can be awkward, but it has a lambda with receiver feature for DSL support.
14. Advanced features of TypeScript include union types, intersections, conditional types, generics, map types, and type inference with generics.
15. Suspending functions in Kotlin make it more versatile than JavaScript for asynchronous programming.
16. Kotlin's syntax is generally considered nicer due to its modern design.
17. Destructuring in JavaScript and TypeScript is more flexible than Kotlin's approach.
18. Both languages have their strengths and weaknesses; it depends on the context and preferences of the developer.
19. Jetpack Compose is a game changer as it provides a single DSL for structuring UIs across different platforms (Android, Desktop, Web).


## How to Read Complex Code? • Felienne Hermans • GOTO 2021

URL: [https://www.youtube.com/watch?v=az-MX_M11lg](https://www.youtube.com/watch?v=az-MX_M11lg)

 1. Many people learned programming through self-exploration, which has influenced how they teach children today.
2. Books for kids often focus on the difficulty of programming and fun in making mistakes while overlooking syntax rules. This stereotype is prevalent among professionals who learned programming at a young age.
3. Python's precision can be misleading, as it requires following rules and syntax. Telling children that programming is hard may discourage them from learning.
4. Research shows that kids often learn programming skills but then flatline. Teaching reading code should be emphasized alongside exploration and experimentation.
5. The Advent of Code focuses on writing small programs, which could be more effective for learning new languages. Reading code is crucial as it takes up 60% of programmers' time.
6. Reading code models can apply natural language processing theories to programming. Short-term memory issues and short-term memory overload can cause confusion in code.
7. Improving reading comprehension involves building mental models, learning programming fundamentals, and practicing reading code. Understanding programming languages and their syntax helps with code reading.
8. Techniques for enhancing code reading include flashcards, state tables, reproducing code, summarizing it, and understanding the goal of a program. The "Programmer's Brain" book offers more insights into improving code reading skills.
9. Starting a code reading club at work can help colleagues learn together. Benefits include team building, knowledge sharing, and deliberate practice.
10. Resources for learning more: Felienne's website (flinders.com), Twitter (@sfelienne), Software Engineering podcast (se-radio.net). Free resources on code reading clubs are available at felina.com/club.


## Java Security & the Java Ecosystem • Nicolas Frankel • GOTO 2021

URL: [https://www.youtube.com/watch?v=uVob-4aXbxY](https://www.youtube.com/watch?v=uVob-4aXbxY)

 1. Changing Java class types is no longer possible in recent JDKs, making it harder to manipulate bytecode for malicious purposes.
2. Attaching a JVM to another can be used for both good and bad reasons; the security manager should apply to all dependencies.
3. Auditing source code and building libraries yourself ensures trust in external dependencies. Untrusted code includes any library or dependency used in a project.
4. Managing transitive dependencies is challenging, but restricting them is recommended.
5. Discussion on security issues in the JVM ecosystem focuses on Java, with concerns about Oracle's approach to feedback and community involvement.
6. Deprecation of the security manager in Java 17 raises concerns for companies relying on it.
7. Stability has been a key factor in Java's success, but its current strategy may be causing issues.
8. Concerns about the future of Java and JVM include community involvement decreasing, Java becoming more centralized affecting adoption, stability replaced by faster release cadence, fragmentation due to module system, and possible negative impact on Java adoption.
9. Suggestions for a middle ground between stability and innovation are needed.


## AccessibleJS • Jemima Abu • GOTO 2021

URL: [https://www.youtube.com/watch?v=9SFSJDIg4KE](https://www.youtube.com/watch?v=9SFSJDIg4KE)

 1. Accessibility is the practice of designing products for everyone to use, regardless of their abilities.
2. Web accessibility focuses on navigation, auditory, visual, sound, and motor capabilities.
3. It's crucial for legal reasons and human aspects.
4. This talk will focus on writing accessible JavaScript.
5. Importance of accessibility: Understanding how people with disabilities use technology.
6. JavaScript and accessibility: Interacting with content, communicating updates to screen readers, and handling navigation for keyboard users.
7. Methods for accessible JavaScript: Using area hidden property, aria live attribute, and custom elements.
8. Example of handling navigation: Creating focusable elements that can be reached through tabbing on a page.
9. Demonstrate how to handle content updates for screen readers.
10. Create custom elements with proper tab indexes and focus management.
11. Use skip to main content links for better user experience.
12. Ensure interaction with your site is accessible through both mouse and keyboard events.
13. Handle handler events in JavaScript: Ensure equal keyboard and mouse events for custom elements.
14. Testing accessibility: Use tools like lighthouse, wave, chromevox, ally.js, and accessibility checklists.
15. Accessibility resources: Check out articles, presentations, and wai-aria authoring practices.
16. Stay updated on accessibility: Join communities, attend conferences, and follow experts for the latest information.


## Object Oriented Programming vs Functional Programming • Dave Farley • GOTO 2021

URL: [https://www.youtube.com/watch?v=-VADIcicpcg](https://www.youtube.com/watch?v=-VADIcicpcg)

 - Programming paradigms have evolved from unstructured languages to structured, object-oriented (OO), and functional programming.
- Each paradigm imposes specific constraints on programming aspects such as flow control in structured programming or assignment in functional programming.
- Different paradigms can coexist within a language, with the choice depending on context and personal preference.
- The value of each paradigm lies in its imposed constraints that help programmers avoid mistakes and write better code.
- Functional programming offers advantages like abstraction, stability, and provability.
- Object-oriented programming (OOP) is more aligned with human thinking and easier to understand.
- Limiting side effects in code is beneficial.
- The speaker disagrees with Bob Martin about finding all programming paradigms.
- A new approach called "reactive" limits synchronous calls between modules, resulting in higher performance than functional or OOP designs.


## Explosive Velocity with a Modern Stack • Tejas Kumar • GOTO 2021

URL: [https://www.youtube.com/watch?v=KTkyQ3z7M8w](https://www.youtube.com/watch?v=KTkyQ3z7M8w)

 1. Explosive velocity in web development involves moving fast and safely with technologies like Next.js, Tailwind CSS, and Typescript.
2. Next.js offers various rendering methods, handles routing, and optimizes code splitting.
3. Tailwind CSS provides atomic classes, auto-completion, and efficient build processes.
4. Typescript compiles ahead of time, offers auto-completion, and protects from errors.
5. Combining these technologies enables fast web development with predictability.
6. Create a project with dependencies for speed across the stack.
7. Initialize tailwind and Next.js to build a simple web page.
8. Transform the page into a basic to-do list app using React.
9. Add input field, button, and handle adding new items.
10. Use React's useState hook to manage state for to-do items.
11. Demonstrate how opinions in frameworks help developers move fast.
12. Create a to-do list app with React, add checkboxes, and manage state using hooks.
13. Utilize Back4App for free backend services.
14. Create a database table for to-do items, query and mutate data from the database.
15. Connect the client to the database.
16. Use GraphQL for efficient data fetching.
17. Added mutation to database, auto-completion helps with parameterized to-do item creation.
18. Fetched to-do items from the database and debugged issues with adding new to-dos.
19. Integrated Tailwind CSS for better UI design.
20. Scalability can be achieved through hosting options like AWS, GCP, and cloud providers.
21. Predictability leads to velocity in development.
22. Utilized tools like Hasura and Heroku for load management.


## Functional Programming Through the Lens of a Philosopher & Linguist • Anjana Vakil • GOTO 2021

URL: [https://www.youtube.com/watch?v=0kI-as3K4Zo](https://www.youtube.com/watch?v=0kI-as3K4Zo)

 1. Lars and Anjana discuss various topics, including functional programming, linguistics, philosophy, and readable code.
2. Anjana's background in linguistics and philosophy led her to software development through computational linguistics.
3. Programming languages are primarily for human communication with computers; focus on readability and maintainability.
4. Human performance factor is crucial: consider time spent writing, updating, and maintaining code.
5. Adam Tornhill's idea of using Git data to understand social aspects of codebases.
6. Functional programming languages support pure functions, no state changes, and functional programming styles.
7. Multi-paradigm languages can be considered functional if they have features that support functional programming.
8. Pure functional languages constrain you to work in a functional paradigm; multi-paradigm languages allow for different programming styles.
9. Having first-class functions and utilities like mapping and filtering makes functional programming easier.
10. Some developers prefer pure functional languages due to their constraints, while others find it useful to have multiple paradigms in a language.
11. Functional programming offers predictability, making testing and debugging easier.
12. Pure functional languages can help with debugging, testing, maintaining, changing, and refactoring code.
13. Functional programming is beneficial for scaling up systems and improving performance.
14. Learning different paradigms helps appreciate the benefits of one's preferred language.
15. Functional programming has been around since the 1930s but became more practical in recent decades.
16. Gatekeeping in computer science can be a problem, but there's potential for more inclusivity and accessibility.
17. Functional programming has the potential to become even more prevalent in the future.
18. Challenges of understanding programming concepts and how they can be made more accessible.
19. Importance of welcoming new people into the field, regardless of their backgrounds.
20. Examples of functional programming languages: Elixir and Elm.
21. Functional programming community should focus on improving communication and accessibility.
22. Everyone can contribute to making learning easier by helping others understand complex topics.
23. Attend conferences, events, and connect with others in the field.
24. Speaker emphasizes explaining concepts to beginners for better understanding.


## The Power & Performance of Phoenix LiveView • Geoffrey Lessel • GOTO 2021

URL: [https://www.youtube.com/watch?v=-Rl-26JJ6js](https://www.youtube.com/watch?v=-Rl-26JJ6js)

 1. Phoenix Live View is a real-time web framework built on Elixir, providing efficient communication between server and client via websockets.
2. It sends only changed HTML markup, enabling features like form validation and file uploads in real time.
3. Reusable components with their own state allow for live navigation without unnecessary markup.
4. The framework is built on Elixir and Phoenix, highly recommended for web development.
5. Demonstrated by converting a traditional controller-driven app to a real-time one using Phoenix Live View.
6. In the example, they used Elixir and Phoenix for a real-time stock updates application, focusing on live views for interactive features.
7. LiveView provides real-time updates without page refreshes.
8. The speaker converted a Phoenix app to live view by following steps from readme and using generators for real-time communication.
9. They created a fake database with a publish/subscribe mechanism for updating prices and companies.
10. Subscribed to updates in the socket's connect function, achieving real-time communication between server and client.
11. Added live chat functionality with fallback options for users without JavaScript enabled.
12. Handled submitted comments and updated list of companies in real time.
13. Implemented temporary assigns to handle large amounts of data efficiently.
14. Used pattern matching to handle new comments and update socket connections.
15. Demonstrated real-time chat with high update frequencies, showing the importance of diffing algorithms for efficient updates without reloading entire pages.
16. A book called "Phoenix in Action" is mentioned, along with a discount code. Encouraged further exploration of the project's code on GitHub.


## Svelte - Web App Development Reimagined • Mark Volkmann • GOTO 2021

URL: [https://www.youtube.com/watch?v=4CGzFwHoD0A](https://www.youtube.com/watch?v=4CGzFwHoD0A)

 1. Svelte is a compiler-based web framework with no dependencies and no virtual DOM.
2. StealthKit extends Svelte, offering features like file-based page routing, rest services, layouts, code splitting, hot module reloading, static pages, tooling setup, and serverless functions.
3. To start a project with StealthKit, run `npm init svelt` and configure settings.
4. Development mode can be started using `npm run dev`, while deployment is done via `npm build`. Code checking and formatting are handled by `npm run lint`/`format`.
5. A sample ToDo app demonstrates StealthKit's functionality, showcasing its components and features.
6. Svelte offers unique benefits like compact code without the 'this' keyword, efficient rendering of to-do components, reactive declarations for updates, and built-in animations.
7. State management is achieved through variables and reactive statements, while CSS is scoped by default with clear global placement.
8. Svelte has a small bundle size and fast performance due to its efficient virtual DOM.
9. Component state management can be done using stores for shared data access across components.
10. Pros/cons of using Svelte include its less popular status but easy learning curve, different component splitting approach, and more open source libraries than SvelteKit.
11. Related tools include VS Code extensions, testing libraries, mobile app development with Smelt Native, and resources like Rich Harris' talk on rethinking reactivity.


## Command-line, The Underestimated Tool • Bert Jan Schrijver • GOTO 2021

URL: [https://www.youtube.com/watch?v=bWDuXAQJX8Y](https://www.youtube.com/watch?v=bWDuXAQJX8Y)

 1. Command line tools are simple, powerful, and efficient for tasks like quick data manipulation and automation.
2. Bash is a common shell that interprets commands and can handle built-in commands or external binaries.
3. Utilities such as cut, grep, sed, and awk are useful for basic data manipulation tasks.
4. Automating repetitive tasks saves time and increases productivity.
5. Use standard utilities like cut, grep, sed, awk for cross-platform compatibility.
6. On Windows, use WSL (Windows Subsystem for Linux) to access Linux commands.
7. Improve skills by exploring commands and reading documentation.
8. Command line proficiency can enhance productivity, troubleshooting, and understanding of applications.


## A Beginner's Guide to eBPF Programming with Go • Liz Rice • GOTO 2021

URL: [https://www.youtube.com/watch?v=uBqRv8bDroc](https://www.youtube.com/watch?v=uBqRv8bDroc)

 - EBPF (Extended Berkeley Packet Filter) is a powerful technology that enables running custom programs within the Linux kernel.
- BPF, originally known as Barclay Packet Filters, is now used interchangeably with ebpf; it involves writing C programs and converting them into bytecode instructions for execution in a bpf virtual machine.
- Maps facilitate data transfer between user space and the kernel, allowing programs to respond to various events.
- Events trigger EBPF programs, including system calls, function entries/exits, network packet arrivals, etc., using system calls like perf_event_open and ioctl.
- A library such as libbpf provides higher-level abstraction for interacting with these system calls, simplifying development.
- EBPF programs are compiled into object files that can be inserted into the kernel to run alongside other programs.
- User space code manages loading and attaching programs to events, ensuring they're triggered correctly.


## From Objective-C to Swift and the Latest Innovations at Apple • Daniel H Steinberg • GOTO 2019

URL: [https://www.youtube.com/watch?v=qynCRtJlV8I](https://www.youtube.com/watch?v=qynCRtJlV8I)

 - Daniel Steinberg, a key figure in iOS and Swift development, shares his journey.
- Early iPhone development used Objective-C as its language.
- Apple transitioned from Objective-C to Swift, responding to community feedback.
- Recent iOS and Swift updates include ABI Stability, Module Stability, SwiftUI, and Combine frameworks.
- Apple's swift move from Objective-C to Swift was faster than anticipated.
- ABI and Module Stability enhance app stability across versions.
- SwiftUI and Combine change how developers approach building apps.
- Apple's control over both hardware and software allows for rapid innovation.
- Indoor mapping is an example of their focus on improving existing technologies.
- Beacons were used for indoor navigation but had limitations; Apple improves with more precise sensors.
- Near Field Communication (NFC) enables content sharing without contact.
- Apple Pay customizes its features for different markets.
- Steinberg's book focuses on SwiftUI, teaching advanced concepts and differences from UIKit.
- Future updates will likely strengthen SwiftUI and improve AR and machine learning capabilities.
- HomeKit ecosystem could benefit from more support from Apple.
- Package Manager is expected to evolve further with resources and binaries.
- Steinberg frequently teaches private classes in various European countries.


## The Jamstack Book • Brian Rinaldi & Raymond Camden • GOTO 2021

URL: [https://www.youtube.com/watch?v=x0RoXonhldk](https://www.youtube.com/watch?v=x0RoXonhldk)

 1. Jamstack is a web development approach focused on static sites, build processes, and deployment to edge servers/CDNs.
2. It evolved from the initial focus on JavaScript, APIs, and markup.
3. Key components include static site generators, CICD process, and deployment to CDN/edge servers.
4. Complexity has increased with tools like serverless functions, incremental static regeneration, and distributed persistent rendering.
5. The goal is to simplify the deployment process while still allowing for complex features locally.
6. Jamstack has evolved from simple static sites to complex ones with features like distributed persistent rendering and incremental static regeneration.
7. Managing complexity is a tradeoff, as some people prefer handling it locally rather than on production servers.
8. As Jamstack gains mainstream adoption, it's becoming more versatile and can handle larger websites and complex use cases.
9. Inline editing tools are emerging to make content management easier for non-technical users.
10. While there were once clear limitations for static sites, they have become increasingly adaptable with the evolution of Jamstack.
11. E-commerce is being supported by Jamstack.
12. User-generated content can be managed using various methods in Jamstack.
13. Favorite static site generators: Eleventy (Node.js) and Hugo (Go).
14. Next.js is used for complex UI interactions.
15. Challenges with framework-based solutions include understanding where variables are created and accessed.
16. Debate within the community about broadening Jamstack definition to focus on edge deployments and tooling.
17. Server-side rendering and pre-built routes will continue evolving.
18. Jamstack could become the default way of building websites in the future.
19. A book on Jamstack is available through Manning Early Access Program, with a physical version expected in fall.


## GraphQL Anywhere - Our Journey With GraphQL Mesh & Schema Stitching • Uri Goldshtein • GOTO 2021

URL: [https://www.youtube.com/watch?v=2vwlkJnaV0Y](https://www.youtube.com/watch?v=2vwlkJnaV0Y)

 1. GraphQL is a query language for data, allowing users to describe the data and its structure.
2. Benefits include better organization of code, automation, and orchestration between teams and data sources.
3. Start with an existing process and automate it when introducing GraphQL into a company.
4. GraphQL is a powerful tool that can automate processes and improve developer experience.
5. It can be used on the client, server, or between services for various benefits.
6. GraphQL Mesh allows querying existing data sources as if they were graphical without requiring changes to those sources.
7. Merging different graphical sources is possible using portal federation or schema stitching.
8. Schema stitching can be a good option, even for those who previously used it and thought it was deprecated, as it provides benefits within the GraphQL ecosystem.
9. GraphQL Mesh can generate gateways or SDKs for distributed execution.
10. The Guild's product, GraphQL Hive, is a powerful registry for managing metadata.
11. People are using GraphQL Hive even without actual GraphQL services due to its ease of use and developer tools.


## Should Kotlin Be Your Go-To Language? • Garth Gilmour & Eamonn Boyle • GOTO 2019

URL: [https://www.youtube.com/watch?v=FcrkrsxYigM](https://www.youtube.com/watch?v=FcrkrsxYigM)

 - Both speakers have a background in retro computing, transitioning into professional tech careers.
- They've worked on various platforms like C++, telecoms, desktop applications, and mobile apps. One speaker also pursued philosophy and psychology before becoming a trainer.
- The journey from criminology to IT training is discussed, highlighting the importance of staying updated with new technologies.
- Kotlin is mentioned as their favorite programming language due to its expressiveness and modern design.
- Kotlin's convergence with other languages makes it attractive for developers.
- The speaker's company chose Kotlin for its simplicity and readability over options like Scala.
- Understanding hardware architecture is essential, but prioritize readability and maintainability in code writing.
- Performance testing is crucial to measure efficiency; find a balance between performance and simplicity for most developers.


## Erlang, Elixir, Blockchain & Serverless… What?! • Ulf Wiger, Sasa Juric & Eric Johnson • GOTO 2019

URL: [https://www.youtube.com/watch?v=2QNA6uaBHY4](https://www.youtube.com/watch?v=2QNA6uaBHY4)

 - GOTO conference with Eric Johnson, Saša Jurić, and Ulf Wiger discussing Erlang and Elixir.
- Erlang history: visible outside Ericsson in '92, Saša started using it 10 years ago, Elixir released in 2014.
- Elixir is an evolution of Erlang with better ergonomics and UX focus.
- Differences between languages: Elixir more expressive and complex, while Erlang simpler and direct.
- Elixir attracts web developers seeking scalability, robust servers, and messaging durability.
- Both Erlang and Elixir are used for building software systems with 15+ languages built on Beam runtime.
- Erlang is simple and straightforward, while Elixir offers more expressiveness and complexity.
- Eternity blockchain uses Erlang due to its suitability for specific problems.
- The best language depends on programmer expertise and language fit for the domain.
- Erlang and Elixir are good for building rather than executing code in cloud environments.
- Serverless environments may not be ideal for these languages due to their distributed nature.
- A custom runtime allows using other languages with serverless environments.
- Lambda is stateless, while Erlang and Elixir focus on networking between processes.
- Blockchain's distributed nature fits well with the concurrency semantics of these languages.
- Custom runtime allows bringing own language, with examples for Elixir and Erlang.
- Erlang originated from controlling telephone switches but evolved into a general-purpose language.
- Sumo wrestling analogy: Both languages are lightweight and wouldn't compete due to their different purposes.


## Did We(b Development) Lose the Right Direction? • Stefan Judis • GOTO 2020

URL: [https://www.youtube.com/watch?v=0Vtoblyq8fE](https://www.youtube.com/watch?v=0Vtoblyq8fE)

 - 10 years of web development journey
- Frontend performance best practices
- Building a personal blog with universal javascript framework
- Lighthouse scores and website performance comparison
- Difference in performance due to complexity, optimization, and resource usage
- Javascript's impact on browser performance: Importance of page speed and user experience
- Single-threaded browser environment can cause frustration for users
- Overly optimized websites may not be as fast as they seem, especially on low-end devices
- Universal Javascript apps might add unnecessary overhead for content sites
- Consider using tools like 11ty that focus on performance and don't add extra features by default
- Progressive enhancement is important for ensuring a good user experience regardless of JavaScript availability
- React documentation example shows that the JavaScript version is heavier without offering more functionality
- Average website page weight is 2 megabytes, which could be expensive in some countries
- App frameworks may not always be suitable for content sites
- Gmail offers a low data version with minimal JavaScript, providing a good user experience even on slow connections
- The web is complex and heavy, with varying costs across countries
- Javascript frameworks are popular but not necessarily the best for all scenarios
- HTML, CSS, and JS should be the foundation of building great sites
- Misuse of HTML leads to accessibility issues
- Only 6% of websites use Content Security Policy (CSP) for security
- The web is losing quality due to complexities in technology choices
- Web accessibility issues are common due to misuse of HTML
- Only 6% of websites use Content Security Policy (CSP) for security
- Vulnerable JavaScript libraries are used in 80% of websites
- The web is losing quality, but developers have become more productive
- Serverless functions allow easy API creation with minimal code
- Complexity in modern tech stacks can be overwhelming for newcomers
- Fundamentals like HTML, CSS, and JavaScript are essential for good user experiences
- Consider splitting frontend roles into javascript engineers and UX engineers
- Focus on delivering a good user experience regardless of the underlying technology
- Framework choices impact company's bottom line
- Web developers should focus on building good user experiences
- Consider using simpler tools and prioritize end-user experience over developer experience
- In 2020, front-end developers may need to be more versatile, focusing on different aspects of web development
- Strive for a complete green Lighthouse score and better user experience
- Use the right technology for each project instead of relying on a specific stack


## Life After Business Objects - Confessions of an OOP Veteran • Vagif Abilov • GOTO 2020

URL: [https://www.youtube.com/watch?v=UBUYwpDl3-g](https://www.youtube.com/watch?v=UBUYwpDl3-g)

 1. The speaker shares their journey as a veteran of object-oriented programming (OOP) and emphasizes the importance of choosing the right programming paradigm based on individual needs and preferences.
2. An example is given to compare modeling a point class in C#, which is not thread safe, with its functional programming equivalent in F#.
3. Functional programming languages like F# provide safer defaults that prevent developers from making unconscious mistakes through features such as immutable state and types.
4. Immutability makes concurrency management easier in functional programming.
5. The speaker highlights the need to consider the right paradigm for each developer's needs, acknowledging that there is no one best solution.
6. Functional programming languages with immutable state and types are beneficial for concurrency management.
7. Access visibility in OOP can be limiting, as it doesn't solve the problem of exposing certain methods for specific scenarios. Separating logic into different models based on scenarios allows more control over accessibility.
8. Mixing data and operations in OOP can lead to subjectivity and difficulty in defining where certain operations belong. Splitting business objects into multiple classes per scenario provides better clarity and separation of concerns.
9. Object-oriented development can be subjective, as data and operations are mixed.
10. Approaches to class design differ between languages like C# and Java.
11. Functional programming uses algebraic data types for tight domain modeling.
12. Adopting functional programming in traditional object-oriented languages is possible but not always ideal.
13. Recommendations for using C++ include functional, persistent data structures, magnetic operations, and function composition.
14. Rich Hickey's talk on the harm of optional values highlights differences between sets and slots.
15. Adopting functional programming in object-oriented languages is possible but not always ideal.
16. C# is evolving to include more FP features, but its core remains object-oriented with mutable data structures.
17. F# offers algebraic types for better domain expression and immutable records.
18. Functional programming has shortened development cycles, leading to quicker feature delivery and more compact code.


## Upgrade Time: Choose Java 11+ or the “Other” One…Kotlin • Paulien van Alst • GOTO 2020

URL: [https://www.youtube.com/watch?v=BcVOvdrFaPY](https://www.youtube.com/watch?v=BcVOvdrFaPY)

 1. Migrating from Java to Kotlin:
   - Improve interoperability with the Java ecosystem.
   - Benefit from multi-platform support, readability, and safe programming.
   - Leverage a growing Kotlin ecosystem.
   
2. Challenges in interoperability between Kotlin and Java:
   - Address compatibility issues when mixing languages.
   
3. Demo application:
   - Board game rating service using Spring Boot 2.0, memory database, unit tests, and integration tests.
   
4. Usage of Maven for the demo to showcase Kotlin with a standard build tool.

5. Migrating Java application to Kotlin:
   - Set up dependencies for Kotlin and test libraries.
   - Refactor plain Java objects into Kotlin classes, using data classes for immutability.
   - Rewrite unit tests in Kotlin for better understanding of the language.
   - Attack core logic and refactor Spring configuration.
   
6. Benefits of migrating to Kotlin:
   - Improved interoperability with Java ecosystem.
   - Promotes new features like immutability, non-nullable types, and final classes.
   - Better code organization and readability.
   
7. Migrate Java code to Kotlin for better interoperability and improved features:
   - Use data classes, Lombok, and coupling entities for safer and more efficient coding.
   - Test Kotlin code with mocking frameworks like Mockito.
   - Add dependencies for kotlin reflect, coupling login framework, and Spring Data JPA.
   
8. Migrated Java application to Kotlin:
   - Added dependencies for proper interoperability.
   - Modified Spring configuration and classes.
   - Tested the integration, ensuring everything worked as expected.


## The Future of Java: Will You Have to Pay For It? • Trisha Gee & Daniel Bryant • GOTO 2019

URL: [https://www.youtube.com/watch?v=W-_5AV2qZXs](https://www.youtube.com/watch?v=W-_5AV2qZXs)

 - Java is a popular general-purpose programming language, used by 16% of developers.
- It offers good readability and library support for various technologies.
- The JVM platform enables multiple languages to work together.
- Java balances stability with innovation, but may not be the most cutting-edge language.
- Oracle's new licensing model for Java 11 requires understanding alternative JDK options.
- Java is versatile and preferred by some developers over other languages.
- Containers and cloud technologies evolve, with better tutorials and documentation available.
- Developers should focus on their strengths while learning new skills.
- Full stack development is becoming common, requiring knowledge of frontend, backend, and devops.
- Find companies that value your unique skill set.


## Programming Kotlin: Why, How & Its Future • Venkat Subramaniam & Hadi Hariri • GOTO 2021

URL: [https://www.youtube.com/watch?v=7J2ATE4NGZ8](https://www.youtube.com/watch?v=7J2ATE4NGZ8)

 1. Cat, a busy individual who writes books while traveling, has authored 11 books, including one on DSL in Kotlin.
2. The author chose to write the book because of the story behind it, not for marketing purposes.
3. Cat found Kotlin intriguing due to its unique features and syntax compared to other languages he had used.
4. Initially reluctant to write a book about Kotlin, the author later found excitement in understanding its unique features.
5. Writing a book is challenging but rewarding, as it makes one smarter and helps them learn new things.
6. Feedback from experts improves the final product, and one doesn't need to be an expert to write or speak about a topic.
7. Kotlin was created by JetBrains for Android development, offering features like inline lambdas, multi-paradigm, and non-opinionated approach.
8. Challenges in writing books include balancing depth and breadth of the rich language.
9. Kotlin's appeal lies in treating developers as adults, allowing various coding styles.
10. The author found writing the book a rewarding experience, learning more about the language in the process.
11. The Kotlin team was open to feedback and constantly improving their work.
12. The book aims to help readers understand the depth of Kotlin's features and appreciate its evolution.
13. Kotlin offers advantages such as static typing, conciseness, expressiveness, and reduced errors.
14. Kotlin is versatile for various environments like Android development, DSL creation, and multi-platform applications.
15. Kotlin Native can compile to native platforms on Linux, Windows, Mac OS, attracting developers with C++ and Delphi backgrounds.
16. Jetpack Compose could benefit from being compiled natively in the future for UIs on Android and desktop.
17. The speaker looks forward to attending conferences like GoToConference in person.


## A TypeScript Fan's KotlinJS Adventures • Eamonn Boyle & Garth Gilmour • GOTO 2020

URL: [https://www.youtube.com/watch?v=Si3z82PEB5o](https://www.youtube.com/watch?v=Si3z82PEB5o)

 1. Evan and Garth discuss their love for TypeScript and Kotlin, exploring both languages through a Bash Out clone project.
2. Kotlin JS is fully integrated into IntelliJ, offering built-in support for React and Redux.
3. Both TypeScript and Kotlin are popular languages; while Kotlin focuses on the JVM, TypeScript is built on top of JavaScript.
4. Kotlin adoption has a learning curve due to differences from JavaScript/TypeScript, but interoperability can be achieved using tools like Ducat.
5. TypeScript offers advanced features such as structural typing and mapped types not yet available in Kotlin JS.
6. React UI building with Kotlin JS is possible, though there's a learning curve due to differences from JavaScript/TypeScript.
7. Kotlin JS has impressive core language features but lacks the type safety and flexibility found in TypeScript.
8. TypeScript offers more flexibility with algebraic data types and programmatic creation of types. Ducat struggles with complexities, resulting in mixed results for union and intersection handling.
9. Both languages have strong concurrency support: Typescript with async/await keywords and Kotlin with coroutines and the suspend keyword.
10. Kotlin has a more elegant syntax, making code simpler and more symmetrical.
11. Both languages offer destructuring capabilities, but it's more flexible in TypeScript.
12. Conclusion: Both are excellent languages with different advantages; cautiousness may lead to choosing TypeScript due to community size and existing solutions. Future developments will be interesting for both languages.


## Memory Efficient Java • Kirk Pepperdine • GOTO 2020

URL: [https://www.youtube.com/watch?v=kQEu1VsrG44](https://www.youtube.com/watch?v=kQEu1VsrG44)

 1. Memory efficiency is crucial for application performance, as memory churn rate affects garbage collector performance and runtime.
2. Algorithmic issues can lead to excessive logging and hot allocating threads, causing slowdowns in other processes on the same chip.
3. Optimizing memory usage and tuning applications improve overall performance; reducing allocation rates is significant for performance improvement.
4. Inferring allocation frequency helps identify hotspots in code, which should be algorithmically optimized to reduce churn.
5. Thread local allocation blocks minimize contention on the heap by allocating more memory per thread.
6. High memory churn rates increase garbage collection activity, affecting application performance.
7. The power curve shows that above 1 gigabyte per second, there's little gain; inferring allocation frequency is an approximation.
8. Tuning the garbage collector can be costly and may not solve the problem; focus on finding hot allocators instead.
9. Flight recorder helps identify issues but lacks information on where the hotspot is in code; it's still useful for certain aspects.
10. Applications may have multiple allocation hotspots depending on their execution mode; analyzing code to find solutions can improve performance.


## 97 Things Every [Java] Programmer Should Know • Trisha Gee & Kevlin Henney • GOTO 2020

URL: [https://www.youtube.com/watch?v=T47k2tHXmOA](https://www.youtube.com/watch?v=T47k2tHXmOA)

 - 97 Things Every Java Programmer Should Know is a series of books with various contributors.
- The initial idea came from Richard Monson-Haefel's book about software architecture, and the number 97 was chosen for its properties and to fit within a standard book size.
- A broader reach was achieved by including more diverse voices in the Java edition.
- The book aims to represent different points of view, showing that there is no single right answer in software development.
- It discusses the complexity of software and various approaches for aspects like certifications and testing methods.
- The author highlights the need to focus on broader skills like community involvement and career growth.
- The book is applicable across programming languages due to its diverse content.
- Some parts of the book will age, but most technical pieces remain relevant.
- The book is valuable for software developers in general, not just Java programmers.
- Diversity should be considered when discussing the book's audience.
- Encourage diversity and inclusivity in tech communities. Lower barriers for participation, especially for women. Value individual voices and experiences. Aim for openness and collaboration in projects. Resist the urge to rewrite others' work to fit your style. Focus on statistical sampling with varied perspectives.
- The book is ordered alphabetically, making it easy to find specific topics or themes. It can be used for various purposes like learning, team discussions, or book clubs. Favorite pieces depend on recent conversations and personal interests. Editing process involved removing factually wrong or potentially damaging advice. Importance of being open-minded when reading the book. Short pieces allow for exploration and potential future application.


## Secrets of the Shenandoah Garbage Collector • Stephanie Crater • GOTO 2020

URL: [https://www.youtube.com/watch?v=WcSqLvxwzbA](https://www.youtube.com/watch?v=WcSqLvxwzbA)

 - Shenandoah, a newer Java garbage collector.
- Three main steps: find garbage, collect it, and update references.
- Shenandoah works mostly concurrently with the application running.
- Work stealing balances load between task queues.
- Task Q stats framework tracks task assignments, pops, slow pops, total steals, and attempts.
- Added more statistics for better diagnosis of work stealing issues.
- Included slow pop attempts, breakdown of steals and steel attempts by target queue.
- Used graphs for visual representation.
- Identified issues with unbalanced task allocation and work stealing performance.
- Discovered that cues were not trying to steal due to stop the world pauses during GC phases.
- Understood that adjusting worker usage depends on the phase of GC.
- Shenandoah's garbage collection uses queues, but doesn't consider which ones are active or inactive.
- Work stealing code randomly chooses a queue to steal from, leading to low success rate.
- A solution introduced that biases selection towards recently successful queues.
- This improves the success rate significantly and makes work stealing more efficient.
- Tiff in JDK 11 improves queue selection for stealing work.
- Bias towards last successful active queue pick.
- Code available on GitHub.
- Improved success rate from 75% to around 90%.
- Discussion about optimizing queues and context.


## Gradually Adopt GraphQL Without Writing any Backend Code • Uri Goldshtein • GOTO 2020

URL: [https://www.youtube.com/watch?v=DWBL7GLMVsY](https://www.youtube.com/watch?v=DWBL7GLMVsY)

 1. GraphQL is a query language that enables clients to fetch specific data from various sources efficiently.
2. It offers performance benefits such as reduced network traffic and server load, thanks to its ability to execute queries in parallel.
3. Resolvers handle the logic behind fetching data, eliminating the need for writing code for individual fields.
4. GraphQL can be implemented on both client and server sides, allowing gradual integration into existing systems.
5. Placing GraphQL clients next to UI components simplifies managing changes in data structures and scaling UI teams.
6. Benefits of using GraphQL on the client include less time spent on data handling, more time for UI development, and easier introduction into existing systems.
7. Apollo Client with link architecture enables calling multiple REST or GraphQL servers, providing flexibility in integrating different data sources.
8. Use existing schemas and servers to generate GraphQL schemas and endpoints without writing custom logic.
9. GraphQL Server handles regular queries while REST API calls are made when annotations are present.
10. Tools like GraphQL Mesh enable service-to-service communication, supporting various protocols such as Swagger, OpenAPI, gRPC, SOAP, and Microsoft's All Data.


## Facts You May Not Know About Kotlin • Eugene Petrenko • GOTO 2020

URL: [https://www.youtube.com/watch?v=XwzStZaDpH0](https://www.youtube.com/watch?v=XwzStZaDpH0)

 1. Kotlin's history: Originating as an internal language experiment for JetBrains, it was later named after the island of Kotlin near Saint Petersburg.
2. Interoperability with Java and other languages is a key feature of Kotlin.
3. Kotlin 1.4 introduced optional trailing commas in function calls.
4. The language focuses on concise code, safety, and friendliness.
5. Kotlin's website features an image from the island of Kotlin.
6. Plus operator example: Combines two strings (one with a question mark for potential absence) and prints their combined string if one is 'now'.
7. Kotlin has a special 'nothing' type, representing no value, which can stop execution in certain situations.
8. Using nullable types and safe calls simplifies code.
9. Generics are an advanced concept in Kotlin.
10. Loading code with grey highlighting in IDEs is another feature.
11. Using nullable types to shorten code using Kotlin's light bulb feature.
12. Safe calls and functional programming in Kotlin.
13. Understanding generics in Java and Kotlin, including refined inline functions.
14. Type erasure and workarounds for casting issues.
15. Non-blocking programming with Kotlin coroutines and concurrent features.
16. Kotlin's versatility: used for concurrent programming, game development, mobile app development (KMM), and more.
17. Kotlin's ecosystem: supports multiple platforms like JVM, iOS, Android, and JS.
18. The fun aspect of Kotlin: makes coding enjoyable and leads to interesting ideas.


## Memory Efficient Java • Kirk Pepperdine • GOTO 2020

URL: [https://www.youtube.com/watch?v=sE_dv7piOZg](https://www.youtube.com/watch?v=sE_dv7piOZg)

 1. Memory churn is a significant performance issue in many applications, often invisible.
2. Third-party products like Apache Spark can suffer from high memory churn.
3. Reducing allocation rates leads to improved performance; a one gigabyte per second threshold indicates well-tuned applications.
4. Profilers help identify allocation sites and optimize code for better efficiency.
5. GC log shows excessive memory churn in an application, leading to performance issues.
6. Reducing allocation rates can improve performance significantly.
7. Visual VM and Java Flight Recorder are tools for analyzing allocations; however, Visual VM may sometimes lie due to its external profiling method.
8. Java Flight Recorder records inside the JVM, providing more accurate results.
9. Demonstration of Java Flight Recorder in Java Mission Control: Attach to JVM, start recording, and analyze memory allocation.
10. Observing unexpected appearance of 'score' in the profile (potential regression) - potential issue.
11. Performance improvement after optimizing application: runtime drops from 1 minute to 12 seconds.


## Elixir in Action • Sasa Juric & Erik Schoen • GOTO 2020

URL: [https://www.youtube.com/watch?v=-bCkha6U70o](https://www.youtube.com/watch?v=-bCkha6U70o)

 1. Elixir is a programming language designed for software systems, focusing on high availability.
2. The key ingredient of Elixir's support for high availability is the Erlang Virtual Machine (BEAM).
3. BEAM allows running many small lightweight independent programs called processes within a single instance, providing fault tolerance.
4. Elixir offers basic microservices features directly at the runtime level, simplifying building highly available systems.
5. Go is great for tool development but less suitable for software systems due to shared memory and cooperative scheduling.
6. BEAM languages are stable and proven in large systems like WhatsApp.
7. Dark aims to reduce technical complexity by providing a single tool, similar to what beam languages offer.
8. Static typing is seen as a deficiency in beam languages, but initiatives like Alpaca and Clean aim to bring proper static typing.
9. Elixir offers better approachability and developer productivity compared to Erlang.
10. The entire BEAM ecosystem benefits from each other's progress.
11. Elixir has better tooling support than Erlang initially.
12. "Elixir in Action" focuses on concurrency and is unique for its approach of teaching not only how but also why something should be done.
13. The author's book approach: Teaching both how and why to do something, with a zigzag learning process.
14. Feedback on the book: Surprised by its success, positive reviews, and organic growth.
15. Importance of feedback: Rewarding when unsolicited, showing the book's impact on readers.


## Next-Generation Programming: Rust & Elm • Richard Feldman • GOTO 2020

URL: [https://www.youtube.com/watch?v=ukVqQGbxM9A](https://www.youtube.com/watch?v=ukVqQGbxM9A)

 1. Next generation programming languages: Rust and Elm
2. Both languages are efficient, reliable, and have large communities with open development processes.
3. Rust is broad in scope, has C interop, and shares similarities with Go. Elm focuses on web apps with a fast compiler.
4. They both have static type checking, sound type systems, and no "billion dollar mistake" (null reference).
5. Rust is mutable by opting-in while Elm has strict immutability.
6. Rust has a large community with frequent compiler releases; Elm is smaller but less churn with infrequent updates.
7. Both languages are memory safe and reliable, with negligible runtime exceptions for frontend development.
8. Elm focuses on browser-based UIs, while Rust is more general purpose.
9. Elm has a narrower focus, allowing higher guarantees in terms of performance and safety.
10. Both languages offer free books and online resources to learn them.


## Maximizing Java Application Performance with GraalVM • Oleg Šelajev • GOTO 2020

URL: [https://www.youtube.com/watch?v=PeMvksAZbdw](https://www.youtube.com/watch?v=PeMvksAZbdw)

 - Granville is a high-performance virtual machine supporting multiple languages.
- It offers two execution modes: normal JVM and ahead-of-time compilation.
- Benchmarking shows an average 30% performance boost for Granville compared to OpenJDK.
- Ahead of time compilation (AOT) improves performance by reducing startup speed, memory footprint, and packaging size.
- Native Image utility compiles Java code into platform-dependent binary for faster startup and lower memory consumption.
- Gravimoron's native image supports various frameworks like Spring Boot, providing similar performance to raw versions.
- AOT execution mode has lower CPU usage during startup and warm-up compared to JIT mode.
- 283 utility reduces memory usage from 400MB to 60MB with its native image version.
- Native images improve startup times and reduce CPU consumption during warm-up.
- Graviton ecosystem supports languages like Java, JavaScript, Node.js, Python, etc.
- Companies like Twitter, Oracle, and Nvidia use native image technology in their projects.
- Participate in the Graviton ecosystem by engaging with its community.


## Bootiful GraphQL with Kotlin • Dariusz Kuc • GOTO 2020

URL: [https://www.youtube.com/watch?v=1siPT1pTXFU](https://www.youtube.com/watch?v=1siPT1pTXFU)

 - Demonstration of building a reactive GraphQL web server with Kotlin, Spring Boot, and other libraries.
- Uses reflection to generate schema from source code using the GraphQL Kotlin Spring Starter library.
- Includes a playground for testing queries and viewing documentation.
- Deprecation annotation for removing fields without breaking clients.
- Demonstrates polymorphism in GraphQL with interfaces and unions through a people example.
- Introduced Markdown syntax for formatting transcripts.
- Explained the difference between interfaces and unions in GraphQL.
- Shows how to add arguments to queries and improve performance by using functions instead of properties.
- Discussed benefits of asynchronous code with core teams in GraphQL.


## HTML: How to Make Loveliness • Bruce Lawson • GOTO 2020

URL: [https://www.youtube.com/watch?v=L83LVfhTbzg](https://www.youtube.com/watch?v=L83LVfhTbzg)

 1. Use HTML properly for better performance, accessibility, and responsiveness.
2. Learn semantic HTML to improve accessibility and maintainability.
3. Utilize new HTML5 tags like header, nav, main, article, and footer for better user experience.
4. Semantic HTML elements enhance accessibility and search engine optimization.
5. Accessibility benefits everyone, not just people with disabilities.
6. Test websites for common issues like low contrast, missing alternate text, empty links, etc.
7. Choose accessible component libraries like Reach UI, Tourment UI, and Lion.
8. Reduce JavaScript usage to improve website performance and user experience.
9. WebAIM found 98% of websites have accessibility errors.
10. Test sites without JavaScript and enhance with JS.
11. Choose libraries carefully; some are tested with assistive technologies while others aren't.
12. Beware of bloated JavaScript files that slow down users on mobile devices.
13. Internet accessibility is a global priority, as it can improve education and healthcare in developing countries.
14. The web impacts people worldwide, not just those in developed nations.


## Kotlin Flows and Channels for Android • Ryan Pierce • GOTO 2020

URL: [https://www.youtube.com/watch?v=xch4aw7hNcY](https://www.youtube.com/watch?v=xch4aw7hNcY)

 1. Kotlin's coroutines library uses flows and channels to tackle asynchrony issues in Android development.
2. Flows are versatile abstractions for various streaming tools, offering a safer and easier way to handle different types of streams.
3. Channels are non-blocking queues that enable safe communication between core routines.
4. Kotlin's github issue 254 inspired the creation of flows as an efficient alternative to hot channels.
5. Flows are a versatile and efficient streaming tool in Kotlin coroutines, being lazy, safe, and easy to use compared to channels.
6. Modern Android apps follow recommended architecture with view, view model, repository, and use case layers. Data sources produce flows that are processed by repositories and use cases to generate live data objects in the view model layer.
7. Use S Flow Operator for data flow management. Demonstrate creating a photo repository with names from a data source using operators like map, on each, and zip. Convert live data into a view model using LiveData or custom co-routine builders.
8. Flows are reactive, allowing efficient handling of user input. Multiple ways to use flow in an application.


## Ray: A System for Distributed Applications • Dean Wampler • GOTO 2020

URL: [https://www.youtube.com/watch?v=uPeCk7Wx8HU](https://www.youtube.com/watch?v=uPeCk7Wx8HU)

 1. Ray is a system for scaling applications from laptops to clusters, enabling parallelization of tasks.
2. Demonstration using Monte Carlo Pi calculation shows how Ray speeds up work by leveraging distributed computing.
3. Distributed state example uses parameter servers and actors for efficient cluster resource utilization in distributed computing.
4. Actors are remote objects that handle requests, perform work, and save results within a cluster.
5. Ray is a framework for scaling Python applications, optimizing hyperparameter tuning with Tune library for machine learning models.
6. Solutions for microservices include managing instances across clusters and providing resilience.
7. Drop-in replacements for multi-threading libraries are available in Ray, making it easy to scale applications.


## Adopt GraphQL without Writing any Backend Code • Uri Goldshtein • GOTO 2020

URL: [https://www.youtube.com/watch?v=1bJ_M_v-tso](https://www.youtube.com/watch?v=1bJ_M_v-tso)

 1. GraphQL is a powerful query language that simplifies data fetching and orchestration.
2. Gradual adoption of GraphQL can be done through client-side usage, API integration with tools like Apollo Federation, or creating a GraphQL gateway for multiple data sources.
3. Benefits include simplified UI development, reduced time spent on data fetching, and improved developer productivity.
4. GraphQL reduces code for fetching and filtering data, allowing for better performance when introduced on the client side.
5. Apollo clients have local query engines, enabling queries without affecting backend servers.
6. GraphQL Mesh converts existing APIs into graphical schemas, making them queryable without changing the original source.
7. It allows querying multiple sources as if they were one connected graph, even if not originally GraphQL.
8. The library runs on both client and server sides, offering versatility for different use cases.
9. Gradually integrating GraphQL Mesh into your stack can automate manual coding and improve efficiency.


## The Magic of Music Matching • Roy van Rijn • GOTO 2020

URL: [https://www.youtube.com/watch?v=8Dj0rekeM7g](https://www.youtube.com/watch?v=8Dj0rekeM7g)

 1. Rosa shares her experience with music matching using Java audio system and data lines.
2. Microphones record sound pressure through their smoke membrane, which is represented by data.
3. Sample rate and sample size affect recording quality.
4. Understanding the basics of sound helps create better music matching applications.
5. A microphone works similarly to our ear in detecting sound pressure changes.
6. Sample rate and sample size influence recording quality.
7. Fourier transformation converts time domain signals into frequency domain.
8. Windowing technique combines time and frequency information.
9. Spectrum analyzer visualizes frequencies in a signal.
10. Advanced spectrum analyzers can be used for music analysis with spectral images.
11. A Java-based spectrum analyzer was created to analyze sound.
12. Fingerprinting was done by processing mp3 files and storing their fingerprints as lists of Longs.
13. The algorithm matches songs based on fingerprints, considering offsets for accuracy.
14. A demo showed the system recognizing a song from Spotify's shuffled playlist.
15. Proposed other applications: detect duplicate songs, align subtitles with audio, and copyright infringement detection.
16. Recognized room for improvement and potential challenges with large libraries.


## Making Mutants Work for You • Henry Coles • GOTO 2019

URL: [https://www.youtube.com/watch?v=LoFJajoJQ2g](https://www.youtube.com/watch?v=LoFJajoJQ2g)

 1. Assessing test suite quality involves various methods like TDD, peer review, and code coverage.
2. Code coverage is not always effective as it doesn't guarantee useful testing.
3. Richard Lipton introduced fault diagnosis in 1971 for finding bugs in tested code.
4. Mutation testing, developed in the '80s, gained popularity with Jesse in 2000 and is used for safety-critical projects and normal codes.
5. The process involves creating mutants, compiling code, running tests, and identifying which mutants are killed by the test suite.
6. Mutation testing offers a degree of confidence in the effectiveness of a test suite but isn't perfect.
7. Open source community introduced mutation testing; traditional methods were slow and impractical. PIT (Parallel Instruction Testing) tool improved efficiency.
8. Reduce test execution time by running tests in parallel, skipping compilation cycles, and optimizing test cases.
9. Tessellation helps focus on relevant lines of code for mutant testing.
10. Mutation testing is a powerful tool for providing feedback during development and improving code quality.
11. Equivalent mutants can help improve code readability and intent; performance-related mutants may not be important in unit tests.
12. Main purpose: find equivalent mutants, which are changes that don't affect functionality.
13. Useful tools include Mutant (Java), Ferb (PHP), PITest (Java), Bytecode mutations for Scala and Kotlin, Cosmic Ray (Python), Copperhead (LLVM, Swift, C++), No-strike (JavaScript).
14. New tools to consider: Professional (.NET), Shion (Rust).


## An Introduction to JVM Performance • Rafael Winterhalter • GOTO 2020

URL: [https://www.youtube.com/watch?v=wgJWs14YcEs](https://www.youtube.com/watch?v=wgJWs14YcEs)

 1. JVM performance talks focus on Java program execution and code optimization.
2. The JVM is an adaptive platform with three levels of compilation: interpretation, C1 (static compilation), and C2 (just-in-time compilation).
3. Call sites are crucial for method-level optimization in the JVM.
4. Virtual calls allow overriding methods in languages like Java while maintaining performance despite numerous method calls.
5. Java's method-based JIT (Just-In-Time) compilation focuses on improving methods.
6. Virtual calls in Java are efficient due to vtables, which store method signatures and locations.
7. Smalltalk used caches for performance improvement.
8. The JVM uses linked call sites for faster execution by checking assertions and jumping directly to the code.
9. Call sites can be monomorphic (direct link), biomorphic (conditional jump), or polymorphic (multiple direct links).
10. Optimizations like inlining code are possible based on these types of call sites.
11. JVM call sites can be monomorphic, biomorphic, or mega morphic.
12. Monomorphic call sites are direct links to code positions.
13. Biomorphic and mega morphic call sites use table lookups for dispatching.
14. Ahead of time compilation optimizes static code but is less useful for long-running processes.
15. Inlining code helps JIT compilers optimize further, making methods bigger targets.
16. Maintaining small and simple classes helps with optimization.
17. Double brace initialization can create new types, affecting call site morphism.
18. Inlining code is important for optimization.
19. Mega morphism can make inlining difficult, leading to slower programs.
20. Monomorphic methods are easier to optimize and faster.
21. JIT compilers use techniques like unrolling loops to improve performance.
22. Type systems help processors understand data better for efficient prefetching.
23. Branch prediction helps CPUs work more efficiently by speculating on code execution paths.
24. Escape analysis can optimize memory usage by avoiding unnecessary object allocations.
25. The JVM has improved escape analysis, but it still needs improvement.


## Kotlin 4 vs. Scala 3 • Garth Gilmour & Eamonn Boyle • GOTO 2020

URL: [https://www.youtube.com/watch?v=sIL4mduqHe0](https://www.youtube.com/watch?v=sIL4mduqHe0)

 - Comparison of Kotlin and Scala 3
- Decline in Scala's popularity: novelty, radical changes, functional programming dominance
- Improvements in Scala 3: new compiler, simplified language, better features
- New features in Scala 3: top-level declarations, no need for 'new', extension methods
- Kotlin and Scala 4 comparison (not covered): additional features in both languages
- New Scala 3 features: top-level declarations, no need for new keyword, extension methods, improved enums, try (success/failure), richer data types with unions and intersections
- Union types combine different types in a single parameter; intersection types ensure an object must be of multiple types to be valid
- Literal types treat values as their own type, e.g., 2.3 is a type with only one instance (2.3)
- Nominal typing enforces type restrictions without overhead
- Scala 3 supports significant whitespace; indentation is important
- Export classes to reuse functionality without inheritance
- New Scala features: simplified conditional and iterative statements, exporting classes for avoiding inheritance issues, improved implicit handling, meta programming using TST syntax trees
- Kotlin's approach: pragmatic language focused on delivering solutions without adding unnecessary complexity
- Kotlin's popularity growth with use in various projects; 12 Days of Kotlin blog posts and conferences
- Comparison of Scala 3 and Kotlin: High quality in Scala, pragmatic language in Kotlin
- Kotlin features: Safety, succinctness, functional interfaces, multi-platform library
- Kotlin's future: Universal solution for all platforms, Android development focus
- Google's support for Kotlin: Kotlin first approach in new Jetpack API and features
- Kotlin's popularity for Android development due to simplicity and productivity
- JetBrains' focus on making Kotlin the universal solution for all platforms
- Different approaches lead to varying definitions of quality; Scala might be preferred for learning/experimentation, while Kotlin is better for enterprise environments with junior developers


## You Really Don't Need All that JavaScript, I Promise • Stuart Langridge • GOTO 2019

URL: [https://www.youtube.com/watch?v=rxlJRydqmk8](https://www.youtube.com/watch?v=rxlJRydqmk8)

 1. Importance of web performance: Alex Russell emphasizes the need for better performance.
2. First meaningful paint: A key metric to measure how quickly content appears on a page.
3. Server-side rendering vs client-side: Serving less data doesn't necessarily improve performance; network issues and other factors can affect user experience.
4. User experience is crucial: Focus on making websites load properly for all users regardless of their circumstances or device capabilities.
5. The modern web is complex, difficult to use, build, and maintain.
6. Frameworks and libraries provide benefits like component reuse, consistency, and engineering principles.
7. However, they can lead to fatigue and frustration for developers.
8. The goal should be a consistent great user experience with control over the entire process.
9. Evolution of client-side frameworks: Introducing portals as a simple technology that allows navigating to another page within an iframe.
10. Portals offer control over loading experiences without reimplementing them.
11. A use case for portals is in web documentation pages where separate content can be loaded without losing scroll position.
12. Demonstration of using portal for a web framework with two panes.
13. Portal allows access to both pages simultaneously, unlike other methods.
14. Progressive enhancement: Adding minimal JavaScript on top of plain HTML pages.
15. Portal is currently non-standard and only available in Chrome.
16. Not all websites need single page apps; use portals for interactive elements.
17. Portal is non-standard and only available in recent Chrome versions.
18. Gradual adoption of technologies like React is encouraged.
19. HTML has become smarter, reducing the need for custom JavaScript implementations.
20. Use frameworks to prototype ideas before standardization.
21. Polyfilling with JavaScript can speed up innovation without waiting for browser support.
22. Be aware of performance and accessibility concerns when using new technologies.
23. Stay updated with the industry, not just libraries or GitHub.
24. Not knowing new tech is normal; focus on important issues.
25. Use frameworks for prototyping and polyfilling to speed up innovation.
26. Standardization takes time, so be patient while staying ahead of trends.
27. The web has the power to connect people and share knowledge globally.


## Scaling up an iOS Codebase • Tjeerd In't Veen • GOTO 2019

URL: [https://www.youtube.com/watch?v=n09omYo_QPk](https://www.youtube.com/watch?v=n09omYo_QPk)

 1. Split monolithic iOS application into modules for better organization and management.
2. Consider versioning, stability, and dependency management when working with modules.
3. Organizational challenges include local projects, frameworks, and package managers.
4. Core module is the most important; minimize public API to maintain stability.
5. Test your code, especially public APIs, for quality assurance.
6. Add documentation for clarity and understanding, focusing on public APIs.
7. Maintain a stable public API for better code management.
8. Documentation is crucial, especially for public APIs.
9. Consider offering sample apps and accessibility identifiers for easier integration.
10. Local modules provide hard boundaries between codes and make testing easier.
11. Downsides include fragmented code and difficulty in updating multiple projects simultaneously.
12. Workspace remains monolithic despite using local modules, but it's more manageable with smaller projects for testing and access control.
13. Code is more fragmented with multiple projects, but can be beneficial.
14. Use semantic versioning to handle changes in packages.
15. Major versions are tricky; plan carefully and update dependencies based on application requirements.
16. Avoid major releases by considering dependencies and versioning.
17. Be cautious with enums, open classes, and subclassing to prevent breaking changes.
18. Start with beta versions and gradually move towards stable releases.
19. Use deprecations for code removal while maintaining backward compatibility.
20. Implement escape hatches for flexibility in case of missing features.
21. Beware of secret majors that can be hidden within minor or patch updates.
22. Take extra care in projects to handle pain for others.
23. Use protocols, but consider alternatives like marking classes.
24. Be conscious of options that may break other people's code.
25. Use access levels to narrow scope and reduce chances of clashes.
26. Avoid Singletons with global mutable state.
27. Plan major changes and work together with co-workers.
28. Release minor updates before major ones.
29. Test your framework or module in different environments for compatibility.
30. Use modules or frameworks for versioning to support multiple workspaces and control updates.
31. Dependency management is crucial for software development.
32. Semantic versioning can impact organizations when code breaks or major releases take time to resolve.
33. Package managers like CocoaPods, Sweet Package Manager, and Swift Package Manager help with dependency management.
34. Carthage and its fork, Carthage+, offer framework stability for enterprise-level projects.
35. The speaker recommends checking out their book on the topic.


## Battle of the Circuit Breakers: Resilience4J vs Istio • Nicolas Frankel • GOTO 2019

URL: [https://www.youtube.com/watch?v=kR2sm1zelI4](https://www.youtube.com/watch?v=kR2sm1zelI4)

 - Microservices are an organizational solution, not a technical one.
- Monolithic architectures can be problematic when scaling.
- Sacred breaker is a concept to handle failures in distributed systems.
- Circuit breaker pattern in complex web service architecture: stops calling backend service when failure occurs; self-healing mechanism tries to make calls again after some time; important configuration option: fallback strategy for failures.
- Recommendation engine example: no fallback is acceptable, but it doesn't disrupt business; pricing web service example: requires fallback and business logic integration.
- Service meshes vs libraries for fallback strategies.
- Couple of payment solutions: gray out provider, send invoice; Swiss method: merchant sends goods, customer pays later.
- Kubernetes: popular service mesh, Istio; Resilience4J: Java library for circuit breakers, rate limiting, etc.
- Demo: Spring WebFlux app with network simulation and Resilience4J integration.
- Functional programming challenges for those not familiar with it.
- Two applications: reactive pricing service and non-reactive shop service; uses function composition to assemble features like time limiter, circuit breaker, and caching in the shop service.
- Levin's Eleven test demonstrates system behavior under different conditions.
- Encourages audience to explore further through blog, Twitter, and source code.


## Building Secure React Applications • Philippe De Ryck • GOTO 2019

URL: [https://www.youtube.com/watch?v=O91hJJ5KMLs](https://www.youtube.com/watch?v=O91hJJ5KMLs)

 - Discussing security and React applications
- Important topics in 5 minutes: projects, managing people, securing web and mobile apps
- Cross-site scripting (XSS) vulnerabilities
- Tips for building secure project applications
- Blog posts on security issues
- Security awareness and education
- Importance of documentation and testing
- Examples of real-world cases with security issues
- Discusses various security issues and solutions in web applications, cross-site scripting, credit card information theft, underground markets, etc.
- Introduces Purify as a sanitizer for secure websites
- Highlights the importance of maintaining safe browsing experiences
- Focus on ensuring secure applications and best practices
- Mentions tools like Purify, Snap, React, and other frameworks for improving security
- Discusses proper coding guidelines and best practices
- Shares experiences with different projects and their approaches to security
- Conference talks about cipher pitfalls, web development, security, application design, etc.
- Mentions modern applications, code quality, and ethical considerations in the industry
- NPM landscape analysis and efforts to improve developer experience
- Focus on maintaining and improving software performance and security
- Discusses various topics related to software, patches, updates, advertising, Cuba, feeds, shoes, tickets, CPUs, patches, software, budgets, websites, frameworks, events, exploits, graphics, DVDs, patches, festivals, people, updates, security, marketing, projects, references, budgets, roles, applications, developments
- No context provided for the overall discussion


## Nullable Reference Types in C# 8 • Jon Skeet • GOTO 2019

URL: [https://www.youtube.com/watch?v=1tpyAQZFlZY](https://www.youtube.com/watch?v=1tpyAQZFlZY)

 1. Nullable reference types in C# 8 enhance the type system by providing more information about potential nullability.
2. They aim to improve code readability, reduce bugs, and not eliminate null reference exceptions.
3. Disabling nullable reference types doesn't change a project's meaning; enabling them results in warnings for potential issues.
4. The compiler helps identify problems but won't fix your code automatically.
5. Migrating to nullable reference types is crucial for ensuring code quality and avoiding unexpected behavior.
6. C# 8 introduces these features, focusing on improving code safety without changing runtime behavior.
7. Compilers handle nullability differently; CLR doesn't check nullable reference types like C# does.
8. Arrays can have null values without warnings, making it challenging to reason about them.
9. The compiler trusts developers in some cases but provides warnings for local variables with potential nullability issues.
10. Techniques such as the null conditional operator (?.), is null, and others help handle these issues.
11. C# 6.0 introduced new syntax for nullable reference types, including adding a question mark to a type name.
12. Testing code should be done before changing existing code to ensure desired behavior.
13. Nullability affects properties, method parameters, and return types; specific attributes specify relationships between inputs and outputs.
14. Generics and nullable reference types can clash in certain aspects of language design.
15. The CLR could have been changed for more type safety but would make adopting C# 8 more challenging.
16. Nullable reference types improve code expressiveness without changing behavior.
17. Migration involves fixing warnings and enabling errors after reaching zero warnings.


## How Java & Scala are Imitating Functional Languages • Maurice Naftalin & José Paumard • GOTO 2019

URL: [https://www.youtube.com/watch?v=e6n-Ci8V2CM](https://www.youtube.com/watch?v=e6n-Ci8V2CM)

 1. Announcements: New job as a developer and technology evangelist, Edinburgh & Jalba unconference.
2. Talk about functional programming influences on object-oriented programming.
3. The Pizza Paper (1997) introduced generics, higher-order functions, and pattern matching into Java.
4. Generic Java (2004): Implemented generics in Java with compromises.
5. Higher-order functions: Introduced in Java 8 (2014).
6. Pattern matching: Under development for future Java releases through the Amber Project.
7. Scala avoids compatibility issues by starting from scratch and incorporating functional programming features.
8. Java's slow adoption of generics due to lack of runtime type information.
9. Covariance in arrays allowed generic methods but caused problems with array subtyping.
10. Type erasure was used for compatibility between non-generic and generic code.
11. Scala avoided these issues by not having backward compatibility constraints.
12. Pattern matching is coming to Java, starting with preview features in Java 14.
13. Type erasure in Java removes type information at runtime for compatibility.
14. Inheritance brings challenges, requiring synthetic methods and hacks.
15. JVM and compiler sometimes differ in method signature interpretation.
16. Arrays of generics are not allowed in Java due to difficulties in differentiating them.
17. Java has issues with generics, such as no runtime type information and incompatible array types.
18. Scala addresses these problems by using immutable data structures and defining covariant data structures for better client code.
19. In Scala, the library writer defines the covariance while in Java, it's at the call site with wildcards.
20. The Scala approach makes library methods simpler to use compared to Java's complex signatures.
21. Declaration site variance in Scala simplifies library methods.
22. Java's lack of function types led to the creation of abstract classes with apply methods.
23. Lambdas in Java were introduced after a debate on capturing non-final local variables.
24. In Scala, functions are first-class citizens and can capture local variables.
25. Lambdas in JavaScript don't have concurrency issues as they lack multi-threaded programming.
26. Discussed Java concurrency rules and how they apply to local variables.
27. Compared Scala's approach to handling local variables with concurrent access.
28. Explained partial application in both Scala and Java, using examples.
29. Introduced pattern matching in Scala through the "pizza papers" example.
30. Discussed how pattern matching will be introduced in future versions of Java.
31. Introduced sealed types in Scala, allowing only specific extensions for a class.
32. Pattern matching used to determine vehicle type and color.
33. Java is adopting similar features with sealed types for classes, abstract classes, or interfaces.
34. Language design complexity leads to different approaches between languages like Java and Scala.
35. Backward compatibility affects language evolution and adoption of new features.


## The Future of Machine Learning & JavaScript • Asim Hussain • GOTO 2019

URL: [https://www.youtube.com/watch?v=vfmGII9mGmY](https://www.youtube.com/watch?v=vfmGII9mGmY)

 1. The future of machine learning and JavaScript was discussed, with a focus on AI-powered applications.
2. A meetup group called AI JavaScript led to the creation of ijsrocks.com, showcasing innovative projects.
3. Emoji Fire is an app that detects faces, emotions, and replaces them with appropriate emojis using facial analysis techniques.
4. Calculating emotion in facial features involves detecting facial points and utilizing neural networks.
5. Neural networks are inspired by brain neurons; they can be combined to create complex systems for various tasks.
6. Emotion detection in faces requires identifying facial features and applying neural networks.
7. TensorFlow.js enables machine learning in the browser using JavaScript, making it easier to use and more accessible.
8. Microsoft's Face API uses similar technology to detect faces, emotions, and other attributes in images.
9. TensorFlow and MobileNet are used for image analysis, improving web accessibility with human-readable descriptions of images.
10. Generative adversarial networks (GAN) can generate images based on outlines or data sets, with applications beyond just cats.
11. GANs consist of a generator and discriminator, both competing to improve their performance.
12. Exportable models can run in browsers using JavaScript for further optimization and use.
13. Generative neural networks create new images based on input, with potential applications in art and music.
14. TensorFlow JS book and tutorials are available for learning machine learning with JavaScript.


## What’s New in Swift • Daniel H Steinberg • GOTO 2019

URL: [https://www.youtube.com/watch?v=6P-nh3uNnsQ](https://www.youtube.com/watch?v=6P-nh3uNnsQ)

 1. Swift 5.1 introduces improvements such as single expression return removal, raw strings with pound escape, string interpolation enhancements, key paths in functions, and combine map/filter implementation (not yet in main branch).
2. Result type is a powerful feature used for functional programming, providing optional-like behavior with success or failure cases.
3. Doubled function example demonstrates handling out of bounds errors using result types.
4. Maps are utilized to transform values within result types.
5. Swift focuses on dynamic languages for better interoperability with other languages.
6. Dynamic member lookup allows accessing properties without knowing the exact key at compile time.
7. The Dynamic callable protocol enables treating any type as a function that takes arguments and returns a value.
8. Opaque result types are used in Swift UI, allowing the compiler to determine what's being returned at compile time.
9. Function builders facilitate creating complex structures like V stacks from multiple elements, useful for DSLs (domain-specific languages).
10. Trailing closures improve code readability by moving last closure outside parentheses into curly braces.
11. Swift UI leverages function builders for higher order functions.
12. Swift UI's impressive performance is attributed to value types and optimizations.
13. State in Swift UI enables efficient updates through reference storage instead of values.
14. Property wrappers enable customization, such as rounding values to a specific number of places.
15. New features in Swift are inspired by Swift UI's underlying principles.


## Kotlin/Native: The Good, The Bad, and the Ugly • Ellen Shapiro • GOTO 2019

URL: [https://www.youtube.com/watch?v=JHUY1Ckmo64](https://www.youtube.com/watch?v=JHUY1Ckmo64)

Error


## Building a Blockchain in Erlang • Ulf Wiger • GOTO 2019

URL: [https://www.youtube.com/watch?v=QLwFpT_0c4U](https://www.youtube.com/watch?v=QLwFpT_0c4U)

 1. Erlang is a functional, concurrency-oriented language with fault tolerance and dynamic typing.
2. It features pattern matching for assertions and can implement parallel map functions using list comprehension and process spawning.
3. Monitor function ensures supervision of processes and order preservation in results.
4. Eternity blockchain uses Erlang for its core, offering features such as proof of work, key blocks, microblocks, Sofia smart contract language, state channels, oracles, generalized accounts, context-sensitive authentication, and a carrier class product mentality for stability and efficiency.
5. Quick Check is a powerful testing tool that generates random code to find bugs in Erlang programs.
6. The Fast Eternity transaction engine uses a virtual machine for the Sofya contract language.
7. State channels allow off-chain transactions, improving speed and efficiency.
8. Finite state machines are complex but essential for state channel programming.
9. Blockchain technology requires dynamic languages like Erlang for adaptability.
10. Eternity blockchain has an open-source foundation with grants for development.


## A Veterans Guide To Transitioning Android Teams Into Kotlin • G. Gilmour & E. Boyle • GOTO 2019

URL: [https://www.youtube.com/watch?v=ocCE3s9j-9A](https://www.youtube.com/watch?v=ocCE3s9j-9A)

 1. Eamonn and Garth are trainers at Instill, a software development company focusing on modern JVM languages like Scala and Kotlin for enterprise apps with Spring Boot.
2. Kotlin is an alternative language for the JVM with many useful features, recommended by Google for Android development due to its benefits.
3. Instill has been using Kotlin in their projects and training courses as it offers advantages over Java, such as reduced codebase (40%), simplified coding, and better memory management.
4. Adopting Kotlin didn't require new frameworks; existing ones can be used with the language.
5. Co-routines are a recent addition to Kotlin, making concurrent code easier to write.
6. Kotlin is easy to learn for developers familiar with other languages like Java, C#, and Swift due to its expressive nature, good interoperability story, and features such as data classes, DSLs, and lambdas with receivers.
7. Kotlin's expressiveness makes it easier to write elegant code while reducing complexity.
8. Kotlin offers features like lazy delegation, weak references, and extension methods for better code readability.
9. Null safety ensures non-nullable types by default, requiring defensive coding only when dealing with nullable types.
10. Top-level functions and expressions simplify code without needing classes or complex structures.
11. Kotlin's evolution makes it a natural choice for developers, offering incremental improvements over other languages.
12. Co-routines are a significant feature in Kotlin, allowing efficient handling of asynchronous tasks while maintaining readable code.
13. Co-routines can be used with other libraries like RxJava for specific use cases.
14. JUnit is mentioned for unit testing instead of newer frameworks due to preferences and ease of use.
15. Co-routines are useful for sequential algorithms.
16. Clover teams are game changers, while JUnit works well for Cortland projects.
17. Documentation issues in early days of Kotlin have been addressed.
18. Dependency injection frameworks can be experimented with.
19. Kotlin native and multi-platform libraries simplify development.
20. Existing skills remain relevant, learning curve is gentle.
21. Cortland gives advantages to businesses in terms of agility and customer satisfaction.


## Upgrade Time: Choose Java 11 or the “other” one…Kotlin • Paulien van Alst • GOTO 2019

URL: [https://www.youtube.com/watch?v=VX3UBvwJtyA](https://www.youtube.com/watch?v=VX3UBvwJtyA)

 1. Free event with energy left to listen
2. Various topics discussed: playtime, software engineering company, work, conferences, workshops, tips, happiness, Medion, free time, learning languages, reviews, features in Word, Excel, Wit, Shovel Knight, programming, functional programming, Java, Swift, Huawei, Android, iOS, website, readability, Katleen's languages, badolie, Luca's framework, Spring, Ajax, magic, Albert Heijn, migration, compiling coat, comfort zone, smoothing codebase, programming koppeling, Palmerie, pet project
3. No context provided for summarization- Migrating to Spring Boot
4. Testing and optimizing applications
5. Integration challenges and solutions
6. Board game development and testing
7. Java frameworks and their features
8. Organic functional programming
9. Enhancing technical organizations
10. Adding new features to projects
11. Using different tools for efficiency- Trucje toe showed live koning
12. Site lift, office-apps, and testing
13. Penis is in two hours, choice of the penis
14. Standard library of a second key
15. School of test help
16. Conficker, Linköping coat, and weekend targeted JVM
17. Minutes to finger, site hij woont u beeld
18. Hi-bit solution, bringing it for you
19. Compiler tells, comparison linköping coat
20. Weekend, targeted JVM one place, minutes to finger
21. Aankoop wie sites, hij woont u beeld
22. De hi-bit solution die kan zijn want je brengt mij
23. Online steps in the ben het beter
24. Productie ze live shows en het juiste punt om mijn koppeling coating toen mijn job folder lid sinds may be a bit slappe
25. But at least mijn keuzes living site b, site en dit is organisch' functionele
26. Which might be fair over de technical organisatie
27. RT en migration ik vind je swing neem mijn tja van voldoet te koop in vodden
28. En mol van de rest tussen met of t's wat je kunt u was wel eens je stukken ketens lijnen en wie place despite koppeling en dan dit nota dit huis toe source code
29. De retorische gebouw zo dit ze bouwde hij just added add to my job project zal eenens checken of dit of dit is running
30. Yes appeltjes doe klink test
31. School van mijn test hulpverlenen
32. Hoewel het stil stil
33. Lammy
34. Work now chart work
35. Dan hou je zoals om spring good looking
36. And will search and that mijn voor tests pas met mij
37. Application stil starred up en het mij en points and still working in venlo het mij en appendices
38. Zo dit was a first step to take naar de second step
39. Dat hij moet een lesje om het stuur maar ik weet je opeens java op chicks te koppeling wat wil doe het yes maar ik weet mag jij
40. Hij kindjes start to make
41. Probleem van en wilt starten maar ik weet mijn meenam jack wat je ze bord chemicus test wordt eeuw verkiezingen zal buik
42. Je c oké hier aan mee lezen developer weidser
43. En wieltjes copy micoach dit zo beheer en just face it
44. Dus amnesie en dan will see this poppen
45. Van jane's
46. Yes-r bond itself which doe mijn werk met de vinger is dat jane's will produce het java equivalent coating clans zuivel
47. Kamp our time beslissen shabai coach dit is waar dat we zal gaan buiten mediums hij can use this take it for granted by two trio cupping pad en voor net en wieltjes
48. Kussen vol start je ruben hoe vol de nullen bot ives which indicate het bij de questionmark
49. En de installation toneel hij doen wat hij nu nobel thaise nooit like deel en nu is zou


## Kotlin: Dissecting the stdlib • Huyen Tue Dao • GOTO 2019

URL: [https://www.youtube.com/watch?v=uCMuGVh7W_0](https://www.youtube.com/watch?v=uCMuGVh7W_0)

 1. Kotlin's idiomatic approach can be learned through its standard library, focusing on functional programming concepts.
2. The Collections API in Kotlin is functional and expressive, emphasizing "what" rather than "how".
3. Higher-order functions are crucial in functional languages; they allow storing functions in variables, passing them as parameters, and returning them from other functions.
4. Lambdas are an important part of Kotlin's functional API, enabling anonymous function definitions.
5. Kotlin allows functional programming with higher-order functions, treating functions as first-class citizens.
6. Lambda functions are compiled into internal classes that extend functional interfaces.
7. Higher-order functions enable passing functions around as parameters or return values.
8. Function references can be used to pass declared functions like lambdas.
9. Kotlin's standard library provides higher-order functions for manipulating code scope and behavior through extensions, apply, run, and let.
10. Lambdas with receivers offer a cleaner syntax by elevating parameters and removing qualifications when calling methods inside the lambda block.
11. Extensions allow adding functionality to classes without subclassing or altering them.
12. Lambdas and receiver functions improve code organization, readability, and reduce visual noise.
13. The Executor method pattern abstracts away ceremony, focusing on critical logic.
14. Closures and captures involve a function accessing scoped values from its environment.
15. Inlining functions can help counteract performance issues by copying the function body into the call site.
16. Non-local returns are possible with inlined functions due to execution context clarity.
17. There is a trade-off between using inline functions and code bloat, so it depends on the situation.
18. The 'noInline' keyword allows treating a parameter as an expression instead of inlining it.
19. Reification helps retain type information for better type checking with inline functions.
20. Kotlin conventions provide flexibility and readability through features like infix notation, operator overloading, and destructuring declarations.
21. Contracts (1.3 feature) help define how a function behaves, ensuring correct usage.


## Life After Java 8 • Trisha Gee • GOTO 2019

URL: [https://www.youtube.com/watch?v=eBuFzQeiGe0](https://www.youtube.com/watch?v=eBuFzQeiGe0)

 1. Java release cadence has changed from every three years to six months, with two licenses for Oracle JDK: open source and commercial.
2. OpenJDK is free but updated every six months; the commercial version offers long-term support for three years. AdoptOpenJDK provides community-run builds with long-term support.
3. Java 8 remains popular among developers, while Oracle's focus on licensing and support changes may impact future versions.
4. Oracle's commercial JDK and open JDK are the same but have different licenses; Adopt OpenJDK offers long-term support for various Java versions.
5. New features in Java 9 include JShell, a tool for interactive code execution without class files or main methods, and Far (local variable type inference) for improved readability.
6. Convenience factory methods for collections were introduced in Java 9, making it easier to create lists and sets from arrays or iterables.
7. Java 10 allows collecting two unmodifiable collections; Java 11 added predicates not, providing more options for method references. Optional in later versions improved functional handling and readability.
8. Java 11 introduced a built-in HTTP client with non-blocking reactive streams support. Multi-release JAR files allow libraries to use newer features without requiring specific Java versions.
9. Java 9's jigsaw (modularity) allows for smaller deployables and easier integration of third-party libraries; Java 12 has preview features like switch expressions, which may change before becoming solid.
10. Future releases will include text blocks, lambda leftovers, data classes, and performance enhancements. Moving to a recent version of Java improves performance, memory usage, and attracts better developers.
11. Staying up-to-date with six-monthly release cycles allows for faster updates and testing; Java is evolving with frequent updates, focusing on performance and cost reduction.
12. Multiple garbage collectors cater to different application types; migrating to newer versions of Java can improve code readability, performance, and reduce maintenance costs.
13. Tips for migration: run on updated JDK, fix compiler warnings, update dependencies, build tools, and gradually adopt new features.


## From Spring Boot Apps to Functional Kotlin • Nicolas Frankel • GOTO 2019

URL: [https://www.youtube.com/watch?v=f6a78mCrSeE](https://www.youtube.com/watch?v=f6a78mCrSeE)

 1. Spring Boot simplifies project creation, making it easier to manage dependencies and versions.
2. Kotlin allows for top-level functions and multiple classes in a single file.
3. Inferring types in Java 11 can reduce the need for explicit type declarations.
4. Spring Data provides magic through annotations, but some developers prefer explicit code.
5. Magic is found in annotations, making it difficult to understand implicitly defined code.
6. The speaker discusses using Spring Data to simplify Java code and suggests removing annotations by utilizing Kotlin, Spring Boot 2.3, and Spring Framework 5.2 for better readability.
7. Use the Route DSL for better organization and explicitness in configuration files.
8. The importance of making code more explicit while still being concise and easy to understand is emphasized.
9. Reified generics in line can help with dependency injection, and Shrink creates beans automatically based on dependencies.
10. Spring Foo is an experimental project that aims to be explicit and without annotations.
11. Kofu focuses on functional programming, making code more concise and easier for compilers like Gravy VM.
12. Migrating to Kofu requires being reactive, which may cause issues with existing libraries like Spring Data GP.
13. DSLs are used for different aspects of the application, making it more explicit and easier to check in IDEs.
14. Removing magic from a Spring Boot app involves removing controllers, beans, and using bean DSL.
15. The main takeaway is that Spring Boot is great, and people can experiment with Kofu or other frameworks.


## It Really is Easier to Ask for Forgiveness (than Permission) • Naomi Ceder • GOTO 2019

URL: [https://www.youtube.com/watch?v=SYrVZR_g718](https://www.youtube.com/watch?v=SYrVZR_g718)

 1. Naomi Cedar discusses exceptions in various programming languages, highlighting their unique approaches to error handling.
2. Pearl uses segfaults and return value checks for error handling.
3. C++ adds exception handling but lacks deep integration within the language.
4. Java combines exceptions with checking before performing actions.
5. JavaScript allows flexible error handling by allowing any object as an exception.
6. Go has a unique approach, using error codes returned from functions.
7. Python's exception system is straightforward and customizable through its rich hierarchy.
8. Exceptions can be used for control flow in addition to error handling (Harry Potter theory).
9. Generator exit exceptions occur when generators are not properly cleaned up, preventing memory leaks.
10. Python uses exceptions as a form of flow control and simplifies code readability.


## Rust 2018: Access All Areas • Florian Gilcher • GOTO 2019

URL: [https://www.youtube.com/watch?v=sCSfyQYDImM](https://www.youtube.com/watch?v=sCSfyQYDImM)

 1. Rust is a new language designed for building reliable and efficient software.
2. It focuses on performance, reliability, and productivity.
3. Rust offers memory safety with strict resource handling for concurrency and parallelism.
4. Ownership and resource management are key features of the language.
5. No runtime or garbage collector is needed as it's a native programming language.
6. Rust's memory layout allows custom construction and allocation on the heap.
7. Ownership ensures resources are managed effectively, with values having trackable regions of active use.
8. Results in Rust allow for error handling without exceptions using enums with success or failure variants.
9. Rust's ownership and borrowing system ensure data safety in parallel programming.
10. Parallel and concurrent programming libraries like crossbeam and rayon are available for easy implementation.
11. Async/await syntax allows choosing the right concurrency pattern for different devices.
12. Rust's send and sync properties enable passing values between concurrent units, independent of power or parallelism library used.
13. Rust's ownership concept enables multiple ownership of data through smart pointers.
14. Atomic reference counters (ARC) ensure safe thread access and prevent data loss.
15. Mutexes help synchronize data access in multi-threaded programs.
16. Rust is used for fast CLI programs with structured code generation, serialization, and deserialization capabilities.
17. Embedded Linux is a popular platform for deploying small devices like routers, IoT gateways, and industrial control systems.
18. Rust supports bare metal embedded devices and has a complete tooling system.
19. Rust can interact with C and C++ using static and dynamic libraries.
20. Sealed Rust project aims to bring certification of rust for safety critical use cases.
21. Rust is a memory safe C replacement with performance similar to C and C++.
22. It can be used as a library for existing C code, making it suitable for mobile use cases.
23. Rust has tools for generating libraries that look like C libraries.
24. Sealed Rust project aims to bring certification of the language for safety critical use cases.
25. Rust offers productivity features such as documentation, books, and tooling support.
26. It can be used in various ways without requiring a complete switch from other languages.
27. Rust is useful in IoT sector due to its ability to cover all use cases from small devices to service systems.


## ReasonML: React as a Language and what the Future looks like • Peter Piekarczyk • GOTO 2019

URL: [https://www.youtube.com/watch?v=xGN4BMPbk7Q](https://www.youtube.com/watch?v=xGN4BMPbk7Q)

 1. Draftbit, a platform for building mobile apps visually using Expo and React Native, has transitioned from JavaScript to Reason due to its ease of use and reduced technical debt.
2. The company's stack includes React Native, Expo, GraphQL, Apollo, Postgres, and WebAssembly. They aim to provide a fast and efficient development experience for early-stage companies.
3. Reason is a JavaScript-like functional language with a friendly compiler built on top of OCaml and uses NPM for package management. Benefits include faster compilation, fewer errors, easy integration with existing projects, and helpful error messages.
4. React components in reason are familiar to JSX users with some differences like destructuring. A real-world project demonstrates the use of ReasonML and React.
5. Pipe first feature in ReasonML allows composable functions, while its standard library, Belt, offers useful tools. Converting immutable lists to arrays for browser compatibility is also discussed.
6. Hooks in React are used in ReasonML, offering safety and ease of use. Pattern matching with switch statements in reason is powerful, as well as variants for complex data structures. Jen type generates bindings between JavaScript and reason, simplifying integration.
7. Reason allows using existing JavaScript components, working together with Ohmecamel to provide three output options: byte code, native code, and JavaScript. BuckleScript focuses on readable, safe, and optimized JavaScript compilation, offering tree shaking for smaller compiled files.
8. Deep integration with JavaScript libraries enables efficient optimization and performance improvements. The community can create custom bindings between Reason and JavaScript using specific syntax.
9. Many large companies use BuckleScript in production, including Bloomberg Messenger, Accenture, McKinsey & Company, Jane Street, and Facebook. Learn more through meetups, Google Discord groups, and upcoming conferences. Give BuckleScript a chance as it may become popular like React did.


## Achieving Functional Programming in Java • John Napier • GOTO 2019

URL: [https://www.youtube.com/watch?v=VUH_HhAaNpc](https://www.youtube.com/watch?v=VUH_HhAaNpc)

 - Speaker is a software developer at an algorithmic trading firm.
- Lambda is an open source library for functional programming in Java.
- Guiding principles for effective programming:
  1. Constraints should be precisely stated via type.
  2. JDK generic operations should have generic interfaces.
  3. Lazy evaluation is a useful default.
  4. Partial operations should be encoded as total operations.
  5. Pure and impure operations should be separate in design and type checking.
- Encode partial operations as total operations
- Separate pure and impure operations
- Precisely state constraints
- Use lambda types for better representation
- Utilize co-products for type safety
- Generic interfaces for generic operations
- Discussed issues with tuples and optional values in languages like Java, Ruby, and Go.
- Introduced the Either type to represent success or failure semantics.
- Highlighted the importance of generic operations for functional programming.
- Explained how functors can be used as a first class concept in Lambda.
- Demonstrated flat map operation on different types like Optional, Stream, and Completable Future.
- Discussed lazy evaluation and its usefulness in dealing with dates.
- Lambdas offer a rich library of functional iteration patterns.
- Covers functors, applicative functors, monads, and more.
- Generic operations provide reusability and lawful behavior.
- Data types like Either and Maybe for composable expressions.
- Lambdas' Either type has caching, ensuring, and try with resources semantics.
- Generic operations lead to reusability and efficient code.
- Data types like Maybe, Either, Unit, and Curried functions are useful in functional programming.
- Partial application allows for flexible function usage.
- Semigroups and Monoids provide useful properties and functions.
- Functional iteration patterns (map, filter) can be applied to various data structures.
- Heterogeneous data structures like HList allow different types of elements.
- Lenses for focusing on specific elements in a list or map.
- IO monad for handling asynchronous tasks and concurrency.
- Lambda project available on GitHub under MIT license.

No context:
- Lambdas are functional programming concepts in Java.
- Guiding principles for effective programming.
- Either type represents success or failure semantics.
- Generic operations provide reusability and lawful behavior.
- Data types like Maybe, Either, Unit, Curried functions.
- Partial application allows flexible function usage.
- Semigroups and Monoids offer useful properties and functions.
- Functional iteration patterns (map, filter) can be applied to various data structures.
- Heterogeneous data structures like HList allow different types of elements.
- Lenses for focusing on specific elements in a list or map.
- IO monad handles asynchronous tasks and concurrency.
- Lambdas' library available under MIT license.


## Embracing the Future in a Multi-Platform World: A Kotlin Story • Sean McQuillan • GOTO 2019

URL: [https://www.youtube.com/watch?v=xilI3dIOJfI](https://www.youtube.com/watch?v=xilI3dIOJfI)

 1. Kotlin Multi-platform allows sharing app logic between iOS and Android, with UI layers remaining native to each platform.
2. The technology supports JVM (Android), LLVM (iOS), and JavaScript targets for persistence layer generalization across platforms.
3. Team structure should include frontend teams (iOS/Android) and a mobile backend team responsible for data layer and shared libraries.
4. Kotlin Multi-platform is in beta stage, with new ideas like safe threading, expect classes, and shared data storage between platforms being explored.
5. Adoption curve suggests early adopters should start now while pragmatic users may wait until Q1 2021.
6. Key concepts include atomic references, co-routines, frozen objects, and worker threads for safe threading in Kotlin Multi-platform.
7. Sudoku application demonstrates cross-platform iOS and Android project using Kotlin Multi-platform.


## Server-side Kotlin with Coroutines • Roman Elizarov • GOTO 2019

URL: [https://www.youtube.com/watch?v=hQrFfwT1IMo](https://www.youtube.com/watch?v=hQrFfwT1IMo)

 1. Cotton, a general purpose language, addresses modern programming challenges through its suspend functions for natural asynchronous coding.
2. Service-oriented architecture leads to complex business logic and cascading failures due to slow services; synchronous programming is one solution using threads and waiting for responses.
3. Various approaches like callbacks, futures/promises, and reactive programming are used for asynchronous programming. Cotton's suspend functions simplify this process without complex combinators.
4. Reactive programming can be hard to read due to code combinations; some languages propose a sink await paradigm based on futures (e.g., C# tasks or JavaScript promises).
5. Carbon Curtains use suspend functions for more natural programming without future combinators, and Spring 5.2 natively supports them. Adapters can help integrate with frameworks that don't directly support suspending functions.
6. Performance is crucial for server-side applications; callbacks are efficient low-level primitives. Suspending functions in Spring 5.2 make it easier to write asynchronous code.
7. If your framework doesn't support synchronous or asynchronous operations, use reactive or future builders with adapters. Curtain builder helps transform code with curtains into a synchronous type for other frameworks.
8. Suspending functions are more efficient than traditional approaches in terms of memory allocation and performance. Configuring service threads depends on the I/O framework used but is easier to scale with suspending functions.
9. If blocking occurs due to legacy code or third-party libraries, use a dispatcher thread pool to execute tasks asynchronously. Configure system efficiency by using context to avoid blocking main threads and create separate thread pools for different types of operations (CPU, I/O, etc.).
10. Curtains provide natural support for consolation, allowing cancellation of long-running tasks. They ensure safe execution, preventing leaks and resources from being left behind after failures. Enforcing curtain usage through types helps with documentation and better organization of code.


## The Language of Programming • Anjana Vakil • GOTO 2019

URL: [https://www.youtube.com/watch?v=6EdFiISk22k](https://www.youtube.com/watch?v=6EdFiISk22k)

 1. Programming languages and human language share a relationship, as they both serve as means of communication.
2. Linguistics studies various languages to understand how they work, while linguistic typology analyzes features across different languages.
3. Every language has unique aspects that contribute to the overall picture of human language.
4. Programming involves analyzing software at different levels of abstraction and follows programming paradigms, which are like linguistic theories.
5. Linguistics teaches descriptive analysis instead of prescriptivism, similar to how programming should be understood in context.
6. Code is a human activity that evolves with changing needs and should be considered within broader social contexts.
7. Creating beginner-friendly teaching languages in different languages helps share collaborative power worldwide.
8. Learning programming should be gradual, similar to how children acquire natural language.
9. Communities play a crucial role in learning and advancing skills; investing in these communities is essential for progress.


## Java Current and Future • Georges Saab & Mikael Vidstedt • GOTO 2019

URL: [https://www.youtube.com/watch?v=vJrHHe3IbQs](https://www.youtube.com/watch?v=vJrHHe3IbQs)

 1. Java is a thriving technology, with ongoing development and improvements.
2. Open JDK offers early access binaries for testing new features.
3. Focus on cloud-friendly, small footprint, fast startup time, low latency, and AI/ML applications.
4. Oracle leads most of the investment in Java's future.
5. New release cadence: frequent releases every six months with smaller increments.
6. Long-term support (LTS) releases for stable performance, security fixes, and no new features.
7. Oracle pricing model: $25 per month on servers, $2.50 on desktops; scales with usage.
8. Projects like Amber, Valhalla, Panama, GraalVM, and Quarkus are being developed in open JDK.
9. Valhalla focuses on adding inline classes to Java for better performance.
10. Amber project aims to improve the performance of Java applications through optimized garbage collection.
11. Panama adds support for foreign function interfaces (FFI) for native library access.
12. GraalVM is a high-performance runtime that compiles various languages into native machine code.
13. Quarkus is a Kubernetes-native Java stack for building cloud-native applications.
14. Valhalla project aims to improve Java performance by optimizing memory usage and reducing overhead.
15. Inline classes (value types) are being developed for better performance, but compatibility concerns exist.
16. Matrix multiplication example shows significant improvement in speed, memory allocation, and CPU efficiency with inline classes.
17. Projects aim to make Java more expressive, easier to read while maintaining type safety.
18. Local variable type inference simplifies code by letting the compiler infer types.
19. Switch expressions are a preview feature that allows switch statements to return values.
20. Pattern matching simplifies type checking and casting.
21. Records provide a simpler way of creating objects with default constructors, hash codes, equals methods, etc.
22. Loom enhances concurrency by using fibers (lightweight threads) and delimited continuations for asynchronous programming.
23. Panama connects Java to C/C++ libraries and native data through a new API.
24. Metropolis aims to move Java Runtime components into Java, starting with JIT compilers.
25. Scarlet focuses on modernizing developer experience for JDK development.
26. Portola explores making sure the JDK works well in containers like Alpine Linux.
27. CGC is a project working on a garbage collector with low pause times and support for large heaps.
28. Early access binaries available for JDK 13, including Valhalla, Panama, and J package projects.
29. Focus on improving Java development and user experience.


## The Soul of Erlang and Elixir • Sasa Juric • GOTO 2019

URL: [https://www.youtube.com/watch?v=JvBT4XBdoUE](https://www.youtube.com/watch?v=JvBT4XBdoUE)

 1. Erlang and its runtime, the BEAM virtual machine, are part of Joe Armstrong's legacy.
2. BEAM uses processes for concurrency, with separate execution contexts, memory space, and message passing.
3. Concurrent programming in BEAM allows systems to be split into independent parts for better scalability and flexibility.
4. Demonstration shows the benefits of using multiple processes in a system.
5. BEAM offers an alternative software building style that is simpler yet more powerful and flexible than traditional approaches.
6. Lix implementation uses Erlang with a single OS process, showcasing its potential for millions of lightweight programs.
7. BEAM's schedulers handle process execution efficiently, even managing 10K processes at 20% capacity.
8. User-facing pages and WebSockets enable input and asynchronous results.
9. Calculation processes improve fault tolerance and high availability by handling individual requests.
10. BEAM's scheduler ensures fair distribution of CPU time through frequent context switching.
11. Negative inputs can cause issues, but the system still functions with reduced efficiency.
12. Fixing issues is crucial for maintaining high availability.
13. Using BEAM's debugging capabilities, operators can identify and resolve problems in processes.
14. Elixir's technical uniformity simplifies development and maintenance across distributed systems.
15. Swarm dependency manages cluster state and process associations.
16. Three lines of code make a service distributed without extra processes or containers.
17. Technical uniformity benefits include easier setup, teamwork improvement, and reduced need for specialists.
18. Elixir can handle complex challenges without rewriting everything from scratch.
19. Author promotes their book "Elixir in Action" with a discount code.


## Reaching Beyond Traditional Boundaries with Clojure • Phil Hofmann • GOTO 2018

URL: [https://www.youtube.com/watch?v=2aIWMYcC4Qc](https://www.youtube.com/watch?v=2aIWMYcC4Qc)

 1. Speaker loves programming and believes it's a creative discipline with no limits but one's mind.
2. Philosophy and computer science share similarities, as Ludwig Wittgenstein discussed boundaries/limits in language.
3. Programming languages limit problem-solving due to different paradigms.
4. Majority of audience loves programming, knows multiple languages, and has a favorite one.
5. Closure is a functional programming language with unique features like shared code across platforms and immutable data structures.
6. A lecture capture tool project was developed using closure for audio recording and sharing.
7. Lisp was used in the project to demonstrate how data structures can be utilized.
8. Introduced a lecture capture application idea using Closure, with shared code between platforms and shared libraries.
9. Discussed immutable data structures and atomic references in Closure.
10. Demonstrated hot reloading and state management in development systems.
11. Showcased an example of a fun game with changing states.
12. Encouraged learning various programming languages and paradigms, including Closure.
13. Saved orangutans through the nonprofit organization.


## Why I Was Wrong About TypeScript • TJ VanToll • GOTO 2018

URL: [https://www.youtube.com/watch?v=AQOEZVG2WY0](https://www.youtube.com/watch?v=AQOEZVG2WY0)

 1. Typescript was released in 2012 as a tool for compiling code into JavaScript, aiming to improve the language rather than replace it.
2. CoffeeScript and Dart were other compile-to-JavaScript tools that didn't achieve the same level of success as Typescript due to various reasons.
3. Typescript has been more successful because it feels familiar to existing JavaScript developers while focusing on improving the language.
4. Both CoffeeScript and Dart faced challenges in gaining mass adoption among the JavaScript community, primarily due to unfamiliar code for developers.
5. NativeScript initially considered not using TypeScript but later embraced it as it made developers more productive.
6. Typescript's success can be attributed to its commitment to the JavaScript standard, familiarity for developers, and opt-in typing system.
7. The typescript compiler can infer types without explicit declarations, making it easier to learn and use.
8. Tooling support in editors like Visual Studio Code provides intelligent suggestions, autocomplete, and seamless integration with libraries and frameworks.
9. Types are available for popular libraries and frameworks through NPM packages, enhancing the development experience.
10. Flow is similar to Typescript but operates directly on JavaScript files, making it slightly slower.
11. Benefits of using Typescript include improved productivity for large teams, better code understanding, and easier collaboration with non-JavaScript developers.
12. Downsides of Typescript include configuration complexity and advanced features that may confuse some developers.
13. Organizations with diverse app developers may benefit from using TypeScript, as it can be useful for debugging and non-JavaScript developers can find comfort in using it for front-end work.


## Rust Async Programming in 2018 • Katharina Fey • GOTO 2018

URL: [https://www.youtube.com/watch?v=j0SIcN-Y-LA](https://www.youtube.com/watch?v=j0SIcN-Y-LA)

 1. Rust is a systems programming language focusing on safety in memory and thread ownership.
2. Borrowing data in Rust ensures proper ownership and prevents concurrency issues.
3. Async programming allows non-blocking I/O without creating new threads, making it efficient and easy to use.
4. In 2013, Lib Green was introduced for asynchronous programming but required a runtime; it was removed in late 2014 leading to the development of mio.
5. Rust has zero-cost abstractions like futures RS for efficient asynchronous programming.
6. Tokio combines mio and futures RS with an event reactor, providing a stable technology stack since 2016.
7. Rust 2018 introduced async/await feature for writing asynchronous code using an event loop in the background.
8. Futures library provides building blocks for creating async applications.
9. Ownership model ensures data is accessed by only one function at a time.
10. Async/await syntax uses weight macro to interact with runtime without needing an event loop.
11. Standard library includes futures abstraction for compatibility across devices.
12. The async/await syntax is stable in nightly compiler, but the library ecosystem needs improvement.
13. Stability expected by early 2019, but delays due to other issues.


## Fresh Async With Kotlin • Roman Elizarov • GOTO 2018

URL: [https://www.youtube.com/watch?v=hb0hfHVWCS0](https://www.youtube.com/watch?v=hb0hfHVWCS0)

 1. History of coroutines and synchronous programming
2. Traditional approach: callbacks (callback hell)
3. Solution: Futures/Promises (different names in various languages)
4. Issues with futures: Complexity, learning new primitives, readability
5. Kotlin Coroutines: Designed to solve callback hell and improve code readability
6. Suspend functions: Marked with a special modifier, allowing for suspension of execution
7. Cotton curtains aim to solve callback hell by using the suspend modifier for functions that can suspend execution
8. Suspended functions are compiled into GBM declarations, which use continuation (callback) parameters
9. In Java, there's a variety of future types across different libraries; Kotlin Coroutines integrate with these libraries through 'lift' extension function
10. Async/await is not available in Kotlin; instead, it offers a better solution for asynchronous programming using suspend functions
11. Kotlin coroutines offer simple and powerful features for concurrency
12. Kotlin's approach to concurrency differs from C# and other languages
13. Cotton language focuses on structured concurrency with suspended functions, sync functions, and deferred types
14. Cotton supports parallelism without forcing it upon developers
15. Suspended functions in Cotton allow for synchronous programming without shared mutable state
16. CSP (Communicating Sequential Processes) is a solution to the problem of shared mutable state
17. Cotton 1.30 stabilized curtains, making them a stable feature


## Keeping Up with Java • Sander Mak • GOTO 2018

URL: [https://www.youtube.com/watch?v=cF-rUNCOm2c](https://www.youtube.com/watch?v=cF-rUNCOm2c)

 1. Java 9 introduced a module system for better code organization and dependency management.
2. Modules allow strong encapsulation, ensuring only necessary dependencies are exposed.
3. Module paths help in running applications with explicit dependencies.
4. The module system improves maintainability and flexibility of large code bases.
5. Java 11 has removed some enterprise IPs like JAXB, RI, and XML Web Services; applications must bundle their own dependencies.
6. JShell is an interactive coding environment with code completion and documentation.
7. Collection factory methods in Java 9 improve collection initialization.
8. Local variable type inference was added in Java 10 with 'var'.
9. Java 11 has a new HTTP client API, now part of the standard library.
10. Adopt a strategy based on your company or team needs regarding LTS and non-LTS versions.
11. Oracle JDK's licensing changed to commercial for Java 11, making openJDK more relevant. Long-term support will be provided every three years starting from Java 17.
12. OpenJDK and Oracle JDK feature parity since Java 11, with some proprietary features removed. When moving from Java 8 to 11, consider using openJDK again.
13. Long-term support for Oracle JDK 11 is available through subscription; long-term support for OpenJDK 11 may be offered by other parties like Azul and IBM's AdoptOpenJDK.
14. If following release train (Java 11 to 12 to 13), plain openJDK bills are sufficient. When jumping from LCS to LCS, consider adopting a vendor's JDK (Oracle, Azul, Red Hat, AdoptOpenJDK).


## Zen and the Art of Convincing Your Company to Use Rust • Ashley Williams • GOTO 2018

URL: [https://www.youtube.com/watch?v=Pn-1so-Ibsg](https://www.youtube.com/watch?v=Pn-1so-Ibsg)

 - Mozilla contractor and Rust developer, Ashley Williams, shared her experience of convincing NPM to use Rust.
- NPM is the largest package registry with over 1 million packages.
- Rust is a systems programming language designed for Firefox's codebase.
- To convince companies to adopt Rust, focus on its benefits and potential drawbacks.
- Don't completely rewrite software in Rust; use microservices architecture.
- Showcase Rust through code demonstrations and avoid bashing other languages.
- Be a systems developer and advocate for Rust within your company.
- Emphasize safety, speed, and ergonomics when explaining Rust benefits.
- Ensure Rust is accessible to all developers by using real-world examples.
- Encourage collaboration with other languages; Rust can complement them.
- Be patient and persistent while promoting Rust within your company.
- Introduce new technology without controlling someone's first experience.
- Focus on inclusivity, documentation, tooling, and support tools like cargo and crates.io.
- Rust has a strong focus on documentation and tooling, providing resources for developers.
- Rust cares about inclusivity with programs like increasing breast reach and Russ bridge.
- Selling tech should consider technical merits but also other factors.
- Be prepared for technology changes in the industry.
- Rust's memory management can make writing fast code more complicated, requiring attention to details.
- Rust has a strong compiler that helps catch errors and ensures correctness.
- Boring code can be reliable due to Rust's safety features.
- Compilers provide helpful error messages and guidance.
- Focus on solving problems rather than using the latest technology.
- Rust is good at processing files, particularly markdown.
- Prioritize reliability over speed when possible.
- Server performance affects team dynamics.
- Focus on solving real problems, not just cool ones.
- Rust is useful for specific tasks like file processing and memory management.
- Learning new technologies can be energizing and beneficial for employee motivation.
- Gumption (initiative, resourcefulness, enthusiasm) is essential when introducing new tech.
- WebAssembly allows compiling Rust to run in browsers or Node.js.
- Try new things, but consider context and other people's experiences.


## Functional Programming in 40 Minutes • Russ Olsen • GOTO 2018

URL: [https://www.youtube.com/watch?v=0if71HOyVjY](https://www.youtube.com/watch?v=0if71HOyVjY)

 1. Functional programming is a refactoring of existing programming knowledge, focusing on organizing and reusing working pieces with a new paradigm.
2. Traditional object-oriented programming may have become messy, requiring refactoring, which functional programming aims to address.
3. It starts with a clean sheet of paper, emphasizing simplicity and core ideas while seeking a new paradigm for programming.
4. Functional programming borrows ideas from mathematical functions, introducing pure functions that only consider input and output without side effects.
5. Immutable data structures are used to maintain program understanding, along with persistent data structures that efficiently handle copying during modification.
6. Combining pure functions and immutable data structures creates a functional programming world with no side effects.
7. Closure provides atoms for representing mutable state and bridges between functional and real-world code. Agents are used to handle side effects like database updates or file deletions.
8. Functional programming offers a better way to write programs but still has issues like off-by-one errors.
9. Pedestal, a library written in a functional style, demonstrates that functional programming works in practice.
10. Functional programming mainly consists of writing functions and dealing with interfaces.


## The Do's and Don'ts of Error Handling • Joe Armstrong • GOTO 2018

URL: [https://www.youtube.com/watch?v=TTM_b7EJg5E](https://www.youtube.com/watch?v=TTM_b7EJg5E)

 - Fault-tolerant systems are designed to work despite failures.
- Hardware redundancy helps minimize hardware issues, but software errors are more common and harder to eliminate.
- Distributed programming is crucial for fault tolerance as it allows concurrent execution of programs on multiple computers.
- Message passing is the foundation of object-oriented programming and should be consistent across scales.
- Airline language unifies ideas from concurrent programming, object-oriented programming, and functional programming to create an easy-to-understand framework for fault-tolerant systems.
- Involvement in fault-tolerant systems since 1980: Created Erlang programming language for Ericsson, focusing on detecting and fixing errors; unified object-oriented programming with functional programming; Ellen (Erlang) became open source due to being banned within Ericsson; founded Blue Tail company, later acquired by Altium Web Systems; Nortel Networks bought Altium Web Systems.
- Discussed the importance of messaging in programming and the need for self-consistency in software systems.
- 1985: Moved to Ericsson, worked on Flex (object-oriented hardware).
- In 1998, Erlang became open source due to Nortel Networks acquisition of Ericsson.
- Airline model of computation and shared memory systems were adopted in programming languages.
- Reliability of service should be applied to consumer products.
- Six rules for building reliable systems: support concurrency, encapsulate errors, detect faults, stable storage, make simple choices when errors occur, and have an error kernel.
- Erlang's error kernel is small (200 lines of code) and used by companies like WhatsApp, CERN, and National Health Services in the UK.
- Importance of fault tolerance and scalability in concurrent programming.
- Error handling through hierarchical architecture, where each level handles errors differently.
- Concurrency allows for better fault tolerance and security by isolating components.
- Erlang's approach to error handling: crash immediately, log the issue, and move on.
- Concurrency makes programming easier as it can be applied to both local and distributed systems.
- Importance of reliable systems through isolation.
- Concurrency and programming languages.
- Arithmetic errors and their impact on precision.
- Observational equivalence in system behavior.
- Need for describing protocols and contracts.
- Architecture with client, server, and contract checker.
- Contract checkers assign blame when issues occur.
- Programming languages are not important; focus on behavior at interfaces.
- Observational equivalence is about same patterns in black boxes.
- Focus on interactions between components and message passing.
- Contracts describe protocols, assign blame, and help with architecture.
- Immune system idea for detecting internal errors and self-healing.
- Error kernel logs errors, restarts failed parts.
- Distinction between error and failure.
- Asynchronous messaging needs order in message passing.
- Protobufs are moving in the right direction but not adequate.
- Session types exist for sequencing messages.
- No context provided on existing systems for telecommunications.


## Software Automation in a Polyglot Stack • Jessica Kerr • GOTO 2018

URL: [https://www.youtube.com/watch?v=cEyjEEK0xuo](https://www.youtube.com/watch?v=cEyjEEK0xuo)

 1. Polyglot programming is common due to various reasons, such as fitting the language to a problem and considering community and people involved.
2. Introducing new languages can be beneficial for growth and innovation, but also think about existing enterprise stacks and individual preferences.
3. Gradually build new tools with modern technologies while ensuring automation makes bringing in new languages less painful for teams.
4. Readme-driven development starts with human needs, then automates the process.
5. Automate project setups to help people explore easily using docker containers or other tools.
6. Make automation accessible to everyone on the team and ensure documentation is clear and consistent.
7. Encourage team collaboration with a centralized API for better efficiency and safety.
8. Focus on generativity, which involves overall growth rather than individual productivity.
9. Risk management involves considering worst-case scenarios and making software easier to change.
10. Update organizational tools regularly for an agile development process.
11. Add reversibility through tools and processes.
12. Avoid automating everything in production, learn by hand first.
13. Use mental models and pair/mob programming for shared understanding.
14. Understand the objective behind changes and new tools.
15. Convince people about new tools or languages, focusing on high-level objectives and new capabilities.
16. Empathy plays a role in understanding others' concerns.
17. Start small and show useful results before moving to bigger changes.


## The Robustness of Go • Francesc Campoy • GOTO 2018

URL: [https://www.youtube.com/watch?v=40d26ZGfhR8](https://www.youtube.com/watch?v=40d26ZGfhR8)

 1. Robustness in computer science focuses on how programs function when things go wrong.
2. Go language addresses memory safety through pointers without pointer arithmetic, garbage collection, automatic bounds checks, and escape analysis.
3. Rust has a more complex type system for memory safety.
4. Type safety in Go is achieved via static typing and efficient compiler checks.
5. Erlang's robustness comes from its fault tolerance and graceful handling of errors.
6. Go's memory management uses stack allocation for local variables, offering performance benefits.
7. Type safety is maintained through static typing, no implicit type conversion, and explicit conversions for compatibility.
8. Interfaces are checked at compile time in Go, leading to easy-to-understand errors.
9. No exceptions prevent blocking issues in concurrent programs.
10. Concurrency features include goroutines, channels, and select for multiple operations.
11. Mutable state can lead to incorrect results in Go; data races are detected using the race detector.
12. Nil pointers are useful but require careful handling.
13. Go lacks generics, making some implementations challenging.
14. Panic is similar to exceptions but allows recovery through deferred functions.
15. Robustness in Go depends on underlying systems; it cannot prevent catastrophic failures.
16. Erlang offers better concurrency with actors and fault detection.
17. Live code upgrade enables continuous running without downtime.
18. Stable storage ensures transactions are either fully completed or not at all, preventing data corruption.
19. Kubernetes provides robustness through containers, nodes, clusters, automatic failure detection, and recovery.
20. Rolling updates allow live code upgrades in Kubernetes.
21. Go's robustness comes from its architecture rather than the language itself.
22. Go has not yet decided on a version management system due to its origins at Google with one repository.
23. DEP and Vigo are tools for dependency management and versioning in Go.
24. A dynamic hot code swapping feature is currently impossible in Go, but it's an interesting idea.
25. A potential future direction could be a distributed runtime that allows go routines to run on different machines without needing Kubernetes.


## Functional Programming with Kotlin • Hadi Hariri • GOTO 2018

URL: [https://www.youtube.com/watch?v=eNe5Nokrjdg](https://www.youtube.com/watch?v=eNe5Nokrjdg)

 1. Introducing functional programming in Kotlin
2. Benefits of functional programming: abstraction, expressive and concise code
3. Kotlin as an object-oriented language with functional constructs
4. Basic syntax for functions in Kotlin
5. Understanding unit, nothing, and top-level objects in Kotlin
6. Higher order functions and lambdas support in Kotlin
7. Lambdas can be used with single parameter names
8. Extension functions allow adding new functionality to existing classes
9. Infix notation for more readable function calls
10. Concepts of anonymous functions and lambdas in Kotlin
11. Lambda behaviors, such as non-local returns in forEach
12. Data classes can be made immutable with val properties
13. Immutability helps avoid invalid objects and simplifies validation logic
14. Custom getters on immutable properties may not work as expected
15. Kotlin's Const keyword guarantees constant expressions for properties
16. Partial functions (e.g., process entry) can be handled using checked exceptions or result classes with success/failure subclasses
17. Algebraic data types provide safety by restricting inheritance to specific files
18. Arrow library offers built-in functionality, including Either type for handling either a successful result or an error message
19. Partial functions handle all cases, unlike total functions
20. Arrow library provides built-in solutions to simplify option type handling
21. Introducing the concept of option in Kotlin
22. Map and flatMap functions for working with options
23. Bind function for monadic comprehensions
24. Creating a custom configuration DSL using objects, invocation, and extension functions
25. Implementing DSLs may not be suitable for every class or project; it depends on the requirements and complexity of the codebase


## C++ - the Newest Old Language • Matt Godbolt • GOTO 2018

URL: [https://www.youtube.com/watch?v=HAFrggEDr5U](https://www.youtube.com/watch?v=HAFrggEDr5U)

 1. C++ is a powerful and evolving language with numerous benefits, including recent updates like auto, range for, lambdas, move semantics, smart pointers, and more.
2. Auto allows the compiler to infer variable types, simplifying code.
3. Range for makes iterating over containers easier.
4. Lambdas enable inlining small functions and capturing variables.
5. Move semantics help manage memory efficiently by transferring object ownership.
6. Smart pointers actively manage memory, reducing memory leaks.
7. C++ has seen significant improvements with new features like range-based for loops, lambdas, move semantics, smart pointers, context/constexpr, atomics, user-defined literals, return type deductions, and lambda enhancements.
8. C++17 introduced constexpr if statements (if constexpr) for template meta programming.
9. New features in the pipeline include concepts, ranges, co-routines, and improved network programming support.
10. Value types are passed by value, making them easier to handle and reason about in code.
11. Strong typing helps catch errors early on, such as passing the wrong parameters to a function.
12. Custom types can be modeled with specific behavior and operations.
13. Constructors allow for default initialization, ensuring objects are initialized properly.
14. Const keyword ensures an object remains unchanged during method calls.
15. Object lifetime management is crucial; destructors run when objects go out of scope.
16. Custom types can have their own lifecycle management, such as releasing resources upon destruction.
17. Mutation in objects can indicate they're not allowed to change, signaling callers that methods won't affect the object.
18. C++ unique pointers ensure ownership transfer and prevent copying temporary values.
19. Compilers can optimize code based on memory layout, leading to faster execution.
20. Clang compiler is recommended for its error messages and tooling support.
21. Sanitizers help detect errors in programs, ensuring better security.
22. The C++ community has grown with guidelines, best practices, and resources available online.
23. Rust offers similar performance to C++ but is stricter on borrowing and ownership.
24. Clang tooling is a C++ language server.
25. Sea Lion Community Edition helps with C++ development.
26. The C++ community has improved recently, with clear guidelines and best practices.
27. Rust is similar to C++ but stricter about ownership and borrowing.
28. Sanitizers are used in some core Google components for security reasons.
29. Package management systems like Conan help manage dependencies.
30. TDD can be done using catch library with BDD and TDD modes.
31. Core guidelines support is available, though the standard library is mostly fine.
32. Boost is a high-quality general-purpose library for algorithms.
33. C++ adoption barriers are being addressed to improve user experience.


## Why is Rust Successful? • Florian Gilcher • GOTO 2017

URL: [https://www.youtube.com/watch?v=-Tj8Q12DaEQ](https://www.youtube.com/watch?v=-Tj8Q12DaEQ)

 - Rust is a new systems programming language developed by Mozilla and the community, focusing on safety, concurrency, and speed.
- It has explicit notions of mutability, data ownership (borrowing), and treats errors as values.
- Data ownership ensures static deallocation through reference counting.
- Borrowing can be done in immutable or mutable ways, ensuring no conflicting access to shared state.
- Rust offers a safe environment with an optional unsafe sublanguage for specific cases.
- The language combines safety techniques from research settings into production-ready packages.
- It's used in sizable production environments like Firefox, Dropbox, and canonical infrastructure.
- More than 2000 contributors have worked on the project, with over 80% of contributions coming from outside Mozilla.
- Rust has grown significantly since its inception, now having more libraries than Haskell.
- It's considered a loved language by developers and is used for production software.
- Stylo, the styling engine powering Firefox Quantum, uses Rust's concurrency tracking for efficient parallelization.
- The language has a strict commitment to stability, releasing every six weeks with minimal breaking changes.
- It's backwards compatible and piggybacks on other mature technologies like LLVM.
- Mozilla follows an open governance structure for changes and improvements.
- Visual Studio Code and JetBrains' Rust IDE are recommended for development.
- Compile performance is improving over time with around 20-30% gains in half a year.
- Rust's static nature makes it unsuitable for heavy dynamic programming or object-oriented environments.
- Maturity of libraries varies depending on the field.
- Rust has a framework and library called Tokyo for non-blocking I/O.
- Fuzzing is possible with tools like American Fuzzy Lop, LipFuzz, and LLVM fuzzers.


## Flutter: The Best Way to Build for Mobile? • Kasper Lund • GOTO 2017

URL: [https://www.youtube.com/watch?v=1BXg4wfB9pA](https://www.youtube.com/watch?v=1BXg4wfB9pA)

 - Flutter is a new framework for building mobile apps, designed to be productive and efficient with custom UIs and fast applications.
- Based on Dart language runtime and Skia graphics library, it offers Material design components for easy app development.
- The framework is reactive and compiles to native code, running on Android, iOS devices, and web browsers.
- Flutter provides a layered framework with predefined high-quality widgets for rapid app development, supporting custom UI across platforms.
- It allows building apps with a single codebase for both Android and iOS platforms, offering customization based on platform requirements.
- Dart has been upgraded to have a sound type system for better scalability, and the compiler converts Dart code into native code or JavaScript for different platforms.
- Flutter's Just-In-Time (JIT) compilation during development and Ahead-Of-Time (AOT) compilation for deployment improve productivity.
- The framework has an open source alpha release focusing on localization, accessibility, and screen reader support.
- Accessing platform-specific APIs involves writing native code in Java, C++, or Swift, then exposing it through a messaging API to the Dart layer.
- Flutter is stable with few breaking changes, learning from customer feedback to improve its API.
- The framework compiles to native machine code for better performance and efficiency.


## JavaScript at Uber • Dustin Whittle • GOTO 2017

URL: [https://www.youtube.com/watch?v=IG9gwgUiqZM](https://www.youtube.com/watch?v=IG9gwgUiqZM)

 - Uber's growth and scale: 73 countries, 470 cities, 1.5 million active driver partners
- JavaScript usage in Uber's engineering: Node.js for web applications, Go, Java, Python
- Reasons for using JavaScript: Flexibility, asynchronous nature, mature module ecosystem
- Four ways Uber uses JavaScript: Backend microservices, front-end web properties, data visualization, external API for developer platform
- Migration to other languages: Focus on Go and Java due to their scalability and performance (Uber started with PHP, moved to Node.js)
- Node.js has core strengths: asynchronous I/O, non-blocking single threaded event loop, great module ecosystem
- Uber's marketplace platform consists of 3400+ microservices, with 100 services for the core trip flow
- They use JavaScript for front-end development with React and Express
- The developer experience team focuses on productivity tools and infrastructure
- Microservices allow clear ownership boundaries, product specific velocity, independent team velocity
- Node.js helps Uber scale by providing language and platform independence (started with monolithic architecture, transitioned to microservices)
- Benefits: clear ownership boundaries, product velocity, scalability, language and platform independence
- Challenges: increased complexity, discovery, eventual consistency, operational overhead
- Scaling node applications: geo-sharding, Ring Pop for application level sharding, T Channel RPC protocol, Jaeger for distributed tracing
- Use standard Linux performance tools for profiling and visibility (T Channel: RPC protocol for efficient communication between microservices)
- Node.js provides performance tools and observability for distributed services
- Performance issues with dynamic typing languages like JavaScript
- Microservices require tight interfaces, statically typed languages help enforce this
- Node.js ecosystem has small libraries but some issues with maturity and dependency chains
- C++ can be used to improve performance in certain cases
- Architecture decisions are important for scaling teams and services
- Consistent platform foundation helps maintain web applications efficiently
- Web platform built on node.js, npm, Express, React, and Redux
- Investing in technology platforms solves problems like security vulnerabilities and duplicated effort (Uber's web platform is built on Node.js, Express, React, and Redux)
- They use customized tools for internal NPM registry, build automation, authentication, security, metrics logging, internationalization, error handling, and analytics
- Separating front-end services from back-end services allows better scaling and reusability across platforms
- React components are used to standardize UI design and make it easy for developers to create good-looking websites without dedicated designers on each team (React, Express, Redux)
- Style Tron is used for managing CSS, making it easier to handle styles in one place
- JavaScript is used for data visualization with libraries like React Vis, React MapGL, and Deck GL
- Luma GL simplifies WebGL interaction
- Node SDK exposes microservices for third parties to build custom experiences
- Uber shares open source tools on GitHub and engineering blog (Uber uses open source libraries and tools for their developer platform)
- They expose 3400 microservices as business domain objects via Node SDK (most of these tools are available on GitHub, explained in detail through engineering blogs)
- Uber aims to build an open platform for third parties to create moving experiences using their tools and data
- The company has offices worldwide, and they encourage people to join the team


## Elixir: The only Sane Choice in an Insane World • Brian Cardarella • GOTO 2017

URL: [https://www.youtube.com/watch?v=gom6nEvtl3U](https://www.youtube.com/watch?v=gom6nEvtl3U)

 1. Infinity refers to the increasing demand on engineering teams for solving complex problems.
2. Elixir is a language built upon Erlang, which was created for telecommunication systems with requirements like zero downtime and hot code loading.
3. Jose Valim developed Elixir as a lightweight language built upon the Erlang virtual machine.
4. Elixir inherits battle-tested 30-year old technology from Erlang, offering solutions to complex problems with modern syntax.
5. Elixir is used by multibillion-dollar corporations for its proven technology and features like battle-tested concurrency and distributed systems.
6. Elixir has a strong tooling system with built-in debugging, linting, documentation, and dependency management tools.
7. Pattern matching is a key feature in Elixir, allowing for more concise code and easier refactoring.
8. Phoenix is a popular web framework used with Elixir.
9. Erlang VM manages processes within the language, ensuring efficient resource usage and distribution across available CPU cores.
10. Deployment targets like Roku are not ideal for Elixir due to cost and performance issues; alternatives include Rackspace or AWS Lambda.
11. Bleacher Report reduced infrastructure costs by moving to Elixir/Phoenix, requiring fewer servers and engineers.
12. WhatsApp's scalability is another example of Erlang's benefits.
13. Gen server allows for blocking requests and fire-and-forget queries.
14. Supervisors manage processes, ensuring a clean restart when errors occur.
15. Let it die philosophy in Erlang focuses on maintaining a good initial state.
16. Supervisors in Elixir monitor workers, with strategies for handling errors or worker death.
17. Agents can be used to maintain state outside the process for better resilience.
18. Functional programming focuses on data and data out, making state more visible.
19. Ruby's focus is on making programming enjoyable.
20. Object-oriented programming (OOP) can be complex and challenging.
21. Functional programming is simpler to learn, with Elixir as an example.
22. Elixir uses modules instead of classes for code reuse.
23. Memory allocation in functional programming is more efficient than OOP.
24. Phoenix framework and Elixir are used by Dr. Calm Consulting.


## Introducing Elm to a JavaScript App • Richard Feldman • GOTO 2017

URL: [https://www.youtube.com/watch?v=28aJOb1A34o](https://www.youtube.com/watch?v=28aJOb1A34o)

 1. Elm is a functional programming language that compiles to JavaScript, offering more reliability and predictability than JavaScript.
2. Integrate Elm with existing JavaScript applications using interop techniques.
3. Ellie allows side-by-side development of Elm and JavaScript apps while maintaining Elm's guarantees.
4. Embed Elm in JavaScript apps for interactivity, preserving data transfer between the two languages.
5. Elm Architecture: View function returns virtual DOM, model represents state, user interaction triggers messages, and effects are handled using commands.
6. Interoperability with JavaScript: Use commands to send data from Elm to JavaScript, and subscriptions for data transfer in reverse.
7. Multiple embeds can coexist on a page, communicating through subscriptions.
8. Incrementally integrate Elm into existing applications while considering runtime overhead.
9. Use Elm for business logic and embed it in the DOM or as a drop-in component with libraries like React Elm Components.
10. Refer to official resources for more information on interoperability between Elm and JavaScript, maintaining guarantees, and client-server communication.


## Demystifying Scala • Kelley Robinson • GOTO 2017

URL: [https://www.youtube.com/watch?v=IayQ7lxPUP4](https://www.youtube.com/watch?v=IayQ7lxPUP4)

 - Scala is a statically typed, functional programming language.
- It combines object-oriented and functional programming styles.
- Inherently object-oriented and functional, Scala offers interoperability with Java.
- Popular in industries like finance, telecommunications, and media.
- Large community with resources for learning and development.
- Compiles to Java bytecode, runs on the JVM, and leverages existing tools/libraries.
- Features include type inference, immutable data by default, multiple inheritance of traits, pattern matching, higher-order functions, and flexibility in coding styles.
- Reasons for using Scala: productivity, familiarity with Java, strong community, interoperability, and performance.
- Challenges: lack of standard syntax guide, managing teams, difficulty understanding some code due to complexity.
- Resources for learning: Repl.it, Coursera's Functional Programming Principles in Scala course, LearnScala.org, official Scala website.
- Testing frameworks: ScalaTest, multiple options available.
- Good tooling support for development: SBT (Scala Build Tool).


## Programming Across Paradigms • Anjana Vakil • GOTO 2017

URL: [https://www.youtube.com/watch?v=Pg3UeB-5FdA](https://www.youtube.com/watch?v=Pg3UeB-5FdA)

 1. Paradigms are fundamental patterns that influence our understanding of programming and the universe.
2. Thomas Kuhn's "Structure of Scientific Revolutions" explains how paradigm shifts occur in science, where communities move from one dominant model to another as anomalies arise.
3. Programming paradigms include functional, object-oriented, logic, and others, each with its own theory, methods, and standards.
4. Paradigms can be applied across various domains like data analysis, machine learning, and natural language processing.
5. Shifting from one paradigm to another requires a community consensus on the new model's usefulness and ability to address anomalies.
6. Scientific paradigms and programming languages have evolved over time.
7. Imperative programming focuses on commands, state, and precise timing.
8. Object-oriented programming (OOP) introduced objects with their own state and interactions via messages.
9. Functional programming focuses on pure functions that return values without changing state or side effects.
10. Declarative programming is about describing the desired result instead of how to achieve it.
11. Domain-specific languages (DSLs) are specialized for specific tasks, making code more readable and maintainable.
12. Different paradigms can have similar concepts, making them less distinct than initially thought.
13. Declarative programming includes logic programming and object-oriented (OOP) & functional programming.
14. Both OOP and functional programming reject shared mutable state, focusing on messaging and immutability respectively.
15. Object-oriented code can be rewritten in a functional way using closures.
16. Paradigms are worldviews or mindsets that define how we conceive the universe of our program.
17. No single paradigm is best; it depends on the problem being solved and personal preference.
18. Paradigms are useful in different ways, depending on the problem.
19. Each paradigm has unique contributions to the dialogue of programming.
20. Different paradigms can be combined for better solutions.
21. The key is to understand the problem and choose the best approach.
22. Understand the importance of different programming paradigms.
23. Declarative, imperative, object-oriented, and functional programming each have their strengths for specific problems.
24. Multiparadigm languages allow exploring various approaches without learning new syntax.
25. Expanding your repertory of paradigms helps improve as an individual programmer.
26. Importance of understanding and embracing different programming paradigms.
27. Multi-paradigm languages allow exploring various mindsets and problem-solving approaches.
28. Paradigms define the nature of programs, problems they solve, and solutions they provide.
29. Mixing paradigms in a system is possible if supported by the language; mixing different languages can be more complicated.
30. Assembly code represents the imperative paradigm.
31. Microservices are decentralized systems that fit Alan Kay's vision of object-oriented programming, and can also be seen as pure functions.


## Why You Should Take Another Look at C# • Mads Torgersen • GOTO 2016

URL: [https://www.youtube.com/watch?v=zQXNq-isqFI](https://www.youtube.com/watch?v=zQXNq-isqFI)

 1. C# is a widely used and loved programming language, constantly evolving to remain modern and relevant.
2. Microsoft actively works on improving the language, drawing inspiration from sister languages like F#.
3. C# can be utilized across various platforms beyond Windows, thanks to Project Roslyn and .NET Core.
4. Xamarin enables developers to create native apps for Android, iOS, Mac, and Windows using C#.
5. Unity leverages C# for 2D and 3D game development.
6. The .NET Core framework offers a lightweight solution for server-side use, cross-platform compatibility, and open source accessibility.
7. Project Roslyn modernizes the C# language engine, making it accessible across tools and platforms.
8. OmniSharp uses Roslyn to provide semantically aware C# modes in multiple editors.
9. The Analyzer framework helps build code analysis tools with fixes for enforcing coding styles or refactoring.
10. Roslyn provides complete information for code analysis, enabling developers to create custom analyzers and fixers.
11. C#'s evolution includes aggressive innovation, mainstreaming concepts from other languages, and embracing new core libraries.
12. Roslyn improves the development experience and language evolution by providing better tools and frameworks.
13. Generics are deeply implemented in runtime for improved performance.
14. Async heavily relies on Generics for efficiency.
15. C# 7 focuses on functional programming and data, not necessarily object-oriented concepts.
16. New features include tuples, binary literals with digit separators, refactoring to generate methods, and pattern matching.
17. Tuples are value types, allowing mutability and deconstruction.
18. Pattern matching is being introduced in C# for more flexibility in the 'is' expression.
19. Future plans include smarter patterns for better integration into the language, nullable types for reference types, a 'bang operator', improved framework annotations, and nullability propagation.


## Exploring Swift Memory Layout • Mike Ash • GOTO 2016

URL: [https://www.youtube.com/watch?v=ERYNyrfXjlg](https://www.youtube.com/watch?v=ERYNyrfXjlg)

 1. Memory is fundamental to computing, organized as a sequence of bytes with addresses.
2. Pointers are used to reference memory locations.
3. Modern systems store data in little-endian order.
4. Memory is divided into three parts: hardware level, stack for local variables, and heap for dynamically allocated objects.
5. Unsafe buffer pointers allow creating arrays from containers.
6. Mach call (mach vm read overwrite) can safely read from pointers without crashing.
7. Recursive scanning systems use safe pointer reading and guess how many bytes to read at any given time.
8. Malloc size function is for heap allocation data, dladder function for symbol information, demangling tools for Swift and C++ symbols.
9. Detect textual data using ASCII characters heuristic.
10. Analyzing memory layouts in different programming languages:
    - C structs are simple with fields laid out sequentially.
    - C++ classes have a vtable pointer for virtual method dispatch and inheritance.
    - Swift structs are similar to C, with no extra metadata or overhead.
    - Swift classes have additional runtime information but object data is stored sequentially.
11. Classes in Objective-C have extra metadata, while method calls translate into array lookups for efficiency at runtime.
12. Subclassing multiple levels still results in the same memory layout.
13. Arrays in Swift are reference types but appear as value types at runtime.
14. Protocols in Swift can store structs inline if they fit size limit; otherwise, stored dynamically.
15. Enums in Swift are compact and efficient, representing each case with a single byte.
16. Any Objective-C objects in Swift 3 are now represented as 'any'.
17. Xcode 8's new memory debugging features offer live graphs and limited tracing capabilities.


## Exploring RxJava 2 for Android • Jake Wharton • GOTO 2016

URL: [https://www.youtube.com/watch?v=htIXKI5gOQU](https://www.youtube.com/watch?v=htIXKI5gOQU)

 1. Reactive programming is crucial due to the increasing complexity of asynchronous code.
2. Traditional imperative programming struggles with handling multiple asynchronous sources and managing state.
3. Android apps require reactive thinking for a smooth user experience, as they are inherently asynchronous.
4. RxJava helps model these asynchronous sources in a way that makes it easier to handle complex scenarios.
5. RxJava has two main types: Observable and Flowable, both representing zero to N items with termination possibilities.
6. Backpressure is a concept in RxJava 2 that allows you to slow down data sources when your system cannot process them fast enough.
7. RxJava 2 offers specialized observables for reactive data handling, such as Single, Completable, and Maybe.
8. FromCallable models synchronous behavior, while the create method is useful for wrapping existing sources.
9. The create method allows modeling asynchronous data and cancellation actions when subscribers unsubscribe.
10. RxJava 2 provides various types of observables for modeling data sources and offers operators to manipulate or combine data.
11. Reactive programming helps developers write code that reacts to changes instead of managing state manually.
12. RxJava 2 is an improved version focusing on asynchronous programming in Android, with a developer preview release and a final release planned soon.


## Microservices in Go • Matt Heath • GOTO 2016

URL: [https://www.youtube.com/watch?v=WiCru2zIWWs](https://www.youtube.com/watch?v=WiCru2zIWWs)

 1. Speaker is a back-end engineer focusing on Go for three years.
2. Mons oh is a new startup building a bank with modern technology using Go.
3. The app has features like spending analysis and card control.
4. Reasons for choosing Go: simplicity, static typing, comprehensive standard library, lightweight concurrency.
5. Go's communication approach: favors process communication over shared memory.
6. Statically linked or linked Go code allows easy deployment on various machines without runtime dependencies.
7. Frameworks like go kit, micro, and timeit can be used to build services quickly.
8. Speaker introduces their own framework called Month Called Time (MCT) for communication between services using message buses like RabbitMQ.
9. Infrastructure includes an HTTP routing layer, API services, individual services for specific tasks.
10. Benefits of microservice architecture: easy deployment of new functionality without impacting other services.
11. Microservice architecture with Go language for banking infrastructure.
12. Routing layer to handle HTTP requests and drop into proxy.
13. API services with defined endpoints, public APIs, and external providers.
14. Kubernetes for high availability, cost savings, and efficient resource usage.
15. Exponentially weighted moving average load balancer for detecting failures.
16. Asynchronous processing using Kafka to publish events and handle business logic.
17. Well-defined interfaces and tracing systems like Zipkin for understanding infrastructure behavior.
18. Utilize Go's context package for thread-local variables.
19. Microservices can be beneficial if you understand your business, but may cause issues with interface changes.
20. Kafka handles transactions by writing events into a partition and uses two-phase commit in the credit card network.
21. Cassandra supports SQL databases through standard library drivers.
22. Sample web poker API uses protocol buffers for request/response communication across services.
23. Moving from PHP and Java to Go as a microservice architecture choice.
24. Go stores code in packages with encapsulation and exported interfaces.
25. Kafka is used for distributed transactions, with retry mechanisms.
26. Cassandra supports SQL databases through standard library drivers.
27. Sample web poker API uses protocol buffers for request/response communication across services.
28. Moving from monolithic systems to microservices is a continuous process.
29. Encapsulated Java MQ and Go service using Scala driver service.


## Kotlin - Ready for Production • Hadi Hariri • GOTO 2016

URL: [https://www.youtube.com/watch?v=R0J_Jl7bKY8](https://www.youtube.com/watch?v=R0J_Jl7bKY8)

 1. Kotlin is a language developed by JetBrains in 2010, designed for interoperability and tooling with Java compatibility.
2. It has been adopted by various companies like Google, Pinterest, and Square. Gradle supports Kotlin, recommending plugins be written in it.
3. Kotlin is open source and available on multiple platforms such as IntelliJ IDEA, Android Studio, Eclipse, NetBeans, Maven, Gradle, Kobalt, Ant, and command-line.
4. Kotlin offers easy interoperability between Java and Kotlin, with a small runtime (900KB) and standard library features like filterMap, flatMap, etc.
5. It is statically typed, compiling down to Java, JVM, and JavaScript. Kotlin follows conventions for accessing objects, functions, and properties from both Java and Kotlin.
6. Kotlin allows top-level functions without the need for classes, reducing boilerplate code. It has immutable (val) and mutable (var) variables with a name: type convention.
7. Kotlin reduces boilerplate code compared to Java. Properties are declared in the class, with val for immutable and var for mutable variables. Constructors can be added to initialize objects. Objects can be used for singletons or other purposes. Functions can be created without specifying return types (default is Unit).
8. Kotlin has features similar to JavaScript, TypeScript, and Scala. It focuses on conciseness, readability, and expressiveness.
9. Kotlin's restricted language design aims to improve readability and maintainability compared to other languages.
10. Kotlin offers various features such as lambda with receiver, extension functions, delegation support, lazy evaluation, and algebraic data types.
11. Lambda with receiver allows accessing an object within a lambda expression without explicitly creating it. Extension functions add new functionality to existing classes without inheritance. Delegation provides first-class support for delegating methods from one class to another. Kotlin has lazy evaluation through asSequence, similar to Java's Stream concept. Algebraic data types use the sealed modifier in Kotlin to restrict a class's inheritance and enable exhaustive checks on its subclasses.
12. Kotlin is a pragmatic language with an easy learning curve, interoperating with Java, allowing for low-risk adoption and mixing of classes. It offers various features like sealed classes, co-routines, data class hierarchies, type aliases, deconstructing lambdas, bound method references, delegated properties, local, and Java 8/9 support. Kotlin is committed to providing Java 6 support but improves code optimization for Java 8/9.
13. Resources include kotlinglang.org, try.kotlinglang.org (in-browser IDE), books, community on Slack, Twitter, and forums. Kotlin aims to be enjoyable and provides a starting point for converting Java classes into Kotlin code using IntelliJ.
14. Kotlin provides Java 6 support, but improves for Java 8/9 with code optimization and functionality. Includes JavaScript and Native support (Kotlin to Native). Try.kotlinglang.org offers an in-browser IDE without installation. Kotlin books are available, including "Kotlin for Android Developers". Active community on Slack, forums, and Twitter.
15. JetBrains' commitment to Kotlin is due to its use in their products.


## MicroPython & the Internet of Things • Damien George • GOTO 2016

URL: [https://www.youtube.com/watch?v=EvGhPmPPzko](https://www.youtube.com/watch?v=EvGhPmPPzko)

 - Damien George, a former theoretical physicist, developed Micro Python to run on microcontrollers.
- Reasons for choosing Python: Large community, easy learning curve, shallow but long learning curve, native bitwise operations, and distinction between integer and floating point numbers.
- Challenges with existing Python implementations: High memory usage, inefficient method calls, heap memory allocation, and garbage collection.
- Micro Python features: Optimized memory usage, no heap memory, no garbage collection, and a small runtime environment.
- Kickstarter project: Launched in 2013 to fund the development of Micro Python for microcontrollers.
- Goals: Reduce memory consumption and improve efficiency.
- MicroPython uses interned strings, fixed numbers, optimized method calls, ahead-of-time compilation with a virtual machine, static allocation, and garbage collection reduction.
- Open source project hosted on GitHub allows community contributions and feedback from different platforms.
- Runs on the Pi board (192k RAM, 1MB ROM) at 168 MHz and can be used as a lightweight Python implementation for desktop testing.
- Used in various projects like European Space Agency, BBC micro:bit, and Internet of Things chips.
- Kickstarter campaigns raised funds for developing Micro Python for specific hardware.
- Micro Python is not a full version of Python but aims to enable Python to run where it couldn't before.
- Features include JSON support, hardware access through the machine module, web server capabilities, and Wi-Fi connectivity.
- Access to hardware features like GPIO pins and PWM function for controlling LEDs with adjustable frequency.
- Ongoing work includes async I/O support, multi-threading, and integration with other languages.
- Micro Python is suitable for low-power, small devices like Arduino C or embedded C.
- It can be used in various applications such as internet-connected coffee machines and teaching courses.
- The future of micro Python lies in its growth as an open source project with a sustainable community.


## Using Modern C++ In Anger • Todd Montgomery • GOTO 2016

URL: [https://www.youtube.com/watch?v=9KljYagEPnE](https://www.youtube.com/watch?v=9KljYagEPnE)

 1. Aaron is a modern messaging transport designed for low latency and predictable performance, focusing on simplicity, integration, and composability.
2. The architecture consists of client, conductor, driver, and media components.
3. A C++ version of the driver is in development, allowing C++ applications to communicate with other languages.
4. Modern C++ (C++11 and beyond) emphasizes resource ownership and lifetime management through mechanisms like RAII, smart pointers, lambdas, and function objects.
5. Smart pointers include shared_ptr for reference counting, weak_ptr for soft references, and unique_ptr for single ownership.
6. Lambdas and function objects simplify code and make it more powerful but can be tricky to use effectively.
7. C++11 introduced new features like lambdas, function objects, atomic operations, thread support, move construction, and assignment.
8. Modern tool chains improve development efficiency (e.g., make, Google Tasks, JetBrains' SeaLion).
9. Lambdas, atomic operations, thread support, and tool chains are essential for modern C++ development.
10. Lessons learned: lambdas, atomic operations, thread support, and tool chains are crucial for modern C++ development.
11. Stack allocation is vital for performance, especially in high-performance systems.
12. Value types can reduce memory usage and improve performance.
13. Move construction and assignment can be tricky; sometimes copying may be better than moving.
14. The rule of three/five/zero helps understand the interaction between different constructors and assignment operators.
15. Iterating over collections like images or block buffers can benefit from maintaining arrays instead of using move constructors.
16. Move constructors and assignment operators have deeper implications than just providing mechanisms.
17. Rule of three, rule of five, and rule of zero are guidelines for using these features effectively.
18. Sometimes language features aren't built for specific tasks; alternative solutions may be better.
19. C++11 introduced atomic operations and memory models to address interoperability issues with other languages like Java.
20. A project focused on improving IPC performance in C++ achieved 32 million messages per second, outperforming Java (15 million) and job (started at 15 million).
21. Optimizations in C++ lead to better performance.
22. Working on persistence, replication, and error correction for log buffer structure.
23. Collaboration with other developers leads to innovative ideas.



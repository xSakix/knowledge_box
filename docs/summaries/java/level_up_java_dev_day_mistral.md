## Java Management Service - Managing Your Java Estate Just Got Easier

URL: [https://www.youtube.com/watch?v=tvcC2FMwIIo](https://www.youtube.com/watch?v=tvcC2FMwIIo)


- Java Management Service started offering in 2021.
- Common question: Do I need to manage Java runtimes?
  * Reason for managing Java runtimes: Updating Java runtime can lead to collaboration between developers, improved performance, and security vulnerability fixes.
  * Frequent updates: Java releases a new version every six months, with critical patch updates every quarter.
  * Long-term support (LTS) releases get eight years of support, while non-LTS releases have only six months.
  * Separation between developer code and runtime: Updating the runtime does not require changing the developer code.
  * Open source Java Development Kit (JDK): Oracle contributes to open JDK, which can be updated separately from your application.
- Importance of updating Java runtimes:
  * Security vulnerability fixes: Keeping your Java runtime updated helps protect against known vulnerabilities.
  * Performance improvements: Updating can lead to improved performance in some cases.
  * New features and APIs: Staying current with the latest Java releases allows you to take advantage of new features and APIs.
- Disabling old encryption algorithms:
  * Oracle disables older encryption protocols, such as SSLv3 and TLS 1.0/1.1, in their Java runtimes.
  * Updating your runtime ensures that you are using modern encryption to secure your applications.
- Upgrading within a release family vs. upgrading to a new version:
  * Upgrading within a release family requires less effort and risk compared to upgrading to a new version.
  * However, upgrading to a new version may offer significant benefits, such as new features and performance improvements.
- Redistributing updated Java runtimes:
  * When updating your Java runtime, you may need to redistribute the updated runtime to your users.
  * This can be done by providing them with the updated bytecode or a precompiled application.
- JMS (Java Message Service):
  * JMS is a messaging system that can help manage and distribute updates to your Java applications.
  * It can also provide advanced features, such as flight recording and centralized management of your Java runtimes.
- Using JMS for updating Java runtimes:
  * JMS can help you update your Java runtimes more efficiently by automating the process and providing advanced features.
  * You can use JMS to check which versions are installed, install new versions, and remove old ones.
- Advanced features in JMS:
  * JMS offers advanced features, such as flight recording and centralized management of your Java runtimes.
  * These features can help you monitor and manage your applications more effectively.
- Costs associated with using JMS:
  * Using JMS may involve additional costs, such as storage fees for data collected by the service.
  * However, these costs are typically outweighed by the benefits of using JMS to manage and update your Java runtimes.


## OpenJDK - Change the Future of Java

URL: [https://www.youtube.com/watch?v=09W8wh6rHJM](https://www.youtube.com/watch?v=09W8wh6rHJM)


- The OpenJDK community is a collaborative effort where anyone can contribute.
- Java is an important technology used in various industries, especially finance and banking.
- Java has been releasing new versions every six months for years, with JDK 20 being the latest release.
- The release process involves several phases: ramp phase, RC release candidate phase, and GA (General Availability) release.
- OpenJDK is an open source project that focuses on improving Java performance and adding new features.
- Projects like Panama, Valhalla, and Loom aim to make the Java platform easier for developers to use.
- The community maintains a mailing list for discussing issues and collaborating on solutions.
- Quality outreach programs help ensure that issues are discovered and addressed early.
- Contributing to OpenJDK can lead to recognition and opportunities to work directly with engineers.


## Java Virtual Threads

URL: [https://www.youtube.com/watch?v=MOgynY7VIJI](https://www.youtube.com/watch?v=MOgynY7VIJI)


- The speaker discussed Project Loom, a new feature in Java that allows for virtual threads.
- Goals of Project Loom include allowing developers to write high throughput server applications and enabling effective concurrency without dealing with different types of asynchronous programming.
- Virtual threads are lightweight user mode threads that can run within a single Java process, potentially allowing hundreds of thousands or even millions to run concurrently.
- The speaker warned that the preview API may change in the future and encouraged feedback.
- Virtual threads were initially inspired by JavaScript's thread model but faced issues with operating system threads being expensive.
- Project Loom provides a way to make threads cheaper by using virtual threads, allowing Java developers to write code without worrying about thread details.
- The speaker mentioned that rewriting entire programs in a different language like Kotlin might be necessary to avoid observability and debugging challenges in concurrent programming with Java.
- The use of synchronous programming can lead to performance issues due to user blocking APIs, but asynchronous programming with virtual threads provides better performance.
- Virtual threads can improve the performance of CPU-intensive tasks by allowing for parallelization.
- In a microbenchmark, using virtual threads resulted in faster execution times compared to platform threads.
- The speaker emphasized that Project Loom is not meant to replace classical Java threads but rather to provide an alternative way to handle concurrency and improve performance.
- Project Loom includes a new concurrent lock called javutil ConcurrentLock, which is lock friendly and provides good observability.
- Virtual threads may require significant modifications to existing code, as they change the behavior of classic Java threads.
- The use of virtual threads may introduce additional overhead due to the need for context switching and scheduling.
- The speaker mentioned that Project Loom is still an incubator project and there may be challenges in implementing it at scale.
- Virtual threads may require careful consideration when dealing with resource limitations, as they can increase concurrency and potentially lead to increased stress on resources.


## Building High Performance Microservices for Java with Micronaut & GraalVM

URL: [https://www.youtube.com/watch?v=0PN3KeLNC5U](https://www.youtube.com/watch?v=0PN3KeLNC5U)


* Bert Beckwith from Oracle Micronaut team talks about Micronaut and its integration with GraalVM.
* Micronaut was created to address issues of bloat, reflection, and slow performance in Spring applications.
* Micronaut uses class code scanning instead of runtime scanning, resulting in smaller apps and faster execution times.
* GraalVM's native image feature is used to create static executables with pre-compiled code for even better performance.
* Micronaut does not use reflection or dynamic class loading, which saves memory and eliminates the need for JIT compilation.
* Micronaut supports various databases, including Oracle Autonomous Database, and offers simplified configuration using environment variables.
* Micronaut's repository pattern allows for easy database access and transaction management.
* Micronaut offers various testing frameworks, such as JUnit, Spock, and Kotlin Test, and supports dependency injection through constructor injection.
* Micronaut can be used to create native images using Gradle or Maven and runs faster than traditional Java applications.


## Moving the Java Community Forward

URL: [https://www.youtube.com/watch?v=cntO7bA1xRc](https://www.youtube.com/watch?v=cntO7bA1xRc)


- Speaker is a Java developer from Oracle's relation team and has spent 29 years using Java.
- Java ecosystem is rich and robust, providing a continuous learning path for developers.
- Oracle Java team offers various resources to help developers advance their knowledge and skills.
- Java continues to be relevant due to its long history and the large number of businesses and use cases it serves.
- Innovation in Java is important to address modern application development challenges and opportunities.
- Java's stable and predictable release cycle helps enterprises and organizations plan for the future.
- OpenJDK project allows developers to participate in the innovation process and provide feedback.
- Java user groups are a great way to learn from peers, share knowledge, and understand best practices.
- Oracle invests in accelerating Java knowledge forward through various channels like InsideJava, podcasts, and YouTube.
- Official Java certification program offers a way for developers to validate their skills and extend their careers.
- Java developer relation team continues to grow and bring new expertise and talent to the community.


## GraalVM Native Image — Faster, Smarter, Leaner

URL: [https://www.youtube.com/watch?v=sI-zXYLKzfk](https://www.youtube.com/watch?v=sI-zXYLKzfk)


* Sean Smith from Oracle's Growl VM team discusses the benefits of using GraalVM Native Image for Java applications.
* Native Image is a technology that compiles Java bytecode into machine code at build time, resulting in faster startup times and lower memory consumption during runtime.
* The process involves analyzing application dependencies, statically linking classes and libraries, and generating native executables or shared libraries.
* Native Image can significantly improve performance by reducing the need for JIT compilation and garbage collection, as well as eliminating unused code and methods.
* The speaker provides an example of using GraalVM with Micronaut, demonstrating a reduction in startup time from 706 milliseconds to 44 milliseconds and a decrease in memory consumption.
* Security is another benefit of Native Image, as it does not load new code during runtime, making it harder for attackers to exploit vulnerabilities through the classpath.
* The speaker also discusses the challenges of using Native Image with frameworks that rely on reflection or dynamic loading and how to address these issues.
* Native Image is becoming increasingly popular in production environments due to its performance benefits and ease of use, especially for modernizing legacy applications.


## Z Garbage Collector: The Next Generation

URL: [https://www.youtube.com/watch?v=OnodHoNYE1Y](https://www.youtube.com/watch?v=OnodHoNYE1Y)


- Paul Sue from Oracle presented on various Java garbage collectors and their use cases.
- HotSpot Garbage Collection Team maintains a GC tuning guide for JDK releases.
- ZGC is a low latency, scalable collector designed to handle Java heaps of various sizes.
- ZGC has a concurrent mark phase and concurrent relocate phase.
- It uses a colored pointer technique to achieve concurrency.
- ZGC provides constant sub-millisecond pause times.
- ZGC automatically adjusts the number of GC threads based on workload.
- ZGC is available on various platforms including Linux, Windows, Mac OS x86, and ARM.
- Generational hypothesis is a concept used in ZGC to handle higher allocation rates.
- Weak generational hypothesis assumes that most Java application objects are short-lived.
- ZGC focuses on collecting young generations for increased efficiency and lower overhead.
- The speaker recommends trying the Early Access binary of ZGC for feedback.


## JavaFX 20 and Beyond

URL: [https://www.youtube.com/watch?v=f8TOo8TL4-k](https://www.youtube.com/watch?v=f8TOo8TL4-k)


* Kevin Rushforth presenting JavaFX 20 features and future plans.
* JavaFX is a rich graphic medium content application toolkit, available on desktop, mobile, and embedded platforms.
* JavaFX provides UI control using CSS styling and layout containers.
* JavaFX includes built-in charting capability for 2D and 3D graphics.
* JavaFX supports Swing interop and property binding API.
* JavaFX is hardware accelerated and supports various native platform APIs.
* JavaFX offers automatic fallback support on older Linux machines.
* JavaFX includes the Ensemble sample application and Jpackage for easy distribution.
* JavaFX has a six-month release cadence, with notable features including 3D spotlight ability, HTTP live streaming, and improved constraint resize policy.
* JavaFX 20 was released on March 21, 2023, and includes several enhancements and bug fixes.
* JavaFX Notebook is a utility for creating interactive documentation and code examples.
* JavaFX supports stylized text with syntax highlighting and inline images.
* JavaFX is working on providing a rich text area control and virtualization support.
* The JavaFX team is addressing deprecated libraries, such as the opengl library, and exploring DirectX 11/12 support.


## Helidon - Microservices on Modern Java

URL: [https://www.youtube.com/watch?v=diUvR6gqHVY](https://www.youtube.com/watch?v=diUvR6gqHVY)


* Joe DePaul introduces Heladon, a Java framework for writing microservices.
* Heladon supports both reactive and blocking programming models.
* It is based on Virtual Threads, which are lightweight threads managed by the JVM.
* Heladon offers good performance and high concurrency with virtual thread support.
* It's compatible with Java SE applications and Jakarta EE applications.
* Heladon supports microprofile, a de facto standard for writing microservices in Java.
* Virtual threads are scheduled onto platform threads, which can perform blocking operations.
* Developers should be aware of the potential issues when using virtual threads, such as thread pools and pinning.
* Heladon 4 introduces Nema web server, a high-level abstraction for writing microservices with virtual threads.
* Virtual threads are more efficient than traditional threads in terms of concurrency performance.
* Developers can experiment with retrofitting existing servers using virtual threads for better performance.
* Heladon's performance improvements include faster request processing and handling multiple streams in HTTP 2 connections.
* Heladon supports thread local variables, which can be useful in managing resources and caching.
* Virtual threads cannot unmount carrier threads due to certain JDK limitations, requiring additional platform threads or locking constructs.
* Developers should refactor their code to eliminate synchronized blocks and use locking constructs instead for better concurrency.
* Heladon's new features include scoped values and structured concurrency, which can improve API caching and manage tasks hierarchically.
* Virtual threads are a significant improvement in Java programming, especially for concurrent applications.


## Evolving the Security of the Java Platform

URL: [https://www.youtube.com/watch?v=3O4JtWcmkVQ](https://www.youtube.com/watch?v=3O4JtWcmkVQ)


* Francis Ho and Brad Wetmore discuss Java security in the context of the evolving Java platform.
* Java security consists of language runtime security functionality, a set of APIs for implementing various security features, and a comprehensive framework for building, deploying, and using modern strong algorithms and protocols.
- The Java Security Group, consisting of Oracle and external developers, is responsible for designing, implementing, and maintaining the Java security component.
* The Java platform continuously evolves to adapt to the dynamic security threat landscape by adding support for stronger algorithms and protocols, providing a secure environment for applications, and offering tools to diagnose security issues.
- Some of the recent significant security feature enhancements include the addition of TLS 1.3, Argon2id password-based key derivation algorithm, and support for hybrid public key encryption.
* The Java platform also includes various cryptographic primitives like message digests, ciphers, and digital signatures, which are used in higher-level protocols like TLS 1.3.
* The Java Security Manager feature was originally designed to provide a sandbox for running untrusted applets but has been enhanced to support fine-grained permission models.
* The Java platform supports interoperability and algorithm extensibility through the use of service provider interfaces (SPIs) and multiple implementation algorithms.
* Applications can use the JCA framework to find and instantiate cryptographic providers, which offer different variants of algorithms, and obtain a final message digest or signature using the chosen provider's implementation.
* The Java platform includes a default set of service providers covering a broad range of comprehensive algorithms that are continually updated.
* OpenJDK is an open source project that has almost entirely implemented security areas except for verifying third-party JCE providers used within the framework.
* The cryptographic landscape changes at a fast pace, with algorithms like MD5 and SHA1 becoming weak and obsolete over time. It's essential to continually update default key sizes and use stronger algorithms to protect against emerging threats.
* The Java platform is working on creating post-quantum cryptographic algorithms to ensure security against quantum computers.
* The Java Security Group encourages feedback from developers and customers through various channels, including mailing lists and surveys, to improve the platform continuously.


## Java 20: Reviewing the Enhancements in the Latest JDK Release

URL: [https://www.youtube.com/watch?v=0mo7rEwGaHk](https://www.youtube.com/watch?v=0mo7rEwGaHk)


* JDK 20 is a new feature release every six months.
* It includes support for record pattern, which makes it easier to deconstruct and access data in records.
* JDK 20 also introduces a switch expression statement, allowing developers to test expressions instead of constants.
* Project Panama aims to make Java interoperate with foreign code more easily through foreign function memory APIs.
* Loom is a project that makes it possible to write Java programs for handling bound tasks in a simpler and more efficient way.
* JDK 20 brings back the second preview of record pattern, making it easier to deconstruct records at different nesting levels.
* Record pattern access can be used directly in switch expressions, reducing the need for intermediate variables.
* Project Panama's vector API provides significant performance improvements through vector computation and auto-vectorization.
* JDK 20 includes structural concurrency APIs to make it easier to write concurrent code using a structured approach.
* Structural concurrency allows developers to split sequential code into concurrent flows and join them back together, making error handling and cancellation more streamlined.
* The new APIs are designed to be clear, concise, and consistent with the structural concurrency principle.
* JDK 20 is available for download from Oracle's website and can be installed using various methods, including Docker images.


## Java Language Futures, Spring 2023 Edition

URL: [https://www.youtube.com/watch?v=NA-sB3zvluE](https://www.youtube.com/watch?v=NA-sB3zvluE)


- Spring 2023 Edition: Java language features, continually updated with incremental improvements.
- Project Amber: Explores smaller productivity-oriented Java language features.
- Goals: Make programming experience convenient, comfortable, quicker, and smoother.
- Features: Record pattern matching, switch expressions, text blocks, instance of type patterns, etc.
- Pattern Matching: Allows checking for specific types and values in a more concise way.
  - Switch statements can now use patterns instead of constants.
  - Records can be pattern matched directly.
  - Extract data from objects using methods or fields.
- Record Patterns: Simplify handling records by extracting components directly.
- Sealed Classes: Enhance exhaustiveness checking for switch statements.
- Syntax Changes: New syntax for pattern matching, record patterns, and more.
- Continuous Improvement: JDK releases every six months with new features and bug fixes.
  - Projects like Amber, Valhalla, Panama, and Loom are ongoing efforts.
- Record Pattern Matching: Extract data from records using pattern matching.
- Switch Expressions: Use patterns instead of constants in switch statements.
- Text Blocks: Create multiline strings without escape sequences.
- Instance of Type Patterns: Check for specific types and values in a more concise way.
- Syntax Changes: New syntax for record patterns, instance of type patterns, and more.
- Sealed Classes: Improve switch statement exhaustiveness checking by permitting only certain subclasses.
- Continuous Improvement: JDK releases every six months with new features and bug fixes.
- Record Patterns: Extract components from records using pattern matching.
- Switch Expressions: Use patterns instead of constants in switch statements.
- Text Blocks: Create multiline strings without escape sequences.
- Instance of Type Patterns: Check for specific types and values in a more concise way.
- Syntax Changes: New syntax for record patterns, instance of type patterns, and more.
- Sealed Classes: Improve switch statement exhaustiveness checking by permitting only certain subclasses.
- Continuous Improvement: JDK releases every six months with new features and bug fixes.


## Troubleshooting Native Memory Issues in Java Applications

URL: [https://www.youtube.com/watch?v=NI16bqeGv7U](https://www.youtube.com/watch?v=NI16bqeGv7U)


* The speaker is discussing troubleshooting native memory issues in Java applications.
* Native memory errors occur when the JVM cannot allocate native memory resources.
* The causes of native memory errors can be within or outside the JVM, such as from JNI or direct Java application allocations.
* Tools like Pmap and JConsole can help diagnose native memory leaks by monitoring memory usage and identifying growing segments.
* External tools like Valgrind and Je Malloc can track native memory allocation done both internally and externally to the JVM.
* Common causes of unexpected Java application memory growth include compressed OOPs, incorrect Java Heap placement, or direct byte buffer allocations.
* To prevent native memory leaks, ensure enough garbage collections are made and finalizer threads get a chance to run.
* Tools like nmt, Je Malloc, Valgrind, Purify, dbx, UMDH, and pmap can be used for diagnosing and resolving native memory issues.


## Continuous Monitoring with JDK Flight Recorder

URL: [https://www.youtube.com/watch?v=Gx_JGVborJ0](https://www.youtube.com/watch?v=Gx_JGVborJ0)


* Michael Vidstead from Oracle talks about JDK Flight Recorder.
* Imagines a business-critical application issue and the need for detailed information to identify and resolve it.
* Introduces JDK Flight Recorder as a continuous data recording tool with low overhead, designed for production use.
* Provides an overview of the event-based tracing framework, including its graphical user interface (JMC) and command line tool.
* Discusses the types of information collected, such as CPU usage, method execution, file I/O, socket usage, thread sampling, and garbage collection.
* Mentions the flexibility of JFR to filter data based on duration and specific events or labels.
* Explains that JFR can be used for analyzing high-level business operations by drilling down into transactions and threads.
* Introduces the concept of a configuration file to set default event codes and customize recording settings.
* Discusses the performance benefits, including low overhead, efficient thread local buffer usage, and optimized disk format.
* Provides examples of using JFR with different tools like Mission Control and the command line tool (jfrdump).
* Mentions the ability to scrub recordings for sensitive information and disassembling larger recordings into smaller chunks.
* Introduces event streaming API in JDK 14 for real-time processing of events.
* Discusses using JFR for unit testing and ensuring applications don't introduce new finalizers.


## Java First. Java Always. | DevLive Level Up Keynote

URL: [https://www.youtube.com/watch?v=nS72gSoieso](https://www.youtube.com/watch?v=nS72gSoieso)


* The speaker thanks everyone for attending Oracle Dev live Java day, both in-person and online.
* They mention there's a great program with three tracks and sessions streaming online.
* They launch JDK 20 and discuss the evolution of Java over the past 28 years.
* Java is popular due to its performance, stability, security, and compatibility.
* OpenJDK Community plays an important role in innovation and development.
* The six-month release cadence allows for predictable updates and developer feedback.
* Innovation is a priority, with projects like Amber, Loom, Panama, and Valhalla improving Java's performance, scalability, and memory management.
* Oracle offers long-term support releases and frequent updates through Java SE subscriptions.
* The Java ecosystem includes a rich community, resources, and educational programs.
* Heather Stevens focuses on Java education for the newest generation of developers.



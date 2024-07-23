## How to Upgrade to Java 21 #RoadTo21

URL: [https://www.youtube.com/watch?v=5jIkRqBuSBs](https://www.youtube.com/watch?v=5jIkRqBuSBs)


- Java 21 includes numerous improvements, including faster GC performance, better security, and virtual threads.
- Developers moving from Java 17 to Java 21 should be aware of changes to existing APIs that may require code updates.
- Several APIs have been deprecated, such as the JDK XSLT transformer and certain networking APIs.
- New features include SequencedCollection and SequencedSet interfaces and virtual threads.
- Dependency conflicts may arise from new interfaces, requiring refactoring and updates to dependencies.
- Changes to Thread API include unconditional throw of UnsupportedOperationException in Threadstop, Threadsuspend, and Threadresume APIs.
- Security improvements include the removal of security manager and deprecated removal of finalization.
- JDK 21 also includes changes to networking, such as a lower idle connection timeout for HTTP client and changes to URL handling.
- Encoding matters, particularly for languages that use non-UTF8 encodings, so developers should be aware of the impact on their projects.
- OpenJDK Quality Outreach program encourages open source projects to test early access builds to improve overall quality.


## Java 21 new feature: Virtual Threads #RoadTo21

URL: [https://www.youtube.com/watch?v=5E0LU85EnTI](https://www.youtube.com/watch?v=5E0LU85EnTI)


* Virtual threads are a new feature in JDK 21 to avoid blocking platform threads.
* They unmount the platform thread instead of blocking it when executing I/O operations.
* Creating virtual threads is much lighter than creating platform threads, allowing for the launching of millions on even small machines.
* Virtual threads run on top of platform threads and share a pool, with one virtual thread running on each platform thread.
* When a virtual thread encounters a blocking I/O operation, it detects it and unmounts the platform thread, moving its context to heap memory.
* Continuation objects are used for this process, allowing the operating system to monitor data and trigger a call to the continuation run method when the data is available.
* The cost of running a task on a virtual thread includes the cost of running the platform thread and overhead. However, blocking virtual threads can save significantly on blocking platform threads.
* Virtual threads cannot be made non-daemon threads or stopped/suspended, but they do not prevent the application from exiting.
* Synchronization objects and native code calls may still pin a virtual thread to a platform thread, affecting performance.
* JVM supports virtual threads in popular frameworks like Jetty, Vertx, Tomcat, Spring, Quarkus, and Spring Boot.


## Java 21 JVM & GC Improvements #RoadTo21

URL: [https://www.youtube.com/watch?v=LXWbyf8SUjI](https://www.youtube.com/watch?v=LXWbyf8SUjI)


- JDK 21 includes a significant change to the Z Garbage Collector.
- The JVM team encourages engineers to take advantage of this opportunity for tweaks, refactors, and even rewrites to improve performance.
- JDK 17 to 21 shows improvements in performance, but there are some regressions in footprint and startup time.
- Performance is a complex topic with three major metrics: throughput, latency, and memory footprints.
- Java's flexibility to run on various operating systems and hardware architectures impacts performance testing.
- The JDK 21 upgrade may come with modest benefits in some use cases but significant gains for others, especially in crypto applications.
- Refactoring has been done in the Java core library classes, particularly in handling primitive value conversions.
- String deduplication was introduced in G1 garbage collector back in JDK 9 to reduce memory fragmentation.
- The G1 garbage collector has undergone several key updates since its introduction, including changes to read size, concurrent refinement, and more.
- Java's newest garbage collector, GDC, focuses on scalability and low latency, able to support 16 terabyte heaps with sub-millisecond pause times.
- Generational garbage collection is a commonly observed pattern in Java applications due to the short lifetime of objects and the implication they tend to die young.
- The Young Generation helps save memory and CPU by handling objects with shorter lifetimes, while the Old Generation handles long-lived objects.
- When dealing with workloads that have many long-lived objects and high allocation rates, a generational garbage collector may be beneficial.
- JDK 21 introduces the Z Garbage Collector as the default, but feedback from users has been positive for Generational ZGC.


## Java 21 Tool Enhancements: Better Across the Board #RoadTo21

URL: [https://www.youtube.com/watch?v=nFJBVuaIsRg](https://www.youtube.com/watch?v=nFJBVuaIsRg)


- Java 17 introduces several new tools and enhancements to JDK, including:
  - JShell for experimenting with Java code.
  - JWebserver for serving web pages.
  - JPackage for creating native installers.
  - JMod for encapsulating modules.
- Javadoc now supports code snippets and markdown formatting.
- JDK 18 brings improvements to serialization, such as handling custom logic using writeReplace and readResolve.
- JDK 21 focuses on security updates, including warnings for weak encryption algorithms and SHA1 jars.
- JFR (Java Flight Recorder) and JMC (Java Mission Control) offer performance monitoring tools.


## Java 21 API New Features #RoadTo21

URL: [https://www.youtube.com/watch?v=4mPd2eL0wYQ](https://www.youtube.com/watch?v=4mPd2eL0wYQ)


* JDK 21 introduces several new features to make development easier.
* String class improvements include an overloaded indexOf method and named groups in regular expressions.
* Collections framework updates include SequencedCollection and SequencedSet, as well as factory methods for creating maps with initial capacity.
* Date Time API enhancements include localization support and the ability to read bytes one at a time from ZipInputStream.
* AutoCloseable resources can now be used in try-with-resources statements for simple resource management.
* Math class additions include new ceilDiv methods, clamp method, and unsignedMultiplyHigh.
* Concurrent programming enhancements include virtual threads and new Future interface methods.
* Deprecated elements include the finalize method in applications and certain constructors for wrapper classes like Integer, Long, Float, and Double.
* Preparation for Value Types (project Valhalla) includes deprecated constructor removal.
* For more information on specific topics, check the episode series link in the description.


## Java 21 Security Updates #RoadTo21

URL: [https://www.youtube.com/watch?v=kSjdZZsHM04](https://www.youtube.com/watch?v=kSjdZZsHM04)


* Java Security consists of Language Runtime Security functionality and comprehensive set APIs.
* The Java Security component includes cryptography, PKI, Transport Layer Security, XML Signature, and access control features.
* Stronger algorithm protocols continuously replace weaker ones to provide stronger cryptographic protection.
* Java Security evolves to adapt to the dynamic security threat landscape.
* Deprecated algorithms like SHA1 and 3DES are no longer recommended for use due to vulnerabilities.
* JDK 21 introduces new HSSLMS signature verification implementation and Key Encapsulation Mechanism API (KEM) for securing symmetric keys using public key cryptography.
* OS native security features allow access to credential security information on certain operating systems.
* The JDK Flight Recorder (JFR) captures event related cryptographic operations.
* JMX has evolved to include security enhancements like ObjectInputFilter and default JMX agent settings.
* Java Security Roadmap provides advance notice of upcoming security changes and improvements.


## Java 21 Pattern Matching Tutorial #RoadTo21

URL: [https://www.youtube.com/watch?v=QrwFrm1R8OY](https://www.youtube.com/watch?v=QrwFrm1R8OY)


* The speaker discusses the need for an employee management tool and the challenges of implementing disparate operations in a single system.
* They suggest separating Employee functionality into different types (salaried, freelancer) to avoid complex interactions between subsystems.
* Java 21 introduces pattern matching and sealed interfaces which simplify handling of different types without the need for extensive if-else chains or switch statements.
* Pattern matching allows data-driven dispatch of implementation code rather than API code, improving flexibility and reducing complexity.
* Sealed interfaces ensure that only permitted implementations can be used, providing compile-time verification and safety against unexpected types.
* The speaker discusses the benefits of pattern matching compared to traditional API-based polymorphism, including better expressiveness, improved performance, and easier creation of new polymorphic behavior without changing APIs.
* Data-oriented programming is mentioned as an alternative approach that focuses on data representation rather than object-oriented design, which can be beneficial in certain situations.
* Java 21's record feature is highlighted for its simplicity and immutability when representing specific data closely.
* The speaker mentions the use of guarded patterns to add conditions to pattern matching cases.
* Unnamed pattern variables are introduced as a new feature in JDK 21 that can make switch statements more succinct and clearer.
* The speaker thanks Angelos Bimpoudis for his contributions to Java and mentions some upcoming features in Java 25, including virtual threads and improved security and performance APIs.

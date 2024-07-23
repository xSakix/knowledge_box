## Project Leyden - Capturing Lightning in a Bottle #JVMLS

URL: [https://www.youtube.com/playlist?v=lnth19Kf-x0](https://www.youtube.com/playlist?v=lnth19Kf-x0)


* Project Leiden aims to improve startup time and warmup time in Java programs.
* The team proposes shifting computation temporarily forward or backward in time.
* This approach may require static analysis and specification changes, especially for dynamic languages like Java.
* Condenser is a new tool that enables selective computation shifting by encoding the program image ahead of runtime.
* It preserves the meaning of the original program while enabling better shifting computation and reducing startup time.
* The team explores closed World constraint to constrain Java's natural dynamism for improved shifting computation.
* They also discuss training run, which gathers profile information for deployment runs and optimizes based on that data.
* CDs (Class Data Sharing) are used to save metadata and class data for faster application startup.
* The team mentions the importance of speculative optimization and deoptimization in JIT compilation.
* They also discuss the benefits of using a tiered compilation approach and the role of hotspot analysis in optimizing performance.
* The presentation covers various related improvements, including CDS archives, jModelS, and jlinking.


## Code Reflection #JVMLS

URL: [https://www.youtube.com/watch?v=xbk9_6XA_IY](https://www.youtube.com/watch?v=xbk9_6XA_IY)


* The speaker is discussing the challenges of writing Java code for machine learning and GPU programming, specifically focusing on automatic differentiation.
* They mention issues with using non-Java code snippets in Java programs, the limitations of APIs, and the difficulty of emulating language features within APIs.
* The speaker advocates for designing APIs to better support code modeling, access analysis, and transformation to improve the developer experience.
* They discuss the challenges of dealing with bytecode and class files, especially in the context of machine learning models and Java's limitations in this area.
* The speaker also touches on the importance of understanding the compiler strategy and how it affects program meaning and behavior.


## A Classfile API for the JDK #JVMLS

URL: [https://www.youtube.com/watch?v=pcg-E_qyMOI](https://www.youtube.com/watch?v=pcg-E_qyMOI)


- Maurizio Gary Paul discussed the challenges of designing a class file API.
- The JDM spec called for class file support, but the existing API was unsatisfactory.
- The design process involved several false starts and iterations to balance user ergonomics, performance, and safety goals.
- Class file processing is pervasive in the Java ecosystem, with many tools and libraries using it.
- The JDK has its own class file generation and manipulation mechanisms, but they have limitations and can be improved.
- Rapid evolution of the class file format requires careful API design to maintain compatibility and avoid breaking changes.
- Designing a new class file library involves considering various trade-offs, such as performance, ease of use, and consistency.
- The speaker emphasized the importance of aligning reading and writing APIs, using common vocabulary, and designing for composability.
- ASM and Azim are popular class file processing libraries, but they have different design philosophies and limitations.
- The speaker advocated for a more expressive and flexible API that allows users to explore and transform class files in various ways.


## Value Objects in Valhalla #JVMLS

URL: [https://www.youtube.com/watch?v=a3VRwz4zbdw](https://www.youtube.com/watch?v=a3VRwz4zbdw)


- Dan Smith from Valhalla project discussing key features, focusing on direct representation benefit for Primitives and object class.
- Primitives and objects have different ways of storing data: Primitives use a single storage location, while objects live in the Heap with unique identities.
- Direct representation benefit includes performance optimization through stack optimizations, eliminating pointer dereferences, and avoiding garbage collection.
- Valhalla project aims to bring value types to Java, making it more like C++ in memory layout and improving language approach.
- Primitives are treated as classes with unifying type system, allowing runtime specialization and generic support.
- Value objects have the advantage of being freely copyable and unlocking optimization opportunities.
- The example of a Point class illustrates the difference: traditional Java code involves creating an object for every pixel in an image, while modern hardware prefers neatly collected data in one place.
- Valhalla offers programmer choice with layout optimization, allowing tradeoffs between performance and design principles.
- The project has been ongoing since 2014, with a focus on expressing value types in the JVM and figuring out how to make generic work with primitive-like behavior.
- Some challenges include handling nullness, flattening Heap storage, and managing concurrency.
- Future work includes implementing Loosely Consistent Values and optimizing for null restrictions.
- The goal is to provide a more efficient memory layout for Java, allowing for better performance in specific use cases.


## JVM Language Summit 2023 Keynote #JVMLS

URL: [https://www.youtube.com/watch?v=Ma0NtbG0mHY](https://www.youtube.com/watch?v=Ma0NtbG0mHY)


* George Saab from Oracle welcomes attendees to the Java and JVM Summit 2023.
* He mentions that the conference is an opportunity for experts in the industry to connect, share ideas, and provide feedback on Java and JVM.
* Saab discusses the importance of continuous innovation and the need to balance new features with stability.
* He highlights several projects, such as Amber (pattern matching), Loom (virtual threads), and Valhalla (unified types), that have made significant progress since their introduction.
* Saab also talks about the evolving nature of Java, including its focus on developer productivity, performance, and constant evolution to meet changing needs.


## Java and GPU … are we nearly there yet? #JVMLS

URL: [https://www.youtube.com/watch?v=lbKBu3lTftc](https://www.youtube.com/watch?v=lbKBu3lTftc)


- Speaker Gary Frost discusses building top work with GPUs, focusing on the challenges of Java interacting with GPU accelerators.
- He mentions that he's been interested in this problem for over a decade and has tried various approaches like VM abstractions and code reflection.
- The speaker believes that the mistake was trying to hide behind APIs and instead suggests opening up APIs for better interaction between Java and GPUs.
- He introduces the concept of a heterogeneous accelerator toolkit, which sits on top of Panama and is designed to make it easier to use GPUs in Java applications.
- The toolkit uses ND range, similar to GPU usage, and allows for code reflection and data layout optimization.
- The speaker also mentions the importance of efficient data representation and exchange between Java and GPUs, which can be achieved through Panama's FFM API.
- He discusses the benefits of using a task graph mechanism, which allows explicit control over data movement and avoids unnecessary transfers.
- The speaker also touches on the challenges of managing multithreaded and multi-core environments, as well as the importance of efficient memory management in GPUs.


## Fast JVM Startup with Checkpoint & Restore #JVMLS

URL: [https://www.youtube.com/watch?v=WC98nTslxKQ](https://www.youtube.com/watch?v=WC98nTslxKQ)

### Fast JVM Startup using Checkpoint Restore

* Toby Ill from IBM OpenJ9 team talks about fast JVM startup using checkpoint restore.
* Motivation: Need for faster startup time in cloud environments to minimize compute cost and improve user experience.
* Existing techniques for improving startup time include class metadata caching, static compilation, and checkpoint restore.

### Class Metadata Caching

* Saves internal state instead of rebuilding it at subsequent runs.
* OpenJ9 uses shared class cache for this approach.
* Benefits: Faster path to application readiness; drawbacks: requires JVM restart and custom class loader changes.

### Statically Compile Application

* Avoids loading and running static initializers, which contribute significantly to startup time.
* Native image is an effective solution for this approach.
* Benefits: Faster application start and smaller footprint; drawbacks: requires code change and closed world analysis limitations.

### Checkpoint Restore

* JVM runs a checkpoint when substantial initialization has been completed, then restores the application from the saved state instead of starting from scratch.
* Benefits: Much faster startup time, gets class metadata caching and static compilation benefits; drawbacks: larger disk space requirement and code change for existing applications.
* Cru (Checkpoint Restore Utility) is a user-space tool that takes running container checkpoints, serializes the state to disk, and restores it when needed.
* OpenJ9's support for series enables Java users to take advantage of Cru's capabilities.


## The Challenges of Introducing Virtual Threads to the Java Platform - Project Loom  #JVMLS

URL: [https://www.youtube.com/watch?v=WsCJYQDPrrE](https://www.youtube.com/watch?v=WsCJYQDPrrE)


- Project Loom introduced virtual threads four years ago.
- A virtual thread is a lightweight thread managed by the JVM, allowing for more efficient multithreading and improved performance.
- Virtual threads replace traditional operating system threads and are scheduled within the Java Virtual Machine.
- The JDK 19 and later previews include new APIs to create, configure, and manage virtual threads.
- Serviceability features like thread dumps and Java Flight Recorder have been updated to support virtual threads.
- Continuation and scheduling improvements allow for more efficient handling of blocking operations.
- Virtual threads can be used in a variety of applications, including web servers and enterprise applications.
- The ecosystem is showing significant interest in virtual threads, with many articles and projects being developed.
- Challenges remain, such as managing memory usage and dealing with existing code that assumes thread pools.
- JVMTI debugging tools have been updated to support virtual threads, but there are still performance challenges to address.


## Project Panama - Foreign Function & Memory API #JVMLS

URL: [https://www.youtube.com/watch?v=kUFysMkMS00](https://www.youtube.com/watch?v=kUFysMkMS00)


- The speaker is discussing the use of Project Panama's Foreign Function Memory API for accessing foreign memory and functions in Java.
- The speaker mentions that JNI, which has been used for this purpose in the past, can be convoluted and difficult to maintain due to its native library dependencies and manual memory management.
- The FFM API is a new feature in Java 22 that simplifies accessing foreign memory and functions by providing a more straightforward interface and eliminating the need for JNI.
- The API consists of two parts: one for accessing foreign memory, and another for accessing foreign functions.
- Memory segments are used to represent contiguous regions of memory, and they provide safety features such as bounds checking and lifetime management.
- The speaker discusses some challenges with the FFM API, including the need to specify offsets manually and the potential for performance issues due to garbage collection.
- The speaker compares the FFM API to other solutions, such as Rust's memory safety features and C++'s manual memory management.
- The speaker also mentions some potential improvements to the FFM API, such as adding deterministic location APIs and better support for spatial and temporal safety.


## Continuations - Under the Covers #JVMLS

URL: [https://www.youtube.com/watch?v=6nRS6UiN7X0](https://www.youtube.com/watch?v=6nRS6UiN7X0)


- The speaker discusses the implementation of virtual threads in JDK and their differences from user mode threads.
- Virtual threads do not provide performance benefits through fast context switching but require efficient total latency and minimal CPU consumption.
- There are different types of continuations, including nonreentrant, delimited, asymmetric multipronged, and suspended continuation bodies.
- Continuations allow for nesting inside one another and can be implemented using the Java Virtual Machine (JVM) and its scheduler.
- The JVM uses a thread stack and continuation stack to manage threads and continuations respectively.
- Implementing lazy copy of frames is an alternative to copying entire stacks, which reduces memory usage but requires careful management of object references and garbage collection.
- The speaker discusses the challenges of implementing lazy copy in the context of garbage collection and object management.
- The JVM uses a garbage collector (GC) to manage objects' memory allocation and deallocation, which can impact thread performance when scanning thread stacks.
- Implementing lazy copy involves freezing frames, copying byte arrays, and patching back the copied data into the original frame.
- The speaker discusses the advantages of lazy copy, including reduced memory usage and improved performance.
- Continuation objects contain a thread stack and are used to manage continuations within threads.
- Implementing lazy copy requires careful management of object references and garbage collection, especially when dealing with heap objects and primitive types.
- The speaker discusses the challenges of implementing lazy copy in the context of garbage collection and object management, including the need for synchronized freezing and thawing, as well as managing the GC's view of objects.
- Lazy copy involves allocating new stack chunks when needed and copying frames back and forth between old and new chunks efficiently.
- The speaker discusses the potential benefits of lazy copy, including improved performance and reduced memory usage.


## Project Lilliput - Compressed Object Headers #JVMLS

URL: [https://www.youtube.com/watch?v=9ioh6kprnPE](https://www.youtube.com/watch?v=9ioh6kprnPE)


- Roman is discussing project Lutiput, which aims to compress object headers in Java Heap to reduce memory footprint.
- Lutiput has already reached Milestone 1, reducing the size of the object header from two words to one word.
- The goal is to eventually reduce the header size to four bytes per object.
- The current situation involves a 12 byte object header size, with the potential for savings around 7-10 bytes per object.
- Lutiput uses unused bits in the object header to store additional information, such as metadata and mark words.
- One challenge is safely accessing class pointers when they are displaced by forwarding pointers.
- Another challenge is GC forwarding, which requires copying objects during full GCs and can be slow.
- Lutiput uses a sliding forwarding technique to minimize the impact of GC forwarding on performance.
- Monitor locking is also a challenge, as it requires additional space for monitor pointers.
- One potential solution is compressing monitor pointers using techniques similar to class pointer compression.
- Another potential solution is using a separate hash table for object monitoring.
- The goal is to minimize the impact of Lutiput on performance while maximizing memory savings.


## Generational ZGC and Beyond #JVMLS

URL: [https://www.youtube.com/watch?v=YyXjC68l8mw](https://www.youtube.com/watch?v=YyXjC68l8mw)


- Eric is discussing generational garbage collection (GC) in the Java platform group at Oracle.
- The goal is to maintain low latency for concurrent applications without inflicting long GC processes on large Heaps.
- Concurrent GC can lead to allocation install issues, where the application allocates memory faster than GC can reclaim it.
- A new feature called generational GC in JDK 21 uses a generational hypothesis to exploit the fact that most Java objects have short lifetimes.
- The young generation is split into two logical parts: Young Generation and old generation.
- Objects are allocated in the Young Generation first, and those that survive a collection get promoted to the old generation.
- This allows for more efficient memory reclamation and improved CPU usage.
- The layout of the Heap is discontiguous, with regions separated by free memory.
- Concurrent marking and relocation phases are used to minimize application downtime during GC.
- Automatic tuning is designed to simplify the process for developers by handling most decisions automatically.
- Large young generations can be a challenge due to their size and allocation rate.
- Colored pointers allow for more efficient memory reclamation in generational GC.
- The tenuring threshold determines when objects are promoted from the Young Generation to the old generation based on their age.
- Cost modeling is used to automatically compute the number of threads needed for GC based on the allocation rate.
- Store barriers are used to ensure that GC can detect changes to fields and take appropriate action.
- Colorless roots are an alternative memory representation that eliminates the need for multimapping memory.
- The main challenge with removing color is the extra operation required without adding significant cost.
- Thread local GC is a potential solution for more efficient garbage collection, but it requires careful design to avoid root GC overhead and ensure low latency.
- Project Loom is an upcoming project that aims to make asynchronous code easier to manage by allowing virtual threads to share the same application heap.


## Everything You Never Wanted to Know about Java Class Initialization #JVMLS

URL: [https://www.youtube.com/watch?v=AtbOhgfYhcM](https://www.youtube.com/watch?v=AtbOhgfYhcM)


- Christian Wemaest (architect at Gravy) discusses Java class initialization issues, focusing on the problem and potential solutions.
- Class initializers are executed when a class is first used, which can lead to synchronization and deadlock issues due to implicit synchronization and separate monitors for each class.
- Immutable state should be captured during initialization to avoid potential problems with external state changes.
- Cyclic dependencies in class initializers can cause deadlocks, especially when multiple threads are involved.
- Class initializers often capture external state at random times, making it difficult to recover from changes.
- Security concerns arise when untrusted code is able to initialize trusted code, potentially leading to denial of service attacks.
- Class initialization problems have been a longstanding issue in Java and can be improved through snapshotting and early class initialization.
- Native images can help mitigate some class initialization issues by marking classes as eagerly initialized.
- Static fields should be carefully managed to avoid potential synchronization issues and ensure immutability.


## From CPU to GPU and FPGAs: Supercharging Java Applications with TornadoVM #JVMLS

URL: [https://www.youtube.com/watch?v=VTzGlnv6nuA](https://www.youtube.com/watch?v=VTzGlnv6nuA)


- The speaker is introducing the Eternal VM project, a Java parallel programming framework for heterogeneous hardware.
- Novm is designed to help developers increase performance and decrease energy consumption by efficiently running workload-specific tasks on various types of hardware (GPUs, FPGAs, etc.).
- Novm provides a new API with features like automatic parallelization, task graph building, and execution plan generation.
- The speaker will show a demo using computational photography as an example.
- There are multiple backends for Novm, including OpenCL, PTX, and SPV, which support various types of accelerators.
- The speaker will demonstrate how to use the Tornado framework with Novm to process images more efficiently on different devices.
- Novm's data flow analyzer optimizes performance by minimizing data transfer between components and memory.
- The speaker discusses the design of the Novm API, which includes annotation-based parallelization and a kernel API for expert users.
- The Tornado VM API is designed to be flexible and portable, allowing developers to integrate it into their existing Java projects easily.
- Future plans include integrating Panama and supporting batch processing with automatic device selection based on performance and energy metrics.



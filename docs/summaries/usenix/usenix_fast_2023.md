## FAST '23 - Building and Operating a Pretty Big Storage System (My Adventures in Amazon S3)

URL: [https://www.youtube.com/watch?v=sc3J4McebHE](https://www.youtube.com/watch?v=sc3J4McebHE)

- S3 is a storage service that operates at a massive scale
- The Fleets in the S3 system are constantly growing and evolving, with new hardware being added to improve performance and reliability
- Hard drives play a crucial role in the operation of the S3 system, despite their physical fragility and slow access times
- The S3 system is designed to be highly durable and fault-tolerant, with redundancy built into every layer of the system
- The concept of "organizational scale" is important when considering how the S3 system operates, as it relies on a complex network of teams and individuals working together to maintain and improve the service
- The process of scaling an organization like Amazon involves not only technical challenges, but also cultural and organizational ones
- The concept of "scaling ownership" is key to the success of the S3 system, as it ensures that everyone involved in the operation of the service feels a sense of responsibility and accountability for its performance and reliability
- The S3 system uses a variety of different technologies and tools to manage and store data, including DynamoDB, S3 Connect, and the AWS SDK


## FAST '23 - Practical Design Considerations for Wide Locally Recoverable Codes (LRCs)

URL: [https://www.youtube.com/watch?v=pfnSYWEf5q4](https://www.youtube.com/watch?v=pfnSYWEf5q4)

- Wide Locally Recoverable Codes (LRCs) are used in large scale storage clusters to protect against disk failure.
   - Commonly used Erasure codes, such as Reeder Solomon code or MDS code, aim to reduce the total number of parity chunks and improve data-to-parity ratio for lower storage overhead.
   - LRCs are designed to handle single chunk failures efficiently.
   - Wide LRCs have been proposed to further increase fault tolerance by using many local groups compared to conventional LRCs, thus reducing the reconstruction cost when a single chunk fails.
   - Key factors affecting wide LRC reliability include distance code, coefficient (which depends on Erasure code generator matrix choice), and layout design.
   - Uniform Kaushi LRCs are designed with a focus on simplicity and robustness, using Cauchy coefficients to achieve close-to-maximally recoverable codes while maintaining good layout design.
   - Practical considerations for deploying wide LRCs include measuring their performance in terms of robustness against random failures, average repair cost for one or two erasures, and mean time data loss (MTTDL).
   - The speaker presents a case study where Uniform Kaushi LRCs were deployed at Google, showing that they improved availability by reducing unavailability recorded events compared to the previous deployment.


## FAST '23 - ParaRC: Embracing Sub-Packetization for Repair Parallelization in MSR-Coded Storage

URL: [https://www.youtube.com/watch?v=kd6JTmJY0Xg](https://www.youtube.com/watch?v=kd6JTmJY0Xg)

- Introduced Eurasia Coding and its applications
- Discussed the concept of repair bandwidth, maximum repair load, and tradeoffs in designing erasure codes
- Presented MSR (Minimum Storage Regenerating) code, a new erasure code construction that minimizes repair bandwidth while satisfying MDS property like RS code
- Explained packetization feature and its role in reducing repair overhead
- Demonstrated an example of applying parallelism to the repair process using the MSR code
- Introduced the concept of parallel RC (Parallel Repair Framework) and how it can be applied to balance load across nodes during repairs
- Presented a heuristic for finding an optimal tradeoff between repair bandwidth and maximum repair load, called MLP (Minimum Load Point)
- Discussed the challenges in implementing MLP and proposed a solution using a colored PEC deck approach
- Described a prototype implementation of power RC on Hadoop HDFS and how it can be used to evaluate performance on Alibaba Cloud
- Concluded by emphasizing the importance of parallelism, efficient design, and small block sizes in designing erasure codes for large NK systems.


## FAST '23 - InftyDedup: Scalable and Cost-Effective Cloud Tiering with Deduplication

URL: [https://www.youtube.com/watch?v=E72C3hkYW28](https://www.youtube.com/watch?v=E72C3hkYW28)

- Introduced Infinity, a scalable and cost-effective cloud tiering application
- Aimed to exploit the cloud's capabilities and provide limitless scalability and significant cost reduction
- Developed using NEC Hydra Store as a reference
- Cloud tier encrypted application allows for data duplication in the cloud with efficient batch processing, deduplication, and parallelized work
- Utilizes multiple classes of cloud storage to decrease total costs while storing data
- Batch processing algorithm efficiently processes petabyte-scale datasets at an affordable cost
- Introduced a technique that reduces costs by mixing hot and cold storage classes based on restore frequency policies
- Demonstrated the effectiveness of the approach through experiments, achieving linear scalability and efficient garbage collection algorithms


## FAST '23 - Perseus: A Fail-Slow Detection Framework for Cloud Storage Systems

URL: [https://www.youtube.com/watch?v=DcDnrZY11Yw](https://www.youtube.com/watch?v=DcDnrZY11Yw)

- Raymond Im discusses his work on detecting field slow failures in large-scale cloud storage systems.
- He mentions a joint research project with Shanghai Jiao Tong University and Sharda University.
- Field slow failures are often overlooked but can cause severe performance degradation and downtime.
- The first law of component failure states that even if one component is still functioning, it may have lower expected performance.
- Perseus, an intrusive fine-grained general detection framework, was introduced to detect field slow failures.
- A dataset of 248,000 drives was analyzed for detected field store failures.
- The dataset covers different drive specifications serving nine cloud services and contains device-level performance logs like latency and throughput.
- A time series-based raw data set was also built and released as a test benchmark for fail slow detection tests.
- Previous attempts at threshold filtering were not successful due to the difficulty of setting accurate thresholds empirically.
- Peer evaluation was introduced, where drive node performance is compared with similar peers using sliding windows and latency versus throughput distributions.
- A light regression model scoring mechanism was used to detect slow failures throughout part of the process.
- The design of Perseus utilizes classic machine learning techniques and a general scoring mechanism for accurate finding of fails slow detection problems.
- A test benchmark was released to evaluate the performance of Perseus and other similar systems.
- 315 field slow drive tests were conducted, revealing that most root causes were software-induced resource contention issues.


## FAST '23 - ADOC: Automatically Harmonizing Dataflow Between Components in Log-Structured Key-Value

URL: [https://www.youtube.com/watch?v=g-WbFJzQfcg](https://www.youtube.com/watch?v=g-WbFJzQfcg)

- Introduced City University Hong Kong and the topic of their paper on data flow harmonization.
- Described the background problem: TV Redstone, a popular system used in many scenarios, has performance issues due to its key value store (KVS) structure.
- Presented the KV system architecture consisting of three major components: memory component, buffer, and commit log.
- Explained that ensuring consistency is difficult due to the nature of the commit log operation.
- Introduced RocksDB as their starting platform for the paper since it's a popular representative of an awesome KVS.
- Described the three main components of RocksDB: memory table (MT), write-ahead log (WAL), and store table (ST).
- Detailed the two major operations in the system: background compaction and foreground flush.
- Introduced the concept of Red Store, a common problem observed where performance drops due to resource exhaustion.
- Presented their experimental setup to observe the right store problem and its dependency on different storage devices.
- Described the three categories of red store based on observation: resource exhaustion, level zero/one compaction execution, and deep level compaction.
- Introduced the concept of data overflow, a new way to explain the formation of Red Store by considering overall harmony between components.
- Proposed a new tuning framework called ADOC (Auto Distributed Optimized Compaction) to remove or alleviate red store problems.
- Discussed the limitations of their proposed solution and future work.


## FAST '23 - FUSEE: A Fully Memory-Disaggregated Key-Value Store

URL: [https://www.youtube.com/watch?v=XjkJK9pYN2c](https://www.youtube.com/watch?v=XjkJK9pYN2c)

- Introduced the new paper: "Fuzzy: A Fully Memory Disaggregated KV Store"
- Joint work between Chinese University Hong Kong, Huawei Cloud, Photon University, and Song Asan University.
- The paper tackles issues in existing memory KV stores like Redis and Memcached, which are fundamental building blocks for many cloud services.
- Proposed a disaggregated memory architecture to address the limitations of monolithic server CPU/memory resource coupling and elasticity issues.
- Discussed the challenges of achieving fully memory disaggregated KV stores: client-centric index replication, remote memory allocation, and metadata corruption.
- Proposed Fuzzy as a solution to these challenges.
- Demonstrated the effectiveness of Fuzzy through experiments using YCSB hybrid benchmarks, which showed that it achieves 49 times higher throughput compared to existing approaches.


## FAST '23 - ROLEX: A Scalable RDMA-oriented Learned Key-Value Store for Disaggregated Memory Systems

URL: [https://www.youtube.com/watch?v=pQLKBicYIpI](https://www.youtube.com/watch?v=pQLKBicYIpI)

- Introduced a new, scalable RDMA-oriented Key-Value Store system
- Disaggregated memory system into separate components: leaf constructs and learning indexes
- Used a 3D model to improve data retrieval performance
- Emphasized on reducing network overhead and improving read/write performance
- Implemented an asynchronous, one-set RDMA operation for indexing
- Utilized a relaxed training code, available on GitHub
- Proposed a solution to the problem of inconsistent states in compute nodes
- Demonstrated how to handle large amounts of data and insert/delete operations efficiently
- Discussed the challenges faced by existing systems and proposed solutions for them
- Showcased an example of how the new system can achieve significant improvements over previous methods (13-28 times faster)


## FAST '23 - GL-Cache: Group-level learning for efficient and high-performance caching

URL: [https://www.youtube.com/watch?v=8VMJjdYqX84](https://www.youtube.com/watch?v=8VMJjdYqX84)

- Introduced three types of noncash learning: simple expert, learning distribution, and object level learning.
- Discussed group-level learning, which is a new approach to cache management.
- Compared different caching algorithms in terms of efficiency and throughput.
- Presented a diagram showing the potential efficiency and act throughput of various algorithms.
- Introduced the concept of group object and how it can be used for better cache management.
- Demonstrated how to use feature models and grid boosting tree regression in caching systems.
- Showcased evaluation results using Cloud, Physic Trace, MSR Tree, Wikipedia trace, and other datasets.
- Discussed the importance of choosing the right parameters for optimal cache performance.
- Compared the throughput of different algorithms, highlighting that RB (Relaxed Bloom) has lower support but can achieve higher throughput with group level learning.


## FAST '23 - SHADE: Enable Fundamental Cacheability for Distributed Deep Learning Training

URL: [https://www.youtube.com/watch?v=NwIYM3O-qvA](https://www.youtube.com/watch?v=NwIYM3O-qvA)

- Deep learning is everywhere and its market is expected to grow 19% annually in the foreseeable future.
- Caching can be a solution for speeding up data-intensive deep learning applications, which take around 85-90% of total training time.
- The Shade system addresses the challenge of caching by using four techniques: loss decomposition, rank-based importance course, and patch sampling policy for app cache.
- The Shade architecture consists of two layers: a control layer and a data layer. It uses an analysis framework to facilitate experimentation.
- A distributed training pipeline is incorporated in the system, enabling it to train models on large datasets with multiple GPUs.
- Evaluation results show that using the Shade caching system can improve accuracy, reduce time, increase throughput, and increase heat ratio for deep learning applications.


## FAST '23 - Intelligent Resource Scheduling for Co-located Latency-critical Services: A Multi-Model

URL: [https://www.youtube.com/watch?v=XfFCTuNOHYg](https://www.youtube.com/watch?v=XfFCTuNOHYg)

- Introducing OSMOSML: An intelligent resource scheduling approach for colocating latency-critical services.
- Addresses challenges in scheduling colocated services due to diverse behavior across storage hierarchy, enlarged scheduling exploration space, and the presence of interactive resources like CPU, LLC, memory bandwidth, and I/O.
- OSMOSML uses a multimodel Collaborative Learning based resource scheduling approach that leverages machine learning to achieve higher load take and meet QoS targets compared to prior work.
- Cloud applications are moving from monolithic architecture to loosely coupled designs, which include many LC services with strict QoS requirements. This often results in multiple services being scheduled on the same server simultaneously, increasing server utilization and cost efficiency.
- OSMOSML addresses these challenges by designing a machine learning based resource scheduler that can handle diverse behavior across storage hierarchy, enlarged scheduling exploration space, and the presence of interactive resources.
- The resource scheduler uses a normal machine learning approach to predict optimal allocation areas (OAAs) and avoid resource cliffs, which can lead to significant performance slowdowns if not handled properly.
- OSMOSML's design includes three main components: Model A for predicting Cliff/OE bandwidth; Model B for balancing QoS resource allocation among colocated LC services; and Model C for handling change using reinforcement learning.
- The system also incorporates two Shadow models to handle different scenarios effectively.
- OSMOSML uses a pipeline approach that combines these models in an efficient manner to provide optimal scheduling solutions for colocated LC services.
- In terms of performance, OSMOSML has been shown to converge faster than baseline approaches and can handle dynamically changing loads more effectively.
- The project is open source and encourages community contributions to continue enhancing its capabilities and adding new case studies.


## FAST '23 - CJFS: Concurrent Journaling for Better Scalability

URL: [https://www.youtube.com/watch?v=iSBmgErixXg](https://www.youtube.com/watch?v=iSBmgErixXg)

- Background:
  - Hardware evolution (CPUs, SSDs)
  - Software stack: Cloud Server with many core CPUs and containerized services
  
- Problem:
  - Bottlenecks in software stack due to serial commit process
  
- Solution:
  - CJFs (Concurrent Journal File System)
    + Multiple transaction committed concurrently
    + Four techniques: journaling, multiple potential paging opportunities, policy, compound flush
    
- Evaluation:
  - Improved throughput by 16x in Shield benchmark, 13x in Palm split, and 12x in D benchmark compared to original ESD4
  
- Conclusion:
  - CJFs improves system performance by utilizing parallelism in storage devices.


## FAST '23 - Unsafe at Any Copy: Name Collisions from Mixing Case Sensitivities

URL: [https://www.youtube.com/watch?v=E2zznSP2nl4](https://www.youtube.com/watch?v=E2zznSP2nl4)

- Presentation on case insensitivity in file systems
    - Background and existing security work
        + Name-based attack, name collision detection
    - File system mapping and security issues
        + Resource confusion, data loss, corruption, incorrect file overrides, confidential information leaks
        + Classic squatting attack, link traversal attack
        + Different file systems handle case sensitivity differently
    - Case diversity in modern file systems
        + Linux ext4 folder marking case-sensitive/insensitive folders
    - Real-world implications and examples
        + Git CBE 2021 collision, 2014 Mercurial issue
    - Contribution: coined term "name collision"
        + Place hierarchy name collision in the context of file systems
    - Detection strategy and evaluation
        + Developed a test suite for detecting unsafe responses and novel exploits
    - Defense mechanisms
        + Program conveying case sensitivity to underlying file system
        + Canonicalize path names, normalize path folding, return canonicalized path name
- Q&A session with audience encouraged.


## FAST '23 - ConfD: Analyzing Configuration Dependencies of File Systems for Fun and Profit

URL: [https://www.youtube.com/watch?v=GygCZSnT-_8](https://www.youtube.com/watch?v=GygCZSnT-_8)

### Presentation Summary:
- Researchers present work on analyzing configuration dependency in file systems, focusing on the Ext4 and XFS file systems.
- The talk highlights the importance of understanding configuration dependencies to prevent issues like data corruption or system crashes.
- They introduce a tool called Quantity that can automatically extract multilevel dependencies from file systems and generate valid configuration states based on these dependencies.
- The researchers demonstrate how their tool can help identify bugs in real-world scenarios, such as when the E4 defrag utility causes file corruption due to incorrect configuration settings.
- They also discuss future work, including extending Quantity's support to other types of systems and applications beyond just file systems.


## FAST '23 - HadaFS: A File System Bridging the Local and Shared Burst Buffer for Exascale

URL: [https://www.youtube.com/watch?v=l-pwBIewqno](https://www.youtube.com/watch?v=l-pwBIewqno)

- Speaker introduces birthday system for file systems (FS)
- Focus on maximizing input/output (I/O) performance and scalability
- Discusses two types of photographer systems deployed in the Philippines
- Introduces a global file system (GFS) with local and remote storage nodes
- Talks about balancing read/write operations between different FS nodes
- Explains how to manage data migration for large scale applications
- Mentions the importance of user control over data storage
- Discusses the use of "localized trash architecture" for efficient data storage
- Introduces a new method for bypassing kernel restrictions in FS
- Talks about different types of databases used to store metadata and file information
- Explains how to measure file system performance using various metrics
- Discusses the importance of synchronization strategies for different applications
- Provides examples of data migration flows and their impact on application performance
- Talks about optimizing FS performance by reducing latency and improving bandwidth
- Introduces a new method for comparing FS performance using different configurations
- Explains how to use JFS (Japanese File System) in different models and its impact on performance
- Discusses the importance of kernel cache striping technology for application parallelism
- Talks about the challenges of data immigration and ways to optimize it
- Introduces a new method for tuning FS performance by remapping client/server connections
- Concludes by introducing a personal power file system called "office" that bridges support for local and remote storage nodes.


## FAST '23 - Fisc: A Large-scale Cloud-native-oriented File System

URL: [https://www.youtube.com/watch?v=btDflcOPZ00](https://www.youtube.com/watch?v=btDflcOPZ00)

- Alibaba Cloud Engineer discusses Fisk, a large scale cloud native oriented file system
- Purpose: Optimize backend storage for cloud Big Data applications
- Bottlenecks in current setup:
    - Resource multiplexing among many file clients
    - Inefficient network load balancing
    - Load imbalance between backend storage clusters
    - High cost of using traditional load balancers
- Fisk's design goals:
    1. Reduce resource multiplexing among many file clients
    2. Build a storage-aware kit for better performance and fault tolerance
- Fisk architecture:
    - Two-layer resource aggregation architecture
        - Lightweight phase client load function
        - Fiscal agent (fixed process)
- Key features of Fisk:
    - VRPC (Virtual RPC): A simplified, secure RPC framework that offloads uploaded resources and aggregates traffic
    - Resource Smart Profile: Allows different container computation servers to aggregate local Fisk agents and distribute resources among them
- Benefits of Fisk:
    - Reduced CPU cost by 60%
    - Lower memory footprint
    - Improved network bandwidth usage
    - Better fault tolerance and load balancing
- Evaluation metrics for Fisk:
    - FIO micro benchmark test
    - Production sample average latency


## FAST '23 - TENET: Memory Safe and Fault Tolerant Persistent Transactional Memory

URL: [https://www.youtube.com/watch?v=o800CoToxD0](https://www.youtube.com/watch?v=o800CoToxD0)

- Overview of NVM and its challenges
  - Nonvolatile memory (NVM) is exposed directly to user space, making it vulnerable to data corruption from software bugs or hardware errors.
  - Two main types of errors: medium risk error (hardware side) and application bug (software side).
- Tenet's solution for NVM data protection
  - Develop a programming framework that helps developers build memory safe and fault tolerant NVM applications.
  - The framework includes:
    - A library of functions called PMDK Transaction Library, which supports persistent transaction operations.
    - A design principle called "Tenet" that focuses on preventing application code from causing spatial or temporal safety violations in the NVM data structure.
- Key components of Tenet
  - Spatial safety: Prevent bugs from accessing memory regions beyond allocated ranges.
  - Temporal safety: Avoid dangling pointers and other issues that can lead to unintended memory access.
  - Fault tolerance: Protect NVM data against uncorrectable medium errors, which can cause permanent data loss.
- Design principles for ensuring spatial and temporal safety
  - Enforce read-only permissions on certain NVM regions to prevent accidental writes or reads of corrupted data.
  - Use a Canary bit as an additional check for memory safety violations, such as when writing to the NVM.
  - Implement a pointer tag system that allows developers to validate whether a given memory address is valid or not.
- Fault tolerance techniques
  - Replicate NVM data on a local SSD to provide a backup copy in case of uncorrectable medium errors.
  - Use consistent lossless recovery techniques to ensure that any lost data can be restored without compromising the integrity of the system.
- Evaluation of Tenet's performance and scalability
  - Compared against existing PDMK Transaction Library implementations, Tenet showed minimal overhead and maintained high levels of scalability.
  - The addition of fault tolerance features slightly impacted performance but still remained within acceptable limits.


## FAST '23 - MadFS: Per-File Virtualization for Userspace Persistent Memory Filesystems

URL: [https://www.youtube.com/watch?v=J60sTA3cwJo](https://www.youtube.com/watch?v=J60sTA3cwJo)

- Sean Work presented Med FS, a user space persistent memory file system.
- Metadata embedding: Efficient metadata management in user space without kernel involvement.
- Profile Virtualization: User-space virtualization layer that manages file functionality including metadata management and crash consistency.
- Concurrency Control: Optimistic concurrency control for metadata updates.
- Med FS has better overall performance than X4 Dax, EX4 Deck, and Nova in micro Benchmarks and real-world application tests.


## FAST '23 - On Stacking a Persistent Memory File System on Legacy File Systems

URL: [https://www.youtube.com/watch?v=MHcJ114hVk8](https://www.youtube.com/watch?v=MHcJ114hVk8)

- Introducing SPF (SPF Stack Persistent Memory File System)
  - Lightweight and efficient PMEM file system
  - Offers PM Oblivious File System (PMOFS)
    + Provides persistent right cache
    + Uses extent hashing algorithm for metadata management
- Designing SPF
  - Focus on small synchronous right lightweight
  - Efficiently manages metadata hash table and extent hash table
  - Utilizes sync point profiling mechanism to detect synchronous IO
  - Balances pmem usage by predicting block placement decisions
- Implementing SPF
  - Improves performance of legacy products like FS99
    + Detects smaller synchronous right using Sync Point Profiles
    + Efficiently manages metadata and extent hash tables
  - Utilizes rapid caching mechanism for small synchronous right
  - Focuses on synchronization and IO patterns
- Evaluating SPF
  - Compares performance with XFS, F2FS, and other file systems
  - Demonstrates higher throughput and lower latency in certain scenarios
    + Stacking SPF with block devices and file systems improves overall performance
- Future Work
  - Continue optimizing SPF for specific workloads and use cases
    + Further reduce metadata size and improve hash table efficiency
    + Develop new sync point profiling techniques to better manage synchronous IO


## FAST '23 - Citron: Distributed Range Lock Management with One-sided RDMA

URL: [https://www.youtube.com/watch?v=_Aegd52O_Hg](https://www.youtube.com/watch?v=_Aegd52O_Hg)

- Introduced work on distributed range lock management using onesided RDMA
- Aimed at improving performance and scalability in storage systems like file systems, databases etc.
- Proposed a system that bypasses serverside CPUs to avoid bottlenecks
- Presented a segment tree based data structure for efficient range dog management
- Demonstrated the effectiveness of their approach through experiments on a cluster of four machines (one server and three clients)
- Compared with existing solutions, showed that their system achieved better performance and scalability
- Introduced a novel RDMA extended atomics mechanism to perform synchronization efficiently


## FAST '23 - Patronus: High-Performance and Protective Remote Memory

URL: [https://www.youtube.com/watch?v=zO6CeFCik58](https://www.youtube.com/watch?v=zO6CeFCik58)

    - Ping Xinhua from Xinhua University introduces work on Patronus, a high-performance protective remote memory system.
    - The current data center issue is low memory utilization.
    - Remote Memory Architecture (RMA) separates CPU and memory into two network-attached components: Compute Node and Memory Node.
    - RDMA (Remote Direct Memory Access) allows direct read/write operations on remote memory without involving the CPU.
    - Patronus provides flexible resource allocation, which improves memory utilization.
    - Previous efforts to make remote memory practical include efficient remote index designs, easy-to-use programming models, and deploying popular applications.
    - Despite these improvements, there are still challenges in implementing a practical remote system.
    - The talk focuses on the protection of remote memory, especially in workloads with shared access patterns.
    - Previous works like RHT (Remote Hash Table) and P+3 did not provide robust protection mechanisms.
    - Patronus introduces an efficient permission management system that allows fast permission checks and rejects illegal operations.
    - The Petronas system includes a three-step client workflow: start, data access, and end permissions.
    - The talk presents experimental results showing the effectiveness of the Patronus system in terms of performance and robustness.
    - Three key ideas were introduced to improve common path performance, exception path performance, and QPR (Queue Pair) resource provisioning.
    - Memory Window Operation Reduction reduces memory node overhead by optimizing protection semantics.
    - Client Collaborative List allows clients to handle failures and manage lists efficiently.
    - Q-Pair Provisioning conceals interruptions during QP (Queue Pair) failure recovery, ensuring system performance remains unaffected.
    - The experimental results show that Patronus offers 52 times better throughput compared to competitors while maintaining low overhead.


## FAST '23 - More Than Capacity: Performance-oriented Evolution of Pangu in Alibaba

URL: [https://www.youtube.com/watch?v=Twss7x3Ib2Q](https://www.youtube.com/watch?v=Twss7x3Ib2Q)

- Panku, a unified storage system by Alibaba Cloud, is used widely.
- It's designed to handle various applications like databases, online search, Big Data analysis, and message queues.
- The first generation of Panku was built seven years ago with the focus on scalability, reliability, and availability.
- A new storage medium called Mme SSD has significantly impacted the design of Panku. 
- The second generation of Panku addresses the challenge of performance design by introducing a new storage operating system called USS OS. It simplifies high-performance system development by bypassing the kernel and reducing latency.
- Panku adopts distributed master architecture to enhance availability and increase metadata processor ability, reducing latency.
- Cache profiling is used for batch optimization, which helps reduce latency at the client side.
- The backend network hardware and software are co-designed to remove limitations and improve IO efficiency.
- The P3910 latency is controlled around millisecond level in the second generation of Panku.
- The EBS search service has an average read latency controlled at 200 microseconds, while the write latency is controlled at 100 microseconds.
- The User Space Storage design and tele latency control mechanism are used to optimize full stack latency in Panku.
- Network traffic flow analysis helps reduce network traffic by filtering, compressing, and using image coding compression techniques.
- The RDCA (Remote Direct CASH Access) method is proposed to bypass the DDR memory and improve memory bandwidth efficiency.
- The CPU hardware is fully utilized with many core architecture offloading computational tasks.
- An FPGA-based compression card is used to offload CRC tasks, improving overall throughput.


## FAST '23 - λ-IO: A Unified IO Stack for Computational Storage

URL: [https://www.youtube.com/watch?v=xYENKqthG40](https://www.youtube.com/watch?v=xYENKqthG40)

- Lambda IO: Unified Auto stack for computational storage
- Purpose: To offload user-defined computational logic and read/write data, while improving performance over vanilla Linux IO.
- Challenges in conventional systems: Accessing large amounts of data can be slow and costly.
- Computational Storage: A method that processes data within the storage device itself, reducing the need for data transfer between host devices.
- Lambda IO Design:
    - Easy Studios APIs: Hide underlying details to make it easy to use.
    - Closed Platform & Lambda Runtime: Provides a consistent environment for executing computational logic.
    - Dynamic Request Dispatching: Allows efficient scheduling of I/O requests.
- Advantages over vanilla IO stack:
    - Straightforward porting with minimal overhead.
    - Closed platform and runtime offer better control and consistency.
    - Dynamic request dispatching improves efficiency and performance.
- Lambda IO's Dynamic Checking: Ensures access within memory boundaries, addressing issues related to EBPF (eXtended Berkeley Packet Filter).
- Evaluation Results:
    - Synthetic applications: Lambda IO outperforms vanilla Linux IO in terms of speed and efficiency.
    - Real-world application (SpicyCycle): Lambda IO also achieves better performance than vanilla Linux IO.
- Conclusion: Lambda IO is a unified Auto stack that manages computer computation storage resources across the whole standard device, offloading user-defined computational logic and improving performance significantly over vanilla Linux IO.


## FAST '23 - Revitalizing the Forgotten On-Chip DMA to Expedite Data Movement in NVM-based Storage

URL: [https://www.youtube.com/watch?v=fIUoc8bKZ5k](https://www.youtube.com/watch?v=fIUoc8bKZ5k)

## Summary of conference talk on revitalizing Forgotten Onchip DMA using NVM-based Storage System

- Overview: The speaker introduces the concept of Fast Move, a general data movement engine that exploits on-chip DMA to speed up data transfer in NVMe-based storage systems. This engine incorporates three key techniques: optimized DMA, cooperative bulk read/write, and lightweight scheduler.
   - Optimized DMA: This technique involves batching DRM page pinning, submission, and metadata buffer preallocation to improve efficiency.
   - Cooperative Bulk Read/Write: This method divides data into chunks and has the CPU send a chunk while the DMA sends the rest, effectively pausing the DMA until the CPU finishes sending its portion of the data.
   - Lightweight Scheduler: This scheduler coordinates resources and decides whether to split requests or have the CPU and DMA cooperate.
- Evaluation: The speaker presents experimental results showing significant improvements in latency and throughput when using Fast Move compared to traditional CPU-based data transfer methods. They also demonstrate how adding specific optimizations can lead to even greater performance gains.
- Conclusion: The speaker concludes by emphasizing that their comprehensive analysis of Intel's OAT platform demonstrates the benefits of exploiting on-chip DMA through the use of Fast Move, without requiring changes to existing application source code.


## FAST '23 - NVMeVirt: A Versatile Software-defined Virtual NVMe Device

URL: [https://www.youtube.com/watch?v=cBonhqDooPE](https://www.youtube.com/watch?v=cBonhqDooPE)

- Presenter introduces himself and thanks collaboration partners.
- Short story about the development of an idea for a new key-value store (KVSSD).
- The presenter discusses the challenges faced in evaluating various devices, including the difficulty of accessing and modifying them.
- They mention using an emulator to test software, but also highlight the limitations associated with it.
- The presenter talks about the concept of a virtual MVME device and how it can support RDMA (Remote Direct Memory Access).
- He explains that this approach allows for better performance and lower latency than traditional methods.
- However, he points out that there are still some downsides to using virtualization techniques, such as increased overhead.
- The presenter shares the challenges faced during development, including difficulties in detecting updates and handling interruptions.
- He then discusses the importance of incorporating advanced garbage collection models into the design of the system.
- The speaker introduces a simple model for processing data chunks and moving data between different components.
- They compare performance results from using an emulator versus actual devices, showing that there is a significant difference in performance when using emulators.
- The presenter shares some case studies where they have used their developed system to evaluate the performance of various devices and applications.
- He emphasizes the importance of replicating real-world conditions as closely as possible during testing.
- Finally, the speaker highlights the benefits of using their MVME-based approach for strategic computations and provides some examples of how it can improve overall system performance.


## FAST '23 - SMRSTORE: A Storage Engine for Cloud Object Storage on HM-SMR Drives

URL: [https://www.youtube.com/watch?v=b_iW94OQmbY](https://www.youtube.com/watch?v=b_iW94OQmbY)

- Introduced new starter engine ASMR store
- Joint work with OSS family team
- Replacing S3 compatible service with a new version that supports higher density drives and better cost efficiency
- Asthma drive divides address into fixed size zones, which improves performance
- HMS hmsm drive without compromising performance
- Big picture of OSS architecture: frontend layer processes requests, forwarding them to the service layer for processing
- Pango file system: persistent layer packs Master Manager servers responsible for data persistence
- Drive trunk corresponds to a file in F4 format
- Observation 1: OSS medial stream metadatari stream listed data chunk really small
- Observation 2: f2fs normally opens one zone at a time, putting chunks in different streams
- Techno choice: build new user space storage engine directly, hmsm drive
- HMSM drive codesigns OSS back to achieve high performance
- Design principles for OSS workloads are based on traditional local file systems and exist within the customer's drives by Zoom block interface
- Data layout includes data indexing and memory management
- Master follows log structure design, with records being the basic unit of metadata and user data
- Layout of SMR drive: divide address into three partitions; first zone is a superzone for information performance timestamps, version numbers, etc.
- Three types of records are used to store serialized checkpoint journal chunk data
- Payload data records have four kilobyte headers with invariable payload sizes
- Read reduction and reidentification avoidance through reading small parts of the payload
- SMR store organizes memory structures effectively by optimizing placement and reducing overhead
- Scratch collection is used to manage empty zones efficiently
- Data indexing provides straightforward mapping between logical and physical locations
- Chunk data design includes three workload-aware placement strategies: reduce overhead, collect first, separate chunk different zone stream type adapt multichunk size limit
- The effect of interleaved zones in SMR store is demonstrated through the example of replacing a trunk
- Compared to CMR drives, SMS talks about providing comparable performance and even up to 30% higher throughput for larger sizes
- Micro Benchmark results show that ASMR stock performed well with small outsize, while SMR store achieved consistent register reports at 216 times faster speeds than F2FS
- Comparing the performance of enabling/disabling the SMR drive strategy, it's found that disabling the SMR drive reduces similar performance while optimized displacement CDFS Zoom utilization improves it significantly
- Building a new user space storage engine for ASMR store designs three workload-aware placement strategies to charge according to characteristics
- OSS closing SMS store performs much better than deploying an F2FS system with SMR drives, leading to a decrease in total costs by around 15%.


## FAST '23 - Multi-view Feature-based SSD Failure Prediction: What, When, and Why

URL: [https://www.youtube.com/watch?v=Daa5E083Sps](https://www.youtube.com/watch?v=Daa5E083Sps)

- SSD Value Prediction Scheme:
    - Based on field-determined data.
    - Long-term monitoring data is useful for failure prediction.
    - Multiview, multitask Random Forest (MBTRF) scheme proposed.
    - Finds long-term data monitoring data useful in value prediction.
    - Combines short-term and long-term monitoring data to capture failure.
    - Proposes a new approach for analyzing SSD monitoring data.
    - Designs histogram feature pocket statistic to represent long-term data distribution.
    - Finds that ssds server workload is usually similar, thus trends can be compared.
    - Introduces three features: coefficient variation, artist production degree, and cortex represents stiffness trend slope.
    - Evolves 3D feature to reflect trend differences.
    - Desires a tight-ended lifespan solution that deals with failure operator provided machine learning model.
    - Three main parts of the overall architecture: offline training, online prediction, and real-time monitoring.
    - Combines multiple decision processes to improve prediction accuracy.
    - Uses key decisions to reveal failure causes and verifies them.
    - Evaluates the proposed language art existing scheme using precision, recall, F1 score, and AUC.
    - Compares single task model with multi-task model for better prediction accuracy.
    - Extracts major decision process based on Reverse Medium Error.
    - Main failure codes are extracted to improve failure prediction.
    - The MBTRF model improves the customer storage library serviceability.


## FAST '23 - Fast Application Launch on Personal Computing/Communication Devices

URL: [https://www.youtube.com/watch?v=zGnn7IkIdiE](https://www.youtube.com/watch?v=zGnn7IkIdiE)

- Tony Lee from Texas A&M University presented a conference talk on improving application launch times using SSDs.
- The key problem is that performance flash storage still lags behind expectations, especially in comparison to cheaper QLC SSDs.
- He proposed a new technique called "parafetch" which aims to make better use of CPU cores and internal parallelism within SSDs.
- Parafetch consists of two phases: learning phase and prefetch phase.
- The learning phase involves monitoring disk access patterns and identifying launch-related blocks.
- The prefetch phase involves storing information about these launch-related blocks to accelerate loading subsequent launches of the application.
- He also discussed various challenges in designing a prefetcher, such as accurately collecting launch-related disk blocks and optimizing the order in which they are prefetched.
- Parafetch uses metadata shifting and range merging techniques to reduce prefetching times while increasing metadata shift sizes.
- The talk concluded with an evaluation of the parafetch technique on various platforms, showing significant improvements in application launch times, especially for warm starts.


## FAST '23 - Integrated Host-SSD Mapping Table Management for Improving User Experience of Smartphones

URL: [https://www.youtube.com/watch?v=WUh3AaSdKcQ](https://www.youtube.com/watch?v=WUh3AaSdKcQ)

- Presentation by Yuna Keem, Seoul National University
- Focus on improving user experience in smartphones through integrated host SSD mapping table management
- Long storage latency is a key contributor to poor user experience
- Addressing L2P cache misses and their impact on user perceived latency
- Introduced HPV (Host Processor Virtualization) as a solution for better UX quality
- Two shortcomings in existing HPV management scheme: 1. Critical Miss Penalty still exists, and 2. It might reduce working memory space for user apps
- Proposed HPP Valve to address these issues using two techniques: Foreground App Centric HPV Caching and Dynamic HPB Size Adjustment
- Evaluation of proposed solutions using Snapdragon Triple Eight Mobile Hardware Development Kit showed significant improvements in app launching time and reduced number of important apps killed by LMKD (Low Memory Killer Daemon)



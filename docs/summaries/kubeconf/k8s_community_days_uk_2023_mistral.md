## Effortless Mutual Authentication with Cilium | Liz Rice

URL: [https://www.youtube.com/watch?v=0t_lhV0fvQ8](https://www.youtube.com/watch?v=0t_lhV0fvQ8)

 * Liz Rice discussing "Effortless Mutual Authentication with Cilium"
* Combines EBPF and Psyllium networking plugin for Kubernetes
* EBPF allows customizing kernel behavior, including network stack
* Mutual authentication often achieved using Mutual TLS
* Celium provides network security features based on EBPF
* Demonstrates controlling traffic flow using labels and policies in Celium
* Transparent encryption in Celium encrypts traffic between nodes
* Next Generation Mutual Authentication with Celium uses endpoint handshake protocol for identity verification
* Spiffy generates certificates for endpoints, allowing mutual authentication without encryption
* Demonstration shows dropping packets that don't match policy rules and authentication required packets being allowed.


## Mastering Enterprise Complexity with Service Mesh: A Case Study & Critical Evaluation | Shweta Vohra

URL: [https://www.youtube.com/watch?v=1qr57Oh8EQg](https://www.youtube.com/watch?v=1qr57Oh8EQg)

 * Shweta Vohra, software architect with two decades of experience, shares her learning from designing Enterprise Solutions using Service Mesh
* Agenda: Service Mesh introduction, Enterprise case study, Building a decision-making framework
* Service Mesh definition: Invisible infrastructure layer that makes communication efficient between microservices, decouples communication concern from application business logic
* Major features of Service Mesh: Connectivity control, Security, Observability, Resiliency, Extensibility
* Connectivity control: Enables communication between services, service discovery, load balancing, retries, traffic control
* Security: Authentication, authorization, encryption policy enforcement
* Observability: Distributed tracing, telemetry, visibility into system health
* Resiliency: Fault injection, dark releases, circuit breakers
* Extensibility: Interoperability with different technologies and platforms
* Enterprise case study: Telecom industry's hybrid cloud environment, need for modernization, service mesh identified to enable communication between services across infrastructure
* Service Mesh challenges: Complexity, interoperability, inefficient service discovery, connectivity challenges, limited observability, security concerns
* Service Mesh benefits: Global control plane, easier policy regulation, traffic management, improved observability, simplified architecture.


## Lightning talk 1

URL: [https://www.youtube.com/watch?v=2IdJiATvAB4](https://www.youtube.com/watch?v=2IdJiATvAB4)

 * Observability can be expensive and difficult
* Tip for managing observability: create use cases, define use case without unnecessary data, ensure psychological safety, and adopt a use case-driven approach
* Store logs in associated storage based on performance requirements
* Use tail sampling to save money by storing only necessary data
* Adhere to the YAGNI (You Aren't Gonna Need It) principle
* Store metrics efficiently instead of full documents or logs
* Understand your use case and data thoroughly before implementing solutions
* Archive old data to save costs and improve performance
* Use open telemetry and configuration-driven pipelines for cost optimization.


## 11 tricks to improve your productivity and reduce your frustration with Kubernetes

URL: [https://www.youtube.com/watch?v=5eVhR7XtA-c](https://www.youtube.com/watch?v=5eVhR7XtA-c)

 * Tiffany Jigan and Jerome Petazzoni, developers at VMware, discussing 11 tricks to improve productivity and reduce frustration with Kubernetes
* Running a local cluster with multiple nodes for testing and development (Docker Desktop, Kind, Minikube)
* Using Cude CTX and NS to easily switch between contexts and namespaces
* Waiting for specific conditions before creating resources or deployments
* Using Json paths to get specific field values instead of using generic selectors
* Setting timeouts and monitoring deployment progress with tools like kubectl and fzf
* Using K9s for visual representation of cluster status
* Patching configurations without re-creating resources
* Labeling columns to see important information at a glance
* Changing service account assignments for specific deployments
* Setting resource requests with one-liners
* Watching events with kubectl and JQ
* Transforming JSON data using tools like nixer
* Generating images with Fly instead of writing Dockerfiles and pushing to a registry
* Support for multiple architectures in Nixer is not yet fully developed.

Some of these tricks include using local clusters for testing, using Cude CTX and NS to easily switch contexts and namespaces, waiting for specific conditions before creating resources or deployments, using Json paths to get specific field values, setting timeouts and monitoring deployment progress with tools like kubectl and fzf, patching configurations without re-creating resources, labeling columns to see important information at a glance, changing service account assignments for specific deployments, setting resource requests with one-liners, watching events with kubectl and JQ, and transforming JSON data using tools like nixer. Other tricks include generating images with Fly instead of writing Dockerfiles and pushing to a registry. However, it should be noted that Nixer's support for multiple architectures is not yet fully developed.


## Developer Empathy is your Superpower | Kunal Kushwaha

URL: [https://www.youtube.com/watch?v=5zuDTNkeXww](https://www.youtube.com/watch?v=5zuDTNkeXww)

 * Kunal Kushwaha: Developer Empathy is your Superpower
* Workshop presentation for developers
* Discussed the importance of empathy in software development
* Struggled with technical and non-technical issues, team communication, and user engagement
* Favorite restaurant recommendation for London
* Experience as a developer manager and the need for empathy in leadership
* Empathy is crucial in preventing confirmation bias, curse knowledge, hindsight bias, and availability bias
* Importance of creating personas, active listening, and diversity in teams
* Efficiency within teams: empathy helps resolve conflicts, build trust, improve communication, and boost creativity
* Empathy during the COVID-19 pandemic: practicing perspective taking and providing support to teammates
* Examples of empathetic leaders understanding imposter syndrome and providing reasonable support
* Importance of documenting good code, readable code, simple logic, and good naming conventions.


## Exploring eBPF: Revolutionising Kubernetes Sidecars and Beyond | Ayesha Kaleem

URL: [https://www.youtube.com/watch?v=63KQT5xDIrU](https://www.youtube.com/watch?v=63KQT5xDIrU)

 * eBPF (Extended Berkeley Packet Filter) is a technology that allows running sandbox programs in the Linux kernel without changing its source code.
* It enables custom code to take advantage of kernel resources, like network packet filtering and observability, without rebooting the system.
* Originally created for TCP dump filtering, eBPF has expanded beyond networking into various domains such as security and performance optimization.
* eBPF programs are event-driven and can attach to kernel events (function entry/exit points or trace points) and user probes.
* They are typically written in C or Python using tools like BCC (BPF Compiler Collection) or Clang.
* The JIT (Just-In-Time) compiler optimizes eBPF bytecode for the specific instruction set of the target system.
* eBPF Maps are essential, as they help store state and share data between eBPF programs running inside the Linux kernel or user space.
* Commonly used eBPF map types include hash maps and arrays.
* Writing an eBPF program requires some knowledge of the Linux kernel and its APIs but offers significant advantages like resource utilization, networking security, observability, and performance improvements.
* Various projects using eBPF include Cilium, Isovalent's Tetragon, Falco, KRON, Bumblebee, Kio, Linkerd, and many others.
* Service mesh solutions like Istio, Consul Connect, and Envoy have adopted eBPF technology for advanced features like networking security, observability, and performance improvements.
* eBPF can be used to add functionality to the Linux kernel that was previously implemented in user space, like L7 traffic management, authentication, authorization, tracing, and reliability.
* The sidecar model is still relevant even with the rise of eBPF technology since it offers additional benefits beyond what eBPF alone can provide.
* eBPF does not limit service mesh solutions; it can work alongside them to provide better resource utilization, networking security, observability, and performance improvements.


## Three And A Half Years Of Building Our Kubernetes Platform: Lessons Learned Along The Way | Maryam T

URL: [https://www.youtube.com/watch?v=ADK8Vd5WNZU](https://www.youtube.com/watch?v=ADK8Vd5WNZU)

 * Maran Tavakoli, cloud engineer at Relux Solutions in Finland, has been working on building a Kubernetes platform for their company for the past three and a half years.
* The project began in late 2019 with an internal development team migrating workloads to Kubernetes due to its obvious advantages.
* In early 2020, multiple development teams started using the platform, but there were challenges such as managing service identities and configuration files.
* A major incident occurred when a change was made to managed identity, which caused issues for several teams and required a rollback.
* In mid-2020, the team decided to unify the Kubernetes platform within the company and use Terraform to manage configurations.
* The team grew throughout 2021, with more development teams and environments added, as well as improvements like versioning and automation.
* In late 2021, the team started using a service mesh and deploying applications in isolated namespaces for better security.
* In early 2022, the project became more mature, with additional features being added to support different team requirements.
* Some challenges included implementing automated testing, managing access rights, and optimizing costs.
* The team also had to deal with a major incident when a test environment was deleted by accident, leading to a significant downtime.
* In late 2022, the team introduced start-stop automation for development clusters and changed the release strategy to monthly instead of bi-weekly.
* Some future plans include improving the testing strategy, implementing global load balancing, and adding a web application firewall.


## Admission controllers: the good, the bad, the ugly | Nic Vermande

URL: [https://www.youtube.com/watch?v=BYw3wbuUHvY](https://www.youtube.com/watch?v=BYw3wbuUHvY)

 * Speaker is Nick Vermande, working in software development and Kubernetes community for six years
* Topic: Admission Controllers - The Good, The Bad, The Ugly
* Admission controller enforces governance within a Kubernetes cluster
* Two types of admission controllers: static (compiled part) and dynamic (API server sends admission request to webhook server)
* Important design decisions when building an admission controller include security compliance, PSP/PSA, resource management, and custom logic
* Mutating admission webhooks validate or modify objects in the cluster before they are deployed
* Dynamic admission controllers build and run outside of the cluster
* Building a custom admission controller: need to consider educational purposes, troubleshooting, external APIs (like Marvel API), and whether it's necessary
* Certificates are required for TLS communication between components in an admission controller setup
* The process of creating a mutating webhook involves creating a configuration, handling the handler function, extracting request data, interacting with external APIs, and encoding responses
* Important considerations when implementing admission reviews include best practices, timeouts, and security.


## The Need for Speed - performance benchmarks for HPC and AI workloads in Kubernetes

URL: [https://www.youtube.com/watch?v=D7eazRekwE8](https://www.youtube.com/watch?v=D7eazRekwE8)

 * Matt from a HPC consultancy with 7-year experience in cloud HPC, focuses on applying expertise to cloud native workloads using OpenStack and Kubernetes
* Discusses the importance of performance benchmarking for both infrastructure providers and application developers in the context of HPC and AI workloads
* Mentioned use cases include Loki, an active upstream contributor project in the Cloud Native Computing Foundation (CNCF), and Volcano Batch Scheduler
* Benchmarking is important to understand hardware performance, optimize infrastructure, and identify misconfigurations affecting performance
* Discusses benchmarking in Kubernetes using Cube Perf and the benefits of using a kubernetes operator for defining and executing performance benchmarks
* Mentions testing networking (bandwidth and latency), CPU, storage, and GPUs as key areas for benchmarking
* Specific tools mentioned include Fio for CP per test, OpenFOAM for computational fluid dynamics software, and a Nvidia GPU microbenchmark using AlexNet image classification model
* Discusses the importance of testing hardware offloads and RDMA (Remote Direct Memory Access) for high performance computing workloads in Kubernetes environments.
* Mentions the use of real Nick inside open stack VM and kubernetes pod, and the need for RDMA support and optimization in Kubernetes clusters for RDMA-enabled applications like MPI.
* Discusses the importance of optimizing network traffic and reducing encapsulation in Kubernetes networks using tools like iperf3 and VXLAN.
* Mentions that RDMA can offer low latency and high bandwidth, making it ideal for HPC workloads
* Mentions that Cube Perf is a simple tool that can be used to create benchmark yaml files to test different storage classes in Kubernetes.
* Discusses the importance of testing performance at scale and examining file system consistency locking behavior when scaling kubernetes pods.
* Discusses the importance of using representative workloads, like OpenFOAM for computational fluid dynamics software, to assess cluster performance.
* Mentions the need to test GPUs in a Kubernetes environment for machine learning applications and the use of tools like Nvidia GPU operator and device plugins.
* Discusses the importance of testing network performance, particularly with large message sizes, in MPI applications running on Kubernetes clusters.
* Encourages attendees to get involved in open source projects to find and fix bugs in Kubernetes.


## There’s no i in Kubernetes: Why Kubernetes Security is a Team Sport | Malavika Balachandran Tadeusz

URL: [https://www.youtube.com/watch?v=DD8ikOs-EPg](https://www.youtube.com/watch?v=DD8ikOs-EPg)

 * Malavika Balachandran, product manager at IG and Calico, speaks on Kubernetes security being a team sport
* Challenges in Cloud security include network security and collaboration
* Three types of engineers responsible for Kubernetes security: developers, DevOps, and security engineers
* Developers deploy applications quickly but may overlook security; DevOps keep the platform running smoothly, and security teams ensure application code and platform are secure while not controlling them directly
* Collaboration is key to effective security in a Kubernetes environment
* Shifting security left is important, but can be challenging with alert fatigue and managing vulnerabilities
* Calico is a popular tool for network security in Kubernetes environments with 1 million clusters and 50,000 organizations using it
* Network security, runtime monitoring, threat defense are key components of Cloud security programs
* Calico policy is widely used for Kubernetes network security but not all organizations use it effectively
* Calico policy provides features like policy ordering, which makes collaboration easier among developers, platform engineers, and security analysts
* Network policies allow fine-grained control over pod communication in a Kubernetes environment.


## A day in the life of an OSS maintainer | Patrick Stephens

URL: [https://www.youtube.com/watch?v=GCOcqA9u38E](https://www.youtube.com/watch?v=GCOcqA9u38E)

 * The speaker is an open source maintainer for Fluent Bit, an observability agent used in public clouds and enterprise solutions.
* Fluent Bit is a mature project started in 2014 that processes various inputs and sends outputs to different destinations. It supports collecting logs, metrics, and traces.
* The speaker works for Calpia, the company behind Fluent Bit, where they focus on encouraging contributions from companies.
* Contribution areas include documentation, testing, CI/CD, and engagement in the community.
* The speaker advocates that contributing to open source projects, even indirectly, benefits both the contributor and the community.
* They have been maintaining open source software for several years and previously worked in defense and infrastructure roles.
* They started working on Fluent Bit in 2017 when they joined the Calpia team and began interacting with the community through blog posts.
* They aim to make using Fluent Bit straightforward and user-friendly, focusing on the user perspective rather than implementation details.
* The speaker spends a lot of time in Slack, helping people answer questions, review PRs, and triaging issues.
* They also spend time writing blog posts, giving presentations, and conducting training sessions.
* They have solved various problems reported by users, often involving Docker images or different formats.
* Contributing to Fluent Bit has helped the speaker learn new tech and build relationships with people in the community.
* They encourage companies to contribute to open source projects, citing benefits like gaining expertise and improving their products.


## Webhooks - what's the worst that could happen? | Marcus Noble

URL: [https://www.youtube.com/watch?v=GFMnC1a7bFk](https://www.youtube.com/watch?v=GFMnC1a7bFk)

 * Marcus Noble, platform engineer at Giant Swarm, discussing risks of webhooks in Kubernetes
* Webhooks are powerful features in Kubernetes for validating, mutating, and converting configurations
* Validating admission policy, a type of webhook, enforces rules on API requests and admissions
* Risks of using webhooks include misconfiguration, malicious attacks, and unavailable control plane
* Misconfigurations can lead to cluster issues, such as incorrect content types or redirects
* Malicious webhooks can cause denial of service (DoS) attacks or inject unwanted resources
* Unavailable control plane can make it difficult to upgrade, monitor, or roll back webhooks
* Best practices for using webhooks include proper deployment, monitoring, and error handling
* Webhooks can be used for policy enforcement, such as enforcing enterprise rules or best practices within a cluster
* Example of preventing security exploits using webhooks: the Log4j vulnerability
* Potential risks of webhooks include burden on development and operation, potential errors and unintended consequences.


## Running ArgoCD at scale for 1000+ applications | Saeid Bostandoust

URL: [https://www.youtube.com/watch?v=H3T-Nkxdywg](https://www.youtube.com/watch?v=H3T-Nkxdywg)

 * The speaker, Saeid Bostandoust, works as a kubernetes architect and director of software engineering at CBR, a construction building real estate company. He prefers using open source technologies and contributes to Argo CD and other open source projects.
* Agenda: Discussing running Argo CD at scale for 1000 applications, looking into Argo CD architecture, deploying 1000 applications without optimization, tuning Argo CD for 1000 applications, and deployment patterns.
* Argo CD Architecture: Includes application controller, notification controller, application set controller, redish main component, system repo server, and cluster components.
* Without optimization, deploying 1000 applications using Argo CD took a long time and caused the application controller to get restarted multiple times due to high load.
* Tuning Argo CD: Needed to increase application controller replicas, distribute application controllers across environments, optimize dependency management, and configure cache settings.
* Deployment Patterns: Discussed using one repository per microservice, Helm charts, and deploying multiple applications from a single repository.
* Challenges encountered during deploying 1000 applications included slow manifest generation, memory usage, and network latency.
* Solutions: Included optimizing manifest size, parallelizing manifest generation, increasing fetching timeout, and using web hooks instead of reconciliation time.
* Other optimizations included reducing maximum manifest size, using plugins, optimizing Helm chart deployment, and managing repositories effectively.


## Fly Me to the Moon: Punch cards, Supercomputers, and Kubernetes | Kat Cosgrove

URL: [https://www.youtube.com/watch?v=Pe9V1hG4LUQ](https://www.youtube.com/watch?v=Pe9V1hG4LUQ)

 * Kat Cosgrove, lead developer advocate at Dell, discusses the origins and concepts of Kubernetes
* Kubernetes is a relatively new cloud-native technology that aims to reduce complexity in managing containerized applications
* Origins of Kubernetes predate DevOps and infrastructure as code, with virtualization being a significant challenge since the dawn of computing
* Core Concepts of Kubernetes include an abstraction layer built on top of another abstraction layer, solving previously difficult problems
* Virtualization has evolved over the decades, from hardware to operating system level virtualization, and Kubernetes relies on a variety of virtualization techniques
* The origins of time sharing and virtual memory date back to the 1950s and 60s, with the first patent for multiprogramming filed in 1959
* IBM played a significant role in virtualization and time sharing, with the development of mainframes and virtual memory systems like System/360 and CP40
* Unix operating system began developing containerization concepts in the late 70s, leading to modern container technologies like Docker and Kubernetes
* The timeline of virtualization and containerization diverged around 2008, with the release of tools like LXC and systemd
* Docker, released in 2013, popularized container technology by making it more approachable, user-friendly, and ubiquitous
* Kubernetes was announced as an open-source project in 2014 and has since become a foundational technology in the cloud-native landscape.


## Lightning talk 5

URL: [https://www.youtube.com/watch?v=Qlfl1DCC2SI](https://www.youtube.com/watch?v=Qlfl1DCC2SI)

 * The speaker wants to talk about the platform orchestration pattern, which was recently highlighted on Thoughtworks Tech Radar.
* Platform orchestration goes beyond traditional platform services by providing additional features.
* It is important for organizations to consider buying versus building when it comes to platform services.
* Building internally can differentiate a business in the market, but requires engineering time and resources.
* Next generation platform orchestrators provide managed services with self-service discovery and collaboration capabilities.
* The speaker mentions challenges with managing complex infrastructure and bad developer experiences as reasons for considering platform orchestration.


## Platform Engineering Is Not About Tech | Francesca Carta & Nicolò Cambiaso Erizzo

URL: [https://www.youtube.com/watch?v=SEMUBJ78Lm0](https://www.youtube.com/watch?v=SEMUBJ78Lm0)

 * Francesca Carta and Nicolo Erizzo discuss the importance of organizational change in platform engineering
* Platform engineering involves implementing reusable tools, self-service capabilities, and automating infrastructure operations to improve developer experience and productivity
* The goal is to create a frictionless environment where developers can produce valuable software with minimal overhead
* Every technological change involves organizational change, and technology must adapt to the organization, not the other way around
* Common pitfalls in platform engineering include lack of political capital, misaligned expectations, internal competition, and balance between trade-offs like freedom and standardization
* Successful platform adoption requires effective communication, consensus building, and a focus on developer experience and collaboration
* Three case studies illustrate different approaches to platform engineering: a small digital native startup, a global manufacturing company, and a multinational system integrator.
* The first story is about a small engineering organization focusing on efficient collaboration between teams.
* The second story is about a large industrial organization building an internal platform as a strategic pillar.
* The third story is about a multinational system integrator taking an unexpected approach by throwing away their initial platform and adopting a new one.
* To summarize, the key takeaways from the talk are:
	+ Platform engineering is about providing better self-service developer experiences.
	+ Technology and organization must be closely connected.
	+ Effective communication, consensus building, and change management are crucial for successful platform adoption.
	+ Common pitfalls include misaligned expectations, lack of political capital, internal competition, and balance between trade-offs like freedom and standardization.


## Secure Workloads Know Who They A.R.E: Attestation, Restriction & Enforcement in Kubernetes & Beyond

URL: [https://www.youtube.com/watch?v=TAwY2LXCils](https://www.youtube.com/watch?v=TAwY2LXCils)

 * The speaker, Land Mua, is a senior developer advocate at Kubernetes AWS and CNCF Ambassador
* The session is about securing workloads in complex, heterogeneous environments like Kubernetes and beyond
* The speaker shares a memory from working on a digital product with numerous integrations and the challenges of juggling multiple security identity models
* Modern systems consist of many distributed, heterogeneous services, making security a major concern
* Attestation is a standard mechanism for issuing digital IDs to workloads to establish trust between them
* Spiffy is an open-source security framework that supports universal issuance and attestation of digital identities
* Restriction enforcement ensures that only authorized workloads can communicate with each other within a trust domain
* Open Policy Agent (OPA) is used for policy enforcement based on dynamic rules and Rego language.


## Knative Serverless for AI/ML Applications | Ian Lawson

URL: [https://www.youtube.com/watch?v=UWkPkT8R5wc](https://www.youtube.com/watch?v=UWkPkT8R5wc)

 * Ian Lawson, Red Hat developer advocate with AI/ML background
* Discussed the concept of "unintelligent" AI and the evolution of rule-based systems (genetics, mimetics)
* Introduced K Native and its use in building serverless, event-driven AI applications
* Highlighted the benefits of K Native such as zero resource consumption and autoscaling based on concurrency and request per second
* Described how K Native extends Kubernetes with CRDs (Custom Resource Definitions) for services and configurations
* Demonstrated a simple example of using a K Native serving service to handle events and trigger actions in an AI system using Neurons and grid connect.


## Lightning talk 4

URL: [https://www.youtube.com/watch?v=WQz5cbojxPI](https://www.youtube.com/watch?v=WQz5cbojxPI)

 * Steve Jud from Jet Stack Consult, Kubernetes consultancy
* Spends a lot of time assessing client clusters in audits
* Webinar topic: Making Kubernetes clusters more secure
* Principle 1: Least privilege - don't use cluster admin role for everyone
* Principle 2: Control plane access - keep API behind Bastion or VPN, enable authentication
* Principle 3: Workload isolation using Network Policy
* Principle 4: Secrets management - use services like Secrets Manager or Hashicorp Vault
* Principle 5: Alternative to Helm for managing secrets with Helm templates and custom manifests
* Principle 6: Certificate management - Jet Stack C manager for easier certificate handling instead of manual processes.


## How to Cultivate Belonging in Your Open Source Community | Jennifer Riggins

URL: [https://www.youtube.com/watch?v=YUY3GjhY0UE](https://www.youtube.com/watch?v=YUY3GjhY0UE)

 * Open source communities have a diversity problem, with underrepresentation of women and people of color
* Statistically, only 4% of open source contributors are women and nonbinary individuals
* People from marginalized backgrounds often face barriers to entry in open source, such as lack of technical skills or representation
* Voluntary work in open source projects is a major issue for those who cannot afford to contribute for free
* Open Source companies rely on open source projects, but single maintainers put them at risk of burning out and creating a pay-to-contribute culture
* Women and people of color often feel isolated and unwelcome in open source communities
* Lack of clear code conduct and enforcement can lead to toxic environments
* Open Source Community Health analytics is a project that aims to measure the health of open source communities and provide resources for improvement
* To attract and retain diverse talent, open source projects should have clear pathways to leadership, enforce code conduct, and create welcoming and inclusive environments
* Open source projects can use tools like self-defined apps and AI to make the contribution process more accessible and streamlined for newcomers
* Mentoring and formalized mentorship programs are important for creating a supportive community and addressing the isolation felt by underrepresented individuals.


## Unleashing the Power of AI in Kubernetes through K8sGPT | Alex Jones

URL: [https://www.youtube.com/watch?v=aKVDMh2ha98](https://www.youtube.com/watch?v=aKVDMh2ha98)

 * Alex Jones is a principal engineer at AWS, discussing the power of AI in Kubernetes
* He mentions his background in machine learning and fascination with AI since childhood
* He discusses how AI is being used in various industries, including insurance underwriting and medicine
* He talks about the importance of pattern recognition, prediction, and prognostication in Kubernetes
* He mentions the challenges of diagnosing issues in Kubernetes and the potential for AI to help
* He mentions his experience with using GPT-3 for analyzing Kubernetes clusters and generating reports
* He discusses the potential for AI to simplify tasks, improve observability, and automate workflows in Kubernetes.


## Lightning talk 6

URL: [https://www.youtube.com/watch?v=bJBkjOvlVIc](https://www.youtube.com/watch?v=bJBkjOvlVIc)

 * Speaker went to CUBCon China and shared their experience
* Originally from Argentina, has lived in London for 12 years, felt like a completely different place
* Works at Diag, a cloud native staff company
* Friend Alexa works at Bloomberg building a platform for data scientists using Open Source tools
* Saw presentations on various technologies like Kubernetes, Apache OpenWhisk, Dapper, and more
* Surprised by interaction with Chinese developers and their dedication to platform engineering
* Saw an open function project that brought different projects together to build a specific use case
* Impressed by the architectural diagram of the project and how it combined Open Source tools from the West
* Talked about K native autoscaling and Dapper, which allows developers to connect APIs with infrastructure in a resilient way without needing to know the underlying infrastructure.
* Mentioned working on a book tutorial for an open source project in the CNCF repository.


## Cluster by Cluster: Key Moments in the Cloud Native Ecosystem | Anaïs Urlichs

URL: [https://www.youtube.com/watch?v=brVemuiJMb0](https://www.youtube.com/watch?v=brVemuiJMb0)

 * Anais Urlichs talks about her experience with the cloud native ecosystem and introduces schema theory
* In 2013, companies were moving towards cloud computing and containerization
* Google developed Kubernetes as a response to manage containerized applications
* Docker introduced a simpler way to deploy applications using containers
* In 2014, the first version of Kubernetes was released as open source
* Cloud Native Computing Foundation (CNCF) was formed to provide governance and foster growth in the ecosystem
* Prometheus was created to address monitoring needs in containerized environments
* Helm was developed to manage Kubernetes resources declaratively
* GitHub became a hub for the cloud native community with many projects graduating from incubation
* The CNCF has grown to include over 1500 companies and 13,000 contributors
* Flux CD and GitOps principles have emerged as new ways to deploy resources
* Operators have been developed to automate tasks in Kubernetes clusters
* Celium was added to provide network security for Kubernetes
* The CNCF has a global Ambassador Network to help spread awareness and knowledge about cloud native technologies.


## Lightning talk 2

URL: [https://www.youtube.com/watch?v=dR5T2qNAuCs](https://www.youtube.com/watch?v=dR5T2qNAuCs)

 * Introduced himself as Lewis, Solutions Architect and organizer of the event
* Shared that he wasn't a book author or git connoisseur but had experience with career advice
* Expressed frustration about receiving generic answers to career questions and not finding value in others' journeys
* Encouraged learning Git, Markdown, and writing code as starting points for those getting into the industry
* Advised persistence and taking initiative to become a knowledge owner
* Discussed the importance of networking and sharing opportunities with others
* Shared a lesson learned about not being afraid to fail and allowing others to take chances
* Mentioned sponsoring someone's ticket to a conference as an opportunity to help those starting in the industry
* Expressed nerves about giving the talk but found value in meeting new people and learning from them
* Encouraged asking for consent before approaching new contacts.


## Panel Discussion: The Future of Open Source

URL: [https://www.youtube.com/watch?v=kE5o4_Ed3pU](https://www.youtube.com/watch?v=kE5o4_Ed3pU)

 * Panel discussion on the future of Open Source with Paula Kennedy, Daniel Bryant, Alex Chirop, and Lawrence Dallachy moderated by Liz Rice
* Discussion started with a question about whether we have reached "Peak Open Source" based on a statistic that 90% of software is open source
* Some panelists think open source is changing the way software is developed and business models are evolving
* Others feel open source is not going anywhere and there will always be a need for it
* Discussion touched on topics such as reuse, open core business models, social contracts, innovation, and IP protection in Open Source projects
* Some concerns were raised about the fragmentation of licenses and the potential impact on community contributions
* The role of foundations in Open Source software was also discussed, with some panelists expressing their support for the Foundations' efforts to encourage collaboration and funding.


## Kubernetes MLSec: Securing AI in space | Andrew Martin & Francesco Beltramini

URL: [https://www.youtube.com/watch?v=lZv2a1kjdC8](https://www.youtube.com/watch?v=lZv2a1kjdC8)

 * Introduction: Andrew Martin and Francesco Beltramini talk about securing AI systems in the context of Kubernetes MLSec
* Background: Both speakers have experience in security engineering, with a focus on cloud native technologies and AI
* AI Ecosystem: Overview of different types and levels of AI, focusing on machine learning and its lifecycle
* ML Security Challenges: Discussion of potential threats and risks in the ML ecosystem, especially in the context of Kubernetes
* Threat Modeling: Importance of threat modeling to identify risks and mitigate them in ML systems
* Specific Use Case: Analyzing a hypothetical satellite communications company (Company X) and its AI-based system
* Security Challenges for Company X: Discussion of various threats, including data poisoning, model degradation, and supply chain attacks
* Mitigation Strategies: Suggestions for securing ML systems, such as data signing, access control, and parameter security
* Conclusion: Emphasis on the importance of a thorough understanding of the ML ecosystem and threat modeling to ensure secure implementation and deployment.


## From Frontend Engineering to Cloud Native: Lessons Learned from a Beginner | Shedrack Akintayo

URL: [https://www.youtube.com/watch?v=m6_4vt8gu8g](https://www.youtube.com/watch?v=m6_4vt8gu8g)

 * Shedrack Akintayo: Frontend Engineering to Cloud Native - Lessons Learned from a Beginner
* Transitioned from frontend engineering to Cloud native due to curiosity and interest in DevOps
* Cloud native philosophy: building and running scalable applications using cloud-based service delivery model
* Benefits: increased efficiency, cost reduction, reliability, resilience, and high availability
* Containerization: lightweight, isolates software in particular environments, portability
* Container runtimes: Docker, LXC, OCI, Kubernetes
* Kubernetes: prominent container orchestration platform, manages container run within a cluster, load balancing, scaling, rolling updates, and rollbacks
* Serverless: executes applications without managing servers, AWS Lambda, Celium (CNI), Calico, Flannel
* APF (eBPF): technology to extend kernel capabilities without changing the source code
* CNCF: Cloud Native Computing Foundation, fosters adoption of cloud native principles and ecosystem.

Summary:

* Shedrack Akintayo shared his journey from frontend engineering to learning Cloud native technologies as a beginner.
* Cloud native philosophy focuses on building and running scalable applications using cloud-based services and infrastructure.
* Key benefits include increased efficiency, cost reduction, reliability, resilience, and high availability.
* Containerization is important for creating lightweight, isolatable, portable deployments.
* Container runtimes like Docker, LXC, OCI, and Kubernetes help manage container deployment and execution.
* Kubernetes is a popular container orchestration platform that manages containers within a cluster, ensures desired states, provides load balancing, and handles scaling and rolling updates.
* Serverless technologies enable running applications without managing servers directly.
* APF (eBPF) extends kernel capabilities to enhance observability and networking performance.
* CNCF is an organization that helps drive adoption of cloud native principles and fosters a vendor-neutral ecosystem.


## Lightning talk 3

URL: [https://www.youtube.com/watch?v=mNvP2S7mCOA](https://www.youtube.com/watch?v=mNvP2S7mCOA)

 * Drew is discussing Pod Security Standard for Kubernetes newbies
* Three types of policies: Unrestricted, Baseline, and Restricted
* Enforcing security standards with Pod Security Admission Controller
* Policies can be set at the cluster or namespace level
* Violation of policy results in pod rejection or logging
* Engine X container requires privileged mode and must have a label to deploy
* Removing default security context from deployment causes errors
* Avoid privilege escalation and dropping unnecessary capabilities
* Use Open Policy Agent or other tools like Cerno or Warden for additional security.


## eBPF and Kubernetes — Better Together! Observability and Security with Tetragon | Anna & James

URL: [https://www.youtube.com/watch?v=oU7dPKoVfm4](https://www.youtube.com/watch?v=oU7dPKoVfm4)

 * Anna and James present on eBPF and Kubernetes with a focus on the Tetragon project
* Anna introduces herself as an observability engineer at Valent and previously worked on network observability projects
* James introduces himself as a senior solutions architect who has worked on upstreaming the Kubernetes project and is a former release lead for Kubernetes 124
* Tetragon is designed to solve security, policy enforcement, and monitoring problems in Kubernetes using eBPF
* eBPF programs can be loaded into the Linux kernel without recompiling or using a particular language
* Tetragon is fully kubernetes native, meaning it's aware of pods and namespaces within the cluster
* Process execution: Tetragon allows for monitoring process clusters and network visibility without using CNI (Calico Networking Ingress)
* eBPF maps are used to store state and improve observability by providing context data and correlating different events
* Tetragon can be used for process and file operation observation within the cluster
* Security Context: Tetragon helps manage security policies and access control within the Kubernetes cluster, even in privileged pods
* Network monitoring: Tetragon enables network monitoring with tracing policies that define which hook points to monitor, such as TCP connect, close, and send messages
* Tetragon is deeply integrated with Kubernetes and allows for filtering of kubernetes metadata using namespace, port selector, and label selectors.
* Tetragon code can be found on GitHub.


## Powering SKA science with LOKI | John Garbutt

URL: [https://www.youtube.com/watch?v=oqe5X_vcyxk](https://www.youtube.com/watch?v=oqe5X_vcyxk)

 * John Garbett, ex-Citrix employee, now works on OpenStack and HPC Cloud for the Square Kilometer Array (SKA) project
* SKA is an international collaboration to build a telescope array that can scan the sky faster than any current observatory
* The telescope will generate massive amounts of data, requiring advanced computing infrastructure
* Garbett started working on the project in 2017 as a consultant for Cambridge University
* SKA consists of two telescopes: one in Australia (50-250 MHz sensitive) and one in South Africa (97 dish, 130 antenna)
* Each telescope will generate 8 terabit seconds of data per day, requiring advanced data processing and storage capabilities
* The project aims to process data in real-time, globally, using a distributed computing system
* Loki is an open infrastructure solution for making local bare metal machines dynamic and part of the SKA computing infrastructure
* OpenStack and Kubernetes are being used to make the supercomputer more agile and reconfigurable
* The project requires a significant investment in computing resources and collaboration between academia and industry.


## Gateways of power: building your own service mesh | Miles Bryant

URL: [https://www.youtube.com/watch?v=qcIrvj20d0o](https://www.youtube.com/watch?v=qcIrvj20d0o)

 * Mile Bryant, tech lead at Monzo, discusses building their own service mesh
* Monzo is a digital bank in the UK with advanced money management features and over 5 million customers
* In 2015, they had a simple product architecture but decided to use microservices for extensibility and scalability
* Challenges of working with distributed systems: network unreliability, service discovery, observability
* Initial attempts at handling these challenges included using libraries like Finagle and RabbitMQ
* RabbitMQ was difficult to operate, especially in the Kubernetes environment
* Decided to use Link instead, which provided a neat sidecar proxy with advanced features like service discovery and circuit breaking
* Later faced issues with scaling and security, leading them to upgrade to Envoy
* Envoy provided a more battle-tested solution for their needs, with a similar architecture and the added benefit of XDS aggregated service discovery
* New requirements led them to write custom code for Envoy and make it more complex
* Considering moving to a store-and-forward model for traffic control
* Benefits of building their own service mesh include enabling network policies and customization, but require a significant investment of time and resources.


## Smarter than your average SBOM ! | Matt Jarvis & Andrew Martin

URL: [https://www.youtube.com/watch?v=rvsYnRxq0pU](https://www.youtube.com/watch?v=rvsYnRxq0pU)

 * Matt Jarvis and Andy Martin discuss Software Bill of Materials (SBOM) in the context of Cloud Native software
* SBOM is a structured data that describes the relationships between elements in software, similar to package repositories
* SBOM is important for managing supply chain security by providing standard, machine-readable information about dependencies and vulnerabilities
* SBOM can be generated at different points in the development process and contains various types of information such as licenses, publisher details, and vulnerability data
* There are tools like CycloneDX and OpenSSF that help create and enrich SBOMs
* Enriched SBOMs can include additional data from external sources, such as license information and security vulnerabilities
* SBOMs are crucial for ensuring trust in the software supply chain by verifying the authenticity of components and their dependencies.


## Powering Up Online Multiplayer: Leveraging Kubernetes for Game Server Optimisation

URL: [https://www.youtube.com/watch?v=sBjvOTRIKBQ](https://www.youtube.com/watch?v=sBjvOTRIKBQ)

 * The speaker, a Solutions Architect at AWS, is discussing the optimization of game servers using Kubernetes.
* Game server architecture involves a central authority to manage game state and ensure fairness. Traditional game servers have challenges like scaling, latency, and cheating.
* Kubernetes can simplify the deployment and management of game servers by automating patching, scaling, and managing multiple instances in different regions for lowest latency.
* Persistent world games may require special considerations like memory checkpointing or externalizing state.
* High-performance games with high frame rates need to run close to the player for optimal performance, which can be achieved using edge servers and load balancing.
* Running a game server on Kubernetes eliminates management complexity, especially for large clusters and deployments across multiple regions.
* The speaker demonstrates using Carpenter (Kubernetes autoscaler) to manage resources efficiently, scaling based on demand and optimizing instance size for specific workloads.
* Agonas is used to manage game servers as a fleet, providing features like node selection, patching, and releasing updates automatically.
* The speaker deploys an example racing game using Kubernetes and shows how it can be scaled and managed efficiently with Carpenter and Agonas.
* Key benefits of running a game server on Kubernetes include automated deployment, scalability, resilience, cost efficiency, and the ability to run on different architectures like Arm processors.


## Acquisitions, Assimilation and Alignment | Toby Jackson

URL: [https://www.youtube.com/watch?v=uGZ1oDAM9MI](https://www.youtube.com/watch?v=uGZ1oDAM9MI)

 * Toby Jackson, Reliability Engineering Lead at Future PLC, shares his experiences of team health and acquisitions in the technology industry over the last decade
* Success depends on a healthy team with minimal politics, confusion, and consistent feedback
* Team formed in Bath, England, started as a small group of engineers working together, sharing infrastructure and war stories
* Acquisitions brought new challenges and cultural differences, requiring rebuilding and evolving the team to embrace new opportunities
* Two distinct engineering teams merged, operating under different tools and vendors, which required aligning and simplifying
* Embraced Kubernetes and set default practices for simplification
* Trust and empathy are crucial in remote and distributed teams, especially during acquisitions
* Regular meetings, personal stories, and retrospectives help build trust and collaboration
* Blameless culture and shared accountability are important in a healthy SRE team
* Inconsistency is a challenge for the future of SRE, requiring common friction points to be identified and addressed
* Human interaction and collaboration are essential in building a successful, innovative team.

Overall, Toby Jackson discusses his experiences with team health during acquisitions and how trust, empathy, consistency, and collaboration have played a role in creating high-performing teams. He emphasizes the importance of addressing cultural differences, simplifying processes, and fostering an inclusive environment for success.


## Scaling Systems of Trust for Software | Dan Lorenc

URL: [https://www.youtube.com/watch?v=vtxOS90LGlA](https://www.youtube.com/watch?v=vtxOS90LGlA)

 * Dan Lorenc discusses the issue of trust in open source software, particularly in the context of cloud native ecosystems
* Implicit trust placed on open source code and maintainers is a concern as attackers have started targeting vulnerabilities
* Regulators are noticing the danger and crafting regulations, creating friction
* Trust systems in place for open source are not working at scale, especially in cloud native ecosystems
* Discussion of the history of trust in computing, starting with the early 1980s and Linux distributions
* The story of Ken Thompson's paper "Reflections on Trusting Trust" and the back door in Bell Labs compiler is mentioned
* Debian distribution's approach to building trust through curation and verification is discussed
* The shift towards secure package distribution and cryptographic signing is mentioned
* Modern programming language ecosystems, such as Python, have different trust models and face different challenges
* In the cloud native ecosystem, there are multiple layers of trust to consider, including Docker and Helm
* Open source software security incidents are handled better than closed source software, but there are still challenges
* Lack of a tamper-proof seal and curation are two major issues in open source trust
* Solutions like Sigstore and scaling package managers are being explored to address these issues.


## Bridging the Platform Empathy Gap: Applying Product Management to Platform Engineering | Cat Morris

URL: [https://www.youtube.com/watch?v=yH0rhSyZsqQ](https://www.youtube.com/watch?v=yH0rhSyZsqQ)

 * Cat Morris shared her experience attending a conference where she attended a platform engineering and product management room
* She was surprised to hear developers express frustration and resentment towards platform engineers, who they saw as unable to understand their needs and provide clear guardrails
* Morris identified with this as she had once been a frustrated developer working on a platform team
* She realized that the source of the empathy gap between platform engineers and developers was due to a lack of understanding and communication
* Morris proposes three hypotheses for why the empathy gap exists:
  + DevOps platform engineering created the empathy gap by prioritizing automation over developer experience
  + The larger empathy gap leads to lower platform adoption and slower development
  + Platforms with low adoption are doomed to fail
* She suggests that product managers can bridge the gap by focusing on the application developer user, adopting a Northstar metric to measure adoption, and prioritizing the needs of developers.
* Morris emphasizes the importance of understanding the needs of developers and providing them with the right level of abstraction and configurability to get their jobs done efficiently and effectively.
* She also highlights the need for platforms to be usable, consistent, self-service, and predictable in order to encourage adoption.
* Morris concludes by emphasizing the importance of closing the empathy gap between platform engineers and developers to build successful platforms.


## The Secret Life of Kubernetes Containers | Rory McCune

URL: [https://www.youtube.com/watch?v=zByo74nx-Ak](https://www.youtube.com/watch?v=zByo74nx-Ak)

 * Rory McCune, senior security advocate at DataDog, discusses the secret life of Kubernetes containers
* Background: McCune is a former security pentester and focuses on container security in Kubernetes
* Goal: To provide useful information for debugging, troubleshooting, and designing new containerized applications
* Container basics: Containers are like Docker, used to deploy and scale applications without needing detailed knowledge of what's happening at a low level
* Isolation: Containers are isolated from the host system, preventing random processes from starting and resolving library version dependency problems
* Namespaces and cgroups: Linux features not specifically designed for containers but used by Docker and Kubernetes to isolate processes and resources
* File systems: Containers have their own file systems, allowing interaction using tools like Cube Cuttle and proc
* Networking: Containers can share namespaces and use proxy servers like Cube Proxy for handling network traffic
* Flexibility: Containers are flexible and allow for various ways to interact with components, including API server, scheduler, ETD (Container Runtime Interface), and runC
* Debugging: Tools like nerdctl and chat GPT can be used for container debugging, and understanding underlying container technology is crucial for troubleshooting
* AI: McCune briefly touches on using AI tools like chat GPT to generate code and interact with container APIs
* Security: Containers have security benefits such as isolation and control over access to the API server and SD (Container Storage Interface) cluster, but also potential vulnerabilities if not configured properly.



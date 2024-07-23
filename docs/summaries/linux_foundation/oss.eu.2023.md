## Lightning Talk: How Jenga & Tetris Can Help Run More Containers with Lesser Costs...- Yash Bhatnager

URL: [https://www.youtube.com/watch?v=6HatF5F4n5A](https://www.youtube.com/watch?v=6HatF5F4n5A)

 * The talk discusses how container scheduling in a cluster can be optimized using logic derived from classic games Jenga and Tetris.
* Container scheduler's role is to find the optimal node for running a new container based on resource availability and predefined parameters.
* The scheduling process involves two steps: filtering nodes based on available resources and scoring each node based on several parameters.
* The scheduler may face challenges when available resources are insufficient or when there's fragmentation of resources in the cluster.
* An example of a real-world scenario is a three-node system with six containers running, where one node has high CPU usage while another has low memory usage.
* This imbalance can lead to performance degradation and potential application downtime.
* The talk suggests using techniques like container swapping or load balancing to maintain equilibrium in the cluster and avoid sudden resource imbalances.
* The speaker proposes using a real-time simulation of the cluster, such as a memory map, to identify the best strategy for placing containers.
* The talk mentions that even minor optimizations can lead to significant cost savings, as shown in a test run on a Kubernetes environment where auto-scaling was reduced, saving around $5000 per month.


## Lightweight and Fast WiFi Access in Virtual Machines - Jim Huang & En-Wei Wu

URL: [https://www.youtube.com/watch?v=CIXriWKqMV0](https://www.youtube.com/watch?v=CIXriWKqMV0)

 * The speakers, Jim Huang and En-Wei Wu, are from National Chang Kong University in Taiwan
* They will be talking about a lightweight solution for WiFi access in Virtual Machines (VMs) called vfi, which offers faster and easier deployment with fewer resources used compared to traditional solutions.
* Vfi is a lightweight wireless simulator that doesn't require a complex software stack or hardware. It simulates a virtual WiFi interface.
* The benefits of using a lightweight WiFi access solution include easier deployment in virtualized environments, reduction in resource usage, and faster performance.
* Traditional methods for setting up WiFi connectivity involve complex software stacks that can be time-consuming and costly. Vfi eliminates the need for these complex stacks by using a lightweight software stack.
* When running a VM with vfi, it becomes a wireless version of the driver, providing a wireless interface rather than an ethernet interface. This allows communication between VMs without the need for external hardware or drivers.
* The vfi software stack is much simpler than traditional solutions like Hardware SIM (Harare SC), Mac l211, and the Linux kernel's WiFi simulator. It works with a smaller subset of the L21 protocol and uses less memory consumption.
* In the data path, vfi makes use of the real device backend and Li data path for better performance. The data is transmitted directly without encapsulating it into LM1 frames.
* Vfi maintains a table storing Mac addresses within BSS to identify whether incoming frames belong to the desired BSS, and drops those that do not. This helps improve security by preventing unwanted traffic.
* Identifying the frame type is important for processing management frames. vfi doesn't manage management frames passed through the network protocol layer, so it identifies the type of frame and dispatches it accordingly.
* Comparing vfi to traditional solutions like Harare SC, vfi has fewer locks and less code, making it faster and more efficient. It also uses a MIT license rather than the GPL license used by Mac l211.
* Future work for vfi includes supporting multi-queue IO, reducing lock contention, increasing throughput, and allocating dedicated pages for reception to save time and make BFI faster.


## OpenTofu Project Overview - Kuba Martin & Roni Frantchi

URL: [https://www.youtube.com/watch?v=_-9LhcPgoaY](https://www.youtube.com/watch?v=_-9LhcPgoaY)

 * OpenTofu is a project announced by Kuba and Roni from the OpenTofu core team that aims to declaratively manage infrastructure using code
* The project was in response to HashiCorp's license change from open source to the Business Source License (BSL)
* The community expressed concern about the impact of the license change on the ecosystem and the future of Terraform as an open-source tool
* On August 14, 2022, the OpenTofu team published a manifesto urging HashiCorp to maintain the open source license or contribute the project to the Linux Foundation
* By September 12, 2022, the OpenTofu project was officially launched as a Linux Foundation project
* The project aims to provide a drop-in replacement for Terraform with similar functionality and ease of use
* Key features include:
  + Unit testing support for Terraform modules
  + Support for OCI registries
  + Custom registry implementation using GitHub redirector
* The team is also working on stabilizing the alpha version and polishing the user experience
* The project's goal is to ensure that the ecosystem remains open source and community-driven.


## Lightning Talk: Checking Your Project for Non-inclusive Language - Nico Rikken, Alliander

URL: [https://www.youtube.com/watch?v=ce66oDyXQ2g](https://www.youtube.com/watch?v=ce66oDyXQ2g)

 * Nico Rikken presented on checking projects for non-inclusive language
* He found the importance of checking for non-inclusive language in project presence
* He is a native Dutch speaker and looked up information on inclusive naming initiatives
* Linux Foundation has an inclusive naming initiative and a Slack channel for evaluation
* He checked several open source projects, which took quite some time
* He wanted automation to discover non-inclusive words and suggest alternatives
* He considered using regular expression or repurposing spell checkers like cspell
* He discovered a dedicated tool called "Woke" for checking non-inclusive language
* Woke suggests alternatives and gives explicit warnings, with options for filtering
* He wanted to expand the limited rule set and add specific jargon and energy sector words
* He suggested setting aside 30 minutes per week to check projects for non-inclusive language
* He encouraged everyone to manually or automatically check their projects for non-inclusive language.


## Servo Web Rendering Engine Reboot - Manuel Rego, Igalia

URL: [https://www.youtube.com/watch?v=9lkIX5ryZZ4](https://www.youtube.com/watch?v=9lkIX5ryZZ4)

 * Manuel Rego from Igalia, web platform team and Servo technical steering committee member, gave an update on Servo web rendering engine
* Servo is a top contributor to Chromium and Gecko projects, with a long definition focused on web rendering ending in Rust support, webdl, and cross-platform use
* Web rendering process explained as: parsing HTML and CSS, layout phase, painting, and compositing
* Rust programming language used for Servo due to memory safety and concurrency features
* WebGL support and experiments with modern graphics are ongoing
* Cross-platform work includes Linux, Mac, mobile devices, and embedded applications
* Servo's modular design allows easy integration into other projects as a webview library
* Embedded device support, such as Raspberry Pi, is planned for the future
* The project has been in development since 2001 and currently has around 140 contributors
* Future plans include prototyping Tower using Servo and focusing on CSS improvements.


## Workshop: Building and Managing an Open Source Program Office - Ibrahim Haddad, The Linux Foundation

URL: [https://www.youtube.com/watch?v=Po44mYILw94](https://www.youtube.com/watch?v=Po44mYILw94)

Split:[4571, 4570]
 * Ibrahim Haddad, Linux Foundation, open source expert
* Open Source Software Office (OSPO) transformation in organizations
* Open source everywhere: software, hardware, business models
* Advantages of open source: innovation, cost savings, strategic asset
* Case study: Samsung's open source journey
* Consuming open source components: compliance, licensing, infrastructure
* Contributing to open source projects: governance, culture, policy, incentives
* Building an OSPO: strategy, people, processes, tools
* Open source strategy templates: focus on projects, community, compliance
* Importance of documentation and communication
* Challenges in open source: scale, compliance, infrastructure, technical debt
* Resources for building an OSPO: research, surveys, templates, collaboration platforms.
 * Ibrahim Haddad from The Linux Foundation discusses building and managing an Open Source Program Office (OSPO)
* Different models for setting up an OSPO: corporate level, independent office, or virtual team
* Virtual teams consist of people from different units (marketing, legal, engineering) working together without a formal office
* Importance of having an OSPO to maintain open source projects and build an open source culture within a company
* Examples of companies with successful OSPOs: Microsoft, Google, IBM
* Challenges faced by companies in establishing and managing an OSPO: continuity, education, and respect for open source communities
* Benefits of having an OSPO: facilitating use and consumption of open source software, building an engineering focus on open source projects, and maintaining long-term relationships with open source communities.
* Ibrahim shares his experience setting up and running an OSPO at a large company, including the importance of education and communication, establishing clear guidelines and processes, and leveraging existing resources within the organization.
* Best practices for managing an OSPO: creating an open and collaborative environment, streamlining contribution approval processes, and providing training and mentorship opportunities for developers.



## Will Large-Scale Automated Scanning Stop Malware on OSS Repositories? - Zachary Newman

URL: [https://www.youtube.com/watch?v=QgISuuhBPhU](https://www.youtube.com/watch?v=QgISuuhBPhU)

 * Zach Newman discusses whether large-scale automated scanning can stop malware in open source software repositories
* He mentions his research background in applied cryptography and software repository security, specifically package signing, provenance, policy, and malware detection
* Malware detection methods include signature-based and behavior anomaly-based approaches
* Signature-based methods use a large list of known malware signatures to identify malicious files based on their hash values
* Behavior anomaly-based methods monitor software behavior for suspicious activity, such as sending credit card information to foreign servers or executing remote code
* Dynamic analysis involves running the software in a controlled environment (sandbox) to observe its behavior and detect malware
* Static analysis examines the source code without executing it to identify potential vulnerabilities
* Large-scale automated scanning can be effective for detecting known malware in open source software repositories, but may miss new or obfuscated threats
* Curated community-based repositories with strict access control and review processes are more secure than open repositories where anyone can submit packages
* False positives and false negatives are concerns with automated scanning tools
* Human intervention is necessary for accurate malware detection and response.


## Greening the AI Cloud: Validating Power Models for Kubernetes Containers - Marcelo Amaral

URL: [https://www.youtube.com/watch?v=nqgcKTlbsqY](https://www.youtube.com/watch?v=nqgcKTlbsqY)

 * Marcelo Rao from IBM Research Tokyo presenting on measuring energy consumption in application clouds
* Motivation: Climate change is impacting human activity and increasing greenhouse gas emissions, which contributes to global warming and environmental damage. Companies are looking for ways to minimize energy consumption and reduce emissions.
* Introduction to Kepler, an open source project recently accepted into the Cloud Native Computing Foundation (CNCF) Sandbox that measures energy consumption at various levels in a containerized environment (container, pod, job, node).
* Kepler uses BPF (Berkeley Packet Filter), a kernel extension that allows collecting metrics without requiring a kernel recompile, to collect power consumption data from the operating system and virtual machines.
* Different deployment scenarios:
  * Best-case scenario: Accessing accurate power matrices to calculate energy consumption per container
  * Current public cloud scenario: Using pretrained power models to estimate energy consumption per VM or container
  * Future infrastructure perspective: Cloud providers using Kepler to expose energy consumption metrics accurately and efficiently
* Limitations of power models: They may not cover everything, especially offline workloads, and there is a need for transparent reporting and understanding of the underlying power estimation methods.
* Idle power: Two definitions - constant idle power (machine energy consumption without considering load) and dynamic idle power (increasing energy consumption due to load).
* Kepler uses different regression algorithms to create more accurate power models.
* Earth ML Perth benchmark tool is used for analyzing machine learning workloads and comparing performance across different systems.
* Deploying Kepler using Helm, which is a popular package manager for Kubernetes.
* Consolidating workloads on energy-efficient nodes to improve overall efficiency.
* Changing CPU frequency to optimize power consumption based on the workload.
* Using different visualization tools like Grafana for monitoring and analyzing energy consumption in real-time.


## Establishing Trusted and Secure Foundation for Device Management Using Open... - Tushar Khandelwal

URL: [https://www.youtube.com/watch?v=sNIE9Wx2wGg](https://www.youtube.com/watch?v=sNIE9Wx2wGg)

 * Agenda: Discussing IoT device management and the role of attestation in establishing a secure foundation
* Tushar Khandelwal, Principal Software Engineer at ARM, speaking
* ITF (Industrial Internet Consortium) Rat architecture standard for IoT device management
* Attestation: Establishing trustworthiness through trusted execution environment
* Device claiming identity and producing evidence (attestation token)
* Relying party verifies attestation token to decide if they trust the IoT device
* Key Management: Provisioning keys at different stages
* Passport Model: Interaction pattern between relying party, tester, and verifier
* Verizon's Wakama used in POC for verification
* Different services involved: provisioning, verification, and communication
* Lightweight M2M protocol used for secure device-to-server communication
* IoT Device architecture includes secure enclave, security engine, and normal world (Linux)
* Platform Security Architecture (PSA) guidelines for building firmware to ensure platform security
* Demonstration of token verification process using TLS handshake and FPGA board.


## Scaling the Security Researcher to Eliminate OSS Security Vulnerabilities Once... Jonathan Leitschuh

URL: [https://www.youtube.com/watch?v=x-LvwZOOvtU](https://www.youtube.com/watch?v=x-LvwZOOvtU)

 * Jonathan Leitschuh, senior software security researcher at Project Alpha Omega and Dan Kaminsky Fellow, discussed his experience finding and fixing open source security vulnerabilities
* He started by discussing the Polarquest vulnerability he discovered in the Java ecosystem, which affected multiple organizations including Spring, Apache Software Foundation, Red Hat, and Oracle
* The vulnerability was caused by using HTTP instead of HTTPS to resolve dependencies, allowing attackers to hijack build machines or CI pipelines
* Leitschuh generated 164 Polaris CVEs to address this issue and pushed for the decommissioning of Maven Central's support for HTTP
* He also discussed other vulnerabilities he discovered through code scanning using tools like CodeQL, such as a vulnerable regular expression in GitHub's Hub CLI
* Leitschuh emphasized the importance of automation and targeted transformations to address vulnerabilities at scale in open source ecosystems, using abstract syntax trees and targeted code modifications
* He also discussed the need for maintainers to be aware of security vulnerabilities and the importance of data flow analysis to uncover potential issues
* Leitschuh shared his experience with vulnerability disclosure and the challenges of coordinating fixes across organizations and open source projects.


## Building On-Ramps for Non-Code Contributors in Open Source - Natali Vlatko & Celeste Horgan

URL: [https://www.youtube.com/watch?v=1s6imxKnWL4](https://www.youtube.com/watch?v=1s6imxKnWL4)

 * Celeste and Natalie are open source contributors with experience in Kubernetes and Apache projects.
* They spoke about onboarding non-technical contributors to open source projects.
* The willingness of maintainers to accept help is a prerequisite for getting non-technical contributors involved.
* Non-technical contributors can help with tasks such as bug triage, documentation, succession planning, and project management.
* Communication and onboarding processes in open source projects are different from enterprise projects.
* The importance of mentoring and buddying programs for new contributors.
* Non-technical contributors can own work and be part of the team.
* Projects that provide stability and a clear contribution path attract non-technical contributors.
* Real-time communication through office hours or other channels is important for non-technical contributors.
* People are often afraid to ask questions or take up people's time in open source projects, so making yourself available to answer questions is helpful.
* Non-technical contributors bring valuable skills and perspectives to open source projects.
* The importance of having a welcoming environment and a clear contribution process for non-technical contributors.
* Open source projects can benefit from having diversity in contributors.
* Small projects with strong technical backgrounds can sometimes have a chicken neck problem, making it hard to attract non-technical contributors.
* Technical discussions should be willing to explain concepts clearly to non-technical contributors, rather than diving too deep into specific features.
* Non-technical contributors can gain experience and learn new skills by working on smaller open source projects.
* Unconscious bias and gatekeeping can prevent diversity in open source projects.
* Companies can benefit from encouraging a developer open source mentality and getting people involved in open source projects.


## Automated & Observable Deployments with Flux + Keptn - Priyanka Ravi, Weaveworks

URL: [https://www.youtube.com/watch?v=3psfxO8PBXE](https://www.youtube.com/watch?v=3psfxO8PBXE)

 * Priyanka Ravi, developer experience engineer at Weaveworks, introduces Flux and Keptn
* Flux is a GitOps tool for automating Kubernetes deployments and managing infrastructure using Git as the single source of truth
* Keptn is a Continuous Delivery platform that uses Flagger for canary releases and rollouts
* GitOps principles: system managed, desired state stored in version control, immutable, and software agent observes actual state
* Benefits of using GitOps: stronger security, increased productivity, better developer experience, and reduced burden
* Flux is a package manager for Kubernetes and other cloud-native platforms that uses Git as the source of truth
* Flux supports multiple Git providers like GitHub, GitLab, Bitbucket, S3 compatible buckets, and major container registries
* Flux can be used with popular tools like Helm, RBAC policies, OPA, Kyverno admission controller, and more
* Keptn provides a Cloud Native observability feature that supports Open Telemetry and gives insight into the deployment process
* Captain, maintained by Florian Grunow from Dynatrace, is a lifecycle toolkit for Kubernetes applications
* Goals of using Captain: allow minimal configuration effort, support existing application manifest order, and integrate with GitOps workflow
* Captain supports pre- and post-deployment tasks, evaluations, and notifications. It also provides deep insight into the deployment process and supports open Telemetry tracing.


## Sponsored Session: The Search for Transparency and Accountability in the Age of... - Ezequiel Lanza

URL: [https://www.youtube.com/watch?v=B4GWnUdk_l4](https://www.youtube.com/watch?v=B4GWnUdk_l4)

 * Ezequiel Lanza talks about responsible AI and explainable AI
* Responsible AI: fairness, transparency, accountability, privacy
* Fairness: ensure equally distributed toppings in a pizza analogy
* Transparency: publish model recipe, share data dealings with data protection
* Accountability: replace biased pixels in the model, ask for preferred topping
* Privacy: protect data instance from fraud detection systems
* Explainable AI: explain decisions made by the model like a human would
* Four principles of responsible AI: fairness, transparency, accountability, privacy
* Explanation tools and techniques: bias detection, data documentation, interpretability
* Use multiple tools depending on use case and target audience
* Regulation requirements for explainable models: GDPR, Uber flow detection system
* Model explainability: remove bias, understand model workings, improve performance
* Different approaches to explaining complex models: parallel models, ensemble models
* Importance of understanding user perception and knowledge level
* Collaboration between humans and AI in explanation process
* Value proposition of explainable AI: meet requirements, encourage community, reduce gaps
* Multiple models for different industries: healthcare, finance, etc.
* Centralize tools and data for efficient collaboration and explanation
* Large language models: handle a variety of use cases, need careful consideration for ethics
* Add extra layers to avoid racist or biased models.


## FORK IT ALL if You Fork It - Daniel Doubrovkine, AWS

URL: [https://www.youtube.com/watch?v=B8NlDg_Mevw](https://www.youtube.com/watch?v=B8NlDg_Mevw)

 * Daniel Doubrovkine from AWS talks about his experience working on an open source project, Elasticsearch, and the decision to fork it into OpenSearch
* Problem of downstream dependency troubles in open source projects, especially when a company relies on it for their business
* Case of Elasticsearch being forked by AWS due to licensing concerns
* Benefits of open source software for businesses and customers
* Challenges in forking open source projects, such as trademark issues and community engagement
* Importance of having a clear governance process and communication within the project
* OpenSearch's success and its impact on the security vulnerability with log4j
* Lessons learned from the experience of forking Elasticsearch into OpenSearch.

Here are some specific points:
- Companies often rely heavily on open source software for their business, but can face challenges when the upstream project changes.
- AWS faced this issue when they used Elasticsearch, which was under a nonopen source license. They decided to fork it and create OpenSearch.
- Open source software offers benefits like flexibility, customizability, transparency, and community involvement for both businesses and customers.
- Challenges in forking open source projects include trademark issues, organizational structures, and community engagement.
- In the case of OpenSearch, AWS had to navigate legal concerns, create a new project organization, and engage with the open source community.
- The log4j security vulnerability affected many software deployments, including those using OpenSearch. AWS was able to respond quickly by releasing patches and updates.
- Lessons learned from the experience of forking Elasticsearch into OpenSearch include the importance of clear governance processes, community engagement, and transparency.


## Asymmetries in Open Source: What Can Research Tell Us about Closing the... - Adrienn Lawson

URL: [https://www.youtube.com/watch?v=DwQB6pwMgVw](https://www.youtube.com/watch?v=DwQB6pwMgVw)

 * Adrienn Lawson, data analyst at Linux Foundation Research, discusses the consumption and contribution gap in open source
* Survey covered many regions worldwide to examine current level of open source usage and contribution patterns within organizations
* Objective was to identify inhibitors and motivators for organization's willingness to contribute to open source projects
* Key findings:
  + Open Source is widely used, with widespread significant and moderate use in organizations
  + Development teams are responsible for open source use within companies (around 70%)
  + Open source contribution policy varies, with some organizations having a clear strategy (50-60%)
  + Europe has a more encouraging conception of open source contribution compared to the Americas
  + Organizations tend to check activity levels before deciding whether to use open source instead of proprietary software
* Other findings:
  + 48 organizations contributed code to open source projects, with European organizations contributing more
  + Time spent on personal contributions varies widely, with some people working over 40 hours per week
  + Employers are becoming more supportive of employee open source contribution
  + Organizations see value in open source, with software quality being the most common benefit mentioned
  + Open source contributes to innovation and moral obligation for many organizations.
* Challenges include legal licensing concerns and lack of investment return, as well as time constraints.
* European countries are seen as having a special role in advancing open source and improving sustainability.
* The Linux Foundation Research team will continue to share data on dataworld for reproduction.


## Map of Science: A UI for Open-Source Science - Alexy Khrabrov & Tim Bonnemann, IBM Research

URL: [https://www.youtube.com/watch?v=Elq2K7MDqDI](https://www.youtube.com/watch?v=Elq2K7MDqDI)

 * Alexy Khrabrov and Tim Bonnemann from IBM Research explain the Open Source Science initiative
* Motivation: Scientists need open source tools, but they don't always know where to find them or how to connect with developers
* Goal: Accelerate science by producing software that scientists can use efficiently
* Overview of Open Source Science project at IBM: Community-centric, focusing on connecting scientists and open source developers
* Examples of popular open source projects in data science (Scipy, TensorFlow, NumPy) and machine learning (CircleLearn, Panda)
* Challenges: Finding the right people, understanding their needs, and efficiently exchanging information
* Opportunities: Government funding initiatives (NSF, Horizon 2020), conferences, and open source software communities
* Benefits: Reproducible science, collaboration, and recognition for contributors
* Strategy: Building a map of open source tools in various scientific domains to make discoverability easier
* IBM's role: Providing resources and facilitating connections between scientists and developers.


## For Want of a Nail: Industry Analyst Lessons Learned on the State of Software Dev... - Jon Collins

URL: [https://www.youtube.com/watch?v=G-n4iHExXsE](https://www.youtube.com/watch?v=G-n4iHExXsE)

 * Jon Collins, industry analyst, spent 15 years in software development and IT consulting
* Talks about the evolution of software development and industry trends
* Discusses the importance of understanding organizational speak versus marketing buzzwords
* Mentioned working at Sun Microsystems and involvement with Linux in the late 80s
* Became an industry analyst to have time to think instead of constantly running meetings
* Talks about the challenges of supply chain management in software development
* Discusses the impact of AI on various areas like security, ops, and value stream management
* Mentioned working with Daryl, who emphasized automation
* Talks about the importance of cost control and managing complexity in software development
* Discusses the changing role of cloud computing and the concept of multicloud and hybrid architectures
* Emphasizes the need for efficient processes and effective value stream management
* Mentioned the challenge of dealing with legacy systems and imposter syndrome in development
* Talks about the importance of understanding business needs and the role of technology in meeting those needs.


## AO.Space: An Open Source Solution for Personal Data Ownership - Wang Jianmin

URL: [https://www.youtube.com/watch?v=IjCiYb7rypg](https://www.youtube.com/watch?v=IjCiYb7rypg)

 * The speaker, Timi, is an engineer from the Institute of Software Chinese Academy of Sciences and attended the Linux Foundation Summit Europe in April 2019.
* He introduced his open source project called "Space" which aims to protect personal data ownership.
* His inspiration for creating Space came from concerns about privacy when using digital services, especially regarding cameras in his daughter's room and social media platforms.
* He identified three main issues: security, dependency on centralized platforms, and loss of ownership in the digital world.
* Timi discussed his vision of a decentralized internet based on World Wide Web principles and how Space aims to address these issues.
* The project uses a decentralized identifier system and public-private key design for account security and ownership representation.
* It also includes document signing and history, multi-factor authentication, and data encryption.
* Timi mentioned the importance of open source technology in protecting personal data and the potential integration of hardware and software solutions.
* He discussed some challenges, such as the need for distributed architecture and network design, as well as reducing dependency on third-party services.
* Towards the end of his talk, Timi shared related projects like PASKI and the Open Source Hardware community and invited listeners to join the Space project.


## Emulating Devices in Linux Using Greybus Subsystem - Vaishnav Mohandas Achath, Texas Instruments

URL: [https://www.youtube.com/watch?v=O2VsqYwGfwE](https://www.youtube.com/watch?v=O2VsqYwGfwE)

 * Vaishnav Achath from Texas Instruments discussing emulating devices in Linux using the Graybus subsystem
* Overview of using Graybus for device emulation, focusing on use cases like automated testing and subsystem-level bug fixing
* Emulating devices in Linux: reproducing functionality of actual device software without requiring access to the actual hardware
* Existing methods for emulating devices include network access and behavioral models
* Graybus allows emulating complex systems with multiple peripherals, including USB devices
* Graybus is a strong root within the Linux kernel, keeping intelligence within the host
* Graybus operates using transactions between virtual controllers and remote devices, with the application processor sending RPC calls to remote modules
* Emulating an I²C controller: Graybus package transaction, virtual controller sends operation to remote device, remote node returns result
* Use case: modular smartphones with Internet of Things (IoT) applications and multiple nodes spread across a deployment system
* Emulation challenges for complex modules like cameras can be addressed by emulating the camera control interface and data interface separately
* Graybus design concept: bundling multiple controllers together as entities, like the CSI-2 interface for cameras
* Graybus operation: small header with message ID used to track response, transaction performs operation on host processor
* Implementing a handler in user space: storing context and sending responses back
* Testing virtual devices using standard Linux libraries and APIs
* Use case: testing an I²C GPA controller using Python and the libgpiod API
* Creating fake devices: no need for lower-level firmware development on the remote controller side, keeping intelligence within the host
* Emulating a GPS controller with a virtual emulated GPS device
* Testing the entire system with a virtualized car seat base called I²C 10 device using the new device API
* Probing a device driver: creating a virtual bus and handling device transactions like reading sensor values using standard utilities
* Emulating sensors: returning random values for testing purposes, emulating register values in user space.


## Puzzlefs - the Next-Generation Container Filesystem - Armand-Ariel Miculas, Cisco Systems

URL: [https://www.youtube.com/watch?v=OhMtoLrjiBY](https://www.youtube.com/watch?v=OhMtoLrjiBY)

 * Ariel Nicolas, teaching assistant and master degree candidate in cyber security at Cisco Systems
* Talks about Puzzle FS, a next-generation container file system
* Mentioned LCI (Linux Container Initiative) and its drawbacks
* Goals: reduced duplication, reproducible image builds, direct mounting support, data integrity, memory safety
* Uses content defined chunking for solving boundary shift problem
* Uses CDC algorithm for faster duplicate detection and hash calculation
* Wants canonical representation of file systems for reproducing images
* Prevents tampering with B3 Maps
* Wants direct mounting support without extraction step
* Wants a simple enough format for kernel decoding
* Implements Rust FUSE driver for memory safety and eliminating undefined behavior
* Discusses challenges during implementation, such as dependency on third-party crates and Linux kernel differences
* Demonstrates usage of the file system with a quick demo.

The transcript describes Ariel Nicolas' presentation about Puzzle FS, a next-generation container file system developed by Cisco Systems. The goal is to solve issues in the current Linux Container Initiative (LCI) and improve reproducibility, reduce duplication, provide data integrity, and memory safety for container builds. Puzzle FS uses content defined chunking, the CDC algorithm, and B3 Maps to achieve these goals while also making it easier to integrate with the kernel and prevent tampering. Ariel demonstrates a quick implementation of the file system using Rust and FUSE, highlighting its benefits and challenges.


## Expanding the Capabilities of LLMs Through Community Collaboration - Antonio Fernández & Jose García

URL: [https://www.youtube.com/watch?v=Osokwmcw41Q](https://www.youtube.com/watch?v=Osokwmcw41Q)

 * Antonio Fernández and José García discuss the role of Open Source LLM (Large Language Model) community in expanding capabilities
* They work at Alaska Cloud, an elastic rotation data engineering company focusing on Open AI and Microsoft Partners ecosystem
* Open Source LMs have evolved from private to public development due to community effort and open source libraries like TPT
* Breakthroughs achieved in the beginning of Open AI led to marketing stunts and concerns about regulation as potential competitor
* LLMs can be used for various tasks, including data mining and text summarization, but have limitations such as token input limit
* LLMs can make embeddings from text and find closest similar subjects, but require large datasets and processing power
* Integrations with other tools like vector databases and search engines enhance the ecosystem and make implementation easier
* Developers face challenges in working with LLMs due to knowledge capability limitations and lack of finetuning options
* Python is a popular language for implementing LLMs, while tools like Lama Index and Clutter API simplify implementation
* Open Source LLMs have led to new applications and evolution, such as Auto GPT ordering food or interacting with databases
* The community continues to grow and develop new tools and solutions, making the ecosystem much bigger than before.


## A Milestone for Open Source Security: How the Brand New ISO... - Katharina Grauf & Marcel Scholze

URL: [https://www.youtube.com/watch?v=QUEpiM_yf9I](https://www.youtube.com/watch?v=QUEpiM_yf9I)

 * Speaker: Katarina Grauf from PWC Germany, discussing ISO 18974, the new standard for open source security management
* ISO 18974 is a sister standard to ISO 5230, which focuses on license compliance in open source software
* ISO 5230 has been successful in defining open source compliance processes for organizations and reducing risk in supply chains
* ISO 18974 offers standardization and transparency in managing open source security risks
* Open source security is becoming increasingly important due to the growing complexity of software supply chains and recent high-profile vulnerabilities
* ISO 18974 provides a foundation for implementing an open source security management system, including policy definition, competency development, and incident response measures
* The certification process for ISO 18974 involves document review and approval, requirement adherence, and certification of the open source security management system.
* SBOM (Software Bill of Materials) is a crucial element in managing open source license compliance and security risks
* ISO 18974 can be seen as a stepping stone towards implementing other ISO security standards
* The synergy between ISO 5230 and 18974 allows organizations to harmonize their processes and implement them more effectively.


## Kubernetes Meets Confidential Computing - The Different Ways of Scaling Sensitive... - Moritz Eckert

URL: [https://www.youtube.com/watch?v=RTaXTgiP74c](https://www.youtube.com/watch?v=RTaXTgiP74c)

 * Morris Eckert, architect at agile system startup in Bochum, Germany, talks about confidential computing
* Confidential computing is focused on securing data by protecting it in memory and in use, beyond encryption
* Hardware feature called trusted execution environment (TEE) allows isolating code and data from the rest of the system
* Intel SGX was the first implementation of TEE, but it has performance overhead due to its small context
* Next-generation implementations like AMD Secure Processor (ASP) or Intel TDX provide better interface for running applications
* Confidential computing is important in cloud environments, especially for infrastructure security and multiparty scenarios
* Infrastructure security: protect shared resources and third-party services from unauthorized access
* Multiparty scenario: implement privacy-preserving AI solutions that protect the model owner's IP
* Supply chain security: ensure trust in software and hardware components
* Challenges for confidential computing include orchestration, performance, and compatibility with existing systems
* Confidential Computing is gaining traction in highly regulated industries like finance and healthcare.
* Three approaches to implementing confidential computing: SGX-based solution, confidential VMs, and Constellation project
* SGX-based solution: process-based isolation using Intel SGX
* Confidential VM: entire virtual machine is isolated, including the control plane
* Constellation project: isolating infrastructure from the cloud service provider
* Performance overhead is a concern with confidential computing, but it can be mitigated through hardware optimizations.
* Monitoring challenges in confidential computing environments due to isolation and lack of full observability.


## Growing the Chain: Trusting Build Provenance from Userspace - Billy Lynch, Chainguard

URL: [https://www.youtube.com/watch?v=U7knb0DHoBk](https://www.youtube.com/watch?v=U7knb0DHoBk)

 * Billy Lynch from Chainguard discussing trust in Providence, a concept gaining traction in supply chain security
* Providence refers to metadata and identity used for attestation in the software development process
* Importance of trusting software and signals that can indicate trustworthiness (e.g. reliable sources, vulnerability scans, signatures)
* Providence is a way to assert who made a claim and provide precise information about the build process and artifact
* Challenges in trusting Providence include identity management and ensuring correctness of data generated by CI pipelines
* User space vs system space approaches to generating Providence: user space generates metadata, system space manages control plane and makes assertions
* Examples of tools and projects using Providence: GitHub Actions, Tecton Chain, sigstore
* Importance of defining trust boundaries and enforcing security in open source projects and build environments.
* Automating signature checks for container images is a good example of Providence in action.
* Reproducible builds and the importance of ensuring consistent output from given input.
* Salsa, a project attempting to define levels of trust in the build process, with level one being the most basic (documented build process) and level four being fully automated.
* The tradeoff between security and convenience, as every release may require additional compute resources.
* The importance of identifying reproducible builds and using consistent reference points for comparison.


## Panel Discussion: The Impact of the CRA on the... - Cheukting, Mirko & Greg, Laura, Justin, Philip

URL: [https://www.youtube.com/watch?v=Wx-vwgOZSFk](https://www.youtube.com/watch?v=Wx-vwgOZSFk)

 * Discussion about the Cyber Resilience Act (CRA) and its impact on open source software
* Panelists include representatives from Microsoft, Erickson, Open Source Initiative (OSI), and others
* CRA aims to reduce vulnerability in digital products by ensuring cyber security is maintained throughout their life cycle
* It applies to both commercial and non-commercial entities, but there are exceptions for open source development and charities
* Key provisions include reporting and fixing covered vulnerabilities, providing software updates, and undergoing audits and certifications
* There are concerns that the CRA could inhibit scientific research and impose a major burden on small organizations
* The definition of commercial activity is ambiguous and may affect individual developers and occasional open source contributors
* The CRA applies to high-risk critical products, which explicitly include foundational technologies like operating systems and container runtimes
* There are proposed amendments to address concerns around the impact on open source development, but it's still a work in progress
* Some panelists believe that the CRA could lead to fewer contributions to upstream projects, as well as discourage internal contributions due to legal concerns.
* Others see it as a positive step towards improving cyber security and bringing regulatory clarity to the software industry.


## Ostree for the Uninitiated - What You Need to Get Up and Running with Ostree on Your...- Davis Roman

URL: [https://www.youtube.com/watch?v=_CwGUt0CpvU](https://www.youtube.com/watch?v=_CwGUt0CpvU)

 * Davis Roman, an engineer with experience in home security and automotive industries, discusses getting started with Ostree on Raspberry Pi 4
* Prerequisites: understanding of package versus image versus differential upgrade, different Ostree architecture for embedded Linux devices
* Package vs Image vs Differential Upgrade:
  * Package-based upgrade: RPM, YUM, advantage: low bandwidth, easy use, disadvantage: requires full system download even for small changes
  * Full system upgrade: ext4 squashfs image, advantage: tested exhaustively, disadvantage: consumes excessive network data and storage
  * Atomic differential upgrade: Oilstream, advantage: minimal network bandwidth, power save, smaller difference files, faster update time, disadvantage: requires reboot
* Different Ostree Architecture:
  * OTA update client connects to public Ostree server, pulls summary file, monitors for new commits, and deploys new commit offline
  * Advantages: simple, straightforward path, fine-grained control over device updates, limited exposure to bad updates
  * Disadvantages: lack of strict control over which commit gets downloaded onto specific device
* Setting up Ostree on Raspberry Pi 4 using OCTA project
* Pushing OSG server and using Htop package for custom Linux distribution
* Distributed option: local area network peer-to-peer update scheme using MDNS (Multicast DNS) and collection IDs
* Booting a new commit offline using static deltas and applying static delta files manually.


## Minimalist Best Practices in Kubernetes Operators - Jonathan Berkhahn, IBM

URL: [https://www.youtube.com/watch?v=bNzfbOVbdOo](https://www.youtube.com/watch?v=bNzfbOVbdOo)

 * Jonathan Berkhahn from IBM discussing minimalistic best practices in Kubernetes Operators
* Operator is a complex topic, but can be summarized as replicating exact workflows in Kubernetes using custom resource definitions (CRDs) and controller implementations
* CRD specifies API for user interaction to create new resources, while controller implements the logic to make things happen in the cluster
* Operator SDK is a helpful tool for generating operator scaffolding
* Keep it simple by avoiding unnecessary complexity and following best practices like using filters and event predicates to reduce traffic and improve performance
* Minimize API load on controllers and ensure good citizenship in the cluster
* Watch out for security vulnerabilities and be aware of container image size and complexity
* Namespace scope operator is a good option for managing multiple clusters or namespaces, but consider scalability implications
* Testing operators is important, and tools like Scorecard can help with integration testing
* Use filters to manage resources in specific namespaces, and be aware of the impact on reconciliation loops and resource usage
* Be mindful of custom resource dependencies and the impact on controller design
* Avoid annotation-based configuration and use the declarative style of Kubernetes instead.


## IMA Namespaces for Containers - Asier Gutierrez, Huawei

URL: [https://www.youtube.com/watch?v=bs7EcuF4SSo](https://www.youtube.com/watch?v=bs7EcuF4SSo)

 * Asier Gutierrez from Huawei talks about container security and IMA (Integrity Measurement Architecture) in Linux
* IMA is a Linux security module that ensures file immutability by comparing hashes of files upon opening
* It uses LSM (Linux Security Module) hooks to check whether the hash of a file matches the previous session's hash
* IMA works along with TPM (Trusted Platform Module) chip for added security
* TPM is a cryptographic chip that can generate keys, perform remote attestation, and maintain a chain of trust
* The speaker mentions IBM engineers who created an IMA namespace-based solution for container security called LKN
* The new approach uses virtual PCRs (Platform Configuration Registers) inside containers to emulate real hardware PCRs
* The activation of the IMA namespaces is linked to the username space number, providing an advantage over a shared key ring
* The speaker explains how the IMA measurement list works and how it identifies containers using cpcrs and TPM chip
* He also talks about the importance of maintaining trust in containers and preventing unauthorized access to the root file system or host
* The speaker mentions that running containers in a cloud environment requires changes to the control plane, API server, container runc, and interface.
* The IMA namespaces are created by the user space kernel when creating a container, with the regular flow continuing after that.
* The speaker talks about some challenges, such as the need for a change in the API, the lack of specification of a username space in certain cases, and the issue of non-overlapping policies.
* He also mentions that using external storage like NFS can pose issues with IMA due to its stateless nature and the inability to provide extended attributes for IMA hashes.
* The speaker encourages collaboration and contribution to the kernel community to improve container security.


## BoF: How to Build a Tech Community: The Fine Art of Organizing Meetups - Juan Manuel Perafan, Xebia

URL: [https://www.youtube.com/watch?v=e7cGqsqLkmU](https://www.youtube.com/watch?v=e7cGqsqLkmU)

 * Juan Manuel Perafan, born in Colombia, now based in the Netherlands, works at Xebia and has a passion for organizing meetups and building communities
* Started organizing meetups in 2011 after realizing he had a knack for it during his student days
* Attended a Meetup in 2018 that inspired him to become an organizer, as he saw room for improvement
* Organized Amsterdam Data Visualization Meetup in 2018 and has since organized several other meetups
* Reasons for organizing meetups: marketing (low cost with potential for large attendance), leadership development (practice project management, networking, public speaking), and networking (meeting peers and learning new ideas)
* Tips for organizing a successful meetup: determining the topic (broad vs. specific), creating an identity, using Meetup.com platform, finding a venue and speakers, marketing the event, and ensuring attendee engagement.


## The Compiler Plugin Framework to Facilitate Customized Compilation... - Yongnian Le & Mingchuan Wu

URL: [https://www.youtube.com/watch?v=fqunF73F1Yg](https://www.youtube.com/watch?v=fqunF73F1Yg)

 * The speakers are architects from the GCC compiler team and the Open OLA community, discussing a customized compilation development session focusing on the Plugin Framework Compiler (Pink).
* Pink is a framework that aims to facilitate collaboration between different compiler teams, reduce development effort, and provide ecosystem compatibility.
* The speakers introduce Open OLA as an open-source operating system and its compiler team's mission to improve GCC performance, leadership, and specific scenarios.
* They discuss the need for a plugin framework due to the growing popularity of arm processors, cloud services, and the burden on developers to change whole architectures or write repeated code for different compilers.
* The challenges addressed by Pink include compatibility issues, logging, integrity verification, and the effort required to create and maintain multiple plugins for various compiler infrastructures.
* The framework aims to standardize plugin interfaces, provide common capabilities, and improve collaboration between developers.
* Key features of Pink include a server-client design, IR decoupling, and compatibility verification through an API and interface standardization.
* Potential future developments for the framework include debugging capabilities, improved collaboration, and support for multiple levels of logging and energy efficiency.
* The speakers emphasize the importance of community contributions to the framework and encourage collaboration between developers.


## How SteamOS is Contributing to the Linux Ecosystem - Alberto Garcia, Igalia

URL: [https://www.youtube.com/watch?v=h7YbqrJ0_nM](https://www.youtube.com/watch?v=h7YbqrJ0_nM)

 * Alberto Garcia from Igalia talks about SteamOS contributing to the Linux ecosystem
* Steam Deck is a gaming device released by Valve last year, running on SteamOS
* SteamOS is based on Arch Linux with some customizations
* Regular user has complete access to the operating system and can install any software, including non-Steam games
* SteamOS includes Proton, which runs Windows applications on Linux using Wine compatibility layer and Vulkan
* Several open source projects have been developed or contributed to by Valve and the community for SteamOS, such as Wine, Vulkan, and Proton
* Some improvements have been made to address specific Linux compatibility issues in games, like implementing missing Windows APIs and file system features
* SteamOS is actively developed and maintained by both Valve and the open source community.


## Overcoming I/O Bottlenecks in LLM Training with Open-Source Distributed... - Lu Qiu & Jasmine Wang

URL: [https://www.youtube.com/watch?v=kG2Hh32slBM](https://www.youtube.com/watch?v=kG2Hh32slBM)

 * The speaker, Jasmine, is a machine learning engineer and open source project member of Alexio, an open source distributed data caching system.
* Alexio started as a UC Berkeley research project in 2014 and has grown to have over 11,000 contributors and 13,000 community members.
* It's used by companies like Meta and Uber for serving AI data platforms and improving performance.
* In the era of large language model training with vast amounts of data, data readiness is crucial for high scalability, availability, and performance.
* Data access patterns can vary greatly based on the type and size of files, leading to different performance-oriented caching strategies.
* For example, large structured files like Arrow files may have sequential risk and benefit from position reads, while many small semistructured or unstructured files may have evenly distributed read access.
* The recommended strategy depends on the traffic pattern, which can be either performance-oriented (computer-like) or capacity-oriented (cloud-friendly).
* Performance-oriented strategies prioritize low latency and high throughput, while capacity-optimized strategies focus on large file sizes and reducing API calls.
* One performance-optimized strategy is to preload data instead of loading it from public storage each time, which can reduce request rates and replication issues.
* Another strategy is to optimize position read rates by reading larger chunks of data at once or using local caching for smaller files.
* Alexio provides a distributed caching layer that helps fetch data quickly from cloud storage, serving as a unified caching layer for machine learning infrastructure in hybrid multicloud environments.
* In such environments, the training platform and serving cluster can be separated with a middle storage system to optimize performance and reduce network congestion.
* By integrating cache into AI training platforms, data access latency can be significantly reduced, improving overall performance and reducing costs.
* Evaluating different read strategies, such as position reads versus streaming reads, can lead to better performance depending on the specific dataset and use case.


## Strace - Swiss Army Knife to Trace, Analyze, RT Debug - Harald König, Bosch Sensortec GmbH

URL: [https://www.youtube.com/watch?v=l1LkWUbCEKY](https://www.youtube.com/watch?v=l1LkWUbCEKY)

 * The speaker introduces himself and shares his background with Linux and open source software
* He talks about tracing and analyzing system calls using the tool 'estrace'
* Estrace is based on ptrace, a system call used for debugging control of another process
* It can be used to trace multiple commands and show their execution time, process IDs, and system calls
* The speaker describes how to use strace and estrace with examples
* He mentions that estrace can produce a lot of output and suggests using filters and output files for better analysis
* The speaker also discusses the importance of understanding timestamps in tracing and analyzing system calls.


## DIY Private Container Registry - Márk Sági-Kazár, Cisco

URL: [https://www.youtube.com/watch?v=lYpuwZ-m6Tw](https://www.youtube.com/watch?v=lYpuwZ-m6Tw)

 * Mark Sági-Kazár from Cisco's Innovation Lab discusses the story behind working on container registries
* Initially, he wanted to validate an idea of deploying a container image in a partner environment with minimal operational burden
* He looked into using cloud hosting solutions like Docker Hub and GitHub Container Registry but found them less flexible for authorization
* Peer-to-peer registries were another option, but they didn't fit his specific use case
* He chose Cloud Rusty Registries due to its ease of setup and lower operational cost
* However, he encountered challenges like managing robot accounts, group-based access, and API integrations
* As the project grew, new requirements emerged, such as subscribing to software through a self-serve portal and onboarding customers
* He eventually decided to build something similar to Harbor but with external authorization options
* OCI distribution specification doesn't include an authentication solution, so he had to implement it separately using token-based authorization
* The authorization service communicates with the registry to grant or deny access based on the presented token.


## Building Knowledge Graphs - Sumit Pal, Ontotext

URL: [https://www.youtube.com/watch?v=myH1fRk3F7Y](https://www.youtube.com/watch?v=myH1fRk3F7Y)

 * Sumit Pal from Onotext discusses knowledge graphs
* Knowledge graphs gained popularity since 2010s, used for connecting people, data integration, and fraud detection in financial organizations
* Data scientists use graph databases for managing connections and relationships between data points
* Graph databases are different from relational databases, providing extra insight for fraudsters' cohorts and networks
* Knowledge graphs cover various domains such as supply chain, deadlock detection, and compiler data structures
* Google uses knowledge graphs for search engines and semantic search
* Knowledge graphs help in entity resolution and disambiguation, following standard ontology taxonomies
* Knowledge graphs are useful in data management, especially for unstructured content like text data
* Data integration is a challenge with various data silos and need to be meaningfully tied together
* Enterprise knowledge graphs help model specific domains and validate data against regulatory requirements
* Knowledge graphs can be used for reasoning and inferencing, providing new facts from existing data
* Taxonomies provide a hierarchical structure and help minimize ambiguity, with tools like Protege and RDFS available for building ontologies.


## Creating Dynamic Kubernetes Resources with Crossplane Functions - Steven Borrelli, Upbound, Inc.

URL: [https://www.youtube.com/watch?v=n0j5WiavXEI](https://www.youtube.com/watch?v=n0j5WiavXEI)

 * Crossplane is a project that allows managing infrastructure using Kubernetes and native API.
* It manages anything from AWS buckets to GitHub projects, exposes external APIs as Kubernetes resources, and provides real-time updates.
* Crossplane uses Composition Functions to create complex infrastructure, such as managing an EKS cluster with IAM roles, OIDC clusters, node groups, etc.
* Crossplane's Composition function simplifies the process of creating and managing complex infrastructure by exploding the entire set into smaller pieces, like EKS clusters with IM roles, OIDC clusters, node groups, etc.
* Composition functions use patch transforms to modify desired states and support selector references for security groups and VPCs.
* Crossplane's goal is to enable users to write simple functions using a Unix pipeline-like approach and run them as part of a multistep pipeline.
* Crossplane functions are run in the background and do not restore state, making them stateless.
* Crossplane functions are written in Go and use the kubernetes API machinery to apply changes. They accept input in the form of YAML or JSON, mutate it using JQ, and send the result back as a CR.
* Functions can be installed and run imperatively, with automatic creation of required Kubernetes resources like services, secrets, and certificates.
* Crossplane's composition pipeline is similar to CI systems like GitHub Actions, enabling users to define pipelines using YAML files and reference functions by name.
* Functions can optionally accept input and use go templates to render text as part of the input.
* Crossplane provides an SDK for easily writing functions, which includes handling conversion of protobuf messages to JSON and managing dependencies.
* Crossplane runs functions using gRPC over HTTP and supports mutual TLS authentication.
* Crossplane's design focuses on scalability, with the goal of being able to handle large organizations with massive amounts of resources.
* The Crossplane team is actively adding features every quarter, with a focus on improving the core engine, reducing opinionatedness, and providing multistep pipelines and dependency management.


## WireGuard and the Future of Cloud Networking - Alex Feiszli, Netmaker

URL: [https://www.youtube.com/watch?v=pB3z3EJc6Fw](https://www.youtube.com/watch?v=pB3z3EJc6Fw)

 * Alex Feisli, founder of Netmaker, discussing WireGuard and the future of cloud networking
* Background: IBM devops engineer, multicloud data science infrastructure, Asheville North Carolina resident, music hobbyist
* Previous mindset: VPNs for secure connections over the internet
* Rise of zero trust frameworks and the decline of traditional VPNs
* WireGuard is a new VPN protocol that is simple, fast, and configurable
* History of WireGuard: created in 2015 by Jason Donenfeld, Linux kernel implementation in 2020, widely adopted in personal and corporate spaces
* WireGuard enables arbitrary networking and is the base layer for building secure networks in a zero trust environment
* Demonstration of setting up a WireGuard connection between two devices
* Benefits: low level design, small and fast, modern encryption, embedded in various operating systems, and complements zero trust frameworks.


## Tutorial: Linux Memory Management and Containers - Gerlof Langeveld, AT Computing

URL: [https://www.youtube.com/watch?v=ql1axx--8sI](https://www.youtube.com/watch?v=ql1axx--8sI)

 * Gerlof Langeveld is a senior trainer at AT Computing, which provides Open Source training in Linux and related technologies. He also maintains the atop performance monitor.
* The topic of the session is Linux memory management in relation to containers.
* Memory management in Linux includes static part (kernel and ROM) and dynamic data created via slab cache.
* Containers simplify resource allocation and guarantee memory usage for processes through cgroups.
* Memory can be used in various ways, such as page cache, shared memory, and tempFS.
* Swapping is a mechanism to free up memory when it gets full, but it can lead to performance issues.
* The session includes a demonstration using the mem exerciser program and atop tool.
* Physical memory is subdivided into nodes, with each node having its own threshold values for free pages.
* Kernel decides which pages to swap based on swappiness parameter and available swap space.
* Ohmscore is a value calculated by the kernel to prioritize processes for killing when memory gets full.
* Containers can be managed using cgroups, which allow limiting resource usage for each container.


## Building SaaS Services with CHAOSS Technology to Evaluate Community...- Daniel Cortázar & Yehui Wang

URL: [https://www.youtube.com/watch?v=w9CL-trz-I0](https://www.youtube.com/watch?v=w9CL-trz-I0)

 * Daniel Cortazar and Yehui Wang discussed building SaaS services using CHAOSS technology for evaluating community health in open source projects.
* CHAOS is an acronym for Community Health Analytics Open Source Silver Project, which aims to provide metrics for the health of open source communities.
* The concept of open source community health was introduced with a focus on user care, collaboration, diversity, inclusion, risk, and productivity.
* The CHAOSS project started around four years ago and has released over 30 metrics and the Matrix model to define health metrics in a technological agnostic way.
* The goal is to produce open source software and bring together industrial partners, universities, individual contributors, and open source foundations to collaborate on defining community health metrics.
* CHAOSS uses a Matrix model to measure open source health, focusing on productivity, robustness, and niche creation.
* The ecosystem evaluation system is a theoretical framework provided by CHAOSS that combines metric and matrix models to evaluate open source communities.
* Currently, there are four matrices in use: collaboration development index, community service support, organization activity, and community activity.
* The homepage of OSS Compass provides access to the SAS platform and an OS ecosystem evaluation system.
* CHAOSS aims to help organizations understand their community's health by providing detailed metric results for single repositories and comprehensive community-level monitoring.


## Contributor Growth Strategies for OSS Projects - Dawn Foster, CHAOSS

URL: [https://www.youtube.com/watch?v=xRCFHhL1IgE](https://www.youtube.com/watch?v=xRCFHhL1IgE)

 * Dawn Foster discusses strategies for sustainable contributor growth in open source projects
* Building a strong open source community is essential but finding and retaining contributors can be challenging
* Humans are necessary to maintain an open source project, and maintaining one can be a long-term effort that requires balancing day-to-day work with future sustainability
* Communication and clear expectations are key to encouraging participation and reducing friction
* Explicitly documented governance and welcoming inclusive communities can help motivate people to contribute
* Effective onboarding and mentoring programs can help bring new contributors into leadership positions and reduce the load on existing maintainers
* The use of contributor ladders, clear documentation, and a focus on diversity and inclusion are effective strategies for growing contributor bases and scaling projects.


## PostgreSQL Versus MySQL - Isn't a Database Just a Database - Pep Pla, Percona

URL: [https://www.youtube.com/watch?v=-C6t4z3uGqY](https://www.youtube.com/watch?v=-C6t4z3uGqY)

 * Two friends discussing which database to buy: PostgreSQL or MySQL
* Comparison based on features, licensing, and performance
* MySQL originated by Michael Widmer and Monty Widenius, different companies
* Ferrari Roma vs. John Deere 640 tractor analogy for comparing horsepower and price
* Important to check requirements before making a decision
* Disagreement on licensing: PostgreSQL is more open source than MySQL
* PostgreSQL has parallel processing capability, which Google recommends
* Comparison of SQL support and standard features between the two
* MySQL's InnoDB engine is popular by default
* Handler in MySQL layer handles different operations with different handlers
* Data ordering is a significant difference between PostgreSQL and MySQL
* Primary key indexes can affect performance and should be considered carefully
* PostgreSQL stores old versions of rows in product segments, while MySQL uses rollback segments
* PostgreSQL offers more flexibility with its multi-version concurrency control system
* Vacuum process helps manage old data and reclaimed space in PostgreSQL.


## Insights from the Cloud Native Security Slam - Eddie Knight, Sonatype

URL: [https://www.youtube.com/watch?v=-jUtWEcXVyk](https://www.youtube.com/watch?v=-jUtWEcXVyk)

 * Eddie Knight discussing cloud native security at Cloud Native Computing Foundation (CNCF) event
* Author, trainer, and tech program manager at Sonatype
* Talked about the importance of security hygiene in cloud native computing
* Mentioned the challenges of keeping up with security in open source projects and Sandbox projects
* Discussed tools like Kubernetes, Google's Open Source Security Scorecard, and Renovate bot for improving security
* Highlighted the need for communicating security policies and best practices within the community
* Encouraged collaboration and learning from each other to improve security in the CNCF ecosystem.


## Early Splash Screen Using U-Boot - Devarsh Thakkar & Nikhil M Jain, Texas Instruments

URL: [https://www.youtube.com/watch?v=-uJ_mNUjYpM](https://www.youtube.com/watch?v=-uJ_mNUjYpM)

 * Texas Instruments believes in open source ecosystem and upstream mentality
* Outline of presentation: introduction to boot loader, splash screen, early splash screen, U-Boot SPL, persistent splash screen, and flicker-free transition
* Boot loader is software that loads the operating system; U-Boot is an open-source boot loader used in embedded systems
* Splash screen is an introductory screen displayed when a device boots up
* Early splash screen is displayed as soon as possible after power-on, before the operating system takes over
* U-Boot sets up the necessary environment for the operating system to load
* U-Boot provides several advantages such as easily upgradeable boot loader and command line support
* Splash screen support can be added using configuration files and properties
* U-Boot SPL is a statically linked version of U-Boot used in early boot stages
* Persistent splash screen ensures that the splash screen stays displayed even after the operating system transitions to it
* To add early splash screen support in U-Boot, you need to: initialize DDR and peripherals, load the SPL, and set up the display controller and panel
* The video covers adding early splash screen support for a Texas Instruments device using U-Boot in detail.


## Open Source as a Product: Strategies for Building and Scaling Successful Open Source..- David Hirsch

URL: [https://www.youtube.com/watch?v=3HWdBD71P10](https://www.youtube.com/watch?v=3HWdBD71P10)

 * David Hirsch, from Dynatrace, discusses open source as a product strategy
* Open source is essential for software companies to survive
* Challenges include software development life cycle, collaboration with competitors, and legal aspects
* Creating an open source project means ensuring community involvement and alignment with existing projects
* Focus on business goals when creating or contributing to open source projects
* Aligning roadmaps and coordinating efforts is important for success
* Tracking contributions, managing governance, and justifying resources are also essential aspects of open source product development.


## Backup and Recovery Strategies for Linux Systems - Riya Bansal, Microsoft

URL: [https://www.youtube.com/watch?v=9yT4J8tLGLo](https://www.youtube.com/watch?v=9yT4J8tLGLo)

 * Riya Bansal: Software Engineer at Microsoft, previously worked at Flipkart and American Express
* Loves teaching and mentoring students in open source technologies
* Discussing backup and recovery strategies for Linux systems, focusing on Bakula open source backup software
* Importance of backups and recoveries: data loss can occur due to hardware failure, human error, or cyber attacks, leading to significant downtime and potential revenue loss
* Three types of backups: full backup (copy entire data set), incremental backup (save changes since last backup), differential backup (store changes since last full backup)
* Bakula is a fully-featured open source backup tool that supports multiple platforms including Linux, Mac OS, and Ubuntu
* Bakula has a simple architecture with four components: director, catalog, storage demon, and client
* Director performs backup and restoration jobs; catalog stores metadata; storage demon writes data to different storage media; client interacts with the system
* Bakula provides a GUI and console-based interface for easy use
* Bakula supports three types of backups and allows defining job schedules
* Bakula also has restore functionality and can copy jobs between different storage pools
* Bakula is configurable and offers cloud-based backup options
* Best practices: implement regular backups based on criticality, choose secure backup storage, test backups regularly, monitor alerts for failures or anomalies.


## Tutorial: Developing Portable eBPF Applications Workshop - Lin Sun, solo.io

URL: [https://www.youtube.com/watch?v=DLF3qPioLqM](https://www.youtube.com/watch?v=DLF3qPioLqM)

 * Introducing Lin Sun from solo.io, author of two Istio books and ex-IBM master inventor
* Talking about eBPF (extended Berkeley packet filter) and its innovations in the Linux kernel
* eBPF is a safe and efficient way to run code within the Linux kernel without needing to wait for kernel updates
* bumblebee.go, an open source project from solo.io, helps build, distribute, and run eBPF programs in a Docker-like experience
* Using BPF Compiler Collection (BCC) or BPF Curry to write and compile eBPF programs
* Bumblebee simplifies the process of building, pushing, and running eBPF programs using OCI images
* Discussing memory optimization techniques like Rim buffer and Shield buffer in eBPF
* Using Bumblebee, you can install and configure metric collection and visualization for observability purposes.


## Keynote: Contributing to Critical Open Source Projects: Lessons from PostgreSQL - Jonathan Katz

URL: [https://www.youtube.com/watch?v=DSc6WTrSHSI](https://www.youtube.com/watch?v=DSc6WTrSHSI)

 * PostgreSQL started as an academic project at UC Berkeley in the late 1980s
* Became open source project in the early 1990s due to hobbyist contributions
* Critical open source project today, used by many production systems including AWS services like Amazon RDS and Amazon Aurora
* Logical replication, a new feature in PostgreSQL 16, is important for streaming change data capture and real-time analytics processing
* AWS has been contributing to PostgreSQL development, focusing on features like logical replication standby and extensions
* PostgreSQL community is collaborative, with a focus on code review, testing, and design
* Beyond the core database software, there are many extensions available to add functionality without forking the database
* AWS is involved in various aspects of the project, including extension development and advocacy
* PostgreSQL has been around for over 37 years, and there is a whole generation of developers who have used it extensively
* Lessons from contributing to PostgreSQL include the importance of mentorship and continuing to grow and sustain the community.


## Let's Build Our Own Virtual RaspberryPi Using QEMU Virtualization - Vipul Gupta, balena

URL: [https://www.youtube.com/watch?v=EYVkSUydqMI](https://www.youtube.com/watch?v=EYVkSUydqMI)

 * Vipul Gupta from balena presented at Open Source Summit about building a virtual Raspberry Pi using QEMU
* He started by discussing his background and his interest in virtualization as a solution to the chip shortage issue
* He provided an overview of KVM virtualization, TCG, and how it allows multiple machines to work together within isolation
* He explained that QEMU is functionally accurate virtual emulation platform that simplifies the process of running software on different targets without requiring specialized hardware
* He demonstrated using QEMU to build a virtual Raspberry Pi machine, mentioning the necessary dependencies and configuration options
* He discussed the benefits of QEMU, including its ability to execute code on target platforms and provide near-native performance with dynamic translation
* He also mentioned the flexibility of QEMU, which allows running multiple virtual machines at once and using different architectures within a single host machine
* He provided an example of using QEMU for building a Raspberry Pi CI/CD environment and emphasized its usefulness in prototyping and testing hardware without requiring actual devices.


## Overcoming Imposter Syndrome and Gaining Confidence as an Open Source Mentee - Malakannawar & Burse

URL: [https://www.youtube.com/watch?v=G16_Zc6GX8Y](https://www.youtube.com/watch?v=G16_Zc6GX8Y)

 * Speakers: A. Smith and Pesha Verma, open source mentees
* Topic: Overcoming imposter syndrome in open source projects
* Imposter syndrome: feeling like a fraud or inadequate despite skills and achievements
* Common among open source contributors, especially those new to the community
* Mentees may feel:
  + Unqualified or inexperienced
  + Anxiety, low self-esteem, even depression
  + Hesitant to engage in discussions or give feedback
  + Setting unrealistic standards and striving for perfection
  + Fear of taking risks or missing opportunities
* Mentors also experience imposter syndrome and may expect mentees to ask questions
* Myths about open source mentors:
  + Expecting mentees to know everything right away
  + Feeling incompetent or unable to answer questions
  + Being too busy for mentorship or reviewing PRs
* Reviewing feedback is not a negative comment, but an opportunity for improvement
* Open source projects require contributions beyond coding, such as documentation and design
* Setting small, attainable goals can lead to a sense of achievement and confidence
* Joining open source communities can help establish valuable connections and learn from others
* Imposter syndrome can be overcome by recognizing it, seeking mentorship or peer support, and embracing the learning process.


## Best Practices for AI-Assisted Code Generation Tools (Like CoPilot) - Van Lindberg, OSPOCO

URL: [https://www.youtube.com/watch?v=NPMb95fuVBQ](https://www.youtube.com/watch?v=NPMb95fuVBQ)

 * Van Lindberg discussing best practices for AI-assisted code generation tools, specifically focusing on Copilot
* Many organizations are rolling out AI assistant code generation due to increased productivity and developer satisfaction
* Reasons for using AI code generation:
  + Conserves mental energy and improves flow
  + Generates repetitive code more efficiently
  + Improves refactoring process
* Risks of copyright infringement with AI-generated code:
  + Increased likelihood of memorized or copied output due to similar input
  + Need to be aware of copyrighted code and provide attribution
* Best practices for avoiding copyright infringement:
  + Don't accept code without editing and indemnity doesn't apply if you don't accept the exact code
  + Train your own model with your own data to get higher quality output
  + Negotiate confidentiality terms for third-party code
* Security risks of using AI-generated code:
  + Generated code could include insecure paths or vulnerabilities
  + Use test driven development and review the code carefully
* Snippet scanning is difficult and noisy with AI-generated code, consider marking files containing AI generated content for specific scanning
* Idea: AI drafts human edits to preserve copyright ability
* Maintain context around the code by understanding the underlying documentation and code history.


## Beyond Code: The Importance of Elevating Non-Code Contributions - Abubakar Ango & Fatima Khalid

URL: [https://www.youtube.com/watch?v=OIfasnGEees](https://www.youtube.com/watch?v=OIfasnGEees)

 * Fatima Khalid from GitLab Developer Evangelism Team talks about the importance of non-code contributions in open source projects.
* She shares her background and experience working in the open source community and how she started contributing to GitLab.
* Non-code contributions include event planning, documentation, testing, onboarding, translation, and community management among others.
* Examples given include organizing events like Open Source Summit, maintaining a newsletter, and mentoring new contributors.
* Non-code contributions are valuable as they bring the community together, help learn from each other, and create opportunities for future growth.
* Recognition and gamification systems like badges, awards, and swag can motivate and reward non-code contributors.
* Organizations like GitLab have programs like Heroes and Advocates to recognize and give opportunities to technical and non-technical contributors alike.
* Creating a safe, inclusive, and healthy environment is crucial for a vibrant community, where everyone feels welcomed and valued.


## The Future of JavaScript Package Management - Darcy Clarke, Independent

URL: [https://www.youtube.com/watch?v=OyL20471Yy8](https://www.youtube.com/watch?v=OyL20471Yy8)

 * Darcy Clarke, independent, discussing the future of JavaScript package management
* Current state:
  + Large number of dependencies in a project, many transitive dependencies which can lead to security vulnerabilities and performance issues
  + Npm is the largest package registry with over 25 million packages and 210 billion downloads per month
  + Dependency resolution and versioning can be complex and inconsistent across package managers
  + Interoperability between different package managers can be limited
* Problems:
  + Supply chain attacks and vulnerabilities in open source software are a concern
  + Managing dependencies and their updates takes significant time and effort, especially for smaller teams
  + The cost of maintaining open source packages is not fully understood or visible to consumers
* Future state:
  + New tools like DSS dependency selector syntax and policy engines may provide more accurate and standardized dependency resolution
  + Open source ecosystems need to focus on security and sustainability
  + Collaboration and community building are important for improving the overall quality of the JavaScript package ecosystem.


## Cost Visibility for Infrastructure as Code - Rufaida Mugalli, Liquid Reply

URL: [https://www.youtube.com/watch?v=TjTPEyofBNU](https://www.youtube.com/watch?v=TjTPEyofBNU)

 * Rufaida Mugalli from Liquid Reply spoke about cost visibility for infrastructure using Infracost tool
* Infracost is a tool that scans Terraform code and provides cost estimation for infrastructure
* It integrates with different CI/CD tools like GitHub Actions, Jenkins, CircleCI
* To use it, you need to install the Infracost CLI, retrieve an API key, and configure it in your GitHub action or CI/CD tool
* Infracost works by scanning a Terraform plan and applying cost estimates based on the resources used
* It can help prevent unexpected costs and make informed decisions about infrastructure choices
* In the demo, Mugalli showed how to create an Infracost action using a container action in GitHub Actions, and how it can be integrated with a Jenkins pipeline.
* Mugalli mentioned that Infracost supports multiple directories for different services and environments, and that it can break down costs by service or resource.
* She also discussed the importance of understanding Terraform and using Infracost together for effective cost management.
* Mugalli encouraged the audience to try out Infracost and provided resources for learning more about it.


## Ten Practical Approaches for Building Inclusive Open Source and InnerSource..- Saebi & Gale & Clare

URL: [https://www.youtube.com/watch?v=TyJB5vqNJ6I](https://www.youtube.com/watch?v=TyJB5vqNJ6I)

 * Claire Dillon and Gail McCormick share 10 practical approaches for building inclusive open source and innerSource communities.
* They emphasize the importance of intentional inclusion and respecting every member as a full citizen in the community.
* Approaches include:
  + Using clear and inclusive language, being cognizant of different time zones, and implementing succession planning.
  + Creating safe spaces where people can share ideas authentically and feel heard, and actively working to diversify representation beyond gender and race.
  + Building psychological safety through intentional actions and creating opportunities for personal connections.
* Gail shares examples of successful inclusive communities she's been a part of and the impact they've had on her career.
* They encourage active listening, empathy, and open communication to foster an inclusive environment where everyone feels valued and empowered to contribute.


## A Guide to Securing GitHub Based on Lessons Learned - Christine Abernathy, F5, Inc.

URL: [https://www.youtube.com/watch?v=VYpJF8DeTZ8](https://www.youtube.com/watch?v=VYpJF8DeTZ8)

 * Christine Abernathy from F5 shares lessons learned in securing GitHub repositories, especially for open source projects.
* Challenge: managing multiple GitHub organizations with different policies and processes.
* Importance of security in managing GitHub organizations and repositories.
* Different types of threats to consider: supply chain attacks, secret leaks, dependency threats, etc.
* Best practices for securing GitHub repositories: two-factor authentication, access control roles, code reviews, etc.
* Tools like Legitify and Scorecard can help establish a baseline and improve security posture.
* Importance of community involvement in security, including open source security foundations and incident response teams.
* Holistic approach to securing open source software supply chains.
* Focus on establishing consistent policies and compliance across organizations.
* Use of automation tools for configuration management and vulnerability scanning.
* Importance of regular reviews and updates to security practices.


## The SBOM Way! The Art of Consuming, Enriching, and Managing Inbound..- Anupam Ghosh & Arun Azhakesan

URL: [https://www.youtube.com/watch?v=Vwn2uLXfRj0](https://www.youtube.com/watch?v=Vwn2uLXfRj0)

 * Anupam and Arun discuss the challenges faced in managing compliance workflow for software components using Siemens Software 360 (SW360)
* SW360 is used to register, review, assess, and manage components with their corresponding project
* Challenges include identifying OASIS components, generating SBOMs, enriching information, managing multiple SBOM formats, and exchanging information between tools
* SW360 supports open source component hub tracking, license clearing, and vulnerability monitoring
* Automation is used to minimize duplication, reduce workload, and ensure consistency in component data models
* The presentation covers SB360's approach to component management and the importance of accurate SBOMs for managing open source components.


## OSPOs and Engineering Effectiveness - Nithya Ruff, Amazon & Mary Wang, Volvo Car Corporation

URL: [https://www.youtube.com/watch?v=bL5NMWqYNRg](https://www.youtube.com/watch?v=bL5NMWqYNRg)

 * Mary Wang, Director of Open Source Ecosystem at Volvo Car Corporation, and Nithya Ruff, Senior Manager for Open Source Program Office (OSPO) at Amazon, discussed their experiences with OSPOs and engineering effectiveness in two different companies.
* Volvo Car Corporation has a complicated background in open source, starting from the invention of the three-point safety belt which was not a commercial product but saved lives by being open sourced.
* Open source is now a focus on safety, sustainability, and new technology at Volvo. The OSPO helps manage risk, compliance, and makes developer life easier.
* Amazon's approach to open source is driven by its history of using open source infrastructure and services, supporting customers who want to use the platform and open source development, and being a good global citizen by building upon open source.
* Amazon's OSPO removes barriers to using open source projects in their development process by automatically verifying license acceptance during build and release processes.
* Volvo has also started an OSPO with 80,000 developers, who need help scaling due to the large number of products and distribution challenges. They also have champions dedicated to each product division who help with compliance and training.
* Open source compliance is important for both companies, and they depend on the community for engagement and education. They also prioritize automating compliance processes where possible.
* Developers spend a significant amount of time on administrative tasks instead of innovation, and open source champions can help reduce friction and make development more efficient.
* Open source champions are dedicated experts who build relationships with upstream communities, ensure compatibility with internal code, and provide training and support for their teams.
* Companies need to justify spending time and resources on open source initiatives by focusing on the value of contributions, reducing risk, and improving innovation.
* The Linux Foundation has done an assessment of the cost of maintaining the Linux kernel which is worth the technical debt perspective.
* Spdx version 30 RC is expected to get soon, it will hopefully integrate license compliance part and security compliance part in AI data unit.
* Developers need to be aware of vulnerability reports and SBOM alignment across different teams requirements within development process CI CD.
* The interesting part is the challenge of generating Boom information with standard like company define data and put it, and fulfilling license compliance and security compliance totally is needed.


## Node.js - What's Next - Catalyzing Change in the Node.js Ecosystem - Michael Dawson & Jean Burellier

URL: [https://www.youtube.com/watch?v=f61KgJVzq78](https://www.youtube.com/watch?v=f61KgJVzq78)

 * Michael Dawson and Jean Burellier discuss the future of Node.js ecosystem
* Changes in the Node.js ecosystem: release of new versions, end-of-life for older ones, notable changes in change logs
* Following what's new: GitHub notifications, weekly or daily working group meetings, YouTube recordings
* New features and initiatives: performance improvements, modern HTTP support, web assembly integration, observability, security enhancements
* Community involvement: open source projects, collaboration with existing maintainers, contributor experience, documentation improvement
* Technical priorities: developer experience, sustainability
* Constituencies: education, students, teachers, organizations
* New initiatives: single executable applications, observability, serverless, CI infrastructure
* Teams to get involved with: performance, security, website development, documentation
* Upcoming initiatives: CI flakiness, tree shaking, internationalization
* Joining the Node.js community: open meetings, transparent projects, bringing specific expertise.


## Including Voices and Perspectives that Often Go Unheard - Stefka Dimitrova, VMware Bulgaria Ltd

URL: [https://www.youtube.com/watch?v=hEG7XxHMwIE](https://www.youtube.com/watch?v=hEG7XxHMwIE)

 * Stefka Dimitrova is a community strategy team manager at VMware Bulgaria Ltd.
* She has a background in business economics and has worked in the tech industry for 10 years.
* She is passionate about outdoor climbing, education, mountaineering, improvisational theater, and Playback theater.
* Dimitrova shares her experience of not feeling worthy enough to share her thoughts and ideas in the past due to her gender and non-native speaker status.
* She talks about the importance of recognizing power dynamics and underprivileged areas, and the need for open communication and collaboration.
* Dimitrova mentions the cost of exclusion and loss of human capital wealth due to gender inequity, homophobia, and racial gaps.
* She shares her inspiration from improvisational theater, specifically Playback theater, and how she applies its principles in various aspects of her life.
* Dimitrova stresses the importance of creating safe spaces for vulnerable sharing and active listening.
* She mentions using sociometry, a method used in Playback theater, to help extend existing relationships and build trust.
* Dimitrova discusses the benefits of conscious brain connection and the use of art and creativity to connect at deeper levels.
* She encourages finding opportunities for one-on-one conversations and small group work to encourage open sharing.
* Dimitrova emphasizes the importance of empathetic listening, active listening, and providing opportunities for creative expression.
* She concludes by expressing her optimism for humanity and the world, and inviting questions from the audience.


## Getting Started with BPF Security Observability - Vandana Salve, Independent Consultant

URL: [https://www.youtube.com/watch?v=k1r_lHNKGCc](https://www.youtube.com/watch?v=k1r_lHNKGCc)

 * Vandana Salve: Independent Consultant with experience in product development, networking, storage, and mentoring
* Recently joined Micron working on CX memory software
* Passionate about open source technologies and guiding people interested in learning
* Talked about BPF (Berkeley Packet Filter) security observability using the baby tool framework
* BPF allows program execution without modifying the kernel or adding additional kernel modules
* Extended BPF enables virtual machine, VPN program execution with customization based on use cases, particularly for security
* Helped explain various hooks in BPF like Network, system call function entry/exit, and specific triggers called hoots
* Discussed the importance of verifying BPF program loading, preventing compromising the kernel system accidentally, and using helper functions to collect data
* Mentioned that BPF can be used with various programming languages like C, Rust, Lua, Python, etc.
* Demonstrated how to use BCC (BPF Compiler Collection) tools for tracing and collecting performance data
* Explained the role of Linux Security Model Interface (LSM) in enforcing Mandatory Access Control policies and the importance of observability across management processes.


## Keynote: Software Security: _You_ are the Calvary - Cristina Bentué, Co-founder and COO, IriusRisk

URL: [https://www.youtube.com/watch?v=l8F8g2EggjQ](https://www.youtube.com/watch?v=l8F8g2EggjQ)

 * Cristina Bentué is the COO of IriusRisk, a company that helps build secure software
* Misconception: Believing that cybersecurity is something that can be added as an afterthought or bought as a package to make software secure
* Reality: Good security requires careful consideration and planning from the beginning
* Cristina's background: Started in cybersecurity consulting, worked as business developer and security analyst, founded IriusRisk
* Pen testing experience: Discovered vulnerabilities in existing applications, rebuilt some from scratch to make them secure
* Importance of secure software: Needed for businesses, ethical responsibility, and national security
* Challenges: Hackers can exploit complex software, and the sheer quantity produced creates an incentive for attacks
* Threat modeling: A design activity used to identify potential threats and vulnerabilities in software
* Regulations: NIST, National Cyber Security Strategy, European Union's Cyber Resilience Act propose regulations for secure software development
* Shift left: Incorporating security into the software development process early on
* Cavalry analogy: Thinking of security as the cavalry coming to save the day is a misconception; it should be built in from the beginning.


## Dependency Management: The Cause of—and Solution to—All Supply...- Eve Martin-Jones & Josie Anugerah

URL: [https://www.youtube.com/watch?v=liPFU9R7g4k](https://www.youtube.com/watch?v=liPFU9R7g4k)

 * Eve Martin-Jones and Josie Anugerah discuss dependency management in open source software projects
* Dependency management is crucial for preventing security vulnerabilities in supply chains
* Dependency resolution algorithm determines which version of a package to include based on direct dependencies and constraints
* Indirect dependencies can create conflicts and make resolving issues more complex
* Scalable solutions are necessary for managing dependency graphs and dealing with frequent changes
* Open source ecosystems like npm, Maven, and Cargo have different approaches to handling dependencies and version requirements
* Pinned requirements specify exact versions, while open requirements allow for flexibility and automatic updates
* Managing large dependency graphs can be time-consuming and require coordinated effort across the ecosystem
* Real-world examples, such as the Log4j vulnerability, demonstrate the importance of effective dependency management.

Some key points:

* Dependency resolution algorithm selects the version based on direct dependencies and constraints.
* Indirect dependencies can make resolving issues more complex due to potential conflicts.
* Scalable solutions are necessary for managing large dependency graphs and dealing with frequent changes.
* Open source ecosystems like npm, Maven, and Cargo have different approaches to handling dependencies and version requirements.
* Pinned requirements specify exact versions, while open requirements allow flexibility and automatic updates.
* Real-world examples, such as the Log4j vulnerability, demonstrate the importance of effective dependency management.


## Keynote: Do Repeat Yourself - Designing Open-source Libraries for Modern... - Patrick von Platen

URL: [https://www.youtube.com/watch?v=mcCcwZ2SWh0](https://www.youtube.com/watch?v=mcCcwZ2SWh0)

 * Patrick von Platen discusses his experience creating open-source machine learning libraries, specifically Transformers and Diffuser
* He challenges the DRY (Don't Repeat Yourself) principle in software design, focusing on machine learning libraries
* The DRY principle states that every piece of knowledge in a system should have a single unambiguous authoritative representation
* In machine learning, the fast-evolving nature of the field makes it challenging to define clear and unambiguous abstractions
* Open source software, especially in machine learning, relies heavily on community contributions
* The DRY principle can be difficult for new contributors to follow due to the large amount of existing code and the ambiguity of some abstractions
* Transformers, a popular machine learning library, has a stable number of commits per week and relies on trusting contributors not to break core components
* Transformers follows a "single model file policy" where every model knowledge is in one code file for ease of reading and understanding
* Enforcing unified APIs across models is important for user experience, especially in production use cases
* Avoiding unnecessary abstraction layers and copy-pasting code are also important considerations when designing machine learning libraries.


## Alternative Introduction to Quantum Computers - Konrad Gawda, Orange Polska

URL: [https://www.youtube.com/watch?v=piumiPpWVs4](https://www.youtube.com/watch?v=piumiPpWVs4)

 * Conrad Gawda, Orange Polska Cloud evangelist, Python developer trainer, and podcast host
* Quantum computers are like analog calculators with the advantage of being able to represent an infinite number of states unlike analog computers
* Ancestor of quantum computing was the differential analyzer created by Lord Kelvin in the 19th century
* Leonardo Torres Quevedo, a Spanish engineer and inventor, also worked on early forms of electronic and analog computers
* The difference between classical and quantum computing:
  * Classical computing uses bits with distinct states (0 or 1)
  * Quantum computing uses qubits which can exist in multiple states at once (superposition)
* Qubits store and manipulate information using probability, not definite values
* Measuring a qubit collapses its superposition, making it impossible to measure multiple qubits at once without destroying the superposition of the others
* Quantum computers can perform complex calculations much faster than classical computers due to their ability to process many possibilities simultaneously
* Entanglement is a physical phenomenon in quantum mechanics that allows quantum systems to be correlated in such a way that the state of one system cannot be described independently of the other
* Quantum gates are used to manipulate qubits and perform operations on them, similar to classical logic gates but with different properties
* Quantum circuits can be expressed as matrices and can reflect their code behavior, making them interchangeable with matrix representations
* Amazon Web Services (AWS) provides access to quantum computing resources for simulation and experimentation.
* To use AWS quantum services, an AWS account is required, along with the installation of certain libraries and tools.
* Simulating a quantum circuit using AWS simulator can yield statistical results that show probability amplitudes for different states measured over multiple runs.
* Running the same circuit on real quantum hardware will yield actual outputs with potential errors due to qubit noise and other physical limitations.
* The future of quantum computing may involve larger, more error-corrected qubits, breaking encryption, optimizing problem solving, and even contributing to artificial intelligence.


## Revolutionising Browser Automation: A Deep Dive into the WebDriver BiDi Project and...- Tamsil Amani

URL: [https://www.youtube.com/watch?v=qRwoYOTocbw](https://www.youtube.com/watch?v=qRwoYOTocbw)

 * Tamsil Amani, software engineer at browserstack, discussing advancements in browser automation testing
* Browser automation testing faced common problems like tests passing on one browser but failing on others and handling real-time events
* History of browser automation testing: Web came in 1993, Selenium project started in 2006 with a different approach called WebDriver
* WebDriver uses a protocol to communicate with the browser, either WebDriver classic or Chrome DevTools Protocol (CDP)
* High-level approach tools like Cypress, TestCafe, and Puppeteer use APIs and Node.js, while low-level approach tools like WebDriver RPM and Night Watch use WebDriver classic protocol
* Problem: browser doesn't trust JavaScript code from automation tools for complex tasks like opening new tabs, windows, or testing within iframes
* Solution: low-level approach using remote commands and direct event handling in the browser
* Event Loop in browsers allows for event handling, and trusted events have a property called "trusted" set to true if generated by user action, false otherwise
* Previous example showed Selenium navigating a website and clicking an add cart button using WebDriver classic protocol
* Disadvantages of WebDriver classic: not event-driven, limited cross-browser support relies on browser vendor implementation, and low scalability
* Advantages of CDP: event-driven bidirectional messaging using websockets, provides low-level control for developers, and designed specifically for chromium-based browsers
* WebDriver Die project merges single protocol for better cross-browser support and collaboration between browser vendors and open source automation projects
* Demonstration of WebDriver die navigating a locally hosted page, raising a JavaScript exception, and catching it using the log inspector module in real time
* Network interception allows testing without actual network requests, but requires mocked responses for irrelevant tests
* Accessibility testing is important, and WebDriver Die includes accessibility APIs and support for screen readers and alternative text
* WebDriver Die's roadmap includes implementing Network interception and improving developer experience by making it easier to use.


## Scaling AI Workloads with Kubernetes: Sharing GPU Resources Across Multiple Containers - Jack Ong

URL: [https://www.youtube.com/watch?v=t68ayhtaUQ8](https://www.youtube.com/watch?v=t68ayhtaUQ8)

 * Jack Ong, machine learning engineer at Gene Ai, discussing scaling AI workloads with Kubernetes and sharing GPU resources across multiple containers using Nvidia GPUs
* Reasons for using Kubernetes: reproducible services, infrastructure agnostic, easier GPU management with operator support
* Multiinstance GPU in Nvidia GPUs: sharding a single GPU into multiple instances, each instance having its own memory and compute slice
* Partitioning GPU slices: specifying the size of each slice, importance of ordering partitioning, sharing compute instances and memory, and error isolation
* Managing GPUs with Kubernetes: installing Nvidia GPU operator, using node selectors, defining resource quotas
* Sharing GPU resources across containers: labeling nodes to expose multiple GPUs, using single or mixed strategies, time slicing, and Mic partitioning
* Optimizing deep learning workloads in Kubernetes: low precision arithmetic models, attention slicing, speculative decoding, model distillation.


## Bringing Service Security to a New Level: An Introduction to SaaSBOMs - Ivana Atanasova & Rose Judge

URL: [https://www.youtube.com/watch?v=vZgW1KxjI68](https://www.youtube.com/watch?v=vZgW1KxjI68)

 * Introduction to SaaS Bill of Materials (SBOMs) by Rose Judge and Ivana Atanasova, open source engineers at VMware
* SBOMs are used for securing software supply chains, especially in the context of cloud-based services
* SBOMs describe components of a service, including dependencies, licenses, and version numbers
* SBOMs help build trust between consumers and providers by providing transparency around software components
* SBOMs can contain security information, such as vulnerabilities and compliance details
* The US government is requiring vendors to provide SBOMs as part of Executive Order 14028
* SBOMs are important for understanding the risks associated with the third-party services used in applications
* SBOMs help organizations manage risk around vulnerable components and comply with security policies
* Challenges with SBOMs include gathering information, ensuring correct formatting, and keeping up-to-date
* The Cybersecurity and Infrastructure Security Agency (CISA) is working on standards for SBOMs, such as the SPDX format and the SAS Profile specification.
* The SAS Profile complements the SPDX standard by providing additional contextual information about services.
* The SAS bomb standard is focused on describing software components in a service, including service endpoints and data flows.
* SBOMs can be used to track transitive dependencies and regulatory compliance requirements.
* The working group for SBOMs meets every Monday morning to discuss progress and prepare advisories.
* Questions from the audience included how to handle dynamic services with frequent changes, the role of observability tools in SBOM production, and the potential benefits of open source solutions for managing SBOMs.


## Keynote: Given the Choices We Have: The Power of Allyship - Fatima Sarah Khalid

URL: [https://www.youtube.com/watch?v=xOkDxLKhUxk](https://www.youtube.com/watch?v=xOkDxLKhUxk)

 * The speaker shares her experience of forming a strong friendship with Gloria in childhood.
* Their friendship was affected when she was labeled as a terrorist after 9/11.
* She learned about allyship and its importance during this experience.
* Allyship goes beyond pronouns and requires commitment, especially in uncomfortable situations.
* Some tools for building an allyship knapsack include educating oneself, listening to the marginalized group, speaking up against racism or discrimination, donating money, using social networks for advocacy, and promoting equity and justice.
* The speaker shares five examples of allyship she has experienced: a manager encouraging her to speak up in a team meeting, a white male coworker advocating for diversity at a conference, an ally protecting a black woman from discrimination at an airport, a colleague offering to walk her back to her hotel late at night, and a community member reporting a code of conduct violation.
* The speaker reflects on the importance of allyship in shaping identity and making positive change in the community.


## Securing Modern Apps with Zero Trust and Next-Gen Web Application Firewall - José Carlos Chávez

URL: [https://www.youtube.com/watch?v=yS7ZkzpL_80](https://www.youtube.com/watch?v=yS7ZkzpL_80)

 * Jose Carlos Chavez: software engineer, open source enthusiast, and father
* Traditional Web Application Firewall (WAFF) protects web applications from known attacks like cross-site scripting, SQL injection, etc.
* WAFF is deployed as a reverse proxy at the front server, analyzes traffic, and decides whether to allow or block requests based on rules.
* Old WAFF features: IP fencing, Geo blocking, request response inspection, anomaly scoring, and block/allow certain number of requests per window time.
* Traditional Perimeter Security is not effective in modern cloud-native environments due to scalability needs, microservices, and dynamic nature of traffic.
* Zero Trust security model: trust no one, verify everything, least privilege access, and constant monitoring.
* Shift from Perimeter Security to Zero Trust Architecture: assume attacker is already inside the network and implement policies accordingly.
* Key principles of Zero Trust: trust verification, least privilege access, continuous monitoring, adaptive policy enforcement, and dynamic resource authentication and authorization.
* WAFF still plays a role in Zero Trust security as it provides additional security measures like threat detection, vulnerability remediation, and anomaly analysis.


## OWASP Top 10 Vulnerabilities in Node.js - Marco Ippolito, NearForm

URL: [https://www.youtube.com/watch?v=0lMn0ZpsycE](https://www.youtube.com/watch?v=0lMn0ZpsycE)

 * Marco Ippolito from NearForm discusses the OWASP Top 10 security vulnerabilities in Node.js
* Open Web Application Security Project (OWASP) is a nonprofit organization that provides ranking of top 10 critical web application security risks based on expert surveys and common vulnerabilities
* The Top 10 list includes server side request forgery, security logging monitoring failure, software data integrity failure, interconnected system vulnerability, authentication failure, insecure design, injection, cryptographic failure, broken access control, and vulnerable components
* Server Side Request Forgery (SSRF): an attacker can manipulate a web application to make unintended HTTP requests on behalf of the client
* Security logging monitoring failure: lack of security logging or proper alerting can allow attackers to go undetected for long periods of time
* Software data integrity failure: malicious code can be injected into software through insecure CI/CD pipelines or deserialization vulnerabilities
* Interconnected system vulnerability: unsecured access to one part of a system can lead to compromise of the entire system
* Authentication failure: lack of proper authentication checks and weak passwords can make it easy for attackers to impersonate users
* Insecure design: applications that don't consider security in their design can leave many vulnerabilities open to attackers
* Cryptographic failure: using outdated or weak cryptographic algorithms can make it easier for attackers to gain access to sensitive information
* Broken access control: improperly implemented access controls can allow unauthorized access to resources and data
* Vulnerable components: using outdated or insecure third-party dependencies can leave applications open to attacks
* To mitigate these vulnerabilities, developers should always validate user input, log everything, ensure data integrity through signing and hashing, use multifactor authentication, enforce strong passwords, keep software up-to-date, and follow best practices for access control.


## Deploying Your Own Language Models: A Use Case Demo with Open Source... - Shrey Anand & Surya Pathak

URL: [https://www.youtube.com/watch?v=2NgUlbBbelY](https://www.youtube.com/watch?v=2NgUlbBbelY)

 * Shrey Anand and Surya Pathak from Red Hat discuss deploying an open source language model application using the OpenShift platform on a Kubernetes cluster.
* They explain the components of the language model application architecture, including vector embeddings database for model finetuning and Transformer architecture for generation mode.
* The demo uses the Rosa service for question answering, where the application loads documents into a vector store and generates top candidate answers based on query embedding similarity.
* The Vector database is used to efficiently find nearest neighbors using an approximate nearest neighbor algorithm.
* They mention the importance of model performance evaluation, responsibility separation, and adapting open source language models to specific use cases.
* They also discuss open source models like Hugging Face and their considerations for choosing a model based on resource budget, license requirement, and performance.
* The presentation covers topics such as pretraining, supervised finetuning, and reinforcement learning, as well as deployment considerations including infrastructure management, cost optimization, and security privacy.
* They demonstrate deploying the pretrained T5 text generation model using Ray serve for serving and scaling.


## Why Should You Consider JavaScript on WebAssembly? - Angel Maria De Miguel Meana & Saúl Cabrera

URL: [https://www.youtube.com/watch?v=7i3hGtMUdAA](https://www.youtube.com/watch?v=7i3hGtMUdAA)

 * Angel Maria De Miguel Meana from VMware AI Labs talks about extending Shopify using JavaScript and WebAssembly
* WebAssembly is a binary format for executing code in web browsers, providing the ability to run code written in different programming languages like C, C++, and Rust, without the need for transcompilation.
* JavaScript can be used inside WebAssembly, allowing developers to take advantage of its interpreting capabilities and large community.
* Shopify started using WebAssembly a few years ago to develop applications more efficiently, such as Figma, and has also ported existing applications like Adobe Photoshop and Google Earth to run in the browser.
* JavaScript code can be compiled into WebAssembly bytecode and executed directly in the browser without needing to deal with transcompilation or the need for specific architectures or operating systems.
* WebAssembly enables running code in various environments, including mobile devices, servers, and embedded devices.
* The use of WebAssembly is important because it opens up new possibilities for running JavaScript in different environments and allows developers to avoid the limitations of traditional JavaScript runtimes.
* Shopify's use of WebAssembly has enabled complex interaction between buyers, merchants, and third-party developers, making the platform more extensible and accessible.
* The presentation covers the internals of how WebAssembly works, including the compilation process and the role of the Interpreter and Baseline compiler in optimizing code.
* JavaScript can be used alongside other programming languages in WebAssembly, allowing for complex applications to be developed using different libraries and ecosystems.


## Enabling VEX and Full SBOM Coverage with Wolfi Based Containers - Adolfo García Veytia, Chainguard

URL: [https://www.youtube.com/watch?v=9MGk1hz2KNQ](https://www.youtube.com/watch?v=9MGk1hz2KNQ)

 * Adolfo Garcia, an open source engineer at Changard, discusses the importance of Software Bill of Materials (SBOM) and VEX, a vulnerability exchange platform.
* He uses the analogy of a car tire recall to explain the need for complete and accurate SBOM information.
* A tire recall in the late 1990s affected Ford Explorers and other vehicles due to faulty tires that could blow out and cause accidents, leading to over 270 deaths. The issue was traced back to a specific batch of tires manufactured by Firestone in the 1990s.
* In software development, SBOMs are essential for keeping track of components and their dependencies in complex systems like cars. VEX helps assess vulnerabilities and provides up-to-date information to ensure vehicle safety.
* The Wolfi Linux distribution includes full coverage SBOMs and can generate VEX documents containing vulnerability information, making it an effective solution for secure software supply chain management.
* Wolfe's advisory feed fetches vulnerability data automatically, while Vexctl is used to create VEX documents.
* Using the example of a car tire, generating a VEX document involves documenting the vulnerability, product information, and affected components.
* VEX also provides machine-readable justifications for vulnerabilities, making it easier for developers and security teams to understand and prioritize issues.


## Security Research with Open Source Software: Vol. Omega - Yesenia Yser, The Linux Foundation

URL: [https://www.youtube.com/watch?v=DsCsOgykJU4](https://www.youtube.com/watch?v=DsCsOgykJU4)

 * Yesenia Yser, first-generation Cuban American, discusses her role in protecting the digital realm and advocating for diversity and inclusion in tech
* Extensive background in cybersecurity and software development, including work on open source projects and security research
* Alpha Mega project focuses on improving the manual security vulnerability disclosure process in the open source ecosystem
* Omega tool chain includes a scan of Docker containers, identification of security vulnerabilities, communication with open source maintainers, and automation of vulnerability disclosure processes
* Collaborating with Purdue University to leverage Omega analyzer for research
* Advocating for personal development, self-assurance, and mentorship in the tech industry
* Discusses the challenges of identifying and remediating security vulnerabilities in open source projects, including long timelines, communication, and documentation issues
* Calls for improving automation and collaboration in the open source ecosystem to reduce the burden on maintainers and improve the overall security posture.


## Identifying and Mitigating Cloud and Container Threats - Pablo Musa, Sysdig

URL: [https://www.youtube.com/watch?v=GGYYVOTIplU](https://www.youtube.com/watch?v=GGYYVOTIplU)

 * Pablo Musa from Sysdig discussing cloud and container threats
* Covers image vulnerability management, runtime security, and secure registry
* Importance of securing source code repositories and minimizing image size
* Discusses the risks of malicious images and attacks on registries
* Emphasizes the importance of a holistic approach to security

Image Vulnerability Management:
- Access control for repository
- Source code scanning
- Vulnerabilities in code or dependencies

Runtime Security:
- Container image integrity
- Malware injection during build process
- Crypto mining attacks on build machines
- Need to minimize attack surface

Secure Registry:
- Privilege misconfiguration
- Image signing and verification
- Trusted base images from verified sources

Other topics discussed:
- Least privilege principle
- CICD pipeline security
- Visibility into running containers with tools like Falco.


## Sponsored Session: Your Software Supply Chain is Only as Secure as its Weakest Link - Boris Cipot

URL: [https://www.youtube.com/watch?v=IRcxgxtsdUw](https://www.youtube.com/watch?v=IRcxgxtsdUw)

 * The speaker acknowledges that software supply chain security is a crucial but often overlooked topic
* Developers focus on functionality and usability, but security is also important
* Open source software is widely used in development and can introduce risks through transitive dependencies
* Keeping informed about vulnerabilities and updating software promptly is essential for mitigating risks
* Hackers are constantly evolving their tactics and motivated by various reasons, including financial gain or political motivations
* DevOps practices, such as continuous integration and delivery, require careful consideration of security at every step
* The EU Resilience Act will introduce new regulations for software development and supply chain security
* Open source licenses can impact the use and distribution of software components
* Creating a culture of security awareness and training within an organization is crucial for effective devsecops practices
* Real-time monitoring and response to vulnerabilities are essential for minimizing damage in case of a breach.


## Keynote: State of the Foundation - Jim Zemlin, Executive Director, The Linux Foundation

URL: [https://www.youtube.com/watch?v=IXrdd0dd2ZU](https://www.youtube.com/watch?v=IXrdd0dd2ZU)

 * Jim Zemlin, Executive Director of The Linux Foundation, discussed the state of open source at The Linux Foundation's event in Bilbao, Spain.
* He highlighted the importance of humility, helpfulness, and hopefulness in the open source community.
* Discussed concerns around licensing changes and the maturing of open source businesses.
* Hashicorp's recent change to a business license for Terraform was discussed, with Zemlin arguing that it's not a sign of impending doom for open source but rather a natural evolution as companies grow.
* Open Source projects need better education on the risks of centrally owned copyright regimes and single companies having the ability to change licenses later.
* Introduced Sebastian Stadel, core contributor to OpenTofu, a drop-in replacement for Terraform, which is being developed neutrally under the Linux Foundation.
* David Rahal from Allianz Indonesia discussed their use of open source software and their investment in OpenTofu.
* Carlos Clemente from ExpressVPN discussed his experience working with open source and his excitement about OpenTofu.
* Zemlin discussed concerns around large language models and the potential for negative outcomes, but emphasized that open source always creates more good than bad.
* Linux Foundation is creating a community data license to make it easier for people to share large datasets for LLM development.
* Discussed the importance of addressing intellectual property concerns in open source communities and the role regulators can play in clarifying terms around derivative works.
* Announced the UXL Foundation, a new initiative to build an accelerated computing ecosystem with unified standards.
* Rod Burns and Sanjeev Vivek from Intel and Fujitsu respectively discussed their involvement in the UXL Foundation and the importance of open standards for building software accelerators.


## Using Kaskada to Do Real Time AI - Mick Semb Wever, DataStax

URL: [https://www.youtube.com/watch?v=IlKqwlQSmwE](https://www.youtube.com/watch?v=IlKqwlQSmwE)

 * Mick Semperwever, a committer and PMC chair of Apache Cassandra, talks about using Kaskada for real-time AI in RAG apps.
* He emphasizes the importance of open source and shares his background with open source projects, including Cassandra.
* He explains that companies today are moving towards open source products and strategies, and mentions Cascada as a real-time AI platform for RAG apps.
* Cascada was started a couple of years ago to address the missing piece in ML platforms for real-time feature engineering and inference.
* It is a native Python implementation that is faster than Spark streaming, and uses a declarative reasoning abstraction layer and a custom DSL language called Fennel.
* Cascada is written in Rust and uses Apache Arrow to take advantage of GPU performance.
* He shows an example of using Cascada to create embeddings from data and make predictions based on user sessions in real-time.
* He also mentions the importance of vector search and how Cascada can handle it efficiently, as well as its ability to handle large datasets and provide accurate results quickly.
* He briefly touches on the use cases for Cascada in industries such as retail, finance, and customer service.


## Using Machine Learning Models in JavaScript Application - Aileen Villanueva Lecuona, Endava

URL: [https://www.youtube.com/watch?v=J7-EZCj96_Y](https://www.youtube.com/watch?v=J7-EZCj96_Y)

 * Aileen Villanueva Lecuona talks about using machine learning models in JavaScript applications
* She mentions her background as a software developer and her interest in AI
* Machine learning has been around for a long time but is constantly evolving
* She chooses to focus on TensorFlow.js for this talk
* TensorFlow.js allows running machine learning models in the browser or Node.js
* Deep learning is a type of machine learning used for complex problems like generative AI and self-driving cars
* JavaScript ecosystem has grown significantly with tools like TensorFlow.js and libraries from Google
* JavaScript can be used for web, server, mobile, IoT, and more
* TensorFlow.js is backed by Google and updated every year
* She covers the basics of machine learning, deep learning, supervised learning (regression example), and unsupervised learning (anomaly detection example)
* TensorFlow.js has a model hub with pre-trained models that can be used directly in applications
* Model conversion is required for some models to work with TensorFlow.js
* She mentions using the layer API to modify models for specific use cases and the core ops API for linear algebra operations
* Running machine learning models in the browser has benefits such as no server needed, lower latency, and offline access to models
* She also talks about finding the best model for a use case and deploying it responsibly with proper data.


## Keynote: Creating Sustainable Value – Open Source Technology Delivers the Essential..- Vivek Mahajan

URL: [https://www.youtube.com/watch?v=NPMw50pzo8I](https://www.youtube.com/watch?v=NPMw50pzo8I)

 * Speaker is talking about open source technology and its role in creating sustainable value for businesses
* Feedback from 1800 business leaders shows increasing importance of sustainability and digitalization, with a focus on open source
* Fujitsu, a $35 billion revenue company, has seen major polarization in social values, with a need for both sustainability and digitalization
* Digitalization and sustainability are interlinked and open source is a key accelerator
* Fujitsu has a long history of collaborating on open source projects, including Mission critical systems like the Fugaku supercomputer
* Key focus areas: Creating an innovative ecosystem, Web 3, and the Fujitsu Kozuchi AI platform
* Fujitsu Monaka is a world-first two nanometer chip driving high performance computing, focused on power efficiency and open source collaboration
* Web 3 is becoming increasingly important and Fujitsu is building open source code for multiple blockchain integration and security
* The Kozuchi AI platform focuses on human sensing, explainable AI, and addressing issues like auto ML and black box nature of generative AI models
* Open source collaboration helps alleviate the lack of qualified data scientists and makes widely used technologies more accessible.


## Cloud-Native MLOps Platform for Python- and ML Engineers - Joan Fontanals Martínez, Jina AI

URL: [https://www.youtube.com/watch?v=Q7N3RVSjy0M](https://www.youtube.com/watch?v=Q7N3RVSjy0M)

 * The presentation is given by Joan Fontanals Martínez, Principal Engineer at Jina AI.
* Jina AI is a company founded around 3 years ago with about 50 members distributed globally.
* Overview of ML apps and challenges in deep learning powered applications.
* Introducing the concept of MLOps platform and mentioning Gina, an open-source framework provided by Jina AI.
* Docker is used for modularizing models and data, with a focus on building PoCs locally.
* Vector databases are introduced as a solution for indexing and retrieving data seamlessly.
* Code snippets demonstrate how to build and serve an ML application using Gina.
* Discussion of the importance of observability in serving models and the role of Kubernetes in scaling applications.
* Comparison of Gina with other MLOps platforms and a mention of its open-source status and ease of use with Python, TensorFlow, and gRPC.
* Recap of the benefits of using Gina for ML deployments, including automation and scalability.

Note: The transcript is quite long, so it's essential to read or listen to the original video presentation for a more comprehensive understanding.


## OpenJS and Security Updates... - Robin Ginn, Joe Sepi, Paloma Oliveira, Bethany Griggs, Erick Zhao

URL: [https://www.youtube.com/watch?v=R3Eq-_4PAX0](https://www.youtube.com/watch?v=R3Eq-_4PAX0)

 * Robin Ginn, executive director of OpenJS Foundation, discusses the importance and relevance of JavaScript with over 2 billion websites using it
* OpenJS Foundation supports the entire JavaScript ecosystem by ensuring projects stay open long term and protecting maintainers
* Discussion on misconceptions about the foundation's role in open governance work
* Highlighting of successful projects under the OpenJS Foundation like Node.js, which received significant funding from Google, Microsoft, and The Sovereign Tech Fund for security updates
* Bethany Griggs from Red Hat shares her experience as a product manager for a node.js project and mentoring others in the community
* Eric Zhao, maintainer of Electron, discusses his experience maintaining the project and the importance of volunteer contributions and open governance model.


## Cross-dimensional Careers: Transitioning from Frontend to Backend - Jennifer Creighton & Wes Todd

URL: [https://www.youtube.com/watch?v=WwENhYmoI1I](https://www.youtube.com/watch?v=WwENhYmoI1I)

 * Jen and Wes discuss transitioning from frontend to backend development with a focus on their personal experiences
* Jen started as a frontend engineer, but felt the need to learn backend due to negative comments about frontend being easy and motivated by potential for higher pay
* Wes had a disdain for the browser and spent most of his career learning backend, but made a late-career switch to frontend out of boredom and to combat stagnation
* Switching domains can be tricky, but there are commonalities between frontend and backend knowledge that can be applied
* Frontend is specifically web-based JavaScript and mobile native applications, while backend is JavaScript-based server runtimes, observability, databases, and data pipelines
* Making the switch involves finding a clear path forward, which may involve taking small steps or making a larger leap depending on individual circumstances
* Learning new technologies and tools can be challenging, but resources like books, mentors, and online courses are available to help
* Key skills for backend development include designing principles, security best practices, and debugging
* Understanding the fundamental concepts of both frontend and backend is important, as they share some similarities but also have distinct differences
* Communication skills are essential in the software industry, regardless of role or discipline
* Tools like terminal and editors are transferable between frontend and backend roles, and debugging skills are valuable in both areas
* Understanding networking and server architecture is crucial for backend development, as is understanding how to scale applications and manage latency
* Observability, logging, and tracing are essential for diagnosing and resolving issues in the backend
* Frontend and backend have different concerns when it comes to performance, with frontend focused on time-to-paint, size, and asset optimization, and backend focused on concurrency, parallelism, and observability.


## SEAPATH: A LF Energy Project for Critical Infrastructure with an... - Eloi Bail & Mathieu Dupré

URL: [https://www.youtube.com/watch?v=XODkyJ8I1Cc](https://www.youtube.com/watch?v=XODkyJ8I1Cc)

 * Eloi Bail and Mathieu Dupré presented CPAs (Critical Protection Architecture), an open source project for critical infrastructure, mainly in the energy sector
* Based in Montreal and Paris, Industrial Products is a company involved in different sectors including medical devices, robotics, avionics, entertainment, and energy
* CPAs is an open source solution for substations, which manage electricity distribution grids
* The project aims to use virtualization with a multi-vendor approach and aggregate Open Source software related to the power industry
* Challenges include performance expectations, real-time network latency, cyber security, and managing vulnerabilities
* CPAs has two flavors: one based on YouTube and another on Debian
* The project follows best practices such as openSSF, testing processes, continuous integration (CI), and security tracking
* Goals include maintaining the system secure, reducing vulnerabilities, providing responsibility information, and ensuring interoperability
* SPDX (Software Package Data Exchange) is used for software bill of materials (SBOMs) and vulnerability tracking
* The project uses automated tools for building SBOMs, analyzing dependencies, and checking vulnerabilities
* Challenges include managing large amounts of vulnerability data, dealing with false positives, and ensuring mitigations are implemented effectively.


## A New Data Model for Time Series Data Processing - Jeff Tao, TDengine

URL: [https://www.youtube.com/watch?v=_inqNfD1dkk](https://www.youtube.com/watch?v=_inqNfD1dkk)

 * Jeff Tao, CEO of TDengine, talks about a new data model for time series data processing
* Time series data used in various industries such as finance, energy, transportation, and manufacturing
* Purpose of time series data: monitoring change, predicting, and abnormal detection
* Challenge with time series data: large volume, real-time processing, and deletion of old data
* TDengine's new data model: one table one data connection point one sensor one minute multimeters
* Benefits of the new data model: efficient writing, faster read operations, easier compression, and simpler design
* TDengine compared to other time series databases: InfluxDB, TimescaleDB, and OpenTSDB
* Efficient aggregation using soup table concept
* Super table design for efficient aggregation
* TDengine benchmarks show better performance than InfluxDB and TimescaleDB
* Distributed design for scalability and high availability
* TDengine is open-source with editions available for single machines, clusters, and clouds.


## Secure the Linux Kernel with eBPF Linux Security Module - Vandana Salve, Independent Consultant

URL: [https://www.youtube.com/watch?v=_tG1G6Oewc4](https://www.youtube.com/watch?v=_tG1G6Oewc4)

 * Wandera Salve, senior software architect at Micron, discusses securing Linux kernel using BPF LSM
* Agenda: understanding security basics, existing security frameworks in Linux kernel, and BPF's role
* Existing security frameworks: audit framework, monitoring framework, and enforcement policies (discrete access control, mandatory access control)
* BPF fits well due to its ability to monitor signal events, process activities, and implement security hooks
* Demonstration of securing Linux kernel with SELinux LSM as an example
* SELinux LSM: implementation, hook attachment, policy enforcement, and action taken upon policy violation
* BPF provides a secure execution environment and eliminates the possibility of system crashes caused by malicious modules
* The use of BPF programs to implement policies without configuring kernel or using kernel modules is recommended.


## Sponsored Session: Building Python Binding for the Delta Lake Library in Rust - Florian Valeye

URL: [https://www.youtube.com/watch?v=aRcfmjimv6I](https://www.youtube.com/watch?v=aRcfmjimv6I)

 * Florian Valeye, data engineer at Bug Market, introduces himself and his role in the Delta IRS project within the Delta Lake ecosystem
* Delta Lake is an open-source technology created by the Linux Foundation that provides a scalable transaction log and storage layer for data lakes
* Python and Rust combination: Delta Lake is primarily written in Java and Scala, but using Rust for data processing can be beneficial due to its reliability and performance
* Rust's memory management helps mitigate common challenges in low-level programming languages like C
* Polars is a blazing fast data frame library in Rust that can be used with Delta Lake to create Python bindings, making it easier to incorporate both libraries into the data ecosystem
* The benefits of using Python and Rust together include:
  + Improved connectivity between the two libraries
  + Faster performance with Rust's core library
  + Use of high-level APIs provided by Rust for efficient, reliable call runtimes

* Delta Lake provides features like ACID transactions, time travel, and unified API calls to handle data stored in different cloud providers
* Using Python bindings to access Delta Lake can be beneficial when:
  + You don't need to spin up a large cluster or only require read access for small portions of the table
  + Triggering actions using Python without spinning up a cluster is more efficient
  + Event-based processing with smaller resources, such as AWS Lambda, can handle the processing part
* Rust and Java are used together in Delta Lake to create a simpler development process by connecting connectors and providing a kernel for Rust
* Polars' Python binding, implemented using PyO3, has been instrumental in increasing the usage of Delta Lake within the Python community.


## Digital Forensics with Container Checkpointing - Daniel Simionato & Javier Martinez, Sysdig

URL: [https://www.youtube.com/watch?v=cQkCOZWjXNs](https://www.youtube.com/watch?v=cQkCOZWjXNs)

 * Daniel Simionato and Javier Martinez discussing digital forensics, specifically container checkpointing
* Digital forensics: retrieving, analyzing, preserving electronic data related to criminal activity
* Container checkpointing: saving the equivalent state of a container like a snapshot for faster recovery in case of a criminal attack
* Checkpointing could allow investigators to quickly retrieve criminal evidence without the attacker being aware and remove their traces
* Cryo project started as proof of concept in 2011, first patch got merged into Linux kernel in November 2013
* Container checkpointing involves precise control over CPU registers, ram memory, and other details
* Live migration process can be complex: copying definition, freezing processes, applying security checks
* Podman supports container checkpointing with exporting a file containing the checkpointed state of a container
* Kubernetes also uses checkpointing for live migrations since version 1.25 (Graduated Alpha)
* Checkpoints are important for digital forensics investigations as they preserve exact container states, including process IDs and open files or sockets.


## Improving the Security of a Large Open Source Project One Step... - Michael Dawson & Rafael Gonzaga

URL: [https://www.youtube.com/watch?v=eTt6XnPaNa4](https://www.youtube.com/watch?v=eTt6XnPaNa4)

 * Michael Dawson and Rafael Gonzaga discussing improving security in large open source Node.js projects
* Node.js is widely used with over a billion downloads last year, co-funded by OpenJS Foundation
* Reactive approach: addressing vulnerabilities reported to the project
	+ Challenges with communication and understanding threat models
	+ Example: reading huge files can lead to security issues if not properly checked
* Proactive approach: creating initiatives for security improvements across the project
	+ Importance of having dedicated resources to focus on security
	+ Collaboration between teams and individuals to address vulnerabilities
	+ Use of tools like HackerOne to report and handle security issues
* Challenges in handling security vulnerabilities
	+ The impact of false positives and the cost to the ecosystem
	+ Difficulty in managing email notifications and triaging reports
	+ Need for a larger number of triage team members
	+ Importance of clear communication and documentation
	+ Balancing resource availability and addressing urgent vulnerabilities
* Current initiatives for improving security in Node.js projects
	+ Threat modeling and risk assessment
	+ Automation for dependency updates and vulnerability checks
	+ Implementing secure best practices and guidelines
	+ Continuous integration (CI) and continuous delivery (CD) improvements
* Upcoming initiatives
	+ Secure release process
	+ Review build process and supply chain security
	+ Permission model and access control
* The role of individuals and organizations in contributing to security improvements
	+ Encouraging a culture of security within the community
	+ Supporting the OpenJS Foundation and other initiatives
	+ Reporting vulnerabilities and working together to resolve them.


## Y2038 and Utmp/Wtmp on 64bit Systems - Thorsten Kukuk, SUSE

URL: [https://www.youtube.com/watch?v=hYA_SuxAg14](https://www.youtube.com/watch?v=hYA_SuxAg14)

 * Thorsten Kuckuck from SUSE discusses Y2038 and Utmp/Wtmp on 64-bit systems
* Y2038 problem refers to the Unix time representation which will roll over in 2038, causing issues with dates and timestamps
* Utmp and Wtmp are system logs that record user login and logout activities
* With the transition to 64-bit systems, these logs may cause problems due to the large file sizes and the need for new time fields
* Solutions include replacing or modifying the current logs, implementing SQLite databases, or using alternative solutions
* Other topics discussed include application performance issues, file formats, and compatibility with different systems
* It is important to plan and prepare for the transition to 64-bit systems to avoid potential issues.


## Tutorial: Getting Started with Serverless WebAssembly and Spin - Mikkel Mørk Hegnhøj, Fermyon

URL: [https://www.youtube.com/watch?v=iqUbsrqtijY](https://www.youtube.com/watch?v=iqUbsrqtijY)

Split:[4229, 4229]
 * The tutorial is about getting started with Serverless WebAssembly and Spin, an open-source framework by Fermyon.
* Migel Mørk Hegnhøj from Fermyon will lead the workshop.
* Topics covered include: server side WebAssembly, Spin framework features, deployment on Firan Cloud and Kubernetes, and use cases.
* Server side WebAssembly is a specification that enables running WebAssembly outside of a browser. It's important for small binary size, fast startup time, and portability.
* The workshop will involve creating a new application using the Spin CLI and building it with various programming languages like Rust, Go, or JavaScript.
* Spin is a developer tool for building serverless WebAssembly applications, providing a simplified experience and easy access to APIs and services.
* The framework supports large language models for inference and has a key-value store for persistent cache. It also offers a SQL database feature.
* The tutorial will cover the basics of Spin, including its core concept, triggers, configuration, and deployment options (Firan Cloud or Kubernetes).
* Use cases include cloud plugins, IoT, function services, and AI applications.
* The workshop includes building a Magic Eight Ball application using JSON API, SQL live feature, and Spin Hub for deploying and sharing applications.
* Participants are encouraged to ask questions throughout the tutorial.
 * Speaker is giving a tutorial on getting started with Serverless WebAssembly and Spin, a framework for building web applications using WebAssembly
* Spin uses the Magic 8 Ball as a metaphor for making decisions in development
* To get started, create a new Spin application and write function code. Use Spin watch to iterate and see changes in real-time
* Spin supports various languages including TypeScript and Go
* Spin has an HTTP trigger feature which allows for building APIs
* When deploying, Spin builds WebAssembly using Cargo and runs it on a Caro server
* Spin's Magic 8 Ball function uses the import SDK and Annotated Handler macro to handle requests and return answers in JSON format
* Speaker mentions implementing another function and creating a type function structure for small libraries
* Discusses using the HTP component annotated function Handler to handle HTTP requests and set answer types
* Speaks about creating an LLM (Large Language Model) based application with static files served by Spin
* Talks about deploying the application on Cloud and integrating it with AI models for inference
* Discusses using capabilities for access control and security in Spin components.



## URUNC: A Unikernel Container Runtime - Georgios Ntoutsos & Anastassios Nanos, Nubificus LTD

URL: [https://www.youtube.com/watch?v=lXREy2sylTY](https://www.youtube.com/watch?v=lXREy2sylTY)

 * URUNC: A Unikernel Container Runtime presented by Georgios Ntoutsos and Anastassios Nanos of Nubificus LTD
* Focus on building a container runtime for unicorn VMs (Unikernel Virtual Machines) using Go
* Lightweight containers with faster spawn time, run anywhere, scalable, and truly isolated using hardware-assisted extensions
* Challenge: deploying unicorn containers in a cloud-native way due to packaging issues
* URUNC handles unicorn VMs directly, making it extensible and easy to add hypervisors
* Image building uses a specialized image builder tool (Bima) that copies the binary and provides specific labels for identification
* Execution flow: containerd invokes URANus which creates a new process, sets networking and storage components, and starts the container using hooks
* Unicorn VMs offer strong isolation and better scalability compared to traditional containers and VMs
* URUNC is compatible with Kubernetes, can be deployed as a sidecar container, and offers improved serverless computing by optimizing resource usage and reducing memory footprint.


## Sponsored Session: How to Survive to High Demanding Services - Endika Gandarias

URL: [https://www.youtube.com/watch?v=lpxb8TS0DB4](https://www.youtube.com/watch?v=lpxb8TS0DB4)

 * Indik Gandarias has been working in the Innovation Technology Surveillance Department of the Basque Government since 2016.
* Ichi is an online tool promoted by the Basque government to promote the use of the Basque language and solve translation problems between Basque, English, French, and Spanish.
* The tool uses AI models trained on public and government data to perform text-to-speech operations and translations.
* The system is designed for high demand services and can handle over 400,000 requests per hour, with nearly 300,000 distinct IP addresses making requests.
* The service runs on a Kubernetes cluster to ensure resilient services and uses Fluentd for collecting logs and building dashboards to monitor service information.
* To make it easier for developers to read application logs and send data, a custom Fluentd image was created with a JavaScript program script that installs easily and is familiar to developers.
* The configuration file sets the path to the log file, rotates log files, and runs the Fluentd script to read logs and send data.
* The service uses error handling mechanisms like alerting on specific conditions and using Microsoft Teams for notifications.
* Synthetic tests are used to test APIs and websites and send notifications when errors occur.
* Shadow deployment is used to deploy multiple versions of a service in parallel for testing and rolling back if necessary.
* Canary deployment is used to gradually roll out new releases and monitor performance.
* To avoid duplicating files, customized directory structures are used and common objects are defined in separate configuration files.
* Jenkins is used to automatically deploy new versions of applications and test them using Podman and JMeter scripts.
* When deploying multiple versions of a video service, the stable version is deployed first and the release candidate version is deployed using Jenkins for testing. The virtual service configuration is then changed to distribute traffic and replicate traffic from the release candidate version. Once the release candidate version is performing well, it can be gradually replaced with the stable version using a canary deployment.
* To improve performance, the load balancer can be configured to balance traffic and use TLS security mode. The architecture should also be designed with basic AR architecture principles in mind.
* The system uses rolling updates to deploy new versions of applications while minimizing downtime and using stealth mode for added security.
* To contact the speaker for any questions, please see the provided contact info.


## X86/Pie: Make Kernel Image's Virtual Address Flexible - Wenlong Hou, Ant Group

URL: [https://www.youtube.com/watch?v=mywXUxR0tkA](https://www.youtube.com/watch?v=mywXUxR0tkA)

Error


## Adding Functionality to Make Windows Games Run Faster on Linux - Muhammad Usama Anjum, Collabora

URL: [https://www.youtube.com/watch?v=sD1G2B-2Q0k](https://www.youtube.com/watch?v=sD1G2B-2Q0k)

 * Usama from Collabora working on making Windows games run faster on Linux by improving kernel window APIs
* Problem: Games need to find and manage specific pages of memory, which can be complex due to different semantics and handling mechanisms
* Need to translate window APIs for Linux user space efficiently
* Linux kernel already has some mechanisms like AMP protection and write-protect memory, but improvements are needed
* Soft dirty flag introduced in memory management, causing issues with merging VMAs (Virtual Memory Areas)
* Solution: Add an octel-based soft dirty flag to handle specific ranges of memory atomically
* User fault FD (File Descriptor) and write protect asynchronous feature added for improved performance and user space messaging
* Performance boost expected by reducing communication between kernel and user space, especially with large data sets
* Current limitations in memory management, such as the size increase required for VMAs, are being addressed
* Future improvements include adding flags to ioctls (Input/Output Control functions) and handling different types of memory.


## Automated Full System Testing on Hardware with OpenQA - Laurence Urhegyi & Sam Thursfield, Codethink

URL: [https://www.youtube.com/watch?v=xENaEZL16sc](https://www.youtube.com/watch?v=xENaEZL16sc)

 * Speakers: Lawrence Urhegyi (project manager at Codethink) and Sam Thursfield (senior engineer at Codethink)
* Topic: Automated full system testing on Hardware using OpenQA in the embedded industry, specifically in automotive projects.
* Background: Increasing software complexity in the automotive industry, with exponential growth in code size, making testing critical but often overlooked.
* Previous work: Combining Lava and OpenQA for testing Linux-based systems, reducing regression testing burden by making it more accessible.
* New advantages: Improving testing efficiency by focusing on end-to-end tests, automating repetitive tasks, and using open-source tools like OpenQA to optimize the testing process.
* Overview of OpenQA: Established testing framework designed for test automation in desktop environments, with web-based reporting and powerful model architecture.
* Needle testing: Comparing screenshots of user interfaces with JSON files to ensure they match, enabling rapid detection of changes and reducing manual effort.
* Testing virtual machines vs. specialized operating systems on real hardware: Simplifying the process of testing specialized operating systems on real Hardware using OpenQA.
* Custom Hardware: Adapting OpenQA for testing custom and specialized Hardware with remote control, allowing for more efficient and effective testing.
* Remote access to testing rigs: Control and test Hardware from anywhere, reducing travel costs and improving overall efficiency.
* QAD (quality assurance daemon): Developed by Codethink to inject events and get screenshots on demand, enabling more comprehensive testing.
* Testing complex systems: Automating the testing of complex systems with multiple components, such as USB switchers, and ensuring compatibility across different platforms.
* Collaborative testing: Encouraging community contributions to improve OpenQA's capabilities and make it a more powerful tool for testing various projects.


## Lessons Learned Migrating an Existing Product to a Multi Tenant...- Natalia Angulo & Carlos Sanchez

URL: [https://www.youtube.com/watch?v=xc-x4HuRvmQ](https://www.youtube.com/watch?v=xc-x4HuRvmQ)

 * The speakers are Natalia Angulo and Carlos Sanchez, they work at Adobe and have experience with open source projects and Kubernetes.
* Adobe Experience Manager (AEM) is a content management system used by many enterprises, which was previously running on a monolithic Java application using Open Source components.
* AEM team wanted to move to a multi-tenant Cloud native environment using Kubernetes for better isolation, scalability, and security.
* Reasons for moving to Kubernetes: Different customers in different regions requiring separate availability zones, microservices architecture trend, and managing customer environments themselves with self-serve platforms.
* Challenges encountered during the migration included dealing with various teams building services using different languages (Java, Node.js), ensuring security while allowing customers control over their environments, and managing Kubernetes clusters for each customer.
* Solutions used during the migration: Using a service mesh pattern with sidecar containers, managing custom resources with operators like Flux and Helm, and using Argo rollouts for advanced deployment strategies.
* Important aspects of migrating to Kubernetes include understanding resource requests and limits, handling memory management in JVM applications, and setting up auto-scaling.
* Advice given: Trusting JVM ergonomics, setting proper resource limits, and using different garbage collectors depending on the use case.


## Breaking Out of the Open Source Burnout Cycle - Nigel Brown, Intuit

URL: [https://www.youtube.com/watch?v=0p3JrEl_mOI](https://www.youtube.com/watch?v=0p3JrEl_mOI)

 * Nigel Brown, a senior developer advocate at Intuit and open source enthusiast, shares his experiences with burnout in the open source community
* Draws a comparison between different types of stories, using the Cinderella story as an example for the cycle of open source burnout
* Describes the honeymoon phase of open source projects, where enthusiasm and progress are made
* Discusses how priority shifts can lead to resentment and burnout
* Suggests recognizing effort and celebrating accomplishments as a way to break the burnout cycle
* Offers specific advice for individual contributors: time blocking, managing tasks effectively, delegation, and communicating with maintainers
* Emphasizes the importance of setting boundaries and self-care for open source work
* Shares personal experiences of finding energy in travel and focusing on smaller, manageable tasks
* Discusses the importance of clear communication and community management in open source projects.


## Laying the Foundation on OSS Environmental Sustainability - Max Körbächer, Liquid Reply

URL: [https://www.youtube.com/watch?v=1ExjyxQx6B4](https://www.youtube.com/watch?v=1ExjyxQx6B4)

 * Max Körbächer from Liquid Reply, cloud native advocate and founder of a consulting company focused on open source sustainability in the CNCF ecosystem
* Environmental sustainability group within CNCF was founded three years ago, focusing on optimizing system sustainability in cloud native projects
* Discussing current strategies for reducing carbon footprint in the cloud native ecosystem
* Comparison between the carbon footprint of a server and a cow
* Importance of building a cleaner open source world, focusing on optimizing energy consumption in software and infrastructure
* Challenges in measuring and comparing the carbon intensity of different projects and supply chains
* The role of frameworks like SEI and ISO in certifying green software
* Discussion on the importance of transparency and awareness in the open source community regarding sustainability efforts.


## Building an Open Government with Open Code and Open Source - Hans Kristian Flaatten

URL: [https://www.youtube.com/watch?v=4v05Huy2mlw](https://www.youtube.com/watch?v=4v05Huy2mlw)

 * Hans Christian Flaatten speaks about his experience with open source in the Norwegian government, specifically in the Labor Welfare Administration
* He starts by recalling his background in open source, starting with Apache web server and PHP CMS systems
* In the 2010s, he became part of Node.js Foundation and created IoJS, instituted an open governance model
* The Norwegian government's Labor Welfare Administration provides various welfare benefits such as parental benefit, sickness benefit, unemployment benefit, and pension
* He describes the Nordic model as a political system common in Nordic countries characterized by social welfare, free universal healthcare, income distribution, labor market flexibility, strong worker rights, and gender equality
* In the past, government projects were often slow, costly, and error-prone due to long and tedious procurement processes
* The Phoenix project was an attempt to improve the situation by collaborating across authorities and sharing knowledge within the public sector
* He mentions that Norway has a large number of open source repositories in the public sector and encourages developers to contribute back to the community
* In recent years, the Norwegian government has been focusing on autonomous teams, high velocity development, and open source technology
* He highlights the importance of sharing learning and collaboration within organizations, as well as using open source tools for security and design systems.


## Understanding Observability in Kubernetes - Divine Akachukwu Odazie, Independent

URL: [https://www.youtube.com/watch?v=6wCjKTwPS9U](https://www.youtube.com/watch?v=6wCjKTwPS9U)

 * Observability vs Monitoring: observability provides insight into application behavior, performance, and diagnosing issues in complex systems, while monitoring collects data to ensure components are performing as expected.
* Kubernetes built-in tool for observability is Cube CTL, which can be extended with external tools like Prometheus and Grafana for better visibility.
* Observability best practices include setting alerts and notifications, creating dashboards, and using telemetry data for deeper analysis.
* Kubernetes components emit metrics in various formats (text-based, JSON, etc.) that can be used to gain insight into resource utilization, system performance, and application behavior.
* Logging is an essential aspect of observability, providing detailed information about events and their context. In Kubernetes, logs can be collected and stored for analysis using tools like Elasticsearch and Fluentd.
* Profiling, tracing, and monitoring are key components of observability, helping to identify bottlenecks, optimize performance, and diagnose issues in complex systems.
* Observability is particularly important in microservices architectures, where services may be deployed across multiple clusters and environments.
* Tools like Grafana and Prometheus can be used to create visualizations and dashboards for monitoring and observability, while Jager and Zipkin are popular distributed tracing tools.
* Secure access to data is a critical consideration when implementing observability solutions in production environments. Authentication, authorization, and encryption should be used to protect sensitive information.


## Beyond the Trend: Authentic Approaches to Fostering Diversity in Open Source - Jessica Tegner

URL: [https://www.youtube.com/watch?v=EHqCaUVCOqQ](https://www.youtube.com/watch?v=EHqCaUVCOqQ)

 * Jessica Tegner, 20-year-old computer science student, talks about fostering diversity in open source
* Started a popular Python library project called Pipe Pandok as part of GitHub's accelerator program
* Discusses her experience working with proprietary and open source software at companies like Uber
* Explains the concept of Equity, Diversity, Inclusion (EDI) and its importance in the tech industry
* Shares her perspective as a minority group member (women and disabled)
* Talks about diversity hiring, imposter syndrome, and diverse leadership
* Offers tips for smaller open source projects to be more inclusive
* Discusses the importance of communication, documentation, and mentoring programs in promoting diversity
* Encourages openness to experimentation and collaboration in achieving equity, diversity, and inclusion.


## Lightning Talk: Building Ersilia: Open Source AI Modeling for Infectious Disease...- Dhanshree Arora

URL: [https://www.youtube.com/watch?v=EnsQYpO2YB8](https://www.youtube.com/watch?v=EnsQYpO2YB8)

 * Dhanshree Arora, machine learning engineer and open source maintainer of Ersilia
* Joined Outreach intern at Ersilia in December 2022
* Problem: Large income disparity leads to neglected diseases in low-income countries
* Ersilia is a nonprofit building a low-code tool for early stage drug discovery in low resource settings
* Completely open source, licensed under GPL3, and entirely volunteer-driven
* Partnerships with universities, industry volunteers, and organizations like Outreachy
* Cilium Model Hub: incorporates AI models from various stages of drug discovery research
* Simplest case: binary classification targeting a drug candidate for a specific pathogen (e.g., malaria or influenza)
* Drug candidates are represented as machine learning models and run through an ML workflow
* Ersilia Model Hub includes existing research models, molecular embeddings, activity target prediction, and chemical space exploration
* Over 5,000 commits across the repository
* Contributor tooling built by the community of over 70 contributors spread across different time zones
* Funding through grants (e.g., GitHub Sets) and internships (e.g., Outreachy program)
* Published papers in reputable journals like Nature
* Work on developing novel drug candidates happening in Africa and other parts of the world.


## Diversity in Open Source, an Asian Perspective - Masae Shida, VMware

URL: [https://www.youtube.com/watch?v=FzIEU3PfmuI](https://www.youtube.com/watch?v=FzIEU3PfmuI)

 * Masae Shida, Staff Program Manager at VMware's Open Source Community Strategy, discusses diversity in open source from an Asian perspective
* Representing data on Open Source participation in Asia
* Asian countries have great potential to be a driving force in Open Source due to cultural diversity and large population
* Barriers to strong Open Source participation in Asia:
  + Limited representation in community leadership positions
  + Language barrier
  + Time difference limitation
  + Cultural differences
* Reasons for limited participation:
  + Lack of support from companies
  + Fear of confrontation or lack of confidence
  + Lack of role models
* Ways to overcome these barriers:
  + Encouraging more Asian participation in Open Source communities
  + Addressing language and cultural differences
  + Providing flexible work hours and remote collaboration opportunities
  + Encouraging companies to support employee involvement in Open Source projects
* Recent improvements:
  + Younger generations are more comfortable with English and open to contributing to Open Source projects
  + Technology tools like translation software and communication platforms have made it easier for non-native English speakers to participate.
* Conclusion:
  + The key is to create a welcoming, inclusive culture that values diversity and encourages open communication.
  + Asian people need to make an additional effort to lead and contribute to Open Source communities.


## Istio and Cilium: Pushing the Boundaries of the Possible on Zero-Trust - Lin Sun, Solo.io

URL: [https://www.youtube.com/watch?v=H4iJQaHOB0A](https://www.youtube.com/watch?v=H4iJQaHOB0A)

 * Lin Sun from Solo.io speaks about Istio and Cilium, pushing the boundaries of zero-trust architecture
* Lin introduces himself as a founding member and technical oversight committee member of Istio project, also the author of two books on Istio and Ambient
* Psyllium is a cloud native solution providing securing and observing network connectivity for workloads running in Kubernetes or VM environments
* Psyllium uses eBPF technology to provide faster and safer processing, allowing direct kernel access for sandboxed programs
* Psyllium enhances Kubernetes Network Policy with visualization tool Hubble for troubleshooting network problems
* Istio provides a service mesh framework with programmable interface for managing application communication securely
* Ambient is a new deployment model proposed by Istio allowing applications to run without sidecars
* Zero Trust architecture is important in today's environment as it assumes nothing and verifies everything, enforcing least privileged access and defense in depth
* Traditional security models like firewalls may not be enough as they focus on edge security and monolithic applications are moving to microservices
* Defense in depth can be achieved by layering security measures such as network policies, Istio sidecar proxies, and eBPF sandboxing
* Psyllium Network Policy supports layer 3 and 4 traffic control and is more flexible than Kubernetes Network Policy with enhanced features like dline policy and observability history UI.


## Implementing the OpenSSF Best Practices Badges & Scorecards Into Your Project - CRob & David Wheeler

URL: [https://www.youtube.com/watch?v=Hw3LbIXeZ2k](https://www.youtube.com/watch?v=Hw3LbIXeZ2k)

 * Chris Robinson (Cobe) and David Wheeler discuss implementing OpenSSF's Best Practices Badges & Scorecards into projects
* OpenSSF focuses on improving security in Open Source software through various initiatives
* The Best Practices Working Group is dedicated to identifying, documenting, and promoting good security practices
* The group divides work roughly into three categories: project identification, developer adoption, and learning and education
* The HandsOn Developer Platform (renamed from SKF) offers interactive labs for developers to learn about security best practices
* OpenSSF's Security Scorecard is a representative project that assesses software based on documented security practices
* Companies like Intel use the scorecard as part of their open source management practices, providing valuable information for consumers
* The Scorecard automatically scores projects on a scale from 0-10 in various areas, including vulnerability reporting and testing
* Projects can integrate the scorecard analysis into GitHub Actions or run it manually via command line API
* The Rest API allows querying data from large public datasets for detailed information about open source projects' security practices.


## Is ChatGPT (and Other AI) the Enemy of Diversity? - Quiana Berry, Red Hat

URL: [https://www.youtube.com/watch?v=KyoUxP-WIxg](https://www.youtube.com/watch?v=KyoUxP-WIxg)

 * Quiana Berry from Red Hat discussed the role of AI in promoting diversity, equity, and inclusion (DEI) at OSS Europe.
* She highlighted the potential of AI to create opportunities while perpetuating existing biases and systemic inequality.
* Representative conversation around ethical AI is essential, especially for marginalized communities who are often overlooked in tech.
* The impact of AI on human rights, privacy, and societal issues was addressed.
* Examples of AI ethics gone wrong include discriminatory hiring, health care, and law enforcement applications.
* Potential benefits of AI include assisting in education, increasing productivity, and aiding in disaster relief efforts.
* The need for open source community involvement in ethical AI development was emphasized.
* The importance of transparency, fairness, and equity in AI governance was discussed.
* Balancing the benefits and risks of AI was recommended through careful consideration and regulation.


## OSPOs & Transition Paths for Regulated Environments - Ana, Remy, Nico, Clare, Thomas

URL: [https://www.youtube.com/watch?v=MH04mHkIDu0](https://www.youtube.com/watch?v=MH04mHkIDu0)

 * The speakers are from various industries with experience in open source program offices (OSPOs) and transition paths for regulated environments.
* Anna Dillon: Executive director of Inner Source Commons, has worked on folk-based OSPOs in academia and the science foundation.
* Nico Rice: Grid operator in Netherlands, background in electrical engineering, working on open source policy process tooling.
* Thomas Steenbergen: Helps organization adopt open source, background in automotive industry, focusing on facilitating open source collaboration and supply chain management.
* Claire Dillon: Program manager at Open Group Practice, building a best practice tool for effective and sustainable open source offices, working with regulated industries.
* Topics discussed include the challenges of building an open source initiative in a regulated environment, convincing different stakeholders to collaborate, and regulatory compliance in various industries.
* The speakers shared examples from their experiences, such as collaboration between financial institutions on open source projects and the role of open source in healthcare organizations.
* Remy Cosmas: Open source lead at Medicare Medicaid service, has helped stand up the first hospital's OSPO, and previously worked at Red Hat and RIT.
* Public sector tends to have a conservative approach to open source and risk, but can benefit from collaboration and standardization.
* Open Source Readiness: Tackling the problem of culture change needed for people to work collaboratively in an open source environment.
* Aliana: Example of an open source project that started as a power grid model application, became a library, and involved data scientists contributing code and fixing bugs.
* Mercedes-Benz: Old companies like Mercedes have been resistant to open source due to fear of losing control and antitrust concerns, but are now adopting it for business process management and collaboration.
* Cyber Resilience Act: Lawmakers in Europe are engaging with the tech industry on open source and AI regulation, and the role of OSPOs in helping companies stay ahead of the game.


## BoF: Positioning Your Next Open Source or Standard Project for Success - Scott Nicholas

URL: [https://www.youtube.com/watch?v=OVLlSDpu2qU](https://www.youtube.com/watch?v=OVLlSDpu2qU)

 * Scott Nicholas, Vice President of Project Formation at Linux Foundation, discussing guidelines for successful open source projects
* Focus on Greenfield technical community preparation, foundation return investment, and neutrality structure
* Clear IP Clarity and license information, simple project focus, effective communication, and documentation are important
* Make decisions publicly, leverage tools and best practices, and provide a welcoming inclusive community
* Transitioning from custom environment to open source requires documentation, clear mission statement, and governance
* Naming is crucial for company decision making and avoiding confusion or trademark issues
* Commercial dependency projects can be approached early for easier decision making
* Documentation is important for due diligence reviews and attracting commercial funding
* Cost savings, problem solving, and new revenue are common motivators for companies to participate in open source projects
* Understanding the company's financial goals and return on investment is crucial when pitching a project for funding.


## Demystifying Platform Engineering with OSS - Gedd Johnson, Defense Unicorns

URL: [https://www.youtube.com/watch?v=OXQbg4qwaj4](https://www.youtube.com/watch?v=OXQbg4qwaj4)

 * Jed Johnson, Software Engineer at Defense Unicorns, discusses platform engineering
* Platform engineering is about standardizing the process of deploying applications and underlying infrastructure
* Devops culture is about shared ownership across entire software life cycle and using the best methodology for a specific context
* Disparate app teams can lead to inefficiencies and silos when implementing devops culture
* Platform engineering aims to balance freedom for developers with opinionation and standardization
* A simple application requires services like health checking, monitoring, logging, and security
* Platform components include Kubernetes, AWS ECS, load balancers, DNS records, and developer portals
* Platform engineering involves creating a reusable CI pipeline, enforcing static code analysis, and securing access to resources
* Platforms can be outsourced to cloud providers like AWS or built using open source software
* The US Air Force's Platform One is an example of a widely adopted open source platform
* Platform engineering involves making technology decisions that are easy for developers to use and operate
* The presentation covers the process of building a Kubernetes-based platform using open source tools like Prometheus, Loki, Grafana, and Istio.


## When Observability Meets Sustainability: A Real World Experience - Marcelo Amaral, Hua Ye & Fan Meng

URL: [https://www.youtube.com/watch?v=OvBdccD8_Jg](https://www.youtube.com/watch?v=OvBdccD8_Jg)

 * IBM China's CTO, Meng, presented IBM's experience in deploying a framework to help companies become sustainable by optimizing hardware infrastructure and applications.
* The motivation for sustainability comes from CEO surveys indicating it will be a priority in the next three years, as well as energy consumption concerns in data centers.
* Sustainability encompasses security, compliance, stability, performance, and efficiency. IBM China aims to apply this full-stack approach to infrastructure optimization and energy reduction.
* The presentation covers IBM's implementation of a framework with levels from infrastructure optimization to application optimization and energy saving techniques like power knob adjustments.
* IBM China implemented a solution connected to their data center, collecting temperature and power consumption metrics to improve sustainability. They also use open-source tools for processing data and creating solutions.
* The Kepler project, which IBM is involved in, aims to calculate energy consumption at the container level in cloud environments using Intel CPUs and IBM Z mainframes.
* Observability is important at different levels - soft engineers, CEOs, and administrators, with various metrics of interest. Energy consumption and CO2 emissions are key metrics for data centers and applications.
* The Capper project involved estimating power consumption in a X86 cloud environment using Kubernetes. Kepler collects power metrics from IBM Z machines and containers to optimize energy usage.
* IBM uses open-source software like Dashi, which helps categorize different tools based on their metric monitoring needs, for managing data center infrastructure. This includes wireless type equipment and network devices.
* IBM also utilizes advanced analytics and machine learning capabilities to prevent application system failures proactively. They use container management tools and automation for efficient deployment and service communication problem resolution.
* The presentation covers energy efficiency improvements using AI-based data analysis, job scheduling strategies, resource management tools, and real-time monitoring dashboards.


## Sponsored Session: Don't Start Over, Start Left: Choosing the Right Open Source... - Martin Hell

URL: [https://www.youtube.com/watch?v=SEOJiTQIJbw](https://www.youtube.com/watch?v=SEOJiTQIJbw)

 * Martin Hell, from Open Text The Brick, discusses choosing the right open source component for secure usage
* Focus on minimizing risks when adding open source components to software
* Discussed using SQL Alchemy instead of Pony ORM due to its popularity and larger community
* Talked about issues with Flask RestPlus and switching to Flask Rest X
* Shift left security approach, testing security early in the development process
* Importance of choosing open source components carefully to avoid negative implications (security vulnerabilities, legal issues, licensing risks)
* Difficulties in evaluating open source projects, comparing popularity, contributor activity, and code quality
* The importance of having a clear policy for open source usage
* Using metrics like popularity, developer influence, and community activity to evaluate open source components
* Choosing SQL Alchemy over Pony ORM based on data analysis
* The abandonment of Flask RestPlus and the adoption of Flask Rest X
* Shift left approach in security testing, scanning containers and infrastructure code as soon as possible
* Importance of considering transitive dependencies and their potential risks
* Evaluating open source components by comparing them based on metrics like popularity, contributor activity, and code quality.


## Sponsored Session: Jumpstart Your Journey to Cloud Native with SUSE..- Miguel Colino & Stacey Miller

URL: [https://www.youtube.com/watch?v=WaZT8CKKw34](https://www.youtube.com/watch?v=WaZT8CKKw34)

 * Miguel Colino and Stacey Miller from SUSE discussing the journey to cloud native using System Manager
* System Manager is an open source infrastructure management solution that manages Zeus Enterprise Server and 16 Linux distributions in a single console
* Reasons for containerization: security, simplicity, scalability
* Security: System Manager provides patch distribution and scheduling with internal calendaring tool and SCAP profile
* Simplicity: reduces overhead of manual patching and allows import of Ansible playbooks
* Scalability: handles millions of instances and workloads in various environments (premise, cloud, hybrid)
* Containerization journey: start with a small application, transition to containerized environments using tools like Podman and K3s, and manage containers with System Manager
* Benefits of containerization: reduces footprint, addressable attack surface, makes updating easier, and allows for better dependency management
* System Manager supports multiple micro OSs (SLES, Rocky Linux, Oracle Linux, etc.) and integrates well with tools like Kubernetes, Prometheus, and Grafana
* System Manager manages workloads in various environments and scales to manage slot and microservices
* Containerization allows for easier management of complex applications and makes innovation possible by aligning with DevOps strategy.


## Sponsored Session: Don’t Ask What Community Can Do for You, but... - Bart Farrell & Jorge Turrado

URL: [https://www.youtube.com/watch?v=XiY4qHZHr4Y](https://www.youtube.com/watch?v=XiY4qHZHr4Y)

 * Bart Farrell and Jorge Turrado giving talk at CDF event
* Bart is a CNCF Ambassador, maintainer of Keda project, Microsoft MVP, and content creator
* Jorge is also speaking at the event and helping MC
* Both have diverse backgrounds but share interest in CNCF ecosystem
* CNCF collaborates with foundations and cloud providers to ensure compatible software across different places
* CNCF has three stages for projects: sandbox, incubating, and graduated
* Sandbox projects are in early stages, incubating projects have growing adoption, and graduated projects are production-ready
* CNCF Foundation also supports legal issues and provides credit for open source interactions with third parties
* Noncode contributions like documentation, bug reporting, and translation are valuable to the community
* CNCF offers mentorships and scholarships for those wanting to contribute to cloud native projects
* Becoming a CNCF Ambassador involves making leading community contributions, creating content, or holding a case study
* There are many ways to get involved in CNCF such as attending local meetups, submitting talks, and contributing to projects on GitHub.


## Using AI-enabled Edge Cloud Technologies to Strengthen Europe’s... - Idoia Iglesia & Marco Hierro

URL: [https://www.youtube.com/watch?v=YE2UqnFZw3Y](https://www.youtube.com/watch?v=YE2UqnFZw3Y)

 * Marco Antonio Iglesia from iCarly multisectorial research center explains using AI-enabled edge cloud technologies in industries
* AI models integrated into products and services to increase competitiveness and add value
* H2 Cloud Continuum Technologies take advantage of edge cloud's strong points: increased privacy and reduction of latency
* Critical industries want to keep data local for security reasons, using a Federated learning approach instead of sending data to the cloud
* Open source technologies used for building blocks and customization, allowing interoperability and vendor neutrality
* One industrial use case example is Mon Dragon Assembly, an international automatization assembly solution in the automotive space
* Problem arises when training big models requires information from multiple locations without sending actual data to the cloud due to data sovereignty concerns
* H2 Cloud Continuum platform manages life cycle of AI models and allows for model deployment and updating at edge locations
* Building a European open source function service framework, called Sovereign, to empower IoT devices and allow them to choose whether to perform tasks locally or on the cloud.
* Federated learning enables multiple clients to train models locally while ensuring data quality through data signatures and trust mechanisms
* Use case examples: defect detection in images using edge cameras and time series data collecting from machines
* Monogram Corporation, a big industrial group in Spain, uses H2 Cloud Continuum platform for different use cases and plans to share data space with partners.


## Panel Discussion: Demonstrating OSPO Value - Daniel Izquierdo, Dawn Foster, Chan Voong, David Hirsch

URL: [https://www.youtube.com/watch?v=ZSTupbcshGo](https://www.youtube.com/watch?v=ZSTupbcshGo)

 * Introduction by Hannah Jimenez, program manager at City Group, welcomes attendees to the Open Source Summit EU and announces the release of a new survey report on OSPOs (Open Source Program Offices) and their role in sustaining open source projects.
* Chan Voong, program manager at Comcast OSPO, introduces the panelists: Daniel Izquierdo (co-founder of Etherea and President of Open Source Commons Foundation), Dawn Foster (Director of Data Science for the chaos project at VMware), and David Hirsch (Open Source Program Manager at Dynatrace).
* The panel discussion focuses on effective communication and metrics to demonstrate value in OSPOs, as well as challenges in identifying and measuring metrics for open source projects.
* Daniel Izquierdo talks about his experience working with Etherea and Open Source Commons Foundation, and the importance of contextualizing data to effectively communicate its meaning to stakeholders. He measures various things such as company growth, workouts, cooking, and responsiveness.
* Dawn Foster discusses her 20+ year experience in open source, and how she focuses on community engagement and collaboration when working on projects. She measures influence, impact, and adoption within the open source community.
* David Hirsch talks about his role at Dynatrace and his experience working with open source communities, emphasizing the importance of understanding different stakeholder perspectives when working on projects. He measures various things such as coffee intake, metric usage, and the impact of open source on a company's bottom line.
* The panelists discuss the importance of effective communication in OSPOs, using data to create narratives that resonate with different stakeholders, and the challenges of measuring indirect contributions and long-term sustainability. They also mention tools such as GrimoireLab, OSS Compass, Augur, Jira, GitHub, and Orbit for metrics and reporting.
* The panelists answer audience questions on topics such as measurement in data science use cases, the challenges of measuring performance and contribution, and the importance of understanding the tradeoffs between short-term deliverables and long-term sustainability in open source projects.


## Understanding the Sec in DevSecOps: Beyond Just Shifting Left - Abubakar Siddiq Ango, GitLab

URL: [https://www.youtube.com/watch?v=_PtHE7gGOUg](https://www.youtube.com/watch?v=_PtHE7gGOUg)

 * Abubakar Sadiq Ango, GitLab developer evangelism program manager, discussing understanding Sec in DevSecOps
* Shifting security left is important, but there's more to it than just that
* Security was once an afterthought in software development, but now organizations are prioritizing it earlier in the process
* Attack vectors have evolved, and securing the entire software development life cycle is crucial
* Common attack vectors include network issues, human error, and supply chain security
* Shifting security left means implementing security best practices from the planning stage to production
* Ensuring secure remote development environments and using zero trust principles are important
* Static and dynamic application security testing, container scanning, dependency scanning, license securing, and secret detection are necessary security practices in DevSecOps
* Vulnerability management is essential for addressing detected vulnerabilities and ensuring compliance with industry regulations.


## OS-Climate: A Breakthrough Open Data and Open Source Analytics Collaboration for... - Matthew Sandoe

URL: [https://www.youtube.com/watch?v=g471_KbUed8](https://www.youtube.com/watch?v=g471_KbUed8)

 * OS Climate: open source collaboration for managing climate risk and accelerating carbon transition
* Problem: Overexposure to climate risk, under-preparation for transition, need for data management and analysis
* Solution: Holistic data analytics solution to manage risk and align with Paris Agreement goals
* OS Climate ecosystem: Community of data providers, banks, asset managers, research institutions, and nonprofit organizations
* Data challenges: Need for multiple sources, accurate carbon footprint data, forward-looking predictions, and transparent models
* Analytical tools: Alignment tool for demonstrating Paris Agreement compliance, physical risk resilience stream, and transition analysis
* Partners: BNP Paribas, Goldman Sachs, Amazon Web Services, London Stock Exchange, etc.
* Collaborative projects: Sector alignment project, OS Climate Transition Scenario Tool, Integrated assessment model, etc.
* Physical climate risk: Lenders and investors face risks from extreme weather events and climate change impacts on assets
* Disaster recovery and strategic planning for climate adaptation
* Data Commons (data mesh): Red Hat's approach to data governance, availability, reliability, and scalability
* Principles: Federated governance, self-service architecture, and decentralized product ownership.


## Sylva Project, What Is It, What We Achieved, and Where ... - Guillaume Nevicato & Philippe Ensarguet

URL: [https://www.youtube.com/watch?v=gCeEym0WTZU](https://www.youtube.com/watch?v=gCeEym0WTZU)

 * The Sila project is an initiative aimed at delivering a cloud-native, industrial-grade Telco stack using the Linux Foundation and Open Source ecosystem.
* The project was started in response to the challenges of traditional siloed approaches in Telecom industries, which include high UNM (unitization, normalization, and migration) burden, security concerns, and lack of automation.
* The Sila project's objectives are to gather requirements, validate reference implementations, and create a validation center for cloud native network functions in the Telco ecosystem.
* The project began as an exploratory effort and was hosted by Orange and became the first project under the Linux Foundation Europe.
* The project aims to leverage open source initiatives instead of proprietary solutions and to accelerate Telco Cloud implementation through mutualization and simplification of operating models.
* Key benefits include cost reduction, energy efficiency, sustainability, interoperability, and improved operational models.
* The Sila ecosystem currently includes six working groups focusing on technical solutions, validation center, security, energy efficiency, communication, and governance.
* The project has already delivered key features such as host 5G core, distributed kubernetes clusters, and network automation.
* Future plans include addressing offloading, network modelization, security enhancements, and integrating with new verticals and operators.
* The Sila community is growing, with active participation from Telecom operators, Network function providers, system integrators, hardware infrastructure providers, and many other entities.


## Open Source in the Age of Cloud and Microservices - Michael Meskes, NetApp

URL: [https://www.youtube.com/watch?v=hhBsg8DDrcY](https://www.youtube.com/watch?v=hhBsg8DDrcY)

 * Michael Meskes started actively developing software in 1993 and has worked on various open source projects, including Linux and PostgreSQL
* Free software was not widely used in business during the early years, but it gained popularity as the internet grew
* Open source software became more common in businesses starting in the late 1990s and early 2000s
* Early open source software projects were often started by volunteers and academic institutions, with the goal of creating innovative software and sharing control
* Open source software became increasingly important in business as more companies used it to build their products and services
* Open source software has become a commodity and is now used in various industries, from data centers to consumer electronics
* The open source community has grown and evolved over the years, with companies using open source software as an alternative to proprietary software
* Open source software has also influenced business models, such as the open core model, where a company provides a free core version of the software but charges for additional features or support
* Open source software has become more complex and requires specialized skills to develop and maintain
* The rise of microservices and cloud computing has led to new challenges in managing and securing open source software.

Some key points from the transcript:

* Free software was called "free software" because it was free as in freedom, not necessarily free as in price.
* Apache web server is an example of a widely-used open source project.
* Open source software has been used to build mission-critical systems and replace proprietary software in various industries.
* The open source community has become more organized over the years, with processes for ensuring trust and quality in open source software.
* Companies have adopted different business models for using and contributing to open source software.
* Open source software has become a commodity and is used in many everyday technologies, such as smartphones and home appliances.
* The rise of microservices and cloud computing has led to new challenges in managing and securing open source software.


## Lightning Talk: MPIWasm: Executing WebAssembly on HPC Systems - Mohak Chadha

URL: [https://www.youtube.com/watch?v=sQwTlZQ8fPo](https://www.youtube.com/watch?v=sQwTlZQ8fPo)

 * Mohak Chadha, PhD candidate, talks about executing WebAssembly on HPC (High Performance Computing) systems
* Motivation: Containers like Docker are commonly used in modern HPC systems but have limitations, such as requiring root privilege and not supporting parallel file systems or high-performance networking libraries.
* WebAssembly: Originally created as an alternative to JavaScript in web browsers, is a universal intermediate binary format with lightweight isolation and software fault isolation.
* MPI (Message Passing Interface) is a de facto standard for programming HPC systems.
* Proposal: Use WebAssembly as a distribution format for packaging and executing MPI-based HPC applications.
* Benefits: Simplifies compilation process, allows running MPI-based modules directly in WebAssembly, provides low overhead MPI call and zero-copy memory operations.
* Implementation: Uses Wasmer embedder, Lipsy library for compiling C++ applications to WebAssembly, and a custom Python-based tool for handling text representation of WebAssembly modules.
* Results: Tested on Intel Omni-Path InfiniBand HPC systems with Intel processors and observed performance similar to native execution, with a maximum overhead of around 40%.
* Future work: Extending WebAssembly specification to support flexible Vector Lengths for modern processors like AVX-512.
* Tools: Wasmer embedder fully implemented in Rust, simplifying the compilation process and eliminating the need for installing raw PDKs.


## Lightning Talk: What Can be Learned from the Open Source Community in Israel? - Uriel Ofir, Abra rd

URL: [https://www.youtube.com/watch?v=t7dXuZ4ojik](https://www.youtube.com/watch?v=t7dXuZ4ojik)

 * Uriel Ofir from Abra rd talks about the open source community in Israel called Makaf
* He shares his personal story of how he was encouraged to contribute to open source projects as a beginner programmer
* He found it daunting to effectively contribute, but was inspired in February 2021 and started a Discord server for job seekers to learn and collaborate on open source projects
* The target audience is job seekers who have time and motivation to enhance their skill set and resume by contributing to open source
* Makaf provides a platform for beginners to learn from experienced developers, with the added benefit of real-world experience and collaboration
* The community has grown to 1,300 participants with a dozen programmers managing projects and contributing
* Job seekers receive valuable code reviews from senior developers, gaining experience and adding to their portfolio
* The community also benefits recruiters who can identify promising talent by observing activity within the community
* Uriel envisions expanding this concept globally, creating similar communities around the world
* He invites anyone interested to join the English-speaking channel within the Israeli Community and contribute to fostering collaboration and sharing knowledge.


## How Can Your OSPO Drive Open Source Business Value for Your Organization? - Masae Shida, VMware

URL: [https://www.youtube.com/watch?v=v7r6WXtdobk](https://www.youtube.com/watch?v=v7r6WXtdobk)

 * Masae Shida discussed how an Open Source Strategy Office (OSPO) can drive business value for organizations.
* Companies need a clear strategy when using open source to avoid potential risks and maximize opportunities.
* Shida shared her background in software development and experience leading open source strategies at VMware.
* She highlighted the advantages of open source, such as speed, efficiency, flexibility, and community engagement.
* A strong open source strategy involves aligning business goals with the community's contributions, creating a clear vision, and avoiding misaligned licensing models.
* Companies can adopt various open source business models, including service-based or support models, which provide different benefits depending on the product and market.
* Open sourcing a commercial offering can lead to increased user adoption, engagement, and revenue through the "product-led growth" strategy.
* The timing of open sourcing a project is important and depends on the project's goals and the community's interest.
* Companies should ensure that their open source projects meet functional requirements, are compatible with other systems, and have good documentation.
* Engaging the community and maintaining a healthy open source project is crucial for its long-term success and protecting the company's reputation.


## Let's Talk Community - How to Grow, Nurture, Engage, & Measure - Kim McMahon, Cisco

URL: [https://www.youtube.com/watch?v=v9wpFEVeFR0](https://www.youtube.com/watch?v=v9wpFEVeFR0)

 * Kim McMahon from Cisco's Innovation Incubation unit discusses open source marketing, community building, and product-led growth
* Open source software and closed source software in the context of product-led growth
* Role of community managers in open source projects: providing awareness, transparency, collaboration, and value back to the organization
* Open source projects and communities contribute to product-led growth through a virtuous cycle
* Linux and Kubernetes as examples of open source projects maturing within organizations
* Community building efforts, such as feedback loops, content creation, and education, can help drive adoption
* Adoption-led and community-led strategies for driving open source project adoption
* Aligning organizational goals with community needs to build successful open source projects

Here are some key takeaways:

* Open source software plays a significant role in product-led growth.
* Community managers have unique roles to play in open source projects, including providing awareness, transparency, collaboration, and value back to the organization.
* The virtuous cycle of open source projects involves users contributing back to the project, which helps it grow and mature.
* Linux and Kubernetes are examples of open source projects that have become integral parts of many organizations' technology stacks.
* Community building efforts, such as feedback loops, content creation, and education, can help drive adoption of open source projects.
* Adoption-led and community-led strategies can be effective for driving open source project adoption.
* Aligning organizational goals with community needs is essential for building successful open source projects.


## Open Source for Energy Access: How Open Innovations Promote Interoperability &...- Vivien Barnier

URL: [https://www.youtube.com/watch?v=xQOv7KBfSQ8](https://www.youtube.com/watch?v=xQOv7KBfSQ8)

 * Vivien Bernier from Nexus Foundation discusses the potential of open innovations in energy access at the LF Energy Open Source conference
* Electricity access is a significant challenge, especially in Africa and Asia, with over 700 million people without electricity
* The energy transition has seen some progress but also stagnation due to population growth outpacing electrification efforts
* Open source projects can provide efficient solutions for energy access, particularly in remote areas with expensive infrastructure and unreliable connectivity
* Interoperability is crucial for the energy sector, especially as it transitions to renewable energy sources
* Paygo (Pay As You Go) systems are an example of open source innovations disrupting the energy sector, allowing low-income customers to purchase electricity on a pay-as-you-go basis using tokens
* Open source projects can drive interoperability and collaboration between different stakeholders in the sector, reducing redundancy and improving efficiency.


## Lightning Talk: How Not to Make Open Source - Lessons Learned - Leszek Manicki

URL: [https://www.youtube.com/watch?v=yNfw--DfV-Q](https://www.youtube.com/watch?v=yNfw--DfV-Q)

 * Speaker is from Wikimedia Foundation, focusing on community content creation part of open source software development in Wikimedia projects, specifically Wikibase and Wikidata
* Open source software is important for creating a public platform for knowledge sharing and enabling social and economical change
* The Wikimedia Germany chapter focuses on software development with a project called wikibase
* The speaker reflects on the importance of open source licenses and the role of communities in building upon each other's work
* There are challenges in the Wikimedia community, including a lack of contributor diversity and overly complicated software architecture
* The speaker suggests making software projects more explicit with clear long-term purpose and easier for others to understand, as well as encouraging upstream contributions
* Open source compensation for contributors is an important topic but can be a barrier to entry due to the lengthy contribution process
* The speaker encourages building self-organized groups to help build software and improve the open source community.


## ADHD: The Power of Diagnosis - Amanda Brock, OpenUK & Bart Farrell, Independent

URL: [https://www.youtube.com/watch?v=zUkrJoyz7sA](https://www.youtube.com/watch?v=zUkrJoyz7sA)

 * Bart Farrell and Amanda Brock discuss their experiences with ADHD diagnosis
* Bart, a freelance content creator and mental health professional, was diagnosed at age 37 after struggling with focus, mood swings, and rejection sensitivity
* Amanda, who also has autism spectrum disorder, discusses her experience getting assessed for ADHD in the UK and facing stigma around the condition
* Both speakers emphasize the importance of education and community resources for those with ADHD
* Bart shares how the pandemic has made his ADHD symptoms more noticeable due to increased stress and isolation
* Amanda mentions that diagnosis processes can vary greatly depending on the country and individual experiences
* They discuss the challenges of getting access to medication in the US and UK, as well as the benefits of cognitive-behavioral therapy and establishing routines.


## Smarter Than Your Average SBOM! - Matt Jarvis, Snyk & Andrew Martin, ControlPlane

URL: [https://www.youtube.com/watch?v=5k4-M69VRzQ](https://www.youtube.com/watch?v=5k4-M69VRzQ)

 * Matt Jarvis from Snyk and Andy Martin from ControlPlane discussing Software Bill of Materials (SBOMs)
* SBOMs: structured data that provides relationship information between elements in software, making it easier to manage dependencies and improve supply chain security
* Importance of trust in the software development process and the role of SBOMs in establishing trust between parties
* Different formats for SBOMs include JSON and XML
* SBOMs are not valuable on their own but serve as an important step in improving supply chain security by providing a standardized, machine-readable way to share information
* SBOMs can be created at various stages in the software development process, including build time and deployment, and can be updated to reflect new vulnerability data
* The quality of SBOMs can vary greatly depending on the organization and the tools used to create them, with some organizations using scoring systems to evaluate SBOM quality
* SBOM enrichment allows for the addition of additional relevant data such as license information and security vulnerabilities from external sources
* The responsibility for ensuring trustworthy software supply chains lies with both producers and consumers, with the need for secure build infrastructure, verification, and signing keys.


## Evolution and Scaling of Feature Store at Uber - Divya Nagar, Uber Technologies

URL: [https://www.youtube.com/watch?v=5sueFigi3vA](https://www.youtube.com/watch?v=5sueFigi3vA)

 * Divya Nagar from Uber's feature engineering team discusses the evolution and scaling of Uber's Feature Store
* Feature Store manages features for machine learning models, including offline serving, online serving, and transformations
* Offline serving involves serving data for training models, while online serving serves predictions in real time
* Data is aggregated from event streams into batch features (e.g., orders received per day) or real-time features (e.g., activity within the last minute)
* Feature Store manages scaling challenges such as onboarding new features, ensuring offline-online consistency, and optimizing serving infrastructure
* Feature onboarding is automated with JSON configs, allowing for self-service feature creation and reduction in intervention from team
* Offline serving optimization includes batching data to reduce overhead and improve join performance
* Online serving optimization involves caching features locally to reduce query latency and cost
* Uber's architecture includes realtime data ingestion into Kafka, aggregation jobs, and data storage in Cassandra and Hive
* The Feature Store infrastructure manages ten thousand features and serves hundreds of millions of QPS with a P99 SLA of 10 milliseconds.


## Confidential Containers: Why, How, and Where Are We? - Magnus Kulke, Microsoft

URL: [https://www.youtube.com/watch?v=6fbzHTJk6BE](https://www.youtube.com/watch?v=6fbzHTJk6BE)

 * Magnus Kulke, Microsoft software engineer, discusses confidential computing in the context of containers
* Confidential computing is CPU-aided encryption technology that enables running applications with sensitive data in a trusted execution environment
* Motivated by use cases such as enhancing data privacy and compliance with regulations like GDPR
* Key elements of confidential computing: encryption, measurement, and remote attestation
* Encryption involves encrypting data both at rest and in transit
* Measurement ensures data integrity and involves taking a hash of code and comparing it to a known value
* Remote attestation allows verifying the integrity of a system and ensuring that it is running trusted software
* Challenges of confidential computing include securing data use, measuring remote stations, and establishing trust between parties
* Confidential containers are an interesting technology for democratizing the use of confidential computing in projects
* Qatar container is a specific implementation of confidential computing based on virtual machine technology
* Key features of Qatar container include a shim runtime, a transparent deployment model, and efficient resource utilization
* Challenges of implementing confidential containers include the cost and complexity of deploying and managing them, as well as integration with existing systems like Kubernetes.


## Understanding the Legal Context of AI - Van Lindberg, OSPOCO

URL: [https://www.youtube.com/watch?v=7ILoi62RImc](https://www.youtube.com/watch?v=7ILoi62RImc)

 * Van Lindberg: 25-year computer law expert, involved in AI since 2008, open source, and generative ML
* Focusing on a 10,000-foot view of AI legal context for a mostly technologist and lawyer audience
* Discussing intellectual property (IP) application in machine learning (ML), particularly copyright
* Using an art inspector analogy to explain model training
* ML models involve measuring input data to make predictions based on statistical probabilities
* Logical architecture is the structure of the code, model implementation, and weight data
* Backpropagation updates analysis to improve predictions
* Copyright law: US vs Europe; Google Books case allows fair use for search engines
* Creating a derivative work means copying specific expression from another work
* In the Getty Images vs Stability AI case, copyright infringement claim was dismissed because no registration or filtering
* Anderson v Stable Diffusion: stable diffusion generating copyright-infringing images dismissed due to lack of registration and aesthetic filtering
* Sarah Silverman's work vs Stability AI: copyright infringement argued by using copied material instead of creating a summary
* Getty Images case: copyright infringement claim against AI-generated images, may win on trademark argument
* US Copyright Office recognizing AI-generated works as copyrightable since last year (Zarya v Dawn and Chris Castanova cases)
* Microsoft's indemnity clause for GitHub Copilot unlikely to apply because code provided is not exact copilot output.


## Mix Kubernetes with Linux Kernel Tracing to Boost the Observability of Your... - Tzvetomir Stoyanov

URL: [https://www.youtube.com/watch?v=C30M-DXy9d8](https://www.youtube.com/watch?v=C30M-DXy9d8)

Error


## It's All About Trust: Why Confidential Computing Matters - Mike Bursell

URL: [https://www.youtube.com/watch?v=Gn0ezYi-6oM](https://www.youtube.com/watch?v=Gn0ezYi-6oM)

 * Mike Wessell, executive director of Linux Foundation's Confidential Computing Consortium, discussing trust and confidential computing in the context of secure supply chain
* Trust is a fundamental concept that is often taken for granted, especially when it comes to technology systems
* Three types of trust:
	+ Contextual trust: trust in a computer system depends on its context (e.g., IO context, authentication context)
	+ Time-dependent trust: trust may decay or grow based on expectations and entities involved
	+ Symmetrical trust: trust relationship between two systems may not be mutual (e.g., a doctor performing CPR doesn't necessarily trust the patient back)
* The question of "I Trust You" is a big one in the context of confidential computing
* Confidential Computing refers to protecting data and code during execution, ensuring data integrity and confidentiality
* A trusted execution environment (TEE) is a CPU-created set of memory pages that encrypts workload and protects it from the host OS and hypervisor
* Attestation is a cryptographic process that allows making decisions based on trust
* Protecting keys during operations like signing is crucial to maintain security
* Complexity arises when considering chaining trust relationships, transitive trust, and distributive trust
* The open-source community relies on best efforts for security, but it's essential to understand the limitations and challenges
* Confidential Computing plays a role in securing supply chain management by protecting data and code at runtime
* The hardware level is crucial for confidential computing, as the TCB (Trusted Computing Base) includes both software and hardware components
* Trust Hardware is an important aspect of confidential computing, ensuring the correctness and security of hardware components
* It's essential to keep separate trusted execution environments, each controlled by a different entity or group of entities
* Monitoring and debugging are crucial for maintaining trust in a system, especially when dealing with complex systems like HSMs (Hardware Security Modules)
* The tooling industry plays a vital role in solving the problem of confidential computing but also introduces challenges related to visibility and expertise.


## Large Block I/O for Linux - Hannes Reinecke, SUSE Labs

URL: [https://www.youtube.com/watch?v=HfRhDLbxstk](https://www.youtube.com/watch?v=HfRhDLbxstk)

 * Hannes Reinecke, SUSE Labs: 20-year Linux veteran, involved in storage research
* Discussed the idea of using larger page sizes (block I/O) in Linux for improved efficiency and cost savings
* Current Linux page size is typically 4kB due to CPU architecture and driver subsystem limitations
* Large databases could benefit from larger page sizes as they are organized internally and hardware could move larger pages efficiently
* Larger blocks would reduce overhead, but increase latency and require more memory for page cache
* Folio structure proposed by Matthew Wilcox allows for transferring larger blocks without converting page cache folios
* Buffer hat is a data structure used to manage I/O operations and could be replaced with the folio structure
* The use of large pages has been discussed since the early days of Linux, but the mainframe concept of variable block size drives inspired the idea
* Hardware-assisted memory management allows for determining whether given memory areas are dirty (need to be read from disk)
* Folios are a common structure used in page management and could be used to identify large blocks
* The buffer hat structure, which has been used since the early days of Linux, could be replaced with folios to transfer larger blocks efficiently
* Modern interfaces like IO map already support folios, eliminating the need for intermediate structures
* Converting the file system to use folios instead of buffer hats would require proper documentation and careful consideration of memory management implications.


## Keynote: Welcome Back Day 2 - Gabriele Columbro, Executive Director, FINOS

URL: [https://www.youtube.com/watch?v=IvGomhFumzQ](https://www.youtube.com/watch?v=IvGomhFumzQ)

 * Good morning, glad everyone had a fun first day at the conference
* Housekeeping note: Diversity lunch for marginalized communities at 1 pm, expert session with community leaders, book signing by Lauren Mafel
* Today's agenda will touch on Europe's role in open source and value of open governance
* Open source software standards, maintaining open source licenses, and the USI open source definition will be discussed
* Discussion on open source sustainability, impact on areas like climate change and agriculture
* Keynote speaker Jim Zemlin, Executive Director of Linux Foundation, to be introduced later today.


## Sponsored Session: MLOps: Why DevOps Solutions Fall Short in the Machine Learning... - Eduardo Bonet

URL: [https://www.youtube.com/watch?v=KUOtgqXJXCI](https://www.youtube.com/watch?v=KUOtgqXJXCI)

 * Eduardo Bonet, Brazilian, six years at GitLab, explaining why DevOps solutions fall short in the Machine Learning world
* Two main issues: lack of understanding between people involved and fundamental differences between developing software and machine learning
* Example 1: Uzi Hadoop Orchestra pipeline orchestrator failed to meet data scientist needs
* Example 2: Resistance from data scientists to use tooling that brings software engineering practices into their workflow
* MLOps: similar goal as DevOps but different technology, culture, and process for creating software with a Machine Learning feature
* Data Scientists have different backgrounds and incentives than Software Engineers
* Data Scientists' workflow is different: they need production data for model development and testing
* Resistance to tooling, still using Jupyter Notebooks, and reluctance to install new tools or learn new languages
* Need for explicit logic and code review in machine learning development
* Extracting patterns from data is expensive and time-consuming in machine learning development
* Different testing approaches, need for synthetic data, and versioning of models
* Vision for GitLab MLOps: single application with a cohesive user interface, unified data store, and improved collaboration between data scientists and software engineers.


## Opening the JAR: The Hitchhiker's Guide to JAR File Dependencies - Daniel Haim Breger

URL: [https://www.youtube.com/watch?v=OKDxjgc-OVQ](https://www.youtube.com/watch?v=OKDxjgc-OVQ)

 * Daniel Breger, security researcher at Palo Alto Networks, talks about Java file dependencies
* Motivation: analyzing Java dependencies is important for understanding class loading and managing third-party libraries
* Java Virtual Machine (JVM) runs Java code by first compiling it into bytecode and then running it within the JVM
* Third-party dependency management tools like Maven and osgi help manage Java projects and their dependencies
* Maven uses a pom.xml file to define dependencies with Group ID, Artifact ID, and Version numbers
* Transitive dependencies can cause issues when multiple versions of the same dependency conflict
* osgi framework is another modular Java program that solves the problem of monolithic programs and their dependencies
* osgi uses a Manifest file to include dependencies and define the main class and class path
* Class loading in Java 9 introduces new concepts like module system and module path for better security and reducing Java platform size.
* Understanding dependency management is crucial for secure software development, especially in large projects or organizations.


## NanoVisor: Modernizing Container Runtime with an Architecture Refactor..- Jianfeng Tan & Tianyu Zhou

URL: [https://www.youtube.com/watch?v=Pmmk4RHYZRA](https://www.youtube.com/watch?v=Pmmk4RHYZRA)

 * Jianfeng Tan and Tianyu Zhou presented on NanoVisor, a project for modernizing container runtime architecture
* Goal is to optimize performance and improve security in container runtimes
* Comparison of low-level container runtimes like containerd and high-level container runtimes
* Discussion on misconceptions about container isolation and alternatives like Kata, Firecracker, and sandboxing
* Introduction to NanoVisor architecture: interception, limit, and security components
* Interception component intercepts Cisco application processes in guest kernel
* Limit component enforces resource limits using the host kernel
* Security component restricts access using the host kernel and provides isolation without requiring a separate hypervisor
* Discussion of advantages and disadvantages of NanoVisor compared to other container runtimes, like Docker and Kubernetes
* Comparison of performance and security between NanoVisor and traditional container runtimes in various scenarios
* Conclusion: NanoVisor offers better performance and stronger isolation while using less resources than traditional container runtimes.


## Poisoned Pickles Make You Ill - Adrian Gonzalez-Martin, Seldon Technologies Ltd

URL: [https://www.youtube.com/watch?v=T_aBXcR-75A](https://www.youtube.com/watch?v=T_aBXcR-75A)

 * Adrian Gonzalez-Martin from Selden Technologies Ltd spoke about securing machine learning workloads using the example of pickle, Python's native serialization format.
* Pickle is widely used in machine learning, including popular frameworks like Jupyter Notebook and Keras.
* Poisoning pickle files can be a security risk as they can execute arbitrary code upon deserialization.
* MLSACUPS, an intersection of standard devops and machine learning security policies (DevSecOps), is important in securing AI systems.
* Top 10 vulnerabilities in machine learning systems include supply chain risks, and pickle files are vulnerable to incompatibility issues between Python versions.
* To mitigate the risk of pickle poisoning, alternatives like Onyx, a modeling descriptive format, can be used instead of pickling code directly.
* Other security measures include using secure package managers, signing artifacts, and implementing multi-factor authentication for access to model serving environments.
* The talk covered a demo of easy poisoning of a pickle file, the importance of supply chain security, and the use of tools like Scopes and Onyx to mitigate risks.


## The Kernel Report - Jonathan Corbet, LWN.net

URL: [https://www.youtube.com/watch?v=VaA8LGPT3U8](https://www.youtube.com/watch?v=VaA8LGPT3U8)

 * Jonathan Corbet of LWN.net discussed the current state of the Linux kernel community in a recent talk
* Six major kernel releases have been made since October 2020, with over 13,500 individual commits
* Over 2100 developers contributed to the latest development cycle, with a record number of first-time developers
* Stable kernel updates are expected around the end of October, with around 15,000 changes already merged
* Major changes include improvements to the CPU scheduler and security fixes for Android kernels
* The community is seeing increasing pressure to merge code written in Rust, but there are concerns about maintenance burden and compatibility with existing C code
* There have been complaints from maintainers about burnout and understaffing, as well as a lack of employer support
* Documentation and build system improvements are needed to make the kernel development process more efficient and accessible.


## Improving Container Image Registry Availability with Kube Image Keeper - Jérôme Petazzoni

URL: [https://www.youtube.com/watch?v=W1wcIdn0DHY](https://www.youtube.com/watch?v=W1wcIdn0DHY)

 * Jérôme Petazzoni is talking about improving container image registry availability using Cube Image Keeper
* Registries, such as Docker Hub and Quay, can have issues causing delays or even deletion of images
* These issues include network problems, pull quotas, and the need to remove old images that are no longer in use
* Alternatives for improving registry availability include using a mirror registry and setting up a local cache
* Cube Image Keeper is a solution for automatically managing image caching and removing old images
* It uses a DaemonSet to run on every node in the cluster, creating a proxy that rewrites image references to use the local cache instead of pulling from the registry
* The controller runs in the background and checks for new images, creating an entry in etcd when one is detected
* Cached images are kept for 30 days and can be forced to be refreshed by adding a specific annotation to the image
* High availability can be enabled by using MinIO as a backend object store and enabling cache replication
* The presentation includes live demonstrations of deploying and scaling a Kubernetes cluster, creating a demo image, and using Cube Image Keeper to cache it locally.


## Adventures in Securing an Open Source Project: From Repo Security Zero... - Kara Olive & Pedro Nacht

URL: [https://www.youtube.com/watch?v=bmpRont2r5A](https://www.youtube.com/watch?v=bmpRont2r5A)

 * Cara Olive and Pedro Nacht from Google Open Source Security Team discuss supply chain security in open source projects.
* Supply chain attack involves injecting code into a project to harm its dependents.
* Simple compromises can lead to major risks, as seen in the Log4j vulnerability and Target data breach.
* Project maturity and popularity increase the risk of being targeted.
* Dependencies can pose a significant risk, with hundreds or even thousands added to a project.
* Keeping dependencies updated is crucial for maintaining security.
* Automated testing, branch protection, and code review are essential for reducing risks.
* Tools like Scorecard and dependency management bots can help evaluate and manage risks.
* Adopting automated release workflows and setting up token permissions can improve security.
* Regularly checking project dependencies and using strong security policies can prevent attacks.
* Keeping the codebase clean and avoiding runtime dependencies are also important for securing open source projects.


## FedLess: Secure and Scalable Serverless Federated Learning - Mohak Chadha

URL: [https://www.youtube.com/watch?v=fQ8sul-yHTA](https://www.youtube.com/watch?v=fQ8sul-yHTA)

 * Mohak Chadha is a PhD candidate discussing FedLess, a secure and scalable serverless Federated Learning system.
* Traditional IT infrastructure evolution: physical servers, virtual machines (VMS), containerization, AWS Lambda introduction in 2014 as functional service platform.
* Serverless Computing platforms like AWS Lambda, Google Cloud Function, Azure Function, IBM Cloud Function, and open-source alternatives offer event-driven, ephemeral stateless containers for function instances and automatic scaling.
* Cold start process: when a new function instance is created, it goes through bootstrapping and runtime execution to handle an event and return a response.
* Federated Learning (FL) involves collaborative learning between devices without sharing data, contrasting traditional cloud-centric deep learning approaches that require centralized processing of training data.
* Two types of FL: cross-device participating clients (mostly mobile Edge devices with limited compute capability) and cross-Silo organized clients (institutions with sufficient compute capability).
* Challenges in Federated Learning include scalability, handling heterogeneous hardware, and resource provisioning, leading to the need for a serverless Federated Learning system.
* FedLess is a research project that aims to address these challenges by offering security, flexibility, and ease of use with modular design and support for multiple FL training strategies like FedAvg, FedProx, and Scaffold.
* System architecture components include client (serverless function), controller (managing monitoring and strategy management), parameter server, accuracy trade-off model, and security features.
* The project uses a Corpus system entirely written in Python 3 with TensorFlow and Keras for performance optimization.
* FedLess addresses the straggler problem by implementing a Federal Scan strategy called Fella (Federated semi-asynchronous clustering based strategy) to adapt client behavior dynamically.
* The experimental results show that FedLess outperforms traditional Federated Learning systems in terms of training time, cost, and convergence speed.


## Data Access Monitoring Operator (DAMO): User-Space Tool/Python Library for Access... - SeongJae Park

URL: [https://www.youtube.com/watch?v=i7_W8-MozxY](https://www.youtube.com/watch?v=i7_W8-MozxY)

 * The speaker introduces a Python program called "Data Access Monitoring Operator (DAMO)" for profiling access patterns and optimizing memory system operation.
* DAMO supports various memory devices such as cache, drum, flash disk, hard disk, tape, etc., with different characteristics like capacity, latency, bandwidth, power efficiency, and price.
* The speaker mentions the importance of efficient memory management and keeping critical data items closer to the first memory device for faster access.
* Previous works mentioned include the access transplant page color split problem and practical climate memory adaptive approach.
* DAMO is a Python library that uses offline profiling, record-based monitoring, and profiling convenience, with features like controlling data access, snapshot monitoring, research, debugging, and optimization.
* The demo shows how to use the tool to monitor data access patterns and optimize memory usage in real-time, using various commands and options.
* DAMO can be used for various industries, including cloud computing, machine learning, and big data, which continuously become more data-intensive with lower costs and higher efficiency trends.
* The speaker shows examples of memory access patterns, hierarchical memory systems, and excess memory management optimization techniques using DAMO.
* DAMO can also be used for automating memory management tasks like reclamation and reducing memory overhead in large serverless products.


## Ketchup, Mustard, and Relish... - Laura Seay, Arnaud Hors, Jay White, Michael Lieberman, Joshua Lock

URL: [https://www.youtube.com/watch?v=jGSVMBQHIJg](https://www.youtube.com/watch?v=jGSVMBQHIJg)

 * Arnold Doore from IBM discusses the Open Source Software Supply Chain Integrity Working Group at OpenSSF
* Discussed the importance of addressing supply chain security issues in open source software, with recent attacks highlighting the need for a solution
* Salsa and Fresca are two projects within OpenSSF aimed at improving supply chain integrity
* Salsa focuses on securing software build and delivery pipelines, while Fresca is an implementation of Salsa using various open source tools
* S2C2F (Secure Software Consumption Framework) is another project that provides a maturity model for securely consuming open source software
* Guac is a tool that helps understand artifact composition and identities in the software supply chain
* OpenSSF has grown significantly in the past year, with more organizations investing in its efforts to improve open source security.
* Compliance is becoming increasingly important in the open source world, and OpenSSF projects align with various industry frameworks and standards.
* There have been debates within OpenSSF regarding the focus and scope of different projects, but progress is being made towards implementing solutions for secure software supply chains.
* Salsa version 1.0 was released in April 2021, and it focuses on build requirements and producer-oriented approaches to managing dependencies.
* The SEI (Software Engineering Institute) working group is taking best practices from the community and enshrining them as standards.
* OpenSSF is addressing the challenge of creating clear and easily implementable solutions for small projects with limited resources.
* S2C2F has added new controls to address emerging threats, and there have been efforts to operationalize OSCoW (Open Software Supply Chain Observability) format for machine-readable reporting and assurance.
* Guac is currently in beta and aims to help answer questions about software supply chain artifacts and dependencies.
* OpenSSF invites everyone to join the community and learn more about these projects at the upcoming tech talk on October 5th, 2022.


## Reliable Userspace Spinlock - André Almeida, Igalia

URL: [https://www.youtube.com/watch?v=nve9rPDzb7k](https://www.youtube.com/watch?v=nve9rPDzb7k)

 * Spin lock is a locking mechanism used in user space to ensure only one thread accesses a critical section at a time.
* Spin locks are preferred over other locking mechanisms like mutexes and semaphores for short critical sections as they avoid the overhead of context switching and kernel interaction.
* Spin locks work by having threads spin (repeat a loop) instead of sleeping and waiting for the lock to be released.
* The main problem with spin locks is that if the critical section is long, threads will waste CPU cycles spinning instead of doing useful work.
* To address this issue, there are different ways to implement spin locks efficiently such as using CAS (Compare-and-Swap) instructions and restartable sequences.
* Restartable sequences allow a thread to atomically measure if the critical section is available before entering it, reducing unnecessary spinning.
* Spin locks can be implemented in user space without needing kernel assistance by using atomic operations and managing lock state.
* The Linux kernel provides a user-space API called RTLM_SLEEPOK that implements efficient per-CPU operation without lock, which is an alternative to spin locks for long critical sections.
* Spin locks are useful when dealing with short critical sections where thread contention is high and context switching overhead is significant.
* There have been improvements in reading CPU ID using RTLM_SAC instead of the traditional getcpu() function, resulting in better performance in some benchmarks.


## Lightning Talk: How Jenga & Tetris Can Help Run More Containers with Lesser Costs...- Yash Bhatnager

URL: [https://www.youtube.com/watch?v=6HatF5F4n5A](https://www.youtube.com/watch?v=6HatF5F4n5A)

 * The speaker discusses how container scheduling in a cluster can be optimized using logic derived from classic games Jenga and Tetris.
* Container scheduler is responsible for finding the optimal node to run a container based on resource availability and other predefined parameters.
* The scheduler uses a two-step process: first, it figures out which nodes fit the existing containers' resource requirements; then, it scores each node based on several parameters and chooses the one with the highest score.
* Jenga analogy: A row in Tetris represents a node cluster's available capacity and utilized capacity, with incoming blocks being containers needing to be scheduled. The goal is to minimize gaps and pack nodes densely. However, resource decrease can lead to optimization difficulties, similar to playing Tetris when the game becomes increasingly challenging.
* High-level resource allocation in a cluster considers various resources like CPU and memory. Factors such as lesser scheduling optimization and less effort are considered for densely packing the system.
* In a real-world example with three nodes and six containers, a scheduler might fail to place container C4 because it requires more resources than what is currently available in the cluster. Autoscaling might add another node, but this adds cost without optimizing placement logically. The scheduler could generate a recommendation to move or reschedule containers.
* Clusters like Kubernetes can use underlying APIs and constructs like node pod affinity and multiple migration strategies to solve this problem recursively by swapping larger containers with smaller ones or removing multiple smaller containers to fit a bigger one.
* Swapping imbalanced nodes causing application performance degradation is crucial, as it keeps the balance between nodes and applications, allowing them to handle sudden extreme bursts of load traffic without degradation.
* Jenga analogy: A node represents a block in Jenga, with containers being the turn of the game. Removing blocks that contribute least to overall balance is crucial for entire Jenga building stability.
* Swapping containers causing imbalance can be identified using mathematical constructs like entropy. Swapping regularly or periodically based on entropy value can help optimize resource usage in a cluster.
* In a real-world example, swapping CPU and memory-intensive applications between nodes C1 and C3 can improve overall system performance and reduce costs significantly by reducing auto scaling.
* Implementation details of the optimization techniques discussed can be found on GitHub.


## Lightweight and Fast WiFi Access in Virtual Machines - Jim Huang & En-Wei Wu

URL: [https://www.youtube.com/watch?v=CIXriWKqMV0](https://www.youtube.com/watch?v=CIXriWKqMV0)

 * The speakers are from National Chang Kong University in Taiwan and will be discussing a lightweight WiFi access solution for virtual machines (VMs) through a project called BFI.
* They introduce themselves and explain the need for lightweight WiFi access in situations like continuous integration and easy deployment of virtualized environments.
* The traditional wireless interface usually requires a complex software stack, but Virtual WiFi (VFI) offers a lighter solution with a smaller software stack.
* VFI doesn't implement a21 protocol or offer full L2 protocol support but provides a Wireless interface device backend for the VM.
* When running in a horse (VM) environment, VFI provides a wireless version of the driver and works like a CFG l211 driver with some differences.
* The data path for VFI is simpler compared to traditional WiFi interfaces, as it doesn't need to encapsulate ethernet frames into L2 11 frames and can transmit ethernet frames directly.
* In the management path, VFI uses a lightweight management path feature and delegates management to the CFG l21 driver for less resource usage.
* The data path and management path work differently depending on whether VFI is running in a VM or a host (HSE) environment.
* They also discuss how VFI maintains a table of Mac addresses within BSS and checks them when receiving frames to determine whether to drop them.
* Future work for BFI includes supporting multi-queue RX IO, reducing lock contention, increasing throughput by allocating dedicated pages for reception, and saving time by not needing to allocate memory for receive frames.


## OpenTofu Project Overview - Kuba Martin & Roni Frantchi

URL: [https://www.youtube.com/watch?v=_-9LhcPgoaY](https://www.youtube.com/watch?v=_-9LhcPgoaY)

 * OpenTofu is a new project announced by the Linux Foundation to declaratively manage infrastructure using Terraform, with a focus on keeping it fully open source.
* The project was started in response to HashiCorp's decision to change the license of some of its Terraform modules from open source to the Business Source License (BSL).
* OpenTofu aims to provide a drop-in replacement for HashiCorp's Terraform registry, allowing users to continue using their existing provider modules while also benefiting from an open source ecosystem and community governance.
* The project has gained significant attention and support since the announcement, with thousands of GitHub stars, positive media coverage, and individual and corporate pledges to contribute.
* OpenTofu will offer a custom solution for the official registry that is fully compatible with existing Terraform providers and workflows. It will also allow unit testing of module code and support OCI registries.
* The project's development process will be transparent, with regular pull requests and community review and decision-making through an impartial steering committee.
* OpenTofu will also support state encryption and optional end-to-end encryption for sensitive data.
* The team is currently focusing on stabilizing the alpha version of OpenTofu, which is expected to include a polished version with new testing features, an experimental provider module registration approach, and a stable release coming later in the quarter.


## Lightning Talk: Checking Your Project for Non-inclusive Language - Nico Rikken, Alliander

URL: [https://www.youtube.com/watch?v=ce66oDyXQ2g](https://www.youtube.com/watch?v=ce66oDyXQ2g)

 * Nico Rikken presented on checking projects for non-inclusive language
* He was motivated by observing hostile structures towards certain people and the importance of inclusive language in projects
* Linux Foundation has an inclusive naming initiative and a Slack channel where word choices can be evaluated
* Git changed the name of their main branch from "Master" to "main" as an example
* As a native Dutch speaker, he found it important to check for non-inclusive language in his projects
* He suggests checking for words that might be considered non-inclusive and recommends alternatives
* He prioritizes urgent replacements and automating the process
* He wanted a tool to help discover and suggest alternatives for non-inclusive language
* He found a dedicated tool called "Woke" which checks grammar, spelling, and non-inclusive language
* He developed Caitlyn Aling to help check projects for non-inclusive language using a whitelist of words to check against
* Woke also provides explanations and suggestions for alternatives, as well as case sensitivity warnings
* He suggests setting aside time to check projects for non-inclusive language and checking alternative tools like "Veil"
* He emphasizes the importance of inclusive language and learning from resources like the University of Washington's extensive guide.


## Credential Format Comparison SIG - Torsten Lodderstedt - Technical Advisor, OpenWallet Foundation

URL: [https://www.youtube.com/watch?v=y2CQcutAq3s](https://www.youtube.com/watch?v=y2CQcutAq3s)

 * The Credential Profile Comparison special interest group (CPC SIG) of the OpenWallet Foundation aims to compare different credential profile formats.
* During a session at an unconference, there was a discussion about which is the best credential format with around 20-30 people present.
* Various credential formats were proposed, including World Wide Web Consortium (W3C) Credentials, Anoncreds, JOT, Mossip, and Json LD.
* The OWF believes that a technology-agnostic solution is the best fit for different use cases and requirements.
* The CPC SIG helps implementers figure out the best solution based on the problem at hand.
* Different credential profile formats were compared, including ISO 18135, Anocrats, MDOC, and ID Union.
* Factors considered included privacy serving, hardware-backed security, signature algorithms, revocation mechanisms, key management, and unlinkability.
* Some examples of existing profiles included ISO 18135, Anocrats, MDOC, and ecdsa assigning algorithm with revocation mechanism per day.
* Different technologies used for security were also considered, such as hardware-backed security, public key infrastructure (PKI), and COSE key management.
* The CPC SIG is looking for community contributions to keep the information up-to-date and provide tools for implementers to make informed decisions.
* There is a need for transparency and innovation in the credential format space.


## Building On-Ramps for Non-Code Contributors in Open Source - Natali Vlatko & Celeste Horgan

URL: [https://www.youtube.com/watch?v=1s6imxKnWL4](https://www.youtube.com/watch?v=1s6imxKnWL4)

 * Speakers: Celeste Horgan and Natali Vlatko
* Both are open source contributors in the tech industry, with experience in Kubernetes and Apache projects
* They discuss the importance of onboarding non-technical contributors to open source projects
* Prerequisite for involving non-technical contributors is making them feel welcome
* Communication is crucial: synchronous communication helps non-technical contributors contribute effectively
* Onboarding processes should be clear and easy to follow, with a buddy or mentor available to help
* Inner source (bringing open source practices to internal projects) can help attract and retain non-technical contributors
* Non-technical contributors can shine in project management roles, especially as projects scale
* Effective onboarding processes can reduce burnout and increase diversity in open source projects.

Some benefits of involving non-technical contributors in open source projects:

* Reduces toil for maintainers by handling tasks like documentation, triaging issues, and organizing meetings
* Brings stability through creating a diverse team and sharing the workload
* Helps attract and retain contributors who may not have the time or technical expertise to contribute code
* Can lead to innovative ideas and better feature development due to different perspectives.


## Servo Web Rendering Engine Reboot - Manuel Rego, Igalia

URL: [https://www.youtube.com/watch?v=9lkIX5ryZZ4](https://www.youtube.com/watch?v=9lkIX5ryZZ4)

 * Manuel Rego, Igalia web platform team member and Servo project lead, gave an update on Servo web rendering engine
* Servo is a rendering engine written in Rust, with features like memory safety, concurrency, WebGL support, and cross-platform compatibility
* It is used in production by Firefox for parsing and serving CSS and HTML, and its painting and compositing phases are shared with Blink
* The project has a long definition of web rendering as the process from taking HTML and CSS to displaying it on a screen
* Servo's main features include parsing, style resolution, layout, painting, and compositing
* It is currently in active development with a team of around 140 people worldwide
* The project was founded in 2001 and has been maintained by Mozilla since 2014
* Servo's goal is to create a faster, more energy-efficient web rendering engine that can run on various devices, including mobile and embedded applications
* Current work includes improving the rendering engine for use in Tower, an application framework, and experimenting with WebGL support on Android
* The project is also focused on security and has features like memory safety, borrow checker, and ownership system to eliminate vulnerabilities related to memory management.


## FORK IT ALL if You Fork It - Daniel Doubrovkine, AWS

URL: [https://www.youtube.com/watch?v=B8NlDg_Mevw](https://www.youtube.com/watch?v=B8NlDg_Mevw)

 * Daniel Doubrovkine from AWS talked about engaging with the open source community and the challenges of forking open source projects
* Elasticsearch is an example of a large open source project forked by AWS to create OpenSearch
* Forking allows AWS to accept contributions, maintain control, and provide a stable and healthy project for customers
* Log4j vulnerability highlighted the importance of timely security patches in open source projects
* Governance is essential in managing open source projects and ensuring long-term development
* AWS followed a transparent process when forking OpenSearch, including setting up a GitHub organization and creating a common contributing document
* Automation, such as CI/CD pipelines, can help ensure the quality and security of an open source project
* Engaging with the open source community is essential for the success of a project, with Amazon actively participating in OpenSearch governance and contributions.


## Asymmetries in Open Source: What Can Research Tell Us about Closing the... - Adrienn Lawson

URL: [https://www.youtube.com/watch?v=DwQB6pwMgVw](https://www.youtube.com/watch?v=DwQB6pwMgVw)

 * Adrienn Lawson, data analyst at Linux Foundation research team, discusses findings from a survey on open source usage and contribution patterns in organizations.
* The survey covered many regions worldwide, with a focus on Europe, and aimed to examine the current level of open source usage and contribution within organizations, as well as identifying motivators and inhibitors for contributing.
* Key findings:
  + Open source is widely used, with around 90% of respondents reporting significant or widespread use within their organizations.
  + Open source development teams are encouraged to contribute in many cases.
  + Permissive open source policies are more common than restrictive ones.
  + European organizations have a higher percentage of widespread use and encouragement compared to other regions.
  + There is a gap between open source usage and contribution, with only around half of respondents reporting contributing code or assets to open source projects.
* The survey also explored the opportunity open source landscape presents for organizations, recognizing growing reliance on open source and its perceived value as an investigator benefit and challenge.
* The survey was distributed globally, with a regional distribution of 33% Americas, 34% Europe, 27% Asia Pacific, and 7% other regions.
* The methodology included a distributed survey from April to June 2023, and the European sample consisted of 307 usable responses out of a total of 900.
* The consumption contribution gap was measured by comparing open source usage policy on the horizontal axis with contribution policy on the vertical axis, with fully symmetrical organizations appearing in the top right corner.
* Respondents reported that open source is used for a variety of purposes within their organizations and that they evaluate components better before use.
* There was also discussion about the importance of security concerns and development training for secure software contributions.
* The survey found that 48% of organizations have contributed code to open source projects, with Europe leading the way at 54%.
* The difference in approach between organizations with clear open source strategies and those without was highlighted, with varying steps taken in code review, quality assurance testing, security testing, and legal approval.
* The survey also explored whether respondents agree that certain actions would increase contribution to open source projects, including allocating employee time and providing education on the value proposition.
* The time spent contributing to open source projects was also investigated, with some respondents reporting working as many as 40 hours per week on open source projects.
* The survey found that there is a difference in how employers support open source contributions between different regions, with Europe leading in employer support and Asia Pacific focusing more on fostering a global technology standard and funding the commercial open source startup ecosystem.
* The survey also asked about the sustainability of open source projects and whether respondents believe their organizations could improve sustainability by investing in open source across geographic regions.
* The conclusion emphasized the importance of realizing responsibility, following contribution steps, and using open source to help advance innovation within organizations.


## AO.Space: An Open Source Solution for Personal Data Ownership - Wang Jianmin

URL: [https://www.youtube.com/watch?v=IjCiYb7rypg](https://www.youtube.com/watch?v=IjCiYb7rypg)

 * Speaker, Wang Jianmin, is an engineer and leading researcher at the Institute of Software, Chinese Academy of Sciences
* He attended Linux Foundation Europe Summit in April 2019 and introduced his open source project, AO.Space
* AO.Space focuses on protecting personal data ownership and was inspired by concerns over privacy and security with home cameras and social media platforms
* Goals: solve dependency issues, address digital world account termination or suspension, and provide better ownership of personal data in a decentralized way
* Decentralization is preferred to reduce dependency on centralized internet platforms and prevent monopolization
* Proposed design includes:
  + Decentralized identifiers (ID)
  + Documentary representation of owned private key
  + Public-private key authentication and authorization
  + Multi-based authentication
  + Document signature and history chain
* AO.Space aims to improve security, allow user control over public and private keys, and prevent false account changes by third parties
* Also supports different architecture designs and open source hardware technology for better data protection.


## Workshop: Building and Managing an Open Source Program Office - Ibrahim Haddad, The Linux Foundation

URL: [https://www.youtube.com/watch?v=Po44mYILw94](https://www.youtube.com/watch?v=Po44mYILw94)

Split:[4571, 4570]
 * Ibrahim Haddad from The Linux Foundation discusses building and managing an Open Source Program Office (OSPO)
* Experience working in open source at Ericsson, IBM, Intel, and Samsung
* Critical role of open source in modern infrastructure and business
* Benefits of open source for organizations include access to talent, cost savings, innovation, and partnerships
* Importance of having a formal open source strategy and culture within an organization
* Challenges of managing open source usage and contributions, including compliance and infrastructure
* Importance of clear policies and communication around open source usage
* Case studies from Motorola, Ericsson, and Samsung on implementing open source strategies
* Building an OSPO includes setting up processes for contribution management, compliance, and community engagement
* Continuous growth in open source adoption across industries according to Linux Foundation surveys.
 * Ibrahim Haddad from The Linux Foundation discusses building and managing an Open Source Program Office (OSPO)
* Different models for setting up an OSPO: corporate level, independent office, virtual team
* Importance of having an OSPO to manage open source projects, ensure compliance, and build a culture of open source within a company
* Role of an OSPO includes contributing to open source projects, tracking metrics, implementing inner sourcing, and creating guidelines
* Challenges faced when implementing an OSPO include education, budgeting, and maintaining open source infrastructure
* Best practices for running an effective OSPO include providing clear guidance, fostering a cooperative mindset, and facilitating collaboration with competitors
* Case studies from companies such as Microsoft and Google illustrate the benefits of having an OSPO.



## A Milestone for Open Source Security: How the Brand New ISO... - Katharina Grauf & Marcel Scholze

URL: [https://www.youtube.com/watch?v=QUEpiM_yf9I](https://www.youtube.com/watch?v=QUEpiM_yf9I)

 * Speaker: Katarina Grauf from PwC Germany, discussing ISO 18974 and its synergy with ISO 5230
* ISO 18974 focuses on open source security management
* Synergy between ISO 5230 (open source compliance management) and ISO 18974
* ISO 5230 was successful in reducing risk in software supply chains and building trust
* Germany's Open Source Management Study shows an increase in adoption of open source management standards like ISO 5230
* Importance of managing open source security properly due to increasing complexity in software supply chains and recent major incidents (Log4j, LogShell)
* Government regulators are recognizing the need for professional measures to manage open source security
* ISO 18974 offers standardization and transparency in managing open source security incidents professionally
* Similarities between ISO 5230 and ISO 18974, including content review and approval, policy scoping, competency definition, and awareness programs
* SBOMs (Software Bill of Materials) are crucial for handling open source license compliance and identifying vulnerabilities in the supply chain
* ISO 18974 is a stepping stone towards security for organizations that have already adopted ISO 5230
* Benefits of certification include building trust within the supply chain, reducing internal effort, and providing valuable feedback.


## Will Large-Scale Automated Scanning Stop Malware on OSS Repositories? - Zachary Newman

URL: [https://www.youtube.com/watch?v=QgISuuhBPhU](https://www.youtube.com/watch?v=QgISuuhBPhU)

 * Zach Newman discussing whether large-scale automated scanning can stop malware in open source software repositories
* Background on malware detection methods: signature-based and behavior-based
* Signature-based detection uses a list of known malware signatures to identify malicious files, but it's not foolproof as malware can change its signature
* Behavior-based detection monitors software behavior and flags suspicious activity, but it can generate false positives and miss new, unknown malware
* Discussion of the importance of malware detection in open source software repositories, especially those tied to operating system ecosystems like apt, Homebrew, Portage, etc.
* Curated community-based repositories versus open repositories where anyone can submit packages
* Challenges of implementing malware scanning solutions in open source projects due to limited resources, false positives, and latency concerns
* The importance of human review and confirmation for suspicious packages flagged by automated tools
* Discussion of existing malware detection tools like OSS detect, Bandit, and others
* The need for a balance between false positives and catching known malicious packages in a timely manner
* The benefits of implementing malware scanning solutions like improved security and increased user trust.


## Panel Discussion: The Impact of the CRA on the... - Cheukting, Mirko & Greg, Laura, Justin, Philip

URL: [https://www.youtube.com/watch?v=Wx-vwgOZSFk](https://www.youtube.com/watch?v=Wx-vwgOZSFk)

 * The panel discussion aimed to address concerns regarding the Cyber Resilience Act (CRA) and its impact on open source software.
* Justin Colino, a board member of OSI and lawyer at Microsoft, focused on how CRA affects the secure supply chain and GitHub's compliance efforts.
* Philip Robb, from Erickson Software Technology, discussed how the CRA impacts their work in the open source ecosystem, particularly in relation to Linux and Kubernetes.
* The panel agreed that the CRA's goal is to reduce vulnerability in digital products throughout their life cycle and enable informed consumer decisions.
* The CRA applies to both commercial and non-commercial entities providing digital products to the European Union market, regardless of where they are located.
* Open source projects and their developers could be affected if they meet certain criteria, such as being a for-profit organization or having commercial activity associated with the project.
* The CRA requires reporting, fixing covered vulnerabilities, providing software updates, auditing, and certifying products.
* There is concern that the open source development process may be negatively impacted by the record keeping, vulnerability closure, and disclosure requirements in the CRA.
* One proposed solution is for organizations to work together through a task force or open forum to submit well-thought proposals to fix the CRA.
* The panel discussed potential ambiguity and inconsistency in the definition of roles and responsibilities under the CRA, particularly regarding developers and security engineers.
* Some concerns were raised about the cost and time implications for both commercial software producers and consumers.
* It was suggested that a unified international standard could help address these challenges and ensure a level playing field.
* The panel agreed that the CRA has good intentions but may not be perfectly implemented, and they emphasized the importance of continued conversation and collaboration to find solutions.


## BoF: How to Build a Tech Community: The Fine Art of Organizing Meetups - Juan Manuel Perafan, Xebia

URL: [https://www.youtube.com/watch?v=e7cGqsqLkmU](https://www.youtube.com/watch?v=e7cGqsqLkmU)

 * Juan Manuel Perafan, born in Colombia and currently based in the Netherlands, shares his experience organizing meetups and building tech communities
* He discovered his ability to organize events during his college days, realizing it was a valuable skill outside of university time
* In 2018, he started organizing Amsterdam Data Visualization Meetup with no sponsorship or company support
* Perafan emphasizes the benefits of organizing meetups for marketing (reach relevant audience), leadership (practicing project management and networking), and networking (meeting peers in different industries)
* He mentions the challenges, such as finding a venue, handling sponsors, and recruiting speakers
* To create a successful meetup, Perafan suggests determining a specific topic with a balance between beginner and advanced levels, creating an identity for the event, using Meetup.com to reach potential attendees, and focusing on networking
* He also mentions the importance of finding two or more speakers, having a clear vision, and handling marketing effectively
* Perafan stresses that organizing meetups should not be a full-time job and suggests involving a team of two or three people to share the workload.


## The Compiler Plugin Framework to Facilitate Customized Compilation... - Yongnian Le & Mingchuan Wu

URL: [https://www.youtube.com/watch?v=fqunF73F1Yg](https://www.youtube.com/watch?v=fqunF73F1Yg)

 * Speaker: Architect of GCC compiler in Open Ola community, Ming Chao
* Topic: Customized Compilation Development using Pink Plugin Framework for multiple compilers (GCC, VM, etc.)
* Motivation: To reduce development effort and improve collaboration within the open-source community.
* Background: Open Ola is an operating system with a digital infrastructure team, including a compiler special interest group. The team consists of developers from different companies and countries, collaborating on improving compilers like GCC.
* Problem: Developers face challenges when working with multiple compiler infrastructures, such as compatibility issues, building plugins for different versions, and maintaining them.
* Solution: Compiler plugin framework (Pink) to reduce repeated building and testing time, decouple intermediate representation, provide common capabilities like logging and verification, and standardize interfaces between plugins and compilers.
* Features:
  + Decoupled IR and plugins.
  + Provides a server for plugin communication, quick compilation, and compatibility checks.
  + Offers debugging capabilities and integrative verification support.
  + Common capabilities like logging, verification, and user authentication.
* Advantages:
  + Reduces development time and effort by reusing plugins across different compilers.
  + Enables collaboration between developers working on different projects.
  + Provides a standardized interface for plugin development.
* Current challenges: Improving coverage of IR function transformation, extending the plugin mechanism to support more compiler infrastructure, and collaborating with upstream communities to improve compatibility.
* Future plans:
  + Enhance IR capabilities (covering 70-80% of GCC's functionality).
  + Improve user experience by adding a login capability, integrated verification, and compatibility checks.
  + Collaborate with the upstream community to extend the current framework and compare compiler infrastructures.


## Greening the AI Cloud: Validating Power Models for Kubernetes Containers - Marcelo Amaral

URL: [https://www.youtube.com/watch?v=nqgcKTlbsqY](https://www.youtube.com/watch?v=nqgcKTlbsqY)

 * Marcelo Rao from IBM Research Tokyo presents a talk on measuring energy consumption in application clouds
* Motivation: climate change and the need to reduce greenhouse gas emissions, especially in the context of growing data transfer and computation power
* Kepler is an open source project for measuring energy consumption at the container, pod, and job level in Kubernetes
* Kepler uses a power model to estimate energy consumption based on real-time parametrics, such as CPU time and network throughput, collected using BPF (Berkeley Packet Filter)
* Power models are available for bare metal nodes and VMs, with support for different architectures like x86 and s390x
* Kepler can also be used to measure power consumption per process and per GPU, with the ability to partition GPUs for different processes
* Different scenarios for energy measurement: accurate access to power matrices (best), pretrained power models in public clouds (current), and future requirements for accurate measurements from cloud providers.
* Idle power is a consideration in energy efficiency, with different approaches for dividing idle power across VMs or using green gas protocols.
* Earth ML Perth benchmark tool is used to analyze machine learning workloads and compare performance across different GPUs and runtimes.
* Kepler can be deployed using Helm or manually, and exposes metrics for energy consumption at the container level.
* Users are aware of energy consumption through tools like Grafana dashboards, and can change parameters to optimize for energy efficiency.
* Different backends (e.g., Torque, TensorFlow Onyx) can be used with Kepler depending on the workload.
* Testing workloads for performance and energy consumption is important, and different runtimes may perform differently.
* Kepler exports energy consumption data in a format similar to Prometheus, and allows developers to check occurrences of different metrics using various regression algorithms.
* Future directions include improving the accuracy of power models, integrating with scheduling systems like Kappa and Capper, and providing more visualizations for energy consumption analysis.


## Establishing Trusted and Secure Foundation for Device Management Using Open... - Tushar Khandelwal

URL: [https://www.youtube.com/watch?v=sNIE9Wx2wGg](https://www.youtube.com/watch?v=sNIE9Wx2wGg)

 * Tushar Khandelwal discussing IoT device management and the role of attestation in establishing a secure foundation
* ITF Rat architecture standard used for device management, including device registration, remote management, firmware upgrade, fault management, and reporting
* Attestation: establishing trustworthiness through trusted execution environment and creating an attestation token for verification
* Verifier verifies the attestation token and takes a decision based on it
* Two interaction models for verification: passport model and background check model
* Components used in POC include Verizon's Wakama, Arm TrustZone, and the Lightweight M2M protocol
* Devices connect to a server using the Lightweight M2M protocol and TLS secure communication
* Trusted Services verify evidence during provisioning and verification stages
* Linux running on both device and server sides, with secure enclaves and firmware for security
* Communication between relying party server and verifier using TLS handshake and token exchange.


## Building SaaS Services with CHAOSS Technology to Evaluate Community...- Daniel Cortázar & Yehui Wang

URL: [https://www.youtube.com/watch?v=w9CL-trz-I0](https://www.youtube.com/watch?v=w9CL-trz-I0)

 * Daniel Cortázar and Yehui Wang discussed building SaaS services using CHAOSS technology for evaluating community health in open source projects.
* CHAOSS stands for Community Health Analytics Open Source Software and provides metrics, models, and tools to assess the health of open source communities.
* The concept of community health is subjective and can be measured through various metrics like user care, collaboration, diversity, inclusion, risk, and working group focus.
* CHAOSS uses a Matrix model that covers different dimensions and personas to evaluate community health.
* The Matrix model includes productivity, robustness, niche creation, collaboration development index (CDI), and organization activity.
* CHAOSS has evolved from a research project to a commercial product with various use cases like service providers, corporations, and individual contributors.
* Some key features of CHAOSS include its ability to gather data from various sources like GitHub, Jira, Slack, and CI/CD tools, and provide visualization and reporting capabilities.
* CHAOSS has been adopted by several organizations, including OSS Compass, which uses it as a platform for niche-based community management and collaboration analysis.
* The future of CHAOSS includes the launch of new project management data dashboards and the development of flexible algorithms to accommodate different use cases.


## Scaling the Security Researcher to Eliminate OSS Security Vulnerabilities Once... Jonathan Leitschuh

URL: [https://www.youtube.com/watch?v=x-LvwZOOvtU](https://www.youtube.com/watch?v=x-LvwZOOvtU)

 * Jonathan Leitschuh, senior software security researcher at Project Alpha Omega and Dan Kaminsky Fellow, discusses eliminating open source security vulnerabilities
* Started with a simple vulnerability: using HTTP instead of HTTPS to resolve dependencies in build files
* Attacker can hijack CI pipelines or machine running locally
* Impacted major organizations like Spring, Apache Software Foundation, Red Hat, and Jenkins
* Created the Fern Initiative to push for decommissioning support for HTTP in artifact servers and encourage use of HTTPS instead
* Despite blog post announcing deprecation of HTTP, many still using it
* Used CodeQL, a code analysis tool, to find vulnerable projects by querying GitHub
* Found over 1500 critical vulnerabilities across open source ecosystem
* Developed a Python-based wrapper for GitHub's Hub CLI to automate the process of generating and submitting pull requests for these fixes
* Discussed three types of vulnerabilities he tackled: temporary directory hijacking, partial path reversal, and zip slip
* For temporary directory hijacking, attacker can create a file in a shared temporary directory with the same name as one in a different user's directory, and the second user will see the attacker's file instead of their own
* For partial path reversal, an attacker can access sibling directories by reversing the order of a prefix in a file system path
* For zip slip, an attacker can create a malicious zip file with a key/path that tricks the victim into extracting it to a directory outside the original destination.
* To fix these vulnerabilities, he used open rewrite to manipulate abstract syntax trees and keep formatting intact while making targeted changes
* Encouraged using automated transformations to scale security research across open source projects.


## Contributor Growth Strategies for OSS Projects - Dawn Foster, CHAOSS

URL: [https://www.youtube.com/watch?v=xRCFHhL1IgE](https://www.youtube.com/watch?v=xRCFHhL1IgE)

 * Dawn Foster, CHAOSS initiative at The Linux Foundation, discussing strategies for sustainable contributor growth in open source projects
* Human involvement essential for open source projects, but maintaining them can be overwhelming and burnout is common
* Strategies for growing the contributor base:
  + Motivation: clearly communicate project goals, provide recognition and appreciation
  + Governance: clear documentation, fair leadership transition, diversity and inclusion initiatives
  + Onboarding: reduce barriers to entry, make process transparent, mentoring and sponsorship opportunities
* Challenges in implementing strategies include time constraints, complexity, and uncertainty.
* Metrics can help identify problem areas and make informed decisions.
* Collaboration is key to project success, with clear roles, expectations, and communication.
* Mentoring, shadowing, and leadership development are important for scaling projects and reducing the load on existing maintainers.
* The importance of a welcoming and inclusive community cannot be overstated.
* Minimal viable governance models can help small projects get started without overloading them.
* Collaborative decision-making and transparency are essential in open source projects, even for smaller ones.
* Continuous improvement is necessary to maintain the health and growth of an open source project.


## Keynote: From Artisans to AI: The Evolution of the Open Source Ecosystem - Ed Parsons, Google

URL: [https://www.youtube.com/watch?v=FPq0m4B4BoQ](https://www.youtube.com/watch?v=FPq0m4B4BoQ)

 * Ed Parsons from Google presenting virtually due to travel issues
* Artisans and developers' role has changed with the emergence of artificial intelligence (AI)
* AI is used in various applications such as answering questions, geospatial technology, and building new products
* Open source data plays a crucial role in the development of new code and services, especially for AI
* Machine learning requires large volumes of data to train models, which has impacted the open source community
* Regulatory concerns are emerging around machine learning and software development
* The aviation industry can draw parallels with the software industry's evolution towards regulation and quality assurance
* The open source ecosystem needs active participation from individuals and organizations to remain healthy
* Google is committed to being a steward of the open source ethos
* There needs to be open communication between technologists, developers, and legislators to avoid poorly crafted regulations that could harm innovation.


## Keynote: Welcome & Opening Remarks - Gabriele Columbro, Exec. Dir., FINOS & Linux Foundation Europe

URL: [https://www.youtube.com/watch?v=hc6r190NYvk](https://www.youtube.com/watch?v=hc6r190NYvk)

 * Gabriele Columbro, Executive Director of FINOS and Linux Foundation Europe, welcomes attendees to the conference
* Thanks sponsors: Google, Fujitsu, and others
* Shout-outs to program committee and chair
* Housekeeping announcements: WiFi password, schedule, badge information, sponsor showcase floor, coffee breaks, arcade game in hallway track
* Mention of Woman nonbinary open source lunch with registration required
* Expert session for new contributors and export sessions located on sponsor showcase floor zero
* Announcement of Linux Foundation Europe Spotlight 2023 survey focusing on advancement of Open Source specifically in Europe
* Discusses the increasing focus on open source in industries undergoing digital transformation, including financial services, public sector, energy, and insurance
* Talks about the importance of open governance and collaboration in the open source community
* Announces themes for the conference: open source sustainability and open source security support
* Discusses the role of open source in addressing pressing challenges like climate change and biodiversity loss
* Mentions the intersection of Open Source and AI, and the democratization and innovation happening in this area
* Announces Expert panel on Thursday to go deeper into findings from Linux Foundation Europe Spotlight 2023 survey
* Encourages attendees to engage with the open source community and support upstream projects.


## Keynote: openEuler: Ushering in a Future of Intelligent, Diversified Computing - Xinwei Hu

URL: [https://www.youtube.com/watch?v=f9vD5DYBhpw](https://www.youtube.com/watch?v=f9vD5DYBhpw)

 * OpenEuler is an open-source operating system for intelligent and diversified computing
* Diversified Computing is important due to the rapid growth in computing power demand, especially for AI and IoT
* Current data centers waste a significant amount of computing power and face challenges with managing heterogeneous devices and memory
* OpenEuler aims to manage and unify diverse devices and memories with features like GM (Genode-based Memory Management) and converged operating systems
* OpenEuler also provides a single operating system instance for edge and cloud scenarios, enabling technology sharing and simplifying interconnections
* OpenEuler is improving its software components to support AI applications more effectively through projects like Copilot and optimized AI model compilers
* The community behind OpenEuler has grown significantly in the past three years with over 300-4000 daily active developers and 100+ community members using it daily
* OpenEuler is focusing on real-world scenarios and landing technologies for wider adoption, including carrier, finance, and public facilities.


## Keynote: Fireside Chat with Ola Ben Har and Marie Austenaa, OpenWallet Foundation

URL: [https://www.youtube.com/watch?v=jb8A9xCUjQc](https://www.youtube.com/watch?v=jb8A9xCUjQc)

 * Ola Benhar: Leads developer relations team at Google, working closely with Open Wallet Foundation and representing Google in open source projects like Google Wallet, Android, and Chrome
* Marie Austenaa: Represents Visa in the Open Wallet Foundation
* Digital wallet ecosystem dependent on loyalty cards, ticketing, and identification
* Open Wallet Foundation focuses on creating a trusted ecosystem based on open standards to ensure consumer protection, interoperability, security, and accessibility
* Google is collaborating with secure element vendors around the world to make Android devices more secure
* Interoperability is crucial for wallet use across borders and different systems
* Visa's perspective: Wallets are becoming everyday tools, and ensuring they are interoperable with existing payment systems is essential
* Open Wallet Foundation aims to bring together industry, government, non-profit organizations, and technology companies to create comprehensive digital identity and wallet solutions accessible across the globe.
* Google's Android team is building a highly secure privacy-forward solution for everyone.
* Ping Identity announced sharing credential formats, and Microsoft joined the Open Wallet Foundation recently.
* Open discussion and collaboration across different Linux projects are essential.
* Major technology companies and governments have joined the Open Wallet Foundation to ensure interoperability and common solutions.


## Keynote: OpenSearch, Open Security: Bringing Transparency to Our Security Processes - Dave Lago

URL: [https://www.youtube.com/watch?v=cLe3HynpiNY](https://www.youtube.com/watch?v=cLe3HynpiNY)

 * Dave Lago from AWS Open Search Security team
* Discussed bringing transparency to security processes in OpenSearch
* Context: Complex open source project (Derived from Elasticsearch, Apache, and Cabana)
* Challenges: Mature internal security processes vs newborn open-source project
* Considerations: Diverse install base, ecosystem of partners and vendors
* Security processes: Pentesting, Security reviews, Aggressive vulnerability remediation
* Transparency: Importance in a community setting, vulnerability disclosure process
* Pre-disclosure list for partners
* Public discussion on GitHub, Slack, Zoom meetings
* Openness: Balancing speed, correctness, and security
* AWS example: Transparent internal security review with extensive testing
* Community involvement in feature discussions
* Commitment to open source best practices
* Vulnerability remediation: Committing fixes publicly
* Recent independent security audit report impressed reporter
* Encourages reporting and collaboration through a private fork
* Engage GitHub for help in making OpenSearch better.


## Keynote: Thrive with Clean Code - Jonathan Vila, Developer Advocate, Sonar

URL: [https://www.youtube.com/watch?v=JG6KQIhyfew](https://www.youtube.com/watch?v=JG6KQIhyfew)

 * Jonathan Vila, Sonar developer advocate and Java Champion, emphasizes the importance of clean code
* Two trillion dollars spent annually on fixing poor quality code in the USA, with four days spent per developer
* Clean code follows four main attributes: consistent format, clear intentional design, efficient use of resources, and adaptability
* Clear focus on goal, modular design, and test-driven development are important aspects of clean code
* Sonar provides tools for analyzing code quality, identifying issues, and following best practices
* Sonar supports open source projects and integrates with various development platforms
* Sonar Cloud offers a free edition for analyzing open source projects, including 87,000 projects from the Apache Software Foundation, Eclipse Foundation, and others
* Tools like Sonar Link, Sonar Cube, and IDE plugins can be used to check code type, learn about issues, and follow methodologies for fixing them.


## Keynote: Keeping Open Open - Bryan Che, Chief Strategy Officer, Huawei

URL: [https://www.youtube.com/watch?v=aiouSeb-HGc](https://www.youtube.com/watch?v=aiouSeb-HGc)

 * Huawei believes in keeping the open ecosystem alive and ensuring it remains open
* Open means open source, with software licensed under certified open source licenses like Apache License
* Huawei released an open source project called Quark earlier this year for multi-sandbox container capability in cloud computing
* Open governance is important, as seen in Huawei's involvement with the Cloud Native Computing Foundation (CNCF)
* The CNCF IP Charter ensures that all code must be open source and cannot be relicensed or withheld
* Some companies want to use open source technology for business benefits but don't believe it should be freely available to everyone
* Huawei also released another open source project called Expanses as part of the New Open Services Cloud initiative
* The European Union's Cyber Resilience Act could create potential threats and Huawei has filed a response with the European Commission
* Companies selling open source-based products must be able to comply with strict security regulations
* Open participation is important, from individuals to large companies like Huawei, as we all build on each other's work in the global community.


## Keynote: The Evolving OSPO - Nithya Ruff, Director, OSPO, Amazon

URL: [https://www.youtube.com/watch?v=wkZMkRz_nmY](https://www.youtube.com/watch?v=wkZMkRz_nmY)

 * Nithya Ruff, Director of OSPO at Amazon, discussed the challenges and opportunities for Open Source Program Offices (OSPOs) in large companies, governments, and institutions in 2023.
* She highlighted that this year has been challenging due to economic headwinds and the ongoing pandemic.
* Ruff shared her experience of working in open source for over 25 years and how it has become mainstream and pervasive.
* She discussed five key areas where OSPOs have faced challenges and opportunities:
    1. Licensing: Companies need to understand open source licenses and ensure they can be used without legal or procurement issues. Confusion around open-source licensing has held back innovation in the past.
    2. Openish: With open source becoming more widespread, there is a risk of it being taken in a closed or restricted way, which creates uncertainty and confusion.
    3. AI: Open source plays an essential role in the development of AI, but there is a lack of standard definition and understanding of what open source means in the context of AI.
    4. Security: The supply chain for open source software is complex, with different players involved, from maintainers to foundations and regulators. Collaboration and coordination are necessary to ensure security.
    5. Open Source Program Offices (OSPOs): OSPOs play a crucial role in reducing risk, ensuring integration of open source into development processes, and removing friction for developers. They also advocate for open source in the public sector and work with regulators to ensure proper regulation.
* She concluded by emphasizing the importance of neutral governance, standard definitions, collaboration, education, and advocacy in the open source community.


## Keynote: Welcome Back Day 3 - Gabriele Columbro, ED, FINOS & GM, Linux Foundation Europe

URL: [https://www.youtube.com/watch?v=QpDhu2F3NbI](https://www.youtube.com/watch?v=QpDhu2F3NbI)

 * Gabriele Columbro, ED of FINOS and GM of Linux Foundation Europe, welcomes attendees to Day 3
* Housekeeping items: Speed mentoring at 11:00am, third-party ask the expert session, morning break at 10:30am
* Theme for the day: Open Source AI
* Ibrahim Adamus, Executive Director of LF Data, speaks about LF Data's efforts in open source AI
  + Started 5 years ago with one hosted project, now 55 hosted projects
  + New effort focusing on data, ML Ops, and ML security launched in the past month
  + 650 organizations contributing code across various metrics
  + Intel, IBM, AWS join as new members of LF Data
* Generative AI Commons initiative announced to bring organizations together for collaborative work
- New LF Incubation project, Luther AI Community, welcomed
* LF Data showcases growth and expansion in the field of open source AI
* Research collaboration between LF Data and LF Research organization discussed
* Linux Foundation Europe update on initiatives like Open Wallet, Silvaplus, and public sector engagement.


## Keynote: The Sovereign Tech Fund: Investing in Open Source In... Fiona Krakenbürger & Tara Tarakiyee

URL: [https://www.youtube.com/watch?v=9knCTZNp8QI](https://www.youtube.com/watch?v=9knCTZNp8QI)

 * The Sovereign Tech fund is an initiative to invest in open source infrastructure supported by the German Federal Ministry for Climate Action and Economics.
* Open source infrastructure is critical for modern digital society and often overlooked when it comes to resource allocation.
* The Sovereign Tech fund was inspired by a feasibility study published in 2020, which outlined the need for public money to support maintenance of digital infrastructure in the public interest.
* The fund was created in late 2021 and has already supported several projects, including curl and OpenBSD.
* The Sovereign Tech fund provides contract work to maintain important technologies and helps organizations rewrite critical infrastructure.
* The fund invests in core foundational technologies and partnerships with organizations like the openJS Foundation.
* The approach of the Sovereign Tech fund is to ensure that financial resources are allocated towards maintaining digital infrastructure in a sustainable way.
* The speakers, Fiona Krakenbürger and Tara Tarakiyee, discussed the importance of investing in open source infrastructure maintenance and the challenges of relying too heavily on volunteers or underfunded projects.
* They also highlighted the need to support technical depth and timely opportunities for infrastructure improvement.
* The Sovereign Tech fund aims to build a complimentary program to support open source developers and maintainers in a sustainable way, and continue advocating for public policy that prioritizes investment in digital infrastructure.


## More Renewable Energy Into the Power Grid with Open Source - Jonas van den Bogaard & Nico Rikken

URL: [https://www.youtube.com/watch?v=DicVQbyhedU](https://www.youtube.com/watch?v=DicVQbyhedU)

 * Jonas van den Bogaard and Nico Rikken from Alander, the largest distribution system operator in the Netherlands, discuss the challenges of integrating renewable energy into the power grid and how open source software plays a role in their efforts.
* Alander is responsible for managing the electricity and gas grids for nearly 6 million customers and overseeing nearly 90,000 km of electricity and 40,000 km of gas lines.
* The energy transition poses challenges for companies like Alander as fossil fuels become scarce and renewable energy becomes more prevalent.
* Solar panels, wind energy, and electric cars are creating a major challenge for distribution system operators to support the transition in the Netherlands.
* Alander is investing in digitalization and smart solutions to better use available capacity in the grid and manage congestion.
* Open source software is becoming increasingly important for mission-critical applications in companies worldwide, and Alander sees its potential in their energy projects.
* The Open Staff Power Grid Model Shifter project is an open source initiative that helps distribution system operators integrate renewable energy into the electricity grid and manage congestion through active demand response management.
* Open Source software allows for incremental innovation, collaboration, and crowd innovations to come from both inside and outside the organization.
* Alander is using open source software like Open Sta for forecasting load and generation in the electricity sector and power system analysis.
* The PowerG model library is a python library used for power system analysis and can be integrated with Open Sta for active congestion management.
* Shape Shifter is another open source project that enables trading flexibility to help mitigate issues like congestion in the energy market.
* Active congestion management involves analyzing the grid, determining potential issues, creating incentives for flexibility, and balancing supply and demand to maintain grid stability.
* The Linux Foundation Energy (LF Energy) is an open source foundation that provides a neutral collaborative community to build shared digital investments around energy.
* Open Standards are important in the energy sector as they enable interoperability, flexibility, and innovation across different organizations.
* The Shape Shifter project is built on open standards and has been adopted by several grid operators, consultancy companies, and universities.
* Recent reports published by the Linux Foundation Research highlight the role of open source in the development of the energy sector.


## Illuminating Global Electric Vehicle Battery Supply Chains using Hyperleger... - Coenraad Deventer

URL: [https://www.youtube.com/watch?v=jslC_-35jSg](https://www.youtube.com/watch?v=jslC_-35jSg)

 * Conrad Deventer of CD Circular discusses traceability solution using Hyperledger HFabric platform
* Goal is to illuminate global electric vehicle battery supply chain, addressing complexities and sustainability challenges
  - Critical minerals sourcing responsibility
  - Child labor, sanctioned countries, environmental damage, carbon footprint
* Platform uses blockchain technology for tracking CO2 emissions, material origin, and compliance with regulations
  - Digitizing information from the first mile (mine to refinery) using mobile apps and a digital product passport
  - Real-time data dashboard for customers to see supply chain details, including hotspots contributing to pollution
* Platform also provides CO2 calculation, ESG compliance, and regulatory documentation linking
* The goal is to improve transparency and traceability throughout the supply chain, making it easier for auto manufacturers to make informed decisions about their sourcing
  - Automated risk analysis and anomaly detection based on data quality and multiple data points throughout processing orders
  - Ensuring recycled materials are actually coming from reputable recyclers and not just claimed in contracts signed long ago.
* The platform also provides a CO2 emission tracking dashboard that can be accessed by the final customer, showing the carbon footprint of each item produced.
* The EU battery passport is an example of how this technology could be used to ensure materials are coming from friendly countries and contributing to the tax credit system.
* Security is built into the platform, with selective disclosure and access control for relevant information.
* The platform can integrate with existing manufacturing systems and third-party blockchain instances to enhance in-house offerings and provide real-time data for improvement.
* The ultimate goal is to help organizations improve their responsible sourcing practices and promote circular economy by providing transparency, reducing fraud, and ensuring regulatory compliance.


## Panel Discussion: Advancing..- Anna Hermansen & Kate Stewart, Sumer Johal, Chris Xie, Matthew Sandoe

URL: [https://www.youtube.com/watch?v=K9h4lNOktXo](https://www.youtube.com/watch?v=K9h4lNOktXo)

 * Anna Hermansen: Introduced herself as an ecosystem manager at LF Research and discussed her background in qualitative research and sustainability. Mentioned the recently published report on open source sustainability and its connection to the UN's sustainable development goals.
* Kate Stewart: Introduced herself as the focus lens foundation's executive director for AAC Project Linux Foundation, which aims to achieve efficiency in digital infrastructure for the food ecosystem. Discussed Zephyr project, a small embedded system used for energy management in various applications such as animal tracking and temperature monitoring.
* Suir Johal: Introduced himself as the head of Open Source Strategy at Future and discussed the importance of open source in addressing global challenges such as energy production and consumption, particularly in the context of the Internet of Things (IoT) and telecommunications networks.
* Chris Xie: Introduced himself as the head of Open Source Strategy at Future and spoke about the potential of open source to address various sustainability challenges, including agriculture and climate change, through collaborative approaches and standardization.
* Matt Sandoe: Discussed his background in finance and how he has worked with organizations like BMP Parabank and Goldman Sachs to accelerate financing for decarbonization efforts. Mentioned the importance of open source in providing data and enabling collaboration in climate-related projects.


## How Open Source...- Dan Brown, Hilary Carter, Jonas Bogaard, Christophe Villemer, Bryce Bartmann

URL: [https://www.youtube.com/watch?v=hQvij67v5GM](https://www.youtube.com/watch?v=hQvij67v5GM)

 * Dan Brown moderates panel discussion on open source in energy sector
* Jonas Bogard (Alander): Open source software essential for digitalization in energy sector, especially for grid operators like Alander facing challenges with increasing demand and renewable energy production
* Kristoff Kroes (Salair): Multivendor approach and open source collaboration are key to addressing IT service challenges in the energy sector and accelerating new solutions
* Hillary Carter (Linux Foundation): Regulation and collaboration between regulators, technologists, and industry players are important for the proliferation of clean energy systems and consumer initiatives like peer-to-peer energy trading and blockchain infrastructure
* Bryce Bartmann (Shell): Shell is involved in open source projects to collaborate with partners on digitalization efforts, such as realtime data infrastructure platform, and to make the most effective use of public funds
* Examples given of successful open source projects in the energy sector, including Alander's open staff project for forecasting electricity demand and load, and RTE's RT Cass project for digitizing substations.


## Energy Proportional Edge Computing Infrastructure - Francesc Guim, Intel Corp

URL: [https://www.youtube.com/watch?v=ZCUca4J5ATs](https://www.youtube.com/watch?v=ZCUca4J5ATs)

 * Francesc Guim from Intel's Pathfinding team in the Network Division presented on Energy Proportional Edge Computing Infrastructure
* Discussed motivation for energy management in edge computing with focus on sustainability and reducing carbon emissions
* Traditional deployment models have moved from grid computing to cloud, then to edge, due to power requirements of smaller devices
* Energy proportional systems are becoming necessary for companies aiming for zero carbon deployment by 2030
* Challenges of elastic systems include adapting to changing demands and efficient use of resources in a distributed system
* Three pillars of energy management: embodied carbon (manufacturing), operational carbon (energy consumption), and end-of-life disposal
* Hardware and software components must work together to adaptively manage energy usage at the edge
* Intel is exploring proportional computing systems using IPUs, FPGAs, and other technologies to optimize energy use in real time
* Proportional peak power management involves understanding load patterns and keeping utilization below maximum to save energy
* Elastic time space shifting involves moving processing tasks to locations with available energy and reducing latency by adapting to energy availability
* Intel is working on a prototype of a proportional system using IPUs, monitoring performance and energy usage in real time.


## How to Lead Open Source Projects and Teams with Better Feedback - Jessica Tegner

URL: [https://www.youtube.com/watch?v=KIU5c-5w6Mg](https://www.youtube.com/watch?v=KIU5c-5w6Mg)

 * Jessica Tegner, a blind computer science student and open source project maintainer, shares her experiences with giving and receiving feedback in open source projects
* Feedback is essential for improvement, but it can be challenging to deliver and receive effectively, especially in the open source community
* Defining different types of feedback: positive, negative, constructive, timely, specific, actionable, and sandwiched (positive-negative-positive)
* Maintainers and contributors need to give and receive feedback collaboratively and respectfully
* Negative feedback can be miscommunicated easily and may demotivate or discourage contributors
* Providing clear, specific, and actionable feedback helps maintainers and contributors grow individually and as a community
* Feedback should be given in a positive and constructive manner using the sandwich method
* Physical space, tone, and body language play a role in delivering effective feedback
* Open discussions, offline conversations, and clear communication channels help foster a positive feedback culture in open source projects.


## Panel Discussion: What's the State of... - Hilary Carter, Colin Eberhardt, Sachiko Muto, Mirko Boehm

URL: [https://www.youtube.com/watch?v=D04BB12cWOs](https://www.youtube.com/watch?v=D04BB12cWOs)

 * Hillary Carter: Europe report focuses on collaboration between public sector, industries, and social impact in the European open source ecosystem.
* Key findings:
  + Two modes of collaboration - Europe-based vs industry-developed.
  + Public sector's role as a rule maker interfering with industry is shifting.
  + Procurement can contribute to open source indirectly through contracting companies.
  + Collaboration based on partial consensus allows organizations to share software together and accomplish shared missions.
* Research conducted by the Linux Foundation Europe team, with contributions from Sano Muto and Colin Eberhardt.
* Topics of ongoing research include blockchain, cloud native, IoT, and generative AI across various industries.
* The European report aims to enable continent-wide discussion, ensure open source continues to thrive in Europe, and identify challenges and focus areas for research.
* Findings from the survey and interviews conducted across the community, including insights from stakeholders like Scott Logic and the Linux Foundation Europe Research Institutes Sweden.
* The report is available for free on the Linux foundation's website and was published on August 31, 2023.


## Measuring the Impact of Community Events - Brian Proffitt & Natalie Pazmiño, Red Hat

URL: [https://www.youtube.com/watch?v=QjV6BUA4HxU](https://www.youtube.com/watch?v=QjV6BUA4HxU)

 * Brian Proffitt and Natalie Pazmiño from Red Hat discuss measuring the impact of community events
* Community events are different from industry events, which primarily aim to generate sales leads
* Measuring the impact of community events is challenging due to the intangible benefits they provide, such as community building, networking, and brand awareness
* Metrics for community events include white papers, QR codes, landing pages, and engagement at booths
* Creating dynamic solutions like Slack channels or Discord servers can help engage attendees before and after the event
* Collaboration with other projects and organizations is a key goal of community events
* Engagement metrics, such as attendance numbers and swag pick-ups, are useful but may not capture the full impact of the event
* Community building and attracting new contributors are important goals for community events
* Companies can use community events to recruit talent and build brand awareness.


## Lessons Learned from Organizations' Use of Open Source - Javier Perez, OpenLogic by Perforce

URL: [https://www.youtube.com/watch?v=R0uxgEOZBFo](https://www.youtube.com/watch?v=R0uxgEOZBFo)

 * Javier Perez from OpenLogic by Perforce discussed key findings from the annual OSI survey on open source software usage in organizations
* Over 1,000 respondents provided information about their use of open source software
* Trends include growth in number of packages per day being added to registries and increasing use of containers, cloud native technologies, and data technologies
* Cost reduction is a major reason for using open source software, but support challenges persist
* Europeans are more likely to reduce usage due to cost and development velocity, while Americans prioritize access to the latest technologies and innovation
* Middleware tools like Java Stacks and Apache Tomcat are popular, but there's a shift towards container-native solutions like Kubernetes
* Security is a concern for organizations using commercial software instead of open source tooling, and there's a need for more personnel with expertise in new technologies
* Linux Foundation is the largest organization using open source software, with 850 projects in its top tier
* Longterm support is important for successful adoption of open source software, but shorter support periods are becoming more common due to rapid release cycles
* Organizations should keep track of the versions they're using and update regularly to maintain security and functionality.


## Beyond OSPOs - Build a Strategic Open Source Business Unit - Alois Reitbauer, Dynatrace

URL: [https://www.youtube.com/watch?v=EORWLUySoGY](https://www.youtube.com/watch?v=EORWLUySoGY)

 * Alois Reitbauer, Dynatrace, background in community standardization and open source
* Beyond OSPOs approach to building an open source business unit
* Open source projects can bring value to a company even if they don't directly generate revenue
* Example of Dynatrace's involvement in the OpenTelemetry project and its impact on the industry
* Importance of aligning corporate strategy with open source initiatives
* Challenges in funding and managing an open source business unit
* Strategy for finding and contributing to open source projects that fit the company's goals
* Discussion on the benefits and drawbacks of traditional OSPO models versus a more integrated approach.
* Importance of community engagement and interaction in open source projects
* Role of product management and engineering teams in open source initiatives
* Balancing the needs of a core product team and an open source team
* The role of independent contributions versus product-driven initiatives
* Documentation and communication in open source projects
* Importance of consensus building and prioritization in open source projects
* Challenges and benefits of open source projects for large organizations.


## Accelerating Software Defined Vehicles Through Open Source Software - Dan Cauchy

URL: [https://www.youtube.com/watch?v=noUwAvaEw50](https://www.youtube.com/watch?v=noUwAvaEw50)

 * Dan Cauchy, Executive Director of Automotive Grade Linux (AGL) project at Linux Foundation
* Goal of AGL: Build a single software platform for automotive industry to eliminate fragmentation
* AGL started in 2016 to support infotainment systems; now also supports instrument clusters, telematics, and functional safety
* Over 150 members including major car manufacturers (Honda, Mazda, Mitsubishi, Nissan, Suzuki, Toyota), tech companies (Intel, Qualcomm, NXP, Nvidia), and automotive suppliers (Denso, Panasonic, Harmon, Bosch)
* AGL is open source and uses a unified codebase to alleviate fragmentation
* AGL supports popular apps like Spotify and Google Maps with ease of integration
* AGL releases updates regularly with new features, bug fixes, and long-term support
* AGL is currently working on containerization, webOS support, and functional safety certification
* AGL has been adopted by several car manufacturers including Toyota, Subaru, Mercedes-Benz Vans, and expects more to join soon
* AGL also supports virtualization technologies like KVM and Verdi iio, and is exploring flutter for UI development
* AGL is now a part of the Software Defined Vehicle (SDV) initiative led by Panasonic, Amazon AWS, Volkswagen, and others.


## PyTorch Foundation: 1 Year of Open Governance - Ibrahim Haddad, PyTorch Foundation

URL: [https://www.youtube.com/watch?v=XVPaxPtXKpk](https://www.youtube.com/watch?v=XVPaxPtXKpk)

 * Ibrahim Hadad, Executive Director of PyTorch Foundation, discussing one year of open governance for the project
* PyTorch started in 2016 and became leading AI research tool in academia by 2018
* In September 2022, PyTorch transitioned to Linux Foundation as a host organization under open governance model
* This move signaled market importance of open source commitment and continuous investment in the open source AI ecosystem
* PyTorch Foundation is focused on providing dedicated resources for project infrastructure, marketing communication, and events
* Since joining Linux Foundation, PyTorch has seen significant growth with 60,000 dependencies on GitHub and a community of over 95,000 contributors
* PyTorch Foundation's governance consists of technical leadership and funding body to support the project
* PyTorch Foundation offers training and certification programs for developers and companies looking to adopt PyTorch
* The foundation also hosts events like P Conference and smaller events in different geographies, as well as webinars and video recordings
* In 2024, PyTorch Foundation plans to expand its focus on developer experience, training and certification, marketing events, and Academia adoption.


## GMEM: Generalized OS Memory Management for Accelerators - Weixi Zhu, Huawei

URL: [https://www.youtube.com/watch?v=coQyMz2eODQ](https://www.youtube.com/watch?v=coQyMz2eODQ)

 * Weixi Zhu, Huawei OS technical expert, introducing Generalized Memory Management (GMM) for accelerators
* Originally inspired by PhD study at Rice University with advisors Rickner and Cox
* Motivated by the need for better memory management in AI applications that require CPU-GPU coordination and large amounts of fast memory
* Current accelerators, such as GPUs and TPUs, have poor programmability and limited HBM capacity
* Existing memory management systems like Malo Library face issues with fragmentation and latency
* GM aims to provide high-level APIs and a unified virtual address space for CPU and accelerator pointers
* Unifies memory management system with Linux mm, allowing deeper coordination between the operating system and accelerators
* Improves programmability by sharing CPU accelerator pointers and reducing redundant memory management code
* Enhances performance through user-guided hydrogenous memory hints and transparent memory subscription
* Preliminary evaluation results show faster Malo speed, improved memory utilization, and defragmentation of memory in large applications like protein folding prediction.


## Panel Discussion: Open Source... - Jesús Ruiz, Vanessa Santos, Coenraad Deventer, Hart Montgomery

URL: [https://www.youtube.com/watch?v=PWdoLvpIt4Y](https://www.youtube.com/watch?v=PWdoLvpIt4Y)

 * Hart Montgomery (Linux Foundation, Hyperledger CTO) moderating panel discussion on blockchain in Europe
* Participants: Jesus Ruiz (board member CDOL and Spanish Blockchain Association), Conrad Deventer (Circular), Vanessa Santos (Fujitsu, Enterprise Blockchain Solutions Center)
* Europe's blockchain market lags behind US and Asia in terms of innovation and investment but focuses on solving real-world problems for the region, especially in regulation, sustainability, and the real economy
* Challenges to making blockchain real include education, interoperability, and energy consumption concerns
* Conrad Deventer (Circular) shares experience deploying Enterprise blockchain applications, specifically in supply chain, and addressing challenges through adaptation and learning from business growth and new technology
* Vanessa Santos (Fujitsu) discusses marketing blockchain to potential customers who may not be tech-savvy or familiar with the concept, focusing on real-world problem solutions and benefits like transparency, trust, and sustainability.
* European government focus on protecting citizens and regulation, especially GDPR, creates opportunities for blockchain innovation in areas like identity and digital certificates.
* Europe's advanced infrastructure and support from public and private sectors make it an attractive region for blockchain investment and development.
* Challenges include education, interoperability, and energy consumption, as well as the need for a decentralized governance model and trust frameworks in a pan-European context.
* Blockchain infrastructure is expected to play a significant role in the next generation internet, with potential use cases including public services, identity verification, and traceability across industries.
* European countries are exploring various approaches to creating national blockchains and collaborating on cross-border projects, such as ISB and EAS regulations.
* The panelists encourage collaboration between public and private sectors, focusing on infrastructure development, real-world use cases, and decentralized governance models.


## Fully Verified Open Silicon - Marno van der Maas, lowRISC CIC

URL: [https://www.youtube.com/watch?v=qG6AOnx2WV8](https://www.youtube.com/watch?v=qG6AOnx2WV8)

 * Dr. Marno van der Maas of lowRISC CIC presents on Fully Verified Open Silicon, the open source root trust chip project Open Titan
* Goal is to make open silicon a reality with fully verified hardware
* Open Titan is a secure root trust chip that provides security services like secure boot
* Partners include companies and individuals working to make Open Titan a reality
* Verification is important; in the context of silicon, it means ensuring that the design functions as intended
* Challenges with open source silicon include the lack of an update mechanism once the hardware has been manufactured
* Synopsys Cadence EDA tool is used to translate hardware designs into chip layouts, and support is needed for open source versions
* Open Titan includes open source RTL design for the processor and instruction set architecture, as well as physical design kits
* The project aims to release all IP blocks under permissive licenses, including hardware design kits
* Security is a priority, with a focus on providing a minimum level of security that industry believes is necessary
* Open Titan includes tools for continuous integration and testing, as well as formal verification methods
* Differential fuzzing is used to test the silicon by comparing the behavior of two different programs
* The project aims to make all design artifacts openly available, including coverage results and test data
* There are challenges in verifying individual IP blocks and ensuring interoperability between them
* Verification includes simulation at block and chip level, as well as FPGA testing
* Open Titan uses a three-stage pipeline processor with memory protection units to enhance physical memory protection.
* The enhanced part adds extra security features like the ability to bypass locked rules temporarily
* The project aims to test all aspects of the design, including MML mode lockdown and whitelist policies
* Open Titan includes a library of primitive blocks that are essential for building complex silicon designs
* Clock domain crossing testing is important to ensure that different clock domains interact correctly
* The open source project has a focus on commercial relevance, decision making transparency, issue tracking, and formal request processes.
* The team aims to create a root trust solution that meets ambitious security goals.



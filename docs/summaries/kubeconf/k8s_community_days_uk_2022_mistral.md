## Kubernetes-based platforms - of the people, by the people, for the people | Nicki Watt

URL: [https://www.youtube.com/watch?v=CX3gOeU4200](https://www.youtube.com/watch?v=CX3gOeU4200)

 * Nicki Watt, CEO/CTO of Open Credo, discussing challenges in building successful Kubernetes-based platforms
* Observation: focus on technology often overlooks human developer experience
* Building a platform for internal developer teams requires understanding diverse user communities (developers, data analysts, etc.)
* Clear responsibilities established to avoid blame game behavior
* Self-service and automation are key for user empowerment
* Flexibility and evolvability to cater to different user needs
* Reliability through auto-scaling and configuration management
* Community principles: defining platform contract, promoting freedom within boundaries, practicing role models, respecting community differences.


## Don't blame it on Kubernetes! | Federico Nardini

URL: [https://www.youtube.com/watch?v=CrlvnjdRnH8](https://www.youtube.com/watch?v=CrlvnjdRnH8)

 * Federico Nardini, a technical product manager, tells a story of a project failure related to implementing digital identity services using Kubernetes in the UK government's digital service (GDS)
* The project involved building a trust anchor, German middleware, and a UK proxy node for the European Identity Framework (EIDAS)
* The UK proxy node was built with national cybersecurity center involvement due to security concerns
* However, the team faced challenges in deploying and maintaining the platform due to high risk and complexity, steep learning curve, and resistance from team members unfamiliar with Kubernetes
* The team was under pressure to deliver quickly due to a deadline related to Brexit process
* Senior management forced the team to migrate to another critical infrastructure software, resulting in a 15-month decommissioning process of the Kubernetes platform
* Nardini emphasizes the importance of communication and empathy between teams, gathering data, and maintaining sustainability in operating platforms
* He also stresses the need for careful consideration of skills, training, and processes when building and implementing technology solutions.
* The main takeaway is that technology should not be blamed for failures, but rather the lack of adequate upskilling, training, and consideration of sustainable processes.


## In Clouds We Trust | James Laverack & Josh Van Leeuween

URL: [https://www.youtube.com/watch?v=EaSfAf1ynA0](https://www.youtube.com/watch?v=EaSfAf1ynA0)

 * James Laverack and Josh Van Leeuwen discuss trust in cloud computing, specifically focusing on the issue of compromised private keys and certificate authorities
* TLS (Transport Layer Security) is the foundation of internet security, with certificates given by web servers signed by certificate authorities that clients trust
* Certificate authorities can be distributed inside containers, leading to questions about their updates and storage locations
* The JetStack team created a tool called Paranoia to help find CA certificates in container images and verify their trustworthiness
* Trust management is a significant issue in the cloud native space due to the ease of rogue state signing and default container trust
* Trust Manager, an open source project by JetStack, aims to tackle this problem by providing visibility and control over certificate usage across an organization
* Paranoia and other tools like Chainguard can be used to verify trust bundles and build images with known dependencies
* NYX is a functional programming language that offers clear dependency tracking, which could be beneficial for software supply chain security
* Trust Manager and similar projects are ongoing efforts to address the trust distribution problem in the cloud native space.


## WTF Are Inclusive Communities and How to Maintain Them? | Carla Gaggini & Jade Amic

URL: [https://www.youtube.com/watch?v=FIjkWKJdvWY](https://www.youtube.com/watch?v=FIjkWKJdvWY)

 * Title: WTF Are Inclusive Communities and How to Maintain Them?
* Speakers: Carla Gaggini and Jade Amic
* Agenda: Definition, Building, and Maintaining an Inclusive Community
* Definition: Inclusive community is a space where people are welcomed, valued, and respected regardless of their differences such as gender, gender identity, sexual orientation, political view, marital status, name, or proficiency.
* Building: Creating a safe space requires empathy, psychological safety, support, and accountability. Giving everyone a voice, creating shared values, and representing values through characters can help bring people together and facilitate meaningful change.
* Maintaining: Regularly unpacking words and meanings, creating representation and character, and having open and honest conversations are key to maintaining an inclusive community. Accountability and constant learning are essential.
* Carla Gaggini is the curator of the container Solutions Slack channel within the tech community and a writer. She cares deeply about people in her community and is passionate about creating safe spaces for them.
* Jade Amic is the head of marketing at Container Solutions and is known for her excellent strategy, creativity, ingenuity, determination, kindness, and understanding. She shares Carla's passion for building something that leaves the world a better place.
* Inclusive community in tech is important because it fosters belonging and creates a sense of connection among individuals with diverse experiences. It allows everyone to bring their unique perspectives to the table and create shared value.
* The WTF Cloud Native Community was created by Carla and Jade in 2020 as a response to the pandemic and has since grown to over 4,000 subscribers, run bimonthly collections, and host events, podcasts, and conferences to facilitate learning and conversation.
* Maintaining an inclusive community requires creating a safe space for open and honest conversations, holding people accountable for their behavior, and constantly working towards shared values and understanding. It's important to remember that everyone makes mistakes and that empathy always wins.


## Stop wasting time: Use Falco Plugins to extend detection with any event stream | Alba Ferri

URL: [https://www.youtube.com/watch?v=YbkpIn-scaA](https://www.youtube.com/watch?v=YbkpIn-scaA)

 * Alba Ferri, senior product marketing manager at Cisco Systems, discusses Falco plugins in the context of extending detection capabilities with any event stream
* Falco is an open-source project within the Cloud Native Computing Foundation (CNCF) that helps answer security questions in real time
* Originally created by Sysdig in 2016 and joined CNCF in 2018, Falco collects system call events at the kernel level and enriches them with user space libraries
* Plugins extend the functionality of Falco by adding new data sources, extracting specific fields from event streams, and performing filtering or analysis
* The plugins framework follows Falco's runtime security philosophy based on parsing data in a streaming fashion and implementing real-time detection with a lightweight engine
* Examples of plugins include:
  + OCTA plugin for identity management (extracting OCTA log events and detecting suspicious activity)
  + AWS Cloudtrail plugin for collecting and analyzing AWS cloud trail events (detecting Lambda function configuration updates or S3 bucket encryption changes)
* Creating a Falco plugin involves picking a source ID plugin, writing the plugin code in C/C++, and registering it with the Falco library
* Resources for creating plugins include the project documentation, developer guide, and weekly meetings on Wednesdays at 4 pm UTC.


## Secret Management: The Soft Way | Lian Li

URL: [https://www.youtube.com/watch?v=Z80ns81QbeE](https://www.youtube.com/watch?v=Z80ns81QbeE)

 * Leanne Lee, developer advocate at Loft Labs, discussing secret management in software using a softer approach
* Background: software developer, web developer, devops, kubernetes, former cloud native consultant
* Importance of secret management: prevent credential exposure, maintain desired state environments, ensure secure access to secrets
* Two options for managing secrets:
  + Encrypt and deliver the secret: use tools like sealed Secrets or Subs, keep secret in a git repository, decrypt and apply to cluster
  + Reference a secret stored elsewhere: use a hashed secret store like Vault, grab secret from external operator, create kubernetes secret
* Benefits of using open source tooling for managing secrets
* Desire path: avoid leaving system open, keep security in mind, provide good developer experience
* Summary: manage secrets separately, don't put them in git repository, use external tools or hashed stores to securely deliver and reference secrets.


## Be a Good Corporate Citizen in Kubernetes | Dawn Foster

URL: [https://www.youtube.com/watch?v=ekKUX-8erhw](https://www.youtube.com/watch?v=ekKUX-8erhw)

 * The speaker has worked in the technology industry for 20 years and is involved in various open source projects and communities, including Kubernetes.
* Individual contributors can move from being a bottom contributor to leadership positions within the community.
* Companies also participate in Kubernetes by dedicating time and resources of their employees.
* The Kubernetes community consists of many special interest groups (SIGs) and working groups that collaborate on subprojects.
* Balancing individual and company interests can be challenging, as companies want to ensure their contributors are happy and contributing effectively to the project without conflicting with the open source community's needs.
* Open source contributions should align with a company's overall business strategy for justification and retention of talent.
* When pitching Kubernetes contributions to executives, it is important to describe the contributions in terms of how they support the overall goal of the company, rather than as charitable work.
* Determining where to focus contributions within Kubernetes requires understanding the current pain points and future product strategy.
* To get started contributing, join relevant mailing lists, attend meetings, and familiarize yourself with contribution guidelines and expectations.
* Collaboration is key in Kubernetes, with a focus on easy work and influence rather than strict control.
* Mentorship programs are available to help new contributors get started and learn the ropes from experienced contributors.
* Encouraging employees to attend Kubernetes events can lead to valuable relationships and learning opportunities.
* Within Kubernetes, there is a focus on decentralization, authority, and decision making through technical design, code ownership, documentation, and delegation of responsibility.
* Employees should be encouraged to engage with the community in a helpful way and show appreciation for their hard work.
* Kubernetes requires a welcoming, respectful environment that values different perspectives and skills.
* Mentorship and sponsoring newer contributors is expected within the Kubernetes community.
* Companies benefit from the status gained by having active contributors within the community.
* It is important to find a balance between individual and company interests in contributing to Kubernetes, with a focus on what's best for the community overall.


## Managing Kubernetes without losing your cool | Marcus Noble

URL: [https://www.youtube.com/watch?v=fnLRFGaG9II](https://www.youtube.com/watch?v=fnLRFGaG9II)

 * Speaker: Marcus Noble, platform engineer at Giant Swarm
* Has worked with Kubernetes for 5-6 years in various roles: app developer, tooling builder, operator
* Sharing 10 tips for managing Kubernetes effectively
* Tip #1: Learn and love the terminal (spend a lot of time in it, customize it)
* Tip #2: Use kubectl (learn its documentation, save time with aliases)
* Tip #3: Manage multiple Kubernetes contexts with tools like kubecontext or kubeswitch
* Tip #4: Use tools like Canine for interactive debugging and logging
* Tip #5: Use OpenLens for a UI-based view of your cluster
* Tip #6: Build custom plugins using the built-in CLI plugin mechanism in kubectl (e.g., kubectl dash)
* Tip #7: Use tools like Crew for managing and installing kubectl plugins
* Tip #8: Debug pods using techniques like kshell, kubectl exec, or kubectl debug
* Tip #9: Use QPatrol for debugging issues affecting multiple workloads within a cluster
* Tip #10: Implement web hooks for advanced access control and policy enforcement
* Tools mentioned: Canine, OpenLens, Crew, kubectl dash, QPatrol, Giant Swarm's cavern policy, Kubernetes official client, Terraform provider
* No video description provided.


## How's your Supply Chain, with your insecure ingestion? | James Holland

URL: [https://www.youtube.com/watch?v=hqTBALXKWAc](https://www.youtube.com/watch?v=hqTBALXKWAc)

 * James Holland, Head of Security at City, discussing supply chain security issues and focus on secure ingestion
* Increase in supply chain attacks, especially targeting enterprise package managers
* Discussion on the use of Artifactory and other tools for bringing packages directly into pipelines
* Problem of vulnerable libraries and pre-post install scripts in Node.js packages
* Importance of signing libraries to ensure maturity and testing
* Challenges with continuously evolving packages and Intel feed systems
* Use of automation and security checks, such as SBOMs, Vex, and Kev, for detecting vulnerabilities and enforcing policies
* Role of open source software in supply chain security and tools like Fresca and Spiffy for securely managing dependencies
* Discussion on continuous secure software ingestion and the need for flexible risk management policies.


## OCI? Oh, I see! (How pulling one thread revealed a wealth of unexpected info...) | Winna Bridgewater

URL: [https://www.youtube.com/watch?v=loiFDXxfEbo](https://www.youtube.com/watch?v=loiFDXxfEbo)

 * The speaker, Winna Bridgewater, has six years of experience working with Cloud Foundry and building binaries in Golang.
* She had never worked with Kubernetes, Dockerfiles, or containers before.
* While trying to deploy an application, she discovered that it was using a container image based on the Bitnami Cube Cuddle base image.
* She wanted to understand why her application's dependency seemed to be going awry and started tracing back to find out that the base image was using curl, which she hadn't pinned.
* She didn't have much experience with Docker Hub or container images in general.
* She learned that containers allow you to create an application that runs consistently across different environments and that it's important to know what's inside each layer of a container image for peace of mind.
* She was puzzled by the Dockerfile, which she had no experience with, and felt overwhelmed by the industry practice of creating non-deterministic operations in the build process.
* She stepped back and decided to learn more about the fundamentals of containers and their history, starting with multiprogramming in the late 1970s and early 1980s.
* Containers have evolved from virtualization to a more lightweight solution for running applications in isolated environments.
* Linux container technology started with LXC and later evolved into Docker, which was introduced in 2013 and quickly gained popularity due to its ease of use and ability to make life easier for developers.
* The speaker also learned about the Open Container Initiative (OCI), a collaboration between various organizations to develop open container formats, runtime specifications, and certification programs.
* Since 2015, there has been significant growth in the container landscape, with Kubernetes becoming the main orchestrator for managing containers in production environments.
* The speaker also learned about the importance of being patient and understanding that new technologies take time to evolve and that it's important to go wide instead of getting stuck on one specific tool or technology.
* She also mentioned the importance of listening to others, learning from their experiences, and not ignoring parts of the day-to-day product delivery process.


## Paving a path: rebuilding the SDLC in record time with minimal disruption at ... | Debbie Wood

URL: [https://www.youtube.com/watch?v=n5fNzIRowv8](https://www.youtube.com/watch?v=n5fNzIRowv8)

 * Representative from Sneak, a tech unicorn, discusses rebuilding their software development lifecycle (SDLC) with minimal disruption
* The case study involves the establishment of Polaris, a new platform service API across several Kubernetes clusters in different geolocations using a consistent pattern
* Goal was to enable fast onboarding for new engineers and create a repeatable platform
* Technical challenges included deploying using an open source orb, deprecating entrenched Legacy python deployer, and communicating across teams with a ubiquitous language
* Key decisions involved setting milestones, utilizing cross-functional teams, and implementing tools like Argo CD, Circle CI, and Helm charts
* Learning from past failures and adopting a more flexible approach were also important factors in the success of Polaris.


## What does sigstore get you as a kubernetes operator? | Luke Hinds

URL: [https://www.youtube.com/watch?v=xrPzAetGhzY](https://www.youtube.com/watch?v=xrPzAetGhzY)

 * Sigstore is a relatively new project focused on software signing transparency and provenance
* Six Doors, the team behind Sigstore, started in 2020 and has since become a part of the Open Source Security Foundation
* Sigstore offers attestation within a transparency log, supporting multiple languages like Rust, Go, Python, JS, and Java
* Fulsio is a short-lived signing certificate system interface
* Transparency log acts like a blockchain, providing an immutable and tamper-resistant record of software artifacts and their interactions
* Sigstore provides tools to sign container images, generate attestations, and manage long-term private keys
* Kubernetes has adopted Sigstore for standardized signing of images using the Sinus Bomb mechanism
* Kyverno is another popular project that integrates Sigstore for admission control in Kubernetes clusters
* Sigstore can prevent typo squatting attacks by checking against expected image signatures and blocking unauthorized builds
* The transparency log ensures a reliable cryptographic guarantee of source origin, making it difficult for attackers to impersonate developers or repositories.


## How We Learned to Stop Worrying and Love Kubernetes Networking | Anna Kapuścińska

URL: [https://www.youtube.com/watch?v=rP-yWZYP2R8](https://www.youtube.com/watch?v=rP-yWZYP2R8)

 * Anna Kapuscinska from Isovalent, known for Psyllium CNI plugin in Kubernetes
* Connecting observability and networking in Kubernetes using Psyllium
* Networking 101: OSI model, TCP (Transmission Control Protocol), UDP (User Datagram Protocol)
* Kubernetes networking perceived complicated due to multiple components: CNI plugins, load balancers, core DNS, Ingress controllers
* Introducing eBPF (Extended Berkeley Packet Filter) technology and Evpf stadium for observability in Linux kernel
* Psyllium CNI plugin provides basic connectivity and additional features like Network Policy, Q proxy replacement, layer 7 load balancing
* Hubble from Isovalent is an observability layer that provides CLI for observing kubernetes networking with primitives and metrics
* Hubble collects data using evpf technology, provides visibility into network events, and exposes kubernetes Primitives for Prometheus scraping
* Psyllium and Hubble work together to provide comprehensive observability for kubernetes networking.


## Karpenter goes offline bin packing | Marko Bevc

URL: [https://www.youtube.com/watch?v=jJjVe4k0oH0](https://www.youtube.com/watch?v=jJjVe4k0oH0)

 * Marko Bevc talking about Kubernetes node scaling and Carpenter, a solution for efficient node provisioning and management
* Reason for discussing Carpenter: dealing with Auto scaling in Kubernetes, optimizing resource utilization, and reducing costs
* Overview of Kubernetes note scaling: horizontal (adding nodes) and vertical (resizing nodes)
* Challenge with Kubernetes node scaling: managing node consolidation and cross-node affinity in complex scenarios
* Carpenter's approach: manage node lifecycle, use first-fit descending algorithm for container placement, and provide constant optimization
* Key features of Carpenter: provisioning capacity, handling node expiration, and optimizing cost with intelligent decision-making.

Live demo:

1. Deploying Carpenter controller using Helm chart on a Fargate cluster
2. Creating a simple deployment and scaling it to check CPU utilization and see how Carpenter provisions new nodes accordingly
3. Scaling the deployment up and observing Carpenter's behavior in handling unscheduled ports and node availability.


## Machine Learning on Kubernetes | Salman Iqbal

URL: [https://www.youtube.com/watch?v=r7YMDBmlGh4](https://www.youtube.com/watch?v=r7YMDBmlGh4)

 * Speaker is talking about machine learning on Kubernetes
* Gives examples of guessing games and jokes related to technology
* Explains the concept of supervised and unsupervised learning in machine learning
* Mentions the challenge of managing multiple containers in Kubernetes and the benefits of using services for discovery and load balancing
* Talks about the process of building a machine learning model on Kubernetes, from data collection to serving the model
* Discusses the importance of data science and resource management in machine learning
* Mentions the use of popular machine learning frameworks like TensorFlow and PyTorch in Kubernetes
* Introduces Kubeflow as an open-source project for deploying and managing machine learning workflows on Kubernetes
* Explains how to run machine learning models on Kubernetes using operators, which can automate the deployment, scaling, and management of complex applications.
* Mentions other machine learning frameworks like Apache Spark and MXNet and their benefits in running on Kubernetes.


## Tall Oaks from Little Acorns Grow - an Open Source Journey | Dan Finneran

URL: [https://www.youtube.com/watch?v=VSqBuiZiSlU](https://www.youtube.com/watch?v=VSqBuiZiSlU)

 * Dan Finneran shares his journey in the open source world, starting with his early computer experiences and disappointment in software engineering
* He discovered open source through GitHub and contributed to a Docker project, despite not having experience with Go
* He faced challenges in understanding testing and documentation, leading to rejected pull requests
* He then created a Kubernetes script for deploying servers and named it DOT IO, eventually releasing it to the public
* The feedback was mixed, with some users finding it useful while others preferred traditional methods
* He learned the importance of community support and engagement, as well as the benefits of open source projects gaining visibility through conferences and foundations like CNCF
* He encountered challenges with enterprise companies' open source review boards and legal teams
* He shared a strange experience pitching a VC firm for funding, highlighting the importance of preparation and clear plans for monetization
* Overall, Dan emphasizes the impact of open source on software development, making it easier and more accessible to everyone.

Bullet points:
- Discovered open source through GitHub contribution to Docker project without Go experience
- Struggled with testing, documentation, and rejection of pull requests
- Created Kubernetes script named DOT IO, released to public with mixed feedback
- Learned importance of community support and engagement, increased visibility through CNCF
- Encountered challenges with enterprise open source review boards and legal teams
- Pitched VC firm for funding, learned importance of preparation and clear plans for monetization
- Emphasizes impact of open source on software development and accessibility.


## In theory, there’s no difference between practice and theory | Rory McCune

URL: [https://www.youtube.com/watch?v=v4CC1hj2c8E](https://www.youtube.com/watch?v=v4CC1hj2c8E)

 * Speaker is Rory McCune, Senior Security Advocate at Datadog
* Background: Previously worked as a developer advocate and penetration tester
* Focused on IT security, author of CIS Benchmark for Docker and Kubernetes
* Interested in cloud security trends
* Talking about differences between theory and practice in Kubernetes security

Theory:

* Quote from Albert Einstein: "In theory there is no difference between theory and practice. In practice there is."
* Speaker has encountered ideas online about the widespread adoption of Kubernetes, service meshes, multicloud, and container security best practices

Practice:

* Experienced finding vulnerabilities in Kubernetes clusters as a penetration tester
* Observed that patching and updating kubernetes nodes often get less attention than application workloads
* Noticed that some organizations still run outdated versions of containerd and Docker shim, which can pose security risks
* Saw that long tail support for older versions of Kubernetes and OpenShift can make upgrades challenging

Interesting trends:

* Cloud native technologies are being adopted quickly but not uniformly across all organizations
* Service mesh adoption is growing but still not ubiquitous, with Istio being the most popular choice (but not yet at 100% penetration)
* Kubernetes patching and upgrades can be aggressive, with new versions coming out frequently and older versions going end-of-life relatively quickly
* Some organizations are still running older versions of Kubernetes that are unsupported, which can pose security risks

Conclusion:

* In practice, it's important for organizations to keep track of their Kubernetes cluster version and underlying component versions, as outdated software can leave vulnerabilities open.
* The removal of deprecated features in Kubernetes can impact production clusters, so it's essential to plan for those changes and stay informed about them.
* Organizations need to prioritize patching and upgrading their Kubernetes infrastructure to maintain security and compatibility with new features.


## State of Open - Will Open Source Fail? | Amanda Brock

URL: [https://www.youtube.com/watch?v=Sj3rG5qDIh8](https://www.youtube.com/watch?v=Sj3rG5qDIh8)

 * Amanda Brock, CEO of Open UK, discusses the future of open source
* Started her career in open source 15 years ago at Canonical
* Left canonical due to business model shifts and joined a law firm
* Has been involved in various open source initiatives including advisory boards, government appointments, and OSI
* Written a legal textbook on open source and has spoken at events and conferences
* Discusses the importance of community building and recognition in the open source world
* Mentioned the challenges of export controls, economics, and commercialization in open source
* Talks about Open UK's mission to build a diverse and inclusive open source community in the UK
* Discusses her experience with awards and recognition in the open source community
* Mentions the importance of policy, legal, and community aspects of open source
* Expresses concern over the future of open source due to lack of understanding and potential revenue disruptions for companies
* Emphasizes the need for good governance, technical hygiene, and responsible use in open source
* Calls for a shift in considering open source as a digital public good.


## Community hacks to enhance your career | Sam Hepburn

URL: [https://www.youtube.com/watch?v=Y9emTrpdyME](https://www.youtube.com/watch?v=Y9emTrpdyME)

 * Sam Hepburn talks about enhancing careers through community involvement
* Writing bad code can help grow a personal profile
* Favorite ways to get involved in the community: Discord server (devsecops), Twitter, LinkedIn
* Public speaking: submit talks to conferences, blogs, engage with audience
* Open source projects can lead to next roles or school projects

Public speaking tips:
- Speak about challenging problems you couldn't solve
- Share solutions even if they aren't perfect
- Use humor and relatable analogies
- Prepare an abstract that is clear and has a takeaway
- Be open to feedback and ask for it

Feedback:
- Be specific and positive
- Give constructive feedback in a respectful way
- Learn from the experience and improve

Conference submissions:
- Don't be daunted by the process
- A good title can help get accepted
- Use humor and make your talk unique

Session styles:
- Different types of sessions (birds of a feather, panel discussions, workshops)
- Be prepared to answer questions from the audience

Open source contribution:
- Contribute code or help with documentation or organization
- Utilize open source projects in your work and share your experience
- Referral bonuses can be a motivation for finding new jobs


## Lessons Learnt from deploying CICD Infrastructure while leveraging K8s | Riyanat Shittu

URL: [https://www.youtube.com/watch?v=8uG89bU-aXc](https://www.youtube.com/watch?v=8uG89bU-aXc)

 * Riyanat Shittu, engineering team leader at Turntable, shares lessons learned while deploying CI/CD infrastructure for an in-house application using Kubernetes (k8s)
* Project involved migrating from manual development and deployment processes to automation with a goal to support 100 software engineers
* Initial challenges: lack of automation, security concerns, cost management
* Lesson 1: Prototyping & Automation - Automate infrastructure setup as early as possible using tools like Terraform
* Lesson 2: Secure Networking - Keep resources within private subnets and use managed services to reduce costs and improve security
* Lesson 3: Scalability - Optimize resource utilization, consider auto-scaling options, and be aware of potential limitations (e.g., IP addresses)
* Use Kubernetes for scalable deployment and load balancing
* Use Helm for simplified configuration management
* Define a consistent process for development, testing, and production environments using GitLab CI/CD pipelines
* Encourage a DevOps culture within the team
* Leverage managed services like AWS Splunk for centralized logging
* Utilize Kubernetes dashboard for developer access and onboarding.


## Wolfi OS and Building Declarative Containers | Eddie Zaneski

URL: [https://www.youtube.com/watch?v=i4vE45c0fs8](https://www.youtube.com/watch?v=i4vE45c0fs8)

 * Eddie Zaneski from Chain Guard discussing Wolfi OS and building declarative containers
* Problem with manual, tedious process of building containers using Docker files
* Introduced Julius, a tool to build containers without writing bespoke Docker files
* Discussed the size difference between Alpine-based and Debian-based images
* Introduced Wolfi OS as an alternative to traditional container images
* Wolfi OS is an undistro, which means it brings its own Linux kernel
* It uses a declarative pipeline for building containers
* Supports x86_64 and soon ARM architectures
* APK package manager used in Wolfi OS, which provides dependency resolution and signing keys
* Melange tool used to build APK-based OCI images
* Fully reproducible and fast container builds
* Small image size due to default one-group installs and caching layers
* Q&A session covered topics like running APK tools natively, building packages using APKO, and joining the Wolfi community.


## Turn me on with cloud-native feature flags! | Alex Jones

URL: [https://www.youtube.com/watch?v=hRl4x_dnhJ4](https://www.youtube.com/watch?v=hRl4x_dnhJ4)

 * Alex Jones, engineering director at Canonical, talks about feature flagging in cloud-native environments
* Feature flagging is used for delivering new functionality safely and efficiently
* Different types of evaluation contexts can be used, such as IP address, user agent, API call, or decapsulating TCP packets
* Cloud-native design principles require a discreet and interoperable feature flagging solution
* OpenFeature is a new CNCF project that aims to unify feature flag APIs for developers
* Flag D is an example of a lightweight, modular way to evaluate feature flags at the system level
* Feature flagging can be used in various environments, including web applications, Linux distributions, and embedded devices
* OpenFeature Operator is a Kubernetes operator that injects feature flags into existing workloads
* Watchman is an admission controller that uses feature flags for access control and real-time updates.


## Three Surprising K8s Networking "Features" and How to Defend Against Them | James Cleverley-Prance

URL: [https://www.youtube.com/watch?v=T7RdogXfs-8](https://www.youtube.com/watch?v=T7RdogXfs-8)

 * James Cleverley-Prance, Cloud native pen tester, discusses Kubernetes networking security and potential vulnerabilities
* Unauthenticated access to the cluster's control plane:
  + Commonly used ports (10, 22, 50, 10256) for CNI components and APIs
  + Unsecured API server can reveal information through HTTP certificates and subject alternative names
* TCP port scanning and DNS queries to discover information about the cluster:
  + DNS service often used to list services and pods within a Kubernetes cluster
  + DNS querying may be possible even without authentication
* IP forwarding and routing vulnerabilities:
  + IP packet forwarding can allow an attacker to make use of unintended consequences, like the Kubernetes router
  + Layer 2 networks may be used in architecture to encapsulate packets, allowing an attacker to manipulate the source IP address
* Defending against these vulnerabilities:
  + Implement Bastion hosts and secure network access to control planes
  + Use DNS query logging and Network Policy to prevent unauthorized queries
  + Ensure proper configuration of iptables, CNI, and other components
  + Regularly update software versions and patches
* Other security considerations:
  + Kubernetes is primarily built on Linux nodes, which may have IP forwarding enabled using tools like cube-ctl
  + Use managed provider offerings for better control plane security
  + Be cautious when using overlay networks like Calico or Canal in multi-subnet architectures.


## Fantastic API Gateways and where to find them | Giorgia Fiscaletti

URL: [https://www.youtube.com/watch?v=eVC83h_BOPY](https://www.youtube.com/watch?v=eVC83h_BOPY)

 * Giorgia Fiscaletti, Italian computer engineer and cloud engineer at Mia Platform
* API Gateway: entry point for managing inwards and outwards traffic in microservice architecture
* Features: request routing, performance optimization, availability, scalability, security
* Researching for a new tool to use for a project one year ago
* Overwhelmed by the number of options (CNCF landscape page)
* Narrowed down selection to service proxy API gateways (Proxy, Nginx, Emissary, Kong, Tyk)
* Decided to focus on Envoy due to its high performance, extensibility, and freedom in implementation
* Essential features: URL mapping, rewriting, rate limiting, authorization, API key management
* Benefits of Envoy: simplification, automatic service discovery, stateless architecture, custom resource definition, Lua scripting
* Implementation example: URL matching, rewriting, and rate limiting using Envoy configuration.


## ESO: Manage Secrets Cloud Natively | Ben Gurney & Emin Alemdar

URL: [https://www.youtube.com/watch?v=TEV13ELPhI8](https://www.youtube.com/watch?v=TEV13ELPhI8)

 * Emina Lamdar and Ben Gurney discussing the challenges of managing secrets in cloud-native environments using External Secrets Operator (ESO) in Kubernetes
* Discussed the importance of securely managing secrets due to increasing attack surface and complexity
* Traditional methods for secret management like in-app configuration and sidecar containers have their own limitations, especially in distributed systems with microservices
* Introduced External Secrets Operator as a solution for managing external secrets within Kubernetes
* ESO sits inside the kubernetes cluster and acts as an operator extension to take external secrets from various providers
* Provided an overview of the controller pattern used by ESO, which involves reconciliation loops and custom resource definitions
* Highlighted the benefits of using a centralized management control plane like ESO for managing secrets easily within Kubernetes
* Demonstrated how to use External Secrets Operator with different secret management providers, such as Hashicorp Vault and AWS Secrets Manager
* Discussed the community collaboration around ESO being part of CNCF Sandbox project.


## ArgoCD and a Helmfile Operator walk into a bar: a guide to declarative bootstrapping | Steve Judd

URL: [https://www.youtube.com/watch?v=HmseOS6k2yg](https://www.youtube.com/watch?v=HmseOS6k2yg)

 * Steve Judd from JetStack's Consulting and Training Division shares his experience of managing Kubernetes clusters and installing preferred add-ons like Cert-Manager, Nginx Ingress, and Argo CD.
* He mentions the challenges in manually deploying add-ons using scripts or Terraform and introduces Argo CD as an alternative.
* Argo CD is a continuous delivery tool for Kubernetes that monitors Git repos for application code changes and ensures the desired state of the cluster by applying those changes.
* Argo CD uses Application Custom Resource Definitions (CRDs) to manage applications, which can store raw Kubernetes manifests or Helm charts with custom templates.
* The demo shows how to install and use Argo CD to deploy a simple Hello World application from a Git repo, using a sync policy for automatic updates.
* Argo CD applies both standard Kubernetes resources and Application CRDs, making it an essential tool in managing complex applications.
* To bootstrap an Argo CD cluster, one must install the Argo CD application CRD first, then use Helm file to manage the installation order of other components like Cert-Manager, Prometheus, etc.
* The presentation discusses using Helmfile operator and External Secrets operator for managing GitHub tokens and secrets, respectively.
* The demo concludes with an overview of how Argo CD manages child applications as part of a single application and the benefits of using it to automate getting a vanilla cluster ready.


## Policy as [versioned] code | Chris Nesbitt-Smith

URL: [https://www.youtube.com/watch?v=yL62l-XE268](https://www.youtube.com/watch?v=yL62l-XE268)

 * Chris Nesbitt-Smith gives a presentation on "Policy as [versioned] code"
* He uses an imaginary scenario of being in an elevator with important people and trying to sell them on the idea of policy as code
* Policy as code makes it easier to communicate, enforce, and manage policies across an organization
* Policies can be versioned, updated seamlessly, and made consumable for different teams
* Policies can be treated like dependencies and checked locally using tools
* Visibility into policy changes is important to prevent workarounds and maintain compliance
* Policy code can find and address issues in source control, such as missing release notes or incorrect spelling mistakes
* Automatic pull requests and testing can help ensure policy compliance and reduce feedback loops
* Multiple versions of policies can be evaluated within a single runtime environment using tools like Kubernetes
* Agile teams can benefit from clear policy guidelines and the ability to reasoned debate exemptions
* Policy design should prioritize proportional mitigation and avoid unnecessary friction or complexity.


## How MicroVMs can take your Kubernetes home lab to the next lvl | Claudia Beresford & Josh Michielsen

URL: [https://www.youtube.com/watch?v=8GjFLRpyilw](https://www.youtube.com/watch?v=8GjFLRpyilw)

 * Josh Mickelson and Claudia from WeWorks introduce themselves and the topic of microVMs in Kubernetes home labs
* MicroVMs are lightweight virtual machines designed for running cloud-native workloads with reduced device emulation support and process isolation
* Weaveworks has built an open-source tool called Weave Kubernetes MicroVM (WKMVM) using Flintlock, Cap NVM, and Firecracker
* WKMVM includes a cost API provider for managing micro VMs on physical nodes and handle placement across given set of nodes
* MicroVMs provide fast startup times, scalability, and reduced attack surface compared to regular virtual machines
* Demonstration using Dell XPS running Ubuntu 22.04, Raspberry Pi model 4bs, Flintlock D containerdy, and Firecracker
* Goals are to create a Kubernetes node with minimum 4GB memory and use microVMs to provide better isolation and control compared to containers
* Challenges include managing network setup, power supply, and image registry access for the Raspberry Pi nodes
* MicroVMs can be used in edge computing, CI self-hosted runners, and home labs with limited resources.
* WKMVM creates a Mac vtap interface for internet access, maps VLAN interfaces, and creates microVMs using Firecracker and Flintlock D service.
* MicroVMs need internet access to download required binaries and operating systems, and use VLAN interfaces to communicate with other nodes in the cluster.
* WKMVM can create forwarding rules for traffic between microVMs and physical machines, and provides a simple way to scale the number of nodes in the cluster.


## Machine Learning Deployments on Kubernetes | Ed Shee

URL: [https://www.youtube.com/watch?v=eaYLlD16gFg](https://www.youtube.com/watch?v=eaYLlD16gFg)

 * The speaker discusses the challenges data scientists face in deploying machine learning models
* Traditional approach: data scientists build and train models using frameworks like TensorFlow, PyTorch, etc. and save model files, which can be versioned and stored in registries
* Challenges in deployment include scaling different types of models for various use cases, ensuring a good developer experience, and managing infrastructure for large models
* Data scientists often work separately from devops and deployment engineering teams
* Kubernetes is popular in the machine learning world due to its ability to quickly adopt devops best practices
* Seldon Core is an open-source framework used to deploy and manage machine learning models on Kubernetes
* Seldon Core creates containerized microservices with a standardized interface, allowing for scalable and independent deployment of preprocessors, models, and post-processors
* The speaker shows how to create and deploy a Selden Core model using YAML files and provides an example of deploying an XGBoost model using Canary releases.


## One YAML to rule them all | Tom Harris

URL: [https://www.youtube.com/watch?v=eCVThJusQ1c](https://www.youtube.com/watch?v=eCVThJusQ1c)

 * Tom Harris talks about Humana Tech and an open source project called Score
* Score is designed for single source truth workload management, enabling workload run across various orchestration platforms (e.g., Docker Compose, Kubernetes, Helm)
* Developer cognitive load is a problem with context switching between different tools and workflows
* Infrastructure management is another challenge for developers
* Score advocates for workload-centric development instead of infrastructure-centric development
* Workload-centric development focuses on the developer's job rather than worrying about the complexity of container orchestration systems
* Score consists of three main components: specification, implementation, and CLI tool
* Score specifications are platform-agnostic and define everything needed to run a workload (dependencies, variables, application code)
* Implementation translates score specifications into platform-specific configuration files (e.g., Docker Compose, Helm)
* The demo shows running `score compose` and `score helm` to translate Score specifications into Docker Compose and Helm files respectively
* The goal is to make it easier for developers to manage workloads across different platforms with a single source of truth.


## Bugs in Collaboration: Cloud Native Edition | Russ Miles

URL: [https://www.youtube.com/watch?v=CSkqf-C0psE](https://www.youtube.com/watch?v=CSkqf-C0psE)

 * The speaker, Russ Miles, shares his experience of dealing with a challenging moment in his career where he was diagnosed with cancer while working as an engineering manager at a bank.
* He discusses the importance of developing skills such as resilience, empathy, and collaboration during intense moments in life and work.
* He also talks about how learning to listen and connect with people, especially in difficult situations, can be a valuable skill.
* He mentions that humor can help cope with challenging situations and that he learned the importance of emotional intelligence and compassion through his experiences.
* He encourages volunteering and helping others as a way to learn empathy and listening skills.
* He emphasizes the importance of psychological safety in a team environment, where everyone feels safe to bring their whole selves to work.
* He also mentions that technology, such as Kubernetes, can fail even in a cloud-native environment and the importance of teamwork and collaboration during those moments.
* He encourages learning new skills and being an incredible collaborator and teammate, as you never know when you might need to rely on others during difficult moments in life or work.


## Retro of KCD UK 2022

URL: [https://www.youtube.com/watch?v=jnJ_bTETDqc](https://www.youtube.com/watch?v=jnJ_bTETDqc)

 * The Point Session at KCD UK 2022 was a meeting for attendees to discuss improvements for next year's event.
* Goals were to make the session public, increase open participation, and use a survey for feedback.
* Topics discussed included improving communication, continuous improvement, venue suggestions, food options, and workshop organization.
* Feedback from previous years included issues with catering quality and quantity, dietary requirements, and scheduling.
* The organizers want to find a more affordable and accessible venue outside London.
* Attendees suggested having fewer simultaneous workshops, prioritizing content quality, and providing a clearer schedule.
* Some attendees felt that the pacing was good overall but that there wasn't enough time between talks.
* There were suggestions to provide clearer theme guidance for CFPs and possibly add lightning talk sessions to the schedule.
* The organizers are open to ideas for making the event more engaging, such as enabling heckling or adding different formats for talks.
* Some attendees suggested recording and publishing lightning talks afterwards.
* Overall, attendees expressed gratitude for the hard work of the organizing team and appreciated the opportunity for feedback.



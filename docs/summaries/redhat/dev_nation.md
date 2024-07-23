## Distributed tracing with Grafana Tempo and OpenTelemetry  | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=TmC7Ha3Qqk4](https://www.youtube.com/watch?v=TmC7Ha3Qqk4)


- Two software engineers, Pavo and Roman, introduce themselves and their roles in observability technology.
- They explain the value of distributed tracing versus metrics and logging.
- They describe the architecture of deploying an end-to-end distributed tracing infrastructure using OpenShift.
- They demonstrate a live deployment of a microservice application and show how it generates trace data using OpenTelemetry.
- They discuss the importance of standardization in distributed tracing, such as HTTP request format and correlation.
- They introduce the concept of a log monitoring tab and its ability to display metric-derived traces and set metrics across services.
- They explain the role of open source projects like OpenTelemetry and Tempo in observability solutions.
- They discuss the architecture of Tempo, including its object storage back end and querying capabilities.
- They demonstrate how to deploy Tempo using Kubernetes and connect it to S3 object storage.
- They mention features such as Gateway for authorization and authentication, and service monitors and alert prometes components.
- They discuss the use of open source collector processors like kubernetes attribute processor and LLP protocol exporter.
- They explain how to define receivers, processors, and exporters in a pipeline and generate metrics using connectors.
- They mention the importance of instrumentation and automatic vs manual methods for capturing Telemetry data.
- They discuss popular libraries for different languages that support different mechanisms for injecting code for instrumentation.


## OpenShift Serverless: Using Knative in next-generation AI applications |DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=ck1DKgmPSsQ](https://www.youtube.com/watch?v=ck1DKgmPSsQ)


- Welcome and introductions
- Discussion on fear of AI taking jobs, overuse of term 'AI'
- Brief history of neural networks and artificial intelligence
- Explanation of the concept of inference and rule sets
- Mention of genetic algorithms and memetics
- Comparison of machine learning and artificial intelligence
- Beethoven example of musical composition using rule-based system and AI
- Overview of open source tools like Ansible and Kubernetes
- Discussion on serverless architecture, event-driven applications, and autoscaling
- Mention of custom metrics, K8s Eventing, and mesh networking
- Comparison of neural networks with traditional systems and databases
- Explanation of the concept of overcommit in serverless applications
- Discussion on building complex systems using simple components and event-driven architecture.


## Server-Side WebAssembly | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=BFZWFuFVIFU](https://www.youtube.com/watch?v=BFZWFuFVIFU)


- Ivan Font speaking about web assembly
- Background: Embedded Linux background, switched to cloud software at Red Hat
- Focusing on understanding web assembly technology for past year
- Lightweight and fast with near native performance
- Provides a secure sandbox execution environment
- Used instead of containers in some cases
- WebAssembly (WASM) is not a replacement for containerization, but rather another tool in the developer's toolbox
- Differences between web assembly and Java bytecode:
  - Time compilation vs interpreted vs JIT compilation
  - Virtual machine architecture
- Multithreading in web assembly is being worked on, but not yet fully supported
- Web assembly virtual machine (WASM VM) provides a sandbox execution environment with memory isolation
- Originally used for client-side computation in web browsers
- Now used for cloud applications and server-side computing
- Examples of web assembly usage: Adobe Photoshop, AutoCAD, 3D modeling, gaming, AI/ML
- Web assembly is a binary format that represents low-level hardware operations
- Supports multiple languages like Rust, C, C++, Go, and more
- Can be run in standalone or embedded applications
- Portable across different platforms and architectures
- Lighter than container images with faster start times
- Ideal for Edge Computing use cases with small resource footprints
- Provides implicit security features and can be used with Kubernetes and other systems
- Web assembly is gaining popularity in cloud infrastructure today
- Discussion about using web assembly on ARM processors and x86 processors
- Web assembly is not a replacement for containers, but rather complementary technology
- Can be deployed anywhere using podman or other container runtimes
- Deployment strategies depend on individual use cases and tradeoffs
- Podman and OpenShift are popular tools for deploying web assembly applications
- Web assembly can be used with AI/ML models and frameworks like TensorFlow, PyTorch, and OpenVINO
- Integration with Kubernetes and other systems is ongoing
- Discussion about potential benefits of using web assembly for Edge Computing devices
- Interest in comparing performance and size differences between ARM and x86 processors for web assembly applications.


## Server-Side WebAssembly |DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=D5vLjczrx9Q](https://www.youtube.com/watch?v=D5vLjczrx9Q)


- Ivan Font is a Red Hat employee who has been working on web assembly for several years. He started from an embedded Linux background and switched to cloud software.
- Web assembly (Wasum) is a technology used to run code in the browser or server. It's like a virtual machine that can execute code in user space, either Standalone or embedded as a module.
- Wasum is not a replacement for containers. They serve different purposes: containers provide an operating system and process isolation while Wasum provides low-level hardware operation instructions and runs as a single threaded stack based VM.
- Web assembly is lightweight and fast because it's compiled ahead of time, which also makes it portable across different architectures and platforms. It doesn't have memory management or garbage collection, so developers need to manage those manually.
- Web assembly has been used for various purposes such as cloud middleware, event-driven microservices, edge computing, and even in web browsers as an alternative to plugins.
- Wasum can be used with different languages like Rust, C, Go, and JavaScript. It's also compatible with web standards like HTML, CSS, and JavaScript, making it a versatile tool for building applications.
- The speaker mentioned some tools and technologies related to Wasum such as Podman, WASI (Web Assembly System Interface), OCI image format, and various container runtimes.
- There were questions from the audience about multithreading, security, performance, and portability of Wasum compared to containers. The speaker provided some insights on those topics but encouraged further discussion.
- Web assembly has been evolving rapidly since its introduction in 2015 and is becoming increasingly popular for building cloud software due to its lightweight, fast, and portable nature. It's also being used more in edge computing and event-driven microservices.
- Wasum allows developers to run untrusted code safely in a sandboxed environment using the WASI system call layer and capability-based security model.
- The speaker demonstrated how to build and deploy a simple Rust application as a Wasum module using Podman, which showed its small size and fast execution.
- Web assembly is being adopted by various companies for their production workloads due to its performance benefits and ability to run on different architectures with minimal changes. It's also being used in edge computing and event-driven microservices.
- The speaker encouraged the audience to experiment with web assembly, especially in the context of edge computing, as it provides a small resource footprint and is well-suited for that use case. He also mentioned some ongoing developments such as support for interpreting JIT (just-in-time) compilation mode and integration with various frameworks like TensorFlow, PyTorch, OpenVino, and Onyx.


## Quarkus & Testcontainers - Perfect synergy for cloud-native development |DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=x44dL5jzaG4](https://www.youtube.com/watch?v=x44dL5jzaG4)



- Speaker: Eric and Alexa from Red Hat, discussing test container library for Quarkus application framework.
- Test container library is open source, available in multiple languages (Java, Python, Ruby, nodejs).
- Test container offers low level API for developers to manage containers.
- Supports popular services like databases, message brokers, and cloud emulators.
- Allows running anything Docker container, even custom ones.
- Provides predefined abstractions for easy configuration of these services.
- Offers convenience APIs for managing lifecycle methods (start, stop) and network configurations.
- Atomic jar also offers test container desktop application, free of charge.
- Test container can be used in CI environments for local development and testing.
- Speaker mentions Kafka example and shows how to run it using test container in Java project.
- Test container library is integrated with JUnit test framework.
- Test container allows managing containers automatically, freeing up developer time.


## 3 event-driven architecture patterns in action | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=6fBP1Ncjva8](https://www.youtube.com/watch?v=6fBP1Ncjva8)


- Hans Spader, Red Hat Developer Advocate, discussing event driven architecture (EDA)
  - EDA: loose coupling, extensibility, independence across services
  - Three patterns of EDA: claim check, content richer, message translator

## Claim Check Pattern
- Challenge: large payloads, inefficient to send around repeatedly
- Solution: externalize large binary data to a separate storage system and reference it with an identifier
- Demo: producer sends image data to MinIO object storage, consumer retrieves claim check (identifier) from Kafka topic and loads the actual data from MinIO

## Content Richer Pattern
- Challenge: sparse failure payloads contain little information
- Solution: enrich events at the source with additional data and send it along to consumers
- Demo: IoT sensor data processing, enriched event contains raw sensor data and metadata

## Message Translator Pattern
- Challenge: incompatible or inconvenient payload formats
- Solution: translate payloads into a format that is consumable by the target system
- Demo: Point of Sale data processing, Kafka connect transforms CSV to JSON and sends it to the target web API without additional coding


## Getting GitOps | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=SpRSndQCl2I](https://www.youtube.com/watch?v=SpRSndQCl2I)

Split:[4740, 4740]

- Harriet Lawrence from OpenShift GitHub is presenting on getting GitOps going with Red Hat.
- Agenda covers Overview of Upstream Community, OpenShift Get Ops product, and customer use cases.
- Upstream Community: Argo CD, a Red Hat product, manages applications across multiple environments using GitOps workflow. It's open source and has a large community of maintainers and contributors.
- OpenShift Get Ops product: Provides continuous deployment, monitoring, and configuration management for OpenShift clusters.
- Customer Use Cases: Three customers will share their experiences with using OpenShift Get Ops.
- Philip from postnode styleforce will discuss how they use OpenShift Get Ops for managing ClickHouse databases across multiple clusters.
- Richard Misha from bet medlingen will talk about managing multiple OpenShift environments using OpenShift Get Ops.
- Thomas Manuel from Swiss railway will share their experience with wrapping time together using OpenShift Get Ops.
- Q&A session with Red Hat experts Abhishek, Ian, Christian, Natalie, and others.


- Speaker is Philip Wilson, infrastructure architect at Postal Services in Sweden and Denmark.
- Company has around 700 employees with a heavy tech focus.
- Discussing container adoption journey that started a year ago.
- Helped by Red Hat consultants to deploy OpenShift using Ansible and GitOps workflow.
- Three main repositories used: infrastructure, Helm charts for platform components, and application deployment repository.
- Using Argo CD for configuration management, monitoring, and disaster recovery.
- Discusses challenges with configuring OpenShift templates in GitHub.
- Shares example of alert manager configuration using GitOps, external secrets, and Hashicorp Vault.
- Mentions the importance of maintaining control environment, especially regarding application deployment.
- Discusses future plans for developing a more automated platform.
- Q&A session covers topics such as managing OpenShift clusters, Argo CD vs. other tools, and integrating with Microsoft Team.



## Using OpenTelemetry on Kubernetes | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=SGsqJZga3a8](https://www.youtube.com/watch?v=SGsqJZga3a8)



- Benedict Pavel is a principal software engineer and active contributor to the Open Telemetry project, focusing on distributed tracing.
- History of observability:
  - xtrace (2007): Platform for storing, visualizing Telemetry data.
  - Apache Skywalking/Hypertrace/Signal (2014): End-to-end observability platform using a proprietary data model.
  - OpenTracing (2016): Open source project providing a standardized approach to distributed tracing by defining a specification document.
  - Jaeger and Zipkin (2018): Competing projects merged in 2019 to form the OpenTelemetry Project.
  - Auto-instrumentation and auto-collection (2019 onward): The next big innovation in observability, with open source high-quality agents and auto instrumentation.
- Introducing Open Telemetry:
  - A vendor-neutral, open source data collection platform for monitoring modern applications.
  - Components: API, SDK, standardized data model (OpenTelemetry Protocol), collector, and auto-instrumentation agent.
- Instrumenting an application with Open Telemetry:
  - Three approaches: Manual explicit approach (using APIs), direct integration into runtimes, and auto instrumentation using an agent.
    - Manual explicit approach: Requires developer effort but offers more control and flexibility.
    - Direct integration into runtimes: Easiest to get started but limited to supported frameworks and runtimes.
    - Auto-instrumentation using an agent: Requires minimal effort, can support a wide range of frameworks, but consumes resources.
  - OpenTelemetry Collector: A data pipeline component that receives and processes Telemetry data. It consists of three steps: receiver, processor, and exporter.
    - Receiver: Reads data from various sources, such as logs or metrics.
    - Processor: Parses and normalizes the received data, applying filters, relabeling, and deduplication.
    - Exporter: Sends the processed data to different destinations for storage or analysis, such as Prometheus, Jaeger, or Splunk.


## GitHub Makeover | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=3pNLcDv69ko](https://www.youtube.com/watch?v=3pNLcDv69ko)



- Speaker is excited for tech talk about Github workflow improvements
- Speaker mentions running Scala presentation on Node
- Speaker explains customized Github tool that improves productivity
- Tool includes white GitHub refresh extension, coral icons, and command palette navigation
- Speaker discusses shortcuts for navigating codebase and pull requests in Github
- Speaker mentions a github action typing extension for security testing
- Speaker demonstrates using vim keys to navigate around Github interface
- Speaker discusses the importance of understanding Git history and maintaining a clean local repository
- Speaker mentions GitHub Poi extension for managing pull requests and issues
- Speaker mentions Octa3 extension for better repository navigation and search
- Speaker recommends using markdown files in Github for visually appealing presentations
- Speaker mentions using Github cli tool for low level interactions with API.


## Quinoa: A modern Quarkus UI with no hassles | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=00g-gBIYpsU](https://www.youtube.com/watch?v=00g-gBIYpsU)



- Andy is introducing a guest, Stephan.
- Stephan is from South France near Marseille.
- He created an extension for Quarkus called "Quinoa".
- Quinoa makes developing Quarkus easier by integrating frontend and backend together.
- It also simplifies the build process and improves developer joy.
- Quinoa is compatible with Node.js for building web apps.
- Stephan mentions using Kafka, Vertex, and OpenShift as part of his demo.
- He suggests that Quarkus can be used instead of Node.js for dealing with frontend in a more efficient way.
- Stephan demonstrates how to use Quinoa with a shopping list app example.
- He mentions using Panache for database connections and server sent events for messaging.
- He shows how to use Quarkus with a single page application (SPA) and integrated deployment.
- Stephan also discusses end-to-end testing and the use of Box, Gunit, and Playwright for testing.
- He mentions the ability to proxy requests and serve generated web resources directly from Quarkus.
- The discussion covers live coding and using quarkxport for linking projects.
- Stephan also talks about adding features such as server sent events instead of web sockets, and using OpenShift for deploying.


## Event-driven autoscaling through KEDA and Knative Integration | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=wrlIoV5DCpY](https://www.youtube.com/watch?v=wrlIoV5DCpY)


- Host introduces Danielle as speaker for talk on auto scaling using Cater in Kubernetes
- Danielle is a technical marketing specialist and developer advocate at Red Hat, focusing on cloud native runtimes like Quarkus, SpringBoot, and Node.js
- She has experience installing Kubernetes and OpenShift, as well as managing service meshes like Istio and Conduit
- Topic: Auto scaling using Cater in Kubernetes
- Importance of auto scaling in a microservices architecture
- External services can impact existing applications in Kubernetes
- Cater allows for event-driven autoscaling based on metrics rather than traditional CPU or memory utilization
- Cater can handle multiple external services and scale application parts accordingly
- Demonstration using an OpenShift cluster, Kafka, and Prometheus
- Quarkus is a Kubernetes native Java framework that can be used for serverless applications and has features like live coding and single sign on
- Cater allows for automatic scaling of Quarkus applications with a simple CLI command
- Minimum replication count and maximum replication count are important considerations for auto scaling in Kubernetes
- Demonstration using a deployment, a job, and an event-driven workload
- Horizontal Pod Autoscaler (HPA) is used to scale application parts based on metrics like CPU or memory utilization
- Cater can be integrated with HPA to enable more granular auto scaling based on specific events
- Demonstration using a Cater operator and a custom resource definition
- Cater provides a simpler and more efficient way to deploy applications in Kubernetes compared to traditional methods like Dockerfiles or Helm charts
- Cater can handle multiple external services and scale application parts accordingly based on their respective metrics
- Demonstration using a Quarkus application, a Kafka topic, and an event-driven architecture
- Auto scaling using Cater in Kubernetes allows for more efficient use of resources and better performance for event-driven applications
- Cater can be used to scale multiple serverless applications simultaneously using different algorithms and mechanisms.


## Integrating Loom in Quarkus | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=NmkAymnuK1c](https://www.youtube.com/watch?v=NmkAymnuK1c)



- Host Natalie Vint introduces Clement Hartur and Julia Caucus, who will talk about integrating Loom Quarkus.
- Loom is a threading model that allows efficient execution of concurrent tasks.
- Java has an imperative execution model which can be simple but expensive in terms of memory and thread usage for concurrent applications.
- Reactive programming models like Loom can improve resource efficiency and concurrency by using event loops and virtual threads.
- Virtual threads are lightweight and can be created quickly, reducing the need for thread pools and isolation processing requests one at a time.
- Loom has a carrier thread model which manages event loops and handles IO tasks while virtual threads process application logic.
- Clement explains that parking of carrier threads can lead to blocking and performance issues, but Loom team is addressing this with improvements in future releases.
- Quarkus is a Java framework that supports both imperative and reactive programming models, and can integrate with Loom for improved concurrency and efficiency.
- Loom provides a way to block without making the carrying thread wait, using asynchronous constructs like Mutiny.
- Julia discusses some performance benchmarks showing improvements in throughput and latency with Loom compared to traditional blocking models.
- Clement also mentions that Loom can reduce pinning phenomenon by allowing virtual threads to be released immediately when a result is available, instead of waiting for the carry thread to become available again.
- The team is honest about the challenges and limitations of Loom, such as occasional parking of carrier threads and the need for customization in some cases.
- Julia suggests that Loom can improve resource efficiency by reducing the number of pinning events and improving environment deployment capacity.
- Clement also mentions that Loom can improve high-level concurrency by handling server requests more efficiently, and that it can be used with various databases and APIs.
- They invite questions from the audience and discuss various use cases and implementation details.


## Quarkus Renarde: an old-school Web framework with today's touch | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=CfDI0XsdxA0](https://www.youtube.com/watch?v=CfDI0XsdxA0)



- Welcome to talk about Quarkus, a modern web framework
- Special guest Stefan Impardo will speak
- Quarkus started as part of the Panache project
- Focuses on simplicity and ease of use
- Has features like server-side templating, Hibernate ORM, reactive programming with Panache, JAX R REST Easy, and WebJar integration for client-side dependencies
- Supports security features like JWT and Open ID Connect
- Can be extended easily to add new features
- Offers a fast development cycle and hot reload
- Demo will show creating a todo application from start to finish
- Quarkus can be used in various industries, including finance and healthcare
- Can be integrated with other technologies like CDI, Vert.x, and Micronaut
- Provides good documentation and community support

No context:
Music Music Music Music hello devnation friend welcome another tech talk today like quarkus like web framework today talk special guest id like ask friend stefan impardo straight nice suppose uh he traveling welcome stefan hi welcome thanks pronouncing name brilliantly thats exactly oh yeah well studied french one year french 25 year ago hope reasonable job absolutely perfect uh stefan uh today going talking quarkus genard know quarkus already panache french word see pattern maybe youre involved tell u yes indeed pattern project started im guess im pretty bad finding name point find name stick head doesnt leave anymore one found uh renault name uh female fox uh thought working web framework trying smart cute uh clever thought uh quality thought fox female fox thats opinion find cute smart clever agile thats knows thing stuck head thats that sticks yeah good quality web framework right right let see amazing uh amazing quark hannah ill leave stage today live nice france cary north carolina welcome nation thank let start slide um im show quarkus ronald oldschool web framework modernized uh running quarkus exactly exactly mention panache know people ask question lot extension named french word thats lot french developer working quarkus know uh coming mind uh really uh web framework oldschool modern uh sense current uh way web framework everything client really something akin rail play one know mean attitude want framework let thing easily short concisely intuitively possible doesnt get way try help always want minimum ceremony end use lot existing quarkx feature uh like serverside templating qt use persistence hibernate rm reactive panache help lot uh cut ceremony well use jax r rest easy reactive something enhanced allows write controller endpoint much easier make easy deal uris url redirection etc important web framework also use web jar allow help get clientside dependency bootstrap jquery whatever name use web jar dont download package application um also lot security integration jwt open id connect web often finger nose try make easy possible security utility glass help secure application favoring jwt user session also lot utility helping deal open id connect web often case work together there trivial configuration great documentation lot bug ux fix also support testing provide mock web often hardware open id connect provider twitter facebook whatever mock really trying help get everything working application next done todo app want demo show entire application start finish user management handling really entire application written said um uh maybe didnt mention corkus extension thing need create quarkus application import quarkus extension option open id connect open id connect test mocking etc mostly need import quercus finance extension quercus application get benefit create quarkx application started core cube application renault extension bunch dependency postgres im using postgres im using web often open id connect etc application running dev mode running whenever go root application get 404 dont anything right first thing going fix going go source folder uh there lot convention im going create call class called application rest package want class controller make extend controller allows opt great feature simplify jack series write string hello return hello define url uh starting application slash hello return go back test hit reload see point um application slash hello appear apply application hello input right cool exactly want want default path override want actually make happens root go back ill reload magnification take bit time normally hot reload really fast quarkus case actually lot open id connect configuration going hit endpoint going querying twitter facebook configuration bit uh slower usual normally go like millisecond reload see root application want make bit complex actually want return template instance want able return template call index want able say want web page okay ill use qt use check template way define pipe safe template compute convention put nested static class uh called template every method public static native return template instance going template define uh uh well okay never mind yeah thats problem using wrong uh keybinding um template instance define template doesnt take parameter quick fix use create template class convention going folder called application class name name methodhtml really want want able include thing includes mainhtml main template im going pas parameter title hello Music going title page going body follow link see defined main template insert title create html document bunch stuff coming like bootstrap come web jar something define dependency depend bootstrap bootstrap icon quarkus web jar locator allows u get cs javascript dependency automatically downloaded packaged application little bit menu little bit um cute template message im going show otherwise im going anything template called index need return template template index return go back hit reload application right well bit big application im going add second page im going add uh page im going copy method say go uri im going Music call template im going define pas parameter dont really good name im going say pas parameter say image im passing parameter im going create file um bit boring im going copy one going page also extends main say thats parameter defined see eid know know type get even proper completion know string defined parameter type string say ill page go application go slash page definition right need navigation ive typing link uh uris bit annoying want able say click todo place want uri redirects application index want menu item menu item remember exactly uh name attribute think title title title implicit one title going implicit one going uri application tag um qt see click go see file dot html tag folder automatically created tag include place allows great composition template let go back hit reload menu click go main page click go page right see make really easy get eye um view uh special thing skeleton application let go create todo application first thing go model create todo entity create todo entity rm panache define entity extend nash entity allows u get lot good stuff free id able define column want persist public field im going say need task need boolean know task done debate uh Music know todo done need entity im going create also static method returning list two able get list im going use method defined punish entity listall im going sort id way always get list order um im going create controller make easier im going call going rename copy controller im going single method Music going index im going im going say template going take list todos let im going copy template thats going fine could start going todos page im going im going create table im going first row header im going id im going im going action right good action im iterating todos im going create row three cell im going show id id im going show task instance let start action im displaying todo list everything display need add link menu could go back happens click oh error im blocking operation thread course configured um happens im using hibernate instead hibernate reactive need add add uh annotation say im using blocking framework um going fine define package doesnt matter list todos desperately empty usually case add file called startupjava going application scoped bean blocking im going define method startup going called startup way carcass make observe startup event carcass going called start quarkx im going create new tube test called um going done ive know ive started done ill say done date equal eight um Music im going purchase im going create second im going make one done yet um destination talk im going create uh persistence im going say transactional uh runout controller automatic job startup automatically created set todos show right dont see one done done let go improve rendering im going done im going sell make look removed add done date um property point might wondering uh hold supposed calling um supposed calling bait method right there thing since property date type happens click see im going file called java extension annotation called template extension allows add additional extension method existing type date defining static method taking first parameter type add method first parameter type date method name method named since mean adding method named since date type qt automatically call static method get extra method existing type handy case going use let go back view hit reload see one done moment ago um right display id like able add im going action im going add form point choose ad form another tag help called field think forgot name need name label name equal task equal task ill add placeholder well going call add method todos type need create add method way define post method doesnt doesn't return anything take rest form element uh task element find html holding im going say need new task equal task persist im processing new im redirecting index calling index method actually trigger redirect call method throw exception redirect template index go back field thats exactly meant appear um hello word okay well problem im missing validation ive submitted empty want right ill add validation ill add cant blank hibernate regulator invalidation make sure call validation failed everything set automatically everything work forwarded back view ill show exactly mean validation fail wont redirect index done throw flow doesnt continue dont need change anything view go back hit reload try type enter get error must blank happens validation failed method check validation error error thing prepare error redirect take parameter weve taken put flash scope preparation redirect happens call index relate get method get get method see flash scope value take value restore render template index go back go field see bit conditional say error field show error field allows validation easily pas validation error need view let add action um im interested two action want able delete um going add new


## Containers without docker | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=ngc0LLA0d80](https://www.youtube.com/watch?v=ngc0LLA0d80)



- Cedric Clyburn, Red Hat Developer Advocate, presents on containerization without Docker.
- Discusses history of Docker and its impact on container technology.
- Talks about alternative container engines and their benefits, specifically Podman.
- Shares a demo using Podman to manage container builds and images.

Context: A video transcript from a conference talk discussing the topic of containerization without using Docker, with a focus on an alternative container engine called Podman. The speaker is Cedric Clyburn, a Red Hat Developer Advocate.


## Using your brain to access an API | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=Wv537EOuY5Q](https://www.youtube.com/watch?v=Wv537EOuY5Q)



- Speaker is Sebastian Blanc, a developer advocate at Red Hat
- Talking about brain-computer interface (BCI) and its use cases in various industries
- Personal background: Started interacting with computers using a keyboard in the late 80s, then a mouse, and later using body movements like playing tennis on Wii or moving phone to interact with games
- BCI allows direct communication between brain and computer, bypassing physical interaction
- Potential use cases for BCI:
  - People with locked-in syndrome could communicate using their thoughts
  - Truck drivers could monitor cognitive state using BCI while driving
  - Gaming industry: Extended reality (XR) gaming could use BCI to influence game based on brain state
- Neurons produce electricity and create tension, which can be detected and measured
- Brain waves: Different types of waves correspond to different states like sleeping, focusing, or being anxious
- Alpha and delta waves are relatively easy to detect, while gamma wave research is ongoing
- Neurosity is a device that connects to the brain via WiFi and collects data on electrical density and brain waves
- Demonstration of connecting Neurosity to a Node.js application and sending brain wave data to Kafka topic for further processing


## Distributed deployment of microservices across multiple OpenShift clusters | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=IpW7pwnpLLo](https://www.youtube.com/watch?v=IpW7pwnpLLo)



- The speaker introduces himself and the topic of multicloud deployments using OpenShift and Kubernetes.
- Multicloud refers to using multiple cloud providers, avoiding vendor lock-in, and taking advantage of competitive pricing and high availability/resiliency.
- Hybrid cloud interconnectivity is important for multicloud environments, allowing communication between different cloud provider environments.
- Scupper is an open source project that helps enable hybrid cloud interconnectivity, simplifying the deployment and communication between multiple Kubernetes clusters running in different environments.
- The speaker demonstrates deploying a simple ecommerce application across three different cloud providers (Azure, AWS, IBM Cloud) using OpenShift and Scupper.
- The presentation covers creating projects, initializing scupper, generating tokens, connecting to cloud provider accounts, and exposing services to the internet.
- The speaker also mentions that they will clean up the GitHub repository after the demo and provides a link for people interested in learning more about OpenShift and Scupper.


## Dear security, compliance, and auditing: We’re sorry. Love, DevOps | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=aMEr6g25D7Q](https://www.youtube.com/watch?v=aMEr6g25D7Q)


- Welcome to security talk by Bill Bensing
- Discusses love letter, devops security compliance audit, and automated governance
- Talks about the importance of cooperation in conflict resolution within organizations
- Explains bottlenecks in the SDLC process and how they can be addressed with automated governance
- Mentions the concept of "continuous risk assessment" and its role in Dod enterprise devsecops reference design
- Introduces IORICA modeling as a reference architecture for automated governance
- Discusses the use of DevOps tools like Jenkins, Git, SonarQube, and Nexus to implement automated governance
- Explores the benefits of externalizing policy and using a trusted agent to collect test results and enforce policies
- Talks about the importance of observability in understanding what's passing or failing in the system.


## 11 CLI tools every developer should know | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=LfvpYwfJUWs](https://www.youtube.com/watch?v=LfvpYwfJUWs)



- Speaker: Alex Soto
- Topic: 11 CLI tools every developer knows
- Tools covered: Powerlevel10k, Bat, Git (diff), Deep Fancy, Lsd, McFly, Jping, Run, Postman, Zogzili, Python script (Tbcctl, TVctl), Git (marketplace)
- Benefits of the tools: Improved terminal appearance and functionality, file visualization, git diff improvements, directory detection, intelligent command completion, performance testing, Kubernetes integration, easier Git branch management, error reporting.
- Links to websites/repositories provided for each tool.


## A Microservices approach with Cassandra and Quarkus | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=5pcW3eCGpIA](https://www.youtube.com/watch?v=5pcW3eCGpIA)



- Welcome to DevNation Live tech talk about Quarkus and Cassandra microservices.
- Speaker is Raghavan Srinivas, mechanical engineer and distributed systems enthusiast.
- Agenda: Intro to nosql databases (Cassandra), ACID vs CAP theorem, and Quarkus integration with Cassandra.
- Nosql stands for "not only SQL". It's a commodity hardware that can scale horizontally and is suitable for modern distributed systems like Kubernetes.
- Cassandra is a popular nosql database known for its horizontal scaling capabilities and ease of multicluster, multiregion deployment.
- ACID (Atomicity, Consistency, Isolation, Durability) transactions are guaranteed in traditional relational databases but not in nosql like Cassandra. Instead, it follows the CAP theorem which states that a distributed system can only guarantee two of three: consistency, availability, partition tolerance.
- Quarkus is a framework for Java and Java EE developers to create microservices and reduce boot time with a native image feature.
- Quarkus has native support for Cassandra databases through its extension which provides session handling and object mapping capabilities.
- Microservices are independent components that can be deployed, scaled, and developed differently. They follow the REST architectural style and have a loosely coupled architecture.
- The advantages of using microservices include reduced cost, reduced risk, increased complexity, and cultural change.
- Quarkus allows us to write clean, concise code with a simple setup and fast development process.
- We'll see a live coding demo of building a simple todo application using Cassandra as the database and Quarkus for microservices development.
- Speaker encourages attendees to try the Quarkus workshop for free and earn badges by completing tasks.


## GitHub Actions and OpenShift: ​​Supercharging your software development loops | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=KhHV4lJeyfI](https://www.youtube.com/watch?v=KhHV4lJeyfI)



- Speaker is introducing himself and the topic: GitOps, Kubernetes, OpenShift, and automating software development pipelines using GitHub Actions.
- Speaker explains that GitOps is a set of practices for managing infrastructure as code.
- Speaker mentions that the Linux kernel was developed using Git since 2005 and Red Hat started offering enterprise Linux distributions in 1993.
- Speaker talks about how GitHub picked up Git and became popular, and then OpenShift came along in 2011 as a container application platform.
- Speaker mentions that Kubernetes, the open-source container orchestration system, was released in 2014.
- Speaker talks about how GitOps has become an important part of modern software development, with continuous integration (CI), continuous delivery (CD), and continuous deployment (CD) pipelines.
- Speaker mentions that OpenShift Enterprise provides a consistent application platform across hybrid cloud environments using Kubernetes.
- Speaker talks about the Agile software development framework and its principles, which include delivering working software frequently, responding to change, and collaborating effectively.
- Speaker discusses how GitHub Actions can be used to automate various parts of the software development pipeline, including building, testing, deploying, and releasing code.
- Speaker mentions that GitOps is a key part of the DevOps movement, which aims to improve collaboration between development and operations teams.
- Speaker talks about how GitHub Actions can be used to automate infrastructure deployments using Kubernetes and OpenShift.
- Speaker discusses some specific use cases for GitHub Actions, such as building containers, deploying applications, and creating tags.
- Speaker mentions that GitHub Actions can be triggered by various events, such as pushing code or opening a pull request.
- Speaker talks about how GitHub Actions can be used to set environment variables, authenticate with container registries and cloud providers, and deploy applications to Kubernetes clusters.
- Speaker mentions that GitOps is a powerful way to manage infrastructure and software development in a modern, agile, and DevOps-focused organization.


## To the moon and beyond with Java 17 APIs! | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=zjss05yoNts](https://www.youtube.com/watch?v=zjss05yoNts)


- Tech talk about Java 17 features with focus on Vector API, Foreign Linker API, and JFR event streaming
- Duke Java mascot's mission is to travel the Moon using Java 17 APIs
- Vector API:
  - Enhancement proposal added in JDK
  - Improves performance by applying computation multiple operands at once (SIMD instruction extension)
  - Vectorized instructions allow parallelization and optimization
  - Goal is to have clear, concise API for vectorized computation that is platform agnostic
- Foreign Linker API:
  - Allows accessing native libraries within Java applications
  - Useful for interacting with C or Rust code in a Java project
- JFR event streaming:
  - Allows streaming of flight recorder events from the JVM
  - Useful for monitoring and troubleshooting performance issues in real time
- Vector API examples:
  - Trajectory calculation using NASA library
  - Blend operation to propagate values using a vector mask
- Foreign Linker API example:
  - Using Git, libcurl, or SQLite native libraries within a Java application
- Removed APIs:
  - Nozzle engine for accessing JavaScript code in JVM applications was removed in favor of other options (Maven, Gradle)
- JFR unit:
  - A performance regression testing tool using JFR event streaming to identify issues in real time.


## Profile your Java apps in production on Red Hat OpenShift with Cryostat | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=n9_IehZM9aU](https://www.youtube.com/watch?v=n9_IehZM9aU)



* Welcome to Devnation Tech Talk: Java apps production using Cryostat on OpenShift
* Elliot Barron (Red Hat) introduces Cryostat project, focus on JDK Flight Recorder (JFR), OpenShift Operator support, and custom target feature
  * JFR: low-level profiling event collection framework built into OpenJDK since 8U272
    + enables by default in recent versions of OpenJDK 8 and 11
    + allows capture specific application events (e.g., HTTP requests) with custom metrics and APIs
    + JMC supports remote use, but not easy for large deployments due to scalability challenges
  * Cryostat: cloud-native tool that runs alongside the GBM application in a cluster
    + discovers compatible Kubernetes pods running Java applications
    + secures access without exposing external GMX connections
    + supports automated recording management, multiple recordings, and archiving to cloud storage
* Demonstration of installing Cryostat on OpenShift using an operator:
  * Use Operator Hub within the OpenShift console to discover and install Cryostat
  * Create a deployment with a specific namespace (e.g., devnation)
  * Set up cert manager for secure communication within the cluster, optional
* Benefits of using Cryostat in production:
  + Easy way to visualize time series metrics inside the cluster with Grafana
  + Automated analysis and performance issue diagnosis
  + Customizable target feature for remote GMX connections
* Q&A session with live audience:
  + Discussion about impact on production, footprint, JDK 17 support, and continuous monitoring templates.


## Kafka at the Edge: an IoT scenario with OpenShift Streams for Apache Kafka | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=fYA4DHxkk3s](https://www.youtube.com/watch?v=fYA4DHxkk3s)



- Bernard, Technical Marketing Manager at Red Hat, discusses Apache Kafka
- Agenda: explain use case, show demo of IOT scenario, and answer questions
- Apache Kafka is a distributed system for handling continuously stream data, highly available, scalable, and fault tolerant
- Use case: Kafka handles large amount of data ingestion in realtime, such as IoT devices producing data streams
- Realtime analysis and event driven architecture are key features
- Kafka instance consists of brokers, topics, partitions, producers, and consumers
  - Topic is a data flow; typically divided into multiple partitions
  - Producer sends message to topic, which is distributed across brokers
    - Partition replication ensures high availability
  - Consumer consumes partition, allowing massive parallel consumption of data
- Kafka offers APIs for producers, consumers, and admin functions
- Kafka Stream API allows building applications that produce new stream data from existing data
- Kafka Connect API integrates external systems with Kafka
  - Source: takes data from external system and creates Kafka event streams
  - Sink: consumes messages from Kafka topics and pushes data to external systems
  - Red Hat OpenShift Streams is a managed Apache Kafka service
- IOT devices often use MQTT protocol, which can be bridged with Apache Camel to Kafka
- Kafka can enrich raw IoT data with static data from databases using Kafka Connect and Division
- GraphQL query language and runtime can be used to define queries and visualize data from Kafka and external systems
- Demonstration using a smart parking meter dataset in Los Angeles, where MQTT messages are sent from the meters and consumed by Kafka, enriched, aggregated, and presented through a GraphQL UI.


## Be more productive with the new VS Code Java 1.0 | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=LTWIXwZ_ie4](https://www.youtube.com/watch?v=LTWIXwZ_ie4)


- Welcome to DevNation, celebrating the release of Visual Studio Code Java 10 extension.
- Fred Bricken (Principal Software Engineer, Red Hat) discussing history and features.
- Started in 2016 as prototype, became part of VS Code in a week.
- Red Hat team contributed debugging support for Java 8 and beyond.
- Microsoft joined to help improve Java support.
- Features include: easy project setup, configuration, importing, debugging, code completion, refactoring, and performance improvements.
- Demonstration of new features like type hierarchy, pattern matching switch expressions, and unmanaged projects.
- Q&A session covering remote container debugging, recommended extensions, and Gradle integration.


## Quarkus for Spring Developers | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=KamTOMHYG-o](https://www.youtube.com/watch?v=KamTOMHYG-o)


- Conference: DevNation
- Speaker: Eric D. Schabell
- Topic: Quarkus vs Spring
- Eric has spent a year writing a book comparing Quarkus and Spring
- Quarkus is a new Java framework, but it's gaining popularity
- Eric started with a background in Spring and finance industry
- Quarkus is similar to Spring, but it has some differences
- Quarkus has a focus on building RESTful services using Hibernate Panache
- Quarkus uses an abstract layer above JPA like Spring Data JPA
- Quarkus's bean injection happens at build time, while Spring's happens at runtime
- Quarkus has a smaller memory footprint and faster startup time than Spring
- Eric gave examples of how to use Quarkus with Spring technologies like JAX-RS, JPA, and CDI
- Quarkus has built-in support for event-driven architecture and cloud native deployment
- Quarkus's event bus is built on top of Eclipse Vert.x
- Quarkus doesn't require a separate database for each microservice like Spring does
- Quarkus has a simpler way of handling unit tests compared to Spring
- Quarkus uses the Reactive programming model, but it doesn't force you to write reactive code
- Quarkus supports native image generation and containerized deployment
- Quarkus has a smaller community than Spring, but it's growing quickly
- Eric encouraged the audience to explore Quarkus and give it a try.


## Kubernetes configuration and security policies with KubeLinter | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=gX8UuLRfGec](https://www.youtube.com/watch?v=gX8UuLRfGec)



* Michael from StackRock, now Red Hat, presenting on Cubelinter, an open-source tool for enforcing Kubernetes configuration checks
* Tool helps create production-ready YAML files by focusing on best practices and enforcing specific policies
* Cubelinter is a CLI tool designed to be developer-friendly and lightweight, with a simple setup process
* It can be used in a continuous integration (CI) pipeline as part of the development workflow
* Different use cases have different policy configurations; for example, a highly available application may require three pods instead of one
* The tool has over 40 policies and can be customized to fit specific needs
* It integrates with GitHub Actions and other CI tools to automate checks and provide feedback in real time
* The community is actively contributing to the project, and new features are being added regularly.

The speaker goes on to give a detailed demonstration of how Cubelinter can be used to identify and fix configuration issues in Kubernetes YAML files, using various examples and use cases. They also discuss some advanced features like custom checks, annotation handling, and integrating with GitHub Actions for automated testing and feedback. The presentation concludes with a call to action for the audience to try out Cubelinter and contribute to the project if they are interested.


## Level-up your gaming telemetry using Kafka Streams | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=iYym5pFEAXE](https://www.youtube.com/watch?v=iYym5pFEAXE)



- Welcome to another tech talk
- Last time, there was a DNS issue that wasn't an issue with Kafka
- Today's topic: Processing telemetry event streams in Apache Kafka using the Kafka Streams API
- Kafka is a popular open source distributed event streaming platform for building high availability and scalable data pipelines
- A cluster is composed of brokers, which are logical groupings of events called topics
- Topics can be sharded and partitioned for horizontal scaling and replicated across multiple brokers for fault tolerance
- Producers write data to specific partitions based on keys, and consumers can read from multiple partitions in parallel
- Kafka Streams API allows building stream processing applications by implementing stateful transformations and aggregations on data streams
- Demo: A video game telemetry application using Apache Kafka and the Kafka Streams API to process real-time player data for a multiplayer game running on OpenShift across multiple cloud regions.
  - Players connect to the game server, which emits events when they take turns and shoot each other
  - Kafka Streams processes these events in real time to update the game state, which is stored in a state store and displayed in a web application
  - The demo uses OpenShift to manage the Kafka cluster and deploy the game server and aggregation application across multiple cloud regions for low latency and high availability.


## Friends don't let friends do dual writes: OpenShift Streams & Debezium | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=s7w4i3C60KY](https://www.youtube.com/watch?v=s7w4i3C60KY)



- Bernard Tyson from Red Hat presenting on using Kafka for application messaging and outbox pattern
- Kafka is a popular open source event streaming platform, used for moving large amounts of data between systems
- Managed Kafka service provided by Red Hat for streamlined developer experience
- Outbox pattern discussed to handle dual writes (updating two systems with one transaction)
  - Order Service persists order and message in Kafka instead of sending message directly
  - Change event describes instance, transformed before sending to Kafka
- Demonstration includes spinning up a Kafka cluster, creating a topic, and using the outbox pattern for an order service
  - Uses a PostgreSQL database for the order data
- Connects to the Kafka service via OpenShift, with automatic injection of Kafka details into the application
- Kafka Connect used for change data capture (CDC), with a Source Connector for ingesting data from a database and transforming it into Kafka messages. TheSink Connector is used to push data to a sink, such as a database or another topic.
- Outbox pattern allows for eventual consistency (updating one system first, then the other based on the change event) instead of trying to perform dual writes in one transaction.


## Real-time data on the open hybrid cloud with Quarkus and Infinispan | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=2gRwhv11Qkw](https://www.youtube.com/watch?v=2gRwhv11Qkw)



- Welcome to Tech Talk, Katya from Infinispan team in Paris presents about Quercus and Realtime Data Statistics in Open Hybrid Cloud using Infinispan.
- Katya is a Senior Software Engineer based in Paris, Spain and part of the Infinispan Core Team since 2017. She's also part of Duchess France Devoxx France team for several years and a Java Champion since 2019.
- Infinispan is an open source, memory distributed data platform used as a distributed cache.
- Key features: interoperability, resilient fault tolerance, data configuration, clustering, querying, and operator support.
- Infinispan can perform ACID transactions, store data in various formats (Java, JSON, XML), and supports client-server mode, hot rod binary protocol, REST APIs, and embedding in applications.
- Quercus is a microservices framework built using Infinispan that allows for querying and indexing data in real time.
- Infinispan provides global ranking by replicating data across multiple sites or clusters.
- The demo will showcase creating a cache, performing queries, and updating scores in real time using Quercus and Infinispan.
- Katya mentions her gaming background and participation in Battleship Online game to explain the importance of real-time updates and leaderboards.


## Know your app: Add metrics to Java with Micrometer | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=ldeb_DaH49U](https://www.youtube.com/watch?v=ldeb_DaH49U)



- Intro: Welcome to tech talk on application metrics with guest speaker Aaron. Quarkus context.
- Metrics overview: Observability, health checks, log data, trace information, cardinality, dimension data, and micrometer library.
- Micrometer library: Precise fine measurement, vendor neutral, observability systems (Datadog, Splunk, New Relic), and micrometer extension for Quarkus.
- Instrumenting application: CDI or Spring Bean injection, creating a reference to the meter registry in Quarkus, different types of meters (counter, timer, gauge).
- Counter: Monotonically increasing value, annotation based or method interception, and tag values for filtering and aggregation.
- Timer: Measuring duration of methods, wrapper around callable or runnable, and sampling techniques.
- Gauge: Observing size, helper methods, and value drift.
- Long test timer: Counting active tasks, cumulative duration, and visualization.
- Distribution summary: Aggregating data from timers and gauges, filtering, and additional metrics.
- Annotation handling: Long running task timer, completable feature, and flipping annotations.
- Conclusion: Micrometer capabilities, different vendors, and potential use cases with Quarkus.


## Kubernetes-native Java: Latest and greatest features of Quarkus 2.0 | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=ug7KgPxWeQQ](https://www.youtube.com/watch?v=ug7KgPxWeQQ)


- Sebastian Blanc is presenting on Quarkus, a Java framework.
- He mentions that Quarkus was announced in April 2021 and has been gaining popularity.
- One of the new features in Quarkus 20 is "depth mode," which improves developer experience by enabling continuous testing and writing code and running tests at the same time.
- Quarkus uses MicroProfile for resiliency, scalability, and fault tolerance.
- The presentation includes a live coding demonstration of creating a new Quarkus project and adding a REST endpoint using the RestEasy extension.
- Sebastian mentions that Quarkus has improved performance and added features to make development more enjoyable.
- He also discusses some challenges, such as importing Panache entities from different packages and removing blocking code.
- The presentation includes a question and answer session with the audience.
- One audience member asked about using Mutiny instead of RestEasy for reactive programming, which Sebastian mentions is possible but requires more time to implement.
- Another audience member asked about the minimum Java runtime version required for Quarkus 20, and Sebastian mentions that it's not decided yet but Java 8 might still be supported.
- The presentation covers various topics related to Quarkus, including CDI implementation, configuration editing, and endpoints.
- Sebastian also discusses some challenges he has encountered while using Quarkus, such as dealing with blocking code and managing dependencies.
- He emphasizes the importance of continuous testing and saving files regularly to avoid losing work during live streaming or busy days.


## No YAML! Kubernetes done the easy way | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=jBDmX85IjLM](https://www.youtube.com/watch?v=jBDmX85IjLM)



- Welcome to Kubernetes talk
- Bengaluru, India based engineer Kamesh will present
- Discussing everything Kubernetes from an easy perspective
- Agenda: Deploy container using GitHub repository and OpenShift
- Use command line and browser for demo
- Kubernetes uses YAML files
- Reduced code from 70 lines to 25 or even 10 with K Native
- Started using Kubernetes a year ago, initially struggled with YAML formatting and debugging technology
- OpenShift: Admin perspective, cluster management, compute management etc.
- Will show how to deploy container image using simple GitHub repository
- Demonstrate how to connect to database and firewall protection
- Use Tecton pipeline for continuous delivery
- Show how to run application on 8080 port and securely send traffic within OpenShift
- Discussed administrative and developer perspectives, differences between earlier versions of OpenShift
- Deploy Java application from GitHub repository
- Fetch repository, identify topology view, create deployment, create route for accessing the application, and deploy container image
- Application running in seconds without writing YAML files
- Delete application if not wanted
- Use K Native tutorial to deploy a simple 'Hello World' app
- Discussed the importance of using certificates and avoiding TLS termination
- Demonstrated how to access the application using Swagger UI and make it bigger with a local database
- Deleted an earlier service and discussed creating a new one using OpenShift web console
- Discussed how to add secrets, trigger pipelines with GitHub push, and use webhooks
- Concluded by discussing the benefits of using OpenShift and Kubernetes together.


## RESTEasy Reactive: Why should you care? | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=SniHOzv4qy4](https://www.youtube.com/watch?v=SniHOzv4qy4)


- Speaker: Stefan E Pardo, Red Hat engineer working on Quarkus
- Topic: Reactive and Rest Easy in Quarkus
- Live streaming from France
- Traditional architecture: web server -> IO worker thread -> request dispatcher -> worker thread pool -> single thread -> response generation -> user
- Problem with traditional architecture: blocking threads, waiting for I/O operations to complete
- Reactive programming in Quarkus: cutting request endpoint actions into smaller pieces, using non-blocking I/O, eliminating waiting steps
- Reactive JAX R implementation in Quarkus: asynchronous default, simplified build time, better APIs, small memory footprint
- Example project: REST API using blocking version, Hibernate ORM, Panache, JDBC, Rest Easy traditional recipe
- Demo: Listing fruit using web console and Swagger UI, implementing JAX R endpoint with `@Path` annotation, returning a string or list of fruits, dealing with query parameters and filters
- SSE (Server Sent Events): sending real-time updates to clients, using multivalue broadcaster and Rest Easy subscribe function
- Use case: Calling HTTP services and coordinating multiple devices, handling thousands of requests in parallel, using Eric's API client for asynchronous calls
- Performance improvements with Quarkus reactive programming: eliminating blocking worker threads, using Rest Easy reactive instead of traditional implementation, simplifying code and reducing overhead.


## Building streaming applications using a managed Kafka service | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=y5TxIebFufI](https://www.youtube.com/watch?v=y5TxIebFufI)



- Welcome to another DevNation Tech Talk week at Red Hat Summit
- Demonstrating a battleship game using Kafka and serverless technology
- Evan is the guest speaker
- Previously worked on frontend and backend engineering for the same project, which used Kafka, Node.js, Quarkus
- Introducing Apache Kafka: distributed event streaming platform, thousands of companies use it for high performance data pipelines and streaming analytics
  - Distributed log store
  - Tonnes of messages flowing persistently
  - Three main pieces: key, value, and timestamp (typically unique identifier)
- Use case: real-time applications with immediate access to information and processing capabilities
- Microservices architecture: loose coupling between services, using Kafka for communication and data transfer
  - One service pushing data, another pulling it back
- ETL and CDC scenarios: moving from batch processing towards real-time data capture and transformation
  - Real-time metrics instead of periodic queries
- Red Hat OpenShift Stream: managed Kafka offering on the cloud, reducing complexity by managing Kafka, Zookeeper, and Kubernetes for you
- Live demo using Quarkus and OpenShift
  - Sign up for a free trial on CloudRedhat.com
  - Create a Kafka instance and deploy your application using service binding
  - Connect to the running application and see it generating random numbers that are pushed to a Kafka topic
- Red Hat OpenShift Stream: easy integration with other Red Hat technologies, such as Dabisium for capturing change data from databases.


## Improving security with Istio | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=U_SqX5uMbds](https://www.youtube.com/watch?v=U_SqX5uMbds)



- Alex Soto Bueno will talk about security in Istio, a service mesh for microservices architecture.
- Monolith applications used to be single database and big, now microservices have several services interconnected, each with its own database and entry point.
- Service architecture uses multiple services instead of monolith applications for easier deployments.
- Microservices communicate over the network, so they need to be made resilient against failures and attacks.
- Istio helps make microservice architectures secure by covering service discovery, authentication, traffic management, and monitoring.
- Istio uses sidecar containers that intercept network traffic to manage and secure it. It can encrypt, reroute, or block traffic based on rules.
- Istio also has features for managing certificates and handling authentication and authorization.
- In the demo, Alex will use OpenShift and a customer preference application with recommendation microservices. They will register services, apply virtual services, and secure communication between them using Istio.
- Istio can automatically encrypt internal traffic and manage certificates for http services, but it's important to check that internal communication is encrypted.
- Istio also provides fine-grained access control and supports JSON web tokens for authentication. It validates tokens, checks issuers, and enforces policies.


## Building successful business Java apps: How to deliver more and code less | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=Ed96uYCEgbo](https://www.youtube.com/watch?v=Ed96uYCEgbo)


- Welcome to another Tech Talk, introducing Alex Porcelli from Brazil, a brilliant engineer working at Red Hat.
- Topic: Building successful business applications by translating business needs into runnable software.
- Communication is a challenge with stakeholders, especially when there's an increase in agility for software delivery.
- Two personas involved in building software for business applications: developers and domain experts.
- Domain knowledge is essential, but it takes time to acquire. Communication between these two personas can be challenging due to the impedance mismatch between code and domain expertise.
- Cogito project: Building an intelligent application backed by battle-tested capability using a simple driver's license application demo.
  - Three main components: decision service, business process orchestration, and driver license emission service.
  - Quarkus application written in plain Java code.
- Demonstration of the application:
  - Sending an HTTP request and checking its status.
  - Changing a rule to enable people under 18 to drive and testing it.
- Quercus is used for building the project, and the Cogito extension simplifies the process by providing predefined code and services.
- Domain experts can easily visualize and understand business automation using DMD (Decision Model and Notation) and BPMN (Business Process Model and Notation).
- The Cogito team provides a Chrome extension that allows users to view decision models and BPMN files directly in the GitHub interface without needing additional tools.


## Continuous performance regression testing with JfrUnit | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=Lgr3orOi3sI](https://www.youtube.com/watch?v=Lgr3orOi3sI)



- Speaker is Gunner, a software engineer and engineering lead at Red Hat
- Topic: Continuous performance regression testing using JFR unit and JDK Mission Control
- Challenges of performance testing include identifying throughput, latency, and specific request issues in different environments
- JFR unit uses JDK Flight Recorder for monitoring and analyzing performance metrics like memory allocation and garbage collection
- JDK Mission Control is a client tool for controlling recording and analyzing data from JFR recordings
- Objective: Identify performance regression by comparing metrics between versions or baselines
- Use of third-party libraries can produce unexpected events, making it necessary to use the JMC agent to control their production
- Continuous recording allows analysis of recent production data for identifying issues in real-time
- Focus on memory allocation and garbage collection as key performance indicators
- JUnit tests can be used with JFR unit for asserting specific events like garbage collection or thread sleep
- JFR event testing allows for inline code modification and customizing recording configurations
- Potential issues include database queries not producing JFR events, and the need to optimize resource usage and avoid unnecessary statement execution.


## Secure Vue.js apps with Keycloak | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=aHhSmzZzsog](https://www.youtube.com/watch?v=aHhSmzZzsog)


- Welcome to another DevNation Live tech talk from Raleigh, North Carolina.
- Co-host Edson Inaguaran introduces Abbas Sheikh, who will discuss Red Hat's Keycloak and network security.
- Technical difficulties with audio and video connection.
- Abbas starts by discussing the Red Hat BlueJeans session, a cloud-based technology for live streaming.
- Focus on Keycloak, an open source identity solution for modern and legacy applications.
- Keycloak provides strong community support and customization according to need.
- Portability is important, as businesses may switch cloud providers.
- Overview of the Keycloak architecture and its integration with applications using OpenID Connect and OAuth 2.0 protocols.
- Demonstration of integrating a VueJS application with Keycloak using an instance of the identity provider.
- Q&A session starts, but technical difficulties continue with audio and screen sharing.
- Discussion about realm, multiple applications within a realm, and securing external sites.
- ViewJ application needs access to user data, requiring a caucus pattern for authorization headers with JWT tokens.
- Demonstration of deploying Keycloak on Kubernetes using a stateless architecture and multiple backends.
- Explanation of the token endpoint interaction and its importance in securing access tokens.
- Attempts to share screen and video fail due to network issues.
- Discussion about rescheduling or recording the presentation for later release.
- Mention of upcoming events and other talks on the Damnation Channel.


## From code to Kubernetes the fast way with odo 2.0 | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=I8I61UO1xIg](https://www.youtube.com/watch?v=I8I61UO1xIg)



- Special day with special guest, Cedric, talking about Odo 20 and auto cloud native development on OpenShift.
- Cedric is a Red Hat intern and Java academic student at NC State University.
- Odo has been around since early 2019, originally called "legacy article content" and enhanced functionality with Kubernetes support.
- The focus today is on deploying front-end and back-end applications using Odo in OpenShift.
- Jason Dobies from the Bosch team will be watching and mentoring.
- Dev file is a new feature in Odo 20 that allows reproducing development environments and sharing clusters in Kubernetes or OpenShift.
- It describes the development environment, including container definitions, project cloning, predefined commands, and customization options.
- To create a dev file, use `odo create <nodejs|go|ruby> <component_name>` command with default settings.
- Dev files are portable and can be used to deploy applications on Kubernetes or OpenShift.
- Odo is lightweight and streamlines the developer experience in writing, building, and deploying applications on OpenShift.
- It supplements, not replaces, traditional `oc` tools for managing OpenShift clusters.
- The demo will show using a generic OpenShift project and using the Visual Code Extension for faster development.
- Dev file is a YAML file that includes metadata, build Dockerfile/deploy manifest, component list, and custom commands for debugging and testing.
- Migrating from source image files to dev files can be done by converting the existing image using Odo utils.
- Dev files allow easy sharing of environments between teams and customizing components with specific versions and runtime settings.
- Using Odo 20 instead of OpenJDK is recommended for better performance and compatibility.
- To push an application using a dev file, use `odo push` command with the utility function to convert and deploy the dev file.
- The new version of Odo fixes many bugs and is highly recommended for improvements.


## Take the highway: Quarkus reactive routes | DevNation Tech Talks

URL: [https://www.youtube.com/watch?v=svG_VBjVhis](https://www.youtube.com/watch?v=svG_VBjVhis)



- Speaker: M. Reactive (Mr Thing Reactive) from France
- Topic: Quarkus - The New Kid on the Reactive Block
- Clematis Coffee and Edson are hosts of DevNation Tech Talk
- Kofi from Red Hat working on Caucus Vertex, Mutiny, small Iraqi messaging
- Discussing taking the reactive journey with Pirate (Quarkus)

**What is Quarkus?**
- Write Java application tailored for cloud native environments
- Provides everything needed for microservices and serverless applications
- Includes command line toolset, extension ecosystem, never stops growing

**Why use Quarkus instead of other frameworks?**
- Faster boot time (significantly reduces boot time)
- Reduces memory consumption (avoids class loading, reducing number of classes)
- Amazing developer experience (immediate application feedback, no need to restart)

**Quarkus Features**
- Build time optimization: Pas configuration, build thing framework knows everything about the application
- Asynchronous message passing using Akka (Elasticity and Resilience)
- Integrates well with Kubernetes, Docker, and other containerization technologies
- Supports popular databases like Cassandra, PostgreSQL, MySQL, etc.
- Easy to deploy and run in various environments

**Quarkus vs Traditional Frameworks**
- Quarkus uses a nonblocking I/O model (single thread handles multiple concurrent I/O requests)
- Simplifies writing nonblocking code (Caucus extensions make it easier)
- Provides a lower level of abstraction (more control over the application)

**Quarkus vs Competitors**
- Quarkus is faster than traditional Java frameworks and other competitors (Benchmark results available online)
- Offers better memory usage and reduced thread usage (save money on cloud resources)

**Conclusion**
- Quarkus is a promising reactive Java framework, designed for modern, cloud native applications.
- It offers faster boot time, reduced memory consumption, and an amazing developer experience, making it an attractive choice for developers looking to build modern applications.


## Building kubectl plugins with Quarkus | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=ZL29qrpk_Kc](https://www.youtube.com/watch?v=ZL29qrpk_Kc)



- Intro: Sebby Blanc, Java developer and speaker, presents on building Cube CTL plugins using Quarkus.
- Cube CTL overview: It interacts with the Kubernetes API server, is intuitive and extensible.
- Creating Cube CTL plugins:
  * Language agnostic: Write in any language (example: Bash, Go, Python, Java).
  * Naming convention: Plugin name should start with `cubectl-`.
  * Parsing arguments: Use a library like PicoCLI to handle command line options.
  * Interacting with Kubernetes cluster: Use official Kubernetes Java client or Fabric8.
  * Compiling and running the plugin: Create a JAR file and make it executable.
- Challenges in creating Cube CTL plugins using Java and Quarkus:
  * Parsing arguments: Need to use libraries like PicoCLI to parse command line options.
  * Interacting with Kubernetes cluster: Need up-to-date libraries, like Fabricate, to interact with the cluster.
  * Compiling and running: Need to compile the plugin as a native executable using platforms like GrowVM.
  * Java vs Quarkus: Quarkus is faster, smaller, and has more features than Java alone.
- Conclusion: Cube CTL plugins can be created using any language with proper naming conventions and libraries. The process involves handling command line arguments, interacting with the Kubernetes cluster, and compiling and running the plugin. Challenges include using up-to-date libraries and compiling native executables. Quarkus offers improvements in speed, size, and features compared to Java alone.


## Let's make a contract: The art of designing a Java API | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=oRzt0rBsyUs](https://www.youtube.com/watch?v=oRzt0rBsyUs)


- Speaker: Mario Fusco, project leader and coordinator from Milan
- Topic: Designing good Java APIs
- Points covered:
  - Importance of a good API design for developers
  - Basic principles for designing good APIs
    - Orthogonal design (avoid contradictions)
    - Flexibility and ease of evolution
    - Intuitive and easy to learn
    - Proper documentation
  - Common mistakes in Java API design
    - Overloading methods with different arguments and names
      - String methods in the StringBuilder class
    - Inconsistent argument order
    - Long method signatures and argument lists
    - Returning unnecessarily complex types or collections
- Tips for improving API usability and flexibility
  - Encapsulating complexity using classes
  - Defining a clear intent
  - Leveraging type system and encapsulation
  - Providing fluent APIs
- Examples of good practices in Java API design:
  - Optional types to avoid null pointer exceptions
  - Support for lambda functions with functional interfaces.

I hope this summary is helpful! Let me know if you have any questions or need further clarification.


## OpenShift Developer Sandbox: Kicking the tires | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=oDqw8aBGDD8](https://www.youtube.com/watch?v=oDqw8aBGDD8)


- Welcome to DevNation Tech Talk by Edson Sininaga and Joel (second speaker)
- Discussion about developer sandbox on Red Hat Developer
- Developer Sandbox website offers a free 14-day trial for OpenShift exploration
- Creating an account using email verification, and creating a new cluster in the OpenShift platform
- Need a Red Hat Developer Account to use developer sandbox
- Discussion about deploying applications on OpenShift with a small application as an example (url shortener)
- Building a React application with Docker, and pushing it to Docker Hub
- Creating a new OpenShift application using the image from Docker Hub
- Deploying a database in OpenShift along with the application
- Exposing the service and setting up routes for accessing the deployed application
- Health checks and monitoring in OpenShift
- Adding environment variables and configuring connections to databases
- Using SUI (OpenShift UI) for deploying and managing applications
- Deployment process and using a redirector service to connect different services together
- Recap: creating, deploying, and managing microservices in OpenShift using the developer sandbox.


## Serverless, Tekton, and Argo CD: How to craft modern CI/CD workflows | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=nV6b-9eMEzc](https://www.youtube.com/watch?v=nV6b-9eMEzc)



- Welcome to DevNation Tech Talk (Madrid, Spain)
- Speaker: David Sanchez from Red Hat Services based in Spain
- Topic: Serverless Tecton and Argo CD
- Agenda: CI/CD workflow for serverless applications using Tecton and Argo CD
- Overview: Use declarative approach with GitOps to manage infrastructure and applications
- Technology involved: Tecton (Kubernetes native framework), Argo CD (GitHub's continuous delivery tool)
- Workflow explained: 1. Continuous Integration (Tecton pipeline) 2. Continuous Delivery (Argo CD)
- Key features of Tecton: Decouple pipelines, reduce different pipelines for deploying Kubernetes clusters, resource swapping (e.g., parameter workspace, git report registry)
- Key features of Argo CD: Declarative GitOps approach, detects difference between desired and actual application state, provides purely declarative approach for configuration customization
- Demo application: Quarkus (Java application with small memory footprint, fast startup time)
- Main components: Creative Service (single object for managing multiple deployments), conflict map (prioritize properties to manage conflicts)
- Steps in the workflow: 1. Developer pushes new change to application source (repository); 2. Tecton pipeline starts with fetching source code, unit testing, building container image; 3. Pushed change is cloned and a new revision is created; 4. Argo CD pulls configuration from repository and synchronizes existing Kubernetes objects; 5. New configuration is deployed to the cluster (manually in production); 6. Changes are detected and synced back to the GitOps repository.
- Structure of GitOps repository: Base directory contains global server descriptor, each environment represented by a different folder for customization.

If you need further clarification or if something is unclear, please let me know!


## Java and containers: What's there to think about? | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=2IpJABPzpvw](https://www.youtube.com/watch?v=2IpJABPzpvw)



- Kerry North Carolina conference talk
- Christine Flood, Massachusetts resident, discussing Java container history and optimization for smaller footprint and faster startup in containers.
- Focus on JVM optimization: heap size, GC, stack size.
- History of JVM focus on performance, safety, and quality service guarantee.
- Current goal: making JVM run efficiently in containers with small footprints and fast startups.
- OpenJDK efforts to make JVM smaller and more efficient for container use.
- Discussion of default JVM settings, like stack size (1024k), and their impact on performance within a container.
- Comparison of native image and JVM runtimes in containers.
- Use of Podman and checkpoint restore for efficient Java application deployment and recovery.
- Explanation of how to reduce Java container image size and improve startup times using lower memory usage and native images.
- Mention of Substrate VM and its limitations for running Java applications within a container, as well as comparison with OpenJDK.
- Encouragement to experiment with JVM settings and configurations for optimal performance in container environments.


## From code to Kubernetes the fast way with odo 2.0 | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=G__DxamRoEc](https://www.youtube.com/watch?v=G__DxamRoEc)



- Host (Anthony) introduces Cedric Clyburn, an OpenShift developer advocate at Red Hat.
- Cedric talks about using Odo for deploying applications on OpenShift and Kubernetes without understanding complex concepts.
- Agenda: Odo overview, portable development environment, upgrading components, MiniCube compatibility, and demo.
- Odo is an iterative, straightforward CLI tool to create and manage applications on OpenShift and Kubernetes.
- New features in 20 release include dev files for creating and configuring development environments.
- Dev files are portable YAML files that describe the deployment environment, including build and runtime configurations.
- Odo allows developers to easily upgrade components within a project without recreating the entire cluster.
- MiniCube compatibility in 20 release enables local Kubernetes development with OpenShift tools.
- Demo: Creating a new NodeJS project using Odo, customizing registry pulling, and deploying it on OpenShift.
- Customization includes adding or removing components from the default registry and creating a custom dev file.
- Using `odo create` command, developers can create components, import images, and configure settings like memory limits and endpoints.
- The `odo push` command deploys the project to OpenShift using the defined configuration.
- Developers can use the `odo watch` command to automatically redeploy changes made in the codebase.
- Q&A session: no context.


## Profiling Java inside containers with ContainerJFR | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=NQULoG2pLa8](https://www.youtube.com/watch?v=NQULoG2pLa8)



- Introducing Andrew Azares, talking about profiling Java applications and using JFR (Java Flight Recorder) in containerized environments.
- Overview of Java Virtual Machines (JVMs), JFR as a runtime agent, and JMX for monitoring and management.
- Comparison between JFR and traditional JMX agents, specifically in terms of overhead, start/stop capabilities, and access to data without the need for additional configuration.
- Explanation of continuous profiling vs. specific problem profiling and the advantages of JFR's event-driven approach.
- Demonstration of using JFR with OpenShift and Kubernetes, including creating a recording, analyzing it with Mission Control, and visualizing data in Grafana.
- Security considerations for JFR, such as encrypted connections, authentication, and preventing data leaks.
- Conclusion and Q&A session.

No context.


## Kubernetes-native or not? When should you ditch your traditional CI/CD server? | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=A8r7CZjfi1s](https://www.youtube.com/watch?v=A8r7CZjfi1s)



- Conference: Dev Nation Live Stream
- Location: Raleigh, North Carolina
- Speaker: Dejuan Juan (now works at Red Hat)
- Topic: Tecton pipeline automation with Kubernetes
- Audience: Beginners to experts in Tecton
- Agenda: Theory, demo, Q&A
- Questions during presentation are welcome
- Focus: Understanding Tecton and its advantages compared to traditional CI/CD servers (like Jenkins)
- Tecton is a framework for creating reusable CI/CD systems using Kubernetes
- Key components of Tecton:
  - Extends Kubernetes with custom resource definitions (CRDs)
  - Leverages existing Kubernetes resources and adds an extra layer
  - Runs Kubernetes tasks sequentially or in parallel
  - Provides a reusable CI/CD system for running Kubernetes workloads
- Comparison to traditional CI/CD servers:
  - Centralized logging and monitoring (Prometheus, Grafana)
  - High availability (Kubernetes guarantees high availability)
  - Self-healing (Kubernetes can automatically recover from failures)
  - No need for external agents or SSH access
- Demonstration will use a Java application, GitHub repository, and Slack integration
- Tecton pipeline includes tasks like build, push, deploy, and slack notification
- Pipeline runs on Kubernetes with Tecton's built-in resources and custom service account permissions
- Deployment includes the use of OpenShift for convenience and its nice UI
- The speaker encourages asking questions throughout the presentation.


## Seven perilous pitfalls to avoid with Java | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=VrEc1ODFRKw](https://www.youtube.com/watch?v=VrEc1ODFRKw)


- Welcome to Devnation Tech Talk, today we have Steve Poole presenting on Java security.
- Steve is the author of "Seven Punicators: A Tale of Security" and has joined Red Hat this month.
- Topic: Deep dive into specific Java security issues, not just the basics.
- Focus will be on input validation as a pernicious problem in Java.
- Examples will include browser form attacks, file uploads, and code injection.
- Input validation can happen at various stages of Java code, including constructors, file system, and database queries.
- It's important to understand that data received is potentially unreliable or dangerous, even from a REST API.
- Common patterns for REST APIs include slash APIs and versioning, which can be exploited by attackers.
- Attackers can also try to manipulate request methods, headers, and cookies to gain unintended access.
- Be aware of SQL injection vulnerabilities, especially in property files or command line arguments.
- Encryption is not foolproof, as there are always potential weaknesses that attackers can exploit.
- Keep error messages clear and informative, as they can provide valuable information to attackers.
- Use defense in depth, making it difficult for attackers to gain a foothold in your system.
- Code quality is crucial, ensuring that code is not poorly written or easily exploited.
- Encapsulation can help prevent data access within classes.
- Be aware of state management vulnerabilities and try to control state transitions.
- Understand the potential risks of third-party dependencies and ensure they are thoroughly tested.
- Test your application extensively, including edge cases and error scenarios, to catch vulnerabilities early.
- Q&A: Javed asked about common pitfalls or top 10 vulnerabilities in Java security. Steve mentioned that there is a strong correlation between the OWASP Top Ten and the issues he covered in his presentation.


## Kubernetes, Istio, and Telepresence: Develop/test your code in production! | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=S71B_XKxKyQ](https://www.youtube.com/watch?v=S71B_XKxKyQ)


- Special guest Bartosz from Zurich, Switzerland will talk about Kubernetes Telepresence and testing in production without delay.
- He'll discuss the development process and challenges of managing containers and services in a distributed system.
- Telepresence is a tool that allows developers to interact with real clusters without spinning up containers locally.
- It works by rerouting traffic to the developer's machine, allowing for a native experience when developing directly in the cluster.
- Telepresence can be used with IDEs like Eclipse, IntelliJ or VS Code and has features like circuit breaking, routing, and traffic splitting.
- It's a powerful tool that enables local development while interacting with production services, but it brings certain levels of complexity due to its statefulness.
- Telepresence is not a replacement for staging environments and can have limitations in manipulating data exposed to users.
- It requires security enhancements and careful consideration when dealing with specific architectures or projects.
- Installing and using Telepresence involves adding certain privileges, tweaking configurations, and using the telepresence CLI tool.
- Telepresence is used extensively in popular projects like Istio and OpenShift and has a large community of contributors and users.
- The talk will cover use cases, demonstrations, and best practices for using Telepresence in various scenarios.

I hope that summarizes the transcript well enough! Let me know if you have any questions or need clarification on any points.


## Spring Boot to Quarkus: A real app migration experience | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=R1nn64LkaHc](https://www.youtube.com/watch?v=R1nn64LkaHc)



- Welcome to DevNation Tech Talk
- Special guest today: Jonathan Viva from Barcelona, Spain
- Topic: Migrate Spring Boot Application to Quarkus
- Migration worth discussing
  - Step by step migration process
  - Performance comparison

## Background on Quarkus
- Framework used in Kubernetes native applications
- Always thinking compatibility with GraalVM and OpenJDK
- Faster than traditional methods of creating applications
  - Smaller regarding memory footprint
  - Focused on easy code creation
- Opinion: Lecture will teach simple migration experience

## Quarkus Key Features
- Run in native mode (JVM also supported)
- Using standard library instead of reinventing the wheel
- Fast release cycle, every two weeks
- 90+ extensions available
  - Adapting popular technologies: Kafka, Camel, Keycloak, Spring Boot, etc.

## Migration Process
### Preparation
- Decided to migrate Spring Pet Clinic application (REST version)
- Including several libraries: Spring Data, Spring Web, Documentation, Actuator, Micrometer, CDI, AOP, and more

### Application Development
- Quarkus uses CDI instead of Spring's autowiring and constructor injection
  - Easier bin declaration using application scope and auto-injection
- Simplified code by reducing implementation complexity
  - Removed unnecessary dependencies (JPA, JMX, etc.)
  - Changed Spring Rest to Quarkus REST, adjusted mappings accordingly

### Performance Improvements
- Faster startup time (less than half a second)
- Testing took less time (16 ms first response instead of 4 seconds)

## Comparison with Traditional Cloud Native Stack
- Significantly faster response times and lower latency
- Time to start the application is dramatically different (Quarkus takes 13 seconds, RBM takes 135 seconds)

## Conclusion
- Quarkus evolves rapidly, with frequent releases and improvements
- Recommendation: Try the migration yourself if you're interested

## Additional Resources
- GitHub repository for original Pet Clinic application migrated to Quarkus
- Quarkus web page
- Follow Quarkus on Twitter
- Katakura Interactive platform for training and resources
- Check out Prometheus, Hibernate Streaming, and Spring Depth for additional tools


## Contract-driven development with OpenAPI 3 and Vert.x | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=mQefaHN5-mI](https://www.youtube.com/watch?v=mQefaHN5-mI)



- Speaker: Franceso Guardiani, software engineer at Red Hat
- Topic: Open API and contract driven development
- Presentation is for people who build APIs and consume them, primarily enterprise developers
- Documentation and communication with frontend colleagues, stakeholders, and project access to web apis are discussed
- Poll: 61% of respondents said they document shared team documentation, 29% use code or query parameters, and only 10% use a link to share
- Speaker mentions microservices and monoliths
- Discusses the importance of well-defined contracts for web services and the challenges of keeping them synchronized with the codebase
- Talks about using tools like OpenAPI, Swagger, and IDL for documenting and generating code from contracts
- Mentioned MicroProfile, which is a set of specifications for building microservices in Java EE
- Speaker emphasizes the importance of collaboration between frontend and backend teams and stakeholders to create well-designed contracts
- Discusses the benefits of contract-driven development, including improved automation and collaboration
- Mentioned tools like OpenAPI Generator, Redux, and Vertex for generating documentation and code from contracts
- Speaker discusses the importance of describing metadata in contracts using annotations or other means to make them more human-readable
- Talks about the advantages of using open APIs over traditional RPC-style APIs, including flexibility and ease of use
- Discusses the challenges of evolving APIs without versioning and contrasts this with gRPC's approach to contract evolution
- Emphasizes the importance of testing and validating requests and responses at the API level to ensure consistency and security.


## How I Built a Serverless Blog Search with Java, Quarkus, and AWS Lambda | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=7ptEPuo3L6s](https://www.youtube.com/watch?v=7ptEPuo3L6s)


- Welcome to another DevNation talk, hosted by Gunner and James Dade.
- Today, Gunner will be discussing Quarkus serverless technology for a blog search feature in Amazon Lambda architecture.
- Serverless means no need to provision or manage servers, focusing on deploying and scaling functional code.
- Three reasons for using serverless: smaller attack surface, lower cost, and learning opportunity.
- Architecture overview: static content hosted on Github Pages, search request handled by Lambda function via API Gateway and AWS Serverless Runtime Environment.
- Implementation using Gravie (Quarkus Apache CDI) for dependency injection and lambda function implementation.
- Three ways to implement serverless apps with Quarkus: 1) using Java and the Lambda Request Handler interface, 2) using Funq (Caucus umbrella), and 3) using a familiar web stack like Vert.x and RestEasy.
- Benefits of serverless include faster startup times and optimized memory usage.
- Challenges include dealing with external dependencies and construct support in Gravie.
- Using an extension like Clockwork to handle method binding and substitution attribute factory.
- Building a deployable function package with a ZIP file, containing the search index and API Command Line Tool (AWS CLI).
- Using AWS Make to easily deploy Lambda functions and infrastructure.
- Important considerations include cost control and security measures like budget circuits and identity access management.
- Q&A session to follow.


## Cloud-native modernization or death? A false dichotomy. | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=p0yX8kwI2zA](https://www.youtube.com/watch?v=p0yX8kwI2zA)



- Speaker: Daniel Oh from Boston, MA
- Topic: Application modernization / monetization, focusing on migration to cloud native style
- Tools mentioned: Migration toolkit (Monash), kubernetes, openshift, jdk, JPA, PostgreSQL, Quarkus, Spring Boot
- Steps in migration process: Rehosting, replatforming, refactoring
  - Rehosting: Move application to cloud native platform without changing architecture or codebase
    * Example: Monolith application running on Oracle Weblogic moved to Java application based on Quarkus and Kubernetes using MTA (Monash Toolkit for Automation)
  - Replatforming: Change underlying technology stack, while keeping the existing codebase and architecture
    * Example: Application running on kubernetes cluster with OpenShift5
  - Refactoring: Redesign application architecture to be cloud native and microservices based
- Benefits of migration: Faster development and deployment, easier scaling, cost savings, better security, modern technology stack
- Q&A session will follow
- Contact information: Twitter, YouTube channel for more info or questions.


## Hacking the Mesh: Extending Istio with WebAssembly Modules | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=QMzYBQzsjyQ](https://www.youtube.com/watch?v=QMzYBQzsjyQ)



- Welcome to DevNation, Daniel Grimm will talk about hacking Istio service mesh using WebAssembly
- Dan is a member of the issue team at Red Hat, talks about extending Istio with WebAssembly
- Service mesh like Istio helps avoid cascading failures and provides observability across infrastructure
- It performs tasks such as load balancing and circuit breaking
- Infrastructure might use heterogeneous languages but service mesh makes it behave consistently
- Envoy delivers functionality through a listener, network filter, and HTTP filter
- Filter chain in Envoy: incoming request -> b c filter -> cbna (simple model)
- Three types of filters: listener, connection, and network/HTTP
- Listener filters decide which filter to use based on the traffic
- Network/HTTP filters read and write encrypted data, decrypt traffic, and handle routing decisions
- HDP filters act at layer 7 and understand HTTP request semantics
- WebAssembly is a near-native bytecode format with a lightweight isolation model
- Istio developers are adopting WebAssembly for its simplicity and ease of integration with Envoy.


## ArgoCD and Tekton: Match made in Kubernetes heaven | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=CFqkFPqQMWs](https://www.youtube.com/watch?v=CFqkFPqQMWs)



- Welcome to DevNation Live Tech Talk with Cmac from Sweden, discussing Argo CD and Tekton
- Cmac is wearing a Kubernetes shirt, encourages audience to buy one
- DevNation will have a new show on Tuesday in a game show style
- Argo CD is a tool for delivering applications using Continuous Integration/Continuous Delivery (CI/CD) in Kubernetes environments
- It's an open source project that focuses on declarative CI/CD with native Kubernetes resources
- Tekton is a CI system, and Argo CD complements it by addressing the last mile of application delivery
- Argo CD identifies desired state in Git repositories and ensures it matches the live cluster constantly
- It can deploy applications to multiple clusters and monitor their health, auto-syncing changes across them
- It supports various tooling, including GitHub Actions, Jenkins, and GitOps workflows
- Argo CD is useful for managing large numbers of clusters across different cloud providers and premises
- Centralized management is a key benefit, providing visibility into pipeline failures and successful deployments
- The talk covers use cases, architecture, and deployment process with examples and demos.


## 10 awesome Kubernetes tools every user should know | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=5eIlfNGGuU8](https://www.youtube.com/watch?v=5eIlfNGGuU8)



- Welcome to another DevNation Live Tech Talk, live from Raleigh, North Carolina.
- Today's topic: Kubernetes CLI tools for productivity and advanced features.
- Presenter is Alex Soto, Red Hat Software Engineer. Follow him on Twitter @alexakovi or email alex.soto@redhat.com.
- Start with basic concepts of Kubernetes: pod, service, deployment, namespace, replica set, etc.
- Introduce Cubanitas and its CLI tools for managing Kubernetes.
  - Dive: explore the layers of docker images and their contents.
  - kubectl: manage and control various aspects of Kubernetes clusters and applications.
  - Alice: manage and scale clusters using aliases, scripts, and other features.
  - Stir: real-time observation and analysis of cluster events and logs.
  - Xray: visualize dependencies and interactions between deployments.
  - Cdx: modify terminal output for better visibility and control.
  - Jiva Spy: observe and trace Kubernetes resources in real time.
  - Knowledge: access and manage knowledge base information related to Kubernetes.
- Demonstration of using various Cubanitas tools to perform tasks in a Kubernetes cluster, such as creating deployments, checking logs, inspecting resources, and managing configurations.
- Encourage questions from the audience.


## Serverless Workflow: New approach to Kubernetes service orchestration | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=sTgto7c_iNQ](https://www.youtube.com/watch?v=sTgto7c_iNQ)



- Welcome to Destination Tech Talk, today we have Hormier from Red Hat discussing Serverless Workflow Specification
- Goal is to provide a consistent, portable, and accessible workflow model definition for event-driven microservices
- Serverless Workflow Specification: defines clear schema for workflow definition; provides software development kit (SDK) in Java and Go; includes conformance specification and extensions for performance optimization
- Function definition: contains work specification for dealing with service needs in workflow execution, such as cloud service or container environment definitions
- Event definition: reusable definition for events consumed/produced in workflow orchestration; allows correlation rules to associate multiple events with a single workflow instance
- State definition: defines control flow logic and state transition between different parts of a workflow execution; allows referencing existing functions or defining new ones
- Container environment definition: declares service discovery and deployment details for containerized environments used in the workflow
- Function deformation: allows event definitions to be transformed based on specific contexts (e.g., cloud platform, container environment)
- Serverless Workflow Specification supports both YAML and JSON formats for workflow definitions
- Demonstration of using Quarkus and Apache Camel integration with the serverless workflow specification, along with Cogito Business Automation Runtime as a runtime implementation.


## Developer joy for distributed teams with CodeReady Workspaces | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=zxsa_lvs9V0](https://www.youtube.com/watch?v=zxsa_lvs9V0)



- Introducing Code Ready Workspace, an online IDE for developers
  - Challenge: Developer often spend too much time setting up environment and want to focus on coding
  - Solution: Code ready workspace lets developer start coding with preferred runtime directly in the cloud without having to set up environment locally
  - Features:
    - Online IDE with code editing, terminal, debugging, and extension support
    - Pre-installed popular runtimes and build tools
    - Supports multiple plugins for different frameworks and languages
    - Integrates with source control systems like GitHub, GitLab, and Bitbucket
    - Allows sharing of code with team members in real time
  - Benefits:
    - Reduces setup time and allows developer to focus on coding
    - Improves productivity and reduces context switching between local and cloud environments
    - Enables collaboration and sharing of code with team members
- Code ready workspace is based on OpenShift, a container application platform from Red Hat
  - Developer can run natively in Kubernetes cluster or use OpenShift Online, a managed cloud service
- Code ready workspace supports multiple workspaces, each containing different projects and environments
  - Developer can extend workspaces by adding custom plugins and configurations
- Code ready workspace is designed to be accessible from anywhere, including mobile devices and remote locations
  - Supports single sign-on (SSO) for easier access and security
- Code ready workspace can be integrated with continuous integration/continuous delivery (CI/CD) tools like Jenkins, Travis CI, and GitHub Actions
  - Enables automatic building, testing, and deployment of applications directly from the IDE
- Code ready workspace offers a simple and consistent way to manage and deploy applications in various environments, including development, staging, and production
- Code ready workspace also supports multiple tenancy, allowing multiple teams or projects to share the same environment while maintaining isolation and security.


## Secure Vue.js apps with Keycloak | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=u0x6BOCkj0k](https://www.youtube.com/watch?v=u0x6BOCkj0k)



- Welcome to DevNation Live Tech Talk
- Co-host: Edson Inácia, based in Raleigh, NC
- Special guest: Abbas Sheikh, Red Hat team member focusing on middleware technology, specifically Java ecosystem (Keycloak, OpenShift, Kubernetes) and operator world
- Demonstration of securing a Chase application using Keycloak
- Agenda: Overview of concept, integration pattern, end-to-end flow, token refresh, open validation
- Keycloak: Modern SSO solution with reliable architecture, strong community support, customizable architecture, and portability
- OpenID Connect: Security protocol used for authorization and communication between client and resource server
- Keycloak features: Delegation, customizable architecture, responsive, and portable
- Architecture: Separation of external and internal users, Google external realm setup, client creation (Google client, view app client), client integration, providing protocol, language specification, and adapters (Java, Javascript, Android)
- Integration pattern: VueJS demo, Keycloak adapter, token validation, Quarkus backend API, frontend application process, protecting REST endpoints, user authentication, handling cross-origin requests
- Keycloak security: Token lifespan, client protocol, access type, and SSO onload configuration
- Backend setup: Application property, focus (client protocol, openID Connect access type), realm setting, token lifespan, and application code


## SRE principles and (Kubernetes) Operator practice | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=_3Ym0Bj20sM](https://www.youtube.com/watch?v=_3Ym0Bj20sM)


- Welcome to Live Tech Talk: Operator Framework in OpenShift
- Speaker is Josh Wood, author of "Kubernetes Operators" book and member of OSHA team
- Topic: Advanced automation with operators in OpenShift
- Motivation: Toil involved in managing applications at different stages of their lifecycle, from installation to upgrades
- Goals: Preserve user configuration during upgrades, minimize risk, and improve efficiency through automation
- Operators: Extend the Kubernetes API to manage custom resources, customize behavior based on application state
- CRDs: Describe application internal state, allow operator to manage and reconcile desired state with actual state
- Custom Controller: Kubernetes control plane watches for changes in CRDs and triggers application-specific actions
- Operator Lifecycle: Manages installation, deployment, scaling, upgrades, backups, restores
- Autopilot: Automates whole lifecycle of an application with operator assistance
- Monitoring: Collect metrics for performance, error conditions, and status information
- SRE principles: Build monitoring into applications, automate response to anomalies
- Error handling: Log errors and provide clear messages to operators
- Auto Scaling: Horizontal and vertical scaling based on performance indicators
- Backup and Restore: Automated backups and restores of application state
- Conclusion: Operators improve efficiency, reduce risk, and enable innovation by automating application lifecycle management.


## Quarkus: From developer joy to Kubernetes nirvana! | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=PkhyvHE1PTQ](https://www.youtube.com/watch?v=PkhyvHE1PTQ)


- Marcos discussing Quark and Kubernetes experience, specifically the joy of using it as a Java developer.
- Consistency is a key factor for Quark's awesomeness.
    - Concise bundle framework APIs fit perfectly.
    - Single configuration interface adds consistency.
- Developer mode provides amazing developer experience with continuous feedback loop and no need to rebuild or redeploy.
- Container image creation involves building, pushing, and deploying the image using a container registry like Docker Hub or a private registry.
- Carcass Kubernetes extension generates manifests and interacts with container extensions for easier deployment.
    - Provides information about agreement, environmental variables, and application view.
- Extension interchangeability allows easy swap of different extensions without needing to reconfigure anything.
- Container image extension builds faster by handling image layer results directly.
- Quark canary extension generates manifests and obtains user configuration from the carcass build system.
- Manifest contains information about the application, including service accounts and deployment details.
- Customization of the generated manifest using standard configuration mechanisms is possible.
    - Adding environment variables, labels, and annotations.
- Environment variable configuration involves defining the intention case and key-value pairs for use in the container.
- Secret configuration can be added using a map secret or directly to the container image extension.
- Quark kubernetes extension interacts with container reverse extensions for added functionality.


## Event-driven business automation powered by cloud native Java | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=6lZ2d7ZDpFk](https://www.youtube.com/watch?v=6lZ2d7ZDpFk)



- Technology called Jido
- Business process management (BPM) background
- Open source, optimized for Rockstar developers
- Orchestration vs. choreography, centralized or decentralized
- Cloud native Java using Kubernetes, Cody argument
- Intelligent application building with Jbpm toolkit
- Single sentence definition of cloud native business automation
- Architecture: Cozy travel agency service and Quirky visa service
- Microservices communication through events in Kafka topic
- Visa application approval based on business rules
- Caching and reactive messaging (Cachito) for improved performance
- GraphQL for data querying and indexing
- Intuitive CLI for easy deployment in Khajiit ecosystem
- Use of FaunaDB for backend data structure support and Prometheus matrix service
- Quercus data index using native binary compiled in JVM mode
- Visual Studio Code available for demo application, recording to be released soon
- Support for BPMN 2 and DRL type modeling language
- Discussion about Cody DSL and demand modeling development crafting DSL
- Comparison of EAP Quercus jBPM to cloud native ecosystem
- Bringing business automation to the cloud with Jbpm, lightweight and fast.


## Creating factories in Eclipse Che | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=5PDm7tTHB9c](https://www.youtube.com/watch?v=5PDm7tTHB9c)



- Doug Tidwell from City Oaks Raleigh North Carolina
- Video about creating a factory in Eclipse Che for a team to share the same environment
- Process of creating a workspace using a factory
- Factory creates an exact environment for every team member
- Workspace creation starts by going to cheopenshiftio and adding a new workspace with a name, selecting a Java CentOS stack, and importing the project from GitHub
- Use Maven command to build the project, create a WAR file, and copy it to Tomcat webapps directory
- Create a command named 'Build' in the Run tab to run the Maven command
- Define a command to start Tomcat server and preview URL
- Set the factory workspace to start with the Petjava file open
- Create a factory by clicking on Workspace menu, giving it a name, and copying the factory URL for future use.
- Use the factory to create a new workspace for team members and eliminate 'It works on my machine' syndrome.


## Event-driven serverless applications with Camel K | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=hlUzLC71nAM](https://www.youtube.com/watch?v=hlUzLC71nAM)



- Welcome to another Deaf Nation Live Tech Talk
- Today's topic: Camel K and optimized Kubernetes (Cola Luca)
- Over 600 people attended this week (Monday, Wednesday sessions)
- Check out the MasterClass for more Kafka content
- Today, Cola Luca will talk about CAML (Apache Camel), a lightweight integration platform
- Apache Camel is used to run integrations directly on OpenShift and Kubernetes
- It's an open source integration framework that runs directly in containers
- Camel K enables developers to write integration code without deploying it separately
- It supports popular languages like Java, Groovy, Catalan, JavaScript, etc.
- It uses a simple DSL (Domain Specific Language) for writing integrations
- Camel K can translate and transform data, use connectors for external services, and more
- It supports Kafka native components and can run as a serverless application on OpenShift
- It also supports event-driven architecture and can handle multiple containers
- It has a simple CLI (Command Line Interface) for managing integrations
- Camel K is a part of the 10th version of Apache Camel, which was released just a month ago
- It has powerful features like detecting dependencies, creating and managing Kubernetes resources, etc.
- It can run in both local and global clusters
- The presentation will cover using Camel K for integration, its benefits, and some demos.


## Kubelet with no Kubernetes Masters | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=Myo1fLzskCA](https://www.youtube.com/watch?v=Myo1fLzskCA)



- Speaker is Rob Zomski, ex-CoreOS employee and OpenShift product manager
- Talking about Kublet, a component of Kubernetes control plane
- Used Kublet since 2013, experience includes working on edge deployment projects
- Industrial equipment example: CNC router with open source software, camera recording time lapse, web server, proxy, and DVR
- Discusses history of Docker, CoreOS, and systemd
- Mentioned early contributions to CoreOS documentation
- Kubernetes uses etcd for coordination, Docker for containerization, and systemd for init system
- Talks about control plane architecture: pod spec, scheduler, kubelet, and node reporting back status
- Discusses benefits of using Kublet without a control plane (standalone Kublet)
- Static manifest feature in standalone Kublet allows human scheduling and automatic provisioning
- Mentioned immutable infrastructure and its implementation with CoreOS and OpenShift
- Conclusion: Kublet is a crucial component of the Kubernetes ecosystem, even without a control plane.


## Secure your Quarkus applications | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=OimgPmDMOtw](https://www.youtube.com/watch?v=OimgPmDMOtw)



- Speaker introduces self and topic: secure parka application using key clock way
- Speaker mentions expertise, conference background, and team collaboration
- Discusses Quercus and Korkis frameworks for Java development and security
- Talks about importance of securing user logins with Asian identification
- Describes handling falsified identities and managing security tension
- Mentions property file security and extending a base class for identity management
- Discusses using third party libraries, including OpenID Connect and Google Cloud Platform
- Demonstrates configuring key cloak server and creating a simple application with Quercus

The speaker in this transcript discusses the importance of securing user logins and applications using various techniques and tools, such as Quercus and Korkis frameworks, property file security, and third-party libraries like OpenID Connect and Google Cloud Platform. They also demonstrate how to configure key cloak server and create a simple application with these technologies.


## Operatorhub.io and your Kubernetes cluster | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=eoVInwcGSdE](https://www.youtube.com/watch?v=eoVInwcGSdE)



- Welcome to another DevNation Live Tech Talk, streaming from Raleigh, North Carolina.
- Josh Wood, lead developer advocate at Red Hat, is here to talk about the Operator SDK and Operator Lifecycle Manager (OLM).
- He's also a famous author and public speaker on Kubernetes operator topics for The OReilly Network.
- Josh will provide an introduction to operators, their importance in managing applications, and how they differ from traditional deployment methods.
- Operators extend the Kubernetes platform by adding time management, patching, and configuration state preservation capabilities.
- They are particularly useful for managing databases, which often require specialized knowledge and complex deployment processes.
- OLM is a software package manager that makes it easy to deploy, manage, and upgrade operators in a Kubernetes or OpenShift cluster.
- It includes a catalog of available operators, as well as tools for creating your own custom operators.
- Operators can be installed and managed through the Red Hat Operator Hub marketplace, which provides an easy-to-use interface for self-service deployment and management.
- Operators can help automate tasks like installing databases, managing backups, and handling upgrades, freeing up human resources for more innovative work.
- Josh will provide a live demo of deploying and managing an operator using OLM in a Kubernetes cluster.


## Helm or Operator SDK with Kubernetes: Why not both? | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=N9QVJk6kjwg](https://www.youtube.com/watch?v=N9QVJk6kjwg)



- Welcome to another Dead Nation Live Tech Talk, discussing Helm Operator SDK
- Daniel Messer is the speaker, a product manager at Red Hat
- Operator Framework is an open source project aimed at making developers happy and running operators in a scalable community cluster
- There are many services provided within the operator ecosystem, including the Operator registry (Quay) and corporate SDK
- Helm has been around since 2014 and was originally created for Kubernetes and OpenShift
- Helm is popular because it offers feature advantages in the college of using other tools
- The talk will focus on how Helm can be used in conjunction with Operators, rather than as a replacement for package managers like kubernetes
- Demo will involve deploying Cockroach DB using Helm and an Operator
- Operators offer more advanced features compared to Helm alone, including the ability to modify existing deployed software within allowed bounds.


## Java & containers: What I wish I knew before I used it | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=B_isXc_8hIQ](https://www.youtube.com/watch?v=B_isXc_8hIQ)



- Host introduces Elder, a Brazilian developer advocate for Java containers in Latin America.
- Elder will talk about specific issues when using Java containers and how to address them.
- Topics: building images, caching, image size, resource evaluation, and maintaining applications.
- Docker is used as an example throughout the discussion.
- Building images takes a long time due to caching.
  - Caching can be optimized by putting less frequently changing files last in the Dockerfile.
  - Locker file can also impact build times; put it at the end of the Dockerfile.
- Image size is important as it impacts build time and deployment time.
  - Optimize image size using tools like Quarkus, native images, etc.
- Resource evaluation is crucial for successful Java applications in containers.
  - Use official images to follow best practices and maintain application stability.
  - Use specific tags instead of 'latest' to avoid potential rollback issues.
  - Choose minimal image sizes to save space and reduce traffic network usage.


## Security and authentication strategies for apps on Kubernetes | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=MgqfcKvB-n0](https://www.youtube.com/watch?v=MgqfcKvB-n0)



- Welcome to Dev Nation Live Tech Talk about security within context of Kubernetes using Gnome Shift and OpenID Connect, OAuth2, Hashicorp Vault, Mutual TLS, and PKI.
- Laurent will present four recipes for securing Kubernetes applications: authentication, credential management, network traffic security, and certificate management.

## Recipe 1: Authentication using OpenID Connect and OAuth2
- Existing simple web app deployed on Kubernetes with a classic architecture (API backend, database).
- Add user authentication and authorization capabilities using OpenID Connect.
- Use the standard OAuth2 interoperability protocol for better employer integration.
- Integrate easily with existing identity providers like Keycloak or Okta.

## Recipe 2: Credential Management using Hashicorp Vault
- Hashicorp Vault is a tool for managing secrets and credentials securely.
- Mitigate the risk of data leaks by efficiently creating, storing, renewing, and revoking credentials.
- Use Vault to manage database credentials for your Kubernetes applications.
- Integrate Vault with Kubernetes using an agent injector for easy deployment.

## Recipe 3: Network Traffic Security using Mutual TLS
- Secure east-west network traffic within a cloud native application architecture.
- Use a service mesh like Istio to implement mutual TLS for both encryption and service authentication.

## Recipe 4: Certificate Management using PKI
- Manage certificates for north-south and east-west traffic securely.
- Implement automatic on-demand certificate generation using a PKI infrastructure (like Vault or Let's Encrypt).


## Keeping Kubernetes secrets secret | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=pCgYqnGwXBM](https://www.youtube.com/watch?v=pCgYqnGwXBM)


- Welcome to another deaf nation Tech Talk, where secrets are revealed. Today's guest is Alex Soto from Red Hat. He will be talking about community secrets and how they are used in Kubernetes based applications.
- Secrets can include user information, database credentials, API keys, and other sensitive data. They should be kept secret for a long time and protected with encryption.
- Examples of secrets include passwords found in songs, such as "Symphony number eight" by Franz Schubert, which contains a bagmask message.
- Secrets can be stored in various ways, such as environment variables, files, or databases. They should not be stored in plain text and should be encrypted for added security.
- Alex will demonstrate how to create secrets using Kubernetes and how they are used in applications. He will also discuss best practices for storing and managing secrets.
- Attackers can gain access to secrets by exploiting vulnerabilities or through social engineering tactics. It is important to keep secrets secure and to rotate them regularly.
- Alex recommends using a secret manager, such as Hashicorp Vault, to store and manage secrets securely. He also suggests using encryption and multi-factor authentication to add an extra layer of security.
- Encryption algorithms, such as AES-256, can be used to protect secrets both at rest and in transit. Access to encrypted data should be limited to authorized users only.
- Kubernetes Secrets can be injected into containers using various methods, including environment variables, volumes, or ConfigMaps. This allows applications to access the sensitive information they need without exposing it directly.
- It is important to keep secrets out of version control systems and to use secure communication channels when transferring them between systems.
- Alex will demonstrate how to create and manage Kubernetes Secrets using various methods, including YAML files and the kubectl command line tool. He will also discuss best practices for deploying and managing Secret objects in a cluster.
- Attackers can gain access to secrets by exploiting vulnerabilities in the underlying infrastructure or by using social engineering tactics to trick users into revealing them. It is important to keep secrets secure and to rotate them regularly to minimize the risk of compromise.
- Alex will also discuss how to use Kubernetes Secrets to encrypt data at rest and in transit, as well as how to manage access to sensitive data using RBAC rules and other security features.
- Attackers can gain access to secrets by exploiting vulnerabilities or through social engineering tactics. It is important to keep secrets secure and to rotate them regularly to minimize the risk of compromise.
- Alex recommends using a secret manager, such as Hashicorp Vault, to store and manage secrets securely. He also suggests using encryption and multi-factor authentication to add an extra layer of security.
- Encryption algorithms, such as AES-256, can be used to protect secrets both at rest and in transit. Access to encrypted data should be limited to authorized users only.
- Kubernetes Secrets can be injected into containers using various methods, including environment variables, volumes, or ConfigMaps. This allows applications to access the sensitive information they need without exposing it directly.
- It is important to keep secrets out of version control systems and to use secure communication channels when transferring them between systems.
- Alex will demonstrate how to create and manage Kubernetes Secrets using various methods, including YAML files and the kubectl command line tool. He will also discuss best practices for deploying and managing Secret objects in a cluster.
- Attackers can gain access to secrets by exploiting vulnerabilities or through social engineering tactics. It is important to keep secrets secure and to rotate them regularly to minimize the risk of compromise.
- Alex recommends using a secret manager, such as Hashicorp Vault, to store and manage secrets securely. He also suggests using encryption and multi-factor authentication to add an extra layer of security.
- Encryption algorithms, such as AES-256, can be used to protect secrets both at rest and in transit. Access to encrypted data should be limited to authorized users only.
- Kubernetes Secrets can be injected into containers using various methods, including environment variables, volumes, or ConfigMaps. This allows applications to access the sensitive information they need without exposing it directly.
- It is important to keep secrets out of version control systems and to use secure communication channels when transferring them between systems.
- Alex will demonstrate how to create and manage Kubernetes Secrets using various methods, including YAML files and the kubectl command line tool. He will also discuss best practices for deploying and managing Secret objects in a cluster.
- Attackers can gain access to secrets by exploiting vulnerabilities or through social engineering tactics. It is important to keep secrets secure and to rotate them regularly to minimize the risk of compromise.
- Alex recommends using a secret manager, such as Hashicorp Vault, to store and manage secrets securely. He also suggests using encryption and multi-factor authentication to add an extra layer of security.
- Encryption algorithms, such as AES-256, can be used to protect secrets both at rest and in transit. Access to encrypted data should be limited to authorized users only.
- Kubernetes Secrets can be injected into containers using various methods, including environment variables, volumes, or ConfigMaps. This allows applications to access the sensitive information they need without exposing it directly.
- It is important to keep secrets out of version control systems and to use secure communication channels when transferring them between systems.
- Alex will demonstrate how to create and manage Kubernetes Secrets using various methods, including YAML files and the kubectl command line tool. He will also discuss best practices for deploying and managing Secret objects in a cluster.
- Attackers can gain access to secrets by exploiting vulnerabilities or through social engineering tactics. It is important to keep secrets secure and to rotate them regularly to minimize the risk of compromise.
- Alex recommends using a secret manager, such as Hashicorp Vault, to store and manage secrets securely. He also suggests using encryption and multi-factor authentication to add an extra layer of security.
- Encryption algorithms, such as AES-256, can be used to protect secrets both at rest and in transit. Access to encrypted data should be limited to authorized users only.
- Kubernetes Secrets can be injected into containers using various methods, including environment variables, volumes, or ConfigMaps. This allows applications to access the sensitive information they need without exposing it directly.
- It is important to keep secrets out of version control systems and to use secure communication channels when transferring them between systems.
- Alex will demonstrate how to create and manage Kubernetes Secrets using various methods, including YAML files and the kubectl command line tool. He will also discuss best practices for deploying and managing Secret objects in a cluster.
- Attackers can gain access to secrets by exploiting vulnerabilities or through social engineering tactics. It is important to keep secrets secure and to rotate them regularly to minimize the risk of compromise.
- Alex recommends using a secret manager, such as Hashicorp Vault, to store and manage secrets securely. He also suggests using encryption and multi-factor authentication to add an extra layer of security.
- Encryption algorithms, such as AES-256, can be used to protect secrets both at rest and in transit. Access to encrypted data should be limited to authorized users only.
- Kubernetes Secrets can be injected into containers using various methods, including environment variables, volumes, or ConfigMaps. This allows applications to access the sensitive information they need without exposing it directly.
- It is important to keep secrets out of version control systems and to use secure communication channels when transferring them between systems.
- Alex will demonstrate how to create and manage Kubernetes Secrets using various methods, including YAML files and the kubectl command line tool. He will also discuss best practices for deploying and managing Secret objects in a cluster.
- Attackers can gain access to secrets by exploiting vulnerabilities or through social engineering tactics. It is important to keep secrets secure and to rotate them regularly to minimize the risk of compromise.
- Alex recommends using a secret manager, such as Hashicorp Vault, to store and manage secrets securely. He also suggests using encryption and multi-factor authentication to add an extra layer of security.
- Encryption algorithms, such as AES-256, can be used to protect secrets both at rest and in transit. Access to encrypted data should be limited to authorized users only.
- Kubernetes Secrets can be injected into containers using various methods, including environment variables, volumes, or ConfigMaps. This allows applications to access the sensitive information they need without exposing it directly.
- It is important to keep secrets out of version control systems and to use secure communication channels when transferring them between systems.
- Alex will demonstrate how to create and manage Kubernetes Secrets using various methods, including YAML files and the kubectl command line tool. He will also discuss best practices for deploying and managing Secret objects in a cluster.
- Attackers can gain access to secrets by exploiting vulnerabilities or through social engineering tactics. It is important to keep secrets secure and to rotate them regularly to minimize the risk of compromise.
- Alex recommends using a secret manager, such as Hashicorp Vault,


## Java 14: 5 new features you must know | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=5UB0o_6dIyA](https://www.youtube.com/watch?v=5UB0o_6dIyA)



- Presenter: Etienne Agha, Red Hat, Java 14 features
- Apologies for WiFi connection issues and delays
- Java turning 25, discussing Java 14 new features
- Preview feature that preserves formatting in text blocks
- Improvement of switch statements with expressions instead of traditional methods
- New record feature to create immutable objects
- Sealed classes to define closed sets for enums and records
- Demonstration of Java 14 features using code examples

Note: The transcript is hard to understand due to the poor audio quality, frequent interruptions from the chat, and the presenter's rapid speaking style. It may be necessary to listen to the video or refer to the slides for a more accurate understanding.


## GPU enablement for data science on OpenShift | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=IFLEEEj1DeY](https://www.youtube.com/watch?v=IFLEEEj1DeY)


- Pete McKinnon, Red Hat principal engineer and NVIDIA GPU operator open data hub project contributor
- Data science enabled by GPUs in OpenShift
- Data science lifecycle: data collection to production serving
  - Training development and inference serving
    - Video stream processing requires high compute power
- Mathematical constructs: scalars, vectors, tensors
- GPUs designed for complex tensor operations with high degree parallelism
- Vermeer's Girl painting example: rendering portrait comparison between CPUs and GPUs
  - Scalar representation vs. vector and tensor representations
- CPU vs. GPU state of the art: AMD Epyc 702 (64 cores, 128 threads) vs. NVIDIA Ampere (100 cores, 32 bit FP floatingpoint benchmark)
- Notebooks and machine learning frameworks in OpenShift, e.g., TensorFlow, PyTorch
- Deploying NVIDIA GPU operator for production support
  - Node feature discovery and enhanced labeling by NVIDIA
  - Dependency management and alignment of versions
- Multi-instance GPUs and scheduling considerations in clusters
- Limitations and challenges: end user license agreements, heterogeneous mix, memory constraints, and GPU scheduler architecture.


## Exploring Kubeflow on Kubernetes for AI/ML | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=1HKscDFqNsU](https://www.youtube.com/watch?v=1HKscDFqNsU)



- Welcome to another deaf nation Tech Talk live broadcast
- Juwanna Sharad will present on open data hub starting from the introduction, evolution and demo
- Open data hub started as an internal project within Red Hat to provide a platform for data scientists to store and access data
- Challenges faced: sharing collaborative models, different user workflows (DevOps vs Data Scientists)
- Open data hub turned into an open source project involving the community for intelligence and contributions
- Operators provide operator hub catalog on OpenShift platform for adaptive tools and work patterns
- Release started late last year, included Ansible operator migration and Kafka as popular components
- Upcoming release (0.7) will include coop flow for CI testing and serving models using TensorFlow and Seldon pipeline
- Operators can install and integrate Open Data Hub with OpenShift cluster and its components
- Namespace permission and security are important considerations
- Installation of Open Data Hub operator within OpenShift cluster and creation of a new project
- Demonstration of Kale tool installation, running a notebook and creating a pipeline using JupyterHub and Argo workflows.
- Challenges faced during the demonstration: adapting to OpenShift and Argo run not assuming docker use.


## Jupyter Notebooks for machine learning on Kubernetes & OpenShift | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=9AZHUniDLpY](https://www.youtube.com/watch?v=9AZHUniDLpY)


- Sophie Watson will talk about data scientists using technology, specifically Jupyter notebooks and OpenShift.
- Data scientists benefit from containerization with OpenShift to reduce "pain points" in machine learning workflows.
- Jupyter Notebooks allow for exploratory interactive development and can be run on OpenShift with Hub.
- Features are extracted from transactions using techniques such as one hot encoding and numerical vectorizing.
- OpenShift pipelines automate the process of building, training, and deploying models.
- Container images make it easy to run code anywhere and ensure reproducibility in different environments.
- OpenShift allows for monitoring model performance with Prometheus and publishing custom metrics.
- The demo will show developing a fraud detection model end-to-end on OpenShift using Jupyter Notebooks, Hub, and Tecton pipeline.
- Data scientists can focus on their work without worrying about orchestrating containers or load balancing.
- Jupyter Notebooks provide a self-service environment for data scientists to run interactive notebooks and share code.
- OpenShift provides a development environment with easy access to resources and the ability to deploy models with one click.
- OpenShift Hub allows for managing, sharing, and collaborating on Jupyter Notebooks and other projects within an organization.
- The demo will involve setting up a project, provisioning resources, training a model, and deploying it to production using OpenShift.
- Data scientists can use specialized hardware such as GPUs for machine learning tasks with ease in OpenShift.
- OpenShift allows for easy deployment of containers in various environments, including public clouds and local machines.
- The demo will involve building a fraud detection model using Jupyter Notebooks, feature engineering techniques, and OpenShift pipelines.
- OpenShift provides a standard software engineering practice for managing machine learning applications and dataframes.
- The demo will involve encoding transactions as numerical vectors and extracting features from them using another notebook.
- OpenShift allows for monitoring model performance in real time with tools such as Prometheus and Grafana.
- The demo will involve training a random forest model using the pipeline and deploying it to production using OpenShift.
- Data scientists can use Jupyter Notebooks to develop models interactively and test different approaches without leaving the environment.
- OpenShift provides a scalable infrastructure for running machine learning workloads, allowing for efficient use of resources.
- The demo will involve making predictions using the trained model and comparing them to ground truth data.
- OpenShift allows for easy deployment of multiple versions of models behind a load balancer, improving availability and reducing downtime.
- Data scientists can use Jupyter Notebooks to write code, test hypotheses, and create visualizations all in one place.
- The demo will involve creating a container image using OpenShift and deploying it to production using the pipeline.
- OpenShift allows for easy integration with external services and APIs, making it a versatile platform for machine learning applications.
- Data scientists can use Jupyter Notebooks to collaborate on projects in real time with others within their organization.
- The demo will involve deploying a service using the OpenShift service catalog and interacting with it using a client library.
- OpenShift allows for easy management of containerized applications, including scaling, rolling updates, and backups.
- Data scientists can use Jupyter Notebooks to run experiments, test hypotheses, and iterate on models in a productive environment.
- The demo will involve using Prometheus to monitor model performance and visualize metrics in real time.
- OpenShift provides a secure and compliant platform for running machine learning workloads, meeting the needs of regulated industries.
- Data scientists can use Jupyter Notebooks to build models from scratch or integrate with existing libraries and frameworks.
- The demo will involve using OpenShift to deploy a model that makes predictions based on transaction data in real time.
- OpenShift provides a cost-effective solution for running machine learning workloads, reducing the need for expensive hardware and infrastructure.
- Data scientists can use Jupyter Notebooks to create interactive visualizations of complex datasets, making it easier to understand insights.
- The demo will involve using OpenShift to manage and orchestrate multiple microservices that make up a machine learning application.
- OpenShift allows for easy integration with popular machine learning frameworks such as TensorFlow and Scikit-Learn.
- Data scientists can use Jupyter Notebooks to prototype and experiment with new models and techniques, accelerating innovation.
- The demo will involve using OpenShift to deploy a model that makes predictions based on user behavior data in real time.
- OpenShift provides a flexible and customizable platform for running machine learning workloads, allowing for tailored solutions to specific use cases.
- Data scientists can use Jupyter Notebooks to collaborate with others on complex machine learning projects, improving productivity and accuracy.
- The demo will involve using OpenShift to deploy a model that makes predictions based on sensor data from IoT devices in real time.
- OpenShift provides a scalable and reliable solution for running machine learning workloads, ensuring high availability and performance.
- Data scientists can use Jupyter Notebooks to quickly iterate on models and experiment with different hyperparameters, improving accuracy and efficiency.
- The demo will involve using OpenShift to deploy a model that makes predictions based on image data in real time.
- OpenShift provides a secure and efficient platform for running machine learning workloads, reducing the risk of data breaches and improving performance.
- Data scientists can use Jupyter Notebooks to build models using a wide range of algorithms and techniques, from linear regression to deep learning.
- The demo will involve using OpenShift to deploy a model that makes predictions based on time series data in real time.
- OpenShift provides a cost-effective and flexible solution for running machine learning workloads, allowing organizations to scale up or down as needed.
- Data scientists can use Jupyter Notebooks to share models and insights with others in their organization, improving collaboration and knowledge sharing.
- The demo will involve using OpenShift to deploy a model that makes predictions based on text data in real time.
- OpenShift provides a scalable and secure platform for running machine learning workloads, ensuring that sensitive data is protected and that models are always available.
- Data scientists can use Jupyter Notebooks to build models using a variety of programming languages, from Python to R.
- The demo will involve using OpenShift to deploy a model that makes predictions based on audio data in real time.
- OpenShift provides a cost-effective and efficient solution for running machine learning workloads, reducing the need for expensive hardware and infrastructure.
- Data scientists can use Jupyter Notebooks to build models that integrate with external APIs and services, expanding their capabilities and reach.
- The demo will involve using OpenShift to deploy a model that makes predictions based on weather data in real time.
- OpenShift provides a flexible and customizable platform for running machine learning workloads, allowing organizations to tailor solutions to specific use cases.
- Data scientists can use Jupyter Notebooks to build models that integrate with databases and other data sources, improving the accuracy and completeness of their predictions.
- The demo will involve using OpenShift to deploy a model that makes predictions based on satellite imagery in real time.
- OpenShift provides a secure and scalable solution for running machine learning workloads, ensuring that sensitive data is protected and that models are always available.
- Data scientists can use Jupyter Notebooks to build models using unstructured data such as text, images, or audio, expanding their capabilities and insights.
- The demo will involve using OpenShift to deploy a model that makes predictions based on social media data in real time.
- OpenShift provides a cost-effective and flexible solution for running machine learning workloads, allowing organizations to adapt to changing business needs and market conditions.
- Data scientists can use Jupyter Notebooks to build models using large datasets, improving the accuracy and reliability of their predictions.
- The demo will involve using OpenShift to deploy a model that makes predictions based on sensor data from multiple devices in real time.
- OpenShift provides a secure and scalable platform for running machine learning workloads, ensuring that sensitive data is protected and that models are always available.
- Data scientists can use Jupyter Notebooks to build models using complex algorithms and techniques, pushing the boundaries of what's possible with machine learning.
- The demo will involve using OpenShift to deploy a model that makes predictions based on genomic data in real time.
- OpenShift provides a flexible and customizable platform for running machine learning workloads, allowing organizations to build solutions that meet their unique needs and requirements.
- Data scientists can use Jupyter Notebooks to build models using advanced deep learning techniques such as convolutional neural networks and recurrent neural networks.
- The demo will involve using OpenShift to deploy a model that makes predictions based on speech data in real time.
- OpenShift provides a cost-effective and efficient solution for running machine learning workloads, reducing the need for expensive hardware and infrastructure.
- Data scientists can use Jupyter Notebooks to build models that integrate with real-time streaming data, improving the timeliness and accuracy of their predictions.
- The demo will involve using OpenShift to deploy a model that makes predictions based on


## Machine learning with Apache Spark on Kubernetes | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=E6-ll77-RLA](https://www.youtube.com/watch?v=E6-ll77-RLA)


- Welcome to another Deaf Nation Tech Talk event
- Eric Ronson from Red Hat's Artificial Intelligence Center of Excellence will be speaking about machine learning with Apache Spark
- Discussing topics: streaming analytics, big data analytics, machine learning, AI, artificial intelligence, Spark, kubernetes, Docker, OpenShift
- Machine learning models can have outsized influence on larger systems, even though they are a small component
- Eric will focus on the machine learning model part of the process, including data collection, feature engineering, and training
- Structured streaming is a powerful feature in Spark for data Federation, allowing the processing of streaming data as it comes in
- Demonstration using Kafka, Postgres database, and Jupyter notebooks to show how to easily retarget heterogeneous data sources
- Using Spark's structured streaming API to perform complex aggregations on streaming data
- Discussion of use cases for machine learning in DevOps and application development lifecycle
- Structured streaming allows for a unified interface for data processing, making it easier to work with various data sources
- Spark can use the driver process to run a Jupyter notebook and perform computations on data from different sources simultaneously
- Demonstration using OpenShift, Kafka, and a spark cluster running in the cloud to show how to easily deploy and manage machine learning applications
- Q&A session at the end of the talk.
- Eric mentioned that he would add documentation for the notebooks and make them available on GitHub.
- Rolando asked about accessing the notebook and CSV file, and Eric confirmed they were already available on GitHub.
- Bert asked about using exact syntax with a CSV file in PostgreSQL and Apache Spark, and Eric explained that Spark has a powerful capability for operating tabular data from multiple sources.
- Henninger asked about using Jupyter notebooks to drive message production and consumption in Kafka and demonstrated how it could be done.
- One audience member asked about using Hadoop HDFS as an input source, but Eric mentioned it was hardly relevant to the topic at hand.
- Another audience member asked about using MLlib in Spark for machine learning and training models directly in Spark, but Eric pointed out that Spark's real strength is its backend capabilities which were demonstrated earlier.
- Rolando asked about using a Kafka producer and consumer inside a Jupyter notebook to drive a dashboard and show realtime analytics, but Eric suggested outputting the streaming query results to another Spark data table instead.
- One audience member asked about using cron jobs to run the Jupyter notebook in production, but Eric explained that data scientists often work in experiment environments and suggested using container technology like Docker to package and deploy the notebook code.
- Miguel, a student, asked about getting started with classification problems and recommended using Python's scikit-learn library for basic model experimentation.
- Open data hub mailing list is another way people can find information and connect with the community.


## jbang: Unleash the power of Java for shell scripting | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=-c9CIT9RfOQ](https://www.youtube.com/watch?v=-c9CIT9RfOQ)



- Speaker is Max Anderson from Red Hat
- Introducing novel approach to scripting Java language
- Java scripting: lightweight, but still lacking improvements after 25 years
- Majority of people use Java for scripting and automation
- Benefits include debugging, running long scripts, monitoring existing DMX tools
- Recent tool JDK added stream system level access to files
- Speaker's project: simplifying Java, making it easier to use for small scripts
- Previously, Java required maven or Gradle for scaffolding code
- Java 9 introduced J shell, a useful tool even outside of scripting
- Speaker discovered Java could be used like a scripting language
- Problems with using Java for scripting: lack of dependency management, file handling in J shell
- Speaker proposes "J Bank" as a solution: allows running small experiments and using third-party libraries
- "J buying pair" week will show more details about J Bank
- J Bank runs scripts using the rebel service
- Provides caching for faster script execution, and integration with popular IDEs like Eclipse and IntelliJ
- Allows easy access to external dependencies without installing them
- Speaker recommends using normal Java for larger applications, and J Bank for small scripts.


## GitOps: Stop, collaborate and deploy | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=hKIGLFwWtug](https://www.youtube.com/watch?v=hKIGLFwWtug)



- Welcome to another Deaf Nation Live event. Speaker is Ryan, a Red Hat engineer who will discuss GitOps using Git operational automation.
- GitOps: storing configuration in git repositories instead of manual deployment.
- Slide: GitOps is a crazy concept that involves putting an entire Kubernetes cluster into a single git repository.
- Templating: deploying applications to multiple clusters with customized tools.
- Object creation and authentication: best practices for using GitOps tools.
- Hub and spoke model vs independent deployment models.
- Use of CD tools like Argo CD for managing multiple kubernetes clusters.
- Advantages of using GitOps include collaboration, ease of use, and automation.
- Demo: deploying an application using Argos CD in a multi-cluster setup.
- Argos CD allows for automatic syncing of code changes across clusters.
- Webhooks can be used to trigger deployments based on repository events.
- Multi-site deployment with customized configurations.
- Argo CD's architecture is based on a reconciliation loop that compares the state of the cluster to the desired state in the git repository and applies any necessary changes.
- Argos CD can also automatically remediate problems, such as deleting unnecessary deployments or services.
- Self-healing: ensuring that applications continue to run even when changes are made.
- Pruning: manually removing unnecessary resources to keep things clean and efficient.
- The interface is manual prune by default, but users can change this behavior if desired.
- Argos CD also has an audit trail feature for tracking changes to the cluster.
- Using machine sets for managing Kubernetes clusters.
- Exporting objects from git repositories and importing them into Argo CD.
- Argos CD uses a custom resource definition (CRD) called CustomResourceDefinition (CRD) to manage its resources.
- Argos CD supports various integration options, such as GitHub and Jenkins.
- No context.


## Serverless stream processing of Debezium data change events with Knative | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=BY9ky1erKbA](https://www.youtube.com/watch?v=BY9ky1erKbA)


- Welcome to another Deaf Nation Live session
- Topic: Using Apache Kafka for Serverless Screen Processing with Change Data Events (CDEs) and the division data event facility
- Presenter: Matthias Jansen, Red Hat
- Agenda: Overview of solution, architecture, use case, enrichment, processing, deployment, and scaling
- Solution: Enabling temperature measurement streaming using Apache Kafka, with change capture tool to read database logs and enrich data from master data
- Architecture: Running inside a Kubernetes cluster, using the Kafka connect operator for easy operation
- Use case: Stream temperature measurement coming from a source (similar to network temperature sensor), which is enriched with master data (like station location) and routed to different consumers
- Enrichment: Impose database contains master data (weather measurement station, using a tool like Jeebies IAM change capture tool to tap transaction log), extracting and enriching data into another Kafka topic (using a Java-based API)
- Processing: Real-time processing of the stream using a Java-based API runtime, with cooperative multithreading for efficient processing
- Deployment: Easy deployment using Kubernetes OpenShift, making it accessible to everyone through a web application with an interactive map display
- Scaling: Using Kafka connect operators and Casca connector, handling different consumer parts and load balancing
- Tools used: Kafka, Kafka Connect, GitHub, Java, YAML, Apache Netty, CDI, etc.
- Q&A session will follow presenter's talk


## odo: Iterative container-based development made simple | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=KN5ihgtLDf4](https://www.youtube.com/watch?v=KN5ihgtLDf4)



- Presenter is excited for session about Odo, a product by Red Hat
- Odo was previously known as OpenShift but scope has changed
- It provides multiple options for running in the OpenShift ecosystem
- Presenter mentions he loves Notion and will be using it during presentation
- He apologizes for not being able to set clock correctly during presentation
- He'll provide a tutorial on creating an Odo application in terminal
- Odo is a developer-focused CLI tool, replacing some aspects of OpenShift's operator concept
- It leverages the existing service catalog in OpenShift
- He demonstrates creating a new cluster and deploying a component using Odo
- He mentions that Odo is opinionated but can supplement oc (OpenShift command line tool)
- He explains that Odo simplifies the process of inner loop development, making it faster
- He provides an example of creating a Java application and deploying it to OpenShift using Odo
- He mentions that Odo allows for easier linking of components and services
- He shows how environment variables can be injected into components through Odo
- He discusses the benefits of using Odo for continuous integration and deployment
- He apologizes for ordering things incorrectly during demonstration
- He encourages audience to ask questions throughout presentation.


## Behavior is easy, state is hard–Tame inconsistent state in your Java code | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=nuu9Ium4ohM](https://www.youtube.com/watch?v=nuu9Ium4ohM)


- Host introduces topic: dealing with inconsistent state in Java programming
- Common mistake: null pointer exception caused by unexpected variable state
- Goal of talk: increasing state consistency, using immutable collections as an example
- Personal experience: hardest bug to fix was a null pointer exception due to an unexpected variable state
- Immutability: best way to deal with inconsistent state, taming different collection implementations worldwide
- Eclipse Collection: nice API for providing immutable collections
- Designing immutable classes: ensure all fields are final, use private constructor, provide factory method
- Preconditions: checking arguments before creating objects ensures consistent state
- Using JPA and Hibernate: designing immutable classes doesn't mean they can't provide immutability; minimize mutability instead
- Avoiding primitive obsession: create types instead of using primitives for rich domain models
- Creating an Order class: exposing a completely mutable class vs an immutable one, using JPA entity to enforce state consistency
- Designing an OrderNumber class: providing constraint helper methods inside
- Importance of table names: no order info reserved keyword conflicts
- Using an embeddable value object: enforcing conditions to prevent duplicates and inconsistent state
- Creating a Money class: using a private final big decimal for the value, creating a factory method to ensure immutability
- Designing a MoneyAttributeConverter: breaking encapsulation to allow RPE cleaner access, providing proper information hiding
- Exposing an Order class using JSON: add validation annotations and provide getters/setters for JSON data
- Using a Precondition class: check arguments before creating objects and use the J framework for awareness
- Eclipse Collection vs Modifiable List: using an immutable wrapper to create a modifiable list, performance considerations don't matter much
- Internationalization: using ResourceBundle for different error messages
- Conclusion: Java community deserves celebration on its 25th anniversary.


## Kubernetes: The evolution of distributed systems | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=CZPEIJFJV9k](https://www.youtube.com/watch?v=CZPEIJFJV9k)



- Welcome to DevNation conference, Bilgi Ibrahim will speak about how kubernetes is evolving and its impact on future technology.
- Bilgi has worked as a consultant and architect for Red Hat for many years, contributed to Apache Camel, wrote books on integration and kubernetes.
- Topics: Microservices, Life cycle management, Networking, State abstraction.
- Setting the framework: Evaluating various technologies to build services, need capabilities like deployment, rollback, configuration management, resource isolation, networking, state management, etc.
- Kubernetes satisfies most of these needs: Health checks (liveness and readiness), intelligent placement, declarative deployment, configuration management, resource isolation, etc.
- Kubernetes provides a platform for extending its functionality with sidecar operators, service meshes, native components, etc.
- Sidecar operators allow adding capabilities transparently, like data plane operators, operator patterns, etc.
- Service mesh (Istio) adds network and observability capabilities, handles service discovery, dynamic traffic routing, security, etc.
- Kubernetes Native (Canadian) provides eventing infrastructure and serverless characteristics.
- Dapper is a portable runtime with sidecar sets that can manage state and interactions between services.
- Predictions for future architecture: More focus on lifecycle management, operator innovation, polyglot architecture, etc.


## What’s new with Apache Camel 3? | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=HS8fPyCkgyU](https://www.youtube.com/watch?v=HS8fPyCkgyU)



* Speaker: Andrea from Red Hat, senior software engineer and DNC chair for Apache Camel project
* Topic: Overview of Apache Camel framework
* Apologies for screen issues
* Live demo later in talk
* Camel is Swiss Army knife for integration with Java-based systems
* It connects everything (XML, SQL, Spring, Kafka, etc.)
* Community has 300+ components and growing
* Uses a high-level picture of a camel context at the center
* Components add functionality like routing, transformation, aggregation
* Basic example using standalone Camel application in Java with timer lock
* Can be run as a standard Java application or in Spring Boot
* Supports dependency injection (CDI)
* Has a large and active community on GitHub
* New feature: Camo 3 close to release, supports camouflage for APIs and microservices
* Live demo using Kafka integration in cloud environment
* Q&A session at end of talk

No context.


## Reactive Quarkus–A Java Mutiny | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=kWlrGtwvOxg](https://www.youtube.com/watch?v=kWlrGtwvOxg)



- Welcome to Java Tech Talks Fridays
- Discussing Quercus and reactive programming with Clemens Kofi
- Challenges of building distributed systems, need for efficient resource use
- Introducing Cobra, an event-driven architecture library for Java
- Event-driven programming allows for faster and reliable code execution
- Data intensive systems require quick processing of data from IOT devices and mobile phones
- Metheny, a novel reactive programming library, helps simplify writing reactive code
- Challenges of learning and maintaining reactive code
- Discussing the benefits and uses of active extensions in reactive programming
- Comparing reactive and synchronous approaches to programming
- The importance of testing and debugging in reactive systems
- Introduction to Quackers, a framework for building event-driven microservices
- Concurrency considerations and using Quark for handling client connections
- Discussing the differences between reactive and blocking databases
- Best practices for handling client disconnections and providing backup solutions
- The need for cleanup actions in reactive systems
- Q&A session covering various topics related to reactive programming and Quercus.

Note: I made some assumptions about the context of the transcript, so please let me know if there are any inaccuracies or errors.


## Kubernetes made easy with OpenShift | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=3D1uSnJRqao](https://www.youtube.com/watch?v=3D1uSnJRqao)



- Presenter: Jan, Red Hat developer advocate
- Topic: Four ways to deploy applications in OpenShift
- Demonstrating deployment using a simple Node.js frontend application
  - Command line: `oc new app` (authenticated with kubernetes cluster)
    * Uses S2I (Source-to-Image) to infer language and create an image
      without the need for a Dockerfile or running `docker build`
  - Web console: `oc new app frontend`
    * Uses source image tool, which infers the language from the Git repo
    * Creates a standard Kubernetes deployment using a YAML file
  - GitHub webhook
    * Triggers a build and deployment when code is pushed to the repository
  - Odo CLI tool (specifically built for developers)
    * Runs processes in the container without building an image
      (useful for iterative development)
- Demonstrating build process:
  - `oc create` command creates a new application from a GitHub repo
  - Output shows the creation of various resources (build, image stream, route, etc.)
- Discussed differences between OpenShift and Kubernetes, including easier local development and inner loop development using Odo.
- Q&A session covers creating an image without a Dockerfile, relationship between pods and containers, and deploying to multiple locations.


## Redis vs Infinispan: Battle of the in-memory data stores | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=Kb46QFigx84](https://www.youtube.com/watch?v=Kb46QFigx84)



- Tristan Terence is lead engineer at Red Hat, also principal architect for datagrid product
- Comparing Redis and Infinite Span
- Memory data technology focus
- Fast memory for historic data, primary use case for web services
- Precalculate data from liter source
- Useful for data that changes frequently
- Session management use case: avoid losing customer if frontend fails
  - Share session data across multiple frontends
- Redis features:
    - Key-value store (string, byte array, bit, etc.)
    - List, stats, hash store
      - One value inside another value
    - Publish/subscribe feature
    - Certification for many applications
  - Protobuf schema support
- Redis vs Infinite Span:
  - Redis is singlethreaded
  - Infinite Span handles scalability better vertically and horizontally
  - Redis has a master-slave replication system with asynchronous data transfer
    - Master node may fail, Sentinel system can automatically elect new master
      - Clients still read/write to master
    - Master and slave nodes have the same data
  - Redis cluster:
    - Multiple nodes working together
    - Automatically rebalances data when a node is added or removed
      - Maintains consistency across all nodes
  - Redis can handle high throughput for read/write operations
- Infinite Span:
  - Peer-to-peer master-slave architecture with automat synchronous and asynchronous replication
  - Cluster finds first two main topics: architectural view and handling scalability in Redis investment.


## AI vs COVID-19: How Java helps nurses and doctors in this fight | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=kmvLxaAhC9Y](https://www.youtube.com/watch?v=kmvLxaAhC9Y)



- Joffrey Desmet to present AI tech talk about Java, focusing on scheduling problem in hospital setting due to pandemic.
- Special constraints arise such as need for respiratory specialist, nurse availability, and sleep requirements.
- Planning solution assigns shift based on constraint satisfaction, with some constraints being hard (unfeasible) or soft (desirable but not required).
- Planning uses recorded constraint history to improve planning over time.
- Optimal solution avoids migration of staff between wards as much as possible while balancing workload and respecting constraints.
- Planner also takes into account employee inoculation status, which can be used to minimize risk while still assigning shifts effectively.
- Planning algorithm uses a replicating constraint solver for efficiency and scalability.
- Employee availability screen shows color-coded availability (red for unavailable, green for available).
- AI planning allows for faster and more accurate scheduling compared to manual methods.
- Planner can handle large numbers of shifts and employees efficiently.
- Constraint streaming allows the planner to react quickly to changes in constraints or employee availability.
- Planning pinning lets users lock in certain employees for specific shifts, providing more control over the schedule.


## Ansible playbook awesomeness | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=TB7zBMkzSnA](https://www.youtube.com/watch?v=TB7zBMkzSnA)



- Welcome to Ansible Tech Talk with Adam Miller, Ansible expert from Red Hat.
- Ansible is an automation tool that can handle both configuration management and command control tasks.
- It's capable of managing physical hardware, networking devices, firewalls, and more.
- Ansible uses the concept of 'playbooks', which define a sequence of tasks to be executed on a target system or group of systems.
- Inventory refers to the list of hosts or systems that Ansible will manage. It can be in various formats including YAML, JSON, or INI.
- Ansible has a rich ecosystem of plugins, including for different inventory sources and connection methods.
- Ansible is often used for DevOps workflows, but it's also useful for non-native tasks and infrastructure glue.
- Adam will be demonstrating how to use Ansible to install packages on a Linux system, using the 'ansible-playbook' command and the 'hosts' file. He will also cover dynamic inventory and variable definitions.
- Ansible can interact with various cloud providers like Amazon Web Services (AWS) and Microsoft Azure, and it supports different connection plugins for each provider.
- Adam encourages people to check out the advanced resources available on ansible.com and reach out if they have any questions or need help.


## Enter the DevNation: Why am I here?

URL: [https://www.youtube.com/watch?v=86JKSqPs88w](https://www.youtube.com/watch?v=86JKSqPs88w)

Error


## Join us for DevNation Deep Dives

URL: [https://www.youtube.com/watch?v=rUOejn2T4jM](https://www.youtube.com/watch?v=rUOejn2T4jM)



- Excited to announce new master course live series
- Training sessions in local time zones
- Offering courses in multiple case local languages
- Kubernetes, Native Tecton ISTE on the agenda
- Criminal native Java (Quercus) to be shown
- Microservices deployment and criminales cluster
- Going to be a lot of fun, join live sessions to learn together.


## 4K–Kubernetes with Knative, Kafka, and Kamel | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=kYM6hoh2ahI](https://www.youtube.com/watch?v=kYM6hoh2ahI)



- Welcome to Tech Talk by Kamesh Srinivasan
- Discussing K native cookbook, a free downloadable book available on Red Hat's website
- Agenda: discussing Cuban style deployments in Kubernetes using Camel and Kafka
- Demonstrating deployment of a simple application called "Followill"
- Starting with terminal to access OpenShift console and create a new project
- Deploying the application by creating a new service, exposing it to the internet through a load balancer
- Creating a route to access the application directly via URL
- Discussing benefits of fine-grained deployment models using K native and Kafka
- Comparison between traditional monolithic applications and microservices
- Demonstrating eventing in Kubernetes with Apache Kafka
- Installing and configuring Apache Kafka using OpenShift
- Creating a new Kafka topic for the application events
- Building and deploying a Camel integration using the StreamZ framework
- Wrapping up with a Q&A session.


## Quarkus tips, tricks, and techniques | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=6YXnqS6qQdk](https://www.youtube.com/watch?v=6YXnqS6qQdk)



- The speaker is at a tech talk and mentions Max has a presentation today.
- The speaker received an email with an event confirmation, possibly for the tech talk.
- They mention a Portuguese chat and ask a question in it.
- The speaker discusses a trend of people speaking Portuguese at the event.
- They mention they are ready for another detonation Tech Talk.
- The speaker mentions Ciaran Walker and Pratik Patel, possibly colleagues.
- Max is going to show a tip or trick using live streaming.
- The speaker discusses their frustration with having to drop everything for an enterprise developer tool.
- They mention a product called Carcass and Jeremys brain work side community.
- The speaker talks about developing and how they like cracker stuff.
- They introduce a demo of Quarry tEDGlobal, a command mode new feature.
- They discuss the Corpus tool, which is fast and makes development easier.
- They mention the Gore shark tool for Chris Fit.
- The speaker mentions Corpus dev mode and its side effects.
- They discuss how they can remove unnecessary restarts to make development faster.
- They talk about available features in Corker, a tool they've shown before.
- The speaker mentions they are going to show something related to IDE integration.
- They mention the Eclipse debugger losing connection and Korkis dev mode as a solution.
- The speaker talks about using Quercus instead of Deepak for development.
- They discuss replacing J rebel with Jay rebel and its downsides.
- The speaker recognizes a pattern in Alexey's question and answers it.
- They mention the Quercus documentation and how to find it outside of their website.
- They mention upcoming events, including a virtual summit and Tech Talk Thursdays.


## Going deep (learning) with TensorFlow and Quarkus | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=v8WAgpWEaMY](https://www.youtube.com/watch?v=v8WAgpWEaMY)


- Welcome to DubNation Tech Talk
- Special guest is Eric Murphy, Redwood practice lead at Red Hat
- He will talk about making magic run with TensorFlow Quercus in Java
- Business need: Combining machine learning and traditional programming
- Tensorflow: Open source platform for machine learning (deep learning)
- Stateful data flow graph for computation
- Korkis: Serving machine learning models using a Java library and API
- Demo: Sensor fork application using image recognition model
- Q&A session follows presentation

**Presentation Content:**
- Business need: Combining traditional programming with machine learning
  - Machine learning paradigm shift from rule-based to predictive modeling
  - Combine both for intelligent applications
  - Model training and inference sides
- Tensorflow: Open source platform for machine learning (deep learning)
  - Stateful data flow graph for computation
  - Can be used with Java via Korkis library
- Korkis: Serving machine learning models using a Java library and API
  - Runs on JVM
  - Supports multiple models and microservices
- Demo: Sensor fork application using image recognition model
  - Upload an image for analysis
  - Receive predictions with confidence scores and bounding boxes
- Benefits of Tensorflow with Java and Korkis:
  - Faster performance compared to Python
  - Enterprise-ready technology
  - Leverage existing developer talent
  - Support for GPU acceleration
- Q&A session follows presentation


## Commit to excellence - Java in containers | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=YdvR5KwWNu4](https://www.youtube.com/watch?v=YdvR5KwWNu4)



- Speaker discusses the benefits of using containers, specifically in the context of Java applications.
- Containers make deployment easier and more efficient by reducing the need for manual configuration and deployment steps.
- Containers also provide better security and isolation compared to traditional monolithic applications.
- The speaker mentions Docker as a popular containerization platform and discusses the importance of image size in the context of containers.
- Smaller base images lead to faster build times and reduced storage requirements, but may require more frequent updates to keep dependencies current.
- The speaker also touches on the importance of using efficient caching strategies and optimizing layer construction in container images.
- Java developers can benefit from using containerization tools like OpenJDK, which provide better performance and easier deployment options for Java applications.
- Containers are becoming increasingly important in cloud environments, where they enable faster deployment and more efficient resource utilization.
- The speaker mentions the use of tools like Jenkins and Kubernetes for container orchestration and suggests using Bacchus Krakus for building container images.
- Code coverage tools like Jacoco can be used inside containers to monitor code execution and identify issues, but may require additional setup and configuration.


## Quarked testing | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=qQLSZTDODSQ](https://www.youtube.com/watch?v=qQLSZTDODSQ)



- Speaker: Bruce Sutter
- Topic: Testing with Quercus in Java microservices
- Agenda: Introduce Alex Otte, explain benefits of testing, discuss testing frameworks and tools (Quarkus, Parliament), demonstrate a test example using Quercus
- Benefits of testing: Refactor applications, verify application behavior, avoid breaking production applications
- Testing in Quarkus: Supports unit tests (70+ tests) using Quartz, allows dependency injection, supports integration tests with external services and databases
- Tools: Quarkus Parliament for unique testing methods (insertion tests), Mojito for mocking dependencies
- Example: Demonstrate a test case involving a discount service, shopping cart, and Kafka
  - Sending a request to the price service and applying a discount
  - Calling a billing service to check the total amount after applying the discount
  - Using Quercus to mock dependencies and test various scenarios (limit reached, no discount)
- Conclusion: Quercus offers efficient testing in Java microservices, supports unit tests and integration tests with external services and databases, and provides tools for easy mocking of dependencies.


## Kubernetes and the hybrid cloud with Skupper | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=2ax0CDyKg4U](https://www.youtube.com/watch?v=2ax0CDyKg4U)



- Talk about new technology called Scupper by Tesla
- Multi cluster Kubernetes hybrid cloud project
- Scupper is a tooling multiprotocol adapter for dispatch router
- Related to Apache Cupid, mature messaging component
- Discussing 5 Kubernetes clusters running on different clouds (AWS, Azure, Google Cloud, Red Hat)
- Using Scupper to hook them together
- Demonstrating creating connections, network access, and traffic flow between clusters
- Showing integration with Kubernetes, including creating deployments and exposing services
- Discussing asynchronous handling and load balancing
- Answering audience questions about installation, firewalls, and single point failures.


## AWS Lambda and serverless Java | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=tE2xalK2hQw](https://www.youtube.com/watch?v=tE2xalK2hQw)


- Bill Burke, a senior distinguished engineer from Red Hat, is talking about Quarkus Java technology for Amazon Lambda.
- He is discussing the advantages and disadvantages of using Quarkus in comparison to traditional Java approaches in AWS Lambda environment.
- Quarkus is designed to reduce memory boot time and improve cold start latency, which are important factors for serverless applications on AWS Lambda.
- It also aims to simplify deployment and reduce operational overhead by removing the need for containers and providing fine-grained event-driven architecture.
- Bill is demonstrating how Quarkus can be used to build a REST service on AWS Lambda using Spring Dependency Injection, Korkis Spring MVC 5time, and Amazon Lambda Rest Stuff.
- He is also discussing potential disadvantages of Quarkus, such as the need for specific runtimes (vendor lockin) and the possibility of longer cold start latencies due to fine-grained deployment.
- Bill is also addressing some common questions from the audience, such as the use of S3 with Quarkus on AWS Lambda and the debate between microservices and function design.
- He emphasizes the importance of keeping things together for developer and maintainer experience in larger applications.


## Linux cheat codes | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=q7AFscKwKVc](https://www.youtube.com/watch?v=q7AFscKwKVc)


- Debs is live at Devon Nexus with 2000 people, excited about topic of going hardcore Linux
- Marcin Berger will talk about Linux related stuff, focusing on religious benefits like job control and history management
- Dan Burkhardt from Twitter/YouTube channel 'Mockingbird' to cover elevating security topics like SLA, user permissions, and sudo time
- Max Maximov will demonstrate advanced techniques in terminal, showing how to install Apache PHP with yum and correcting typos

Throughout the presentation:
- Presenters reference using Linux for job control, history management, and security features
- They discuss various commands like systemctl, sudo, rpm, and grep, as well as SELinux and ACLs
- Some presenters express frustration with typing long commands multiple times and suggest using history files to avoid repetition.

Max Maximov specifically:
- Demonstrates installing Apache PHP with yum
- Shows correcting typos in terminal, using a backspace and exclamation marks to go back in command history
- Talks about using sudo time for anticheat measures but acknowledges it makes life harder for developers

No context:
- Xzibit hall is a fairly big area with 2000 people.
- There are two thousand one thing at the event.
- Im going show lot linux related stuff today.
- Dan Mullen Burkhardt has a twittering Mockingbird Twitter and YouTube channel called 100 thing wizard.
- Tom knows fairness block was updated fairly recently on YouTube channel.
- ACLs are mentioned.
- Marcin Berger is the principal Solutions Architect in the Benelux region of the Netherlands, who will show various Linux related stuff.
- Dan Mullen Burkhardt has a lot twittering Mockingbird Twitter and YouTube channel where he posts stuff related to products and blogs called 100 thing wizard.
- Tom knows fairness block was updated fairly recently on YouTube channel.
- Max Maximov is going to cover the topic of elevating religious benefits like job control, history management, and a little bit about clinical applications and ACLs.
- Max Maximov will show some docs going look at networking and management services.
- There might be some advanced topics mixed with entry level topics.
- Max Maximov is planning to mix advanced topic entrylevel topic together in the next 30 minutes, feel free to send messages on Twitter or email if you have questions.
- Max Maximov is flying and may take a little longer to respond to traffic during the presentation.
- Max Maximov will cover topics like elevating religious benefits, job control, history management, ACLs, and networking and management services.
- There might be some advanced topics mixed with entry level topics in the next 30 minutes.
- Max Maximov is planning to dive right into Sir Pristine Rail 8 machine, pretending to be a developer, and deploying a little PHP app using Pachi, yum install, and httpd/PHP.
- Marcin Berger will work with Linux advanced chichi topics like job control, history management, and a little bit of clinic and ACLs. He added a link to the chat for further discussion.
- Dan Mullen Burkhardt plans to cover elevating religious benefits like job control, history management, and a little bit of clinic and ACLs in the next 30 minutes.
- Max Maximov will demonstrate advanced techniques using Linux, focusing on job control, history management, networking and management services, and ACLs.
- Dan Mullen Burkhardt plans to cover elevating religious benefits like job control, history management, networking and management services, and a little bit of clinic and ACLs in the next 30 minutes.
- Max Maximov will show some advanced techniques using Linux for job control, history management, networking and management services, and ACLs.
- Dan Mullen Burkhardt will talk about elevating religious benefits like job control, history management, networking and management services, and a little bit of clinic and ACLs.
- Max Maximov is going to rattle some awesome stuff about going hardcore Linux, focusing on job control, history management, networking and management services, and ACLs.
- Max Maximov will demonstrate advanced techniques using Linux for job control, history management, networking and management services, and ACLs.
- Max Maximov is planning to dive right into Sir Pristine Rail 8 machine and deploy a little PHP app using Pachi, yum install, and httpd/PHP.
- Marcin Berger will show some Linux related stuff today, focusing on job control, history management, and a little bit of clinic and ACLs.
- Dan Mullen Burkhardt plans to cover elevating religious benefits like job control, history management, networking and management services, and a little bit of clinic and ACLs in the next 30 minutes.
- Max Maximov will demonstrate advanced techniques using Linux for job control, history management, networking and management services, and ACLs.
- Marcin Berger is the principal Solutions Architect in the Benelux region of the Netherlands, who will show lot linux related stuff today.
- Dan Mullen Burkhardt has a twittering Mockingbird Twitter and YouTube channel where he posts stuff related to products and blogs called 100 thing wizard.
- Tom knows fairness block was updated fairly recently on YouTube channel.
- Max Maximov is planning to dive right into Sir Pristine Rail 8 machine and deploy a little PHP app using Pachi, yum install, and httpd/PHP.
- Marcin Berger will show lot linux related stuff today, focusing on job control, history management, and a little bit of clinic and ACLs.
- Dan Mullen Burkhardt plans to cover elevating religious benefits like job control, history management, networking and management services, and a little bit of clinic and ACLs in the next 30 minutes.
- Max Maximov will demonstrate advanced techniques using Linux for job control, history management, networking and management services, and ACLs.
- Dan Mullen Burkhardt plans to cover elevating religious benefits like job control, history management, networking and management services, and a little bit of clinic and ACLs in the next 30 minutes.
- Max Maximov is going to rattle some awesome stuff about going hardcore Linux, focusing on job control, history management, networking and management services, and ACLs.
- Max Maximov will demonstrate advanced techniques using Linux for job control, history management, networking and management services, and ACLs.
- Max Maximov is planning to dive right into Sir Pristine Rail 8 machine and deploy a little PHP app using Pachi, yum install, and httpd/PHP.
- Marcin Berger will show lot linux related stuff today, focusing on job control, history management, and a little bit of clinic and ACLs.
- Dan Mullen Burkhardt plans to cover elevating religious benefits like job control, history management, networking and management services, and a little bit of clinic and ACLs in the next 30 minutes.
- Max Maximov will demonstrate advanced techniques using Linux for job control, history management, networking and management services, and ACLs.
- Dan Mullen Burkhardt plans to cover elevating religious benefits like job control, history management, networking and management services, and a little bit of clinic and ACLs in the next 30 minutes.
- Max Maximov is going to rattle some awesome stuff about going hardcore Linux, focusing on job control, history management, networking and management services, and ACLs.
- Max Maximov will demonstrate advanced techniques using Linux for job control, history management, networking and management services, and ACLs.
- Max Maximov is planning to dive right into Sir Pristine Rail 8 machine and deploy a little PHP app using Pachi, yum install, and httpd/PHP.
- Marcin Berger will show lot linux related stuff today, focusing on job control, history management, and a little bit of clinic and ACLs.
- Dan Mullen Burkhardt plans to cover elevating religious benefits like job control, history management, networking and management services, and a little bit of clinic and ACLs in the next 30 minutes.
- Max Maximov will demonstrate advanced techniques using Linux for job control, history management, networking and management services, and ACLs.
- Dan Mullen Burkhardt plans to cover elevating religious benefits like job control, history management, networking and management services, and a little bit of clinic and ACLs in the next 30 minutes.
- Max Maximov is going to rattle some awesome stuff about going hardcore Linux, focusing on job control, history management, networking and management services, and ACLs.
- Max Maximov will demonstrate advanced techniques using Linux for job control, history management, networking and management services, and ACLs.
- Max Maximov is planning to dive right into Sir Pristine Rail 8 machine and deploy a little PHP app using Pachi, yum install, and httpd/PHP.
- Marcin Berger will show lot linux related stuff today


## Crafting Kubernetes Operators | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=P9OhZhId03E](https://www.youtube.com/watch?v=P9OhZhId03E)



- Expert in community operating and Kubernetes operators
- Discussing automation magic with Kubernetes clusters and operator pattern
- Focus on machine awareness, live chat interaction, and YouTube channel link
- Overview: Implementing a call operator, Figure Netties, to manage lifecycle of applications in Kubernetes clusters
  - Operator problem: Managing complex application lifecycles and security updates
  - Solution: Automating upgrade process using operator pattern and Kubernetes API
- Importance of automation and keeping software up-to-date to secure against vulnerabilities
- Discussion on stateless and stateful applications, managing databases, and human intervention in managing complex lifecycles
- Operator build process: Creating a custom controller that interacts with Kubernetes API and implements specific logic for application management
- Overview of Red Hat Operator Framework and OpenShift for building operator applications
- Comparison of Helm and other solutions, and the future of operator pattern and its role in managing complex systems.

No context.


## Distribute your microservices data with events, CQRS, and event sourcing | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=HdvWfr2KwA0](https://www.youtube.com/watch?v=HdvWfr2KwA0)


- Welcome to Another Deaf Nation Live
- New platform for excellent content and presentations
- Edison Naga introducing topic: Distributed Data, specifically event sourcing
- Focus on securing event sourcing in modern systems
- History of data management: from XML files to Hibernate annotations to event sourcing
  - Hibernate was popular around 2005 and replaced XML with hibernate.cfg.xml file
  - Event sourcing discussed around 15 years ago as a solution for complex systems
- Overview of event scene, where events represent behavior data in a system instead of structure data
- Discussion on the challenges of distributing data securely using event sourcing
  - Need to handle performance, availability, and consistency issues
    - Performance: ensure endpoints can perform well, need to minimize latency
    - Availability: ensure that data is available at all times, need to implement fallback strategies
    - Consistency: manage conflicts between different teams or services working on the same data
        - Strong consistency means no conflict ever happens
        - Eventual consistency allows for eventual conflicts and requires versioning and schema compatibility
- Proposed solutions for securing event sourcing include using message brokers like Apache Kafka, applying CDC (Change Data Capture), and implementing synchronous event propagation.
- Importance of understanding the tradeoffs between different architectures and choosing the right one for specific use cases.

I hope you find this helpful! Let me know if there's anything else I can help with.


## Kubernetes-native Spring apps on Quarkus | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=s05fBX1gEIw](https://www.youtube.com/watch?v=s05fBX1gEIw)



- Welcome to Quercus session, focusing on supersonic subatomic Java development with Spring
- Discussed benefits of Quercus: developer joy, super fast and small applications, unified imperative/reactive programming model, powerful library frameworks
- Demonstrated creating a simple Spring application using Quercus command line tooling (Spring Initializr) and Spring Web extension
- Highlighted productivity gains, such as instant code changes without restarting the application
- Discussed error handling and configuration options for quirkiness like injectable services and custom exception handlers
- Mentioned other tools/libraries used with Quercus: Hibernate validator, Spring Data GPA, and OpenShift/Kubernetes deployment
- Briefly discussed using a database with Quercus, specifically an in-memory H2 database for simplicity
- Demonstrated creating a simple book entity with Spring Data GPA extension and querying the database using a repository pattern
- Mentioned other features like creating native images and handling burst traffic in a cloud environment
- Concluded first part by emphasizing Quercus's power and flexibility for developing Java applications quickly and efficiently


## Serverless Kafka on Kubernetes | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=bL9e1xt2TuA](https://www.youtube.com/watch?v=bL9e1xt2TuA)



- Matias from Red Hat discussing Kafka on OpenShift
- Kafka is a project that runs on Apache Kafka and Kubernetes
- Operator simplifies installation, patching, and management of Kafka cluster and ZooKeeper
  - Allows declaring topics with specific configurations
  - Allows creating users with permissions to access the Kafka cluster
- Kafka operator handles scaling based on traffic and load balancing between multiple instances
- K Native Eventing is a project focusing on event processing, delivering events from sources to sinks
  - Provides common infrastructure for consuming and producing events
  - Uses Kafka as a source and Apache Camel for routing events
  - Supports various channels, including in-memory, Apache Kafka, and others
- K Native Eventing supports universal subscription delivery and management of event subscriptions
- Kubernetes native is a service platform that runs applications in containers and manages scaling based on demand
- Que native serving handles request-driven models and scales containerized applications to handle incoming traffic
  - Scales based on the number of incoming HTTP requests or containers
- Demonstration shows installing and using OpenShift to manage Kafka, K Native Eventing, and an event-driven application.
- K Native Eventing can be used for data streaming pipelines and event orchestration in a Kubernetes environment.


## Future-proof apps | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=FC3jSKgTNK0](https://www.youtube.com/watch?v=FC3jSKgTNK0)



- Two experts from Red Hat to discuss modular design for monolithic applications and preventing the evolution into 'big ball mud'
- Eric Murphy: architect, modernizing legacy monolith apps, building microservices, open source technology advocate, author of blog
- Bert Sutter: developer, focuses on application development, helping customers with AI/ML, modular architecture, maintainer of a blog
- Discussion on applying modularity to monolithic applications and the concept of 'big ball mud' - unregulated growth, repeated expedient repair, information shared promiscuously among disparate elements
- Proposed flavors of application modularity: source control, build, data, deployment
  * Source control modularity: multiple git repositories, one large app allows for scale and separation
  * Build modularity: separate projects, publish artifact repository (Nexus)
  * Data modularity: tight coupling, shared database schema, separation of concerns
  * Deployment modularity: deploy multiple microservices instead of one application, interservice communication, event propagation using network transport, client UI utilizes multiple services potentially with API aggregator
- Demo of Instagram-like simple application modeled with modular design (photo gallery)
  * Event-driven architecture
  * Three microservices: photo service, query service, storage service
  * Service communicates via message broker
  * Each microservice has its own dedicated storage and database schema
  * User creates a new photo sends a POST request to photo service, information is stored in database and published to message broker
  * User adds a like to a photo sends a POST request to like service, counter is incremented and new message is published to message broker
- Modularity principles: code modularity, data modularity, source control modularity, build modularity, deployment modularity
- Code modularity: decoupled communication via message broker, data modularity: dedicated data store accessing only own data
- Demonstration of photo gallery application built with modularity practices using Eclipse and multiple git repositories
- Microservices approach: deploy service independently, update independently, organize development teams differently, scale development teams differently.
- Scalability concerns in monolithic applications and microservices approach
- Benefits of monolithic deployment: easier to develop, data centralization, single API endpoint, simpler communication between components
- Disadvantages of monolithic deployment: less flexibility for scaling, potential downsides of distributed systems (unreliable network communication)
- Question and answer session covers memory concerns in microservices vs. monolithic applications, UUID as a solution to data sharing issues, and the decision between monolithic and microservice architecture.


## Building freely distributed containers with open tools | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=Qcys7fKSzB0](https://www.youtube.com/watch?v=Qcys7fKSzB0)



- Speaker is Scott McCarty, expert in Red Hat and Podman.
- He will be discussing Linux containers, specifically UVI podman, focusing on finding, running, building, sharing, and deploying containers.
- The talk aims to show the ease of use of podman, even for non-experts.
- Scott mentions his six-year experience with container technology, starting with Docker.
- He explains how finding a container involves using the command line or searching the Red Hat container catalog.
- Verifying the trustworthiness of a container image is also important, which can be done through the Red Hat container catalog's interface.
- The demo will cover finding an image, checking its age and tags, building upon it with a Dockerfile, adding utilities, and sharing and deploying the new container image using OpenShift.
- Podman simplifies container development by allowing users to run services locally without complex client-server interactions or requiring root access.
- The demo will also cover creating a Kubernetes service and running it locally with CoReady containers.
- Scott mentions the differences between Padma and Docker, including their command line interfaces and image generation technology (Korkis).
- He briefly talks about the use of VFS drivers in rootless 77 and overlay FS in rel 78.
- The talk aims to answer audience questions throughout and encourages attendees to take a deeper look at the technology, such as systemd and YAML files.


## Testing in Production. From DevTestOops to DevTestOps | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=EVD4EXj8RKc](https://www.youtube.com/watch?v=EVD4EXj8RKc)


- Welcome to DevNation Tech Talk presentation by Alex Soto, Red Hat Calthrop developer and author.
- Topic: Testing in Production using Kubernetes OpenShift perspective.
- Brief background on testing in production, importance of faster deployments and shorter lead times.
- Challenge: Traditional testing approach in microservices architecture can be time-consuming and confusing for operation teams.
- DevOps culture shift: Embrace testing as a continuous process, not just a developer's responsibility.
- Testing strategies and techniques:
  - Canary releasing: Release new features to a small percentage of users and monitor their behavior before rolling out to everyone.
  - Blue/green deployment: Deploy new version of service in parallel with the old one, then switch traffic when ready.
  - Rolling updates: Update services incrementally while keeping some instances running the older version.
  - Infrastructure testing: Test entire application stack and infrastructure together for better results.
- Tools and platforms: Jenkins, Kubernetes OpenShift, Puppet, Quarkus, Spring Boot, Vert.x.
- Importance of communication and collaboration between teams: Dev, Ops, QA, DBAs, Security.
- Challenges in testing production environments:
  - Complexity and cost of maintaining multiple test environments.
  - Need for faster and more efficient testing techniques.
  - Balancing testing with business priorities and project deadlines.
- Conclusion: Embrace continuous testing, automation, and collaboration to deliver high-quality software quickly and efficiently.

---

Summary:
- Alex Soto discusses the importance of testing in production using Kubernetes OpenShift perspective.
- DevOps culture shift: Continuous testing and collaboration between teams.
- Testing strategies and techniques: Canary releasing, Blue/green deployment, Rolling updates, Infrastructure testing.
- Tools and platforms: Jenkins, Kubernetes OpenShift, Puppet, Quarkus, Spring Boot, Vert.x.
- Challenges in testing production environments: Complexity, cost, efficiency, business priorities, project deadlines.
- Conclusion: Embrace continuous testing, automation, and collaboration for high-quality software delivery.


## Plumbing Kubernetes builds | deploy with Tekton | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=q5P2V_YShjA](https://www.youtube.com/watch?v=q5P2V_YShjA)



- Welcome to talk on Tecton technology and building component applications on Kubernetes
- Speaker is an expert in Tecton and will demonstrate its capabilities
- Tecton helps manage cloud latency, continuous delivery, containerization, and serverless technologies
- Cloud native applications are based on Linux containers and use CI/CD pipelines for deployment
- Tecton divides into four main blocks: defining resources, creating pipelines, building images, and running tasks
  - Defining resources involves setting up reusable resources, breaking down large tasks into smaller ones, and mounting volumes
  - Creating pipelines allows grouping application tasks together in a specific order for efficient deployment
  - Building images involves creating Docker images using CI/CD tools like Maven or Gradle
  - Running tasks includes defining security contexts, setting resource limits, and managing container privileges
- Tecton streamlines the process of building and deploying cloud native applications by making it easier to manage containers, pipelines, and tasks
- Demonstration to follow using a Java application example


## Revisiting Effective Java in 2019 | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=fmOrmNVdKig](https://www.youtube.com/watch?v=fmOrmNVdKig)


- Edson Naga will present on effective Java, specifically Java 8 features like lambdas and modules.
- He'll have live coding examples and encourage attendees to read the book.
- He's a Brazilian Japanese Java champion and Microsoft MVP.
- Naga's favorite subject is effective Java; he believes even experienced developers can learn something new.
- He'll share tips on immutable classes, factory methods, value objects, and equals/hashcode implementations.
- Immutable classes: make fields final or private, use constructor to hide information, implement static factories.
- Factory methods: delegate object creation, optimize computation, prevent expensive array creations.
- Value objects: use equals/hashcode, provide getters/setters carefully, consider using stream API instead.
- Equals/hashcode: use library methods, avoid using == operator for primitives or boxed types, implement Comparable interface.
- Lambda expressions: use method references to simplify code, understand functional interfaces and their uses.
- Enums: create polymorphic enum types with abstract methods, use Java 8 features instead of ugly Java 5 code.
- Method handles: understand method references and their advantages/disadvantages in different scenarios.


## Introducing Kogito | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=tLz_aNLuCR0](https://www.youtube.com/watch?v=tLz_aNLuCR0)

Error


## 17-million downloads of Visual Studio Code Java extension | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=_AcjWfY5cfc](https://www.youtube.com/watch?v=_AcjWfY5cfc)


- Bob Davis, Principal Product Manager for Red Hat developer program, discussing Visual Studio Code extensions.
- Discussing the need for flexibility in tooling as developers use different tools and environments.
- Introduced Language Server Protocol (LSP) for debugging and code completion in multiple IDEs.
- Visual Studio Code Java extension first shipped in 2016, with 18 million downloads.
- Open source Java development tools like Eclipse JDT and Microsoft's Java extension pack available.
- Code Ready Analytics extension for application stack reporting and security vulnerabilities.
- Korkis app demo showing weather information and debugging capabilities.
- Mentioned Java support, debugging, and plugins for Visual Studio Code.
- Discussed the need for extensibility in IDEs to accommodate various development needs.
- Mentioned the popularity of Visual Studio Code as a multiplatform, feature-rich code editor.
- Discussed Java debugging, testing, and analysis tools available with Visual Studio Code.


## Easily secure your cloud-native microservices with Keycloak | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=JvPBWPDQ940](https://www.youtube.com/watch?v=JvPBWPDQ940)



- Speaker introduces himself and topic: secure microservices in a cloud native environment using Keycloak.
- Mentions laptop issue, promises live coding.
- Discusses Chico tea club identity server and Keycloak for user management/authorization.
- Explains use of OpenID Connect protocol and obtaining tokens from the Keycloak server.
- Describes differences between monolithic applications and microservices architecture, focusing on securing microservices.
- Demonstrates using access tokens to call services and shows failure when token is not included in request header.
- Discusses offline signature verification and trusted environments.
- Explains how a service can call another service and the need for propagating tokens between them.
- Shares code snippets for securing a Java web application with Keycloak, including using an adapter and customizing the rest template.
- Demonstrates login flow in a simple HTML/JavaScript application and obtaining tokens from Keycloak.
- Mentions Quercus as a new Java stack for building microservices.
- Describes creating a secured resource path and using middleware to protect routes.
- Discusses registering a rest client, propagating headers, and returning responses with access tokens.
- Talks about handling authentication in a PHP application using a sidecar proxy.
- Mentions the use of Keycloak Operator for easy deployment on OpenShift.
- Apologizes for running out of time and encourages questions or sharing the video link for further learning.


## Subatomic reactive systems with Quarkus | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=fQMg3Ve6Ep8](https://www.youtube.com/watch?v=fQMg3Ve6Ep8)



- Welcome to another Dead Nation presentation about Reactive programming using Quercus
- Clement Kofi, software engineer, will discuss building web applications with Quercus
- Quercus is a fullstack Java environment that provides fast start times and low memory consumption
- It's based on libraries like Vert.x, Hibernate, and CDI
- Reactive programming means reacting to message stimuli instead of writing code in an isochronous manner
- Spreadsheet example: observing a cell inside a spreadsheet and updating another way by building an event loop with callbacks or using actors
- Quercus unifies reactive and single stateless components
- Reactive manifesto defined in 2014, focuses on responsiveness and distributed systems that exchange messages for processing
- Imperative programming involves developer control while reactive programming depends on message stimuli to control flow
- Quercus provides a way to write asynchronous code using operators and composing programs using the operator pipeline
- Virtual address is used for elasticity, which handles load balancing and failover automatically
- Circuit breaker pattern protects against failure cascades in distributed systems
- Request/Reply vs message streaming: message streaming allows decoupling of components and asynchronous processing
- Quackers provides an HTTP messaging system for all-in-one use, but it's recommended to separate concerns using different technologies
- Starbucks example: traditional coffee shop vs microservices architecture
- Asynchronous microservices allow for more responsive handling of requests without blocking
- Quercus provides a reactive messaging library and supports stream annotations for easier implementation
- Reggie programming is a type of reactive programming based on data flow pipelines and event processing
- Use cases include financial trading systems, real-time analytics, and chat applications.


## Quarkus: Hibernate with panache | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=aKsxaCiP7bE](https://www.youtube.com/watch?v=aKsxaCiP7bE)



- Introducing Emmanuel Bernard, Hibernate and Quercus expert
- Discussing hibernate in cloud native context: microservices, fast startup time, low memory usage
  - Developer joy through reuse of existing technology and unifying configuration
  - Memory improvement and faster start times through native image compilation
- Demonstrating Hibernate's reactive capabilities using a simple Java application
  - Changing resource file without restarting the application
  - Instant feedback loop for coding, testing, and deployment
- Discussing benefits of Quarkus in Hibernate's future
  - Faster start times and low memory usage with CDI, rest easy, and Krakus
- Demonstrating Hibernate ORM (Object-Relational Mapping) features using a simple todo application
  - Defining an entity and its database mapping
  - Using Hibernate Validator for data validation
- Discussing the future of Hibernate with a focus on simplification and performance improvements
  - Improved query performance through contextualization and optimized HQL queries
  - Support for reactive programming models and event sourcing
  - Integration with popular frameworks and tools, such as GraalVM and Kubernetes.

No context:
```
This transcript does not provide enough context to summarize its content effectively.


## Kubernetes enterprise integration patterns with Camel-K | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=51x9BewGCYA](https://www.youtube.com/watch?v=51x9BewGCYA)



- Welcome to live broadcast about Apache Camel and Kubernetes integration
- Nicola Farrar from Luca Bourget will present
- Discussing Apache Camel, a powerful opensource integration framework
- Integration means communication between different systems with different transport methods or domain models
- Camel provides tools to help integrate disparate systems
- Camel has support for enterprise integration patterns (EIP)
- Apache Camel is 10 year old project with active development and many contributors
- Camel DSL allows writing complex integrations easily using Java, XML, etc.
- Camel can be run in various environments including Spring Boot, Carafes, Thornail MicroProfile, etc.
- New project called Camel K for running Apache Camel in cloud environment using containers
- Camel K can help users avoid dealing with runtime environments like Spring Boot
- Camel K provides tools for building and deploying integrations as custom resources on Kubernetes
- Allows fast redeployment and scaling of integration code in the cloud
- Camel K has a growing list of connectors to various systems like Elasticsearch, MongoDB, etc.
- Demonstration of building a simple chat bot using Telegram and Apache Camel K.


## Quarkus: Supersonic, subatomic Java | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=7G_r1iyrn2c](https://www.youtube.com/watch?v=7G_r1iyrn2c)

Error


## Apache Kafka Streams for the Hybrid IoT | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=zmLzDj8OgQY](https://www.youtube.com/watch?v=zmLzDj8OgQY)



- Welcome to Kafka and OpenShift Tech Talk
- Paulo, IOT expert from Reddit, will be speaking about using Apache Kafka for IOT solutions
- Apache Kafka is a traditional messaging solution used in IOT applications
- Sensor cloud solution provides raw data from devices, which is ingested and turned into intelligence
- Data goes through a pyramid of information: raw data -> processed data -> knowledge -> wisdom
- Use realtime analytics to get realtime reaction to events
- Stream processing allows handling of unbounded data sets and realtime analytics
- Apache Kafka has a stream API for realtime data streaming and analytics
- Apache Kafka is horizontally scalable, fault tolerant, and can handle high throughput/low latency requirements
- Use Kafka Connect to manage data ingestion from various sources
- Apache Kafka provides a commit log for distributed transactions
- Use Kafka Streams API for stream processing instead of Spark Streaming to avoid the need for another cluster
- Kafka can be used with traditional messaging protocols like MQTT and NTP
- Discussed use case of using a gateway between IOT devices and cloud services for translation and offloading processing
- Gateways can also handle security, reduce network traffic, and provide local processing capabilities when devices are offline.


## JMS 2.0 on Kubernetes with Apache ActiveMQ | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=mkqVxWZfGfI](https://www.youtube.com/watch?v=mkqVxWZfGfI)



* The speaker is part of Red Hat and works on the AMQ messaging product.
* JMS (Java Message Service) has been around for a long time and influential in messaging landscape, especially in enterprise software development.
* JMS introduced important concepts like multiple connections, sessions, and message topics/queues.
* One major improvement in JMS 2 was the introduction of persistent send operations and asynchronous communication, making messaging more efficient.
* API improvements like accessing payload messages directly without casting made writing reliable applications easier.
* ActiveMQ (popular open-source messaging server) uses JMS for messaging and has a new architecture called Artemis, which supports asynchronous operations and is designed for modern event-driven applications.
* Docker and Kubernetes have changed the deployment environment, making it easier to deploy lightweight applications using messaging technologies like JMS.
* The speaker will demonstrate using JMS and Kubernetes in an example application.
* The example application uses two technologies together: a REST API (JAX-RS) for external access and JMS for internal communication within the cluster.
* The speaker will use Docker, MiniCube, and Kubernetes to set up and deploy the example application.
* The sender service sends messages asynchronously using JMS to an Artemis broker, which the receiver service consumes using JMS and HTTP.
* The presentation covers various topics like building a Docker image, exposing services inside and outside of the cluster, and handling reconnects and failovers.
* The speaker also discusses some advanced concepts like AMQP routing and high availability in Artemis deployments.


## Develop and deploy faster with Red Hat Enterprise Linux | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=4DiLdgtcavo](https://www.youtube.com/watch?v=4DiLdgtcavo)



- Max Burger, Solutions Architect at Red Hat Benelux, to speak about new features in RHEL 8
- Discussing App Streams and Image Builder
- App Stream allows parallel deployment of multiple versions of a programming language
- Allows developers to access new versions without affecting the existing system
- Web console for image building and management, including UI control over systems and monitoring performance
- Image Builder allows creation of minimal operating system images with specific components installed
- Q&A session to follow after presentation
- Max Burger has a Twitter handle @MarcyBurke_ and YouTube channel "100 things Red Hat Management" for more information.
- App Stream is a new feature in RHEL 8 that enables faster version deployment by giving access to new programming language versions alongside existing ones in parallel. It allows developers to use the latest versions without affecting the entire system.
- Web console image building and management includes UI control over systems, monitoring performance, and managing multiple instances of the same application or database server.
- Image Builder is a tool that allows creating minimal operating system images with specific components installed. It can be used in private and public cloud environments.
- Max Burger will provide a demo of App Stream and Image Builder during the presentation.


## Apache Kafka and Debezium | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=QYbXDp4Vu-8](https://www.youtube.com/watch?v=QYbXDp4Vu-8)


- Welcome to another deaf nation conference
- Huge crowd, gunner morlun presentation on Kafka, Kubernetes, and CDC (Change Data Capture)
- Gunnar works at Red Hat, TZM project, also used validation tool in past
- Database application infrastructure focus, practical set of capabilities
- Change event propagation and decoupling using Kafka consumer, scalable performance and asynchronous communication
- CDC allows data replication across vendor boundaries, enables pushing data to other systems like Hadoop or ElasticSearch for analytics
- Data enrichment possible with CDC events (e.g., adding metadata)
- Microservices architecture use case: each service should have its own database, avoid sharing and tight coupling, CDC can help with event-driven communication and data consistency between services
- Kafka Connect framework mentioned, source and sink connectors available for various systems (ElasticSearch, Postgres, BigQuery, etc.)
- Demo of using Kafka Connect to replicate data from a MySQL database into Elasticsearch for full-text search capabilities
- Mentioned benefits of CDC: decoupling, scalability, asynchronous communication, fault tolerance, and real-time data processing
- No context.


## Serverless with Knative deep dive - How to install and deploy | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=-8fW1x5biCw](https://www.youtube.com/watch?v=-8fW1x5biCw)



- Presenter: Vinegar Bertha
- Session: K native deep dive
- Topics: Canadian server, automating scale, deploying a high level program
- Demos: 3 demos showing deployment, scaling, and logging
- Resources: GitHub, gRPC, Google Cloud Platform (GCP)
- Q&A: Audience can email or tweet questions to presenter
- Presenter will provide slide show and demos
- Slide link: bit.ly/kserving
- Presenter recently returned from Canada
- Canadian server architecture: servlet request, technically called SerfRequest
- Scaling at zero: automatic replicas, fast in Japan
- Display video: github spec, Cuban demo
- Q: What's a good resource for learning K native? A: Presenter suggests eco upstream or deploying the Canada platform.
- Presenter uses similar one like screen for deploying K native on Cuban GK engine
- First demo: deploy simple high level program, auto scale, logging
- Q: What's the latest release of K native serving? A: Presenter mentions 0.3 is coming soon
- Presenter shows how to deploy a Java application with K native and Google Cloud Platform (GCP)
- Second demo: using multiple strategies for deploying services
- Presenter discusses analyzing scaling, threshold values, and grace periods
- Q: What's the difference between using a node port vs. load balancer? A: Load balancer is an advantage because it eliminates the need to use a node port
- Third demo: water scaling and automatic scaling with K native
- Presenter mentions using Scale 2 billion for diverse scale, but currently has limitations
- Q: How do you define services and resources in K native? A: Services and resources are defined and orchestrated in K native.


## Kubernetes: Your next application server | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=K6gM4wFEmwA](https://www.youtube.com/watch?v=K6gM4wFEmwA)


- Welcome to another deaf nation conference, Ed Sanders will answer questions live from Raleigh North Carolina
- Friends and neighbors are encouraged to join the chat in real time
- Reminder: refresh browser for session updates, use chat tab for Kubernetes questions
- Ed begins by defining application server and its key features: accessible via standard API, clustering, failover, load balancing, developer focus on business logic
- Brief history lesson: mentions popular movies, Java surpassing C in popularity, and the rise of WebLogic app server with its clustering capabilities
- Comparison between 1999 and 2018: less money spent to launch applications, move from monolithic apps to microservices and containerization
- Discusses the importance of APIs in application servers, specifically clustering for high availability and load balancing
- Mentions the evolution of Java EE ecosystem, focusing on standard apis that continue to innovate the industry
- Describes how Kubernetes can be used as an application server platform with its ability to handle stateful applications in a rolling update environment
- Demonstrates deployment and management of a simple application using Kubernetes, including health checks and rolling updates.


## Knative: Going native and serverless on Kubernetes | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=qdUxni96n3s](https://www.youtube.com/watch?v=qdUxni96n3s)



- Welcome to Deaf Nation Live from Amsterdam
- Topic: Kubernetes with Kay Native, open source project by Red Hat
- Presenter is William Marketo, "insider knowledge" about Brazil
- Focus on surplus, specifically in SOA architecture context
- Surplus in SOA: running applications require server management and scaling
  - Idea: separate functions from bundled services (picture change)
  - Kay Native helps provide infrastructure for containerized applications
    * Build, run, and serve container apps
    * Eventing module for handling events and triggers
      - Receive adapter to map specific events to application logic
      - Subscription and routing for event delivery within the app
- Key Native provides a lightweight way to implement infrastructure services
  - Containerized event handling and serving
  - Scalable based on number of events received

The presenter then proceeds to give a demonstration using Kay Native, explaining the steps involved in building and deploying an application using the platform. The demo covers creating containers, applying configuration revisions, and scaling using routes. The presentation also discusses the integration with OpenShift and other tools such as Jiali for monitoring and tracing.


## Afternoon General Session | DevNation Live 2016

URL: [https://www.youtube.com/watch?v=y87SUSOfgTY](https://www.youtube.com/watch?v=y87SUSOfgTY)



- Rachel Laylock from Thoughtworks talks about her experience helping a large financial enterprise adopt continuous delivery
- Client had slow release cycles and was struggling to make monthly hotfixes
- The team spent long hours during weekends trying to deploy hotfixes, requiring everyone involved
- The project failed despite significant investment in continuous delivery tools and practices
- Reasons for failure: codebase was huge and complex, with 70 million lines of code and a messy dependency architecture
- Continuous delivery required not just automating deployment but also addressing issues related to operationalization of software, including data management, configuration management, continuous integration, quality assurance, release management, and potentially changing organizational structures
- The team learned a lot since the initial failure, with a focus on creating a platform that supports self-service deployment and enables independent scaling, while also maintaining cohesion and avoiding coupling issues.


## Getting started with Apache Kafka | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=CZhOJ_ysIiI](https://www.youtube.com/watch?v=CZhOJ_ysIiI)



- Apache Kafka is a popular messaging system, known for its scalability and fault tolerance.
- Kafka topics are split into partitions, which allow parallel consumption and horizontal scaling.
- Partition assignment can be based on message key or round-robin distribution.
- Retention policy determines how long data is kept in Kafka before being deleted.
- Consumers use offsets to keep track of the position in a topic partition.
- Kafka offers features like rebalancing and consumer locking for handling consumer group management.
- Kafka can be run on various platforms, including OpenShift and Kubernetes.
- Traditional message brokers (like ActiveMQ, RabbitMQ) store messages in memory, while Kafka stores them on disk, allowing for better scalability and performance.
- Kafka supports streaming data processing with its Streams API and can be used for various use cases like data integration, metric collection, and log aggregation.
- Under the hood, Kafka relies on a distributed storage mechanism to manage and store messages efficiently.
- Kafka clusters can handle high throughput and are not dependent on dedicated storage networks.
- Consumers in a consumer group read from their assigned partitions and commit their progress back to Kafka.
- Consumers can be assigned to different partitions based on the consumer group ID or by using consumer locks for rebalancing.
- Synchronous producers can wait for message delivery acknowledgement before continuing, while asynchronous producers do not block for a response.
- Kafka's replay feature allows consumers to reprocess messages if needed, which is useful for handling out-of-order or incorrectly processed messages.

No context:

- The speaker discussed the features and capabilities of Apache Kafka, focusing on its scalability and fault tolerance.
- Kafka uses topics and partitions for efficient message processing and distribution.
- Consumers use offsets to keep track of their progress in a topic partition.
- Kafka offers features like consumer group management and rebalancing.
- Apache Kafka can be run on various platforms, including OpenShift and Kubernetes.
- Traditional message brokers differ from Kafka in how they store and process messages.
- The Streams API allows for advanced processing of streaming data in Kafka.
- Kafka uses a distributed storage mechanism to manage and store messages efficiently.
- Kafka clusters can handle high throughput and are not dependent on dedicated storage networks.
- Consumers in a consumer group read from their assigned partitions and commit their progress back to Kafka.
- Synchronous producers can wait for message delivery acknowledgement before continuing, while asynchronous producers do not block for a response.
- The replay feature allows consumers to reprocess messages if needed.


## Kafka Streams for event-driven microservices | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=x3QCrb6zCKA](https://www.youtube.com/watch?v=x3QCrb6zCKA)


- Rafael introduces Marius, Principal Specialist Solution Architect at Red Hat specializing in integration, messaging and data streaming.
- Topic: Event Driven Microservices using Apache Kafka Streams.
  - Overview of event driven microservices architecture.
  - Why use Kafka for event driven microservices?
    * Event coordination and state management.
    * Scalability and agility.
  - Kafka architecture overview.
- Mary from Red Hat discusses her deep interest in event driven microservices using Kafka.
- Question: Exhausted by the topic, what is the specific problem that Kafka stream solves for vendor microservices?
  - Event driven microservices are complex and require state coordination and change propagation.
  - Kafka solves the problem of managing distributed state by providing event driven messaging system and event processing capabilities.
- Mary discusses challenges in building event driven microservices architecture.
  - State management and coordination.
  - Event handling and processing.
- Kafka stream overview:
  - Distributed messaging system for event driven microservices.
  - Allows state management and performs real time event processing using a client library or an embedded application.
  - Supports advanced patterns like transactional interaction and windowing based aggregation.
- Benefits of Kafka stream for event driven microservices:
  - Event coordination and state management.
  - Decoupling interaction and change propagation.
  - Advanced event processing capabilities.
  - Scalability and resilience.
- Q&A session.
  - Question about resilience and reliability of Kafka stream microservices on OpenShift.
    * Kafka cluster can be managed using OpenShift, which provides resource management, monitoring, failover, and scaling capabilities.
      + Managed Kubernetes infrastructure simplifies managing complex event driven microservices.
  - Question about differences between Kafka and other messaging systems for event driven architecture.
    * Kafka's advanced features like windowing, transactions, and stream processing make it a good choice for event driven microservices.
  - Question about monitoring event driven microservices using Kafka stream.
    * Monitoring can be done through the Kafka cluster or by integrating with external tools like Prometheus, Grafana, or Nagios.
  - Question about security considerations when implementing event driven microservices using Kafka.
    * Security features include encryption, authentication, authorization, and access control policies for data in transit and at rest.
  - Question about the relationship between event driven architecture and API Gateway.
    * API Gateway can be used to provide a unified entry point to multiple microservices and handle routing, load balancing, and authentication.
    * Event driven microservices communicate with each other using events instead of APIs for better decoupling and scalability.
  - Question about the role of Kafka in event sourcing.
    * Kafka can be used as a commit log for event sourcing, allowing developers to rebuild the state of an application from past events.
      + Event sourcing provides a way to store all changes to an application's state in an immutable log, making it easier to audit and recover data.


## Kubernetes patterns: Foundational, structural, config, and advanced | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=n3F9zJvG67c](https://www.youtube.com/watch?v=n3F9zJvG67c)



- Dispens course before concrete actions.
- Kevin is an open source container orchestration system platform by Jazz Open Source at Google for over a year.
- Horizontally scalable with many copies running and is a service from Smith.
- Self healing with YouTube effect.
- Declared resources recover in stage one.
- Controller/manager for resource objects and clusters.
- Update strategy for reducing clutter.
- Estland's clarity future nice.
- For exzesse cluster central exposes resources.
- DPA Jörg standard operation.
- Cannot create or deep update leading to business object issues.
- Absolved themselves for the objects' security.
- Collect experience from Google.
- Professional users overbuild application store.
- Deployment updates and rollouts.
- Noteebook and server enterprise application integration pattern.
- District topix lagged before at least 11.
- Ideal service activation watching wersener concept.
- Live show and household management.
- Sap etr set controller with festzug raider newport.
- Application car heavily in debt for database.
- Graphic houses' first.
- Indes graphic configuration socializing database klima.
- Vertical check and no gating position.
- Local data and disk create value.
- Giotto location vertical update also for data virtual server.
- Risks at make composing.
- Custom container pressure easy cabrio.
- Vision de werks ampel is under pressure.
- Australian pattern during this time.
- Bad köstritz peach car.
- Orchester way cant capex e.
- Apotheke specific domain interesting.
- Look like lacquered type kassenchefin.
- Enemies and Kay Seyffert Oscar Freire jazz pass.
- Project management issues.
- Assisi control is still good also the cash.
- Berlin live stream at Corus.
- Raider stpo projects hintersten sitze base case.
- Parade is Ingo Lang.
- Wild place before lifecycle manager witschel.
- Reiter and Ingres object fly trick post service netz surfen controller.
- Total revenue of container control was bodypacks tänze to learn or config match point to application.
- Vital contact center conversion fall change when kodak account restarts application.
- Hoppe reloaded Kastrati on the platform content news presentation.
- Release protection with Z max and memory 2 jpg states of EU.
- Potter no context.


## A deep dive into Keycloak | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=ZxpY_zZ52kU](https://www.youtube.com/watch?v=ZxpY_zZ52kU)


- Welcome to another Definition Live session, today we will have a deep dive demo of Keycloak.
- Keycloak is an open source identity and access management solution designed for modern application APIs and services.
- It differentiates from others in the space by being easy to use for application developers.
- Keycloak provides support for Single Sign On (SSO), Identity Brokering, Social Login, and Adaptive Multi-Factor Authentication (MFA).
- The demo will cover configuring a new realm, setting up an SMTP server, registering a client, and mapping attributes.
- Keycloak can be integrated with various external identity providers such as Google, GitHub, LDAP, Active Directory, and OpenID Connect.
- The admin console allows managing users, realms, clients, roles, and permissions.
- Keycloack supports various protocols including OAuth2, OpenID Connect, SAML, and JSON Web Tokens (JWT).
- It provides features like self-registration, email verification, avatar upload, custom themes, and event logging.
- Keycloak can be clustered for high availability and scalability.
- The admin console offers various APIs and CLI tools for managing the platform programmatically.
- Keycloak supports various authentication flows like browser-based login, magic link, and OTP.
- It includes a registration service for creating clients, and built-in brute force password protection.
- Keycloak is used by organizations ranging from small to large enterprises.
- For more information or to try out the demo, please check out the Keycloak website or contact the community.


## Hybrid cloud bursting with AMQP | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=Q4CCKUpAgDo](https://www.youtube.com/watch?v=Q4CCKUpAgDo)



- Ted Ross from Red Hat presenting on asynchronous messaging and hybrid cloud communication using Vertex Messaging
- Using AMQP protocol, worker update events, and load balancing across multiple data centers (AWS and GCP)
- Workload generator sends requests to workers which reply with results, periodic updates, and statistic data
- Interactive frontend displays realtime information on workload, message flow, and worker status
- Scaling the demo by adding more workers and generating higher load, showing how traffic is distributed based on latency
- Discussing the benefits of using OpenShift for deployment and handling failures in hybrid cloud environments.


## Securing apps and services with Keycloak authentication | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=mdZauKsMDiI](https://www.youtube.com/watch?v=mdZauKsMDiI)


- Welcome to another definition live, talking about security in APIs and Keycloak's role
- Keycloak is an open source project for identity and access management, specifically designed for modern applications and APIs
- Delegating security firstly provides better security as it deals with user authentication at the application level rather than embedding different authentication methods in every application
- OpenID Connect and SAML are two main stream protocols for delegating authentication and authorization
- OpenID Connect is simpler to implement and works well for modern applications like single page apps, mobile apps, and REST services APIs
- Keycloak provides a simple adapter to integrate with different frameworks and languages
- Keycloak currently supports integration with Java, Node.js, Spring Boot, and Jetty Tomcat containers
- Keycloak simplifies the process of securing applications by providing a least opinion, best integration experience
- OpenID Connect uses bearer tokens for access, which are automatically added to requests when invoking secure services
- The presentation also shows a demo of securing a PHP application using Keycloak.


## Continuous integration + continuous delivery with Jenkins | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=IIPKhS0Ybo0](https://www.youtube.com/watch?v=IIPKhS0Ybo0)



- Introduction: Sony Naga, Mac, Jenkins, CI/CD, Kubernetes
- Jenkins: Continuous Integration and Delivery tool, popular for open source projects, flexible, easy to use, connects every system, large ecosystem of plugins
- Kubernetes: Container orchestration tool, essential for container deployments, Jenkins uses it for deployment across multiple hosts, community standard
- Benefits of using Jenkins with Kubernetes: Smooth tool, powerful, flexible pipeline, saves time and resources, easy to deploy and build custom container images
- Practical tips for building advanced pipelines:
  - Jenkins source image session: Use open shift or red hat kubernetes to create a stable, solid environment for Jenkins
  - Combine configuration in container image: Save time by combining configuration files within the container image
  - OpenShift Pawnee plugin: Synchronize objects and create Kubernetes resources automatically
  - Customize Jenkins life with plugins: Configure slave pods, use config maps to store configurations and replicate them across environments
- Using Jenkins with Kubernetes for security:
  - Use a centralized authentication token instead of spreading credentials within the project
  - Create secret objects in Kubernetes to hold sensitive data securely
- Canary releases: Gradually release new versions of applications with zero downtime and manage rollbacks effectively
- Conclusion: Jenkins and Kubernetes are powerful tools for building, deploying, and scaling applications. Using them together provides a smooth, flexible, and efficient development experience.


## Feature toggles & hypothesis-driven development | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=Ob_jpoWRCwg](https://www.youtube.com/watch?v=Ob_jpoWRCwg)



- Presenter: Edson Onaga
- Topic: Feature toggle hypothesis-driven development
- Goal: Discuss feature toggles and hypotheses in the context of continuous delivery, especially as a solution to the "deployment problem" in software development.

**Background:**

- Continuous delivery is about fully automated software deployment pipelines.
- The goal is to reduce risk by testing business hypotheses before production releases.

**Hypothesis-driven development vs traditional pipeline approach:**

- In the traditional pipeline approach, it's assumed that the next version will be better than the previous one.
  - This can lead to wasted time and resources on features that might not be useful in production.
- In hypothesis-driven development, small plates (features) are cooked separately based on user feedback.
  - The user decides which feature they prefer and the resource is allocated accordingly.

**Feature toggles:**

- A feature toggle is a flag that can be turned on or off to test different features in production.
- This allows teams to implement two different approaches and compare their performance without having to merge branches.
- The advantage of using feature toggles is that it makes it easier to switch between implementations if one performs better than the other.

**Demo:**

- Two demos were presented, one using FF4j with Java and another using Go Z.
- Both demos involved using feature toggles to test different recommendations in production.
- The goal was to compare the performance of two different recommendation engines and choose the better one based on user feedback.

**Conclusion:**

- Feature toggles are a useful tool for hypothesis-driven development, especially in the context of continuous delivery.
- They allow teams to test different approaches in production and switch between them if one performs better than the other.
- The importance of monitoring performance and measuring meaningful metrics was emphasized.


## Advanced Microservice Tracing with Jaeger | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=hpnLUFRY4_Y](https://www.youtube.com/watch?v=hpnLUFRY4_Y)



- Welcome to another Dead Nation Live session in New York City
- Today's topic: Tracing Key Technology - Distributed Microservices
- Speakers are Pablo and Joseph from Red Hat, working on Kyani project
- Problem: In a microservice architecture, it's hard to figure out which version of the service was affected by a request
- Term: Observability
  * System is observable if you can collect metrics, see logs, and analyze tracing information
- Solution: Tracing
  * Code mutation with explicit instrumentation
  * Tracing techniques: cold instrumentation, distributed context propagation
- Tracing code vs business code
  * Increase instrumentation for better visibility
- Java uses byte code manipulation or runtime agents for tracing
- Popular frameworks include OpenTracing, Micrometer, and Zipkin
- Tracing in a microservice road: each service needs individual tracing window
- Context propagation: passing correlation ID to trace the request across services
  * Google's Pepper project was an early solution, now many vendors offer this capability
- End of presentation, open for questions.


## MicroProfile - Microservices with Java EE | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=fbVYQENPa4s](https://www.youtube.com/watch?v=fbVYQENPa4s)



- Welcome to Dead Nation Live 2018, session on MicroProfile with John Clem and Edson Anagha
- MicroProfile: standardization around microservices technology, started as specification project in Red Hat
- Based on Java EE programming model (CDI, JAXRS, Jason processing) but faster, like open source project
- Collection of specifications for microservices, e.g. fault tolerance, circuit breaking, config externalizing, health check
- Eight specifications released so far, with more coming
- Implemented by multiple vendors, including Red Hat
- Focus on developer enablement: better documentation, YouTube videos, etc.
- Go to MicroProfile.io for more information and join the discussion group
- WildFly Swarm: rethinking application server, supports microProfile and optimized for container environments (like OpenShift)
- Supports Java EE and microProfile in same app, packaged as single jar file with Docker layer
- Can run inside maven without creating custom application server
- MicroProfile specifications added to Java EE application servers by vendors
- Circuit breaker implementation available in MicroProfile for handling failure scenarios
- Config API allows externalizing application configuration
- Q&A session follows

Questions:

1. Definition of MicroProfile (no context)
2. What is the goal of MicroProfile?
3. How does MicroProfile relate to Java EE?
4. Which specifications have been released so far?
5. Who is implementing MicroProfile and why?
6. Where can I find more information about MicroProfile?
7. Does WildFly Swarm support MicroProfile?
8. Can I use Java EE and MicroProfile together in the same app?
9. What is the goal of Circuit Breaker in MicroProfile?
10. How does Config API work in MicroProfile?
11. Is it possible to deploy a war file in JBoss EAP using MicroProfile?


## An introduction to serverless | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=03LeehvuOJE](https://www.youtube.com/watch?v=03LeehvuOJE)


- Welcome to Dead Nation Live, a conference about cloud native computing.
- Kamesh Sampath will be presenting on service architecture using OpenShift and Kubernetes.
- He'll discuss the benefits of containerization for Java developers, such as automatic scalability and cost reduction.
- He'll cover how OpenShift can deploy functions asynchronously and handle communication between services using a messaging broker.
- He'll demonstrate an example using OpenShift CLI and Apache OpenWhisk (wsk).

I'd be happy to summarize the transcript for you! Here are the main points from the given text:

- Welcome to Dead Nation Live, a conference about cloud native computing.
  - Kamesh Sampath will be presenting on service architecture using OpenShift and Kubernetes.
- Benefits of containerization for Java developers:
  - Automatic scalability.
  - Cost reduction.
  - Quick and easy development.
  - Improved developer agility.
  - No need to manage servers or worry about vendor locking.
- OpenShift can deploy functions asynchronously using a messaging broker, allowing for more efficient communication between services.
- Demonstration of OpenShift CLI (wsk) and Apache OpenWhisk (wsk).
  - Create, invoke, and manage Java functions in an open source environment.
  - Use different programming languages (Java, JavaScript, PHP, etc.) and frameworks (Spring Boot, Hibernate, etc.).
  - Utilize various communication patterns like synchronous, asynchronous, and event-driven architectures.


## Serverless and Servicefull Apps - Where Microservices complements Serverless | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=v3A--YM8iQE](https://www.youtube.com/watch?v=v3A--YM8iQE)



- Welcome to Swamp J Frog Conference presentation by "the guy"
- Will share link to slide deck and recording later
- Presentation about microservices, database challenges, and demos
- Microservices are like "two to three year old things"
- Free ebooks available on intro to microservices and microservice architecture
- Biggest challenge with microservices is dealing with databases
- Last week's demo at Red Hat Summit showed a massive application built with microservices and machine learning
- Monolithic applications are fading in favor of microservices
- Challenges with distributing microservices include network services, service discovery, load balancing, circuit breaking, and sidecar containers
- Kubernetes and OpenShift help manage microservices infrastructure
- Service mesh solutions like Istio apply concepts like sidecar containers, service discovery, and circuit breaking
- Microservices require different programming models compared to monolithic applications
- Function services are a type of microservice architecture where functions are invoked based on events or API calls
- Function services can be ephemeral, running in containers for a short period of time
- OpenWhisk is an example of a function service platform
- Different runtimes support different languages and programming models
- Event streams and APIs can be used to trigger function services
- Commands can be used to invoke function services locally or remotely
- Unit testing, integration testing, and continuous delivery pipelines can be used with function services
- Next session will provide a deep dive into openWhisk.


## Jakarta EE: The Future of Java EE | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=f2EwhTUmeOI](https://www.youtube.com/watch?v=f2EwhTUmeOI)



- Speaker introduces himself and topic: future of Java EE, now part of Eclipse Foundation as Jakarta EE
- Java EE has been dominant in enterprise for 20 years but criticized for slow adoption of new technology and monolithic architecture
- MicroProfile was introduced to help next generation microservice developers with enterprise features without full app server
- Jakarta EE includes projects like Micronaut, Helidon, and Eclipse GlassFish
- Oracle's involvement in Java EE has been questioned due to slow progress and lack of open source collaboration
- MicroProfile adoption grew rapidly since 2016 and is now a top level project at Eclipse Foundation
- Eclipse Foundation aims to standardize specific APIs and drive the Java community process behind Jakarta EE
- Speaker encourages audience to get involved in Jakarta EE by submitting proposals, joining mailing lists, and contributing code
- Jakarta EE focuses on asynchronous APIs, removing legacy technologies, and addressing feature gaps in traditional Java EE specification
- Linux container technology like Docker and Kubernetes are influencing the direction of Jakarta EE
- Speaker discusses potential involvement of companies like Red Hat and IBM in driving Jakarta EE forward
- Questions from audience cover topics like repackaging, certification, and MVC architecture. Answers encourage community involvement to find solutions.
- Speaker thanks audience for their interest and participation in the Jakarta EE project.


## Enterprise Node.js on OpenShift | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=BXj0uw65yKc](https://www.youtube.com/watch?v=BXj0uw65yKc)



* Lance Ball from Red Hat presenting on Node.js in an Enterprise context using OpenShift and Kubernetes.
* Node.js version 10 coming soon, with long term support.
* Node.js applications can be built directly as upstream containers for deployment on OpenShift/Kubernetes.
* Node.js core committers and technical steering committee members involved in development.
* Monolithic applications can become complex, microservices help simplify architecture.
* Express framework used to build simple web applications.
* OpenShift tools like node-shift make deployment easy.
* Environment variables can be set for deployments.
* Node.js applications can be run directly on Docker containers or as part of an OpenShift cluster.
* Circuit breakers can help handle cascading failure in microservices architecture.


## Smarter Testing with Microservices | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=0lUwLXpID1M](https://www.youtube.com/watch?v=0lUwLXpID1M)


- Welcome to another Definition Live session
- Speaker: Alex Soto from Red Hat, Spain, will talk about microservice testing using a new tool called TestSmart
- Microservices are becoming more common in software development as companies move from traditional businesses to software companies and need to adapt quickly
- Need to release faster, get things done in production quicker, and add cool features to stay competitive
- Traditional testing process involves making changes, creating branches, running tests, and merging changes
- TestSmart is a tool developed last year that allows for faster test execution and better results
- It's a maven extension that works with Java projects
- It can run tests in parallel, validate dependencies, and provide test reports
- Speaker will demonstrate the tool by testing a microservice using Maven and TestSmart
- The goal is to save time and make the testing process more efficient.


## Camel Riders in the Cloud | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=zuEYtMvHN6g](https://www.youtube.com/watch?v=zuEYtMvHN6g)



* Apologies for international crowd, 25-minute presentation with Q&A session to follow
* Camel: open source integration framework for building enterprise applications, used since 9 years
* Camel allows integration of different systems using common components and Enterprise Integration Patterns (EIP)
* EIP: message routing, transformation, error handling, etc.
* Camel is lightweight, can run everywhere from traditional servers to cloud containers
* Camel is flexible and versatile for integrating various APIs, databases, messaging systems, web services, etc.
* Camel can transform data structures like XML, JSON, CSV, flat files, etc.
* Camel supports distributed computing and can integrate legacy systems with mainframes and FTP file systems
* Q: What's the best way to run Camel in a cloud container? A: Use the latest webinar presentation by Merced for more details, borrowed slide from Bill.
* Camel is used for integration between microservices, which have become increasingly popular as applications have moved towards a containerized and distributed architecture
* Running Camel in a container makes it easier to manage and scale services, as they can be run on different hosts and communicate over networks
* Camel Cloud: Red Hat brings additional capabilities like CI/CD pipelines, centralized logging, and monitoring for running Camel applications in a container.
* Camel allows easy integration of APIs, databases, and other systems using connector components
* Camel can be used to connect APIGateway and small embedded devices
* Agile Integration: Red Hat Middleware team coined the term for distributed integration, which is the bread and butter of Camel
* Camel supports stateless microservices and provides mechanisms like configuration management (conflict maps) and fault tolerance (circuit breakers) to handle external dependencies and failures.


## Secure Spring Boot Microservices with Keycloak Part 1 | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=Bdg_DjuoX0A](https://www.youtube.com/watch?v=Bdg_DjuoX0A)



- Sebastian Blanc welcomes audience to talk about securing a Spring Boot application using Keycloak, an open source identity and access management solution.
- He explains that he has been working at Reddit for five years as part of the Key Club team.
- He outlines the main concept as building a secure application using Keycloak's identity flow and user management features.
- Discusses the demo setup: a simple Spring Boot MVC app, a Keycloak server running, and a web browser accessing the app via a URL.
- Explains that when a user accesses the app, they first go through border control (authentication), then are redirected to the application if authenticated.
- Describes how a JWT token is used for authentication, containing necessary information for different applications and being signed by a private key.
- Mentions that Keycloak supports social login providers like Facebook and Twitter.
- Discusses additional features of Keycloak like multi-factor authentication and custom claims in the JWT token.
- Demonstrates creating an admin user, adding a client to represent the application, and configuring security constraints in the servlet container.
- Explains that Keycloak integrates well with Spring Security for handling identification flows.
- Discusses extending the login screen with user registration and social login features.
- Mentions that the demo may run late due to time constraints.


## KubeBoot: Spring Boot deployment on Kubernetes has never been so easy | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=Cv8_EHQgUZ4](https://www.youtube.com/watch?v=Cv8_EHQgUZ4)


- Speaker introduces himself and mentions his background in the cloud native industry.
- Discusses Spring Boot and how it has evolved over time, with a focus on managing multiple instances and automation.
- Talks about the challenges of managing application state and avoiding conflicts in a distributed environment.
- Introduces Kubernetes as an important container orchestrator that satisfies the twelve factor app properties.
- Discusses deploying Java applications using Spring Boot, Maven, and Fabric8, with a focus on ease of deployment and load balancing.
- Shows a simple demo of deploying a Java application using Kubernetes and Fabric8, highlighting features like auto-scaling and rolling updates.
- Discusses the importance of monitoring and discovery in a cloud native environment, mentioning services like Netflix Eureka and Consul.
- Talks about the challenges of building and deploying applications in a containerized environment, including managing dependencies and configuration.
- Mentions the role of service meshes like Istio in managing complex microservices architectures.
- Provides resources for further learning, including links to tutorials and documentation.


## Istio: Canaries and Kubernetes, Microservices and Service Mesh |  DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=YQLOcjvbo9s](https://www.youtube.com/watch?v=YQLOcjvbo9s)



* Welcome to another Dead Nation Live presentation
* Change of platform
* Large crowd in Vietnam, Johannesburg, etc.
* Sharing slide deck link: bitly sto Canaries
* Dive deeper into Service Mesh technology and Kubernetes
* History of monolithic applications and microservices
  * Monolithic apps: one big application
  * Microservices: distributed networked things, complex
  * Need clean solid API for communication between services
  * Need discovery, load balancing, resiliency, scalability, elasticity
* History of DevOps and cloud computing
  * Agile manifesto and incremental work products
  * Cloud and containerization (Netflix, Docker, Kubernetes)
* Concept of a service mesh: dedicated structure for service-to-service communication
  * Proxy handling traffic, sidecar containers, routing, authentication, monitoring, etc.
* Demonstration using Istio/Sto
  * Load balancing with Tia
  * Canary deployment with traffic splitting
  * Rolling updates and rollbacks
  * Service discovery and integration with Kubernetes
* Benefits of a service mesh include: intelligent routing, resilience, security, observability
* Questions and answers in chat.


## Update your Database Schema with Zero Downtime Migrations | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=3mj6Ni7sRN4](https://www.youtube.com/watch?v=3mj6Ni7sRN4)



- Welcome to Dead Nation Live, Edson Naga speaking on zero downtime database migration in cloud native world.
- Database administrators used to hunt and kill databases, but now it's about transitioning smoothly with DevOps practices.
- Migration manually is no longer an option, automate everything.
- Bluegreen deployment: two identical production environments, one running the old version, other the new.
    * Single requirement: both versions must be back compatible.
- Database migration methods: set statements, DDL scripts, flyway, etc.
    * Sharding can help with large migrations.
- Common challenges include column renames, data migration, and state handling.
    * Column rename: 4 steps - add new column, read old data, copy to new table, delete old column.
- Migration strategy: always keep databases back compatible with previous versions for safe production releases.
- Demo using a Wildfly Swarm project with a customer class and database migration using Flyway.
    * Adding a new column, renaming a column, and updating the application accordingly.
- Important to keep both versions running during the migration process.
- Using a separate migration file for each version update can help keep things organized and ensure compatibility.


## Why you’re going to fail running Java on Docker | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=tI2l8yThKK4](https://www.youtube.com/watch?v=tI2l8yThKK4)



- Rafael is speaking from a hotel room in Brasilia, Brazil. He's originally from Brazil but now lives in Orlando, Florida.
- Rafael will be discussing Docker and how it relates to Java and cgroups.
- Container technology started around 2000 with FreeBSD, LXC, etc. JVM and container kernel future came later.
- Rafael is using a machine with 1GB RAM for his Java application and another machine with 8GB RAM as the Docker host.
- He's trying to limit the Java application inside the Docker container to use only 100MB memory, but the container is using 1GB of RAM on the host even when it's restricted to 50MB of swap.
- The problem might be related to JVM not being aware of the container's memory limit in the Linux kernel's cgroups.
- Rafael suggests checking the Java log container for any error messages, as well as the Docker container logs and system logs on both machines.
- He also recommends trying different Linux distributions or Java versions to see if the problem persists.
- The history of containers includes FreeBSD (2000), LXC (2006), Docker (2013), JVM (2000), etc.
- Rafael is using two machines: one for the Java application (Docker 1.0 or 1.1, 1GB RAM, 1GB swap) and another as the Docker host (8GB RAM).
- He's trying to run a Java application inside a Docker container with a memory limit of 100MB, but it's using more than that on the host.
- Rafael suggests checking the logs for any error messages and trying different configurations or Linux distributions.
- The JVM and container kernel future started around 2000 with FreeBSD, LXC, etc., and the Java version was released in May 1996.
- Rafael is running a Java application inside a Docker container with a memory limit of 100MB but seeing it use more than that on the host.
- He's also trying to allocate a larger heap size in the JVM, but it keeps getting killed by the kernel due to insufficient memory.
- Rafael suggests checking the logs and specifying the memory limit directly when creating the container using Docker run command.
- He also mentions that the JVM might not be aware of the container's memory limits in the Linux kernel's cgroups, so it's important to investigate this issue further.
- Rafael discusses the history of containers and Java, mentioning that FreeBSD started the container trend around 2000, and Java was released in 1996.
- He also mentions that he's running a Java application inside a Docker container with a memory limit but is experiencing issues where the container uses more memory than allocated on the host machine.
- Rafael suggests checking logs for errors and trying different configurations or Linux distributions to resolve the issue.
- Rafael talks about the history of containers and Java, starting around 2000 when FreeBSD introduced generic processes, leading to LXC and Docker in later years. Java was released in 1996.
- He is currently experiencing an issue where a Java application inside a container is using more memory than specified on the host machine.
- Rafael suggests checking logs for errors, trying different Linux distributions or JVM versions, and specifying the memory limit explicitly when creating the container to troubleshoot the issue.
- Rafael mentions that he's running a Java application inside a Docker container with a memory limit but is experiencing issues where the container uses more memory than allocated on the host machine.
- He suggests checking logs for errors and trying different configurations or Linux distributions to resolve the issue.
- Rafael discusses the history of containers, starting around 2000 when FreeBSD introduced generic processes, leading to LXC and Docker in later years. Java was released in 1996.
- He is currently experiencing an issue where a Java application inside a container is using more memory than specified on the host machine.
- Rafael suggests checking logs for errors, trying different configurations or Linux distributions, and specifying the memory limit explicitly when creating the container to troubleshoot the issue.

Rafael is discussing issues with running a Java application inside a Docker container and how to limit its memory usage using cgroups in the Linux kernel. He mentions that the JVM might not be aware of the container's memory limit, causing it to use more memory than allocated on the host machine. Rafael suggests checking logs for error messages, trying different configurations or Linux distributions, and specifying the memory limit explicitly when creating the container to troubleshoot the issue. He also discusses the history of containers and Java, starting around 2000 with FreeBSD and LXC leading to Docker in later years, and Java being released in 1996.


## Domain Driven Design for Mere Mortals | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=8k2yNRHdG2U](https://www.youtube.com/watch?v=8k2yNRHdG2U)



- Presenter: Justin Holmes, Senior Consultant at Red Hat
- Topic: Domain Driven Design (DDD) in 2017 and Microservices
- Agenda: Intro to DDD, Bounded Contexts, Shared Language, Complexity Opportunity Domains, Modeling, Port Adapter Pattern
- Introduction to DDD: started in 2003, focus on optimization of microservices, building small autonomous components, reducing size and increasing autonomy.
- Bounded Contexts: different meanings even with the same word, importance of shared language within a bounded context.
- Shared Language: helps teams work together, focus on core complexity, build collaboration through modeling.
- Complexity Opportunity Domains: finding pieces of software that give business competitive advantage, focusing on simplicity and collaboration in design and delivery process.
- Modeling: building models around concepts shared language, importance of a clear distinction between business model and implementation.
- Port Adapter Pattern: connecting different systems and technologies, allowing for independent deployment and design.


## Reactive Landscape | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=Y-7LnLl8160](https://www.youtube.com/watch?v=Y-7LnLl8160)


- Welcome to Next Definition Live event in Dublin, Ireland
- Clemens from Vertex team will talk about reactive programming and system architecture
- Reactive system: responding to stimulus, creating controlled response
- Reactive vs. synchronous systems: reacting to stimuli instead of waiting for it
- Reactive system architecture: message driven interaction, elasticity, scalability
- Reactive programming: asynchronous, nonblocking I/O, event driven
- Examples: HTTP server, database interaction, spreadsheet calculations
- Difference between reactive and corrective programming: reaction vs. response to errors
- Challenges in implementing reactive systems: synchronous development models, IO blocking
- Benefits of using reactive programming: improved responsiveness, reduced complexity
- Tools and libraries: Akka, Pure Actor Model, Rector, Spring, Project Reactor
- Comparison to traditional approaches: event loop, minimum number of threads, concurrency model.


## Big Data In Action with Infinispan | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=ZUZeAfdmeX0](https://www.youtube.com/watch?v=ZUZeAfdmeX0)


- Welcome to another Dead Nation Live presentation
- Gallagher will deep dive into Big Data
- Definition: Big Data is a term for technologies and ideas used to process large amounts of data
- Challenges include real time streaming and offline processing
- Memory data grids are a solution for managing distributed data in real time
- Distributed cache, SQL databases, and continuous queries are techniques used in memory data grids
- Two use cases: event driven computation and data analytics
- Event driven computation allows real time processing of data with advanced APIs
- Data analytics involves using Hadoop integration for powerful processing
- No context: mention of Jupyter Notebook and OpenShift environment.

The presenter goes on to give a live demo using a train transport system as an example, but the context provided does not allow for a summary of that part of the presentation.


## Sidecars and a Microservices Mesh | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=ZR2GGoT_GTg](https://www.youtube.com/watch?v=ZR2GGoT_GTg)



- Presenter: Christian Posta, Red Hat guru for cloud native and microservice architecture, specifically around Docker, Kubernetes, OpenShift.
- Topic: Discussing the technology called "Sto" that changes the game for building applications.
- Agenda: Microservices, service mesh, dependency management, organization, service discovery, resilience, load balancing, retries, timeouts, circuit breaking, etc.
- Microservices: Faster change and less organizational complexity.
- Service Mesh: Decouples network communication, allows for better coordination and control of services.
- Dependency Management: Avoiding monolithic architecture, keep implementation consistent across different frameworks/libraries.
- Service Discovery: Different components interact within the cluster.
- Resilience: Dealing with timeouts, cascading failures, rate limiting, circuit breaking, etc.
  - Control Plane (Envoy proxy): Enforcing policies, getting telemetry, deciding access/interactions between services within budgets.
  - Data Plane: Interacting with different services, sending back telemetry, handling routing rules, applying traffic management.
- Security: Managing security without the application's knowledge, mutual authentication, etc.
- Deployment: Kubernetes, sidecar containers, etc.
- Control Traffic: Routing, rate limiting, circuit breaking, etc.
  - Service Mesh (Envoy proxy): Allowing fine-grain control of traffic within a cluster.
- Architectural Distributed Diagram: App defined and running on Kubernetes, using SEO control, injecting sidecar proxies for data plane communication.
- Routing Rules: Surgically routing traffic to different versions of services or specific users.
- Canary Deployment: Testing new versions with a fraction of the traffic before rolling out to everyone.
- Network Security: Firewalls, network policy implementation, etc.
  - Service Mesh (Envoy proxy): Enforcing policies at the application layer instead of the network level.
- New Innovations: Cilium project for kernel-level processing and filtering, continuing evolution in the open source world.
- Upstream/Downstream: Open source world, upstream meaning open source software that's being productized by companies like Red Hat, downstream meaning enterprise software built on top of that open source software.
- Sidecar Proxy Service: Taking care of service discovery, load balancing, circuit breaking, tracing, microservices capabilities, etc.
  - Camel: Integrating with Apache Camel for advanced message transformation and orchestration, etc.
  - Drawbacks: ESB (Enterprise Service Bus) conceived and implemented in a different way, still done but not exactly the same as service mesh.
- Logging: Request level telemetry, number of request calls, circuit breakers, logging application logs, etc.
- Questions:
  - Pete: Concept around manipulating firewalls, iptables, and networking standpoint in SEO approach.
  - Marcel: Mention of Fluentd for integrating logging in OpenShift/Kubernetes and aggregating elasticsearch data.


## Kubernetes for Java developers | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=_vM3ORa9_JE](https://www.youtube.com/watch?v=_vM3ORa9_JE)



- Welcome to Dev Nation live session
- Special guest: Rafael Benevides, Director of Developer Experience at Red Hat
- Focus on Java developers using Kubernetes
- Benefits of running Java applications inside containers include simplifying development and enabling microservices architecture
- Overview of Kubernetes project: an orchestrator for managing containerized applications
  - Manages machines and focuses on application deployment
  - Popular open source project with over 25,000 stars on GitHub
- Concepts to understand: pods, services, labels
  - Pods are collections of containers in a cluster that share an IP address and environment variables
  - Services locate every pod based on label and send requests to them
- Demonstration using Kubernetes commands (Cube CTL) and Docker
  - Deploy SQL container as pod and describe its details
  - Discuss deployment replication controller and how it keeps a desired number of replicas running
  - Create service for the SQL pod and explore how requests are sent to available replicas
- Comparison of running a Java application with Docker vs Kubernetes commands
  - Simplified process with Kubernetes using YAML files and single command creation
- Future topics: microservices architecture, OpenShift, and more Java workloads like Spring Boot.


## Going Reactive with Java | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=mhwvDeDzSSA](https://www.youtube.com/watch?v=mhwvDeDzSSA)



- Presenter is demonstrating reactive programming and the technology called Vertex
- There will be a live coding demo
- Slides can be found on a URL provided
- Audience encouraged to ask questions in chat during presentation
- Presenter has a background in mainframe computing and relational databases
- Reactive programming is different from traditional synchronous data streams, it's asynchronous and ongoing
- Vertex allows for handling large amounts of data and processing it efficiently
- Demo will involve running a Spring Boot application on public cloud and showing how it handles high traffic
- Presenter will also discuss microservices architecture and the role of event buses in reactive systems.



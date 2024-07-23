## Wasm GC: What Exactly Is It (and Why I Should Care) - Ivan Mikushin, VMware

URL: [https://www.youtube.com/watch?v=ndJP-vmZFYk](https://www.youtube.com/watch?v=ndJP-vmZFYk)

 * Ivan Mikushin from VMware discussing WebAssembly Garbage Collector (Wasm GC)
* Wasm GC needed due to popularity of languages requiring garbage collection like JavaScript, Java, Python, Go, etc.
* Wasm GC proposal adds Heap type with subtypes and recursive types, index type, new instructions, and shorthand notations.
* Heap memory is used for garbage collection and managed data in WebAssembly.
* Three disjoint hierarchies in WebAssembly: functional type, external type, and aggregate type.
* 30 new instructions added to support garbage collection.
* Compilers supporting WebAssembly garbage collection are coming soon for popular languages.
* WebAssembly runtime controls memory management using Heap.
* Garbage collector ensures that unreferenced data is automatically freed.
* WebAssembly uses a 32-bit integer, and i31 refers to an unboxed scalar type.
* Rust uses automatic memory management with borrow checker instead of garbage collection.
* Different languages have different memory models, and some require garbage collection.
* Compiler knows exactly where memory is allocated in WebAssembly, unlike Rust.
* Chrome V8 engine has already implemented Wasm GC support, and other projects are working on it.
* Kotlin is expected to get Wasm GC support soon.


## JavaScript Toolchain for WebAssembly Components - Guy Bedford, Fastly

URL: [https://www.youtube.com/watch?v=ChBGAZRU1qs](https://www.youtube.com/watch?v=ChBGAZRU1qs)

 * Guy Bedford discusses integrating WebAssembly (WASM) components into the JavaScript ecosystem
* Three ways to run JavaScript in a browser: CommonJS, native modules, and ES modules
* Goal is to have WASM embedded like a JavaScript module with minimal glue code
* ebuild is a modern build tool that can run WASM along with JavaScript
* Ebuild uses static analysis to instantiate WASM modules at build time, reducing the need for glue code
* Component model provides first-class embeddability and execution environment ability for WASM modules
* WebAssembly Module System (WASI) enables interoperability between JavaScript and WASM components
* JRR file is used to convert a component to an ES module interface, allowing custom instantiation and transpilation
* The demo shows using the ChaRay library, which can be built for WASM and run in the browser with minimal glue code.


## The WASI OS - Isolation with Communication, Wasm style - Dan Gohman, Fastly

URL: [https://www.youtube.com/watch?v=97jw9v2dRaw](https://www.youtube.com/watch?v=97jw9v2dRaw)

 * Dan Gohman discussing WASI OS design philosophy, focusing on isolation and communication
* Operating systems (OS) have personalities, underlying implementation affects their design
* Unix philosophy emphasizes loose coupling, human interactivity, and modularity
* Isolation and communication are opposing concepts in computing: isolation ensures non-conflicting processes, while communication allows them to work together
* Early computers had limited access control, no virtualization or internet, so trust was implicit
* Unix pipelines (a Unix feature) allow for interprocess communication through a pipeline of connected programs
* WASM (WebAssembly) is a modern technology that isolates and communicates components (programs), similar to the Unix philosophy
* WASI OS, a new operating system built with WASM, aims to provide fine-grained resource handling, contextual name resolution, and efficient code accessing
* Streams are a fundamental concept in WASI OS, allowing for easy data transfer between processes and improving performance and scalability
* The design of WASI OS prioritizes small illusions (limited virtualization), default deny security, and contextual name resolution for composability
* WASI OS also supports loose coupling through import/export, making it easier to write programs that work together.


## Wasm Components for Every Language - Kyle Brown, SingleStore

URL: [https://www.youtube.com/watch?v=IqehHuPYUSc](https://www.youtube.com/watch?v=IqehHuPYUSc)

 * Kyle Brown from SingleStore discusses making Wasm components for every language
* Two main points: making a component for every language and making different languages work together
* Components are structured as modules with import/export abstractions
* Components contain a module and can be instantiated like links
* Component model is layered on top of core WebAssembly, allowing the expression of complicated semantics
* To create a component, one writes code at the component level, which is then lowered to core WebAssembly
* Interface type modules are used for linking components together
* The Wasm toolchain can parse and call the binary component directly
* Creating business logic in assembly language directly is time-consuming and not practical for most use cases
* Runtime wrapping is an alternative approach, where the tool generates bindings to adapt types between languages
* Precompiled runtimes like SpiderMonkey are used for JavaScript components
* Snapshotting improves startup speed by preinitializing component state
* The binding generation process can generate errors if type mismatches occur
* Components can be composed by importing and instantiating them together, creating a graph of components
* Lifting and lowering are needed to convert data between components with different representations
* Tower Wansum is a tool that allows for component drag-and-drop composition using open source tools.


## Develop Wasm Applications with Docker - Angel M De Miguel Meana, VMware & Justin Cormack, Docker

URL: [https://www.youtube.com/watch?v=xPO3-TOZxW0](https://www.youtube.com/watch?v=xPO3-TOZxW0)

 * Angel M. De Miguel Meana and Justin Cormack discuss the intersection of Docker and WebAssembly (WASM)
* WASM allows for portable, sandboxed applications that can run anywhere with a consistent environment
* Containers and WASM share similarities in providing a consistent runtime environment and security isolation
* WASM is a binary instruction format that compiles code from languages like C, C++, and Rust into a single binary
* WASM runs on a virtual machine that provides a structured sandbox with namespaced isolation
* Containers and WASM can be used together to create portable applications with interchangeable benefits
* WASM containers are smaller in size compared to traditional containers as they don't require an operating system layer
* Docker Hub and GitHub Registries offer pre-built WASM container images for various interpreted languages like Python, Ruby, and PHP
* The use of a shim API allows WASM containers to run alongside traditional containers in the same environment
* Kubernetes benefits from using WASM containers as they are smaller and easier to manage in a cluster.


## Embedding WASM in the Future - Chris Woods, Siemens Technology USA

URL: [https://www.youtube.com/watch?v=LuiuA_v8X2Y](https://www.youtube.com/watch?v=LuiuA_v8X2Y)

 * Chris Woods, an industrial researcher at Siemens Technology USA, discusses the future of embedding WebAssembly (wasm) in various industries.
* Wasm is a portable, low-level code format that can be embedded in software and hardware systems, similar to traditional embedded systems.
* Wasm has been successful in the embedded space, with examples like Amazon Prime Video and Disney Plus using it for cross-device support.
* Wasm provides portability, allowing code to run on various platforms without modification, and isolation, preventing unintended access to memory or system resources.
* RL box is a web assembly tool that allows compiling libraries into wasm format with controlled memory access, ensuring sandboxing and security.
* The Acorn Archimedes computer from the 1980s, which was designed to be an embedded system with a custom processor and low power consumption, serves as an inspiration for wasm's potential success in the embedded world.
* Siemens is exploring the use of wasm in its various industries, including power systems, medical equipment, transportation, and industrial automation.
* The increasing importance of cybersecurity and the need to manage code updates in a distributed environment make web assembly an appealing solution for managing large-scale infrastructure.
* WebAssembly's portability and ability to run on multiple platforms with minimal modification make it a de facto standard for developing software, especially as hardware becomes increasingly complex.
* The webassembly community is actively contributing to its development and implementation, with subgroups focusing on both the browser world and non-browser applications.
* WebAssembly's performance, particularly in handling deeply nested data structures, can be improved through optimizations like component model function calls and memory isolation.
* Researchers are exploring new technologies like Cherry Capability to enhance wasm's security and performance.
* The standardization of webassembly is important for ensuring interoperability across various suppliers and maintaining compatibility with older runtimes.
* WebAssembly's potential in the embedded space includes its use in industrial automation, control systems, and microcontrollers.
* Bosch is proposing a potential way forward for wasm in the embedded space by targeting a subset of the web assembly specification for specific use cases, like automation.
* Wasm's role in the future of software development requires balancing the needs of developers and users, as well as addressing challenges like debugging and performance optimization.


## Building a WebAssembly-first OS – An Adventure Into the Unorthodox - Dan Phillips, Loophole Labs

URL: [https://www.youtube.com/watch?v=mQ58pLT8YQ4](https://www.youtube.com/watch?v=mQ58pLT8YQ4)

 * Dan Phillips talks about building a WebAssembly-first OS at Loophole Labs
* Goal is to create an approachable, general-purpose OS with minimal dependencies
* Discusses history of operating systems and influence from Unix and Plan 9
* WebAssembly redefines OS primitives like process management and memory management
* Mentions prior art projects like Nebula, Quasar, and the Gvisor project
* Experimenting with a system layer using the Gvisor project and a virtual file system
* Discusses potential benefits of WebAssembly for reducing syscalls and improving performance.


## Develop the Android Context Hub Runtime Environment (CHRE) Nanoapps in WebAssembly - Mingqiu Sun

URL: [https://www.youtube.com/watch?v=qyNu30eYsFg](https://www.youtube.com/watch?v=qyNu30eYsFg)

 * Mingqiu Sun is talking about developing Android Context Hub Runtime Environment (CHRE) Nanoapps using WebAssembly
* CHRE is a resource-constrained environment within the Android phone, responsible for managing embedded devices and specific tasks
* Challenge: moving existing Nano apps to webassembly, which requires converting data types and addressing memory issues
* Benefits of webassembly for Nano apps include a larger developer community, improved security, and easier portability across different platforms
* Google is building the CHRE environment but it's not open to developers yet
* Current MCUs used in Nano apps have non-standard architectures, which can make development challenging
* Use of webassembly allows for a more modular and linear memory-based system, reducing the need for complex pointer manipulation
* Solutions to common challenges include static assertions to ensure identical data structures and wrapper functions to facilitate communication between CHRE and native apps.


## Don't Get Owned by Dependencies: How Firefox Uses Wasm to Protect Itself from... - Shravan Narayan

URL: [https://www.youtube.com/watch?v=r7DZm5tHEeo](https://www.youtube.com/watch?v=r7DZm5tHEeo)

 * The speaker discusses the motivation and challenges of using WebAssembly (Wasm) in Firefox to sandbox libraries and protect against memory safety issues.
* Traditional methods for defending against native code vulnerabilities, such as ASLR, stack canaries, and CFI mitigations, are no longer effective against sophisticated attacks.
* The idea of isolating libraries using Wasm was first introduced in academia decades ago but only made practical with modern tools like the RL box framework.
* Firefox is a large, complex application written primarily in C++ with many dependencies on C libraries, which can introduce memory safety issues.
* Decoupling and sandboxing these libraries using Wasm allows for better isolation and easier integration into Firefox without introducing significant performance or engineering costs.
* The process involves compiling the library to Wasm, modifying Firefox to use the isolated version, and dealing with interprocess communication and data marshalling challenges.
* The RL box framework simplifies this process by automating many of the low-level details and providing a compositional sandboxing solution that can hide the complexity from developers.
* The talk covers some practical experiences deploying RL box in Firefox, including challenges with performance optimization, platform compatibility, and memory management.
* Ongoing research and development in Wasm security and tooling are continuing to make it a more effective and efficient solution for sandboxing libraries in production applications.


## Bringing AI to the Heterogeneous Edge with WebAssembly & ONNX - Francisco Cabrera & Ralph Squillace

URL: [https://www.youtube.com/watch?v=c9E9lr6YVp4](https://www.youtube.com/watch?v=c9E9lr6YVp4)

 * Francisco Cabrera and Ralph Squillace discussing bringing AI to the Edge using WebAssembly and ONNX
* Working with Azure, specifically Kubernetes Edge, seeing various use cases for AI at the edge including:
  + Industrial scenarios: welding detection, predictive maintenance, visual AI for zone determination and alarm creation
  + Medical vertical: vision AI for diagnosis assistance
  + Retail: customer pattern analysis and order preparation
* Challenges in Edge Computing include resource constraints, heterogeneous environments, cost, connectivity, and security
* WebAssembly allows for faster function execution, unified architecture compilation, improved security, and a unified AI framework (ONNX)
* Demonstration of using ONNX with a simple SqueezeNet model for image classification
* Onyx runtime supports Rust, FFmpeg, and various backends including OpenVINO and TensorFlow Lite
* Future plans include WASI support, larger model compatibility, and evolving the proposal to address AGI problems.


## Leveraging WASM to Improve Quality and Flexibility of the API Plugin Ecosystem... - Rohan Deshpande

URL: [https://www.youtube.com/watch?v=3fbgMzt6_4Q](https://www.youtube.com/watch?v=3fbgMzt6_4Q)

 * Rohan Deshpande, managing director and senior engineer at Goldman Sachs, discusses improving API productivity by supercharging APIs using WebAssembly (WASM)
* Goldman Sachs API platform serves millions of requests per day with a focus on developer productivity
* Traditional API plugins are typically developed in C++ or Lua and can be time-consuming to build and integrate
* WASM offers efficient execution, portability, and the ability to reuse code across multiple engines
* Goldman Sachs began experimenting with WASM for an account number reduction plugin, achieving 83% test coverage and reducing compilation time
* Challenges include integrating WASM modules into existing web engines like Envoy and Nginx, and performance tuning
* Benefits of using WASM include faster development cycles, code reuse, and improved security through isolation
* Goldman Sachs has converted 55 plugins to WASM-based implementation and plans to continue the conversion process.


## Getting Started with AI and WebAssembly - Angel M De Miguel Meana, VMware & Michael Yuan

URL: [https://www.youtube.com/watch?v=sxz-MxMNmRY](https://www.youtube.com/watch?v=sxz-MxMNmRY)

 * Michael Yuan and Angel M. De Miguel Meana discuss getting started with AI and WebAssembly
* Demonstration of object detection using Rust running in WebAssembly
* Benefits of using WebAssembly for AI include: zero Python dependency, easy deployment, portability across CPU and GPU architectures, and interacting with underlying hardware features through the host function
* WebAssembly runtime started in 2019 and allows separation of inference application life from interface, enabling adaptation to different backends
* Watermatch supports multiple machine learning frameworks including TensorFlow, PyTorch, OpenCV, and others through its plugin mechanism
* Supports popular image processing libraries like MediaPipe and OpenCV for preprocessing and postprocessing tasks
* Larger models may require more memory, which can be addressed by using the WasmCE specification to directly copy models from disk into inference frameworks
* Preprocessing and postprocessing functions can be implemented using Rust and the host function for efficient computation
* The ecosystem around WebAssembly AI is growing with improvements to the chain, multilanguage support, and collaboration between companies like VMware and Swati.ai
* Wasm provides a simple way to run large language models on personal laptops without the need for extensive preprocessing or installation of tools.


## Machine Learning in Fastly's Compute@Edge - Andrew Brown, Intel & Matthew Tamayo-Rios, Fastly

URL: [https://www.youtube.com/watch?v=dpOG5YnXDpM](https://www.youtube.com/watch?v=dpOG5YnXDpM)

 * Andrew Brown from Intel and Matthew Tamayo-Rios from Fastly discuss using machine learning inside WebAssembly
* Wasm's potential to transform various industries through AI, including text generation, image recognition, and video generation
* Challenges with previous approaches to running machine learning models in WebAssembly: performance and security
* Introduced Waz DNN, a system interface for webassembly modules that improves performance for machine learning inference
* History of proposals and implementations for integrating machine learning frameworks in WebAssembly
* The need for a function service that simplifies deployment, user experience, and security for scalable machine learning models on the edge
* Performance improvements through decoupling model life cycles from fast request handling
* Model size limitations and the need to run larger models elsewhere
* Managing the model's life cycle and optimizing caching behavior in Fastly
* Changes to WebAssembly specification, including async host APIs and process isolation for better performance and security
* Demonstration of a smaller image classification model using OpenVINO back end in Wazi NN.


## Unraveling the Magic of Two Hot Trends... - Larry Carvalho, Radu Matei, Aparna Sinha, Tyler McMullen

URL: [https://www.youtube.com/watch?v=RDPosMJ3SuE](https://www.youtube.com/watch?v=RDPosMJ3SuE)

 * The panelists, Larry Carvalho (moderator), Radu Matei, Aparna Sinha, and Tyler McMullen, discuss the future of generative AI and its applications.
* Generative AI is a technology that allows models to create new content, such as text, images, or code.
* The panelists discuss the use cases for generative AI in various industries, including healthcare, legal, finance, and retail.
* They also touch on the importance of explainability and avoiding hallucination in generative AI models.
* Radu Matei talks about the intersection of distributed systems and generative AI, and how webassembly can be used to run untrusted plugins in a secure way.
* Aparna Sinha discusses her experience investing in generative AI startups and the potential for the technology to transform various business models.
* Tyler McMullen talks about the importance of low latency and privacy in generative AI applications, particularly in healthcare and other regulated industries.
* The panelists also touch on the role of large language models in generative AI and the potential for open source and proprietary data to be used in training these models.
* They discuss the potential for webassembly to handle the requirements of new platforms and run generative AI workloads efficiently across multiple types of hardware.
* The panelists express their excitement about the opportunities presented by generative AI and the potential for it to transform industries and create new business models.


## Keynote: WASI Standards and the Component Model: Transforming Application... - Liam Randall

URL: [https://www.youtube.com/watch?v=zvDTNrJYnMw](https://www.youtube.com/watch?v=zvDTNrJYnMw)

 * Liam Randall, CEO of Cosmonic, talks about the WebAssembly Component Model
* He mentions his background in webassembly and Wasm Day event
* The component model is a Docker moment for the ecosystem
* CNCF WasmCloud project now supports webassembly component model
* WebAssembly has two specifications: module and executable
* WebAssembly components are like Lego blocks, allowing freed application architecture
* WASM Cloud focuses on freeing application architecture from tight coupling
* Demonstration using QR code to deploy a simple webassembly component
* WebAssembly is ready for prime time and can handle complex infrastructure needs
* Problems in regulated industries like Telco, Energy Systems, Financial Services, and Transportation are solved by the webassembly component model
* Orchestrating webassembly components with machine learning and edge cloud is possible
* Raise abstraction and work together to make webassembly better.


## Keynote: When Wasm Meets Cyber-Physical Systems: A Discussion of WebAssembly in... - Emily Ruppel

URL: [https://www.youtube.com/watch?v=1d4I7hwgxuk](https://www.youtube.com/watch?v=1d4I7hwgxuk)

 * Emily Ruppel, research scientist at Bosch, discusses the intersection of WebAssembly (Wasm) and cyber-physical systems
* Cyber-physical systems are made up of microcontrollers and actuators interacting in the physical world with tight real-time deadlines
* Bosch builds a variety of devices categorized as cyber-physical systems, including drills, dishwashers, and cars
* The challenge is to simplify networked safety-critical applications with virtualization using Wasm
* Wasm offers ultra-lightweight virtualization that covers the hardware platform throughout the rest of the software stack
* Bosch research uses Wasm in both the automotive domain and industrial factory automation domains
* Challenges include large collaboration, international partnerships, vendor compatibility, and maintaining safety and real-time guarantees
* Wasm can potentially streamline automotive software by fully decoupling programming language, application, scheduler, driver, and operating system
* The Silverline architecture leverages Wasm to achieve flexibility and uniformity throughout the network in industrial automation systems.


## Keynote: What is a Component (and Why)? - Luke Wagner, Distinguished Engineer, Fastly

URL: [https://www.youtube.com/watch?v=tAACYA1Mwv4](https://www.youtube.com/watch?v=tAACYA1Mwv4)

 * Luke Wagner, Distinguished Engineer at Fastly, explains the concept of a "component" in the context of WebAssembly (Wasm)
* Wasm is a binary instruction format with a stack-based virtual machine that provides portability and determinism through control flow integrity and subprocess sandboxing
* Use cases for Wasm include deploying large code bases, offloading compute-intensive tasks from JavaScript, and exploring alternative models for distributed computing like serverless and edge computing
* Components are a compositional module that allows for sharing machine code runtime, linkable modules, and binding generation across languages
* Reusing code across language boundaries is difficult with existing package registries and transitive dependencies, so Wasm's component model provides a solution by allowing different packages to be compiled into separate Wasm modules linked together
* The component model enables modularity without requiring microservices and allows for low-overhead cross-module calls using ASM sandboxing and linkable modules
* Virtual platform layering is another use case for components, as it provides strong isolation and efficient memory usage through a virtual file system and shared code development across teams.


## Keynote: Charting a Wasm Landscape - Chris Aniszczyk, Chief Technology Officer

URL: [https://www.youtube.com/watch?v=HGWj1dsDkrc](https://www.youtube.com/watch?v=HGWj1dsDkrc)

 * Chris Aniszczyk, CTO of CNCF, speaks about the growing interest and innovation in WebAssembly (Wasm) outside of the cloud native community
* Wasm is experiencing an innovation cycle similar to container technology with multiple runtimes and specs
* Early adopters include BBC, Disney, Amazon, Bosch, Goldman Sachs, and many startups
* The Wasm ecosystem is still in its early stages but evolving quickly
* Announcement of the open sourcing of a WebAssembly report covering various use cases and what's attracting developers to Wasm
* CNCF has commissioned the first Wasm landscape website (wasm-land.org) for tracking projects and companies using Wasm
* The Wasm landscape will be regularly updated through an annual survey
* Announcement of the creation of a Wasm working group within CNCF.


## Keynote: Welcome & Opening Remarks - Michelle Dhanani, Principal Software Engineer & Founding Member

URL: [https://www.youtube.com/watch?v=00p5ZJrI0DQ](https://www.youtube.com/watch?v=00p5ZJrI0DQ)

 * Michelle Dhanani, Principal Software Engineer and Founding Member at Fermion, welcomes everyone to the inaugural event
* Grateful for support from sponsors: Cloud Native Computing Foundation (Diamond), Cosmonic, Midokura, Microsoft Azure (Platinum)
* Thanks to program committee members and reviewers
* Reminds attendees to check their schedules using badge QR code and mentions onsite reception and networking opportunities
* Reminds everyone about event code of conduct: treat each other with respect and professionalism
* Encourages attendees to share ideas, collaborate, and network.


## Keynote: How WebAssembly can Power the New Wave of Serverless AI - Radu Matei

URL: [https://www.youtube.com/watch?v=8KMcd2X0JcM](https://www.youtube.com/watch?v=8KMcd2X0JcM)

 * Radu Matei, CTO and co-founder of Fermian, speaks about how WebAssembly is powering the new wave of serverless AI.
* Fermian started as a goal to build a new kind of computing platform with WebAssembly as the underlying runtime.
* Traditional application developers face challenges integrating AI infrastructure due to high costs and cold start issues.
* WebAssembly moves compute closer to data, improving efficiency and reducing infrastructure costs by moving machine learning models closer to the GPU.
* Fermian Cloud now offers a serverless AI beta that provides a building block for integrating AI capabilities into serverless applications.
* The Fermian approach involves implementing a host to talk to different hardware acceleration devices like Cuda GPUs, M1 chips, etc.
* Fermian Serverless AI beta includes services like model loading API and database storage for building full stack applications with AI capabilities.
* WebAssembly components can be run locally and deployed in the cloud without changing the developer experience.
* Fermian takes a higher-level interface approach to implement hardware acceleration devices, making it easier for developers.
* The Fermian open source project is available to sign up for a preview at their booth.


## Keynote: WEdge Project: Edge AI enabled by Wasm - Tatsuya Kato, CEO & Dan Dumitriu

URL: [https://www.youtube.com/watch?v=AOn9lWsZrJo](https://www.youtube.com/watch?v=AOn9lWsZrJo)

 * Tatsuya Kato (CEO, Midokura) and Dan Dumitriu (CTO, Midokura) introducing WEdge Project for Edge AI using Wasm
* Midokura is a Japanese IT industry company focused on Edge Computing and IoT since 2010
* Founded by former top management from the Sony semiconductor Solutions subsidiary
* Targeting solution provider for AI Developers, providing 80-year solution platform
* WEdge project born due to challenges in iot development: small memory constraints, lack of a secure environment for code execution, and diverse operating systems
* Goals: create an ecosystem with a plugin architecture, sandbox security isolation, and support for various languages like Python and C
* Consists of two parts: cloud side and agent side
* Cloud side runs alongside IoT platforms, providing REST APIs for developer interaction, AOT compilation, and different target device types
* Agent side wraps Wasm runtime and exposes native libraries, using an OS-agnostic realtime operating system like NuttX
* Provides sensor interfaces, communication modules, and various primitives for image processing and data storage
* WEdge Services APIs include sensor control, different communication types, and accelerator devices
* WEdge SDKs will support different languages, initially focusing on Python and TypeScript to address the challenge of polyglot development.


## Keynote: Are We Componentized Yet? - Bailey Hayes, Engineering Director, Cosmonic

URL: [https://www.youtube.com/watch?v=ReG2T-uMjQQ](https://www.youtube.com/watch?v=ReG2T-uMjQQ)

 * Bailey Hayes, Engineering Director at Cosmonic and member of the Bytecode Alliance, explores the question "Are We Componentized Yet?" in her talk
* Central Station is the top level component model for WebAssembly (WASM) ecosystem, with Wazzy Preview 2 being its current iteration
* WASM components have modular interfaces and are statically analyzable, enabling capability-safe interface definitions using a new IDL called wit
* Component models can be run in various environments, such as the WASI system interface or a webassembly HTTP proxy
* Bycode Alliance is working on building a standard for WASM component models and implementing it through different projects like wasm time, cargo component, Jayco, etc.
* TinyGo, Rust, and JavaScript are some of the guest languages that have tools for componentizing code using WASM
* There are ongoing efforts to make the WASM ecosystem more cohesive, including package management solutions like Warg and documentation initiatives
* TheComponentize World event is happening tomorrow for further discussion on the topic.


## Keynote: Welcome Back - Michelle Dhanani, Principal Software Engineer & Founding Member, Fermyon

URL: [https://www.youtube.com/watch?v=Hnw2LA0Pu4o](https://www.youtube.com/watch?v=Hnw2LA0Pu4o)

 * Michelle Dhanani, Principal Software Engineer and Founding Member of Fermyon, welcoming attendees to the final day of WasmCon
* Announces that there is a bite code Alliance componentize world hackathon taking place tomorrow, encourages attendance with a QR code to preregister
* Mentions that there is an event tonight at Lucky Strike with food, drinks, arcade games, and bowling, invites attendees to join.


## Keynote: WebAssembly in a Containerized World - Brendan Burns, Corporate Vice President, Azure OSS..

URL: [https://www.youtube.com/watch?v=X6WEJOEfDoQ](https://www.youtube.com/watch?v=X6WEJOEfDoQ)

 * Brendan Burns, Corporate Vice President at Azure OSS and co-founder of Kubernetes, talks about WebAssembly in a containerized world
* He has a team working on WebAssembly since last December and wanted to understand its technology better
* Containers and WebAssembly compared: containers provide the kernel and run-time environment, WebAssembly is focused on code
* Inside a container image, we don't care about most things except for essentials like an HTTP client library or necessary code
* Container images can be quite large (17MB for a Go Caddy web server), but with WebAssembly, the size reduces dramatically
* WebAssembly enables building and pushing smaller containers each time a file is saved
* Shrinking image size is beneficial for development use cases
* Containers were designed in the 1970s, while WebAssembly is more suited for cloud-based, distributed systems and connecting kernel calls to the cloud
* Exciting opportunity is rethinking how code interacts with the kernel and cloud services in a WebAssembly sandbox
* WASI (WebAssembly System Interface) HTTP spec and other projects are ongoing efforts to bring the ability to run WebAssembly inside an orchestrator like Azure Kubernetes Service
* WebAssembly containers can still require writing code, but progress is being made in the community.

Dev containers with WebAssembly support are a favorite for programming languages like Pascal, making it easier and quicker to get started.


## Keynote: Deploy WASM on the Edge - Brendan Irvine-Broque, Product Manager, Cloudflare Workers

URL: [https://www.youtube.com/watch?v=-3wKIfKHsB0](https://www.youtube.com/watch?v=-3wKIfKHsB0)

 * Brendan Irvine, Product Manager at Cloudflare Workers, discussing deploying WebAssembly (WASM) on the edge
* Cloudflare is a full stack serverless platform with global distribution, handling millions of requests per second
* Cloudflare Worker is a web interoperable runtime for running code at the network edge
* Worker RS is a Rust binding that makes it possible to write workers in Rust and run them on Cloudflare
* Bindgen is used to generate bindings, making the process of writing bindings less tedious and more portable
* Cloudflare Workers allow for building serverless applications with web interoperable technologies like APIs, WebGPU, etc.
* With WASM support in Cloudflare Workers, you can make interesting capabilities available as serverless functions
* Bindgen also allows publishing of specification definitions to move beyond language-specific bindings and make the process easier for developers
* Cloudflare is working on a new portable key-value store standard, excited about feedback from the worker community.


## Keynote: Wasm from the Inside Out: A Journey Through the Impact of WebAssembly in... - Saúl Cabrera

URL: [https://www.youtube.com/watch?v=lw8MnQ1fkac](https://www.youtube.com/watch?v=lw8MnQ1fkac)

 * Saul Cabrera, staff developer at Shopify, giving a talk on the impact of WebAssembly (WASM) in Shopify's production environment
* Shopify introduced WASM for extending business logic and enabling complex interactions between merchants, buyers, and third-party developers
* Challenges to adopting WASM include high cost, difficulty understanding and debugging programs, and complicated guest host interaction
* Early attempts to adopt WASM in 2014 were unsuccessful due to performance and scalability concerns
* Benefits of WASM include faster execution, improved startup time, and the ability to run multiple languages on the same platform
* Shopify's adoption of WASM was driven by the need to handle increasing merchant-buyer interactions and to scale the platform
* WASM enabled synchronous execution of untrusted code and improved performance through a performant interpreter
* Challenges included preinitialization, linking modules, and handling dynamic languages
* Tools like Wiser and Javi have helped make the process of using WASM easier, with better debugging stories and component models alleviating many challenges.


## Sandboxing Your Sandbox: Leveraging Hypervisors for WebAssembly Security - Danilo (Dan) Chiarlone

URL: [https://www.youtube.com/watch?v=v1bI1eHVwAw](https://www.youtube.com/watch?v=v1bI1eHVwAw)

 * Dan Chiarlone from Microsoft discusses sandboxing and securing WebAssembly (WASM) using hypervisors
* Hyperlite project, a Microsoft initiative, leverages virtual machine managers (hypervisors) to execute untrusted third-party code safely
* WASM is an excellent sandboxing technology for public clouds due to its resource and memory isolation, but it may not be enough for some use cases
* Binary security and host security are important aspects of WASM security
* Buffer overflow vulnerabilities exist in native binary code and can be exploited even in WASM; prevention methods like stack smashing protection and page execution protection are necessary
* Memory safety is crucial to prevent malicious input from crashing or corrupting the program, and Rust, a memory-safe language, can help
* The hypervisor provides an additional layer of security by isolating modules, preventing them from accessing each other's memory, and controlling resource usage (e.g., halting execution)
* Modern hypervisors support snapshotting and rollback, allowing quick recovery in case of a security incident
* Hyperlight demo showcasing the use of hypervisors to run 2,000 micro VMs with improved isolation and performance for web applications.


## Security and Correctness in Wasmtime - Nick Fitzgerald, Bytecode Alliance

URL: [https://www.youtube.com/watch?v=FFPoOR_5urw](https://www.youtube.com/watch?v=FFPoOR_5urw)

 * Nick Fitzgerald from Wasmtime at Bytecode Alliance discusses security and correctness in Wasmtime
* Wasmtime is a safe implementation language for WebAssembly (WASM) that helps extend applications without sacrificing performance
* WASM has historically had memory safety bugs, which Wasmtime aims to help prevent through Rust's type system and careful implementation
* Wasmtime's runtime provides strong isolation, but it can't fully prevent all attacks, such as malicious dependencies or recursive user input
* Cargo vet is a tool used by Mozilla to manually review third-party libraries before use in Firefox
* Wasmtime uses cargo vet and other security measures to help ensure the safety of embedded WASM applications
* Wasmtime's instantiation process is fast, allowing for temporal isolation and continuous fuzzing for security testing
* Crane Lift is a tool used by Wasmtime for instruction selection, optimization, and formal verification of correctness
* Differential fuzzing and formally verified versions of the interpreter are used to test and find bugs in WASM engines like V8
* Wasmtime's collaboration with Verifiable Rust (verasm) and ongoing formal verification efforts aim to improve security assurance.


## Panel Discussion: Browsers & Wasm - Ryan Hunt, Conrad Watt, Adam Klein, David Degazio, Bailey Hayes

URL: [https://www.youtube.com/watch?v=x6X2-UUxEZM](https://www.youtube.com/watch?v=x6X2-UUxEZM)

 * The panelists discuss WebAssembly (Wasm) and its role in browsers.
* Wasm is a binary instruction format for the web that allows running code at near-native speed.
* The Baseline compiler is used to quickly compile Wasm code and starts the process, but it's not always the fastest.
* Mozilla's wasmgc project allows managing memory like Kotlin and Java in Wasm, making use of a garbage collector.
* There are ongoing efforts to bring new languages like Rust and C++ to Wasm, which will expand its capabilities.
* The panelists talk about the challenges of implementing WebAssembly in browsers and the importance of interoperability and partnerships with language toolchains.
* Stack switching is a potential future improvement for Wasm that would allow more efficient multitasking.
* Other areas of focus for improving Wasm include linear memory, tail call optimization, and multithreading.
* The panelists discuss the importance of community engagement and open collaboration in driving the development of WebAssembly.


## SQLite in Wasm: A Glimpse into the Future of Shared Libraries - Carl Sverre, Amplify Partners

URL: [https://www.youtube.com/watch?v=oLYda9jmNpk](https://www.youtube.com/watch?v=oLYda9jmNpk)

 * The speaker is excited about offline first applications and SQLite in WebAssembly (Wasm)
* Offline first applications are designed to function effectively without an internet connection and synchronize state mutations locally with a server when reconnected
* SQLite is a local database that fits well for offline first apps due to its data model and asynchronous design
* Building an offline first application involves dealing with complex problems such as conflict resolution and time management
* The speaker decided to build a collaborative, eventually consistent, synchronized database browser using SQLite in Wasm
* He chose SQL sync architecture for its simplicity and the fact that it can be easily ported between different client and server environments
* SQL sync uses a single SQLite instance running on the server that provides global ordering of mutations, while clients optimistically execute local state changes and replicate them back to the server
* Git is used as an inspiration for handling conflict resolution, with each client maintaining its own local state and the server providing an authoritative state that all clients eventually converge towards
* The speaker found success in compiling SQLite to Wasm using the Emscripten toolchain and was able to build a fully functional reducer library using Rust
* He used a reactor-style model for query execution in Wasm, allowing users to run queries and see results in real time even when offline.


## Unleashing the Power of WASM: Revolutionizing Database Scalability and Application... - RJ Atwal

URL: [https://www.youtube.com/watch?v=IDCS_b7UF0o](https://www.youtube.com/watch?v=IDCS_b7UF0o)

 * RJ Atwal, founding engineer at Mother Duck, talks about unleashing the power of WebAssembly (WASM) in databases
* Database industry's core technology hasn't changed significantly since 80s and 90s
* Traditional databases have a component-wise structure and are difficult to scale
* WASM allows for running code at the edge, which can improve performance and scalability by reducing data transfer
* WASM databases like DrB embed the entire database in the browser or on the edge server
* UDFs (User Defined Functions) have been a limitation of traditional databases due to security concerns and optimization tradeoffs
* WASM databases allow for running UDFs written in various languages without compromising SQL expressiveness and optimizations
* WASM databases like Blossom, embedded in PostgreSQL or Edge SQLite, enable client-side encryption and progressive rendering for fast queries
* Hybrid execution models using both traditional SQL and WASM components can improve performance and reduce network traffic
* The future of WASM databases includes seamless integration with existing technology stacks, improved optimization, and more efficient data management.


## Component Model: The Final Abstraction - Taylor Thomas & Liam Randall, Cosmonic

URL: [https://www.youtube.com/watch?v=WrGRxs_n2z0](https://www.youtube.com/watch?v=WrGRxs_n2z0)

 * Taylor Thomas and Liam Randall from Cosmonic discuss non-functional requirements and the component model in WebAssembly
* Component Model allows for reusable, composable code and gives developers back control of their lives by reducing boilerplate code
* The problem with free open source libraries is that they can become complex and difficult to maintain, leading to wasted time
* Virtualization and containerization have helped alleviate some of these problems by allowing for better resource utilization and separation of concerns
* WebAssembly component model provides a way to export and import components, which click together and run without the need for a shared operating system or runtime
* Components can be composed together using interfaces, providing flexibility and powerful functionality while reducing attack surface area
* WebAssembly also allows for easier API decomposition and application boundary definition, enabling faster iteration and development
* The goal is to build complex applications easily and distribute them anywhere in the world, with components running on different systems and orchestrated by WasmCloud
* Component Model is a key part of Cosmonic's Watson Cloud application runtime and has been in development for several years
* Demonstration of a simple application using WebAssembly components running on different systems, with requests being routed and processed quickly and efficiently.


## Wasm, Kubernetes, Native, or What Else? An Enterprise Architecture Debrief - Sean Isom, ex-Adobe

URL: [https://www.youtube.com/watch?v=3woiH9OSt1A](https://www.youtube.com/watch?v=3woiH9OSt1A)

 * Sean Isom discussing the importance of flexible architecture and how WebAssembly (Wasm) can help build better applications.
* Bad architecture is inflexible and may ultimately cost more in the long run, as it can prevent adaptation to changing business requirements.
* Kubernetes versus Wasm debate: Kubernetes offers stability but may introduce additional complexity for small companies or projects without the need for it. Wasm allows for isolation of code and flexibility to run on various devices with different form factors.
* WebAssembly enables sharing modules, linear memory usage, and unbundling dependencies within specific components, making it easier to isolate business logic and manage dependencies.
* Using an example of serverless functions like AWS Lambda, Wasm can help reduce dependency management burden and shift dynamic responsibilities to the runtime environment.
* WebAssembly in Kubernetes: Leverage existing infrastructure by running chunk code everywhere, enable interoperability with other components, and provide service level isolation within namespaces.
* Flexibility benefits include being able to run code on various devices and form factors, as well as reducing dependency management and maintaining a smaller codebase.
* Use cases for WebAssembly include image processing, edge computing, procedural content generation, and machine learning inference, where the ability to run code closer to the user can increase performance and reduce latency.
* Wasm provides unique opportunities by allowing flexible deployment and runtime environments without sacrificing security or isolation guarantees.


## From Wazero to Wazhero: An Introduction to Wazero for Gophers and Other Species - Edoardo Vacchi

URL: [https://www.youtube.com/watch?v=j09Svvvtd0E](https://www.youtube.com/watch?v=j09Svvvtd0E)

 * Eduardo Vacchi, from Tetrate, introduces Wazero, a Go project for running WebAssembly modules at build time
* Wazero is convenient for Go developers as it leverages the traditional Go toolchain and static linking
* Static linking allows for easy deployment and cross-compilation to various platforms
* However, drawbacks include complications with dynamic code loading and foreign function interfaces (FFI)
* Wazero provides an alternative to monolithic statically linked executables by isolating WebAssembly modules from the host code
* Wazero also supports cross-compiling to various platforms, including freeBSD and Plan 9
* Wazero's webassembly interpreter mode is the default compiler mode for go1.21 and above
* It provides performance benefits and security improvements by isolating WebAssembly modules from each other
* Wazero also supports ahead-of-time compilation for better performance on some platforms
* The project has been under development since 2020, with support from the Go community and contributions from external developers.


## Deploying Your Backend Like a CDN With Wasm - Brooks Townsend, Cosmonic

URL: [https://www.youtube.com/watch?v=goinw_B8sZw](https://www.youtube.com/watch?v=goinw_B8sZw)

 * Brooks Townsend, lead software engineer at Cosmonic, discusses deploying backends like a CDN using WebAssembly (Wasm)
* CDNs distribute static content quickly, cheaply, reliably, and securely to users around the world
* CDNs are typically used for frontend applications but can also be used for backend static assets
* Distributing entire backends with CDNs can optimize long network requests and reduce cloud egress bandwidth costs
* WasmCloud is a project that enables deploying and distributing stateless backends using Wasm, without the need for containers or Kubernetes
* WasmCloud offers automatic load balancing, seamless compute mesh, and hot swappable capabilities
* Using WasmCloud to deploy a distributed application can minimize data size and distance across the network
* Demo of deploying a hobby application called "Fruit Joke" using WasmCloud and distributing it around CDN nodes for faster response times.


## Untangle That Spaghetti Code; Make Dreamy Fettuccine Instead - Taylor Thomas & Bailey Hayes

URL: [https://www.youtube.com/watch?v=Hrsi9F7VWHw](https://www.youtube.com/watch?v=Hrsi9F7VWHw)

 * Taylor Thomas and Bailey Hayes discuss untangling "spaghetti code" in software development
* They use the analogy of cooking to explain refactoring and simplifying complex applications
* Bailey mentions his experience with Rust, Go, and AWS Cloud technologies
* They talk about the challenges of managing dependencies and updating code in monolithic applications
* They highlight the benefits of using cloud-native architectures and Wasm Cloud for deploying components independently
* Taylor demonstrates building and deploying simple applications using Wasm Cloud, including a file server and credential service
* They discuss the importance of separating business logic from infrastructure and leveraging open source technologies.


## Taking WASI-Cloud-Core for a Spin - Jiaxiao Zhou, Microsoft & Joel Dice, Fermyon Technologies

URL: [https://www.youtube.com/watch?v=W-ubCAMAJQc](https://www.youtube.com/watch?v=W-ubCAMAJQc)

 * Joel Dice and Jiaxiao Zhou discussing WASI-Cloud-Core
* Motivation: Portable platform for cloud applications, decoupling business logic from platform concerns
* Key features of cloud-native applications: containerization, stronger security requirements, need common capabilities like key-value store, messaging, and SQL
* WASI-Cloud-Core as an accelerator for cloud-native trends: language neutrality, sandbox support, linkable modules
* Comparison with MapReduce: simple interface, powerful distributed processing
* Goals of WASI-Cloud-Core: accessing key-value store, durability, exchanging event messages, blob storage, inbound/outbound HTTP requests, changing runtime configurations, and transaction management
* Use cases: serverless functions, web crawlers, microservices, multitenant scenarios, and edge environments
* Benefits: low startup latency, quick switching between workloads, minimal gap between average and peak load, and efficient use of resources.


## Bridging the Architecture Divide: How Hardware Limits Wasm, and How We Can Do Better - Tal Garfinkel

URL: [https://www.youtube.com/watch?v=RJcvNEeC1vw](https://www.youtube.com/watch?v=RJcvNEeC1vw)

 * Tal Garfinkel from UC San Diego discussing limitations and optimizations in WebAssembly (Wasm) and possible solutions using Hardware techniques.
* Current hardware isolation mechanisms, like Segmentation and Color Guard, provide performance benefits but have limitations in security, scalability, and compatibility.
* Segmentation:
  + Page table-based memory protection has overhead and wasting space in Wasm.
  + WebAssembly's poor man segmentation using compiler-given segmented memory model avoids Hardware overhead.
  + Guard Regions can accelerate bounce checks but waste space.
* Color Guard:
  + Hardware-assisted fault isolation extension enables faster and secure sharing of memory isolation with minimal overhead.
  + Intel's Simple Set Extension targets addressing the Wasm problem, allowing for cool use cases like microsecond to nanosecond scale contract switches and high concurrency low latency Edge compute platforms.
* Limitations:
  + Virtualization tax and wasification tax hinder performance in Wasm compared to native workloads.
  + Specter safety limits scalability due to its basic math and 32-bit memory instance size.
  + Guard Regions don't always get used efficiently and still require conditional bounce checks, which can be expensive.
* Optimizations:
  + Segway is a clever trick using x86 segmentation for speed improvements in Wasm.
  + Multiyear collaboration between Intel and researchers aims to overcome limitations with Next Generation processors.
  + Hardware-assisted fault isolation provides fast and secure isolation without adding overhead.
* Future work:
  + Support for several critical use cases, such as running unmodified native binaries and custom isolation systems like Uber cage.
  + Provide compatibility with existing code architecture by using a simple notion of regions and explicit region types.
  + Explicit data regions can improve performance and protect against Specter attacks while also supporting code regions and software CFI for native isolation.


## Kotlin/Wasm: Today and Tomorrow - Zalim Bashorov, JetBrains

URL: [https://www.youtube.com/watch?v=Zy2SrhV5ESA](https://www.youtube.com/watch?v=Zy2SrhV5ESA)

 * Zalim Bashorov from JetBrains has been working with Kotlin for 10 years, leading the team behind it
* Kotlin is a programming language developed by JetBrains, known for its safety features, static typing, and automatic memory management
* Kotlin supports multiple compilation targets including JVM, native, JavaScript, fiber assembly, and WebAssembly
* WebAssembly (Wasm) is important as it allows sharing code easily across platforms without writing platform-specific code
* Kotlin/Wasm has several experimental proposals such as exception handling, type function difference, and garbage collection
* The exception handling proposal introduces a dedicated section for storing name entities to improve debugging experience
* WebAssembly is useful for the language's entry into the time as it offers smaller binary size and better runtime performance
* Chrome provides better support for Kotlin/Wasm and makes it easier to set up and use in the browser
* Other popular browsers like Firefox also support Kotlin/Wasm but users need to turn it on manually
* The easiest way to try Kotlin/Wasm is by using online program playgrounds that provide code completion, debugging features, and embedded documentation.
* Predefined browser APIs can help get quick feedback and make typo corrections when writing Kotlin/Wasm code in the browser
* Kotlin/Wasm libraries like Kawasaki offer support for creating clean server applications with high frame rates
* Composable UI frameworks like Jetpack Compose make it easy to prototype and share UI components inside the browser.
* WebAssembly has great potential for server-side applications, especially in areas like Lambda functions, Edge Computing, and microservices.
* Kotlin/Wasm can be used outside of the browser but requires specific setup and support from browsers.
* Garbage collection and exception handling are important proposals for Kotlin/Wasm, with garbage collection being in the experimental phase and exception handling being in the proposal phase 4.
* The future of Kotlin/Wasm looks promising with continuous improvements and new features being added to enhance its capabilities.


## Let's Build a Linux Just for Wasm! - Andrew Randall & Ralph Squillace, Microsoft

URL: [https://www.youtube.com/watch?v=dEeLo-LKf88](https://www.youtube.com/watch?v=dEeLo-LKf88)

 * Andy and Ralph discuss the history of containers and the evolution of WebAssembly (Wasm)
* Wasm is moving towards a full native experience with improved UX, individual projects having smooth experiences, and industry-standard runtime environments
* Flatcar Linux is a community-driven project that can be used to build a Linux distribution specifically for Wasm
* The process involves creating an immutable image using tools like Flatcar, Docker, and QEMU, and deploying it with an automated update mechanism
* Flatcar Linux is inspired by Chromebooks and aims to provide quick updates and automatic rollbacks for fleet management
* The speakers demonstrate the process of baking a Wasm image using Flatcar and discuss various tools and concepts like ignition files, raw layer files, and system extension directories.


## Introducing Componentize-Py: A Tool for Packaging Python Apps as Components - Joel Dice

URL: [https://www.youtube.com/watch?v=PkAO17lmqsI](https://www.youtube.com/watch?v=PkAO17lmqsI)

 * Joel Dice, Principal Engineer at Firon, discussing Python integration with the WebAssembly ecosystem
* Previous vision of fulfilling polyglot promise of web assembly by supporting a wide variety of host environments, including Python
* Componentize-Py introduced to address packaging and running Python apps as components in WebAssembly
* Prior art solutions for targeting WebAssembly using Python already exist, such as Pyodide and Wasmtime
* Discusses static linking vs dynamic linking and the advantages of component linking in WebAssembly
* Componentize-Py allows for easier versioning, sandboxing, and isolation of third-party dependencies
* Comparison between Python and WebAssembly: WASM wants to create a better ecosystem by moving beyond legacy posix systems
* Componentize-Py uses a repository on GitHub with static dependency application dependencies, using components that are strictly enforced in a sandboxed environment
* Discusses the process of prelinking, generating bindings, and initialization in WebAssembly using Python.


## Dapr-Enabled Wasm Microservices - Michael Yuan, WasmEdge & Yaron Schneider, Diagrid

URL: [https://www.youtube.com/watch?v=n_q8S4GbjOw](https://www.youtube.com/watch?v=n_q8S4GbjOw)

 * Dapper project: open-source framework for building microservices using Wasm and other runtimes
* Dapper helps developers focus on business logic while handling infrastructure concerns, such as database configuration, cache, stateful applications, event-driven systems, and more
* Supports various platforms like Kubernetes, AWS, Azure, and others
* Offers integrations with popular cloud services and open-source infrastructure services
* Provides a simple HTTP API for communication between microservices
* Allows running processes locally or in the cloud, even replacing databases and pub/sub systems with Dapper's features
* Improves performance through high-performance networking and non-blocking sockets
* Enhances security by applying authentication, rate limiting, and concurrency control transparently
* Supports various programming languages like Rust, Python, Go, and more
* Dapper is part of the CNCF landscape and has a large and growing community (>3000 contributors) with a rapidly growing Discord channel
* Previously started as an adaptation for running microservices in Wasm, but now also helps with adoption by providing adapters and integrations
* Dapper is not just another layer on top of existing ecosystems; it matches the existing stack and improves productivity
* Some benefits over traditional cloud services include not requiring a client driver or container VM, supporting WebSocket and grpc interfaces, and offering built-in authentication and other features.


## Package Management for Wasm Components - Daniel Macovei, JAF Labs

URL: [https://www.youtube.com/watch?v=1QbfKzQgD0E](https://www.youtube.com/watch?v=1QbfKzQgD0E)

 * Danny Macovei from JAF Labs discusses package management for Wasm components
* Warg is a project by Sig Registries in the Bundle Alliance focused on creating a webassembly registry with cryptographic verifiability and federated characteristics
* Package managers are an integral part of development processes, enabling language neutrality and dependency tree analysis
* Interoperability between languages is a key benefit of Wasm components, allowing developers to leverage existing ecosystems
* The component model enables guest interaction and transitive dependencies through canonical APIs
* Component models work by importing one component into another and instantiating it multiple times with different arguments
* Locking components ensures that the same version is used across instances and prevents dependency conflicts
* Registry-aware runtimes can automatically manage dependencies and provide integrity checks, making production deployment safer
* Demonstration shows using handwritten Wasm components in JavaScript, Rust, and Zig to create a large bundled component through transitive dependencies
* Different programming languages have different maturity levels and tooling for creating components via various methods.


## The Buzz About Green Tech: WebAssembly's Impact on Carbon Footprint Reduction - Christoph Voigt

URL: [https://www.youtube.com/watch?v=zi4d4Hu1HtY](https://www.youtube.com/watch?v=zi4d4Hu1HtY)

 * Christoph Voigt, co-founder of Liquid Reply, discusses the potential of WebAssembly for creating energy-efficient systems
* Underutilization of Kubernetes resources is a common issue leading to unnecessary carbon emissions
* WebAssembly offers several advantages including portability, performance, language independence, and security
* Energy efficiency is an emerging area where WebAssembly shines, particularly in serverless and IoT use cases
* A study shows that the choice of programming language and runtime environment can significantly impact energy consumption
* Rust, a low-level language, is one of the most energy-efficient languages for benchmarked applications
* WebAssembly's small binary size makes it an attractive choice for lightweight applications
* The performance of WebAssembly depends on the maturity of its compiler support and optimization features
* The runtime environment can also influence the energy consumption and performance of WebAssembly applications
* The green software foundation proposes a carbon footprint equation that considers both operational and embodied emissions.
* Energy efficiency should focus on reducing hardware requirements, optimizing energy supply, and minimizing idle time.
* Multitenancy in web assembly security profiles make ideal multi-tenancy scenarios given fully isolated applications.
* Serverless functions written in WebAssembly can save energy by utilizing hardware more efficiently and minimizing embodied emissions.
* WebAssembly's snapshotting functionality allows pre-initializing modules, improving startup latency and reducing energy consumption.
* Future work includes exploring the potential of using solar power for web assembly instances and serverless operating models.


## Doing Server Side WebAssembly the Hard Way - Liam Crilly, NGINX

URL: [https://www.youtube.com/watch?v=T8TcRGfGkEQ](https://www.youtube.com/watch?v=T8TcRGfGkEQ)

 * Liam Crilly talks about the evolution of web technology from Mosaic browser in the early 90s to the current day
* He mentions WebAssembly as a significant event that could empower the next wave of web applications
* Discusses the importance of HTTP context and how it has evolved over time
* Talks about the challenges and solutions for decoupling network layer and runtime in server-side web development with Nginx and WebAssembly.

Some key points:

* Early graphical web brought a surge in content creation and consumption
* First web applications were simple, with guestbooks, counters, and form submissions
* HTTP evolution included the introduction of POST method, image tag, and query strings
* Early frameworks like Ruby on Rails made web development easier by providing rich user experiences without requiring complete reimplementation of backend logic
* WebAssembly allows for running application code directly in the browser without installing software
* Decoupling network layer and runtime can improve scalability and security.

Liam's background:

* Worked at Nginx on server-side WebAssembly
* Started writing web applications in the 90s with a simple guestbook
* Mentioned using languages like PHP, Python, Ruby, and Go for web development over the years.


## Piercing the Veil of WebAssembly in Production - Benjamin Eckel, Dylibso

URL: [https://www.youtube.com/watch?v=Dd2Ped1xFG0](https://www.youtube.com/watch?v=Dd2Ped1xFG0)

 * The talk is about observability in WebAssembly (Wasm) production environments
* Speaker Ben Eckel is from Delipso and has worked at Datadog, a monitoring and observability company
* Wasm adoption in production systems is increasing, but observability tools don't work well with it yet
* Traditional observability tools rely on agents or side processes to collect data, which isn't an option for Wasm due to its sandboxed environment
* Wasm has no unified way of accessing system resources like a clock or IPC layer, making it difficult to get Telemetry data
* To address this, the speaker suggests using language-level bindings and adapters to safely call observability libraries
* The goal is to make observability as efficient and quick as possible in Wasm environments, without affecting performance
* The speaker also mentions exploring the possibility of real-time configuration changes and automatic instrumentation for Wasm modules.


## Inside the Wizard Research Engine - Ben Titzer, Carnegie Mellon University

URL: [https://www.youtube.com/watch?v=HUB4WEcjEKI](https://www.youtube.com/watch?v=HUB4WEcjEKI)

 * Ben Ive, researcher at Carnegie Mellon University, talks about his research on Wizard, a webassembly-based research engine
* Webassembly: standardized compiled executable code, portable and can represent many contexts
* Background in Java VM implementation and optimization
* Focus on building a research engine with new capabilities and architecture
* Interest in webassembly due to its potential for new optimization techniques and flexibility
* Goals include improving debugging tools and observability for production VMs
* Exploring new runtime techniques and optimizations for webassembly
* Comparing Wizard to other virtual machines (V8, JVM) and considering the tradeoffs between observability and performance
* Discusses his paper on interpreter-based analysis techniques for webassembly, including probing and call profiling
* Plans to extend Wizard to support new languages and features.


## Implementing a WASI Host for Visual Studio Code - Dirk Bäumer, Microsoft

URL: [https://www.youtube.com/watch?v=3GT4Z_8L2cg](https://www.youtube.com/watch?v=3GT4Z_8L2cg)

 * Dirk Bäumer, Microsoft employee with a long history in IDEs and editors
* Introducing implementation of WASM (WebAssembly System Interface) host for Visual Studio Code (VSCode)
* Goal: Run local files without installing VSCode, support multiple languages, and use the GitHub repository system
* Challenges: Local file execution, Python interpreter integration, and origin isolation
* Technologies used: Textmate grammars, WASM, VSI (Visual Studio Intellicode Services Interface)
* Preview of demo showing VSCode Dev Insider version running a Python script locally without the need for a server or Python interpreter installation
* Implementation involved mounting the workspace file system inside VSCode and using the Python interpreter within it
* Limitations: Current public preview has limitations around origin isolation, CPython build, and thread support
* Future plans: Improvements to Python interpreter, better threat support, and integration of other languages into VSCode Dev Insider.


## WASM in ByteFaaS, Past, Present, and Future - Wilson Wang, ByteDance

URL: [https://www.youtube.com/watch?v=IfIaugj_3S8](https://www.youtube.com/watch?v=IfIaugj_3S8)

 * Wilson Wang from ByteDance discussing use of WebAssembly in ByteFast (ByteDance Fast Platform)
* Three parts: Legacy environment, current implementation, future research
* Legacy environment: Two types of functions - native and event-driven, container-based architecture
* Optimization in legacy environment: Continuous optimization, snapshotting, pooling, initialization
* Limitations of optimization: Cost, system call overhead, isolation
* Current implementation: Introduced lightweight WebAssembly worker, faster system, Gateway, agent, sandboxing, precompilation
* Future research: Next-generation assembly-based fast system, Weaver service for distributed computing.
* Weaver service components: Execution scheduling, execution, host calls, actor tasks
* Challenges in integration and rearchitecture: Building with Bazel, profile execution results, scaling task actors, improving throughput.
* Demonstration of WebAssembly function execution using Ray and demo of mobile inference using Western Match.
* Future work: Improvements to West Mount Ray, adding support for different languages (C++, Rust) and SDKs.
* Questions: Comparing container latency, handling larger data sizes, use cases for WebAssembly functions, integrating Rust with Western Match.



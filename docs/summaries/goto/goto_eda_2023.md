## Event-Driven Integration Today & Tomorrow • James Urquhart • GOTO 2023

URL: [https://www.youtube.com/watch?v=FEcRuGzrNRs](https://www.youtube.com/watch?v=FEcRuGzrNRs)

 * James Zurek discussed flow architecture and its importance in moving data around the internet, using a water cycle metaphor
* Flow refers to movement within a system, specifically flow in vent-driven integration across organizational boundaries
* Standard interface protocols like HTTP, web sockets, and message queues (Kafka, NSQ, RabbitMQ) enable efficient communication between producers and consumers
* Data gravity is a concept where data pulls applications and services closer due to its value and importance
* Real-time movement of data creates additional value and is essential in industries like finance, traffic systems, and inventory management
* Event Bridge is a smart event bus that simplifies real-time integration between different systems and services
* Cloud events provide a consistent way to describe metadata across various protocols and technologies
* AI models benefit from real-time data feedback loops for improved accuracy and performance.


## Building Practical, Cost-Efficient GenAI Solutions Using Serverless • Veda Raman • GOTO 2023

URL: [https://www.youtube.com/watch?v=-X-YHHU7p20](https://www.youtube.com/watch?v=-X-YHHU7p20)

 - Speaker is an AIML Solutions Architect with experience in serverless solutions and generative AI applications.
- Discussed building machine learning applications using large language models and serverless architecture.
- Three phases of AI model development: design, training, evaluation, and inference.
- Design phase involves data collection, feature engineering, and algorithm selection.
- Training phase uses labeled data to train the machine learning model, which can be intensive and may require multiple CPUs or GPUs for distributed training.
- Evaluation phase tests model accuracy using test datasets and iterates through design changes if needed.
- Inference phase involves making predictions on unseen data using the trained model.
- Prompt engineering is important in generative AI applications, as it determines how the model responds to user queries or prompts.
- Amazon Bedrock is a serverless service for accessing large language models and their APIs for prompt engineering.
- Probabilistic vs deterministic AI models: deterministic models provide consistent answers, while probabilistic models generate different answers based on the context.
- Common use cases for AI include audio/video transcription, text summarization, and data extraction from unstructured formats.
- Amazon Textract, Transcribe, and Bedrock are AWS services that can help meet these requirements.
- Cost efficiency and real-time processing are important considerations when building AI applications.
- AWS Step Functions can be used to create automation workflows for machine learning tasks.
- To optimize cost, consider using serverless services like Amazon Textract, Transcribe, and Bedrock APIs, as well as distributed processing through Step Functions.


## Journey to EDA: Patterns, Best Practices & Practical Tips • David Boyne • GOTO 2023

URL: [https://www.youtube.com/watch?v=39ujoTd2CJI](https://www.youtube.com/watch?v=39ujoTd2CJI)

 - Dave, a developer advocate at AWS, discussed his experience implementing event-driven architecture in various projects and organizations.
- Event-driven architecture provides business agility, decoupled architecture, experimentation, and evolution capabilities.
- Common pitfalls include unclear boundaries, synchronous versus asynchronous thinking, and misunderstanding the behavior system.
- Pizza ordering example used to explain event architecture benefits and challenges: state management, event-driven vs synchronous communication, and complexity.
- Event storming is a recommended approach for identifying and modeling events in an event-driven architecture.
- AWS services like Amazon EventBridge, Lambda, SQS, API Gateway, DynamoDB, and Step Functions were mentioned as useful tools in implementing event-driven architectures.
- Governance, standardization, and discoverability are important considerations when implementing event-driven solutions.
- The speaker emphasized the importance of understanding the behavior system first, using event storming for identifying and modeling events, and considering various patterns like point-to-point messaging, publish-subscribe, and stream processing.


## Bringing EDA to the Containers World • Jessica Deen • GOTO 2023

URL: [https://www.youtube.com/watch?v=DrUFMSsCTZM](https://www.youtube.com/watch?v=DrUFMSsCTZM)

 - Jessica Dean discussed Eda container world, focusing on Elastic Container Service (ECS) and serverless containers
- The need for change in technology industry: organizations require agility to iterate faster and keep up with volatile macro conditions
- DevOps definition: a culture that enables continuous delivery of value through collaboration between development, operations, and product teams
- Serverless containers: enable focus on application delivery while AWS manages infrastructure
- Fargate serverless compute engine: simplifies container operation by removing the need for managing EC2 instances or hypervisors
- ECS vs Lambda: different compute options based on specific use cases (memory, execution time) and event sources
- Event Bridge: a service bus that connects services in the AWS ecosystem to process events asynchronously
- Step Functions: a serverless workflow service for defining and coordinating multi-step applications
- Autoscaling: ECS can be scaled based on metrics, such as CPU usage or queue depth, using custom policies and integration with other AWS services (SQS, Kinesis)


## Empowering Architectural Evolution: Governing Event-Driven Solutions • Sam Dengler • GOTO 2023

URL: [https://www.youtube.com/watch?v=-Pv_kYflEEg](https://www.youtube.com/watch?v=-Pv_kYflEEg)

 - Eric from Capital One discussed governance in the context of adventure architecture, focusing on resiliency and developer experience.
- Eda (Event Driven Architecture) plays a role in making systems more resilient and decoupled by introducing concepts like metadata catalogs, schema registration, and versioning.
- Discoverability is crucial in large organizations where people need to understand the available information for problem solving.
- Standardization of metadata and data formats can make it easier for producers and consumers to interact.
- Producers are responsible for publishing well-formed events, while consumers validate received events based on their context.
- Consumers want an easy developer experience with focus on observability, troubleshooting, and authoring/delivery of code.
- The use of a metadata catalog can help organizations manage access to sensitive information and implement self-service mechanisms.
- Access control is another important aspect of event handling in large organizations.
- Consumers validate events for correctness and ensure they meet required fields and context.
- Producers may need to validate completeness, and there are various ways to handle invalid or incorrect events.
- Event catalogs can help people find relevant events quickly and easily by providing search and tag categorization features.
- The Event Catalog project by David Bo is an open source tool for documenting event schemas and discovering based on search tags and categorization.


## Evolving Your Containerized REST Based Microservices to Adapt to EDA • Dhiraj Mahapatro • GOTO 2023

URL: [https://www.youtube.com/watch?v=kjZdKa5I-Us](https://www.youtube.com/watch?v=kjZdKa5I-Us)

 * Duraj Mahapatra, Principal Servic specialist, focuses on Financial Services and has experience with Java, Groovy, Grails, AWS Lambda, and serverless architecture
* Event Driven Architecture (EDA) is discussed as a new concept in the industry, providing benefits like decoupling producer and consumer, independent scaling, and reliability
* Traditional architecture is compared to EDA, highlighting issues like tight coupling, synchronous invoking, and multiple point failures
* EDA components include event router, event broker, and event store
* Event routing allows for asynchronous communication and decoupling of services, enabling independent scaling and improved reliability
* Asynchronous architecture also enables handling of worst-case scenarios more efficiently, allowing for faster response times and reduced area impact when adding new features or services
* The speaker mentions using AWS services like Amazon Event Bridge, SQS, Lambda, and ECS to build an insurance claim processing application as an example of EDA implementation.
* Key benefits of EDA include handling large scale data processing, reducing area impact, and facilitating evolutionary thinking in the system design.


## Scaling Kubernetes-based Event-driven Workloads with Keda & Karpenter • Roland Barcia • GOTO 2023

URL: [https://www.youtube.com/watch?v=QaPbcayEicw](https://www.youtube.com/watch?v=QaPbcayEicw)

 - Roland Barcia, a worldwide director at AWS, discussed his background in software development and experience with various technologies like JMS, CORBA, and containerization.
- He highlighted the importance of cloud technology and shared an example of using multiple AWS services together to create a gaming application.
- Barcia mentioned working on a team that used Kubernetes for scaling and managing containers, and discussed the use of tools like kada and eks node viewer for monitoring and managing the infrastructure.
- He emphasized the importance of capacity planning and auto-scaling using tools like HPA (Horizontal Pod Autoscaler) and Kubernetes Cluster Autoscaler.
- Barcia also touched upon the benefits of using Carpenter, an open-source project for container and serverless integration, for managing and scaling applications on AWS.
- He demonstrated how to use Carpenter to create a new node and scale pods based on demand.
- Throughout the presentation, he discussed various AWS services like ECS (Elastic Container Service), Fargate, Lambda, SQS (Simple Queue Service), and Kafka, among others.
- He also mentioned the importance of observability tools like Prometheus, Grafana, and Loki for monitoring applications in a cloud environment.


## Use Solace & AWS to Create a Global EDA Backbone • Michael Hilmen & Chintan Sanghavi • GOTO 2023

URL: [https://www.youtube.com/watch?v=HjtDeMJIV_I](https://www.youtube.com/watch?v=HjtDeMJIV_I)

 - The speaker discusses Event-Driven Architecture (EDA) and its benefits, using AWS as an example
- EDA allows for real-time processing of data with low latency
- Use case examples include inventory management in retail stores and loyalty programs
- Batch processing vs real-time mode: Inventory availability in stores and web portals
- Improved customer satisfaction and increased sales are business benefits of EDA
- Technical benefits include better scalability, resiliency, cost savings, and reduced complexity
- Key components of an EDA system include publishers, consumers, brokers, and metadata
- Selecting a broker involves functional and nonfunctional criteria such as reliability, compliance, hybrid architecture support, and dynamic filtering/routing
- Case studies: Mcari Bank's migration to AWS using Solace event mesh, United Airlines implementing EDA for real-time data across their enterprise.


## Serverless & Event-driven Patterns for GenAI • Uma Ramadoss & Dhiraj Mahapatro • GOTO 2023

URL: [https://www.youtube.com/watch?v=dzW3-Mol1yo](https://www.youtube.com/watch?v=dzW3-Mol1yo)

 * Im Duraj Mahapatra, Principal Specialist at ESS, discussing Financial Services and generative AI using serverless architecture.
* Umar Radas, Solutions Architect at AWS, focusing on serverless and event-driven pattern applications in generative AI.
* Agenda: Introduce generative AI, its fit in the industry, and an overview of Amazon Bedrock for building generative AI applications.
* Generative AI Foundation model: Pretrained large language model used to create text, images, and more. Already trained on vast data sets.
* Event-driven pattern: Helps build generative AI applications by dealing with text and providing context for generating new content.
* Short prompting: Provide context to the LLM (large language model) for generating accurate responses. Use Amazon Bedrock for API calls, caching, and rate limiting.
* Fine-tuning: Adjust the LLM's response based on specific use cases and applications.
* Serverless architecture: Handles traffic spikes, scales relatively easily, and offers flexibility in changing specifications.
* AWS services used: Amazon Bedrock, SageMaker Jump Start, Lambda functions, ECS, API Gateway, SQS, SNS, and DynamoDB.
* Industries using generative AI: Healthcare (medical transcription), Insurance (claim processing), and marketing content generation.
* Challenges in using Foundation model: Building applications that work with business logic, context awareness, and zero-shot prompting.
* Patterns for consuming foundation models: Chatbot example, synchronous pattern, caching, and rate limiting.
* Workflow patterns: Workflow (Step Functions), invoking multiple models, and document processing using SageMaker.
* Event Bridge and SNS: Distributed message handling with parallel processing and filtering.
* Document summarization: Using S3, SageMaker, and distributed map capabilities for scale and cost-effectiveness.
* AWS SDK Integrations: Calling text models and stagemaker endpoints directly.


## Unlocking Faster & Efficient Data Processing w/ Serverless • Uma Ramadoss & Adam Wagner • GOTO 2023

URL: [https://www.youtube.com/watch?v=Mbt78pAfuOs](https://www.youtube.com/watch?v=Mbt78pAfuOs)

 * Adam Wagner and Umar Ramadas discussed large-scale data processing using AWS Step Function and Lambda.
* Pain points in processing large data sets include variability, scalability, and integration.
* Invoice processing use case: A common business process with various invoice formats, requiring data extraction, verification, and payment processing.
* Solutions for handling large-scale data processing include distributed computing, using multiple compute nodes, and coordinating tasks to manage interactions.
* Step Function offers benefits like faster time-to-market, scalability, cost effectiveness, and ease of managing concurrency.
* AWS Lambda allows developers to write code without worrying about server provisioning or scaling.
* Step Function's visual workflow designer simplifies development by reducing the need for writing extensive logging code.
* Distributed map functionality in Step Function enables parallel processing of large data sets and integrates with S3 for efficient data access.
* The use case of processing worldwide weather data from 1929, with a dataset totaling 40GB, demonstrates the power of distributed map processing using AWS services.


## A Year of Diagnosing Pediatric Cancer with Event Driven Architecture • Grant Lammi • GOTO 2023

URL: [https://www.youtube.com/watch?v=tpVPgGH4LfE](https://www.youtube.com/watch?v=tpVPgGH4LfE)

 - Grant from Rest M Institute at Nationwide Children's Hospital discusses genomic medicine and real-world example of a serious project they've worked on in the past 18 months.
- Genomics is complicated and involves dealing with large amounts of data, decrypting and aligning sequences, and interpreting results.
- They discussed a molecular characterization initiative that started a few years ago to analyze tumors and normal sequences for differences using various pipelines and assays.
- The project involved sending tissue/blood samples, receiving clinical reports, and sharing deidentified data with researchers around the world.
- They use a variety of tools like S3, Lambda, Step Functions, and DynamoDB to process and store data.
- The pipeline includes event bridge, which sends messages between different services, and various caching techniques for improved performance.
- They discussed the importance of extensibility, security, and scalability in their clinical environment.
- They've been able to help many kids by analyzing their cases and providing results that can lead to better diagnoses and treatments.
- They've learned valuable lessons about handling large amounts of data, automating processes, and interpreting results efficiently.
- They've also discussed the challenges of working with complex genomic data and the importance of human intervention in the process.


## Realtime Serverless Communication with Momento Topics • Allen Helton • GOTO 2023

URL: [https://www.youtube.com/watch?v=GeB_EiDIHWk](https://www.youtube.com/watch?v=GeB_EiDIHWk)

 - Realtime Notification: Architecture, use cases, and benefits discussed
- Definition: Realtime notification as event-triggered, low latency, two-way communication between client and server
- Architecture: API Gateway, Lambda functions, Dynamo DB, SNS, Iot Core, and EventBridge used for implementing realtime notifications
- WebSockets vs. Push Notifications: Misconceptions clarified; WebSockets are stateful, one-to-one connections, while push notifications are server-side messages sent to clients
- Stateless vs. Stateful Connections: Comparison of stateless and stateful connections in realtime notification systems
- Architecture Diagram: Overview of a serverless realtime notification system using AWS services
- Sending Messages: Discussion on sending messages using Lambda functions, Dynamo DB streams, and EventBridge
- Security: Token-based access control and permission levels for topics
- Use Cases: Examples provided in various industries like farming, fantasy football, feature flags, and chat applications
- Benefits: Scalability, fast processing, and ease of implementation highlighted as advantages of using realtime notifications.


## Accelerating Event-driven Architecture with Domain-driven Design • Brian Zambrano • GOTO 2023

URL: [https://www.youtube.com/watch?v=FG4UOoEJvBc](https://www.youtube.com/watch?v=FG4UOoEJvBc)

 - Brian Zbrogger, AWS Solutions Architect, introduces himself and the topic: Accelerating Event-Driven Architecture using Domain-Driven Design
- Definition of Event-Driven Architecture (EDA): A style of building loosely coupled systems where components communicate by emitting and responding to events
- Benefits of EDA in distributed systems: Loose coupling, avoiding cascading failure effects, and simplifying complexity
- History of EDA: Originated in the late 90s with the paper "The Design of the Eventlet System"
- Challenges of building event-driven systems: Distributed systems are complex, and EDA adds another layer of complexity
- Tools and patterns for implementing EDA: CQRS (Command Query Responsibility Segregation), Saga pattern, message brokers, and domain-driven design
- Finding the domain boundary in a problem domain: Identify subdomains, use a shared language, and create a model around specific purposes
- Event Storming: A workshop-based approach to discover and understand complex domains by modeling events and their interactions
- Adding business value: Use sticky notes to prioritize areas based on time saved, cost, reputation, or impact
- Getting the boundary right: It's a crucial design decision when building software; use one team per bounded context and organize your software accordingly.


## Future of EDA Panel • J. Deen, T. Boiteau, E. Shea, V. Panghal, R. Barcia & J. Beswick • GOTO 2023

URL: [https://www.youtube.com/watch?v=P1rD2Bx7WKc](https://www.youtube.com/watch?v=P1rD2Bx7WKc)

 - The panelists discussed the growing adoption of event-driven architecture (EDA) in various industries, including Finance, Retail, and Healthcare.
- EDA provides a simple way for organizations to extend functionality and grow modern applications and cloud infrastructure.
- EDA enables agility by allowing teams to build and deploy new features quickly.
- Step Functions is a popular AWS service used for building serverless workflows in an event-driven architecture.
- Event Bridge (formerly known as EventBridge Serverless Application Model) allows developers to easily create event sources, routes, and targets using simple YAML files.
- EDA helps organizations handle massive data processing efficiently by providing cost performance benefits over services like Glue Spark jobs.
- Step Functions supports both standard and express workflows for handling different types of workloads.
- One common request from customers is the ability to react to events and influence workflow progress based on receiving an event.
- SNS and SQS support various options, including sending infinite amounts of data and maintaining exact message ordering, depending on specific use cases.
- EDA is a good fit for AI workloads as many processes are naturally asynchronous and can benefit from human interaction and approval steps.
- Decoupling teams and using event-driven architecture helps build successful applications by enforcing best practices across the organization.
- Observability is essential in event-driven architectures, with services like CloudWatch Metrics providing valuable insights.
- Serverless Land is a resource for learning about serverless patterns and best practices, including the use of Step Functions and AWS Lambda.
- Dead Letter Queues (DLQs) are crucial in messaging systems as they help handle errors and improve customer experience by redriving messages back to their original source.



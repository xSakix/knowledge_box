## Standalone Components: The Motivation | Pawel Kozlowski | ng-conf 2022

URL: [https://www.youtube.com/watch?v=hnVckmM6GZk](https://www.youtube.com/watch?v=hnVckmM6GZk)

 - Introducing Standalone components in Angular 14
- Motivation: Improve developer experience, eliminate confusion around NG Models and energy models
- Benefits of Standalone components:
    + Smaller subset of components
    + Easier compiler work
    + Clearer dependencies
- Importing Standalone components directly using JavaScript imports
- Preserving the existing Angular ecosystem and compatibility with existing applications
- Interoperability between NG Models and Standalone components
- Possible syntax changes in future versions of Angular
- Continuous conversation and feedback from the community for further improvements

**Summary:**
* Introducing Standalone Components: Improve developer experience, eliminate confusion around NG Models and energy models.
  * Benefits: Smaller subset of components, easier compiler work, clearer dependencies.
  * Importing: Directly using JavaScript imports.
  * Ecosystem: Preserving the existing Angular ecosystem and compatibility with existing applications.
  * Interoperability: Between NG Models and Standalone Components.
  * Future Changes: Possible syntax changes in future versions of Angular.
  * Community Engagement: Continuous conversation and feedback from the community for further improvements.


## Angular Team Keynote | Minko Gechev, Sarah Drasner, Madleina Scheidegger | ng-conf 2022

URL: [https://www.youtube.com/watch?v=CABHcf1gCbg](https://www.youtube.com/watch?v=CABHcf1gCbg)

 - Overview of Angular's past and present
  - Introduction of new features like Standalone components, TypeScript 4.1 support, and improved error messages
- Focus on developer experience and performance improvements
  - Partnership with Aurora team to improve core web vitals and optimize build pipelines
  - Ramping up partnership with Firebase for deployment and hosting
  - Improvements in image directive and build optimization
  - Expansion of the Angular ecosystem through community contributions and partnerships
- Future direction and upcoming features
  - Work on server-side rendering, partial hydration, and reactivity improvements
  - Collaboration with the Chrome DevTools team for better debugging experience and stack trace analysis
  - Continued focus on accessibility, component improvement, and documentation enhancements

### Summary:
* Overview of Angular's past and present
    * Introduction of new features like Standalone components, TypeScript 4.1 support, and improved error messages
* Focus on developer experience and performance improvements
    * Partnership with Aurora team to improve core web vitals and optimize build pipelines
    * Ramping up partnership with Firebase for deployment and hosting
    * Improvements in image directive and build optimization
    * Expansion of the Angular ecosystem through community contributions and partnerships
* Future direction and upcoming features
    * Work on server-side rendering, partial hydration, and reactivity improvements
    * Collaboration with the Chrome DevTools team for better debugging experience and stack trace analysis
    * Continued focus on accessibility, component improvement, and documentation enhancements


## Angular: A Design Review 10 Years Later | Jeremy Elbourn & Alex Rickabaugh | ng-conf 2022

URL: [https://www.youtube.com/watch?v=IY-QOz4oLCE](https://www.youtube.com/watch?v=IY-QOz4oLCE)

 - 10-year retrospective of Angular
    * Fundamental aspects: automatic Global change detection, unidirectional data flow, use of selectors, component RxJS fact, and embrace of compilation
    * Design choices that led to tradeoffs in performance, accessibility, and developer experience
    * Evolution of Angular's design philosophy
        + Role of Zone.js and its impact on the framework's efficiency
        + Future of Angular: Ivy and potential improvements in typescript integration
    * Importance of community feedback and how it has influenced Angular's development

- No context provided for additional points.


## RxJs from Scratch | Alain Chautard | ng-conf 2022

URL: [https://www.youtube.com/watch?v=nQrMgNIvqxM](https://www.youtube.com/watch?v=nQrMgNIvqxM)

 - RxJS is a library for reactive programming in JavaScript, allowing developers to work with asynchronous data streams and events efficiently.
- An Observable represents a sequence of zero or more values over time, emitting values synchronously or asynchronously, errors, or completion signals.
- RxJS operators are functions that transform or manipulate observables, providing over 120 operators for filtering, mapping, concatenating, and combining operations.
- A Subject is a special type of Observable that can both emit values and accept new Observers, useful for creating shared state between components or services.
- A BehaviorSubject always emits the latest value when a new Observer subscribes, making it ideal for storing and sharing state data.
- A ReplaySubject can replay the last N values whenever a new Observer subscribes, which is useful for caching and reusing previous values in an application.
- In an exercise, you create a custom observable using a service to manage country selection and display current countries on the screen. You use the Subject class to emit values from the service and implement two different operators (map and filter) to transform and manipulate the observable sequence.


## Angular based Micro frontends with module federation | Manfred Steyer | ng-conf 2022

URL: [https://www.youtube.com/watch?v=CDKK6FVvqvs](https://www.youtube.com/watch?v=CDKK6FVvqvs)

 - Speaker: Joe Weems, focusing on Angular Enterprise environment
- Topics:
  - Static and Dynamic Federation in Micro Frontends
    - Module Federation concept
    - Sharing library data between applications
    - Combining different Frameworks and framework versions
  - Overcoming challenges in Micro Frontends
    - Managing different application themes
    - Decision order and technology stack
    - Scaling the development team and process
- Useful tools:
  - Webpack
  - Angular CLI
  - NPM
  - Iframes
- Real-world examples: Shell and Micro Front End applications
- Importance of metadata in micro frontends
- Opt-in sharing feature for better control
- Demonstration of a shared authentication library between multiple micro frontends
- Frankenstein's monster metaphor for combining different parts of an application
- Wrapper components to abstract differences between frameworks
- Example of loading and integrating React and different versions of Angular applications within the same shell


## Form Validation Done Right | Ward Bell | ng-cof 2022

URL: [https://www.youtube.com/watch?v=EMUAtQlh9Ko](https://www.youtube.com/watch?v=EMUAtQlh9Ko)

 - NG Conf 2023 will take place in Salt Lake City, Utah on June 14-15.
- Joe Weems' talk focuses on "Form Validation Done Right".
- He emphasizes the importance of type safety and discusses a validation theme throughout his talk.
- The need for clear and concise code is highlighted for form validation, avoiding unnecessary complexity.
- Writing complex validations and ensuring correct form validation are discussed as challenges.
- Validating models at different levels (field, form, domain) is important, with effective exposure of these validations.
- A "Model Validation" approach involves creating a validation engine and reusable validation rules.
- Unit tests for validation rules should be written and integrated into an application.
- The difference between client-side and server-side validations is emphasized, with the need for a unified approach.
- A "Validation Suite" can handle both client-side and server-side validations.
- Challenges of integrating validation rules into an application using Angular's FormControl and NGModel directives are discussed.
- Writing a "Validation Scope Directive" simplifies the process of connecting form controls with validation rules.
- Reusable components and avoiding boilerplate code when building complex forms is important.
- A "Widget Component" can be used to simplify the process of writing complex forms.


## Safer Forms with Strict Types | Dylan Hunn | ng-conf 2022

URL: [https://www.youtube.com/watch?v=Z-vwuG_szVk](https://www.youtube.com/watch?v=Z-vwuG_szVk)

 - Introduction to Angular 14's typed form
    * Key benefits of using a typed form: explicit State Management, compile time error catching, improved autocomplete and code completion
- Differences between value type and control type in forms
- New features and improvements in Angular 14 for typed forms: nonnullable field, optional keys, record and array types, and the FormBuilder API
    * Nonnullable field: ensures that a form field cannot be empty or null
    * Optional keys: allows for optional properties in form groups and controls
    * Record and array types: supports more complex data structures in forms
    * FormBuilder API: provides a more intuitive way to create and manage form controls and groups
- Future plans for improving typed forms in Angular


## RxJS Best Practices Aren't Always Black and White | Deborah Kurata | ng-conf 2022

URL: [https://www.youtube.com/watch?v=rQTSMbeqv7I](https://www.youtube.com/watch?v=rQTSMbeqv7I)

 - Use declarative approach with RxJS for easy composition and communication between components.
- Divide an application into action streams, emit notifications when actions occur, and react to these notifications.
- Best Practices:
  - Always use switchMap for mapping observables.
  - Use mergeMap when the order of emissions doesn't matter.
  - Use forkJoin when you want to combine multiple async operations and wait for all of them to complete before emitting the final array.
- Error Handling: Don't forget to handle errors by catching and handling them using catchError or handleError operators.
- Avoid Nested Subscriptions: Instead of nesting subscriptions, use higher-order mapping operators inside your HTTP requests to automatically manage inner observables' subscriptions and unsubscriptions.
- Use Async Pipe: Use the async pipe to automatically subscribe and unsubscribe to observables in templates, ensuring that you don't create memory leaks by forgetting to unsubscribe.


## Angular TDD Like You Never Seen Before | Shai Reznik | ng- conf 2022

URL: [https://www.youtube.com/watch?v=KHaeVaSkhIE](https://www.youtube.com/watch?v=KHaeVaSkhIE)

 - NG Conf 2023 in Salt Lake City, Utah
- Joe Weems presents on effective Angular testing and TDD (Test Driven Development)
    * Focuses on the balance of confidence and efficiency in testing
    * Introduces Jasmine Singer Single (JSS) for single action tests
        + Demonstrates writing tests using TDD and JSS
- Highlights active retrieval to retain knowledge
- Encourages collaboration, practice, and iteration in testing
- Shares tips on refactoring code while maintaining test coverage
    * Emphasizes the value of humor and memorable experiences in learning


## B.L.A.Z.I.N.G. - 7 core principles of fast Angular application | Ady Ngom | ng-conf 2022

URL: [https://www.youtube.com/watch?v=Q865k5L5wMk](https://www.youtube.com/watch?v=Q865k5L5wMk)

 - NGConf 2023 in Salt Lake City, Utah on June 14-15
- Talk about ancient Egyptian nilometer and its relevance to modern engineering
- Discussion of web performance, budgets, and tooling
    * Presentation of a performance budget template
    * Emphasis on lazy loading for efficient resource management
    * Importance of using source of truth across departments when implementing performance budgets
- Mention of the LCP (Largest Contentful Paint) metric as part of Core Web Vitals
- Brief overview of Angular's performance checklist and its importance in optimizing web applications
- Discussion of the Zone concept in Angular, including its role in change detection
    * Demonstration of nonblocking techniques for improving web performance
- Explanation of preconnect, prefetch, and preload strategies for resource optimization
- Live demo showcasing the impact of performance optimizations on application load times


## What and Why nx  20 reasons in 20 minutes | Erick Slack & Michael Madsen | ng-conf 2022

URL: [https://www.youtube.com/watch?v=aWCdXRrZN_M](https://www.youtube.com/watch?v=aWCdXRrZN_M)

 - NG Conf 2023 featured a discussion on NX, a Next Generation build system
- Michael Madsen and Eric Slack presented the benefits of using monorepos with NX, including efficiency, scalability, and standardization
- Granular library concept helps maintain focused, single-purpose libraries within a monorepo
- One repo rule ensures easy tracking and management of dependencies across applications and libraries
- Package lock files in monorepos help maintain consistent versions across applications and libraries
- NX supports multiple frameworks and languages, making it versatile for large organizations
- Discoverability feature allows developers to easily search and navigate through codebases
- Intelligent build system with distributed caching optimizes build processes and saves time
- Affected command feature helps identify which parts of the codebase are impacted by changes
- NX's modern tooling, including schematics for code generation and custom lint rules, streamlines development processes
- Standardization across repositories ensures consistency and ease of collaboration
- NX console extension offers a GUI alternative to command line interfaces
- Federation-friendly deployment allows modules to be deployed independently while still maintaining connections within the monorepo structure
- NX's vibrant community, extensive documentation, and open-source projects make it an attractive choice for developers.


## Become a Content Projection Artist | Alain Chautard | ng-conf 2022

URL: [https://www.youtube.com/watch?v=-XyMpynvHC8](https://www.youtube.com/watch?v=-XyMpynvHC8)

 - Introduced himself and explained his experience with Angular.
- Discussed the concept of content projection in Angular.
- Explained how to create a reusable component using Angular's Content Projection feature.
- Showcased different examples of content projection, including single and multiple NG content directives, and dynamic content projection with NG template and NG container.
- Demonstrated how to use the multi-slot content projection technique for even more reusability.
- Explained how to create a tab component using Angular's Content Child decorator and passed template references as parameters.
- Showcased the final exercise, where he created a custom directive to select a specific tab based on its name attribute.
- Discussed the concept of accessing context (host component) from within a child component.
- Concluded by emphasizing the importance of toolkits and content production in building reusable components with Angular.


## Standalone Components  The Motivation | Pawel Kozlowski | ng-conf 2022

URL: [https://www.youtube.com/watch?v=JQ6at3-Dh4k](https://www.youtube.com/watch?v=JQ6at3-Dh4k)

 - NG Conf 2023 will take place in Salt Lake City, Utah from June 14th to 15th.
- The conference will feature speakers and talks related to Angular development.
- In 2022, the team published a design proposal for making antibody receptional like a great detailed discussion based on initial feedback. (no context)
- The implementation of angular 14 introduced set Standalone apis, changing the way developers write component structure in an application.
- Pavel from the Angular team discussed the motivation behind the project and provided code examples to illustrate progress.
- The goal is to make the NG model optional, answering questions about roles and consequences of using it.
- Standalone projects are being developed to address confusing bits without sacrificing good parts of Angular.
- The team is working on making the CLI more ergonomic, focusing on the default experience for new application engineers.
- The project aims to simplify the API surface and improve productivity by managing dependencies explicitly.
- The plan is to review the entire API surface in version 15 and make it stable.
- The team is considering using a working language service to help with importing Standalone components, making the Imports array more manageable.
- There's a possibility of introducing a new syntax for Angular templates to better handle control flow directives.
- The goal is to create a joyful touring experience and improve the overall developer experience in Angular applications.


## Accessibility! is! important! | Zach Arend & Emma Twersky | ng-conf 2022

URL: [https://www.youtube.com/watch?v=t1r7-QbkfZM](https://www.youtube.com/watch?v=t1r7-QbkfZM)

 - Zach's passion for accessibility
- Frameworks cannot guarantee accessibility, but they can provide builtin solutions to help get there.
- Guardrails and prioritizing first party built-in accessibility:
  - Ally: an accessibility tool that helps developers improve the accessibility of their web applications.
  - NG updates: constant improvements in Angular's accessibility features.
- Building accessible applications with Angular:
  - Framework guardrails:
    - Primitives: building blocks for creating web experiences.
    - Linting and extended diagnostics: tools that help catch and fix accessibility issues early on.
  - First party localization support: high performance, native API-based solutions for localizing applications.
  - High contrast mode: a feature that allows users to switch between standard and high contrast color schemes.
    - Windows high contrast mode: a built-in Windows feature that enhances the visual appearance of user interface elements for better readability.
- Color preference accessibility:
  - Force color API: a tool that detects and applies forced color modes, such as high contrast or grayscale, to web applications.
- Components and guardrails:
  - Component vetted compatibility: ensuring components are compatible with screen readers and other assistive technologies.
    - Angular Material support: a collection of high-quality, accessible UI components for building web applications.
- Bug fixes and improvements:
  - Accessibility bug fixes: fixing issues that affect the accessibility of web applications.
  - Date picker component: a highly customizable, accessible date picker component that can be used in various applications.
- The importance of testing and continuous improvement:
  - Testing specific user flows: ensuring that all aspects of an application's functionality are accessible to users with disabilities.
  - Updating documentation: regularly updating accessibility documentation to reflect the latest improvements and features.


## Image Optimization Best Practices with Angular | Kara Erickson | ng-conf 2022

URL: [https://www.youtube.com/watch?v=zKQRG8l1OOI](https://www.youtube.com/watch?v=zKQRG8l1OOI)

 - Introduced Image Directive for Angular
- Partnership with Google's Chrome team to improve web performance, specifically focusing on Largest Contentful Paint (LCP) metric
- Demonstrated the impact of using Image Directive in a real-world scenario with Lands End as a partner
- Improvements made in the directive:
  - Preconnect hint for LCP images
  - Built-in image letter system
  - Addition of priority attribute and preconnect tag
  - Use of modern image formats (AVIF) to reduce file size
  - Responsive image sizing using raw Source set
- Acknowledged the need for further improvements, such as automating certain tasks and incorporating picture tag feature
- Requested feedback from developers and encouraged them to test the directive in their applications


## Micro frontends and the multiverse of Frameworks | Adrian Iskandar Espinosa Caballero | ng-conf 2022

URL: [https://www.youtube.com/watch?v=oX7N3Pyo-T8](https://www.youtube.com/watch?v=oX7N3Pyo-T8)

 - NG Conf 2023 introduces a new architecture for implementing micro frontend solutions
- The architecture is called "Micro Frontend Multiverse Frameworks"
- It allows dividing and conquering applications using micro apps, independent codebases, and deployment
- Encourages single responsibility teams
- Demonstrates a demo combining various frameworks (Angular, React, Vue, Stencil) into one application
- Uses web components to encapsulate custom elements and styles
- Explains how Model Federation can help break apart code for better privacy controls and granular access to user data
- Discusses the advantages of using a shared library across applications for common problems like authentication, analytics, and internationalization features
- Mentions that this architecture allows for easier hiring of developers due to smaller codebases and learning curves
- Uses NX mono repo technology to facilitate configuration and build process simplification


## Why are web applications slow, and what to do about it | Misko Hevery | ng-conf 2022

URL: [https://www.youtube.com/watch?v=ICH5EIQXZNE](https://www.youtube.com/watch?v=ICH5EIQXZNE)

 - NG Conf 2023 will take place in Salt Lake City, Utah on June 14-15.
- Mishko CTO of Builder IO discussed web application startup performance and the impact of JavaScript at the conference.
- Google Core Web Vitals are important metrics for website performance.
- Ecommerce websites often have poor performance due to slow response times, which can lead to lost sales.
- The top 50 eCommerce websites mostly have red or yellow scores on Google Page Speed Lighthouse.
- Image optimization and CSS optimization can improve website performance, but JavaScript optimization is often overlooked.
- Moving third-party code (like analytics scripts) from the main thread to a web worker can improve website performance.
- First-party code produced by different frameworks can have varying impacts on website performance.
- Big O notation helps understand how the amount of work scales with input size.
- Server-side prerendering and resumable frameworks can help improve website performance, especially for interactive applications.
- Wiz, Marco, and other upcoming frameworks are focusing on reasonability and fast startup times.


## Community Keynote | Mark Thompson & Emma Twersky | ng-conf 2022

URL: [https://www.youtube.com/watch?v=3Mnp2WYGrVA](https://www.youtube.com/watch?v=3Mnp2WYGrVA)

 - Keynote:
  - Ampleyne Seneca (Angular Developer Engineer) discussed the growth of the Angular Community, showcasing its projects and contributions.
- Mark Thompson (Senior Developer Engineer):
  - Discussed the strong partnership between Google and the Angular Community.
  - Mentioned that the Community Keynote will feature a Partner Update, which will highlight recent achievements and future updates.
- Mike Ryan (Director Devrel, Ionic Framework):
  - Talked about the growth of the Ionic Framework and its partnership with the Angular Community.
  - Introduced new features in Ionic 6, including support for Angular 14 and the Capacitor plugin.
- Mike Ryan (Director Devrel, ngrx):
  - Introduced the latest version of ngrx, focusing on simplified action creation and official ESLint rules.
  - Talked about future updates, including a standalone CLI and improved connect API.
- Anna Boca (NativeScript Developer Advocate):
  - Discussed the growth of the NativeScript Community and its partnership with the Angular Community.
  - Showcased recent projects, such as Universal Plant Services' mobile app built using Angular and NativeScript.
- Jeff Cross (Cofounder & CEO, Narwhal):
  - Talked about the history of NX and how it supports different Frameworks, including Angular.
  - Introduced NX Cloud, which provides distributed computation caching and helps reduce build times.
- Joe Eames (Principal Engineer, RxJS):
  - Discussed the latest version of RxJS and its performance improvements.
  - Talked about future updates, including support for async iterators and observables in Web Workers.


## Angular's Future w/out NgModules Architectures w/Standalone Components| Manfred Steyer| ng-conf 2022

URL: [https://www.youtube.com/watch?v=IU-mms6CMGs](https://www.youtube.com/watch?v=IU-mms6CMGs)

 - NG Conf 2023: June 14-15, Salt Lake City
- Standalone Component: No need for an `app.module.ts`; bootstrap a standalone component and provide providers directly.
- Routing & Lazy Loading: Use the new router configuration to directly point to lazy-loaded routes without needing entry modules.
- Structuring Applications: Use folder peril, where each feature has its own directory with a barrel file for public API exporting.
- NX Workspace: A way to subdivide large applications and maintain an overview while preventing coupling between features.
- Dependency Graph & Library Constraints: NX generates a dependency graph and enforces constraints on libraries, ensuring that they can only access what they're supposed to.


## Just One More Change A Developer's Story for Pushing Angular to the Cloud | John Papa | ng-conf 2022

URL: [https://www.youtube.com/watch?v=XKmOQKXPz1g](https://www.youtube.com/watch?v=XKmOQKXPz1g)

 - Demonstrates building and deploying an Angular web application using various tools and services
  - Developer uses Github Dev for live editing, VS Code Insiders for local development, Docker Containers with Azure Static Web Apps for cloud deployment
  - Pair programming with Github Copilot, creating pull requests, and using GitHub Actions for CI/CD
- Builds an application in a Code Space environment, runs it locally, and deploys it to the cloud
  - Highlights the ease of use and features provided by Azure Static Web Apps, including staging environments and free tier options

Here's a summary of the demonstration:

- The developer showcases building an Angular web application using Github Dev for live editing, VS Code Insiders for local development, Docker Containers with Azure Static Web Apps for cloud deployment. They also use pair programming with Github Copilot, create pull requests, and utilize GitHub Actions for CI/CD.
- The demonstration includes building an application in a Code Space environment, running it locally, and deploying it to the cloud. It highlights the ease of use and features provided by Azure Static Web Apps, including staging environments and free tier options.


## Deciphering the secrets of blockchain with angular | Stephen Fluin | ng- conf 2022

URL: [https://www.youtube.com/watch?v=bhdQobn1aJs](https://www.youtube.com/watch?v=bhdQobn1aJs)

 - NG Conf 2023 in Salt Lake City, Utah
- Introduced blockchain concepts and their applications in software engineering
- Discussed the need to understand developer's perspective on blockchain technology
- Explained how NFTs work using a simple GIF example
- Emphasized that blockchains are built systems where programs run across shared compute environments
- Highlighted that blockchain technology secures itself through autonomous, decentralized execution of smart contracts
- Mentioned the importance of trust in traditional software development and how it's different in blockchain
- Shared examples of security breaches and their financial impact on users
- Demonstrated building a simple smart contract web app using Angular and Remix IDE
- Explained the concept of VRF (Verifiable Random Function) to ensure fairness in decentralized applications
- Showcased a live demo of a blockchain-based raffle system, where users could enter and get picked fairly
- Encouraged the audience to explore and learn more about blockchain development tools and frameworks


## State Management at Scale w/NgRx | Brandon Roberts | ng-conf 2022

URL: [https://www.youtube.com/watch?v=o5iHh6cBPsU](https://www.youtube.com/watch?v=o5iHh6cBPsU)

 - Brandon Roberts, a Google Developer Expert and Ngrx maintainer, shares his experience working on a large-scale enterprise project.
- The project involved managing an AngularJS application spanning multiple business units and consolidating it using ngrx.
- Challenges included:
  - Managing change detection
  - Tracking data effectively
  - Maintaining good action hygiene
- Brandon emphasizes the importance of using ngrx to manage state across components, services, and stores.
- He also highlights the benefits of using circular dependencies, feature libraries, and consistent practices for testing and refactoring code.
- The project eventually fed back into the Ngrx project, with lessons learned and improvements made.
- Brandon is excited about working on a new full-stack meta framework called AnalogJS and encourages others to contribute to the project.


## Solving the Puzzle of Real-Time Collaboration using the Fluid Framework | Dan Wahlin | ng-conf 2022

URL: [https://www.youtube.com/watch?v=4UTqBqwN6Mw](https://www.youtube.com/watch?v=4UTqBqwN6Mw)

 - NG Conf 2023 will take place in Salt Lake City, Utah on June 14th and 15th.
- The speaker discusses collaboration as a buzzword and its application using the Fluid Framework.
- He presents a real-time collaborative todo list app built with Angular and how the Fluid Framework helps sync data across multiple clients.
- The concept of "shared map" is introduced, which is crucial for synchronizing data in the Fluid Framework.
- Websockets are mentioned as a tool for real-time communication between clients and servers.
- Azure Fluid Relay, a service facilitating collaboration in web apps, is discussed.
- The speaker highlights how the Fluid Framework enables developers to build collaborative applications without server code.
- He shares his experience of building a real-time collaborative todo list app using the Fluid Framework and its benefits for data synchronization.
- Autodesk's use of the Fluid Framework in their VR applications demonstrates its versatility across various scenarios.


## TSLint to ESLint in 5 minutes | James Henry | ng-conf 2022

URL: [https://www.youtube.com/watch?v=fsr6CFqqsLc](https://www.youtube.com/watch?v=fsr6CFqqsLc)

 - NG Conf 2023 talk on June 14-15 in Salt Lake City, Utah will cover TS link deprecation and migration to ESLint.
- The speaker will provide an alternative solution using Angular ESLint.
- New approach involves removing the NG Lint Builder implementation in Angular 13.
- The talk will demonstrate the migration process from TSLint to ESLint using a project example.
- The discussion will cover the structure of an Angular CLI project and a library project called Libby.
- The speaker will install the "ng add angular eslint" schematic package and run the "ng generate" command.
- They'll use the "ng run ngg" command to transform the project from TSLint to ESLint.
- The talk will discuss the recommended ESLint config for Angular projects and how it can fit into a five-minute presentation.
- The speaker will demonstrate setting up the eslintrc.json file at both the root level and the project level, as well as extending it like TS lint.
- They'll show how to change the ESLint config and run a full lint check on the project.
- Lastly, they'll demonstrate how to rapidly convert the entire project from TSLint to ESLint while removing any unnecessary dependencies.


## The Greatest Mystery is Realtime with Angular, NestJS, and websockets! | Ely Lucas | ng-conf 2022

URL: [https://www.youtube.com/watch?v=x_2loCZ2u_8](https://www.youtube.com/watch?v=x_2loCZ2u_8)

 - Use of Websockets for real-time applications
- Overview of HTTP polling, long polling, and Server Sent Events (SSE)
- Introduction to Websockets: bidirectional communication, full duplex, event-driven architecture
- Tools used: Angular, Socket.io, NestJS (Node-based web framework), TypeScript
- Use Cases for Websockets: serving web pages, replacing HTTP APIs, caching data, error handling
- Building a chat application using Websockets and NestJS
  * Client-side: Angular
  * Server-side: NestJS with Socket.io
  * Creating services (chat service) to handle state data and persistence
  * Implementing Gateway in NestJS to handle websocket connections, communication between client and server
  * Using decorators and lifecycle methods in NestJS for routing and handling socket events
  * Building chat rooms and user management features using Socket.io and NestJS


## There's Safety in Angular | Alisa Duncan | ng-conf 2022

URL: [https://www.youtube.com/watch?v=NRg-rsMEdQs](https://www.youtube.com/watch?v=NRg-rsMEdQs)

 - NG Conf 2023 in Salt Lake City, Utah on June 14th and 15th
- Topic: "Security in Angular Applications" by Melissa Duncan (Senior Developer Advocate at OCTA)
- Importance of security in web applications, especially with Open Web Application Security Project (OWASP) top 10 vulnerabilities
- Focus on two key vulnerabilities: broken access control and injection attacks (including cross-site scripting)
- Demonstration of how a simple comment feature can be exploited in an application due to poor data hygiene and lack of input validation/sanitization
- Explanation of how Angular's built-in security mechanisms help prevent these issues by automatically escaping values, incorporating them using interpolation, and providing sanitization methods
- Discussion on the importance of using Angular constructs for property binding, interpolation, and input validation to ensure safety in applications
- Brief mention of how to handle situations where you might need to bypass Angular security measures, but doing so can be risky and should only be done with a legitimate reason
- Introduction to OAuth vulnerabilities, specifically broken access control, and the importance of implementing proper authentication and authorization mechanisms in applications
- Demonstration of how Angular's HTTP Client XSRF module can help protect against CSRF attacks by automatically sending a CSRF token with API requests
- Emphasis on the need to implement robust access control measures in applications, including the use of route guards, lazy loading modules, and structural directives for permissioning schemas


## Typescript meta programming from 0 to 100 | Daniel Ostrovsky | ng-conf 2022

URL: [https://www.youtube.com/watch?v=xCsnRQOScrQ](https://www.youtube.com/watch?v=xCsnRQOScrQ)

 - Daniel Ostrovsky, a 20-year industry veteran, will speak on Meta Programming at the NG Conf 2023.
- He will discuss how to use TypeScript for advanced techniques like dependency injection and reflection.
- Dependency Injection is a design pattern that allows developers to create loosely coupled code by injecting dependencies into objects.
- Reflection is a feature in TypeScript that enables runtime type checking and metadata retrieval.
- He will provide examples of how to use these techniques to build complex applications using Angular and other frameworks.
- He will also share his personal experiences working with large-scale web applications at Goh, a company that specializes in taking care of publishers' websites.
- The talk will be based on real-life code examples and will demonstrate how to use TypeScript and Angular to build scalable and maintainable applications.

### Summary:
- Daniel Ostrovsky, an experienced industry veteran, will speak at NG Conf 2023 about Meta Programming.
- He'll discuss using TypeScript for advanced techniques like Dependency Injection and Reflection.
- Dependency Injection is a design pattern that helps create loosely coupled code by injecting dependencies into objects.
- Reflection enables runtime type checking and metadata retrieval in TypeScript.
- Ostrovsky will provide examples of using these techniques to build complex applications with Angular and other frameworks.
- He'll share his experiences working on large-scale web apps at Goh, a company specializing in publisher websites.
- The talk will be based on real-life code examples and demonstrate how to use TypeScript and Angular for scalable, maintainable applications.


## AG Grid | Niall Crosby & Stephen Cooper | ng-conf 2022

URL: [https://www.youtube.com/watch?v=4dhBnvgb5H0](https://www.youtube.com/watch?v=4dhBnvgb5H0)

 - Nile Crosby, AG Grid creator and sponsor, speaks at ngConf
- 50% of Angular developers use AG grid in their projects
- New features include:
  * Integrated charts: allows users to chart data within the grid
  * Club Rows: a new feature that allows grouping of rows for easy comparison and analysis
- AG Grid has expanded its team, including Stephen Cooper, an Angular expert
- Upcoming changes to the component will include:
  * Strict typing support
  * Full IV (Initialization Value) support
- A two-hour workshop on setting up and customizing AG grid will be held by Brian and Mike during the conference.


## Get to Know the 2022 ng-conf Speakers | Dan Wahlin | ng-conf 2022

URL: [https://www.youtube.com/watch?v=Kr_KaM19Hko](https://www.youtube.com/watch?v=Kr_KaM19Hko)

 - Background: Started with Basic in high school, transitioned to engineering and programming after being introduced to the internet.
- Known Programming Languages: Pearl, VB6, C++, Java, JavaScript, TypeScript, SQL databases.
- Favorite Tech: C#, Visual Basic 3.6, ASP Classic, React.
- Challenges in Angular: Learning terminology and concepts, especially for newer developers.
- Memorable NGConf Moment: Giving his first talk at the conference after being convinced by Aaron Frost.
- Current Role: Working on a collaboration framework called Fluid Framework, which focuses on true web-based collaboration in JavaScript apps.


## Simplifying deep angular forms with di equipped custom components | Rafael Mestre | ng- conf 2022

URL: [https://www.youtube.com/watch?v=nZI4Gra_FsM](https://www.youtube.com/watch?v=nZI4Gra_FsM)

 - Rafael Mestre, a senior software engineer from Puerto Rico, shares his journey of becoming a software engineer and how he learned to handle complex forms in Angular.
- He emphasizes the importance of using dependency injection (DI) for managing dependencies between objects in an application.
- Rafael talks about using the Entity Pattern for creating decoupled, reusable components.
- He encourages developers to use typed directives and form group names for ensuring type safety and flexibility.
- The Control Container pattern is useful for managing forms with nested fields and dynamic content.
- Rafael highlights that Angular continues to evolve and improve, with better developer experiences (DX) on the horizon.
- He recommends exploring library resources like the Angular repo, guides, and videos to improve skills in working with forms.


## Partially Zoneless   Performance tuning without big bang refactoring | Michael Hladky | ng-conf 2022

URL: [https://www.youtube.com/watch?v=or8aoOdOsHk](https://www.youtube.com/watch?v=or8aoOdOsHk)

 - NG Conf 2023 will be held in Salt Lake City, Utah from June 14th to 15th.
- The speaker discusses the importance of performance optimization and scalability in Angular applications.
- Focus on understanding runtime performance, especially long tasks, using flame charts.
- Introduce a toolset called RX Angular Open Source Repository for better developer experience.
- Discuss Angular's change detection mechanism, component tree, dirty marking, and rendering.
- Explain the concept of Zone, its purpose, and how it works with asynchronous APIs.
- Showcase a demo of a large-scale Angular application and its performance improvements.
- Present new ways to optimize change detection, local State Management, and rendering using structural directives like pushpap and rx4.
- Discuss the concept of concurrent rendering in Angular, which helps smooth interactions and prevent frame drops.
- Introduce a fully zoneless approach for better performance and scalability.


## Cypress for angular devs hands on workshop | Jordan Powell & Ely Lucas |  n-g conf 2022

URL: [https://www.youtube.com/watch?v=QYtonSoCIyc](https://www.youtube.com/watch?v=QYtonSoCIyc)

 - Introducing Cyprus: An end-to-end and component testing solution for JavaScript applications
  - Demonstration of Cyprus features:
    - Time traveling snapshots
    - Automatic waiting for element existence
    - Component test creation using Cypress schematic
    - Migrating from Protractor to Cyprus using the Cypress migrator tool
- Hands-on Workshop with Cyprus
  - Cloning the Cypress repo and running npm install
  - Three parts of the workshop:
    1. Introduction to Cyprus and its features
    2. Migrating an application using Protractor to Cyprus
    3. Demonstrating component testing with Cyprus
- Migrating from Protractor to Cyprus using the Cypress migrator tool
  - Installing the Cypress schematic and running the command to create an end-to-end test
  - Using the Cypress migrator tool to convert a Protractor test to a Cypress test
  - Running the converted Cypress test using the Cyprus CLI
  - Reviewing the documentation for the Cypress migrator tool and running the command to create a new Cypress test from a Protractor test
- Demonstrating component testing with Cyprus
  - Launching Cypress and selecting the "Component Testing" option
  - Setting up the necessary dependencies for component testing, including the Angular CLI and the @cypress/schematic package
  - Creating a new component using the Angular CLI and running npm install to install its dependencies
  - Using the Cypress CLI to start a new test file for the newly created component
  - Writing a simple test for the component, including setting up the necessary fixture and specifying the behavior of the component's properties and methods
  - Running the test using the Cypress CLI and observing the test results in the Cypress Test Runner
- Q&A session with questions from attendees


## Quick Context about Host Context | Ankita Sood | ng-conf 2022

URL: [https://www.youtube.com/watch?v=tViltuKzruM](https://www.youtube.com/watch?v=tViltuKzruM)

 - NG Conf 2023 will be held in Salt Lake City, Utah on June 14th and 15th.
- Joe Weems is the host of a late-night TV show, morning show, and Angie's List host.
- Ankita is a frontend engineer at Deloitte Secure Work based in Austin, Texas.
### Summary:
* NG Conf 2023 will take place on June 14th and 15th in Salt Lake City, Utah.
* Joe Weems hosts late-night TV shows, morning shows, and Angie's List.
* Ankita is a frontend engineer at Deloitte Secure Work in Austin, Texas.
### Key Points:
- NG Conf 2023 dates and location
- Joe Weems' hosting roles
- Ankita's professional background

---
### Detailed Summary:
* Angular component architecture allows for versatile design and encapsulation modes.
* The View Encapsulation option emulates shadow DOM behavior, which empowers targeting actual DOM elements using CSS selectors consistently across browsers.
* Host context is a pseudo-selector that enables modifying content based on the parent component's context or state.
* An example of host context usage is assigning different classes to a card component depending on its parent group value.
* Host context can also be used to modify content display based on layout (column vs row).
* A popular use case for host context is passing a CSS selector as a theme class name to an Angular component, which then applies the specified theme.
### Key Points:
- Versatile design and encapsulation modes in Angular component architecture
- View Encapsulation and shadow DOM behavior
- Host context usage examples and popular use cases


## Write once, run anywhere with an angular PWA | Michael Dowden & Maritine Dowden | ng-conf 2022

URL: [https://www.youtube.com/watch?v=hqKjYRM9pZY](https://www.youtube.com/watch?v=hqKjYRM9pZY)

 - PWAs (Progressive Web Apps) are web applications built using modern web capabilities, including the ability to work offline or on low-quality internet connections.
- They can be installed on a user's device and run like an app from the home screen.
- To create a PWA, you need a service worker, which is a script that runs in the background of your web application, even when it's not open. The service worker helps to cache web content and serve it faster, especially on low-quality internet connections.
- Another important part of creating a PWA is adding a manifest file, which contains information about your app, such as its name, icon, and the type of screen it should run on (e.g., mobile or desktop).
- To test your PWA, you can use Chrome DevTools or Firefox DevTools, which allow you to simulate different types of devices and internet connections.
- One common issue with PWAs is dealing with icons for different devices and screen sizes. There are tools available that can help you create icons in the correct format and size for each device.
- To make your PWA work on iOS devices, you need to add specific icons and configuration files that are required by Apple's App Store guidelines.
- Adding an Angular Firebase service is important for handling authentication, data storage, and real-time updates in a PWA.


## State Management Techniques and Family Therapy | Kate Sky | ng-conf 2022

URL: [https://www.youtube.com/watch?v=bSJtYNhAqwY](https://www.youtube.com/watch?v=bSJtYNhAqwY)

Error


## I Let Strangers Design My Slides using NgRx Component Store | Mike Ryan | ng-conf 2022

URL: [https://www.youtube.com/watch?v=OCuz2aAtBBE](https://www.youtube.com/watch?v=OCuz2aAtBBE)

Error


## EndBridge: Migrate from Protractor to Cypress in Less Than a Day! | Joe Eames | ng-conf 2022

URL: [https://www.youtube.com/watch?v=s67mDePPifQ](https://www.youtube.com/watch?v=s67mDePPifQ)

Error


## Future Proof your company by effectively scaling engineering | Jennifer Wadella | ng-conf 2022

URL: [https://www.youtube.com/watch?v=XFYMs78wTkA](https://www.youtube.com/watch?v=XFYMs78wTkA)

Error


## OAyDaBy AAm=/y SAinRe9L TArT, wait what? | Jessica Janiuk & Joey Perrott | ng-conf 2022

URL: [https://www.youtube.com/watch?v=9UtwYGYkznc](https://www.youtube.com/watch?v=9UtwYGYkznc)

Error


## RxWut | Kim Maida & Sam Julien | ng-conf 2022

URL: [https://www.youtube.com/watch?v=tH2tmwF9RdE](https://www.youtube.com/watch?v=tH2tmwF9RdE)

Error


## Testable Angular Forms | Martine Dowden | ng-conf 2022

URL: [https://www.youtube.com/watch?v=rWXWXWMy2lE](https://www.youtube.com/watch?v=rWXWXWMy2lE)

Error


## Get to Know the 2022 ng-conf Speakers | Kate Sky | ng-conf 2022

URL: [https://www.youtube.com/watch?v=L6dgOQUeiW0](https://www.youtube.com/watch?v=L6dgOQUeiW0)

Error


## Shit, our Site is Down! Let's build a culture of reliability | Brian Love | ng-conf 2022

URL: [https://www.youtube.com/watch?v=_MgNvmxAJrk](https://www.youtube.com/watch?v=_MgNvmxAJrk)

Error


## NgRx Feature Creator | Marko Stanimirovic | ng- conf 2022

URL: [https://www.youtube.com/watch?v=t69Hj1V9DuE](https://www.youtube.com/watch?v=t69Hj1V9DuE)

Error


## The Tale Tell Code | Lara Newsom | ng-conf 2022

URL: [https://www.youtube.com/watch?v=PE1rUoQVnWk](https://www.youtube.com/watch?v=PE1rUoQVnWk)

Error


## Run Code When Leaving Your Angular Application | Preston Lamb | Ng-conf 2022

URL: [https://www.youtube.com/watch?v=17XyV8iWThA](https://www.youtube.com/watch?v=17XyV8iWThA)

Error


## Get to Know the Angular Team | Sarah Drasner | ng-conf 2022

URL: [https://www.youtube.com/watch?v=26hLCSw7STw](https://www.youtube.com/watch?v=26hLCSw7STw)

Error


## Get to Know the 2022 ng-conf Speakers | John Papa | ng-conf 2022

URL: [https://www.youtube.com/watch?v=3KZ7ZJ2xyaE](https://www.youtube.com/watch?v=3KZ7ZJ2xyaE)

Error


## Get to Know the Angular Team | Emma Twersky  | ng-conf 2022

URL: [https://www.youtube.com/watch?v=WmKi84JTQLY](https://www.youtube.com/watch?v=WmKi84JTQLY)

Error


## Get to Know the 2022 ng-conf Speakers | Alain Chautard  | ng-conf 2022

URL: [https://www.youtube.com/watch?v=aAf7W1nuWCA](https://www.youtube.com/watch?v=aAf7W1nuWCA)

Error


## LeTS play a game | Craig Spence | ng-conf-2022

URL: [https://www.youtube.com/watch?v=Mge_8f94Jd8](https://www.youtube.com/watch?v=Mge_8f94Jd8)

Error


## Migrating from Protractor to Cypress E2E in Under 5 Minutes | Jordan Powell  | n-g conf 2022

URL: [https://www.youtube.com/watch?v=cpd8TUvNEYU](https://www.youtube.com/watch?v=cpd8TUvNEYU)

Error


## Get to Know the Angular Team | Minko Gechev | ng-conf 2022

URL: [https://www.youtube.com/watch?v=LmBYqQmFtJY](https://www.youtube.com/watch?v=LmBYqQmFtJY)

Error


## Slow Down to Get Ahead | Michael Callaghan | ng-conf- 2022

URL: [https://www.youtube.com/watch?v=UMcdrWi_vlk](https://www.youtube.com/watch?v=UMcdrWi_vlk)

Error


## Get to Know the 2022 ng-conf Speakers | Ankita Sood | ng-conf 2022

URL: [https://www.youtube.com/watch?v=plAMq9lr2RY](https://www.youtube.com/watch?v=plAMq9lr2RY)

Error


## Get to Know the Angular Team | Jeremy Elbourn| ng-conf 2022

URL: [https://www.youtube.com/watch?v=NA1psZUQ1H4](https://www.youtube.com/watch?v=NA1psZUQ1H4)

Error


## Get to Know the Angular Team | Wagner Maciel | ng-conf 2022

URL: [https://www.youtube.com/watch?v=y5XKR_bFFr8](https://www.youtube.com/watch?v=y5XKR_bFFr8)

Error


## Get to Know the 2022 ng-conf Speakers | Alfredo Perez  | ng-conf 2022

URL: [https://www.youtube.com/watch?v=NKS4_Y5z0Bs](https://www.youtube.com/watch?v=NKS4_Y5z0Bs)

Error


## Get to Know the Angular Team | Pawel Kozlowski | ng-conf 2022

URL: [https://www.youtube.com/watch?v=fI_cof26TN0](https://www.youtube.com/watch?v=fI_cof26TN0)

Error


## Get to Know the 2022 ng-conf Speakers | Brian Love | ng-conf 2022

URL: [https://www.youtube.com/watch?v=KS6GDgBxnyY](https://www.youtube.com/watch?v=KS6GDgBxnyY)

Error


## Get to Know the Angular Team | Kristiyan Kostadinov | ng-conf 2022

URL: [https://www.youtube.com/watch?v=hCVLV60tadQ](https://www.youtube.com/watch?v=hCVLV60tadQ)

Error


## Get to Know the Angular Team | Mark Thompson | ng-conf 2022

URL: [https://www.youtube.com/watch?v=yNrfwnXtEKU](https://www.youtube.com/watch?v=yNrfwnXtEKU)

Error


## Get to Know the 2022 ng-conf Speakers | Daniel Ostrovsky | ng-conf 2022

URL: [https://www.youtube.com/watch?v=JJOipy9O8Yw](https://www.youtube.com/watch?v=JJOipy9O8Yw)

Error


## Get to Know the 2022 ng-conf Speakers | Jennifer Wadella | ng-conf 2022

URL: [https://www.youtube.com/watch?v=4_yKlcspGkI](https://www.youtube.com/watch?v=4_yKlcspGkI)

Error


## Get to Know the Angular Team | Andrew Scott | ng-conf 2022

URL: [https://www.youtube.com/watch?v=x8OxLm_cgKU](https://www.youtube.com/watch?v=x8OxLm_cgKU)

Error


## Get to Know the 2022 ng-conf Speakers | Lara Newsome | ng-conf 2022

URL: [https://www.youtube.com/watch?v=wYoIi81llqw](https://www.youtube.com/watch?v=wYoIi81llqw)

Error


## Get to Know the Angular Team | Doug Parker | ng-conf 2022

URL: [https://www.youtube.com/watch?v=uv3MZVH6d4k](https://www.youtube.com/watch?v=uv3MZVH6d4k)

Error


## Get to Know the 2022 ng-conf Speakers | Ady Ngom | ng-conf 2022 |

URL: [https://www.youtube.com/watch?v=5nUT2q8TLZQ](https://www.youtube.com/watch?v=5nUT2q8TLZQ)

Error


## Get to Know the 2022 ng-conf Speakers | Jordan Powell | ng-conf 2022

URL: [https://www.youtube.com/watch?v=pVUvRN1rykg](https://www.youtube.com/watch?v=pVUvRN1rykg)

Error


## Get to Know the Angular Team | Madleina Scheidegger | ng-conf 2022

URL: [https://www.youtube.com/watch?v=IKPC6TokM4U](https://www.youtube.com/watch?v=IKPC6TokM4U)

Error


## Get to Know the 2022 ng-conf Speakers | Christina Brink | ng-conf 2022

URL: [https://www.youtube.com/watch?v=uTiBVpRrr2U](https://www.youtube.com/watch?v=uTiBVpRrr2U)

Error


## Get to Know the Angular Team | Miles Malerba | ng-conf 2022

URL: [https://www.youtube.com/watch?v=r-MlQQFRonc](https://www.youtube.com/watch?v=r-MlQQFRonc)

Error


## Get to Know the 2022 ng-conf Speakers | James Henry | ng-conf 2022

URL: [https://www.youtube.com/watch?v=QBifvYONyvk](https://www.youtube.com/watch?v=QBifvYONyvk)

Error


## Get to Know the 2022 ng-conf Speakers | Alisa Duncan | ng-conf 2022

URL: [https://www.youtube.com/watch?v=r3R7nHx-NUI](https://www.youtube.com/watch?v=r3R7nHx-NUI)

Error


## Get to Know the 2022 ng-conf Speakers | Michael Dowden | ng-conf 2022

URL: [https://www.youtube.com/watch?v=VYprehMnPo8](https://www.youtube.com/watch?v=VYprehMnPo8)

Error


## Get to Know the 2022 ng-conf Speakers | Michael Callaghan | ng-conf 2022

URL: [https://www.youtube.com/watch?v=Y0wbheNUpTg](https://www.youtube.com/watch?v=Y0wbheNUpTg)

Error



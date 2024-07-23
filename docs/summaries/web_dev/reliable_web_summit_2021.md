## Clean code is no longer a myth | Karan Balkar | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=wf8zQriwF1g](https://www.youtube.com/watch?v=wf8zQriwF1g)

 - Karan, an Android developer, discussed clean code and its importance in a software development life cycle.
- He emphasized the separation of concerns principle to divide programs into distinct sections handling separate concerns.
- Writing clean code is about continuously refactoring code and modifying logic for better efficiency.
- Four-stage habit building process: Cue, Craving, Response, Reward.
- Husky Git Hooks can automate formatting code and applying custom rules during the precommit phase.
- ESLint, a popular open-source JavaScript linter, helps enforce coding standards and style guidelines.
- Commit Link is a tool that improves commit messages by adding a meaningful link to each commit.
- Node Version Manager (NVM) assists in managing different versions of Node.js and their dependencies.


## Maintainable JavaScript with Functional Patterns | Luis Fernando Alvarez | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=96x2KQExrSM](https://www.youtube.com/watch?v=96x2KQExrSM)

 - Functional programming principles in Javascript
  - Purity: functions don't depend on or affect external state
  - Immutability: everything is constant, no mutation
- Functional programming concepts used in Javascript
  - Map: transforms one list to another
  - Filter: filters elements of an array based on a condition
  - Reduce: combines all elements of an array into a single value
- Higher order functions in Javascript
  - Functions that receive other functions as arguments or return them as values
  - Examples include map, filter, and reduce
- Currying and partial application in Javascript
  - Breaking down multi-argument functions into smaller ones with fewer arguments
  - Useful for composing functions and reusing code
- Composition of functions in Javascript
  - Combining multiple functions to create a new one
  - Example: greeting map
- Libraries for functional programming in Javascript
  - Ramda: provides utility functions for working with data structures like arrays, objects, and strings
  - FP-TS: adds functional programming concepts to TypeScript


## Dear non-performant app, | Nishu Goel | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=C9bJCP0X5N8](https://www.youtube.com/watch?v=C9bJCP0X5N8)

 - Optimizing Application Performance
- Importance of Core Web Vitals: LCP (Largest Contentful Paint), FID (First Input Delay), CLS (Cumulative Layout Shift)
  - Loading: Reduce time to first load and render content
  - Interactivity: Improve user interaction response time
  - Visual Stability: Ensure page layout remains stable during loading
- LCP Optimization Techniques
  - Critical CSS: Load essential styles early, defer non-critical styles
  - Inline Fonts: Avoid external font requests for faster rendering
  - Image Optimization: Use efficient file formats and reduce image sizes
  - CDN: Utilize Content Delivery Networks to serve resources efficiently
  - Preload Important Resources: Prioritize downloading critical assets before rendering
- FID Improvement Strategies
  - Defer Unused JavaScript: Avoid loading unnecessary scripts that slow down page load time
  - Code Splitting: Break up large bundles into smaller, more manageable chunks for faster loading times
  - Minimize Polyfills: Only include necessary polyfills to reduce download size and improve performance
- CLS Optimization Tips
  - Dynamic Content Loading: Ensure content loads predictably without unexpected shifts in layout
  - Responsive Images: Use image tags or iframes to conditionally load images based on screen size
  - Adaptive Serving: Serve resources according to user connection speed for optimal performance
- Finalizers and Weak Refs: Understand how weak references and finalizers work in JavaScript to manage memory usage effectively.


## Keep Running at Runtime | Christoph Guttandin | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=1G2cIXHd120](https://www.youtube.com/watch?v=1G2cIXHd120)

 - Tracking runtime performance in web apps is important, especially for long-running applications.
- Error tracking and handling are crucial to avoid unexpected crashes or user experience issues.
- Use a framework or library that provides built-in error handling mechanisms.
- Implement unhandled rejection tracking to catch errors thrown by promises.
- Track performance metrics like memory usage, CPU usage, and frame rate for better optimization.
- Browsers may throttle certain events or resources based on page visibility or device capabilities.
- Use web workers or audio contexts to avoid main thread blocking.
- Modern browsers offer APIs to control screen locking or resource scheduling.
- Monitoring runtime performance can help identify potential issues and optimize the app's behavior.


## Betterer: Incremental Improvement | Craig Spence | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=y5Q4eXCpn20](https://www.youtube.com/watch?v=y5Q4eXCpn20)

 - Presentation by Craig Shu Mai
- Worked in various environments, emphasized incremental change and working software
- Discusses the importance of understanding the impact of product changes based on user feedback
- Describes a system that evolved over time and became difficult to change without causing issues
- Talks about the dangers of revolutionary change and the importance of communication when making changes
- Introduces the concept of "branch life" and the challenges it presents in managing codebases
- Explains the idea of a genetic algorithm, which can be used to explore potential solutions to complex problems
- Discusses the use of tools like TypeScript, ESLint, and Jest for improving code quality and maintainability
- Talks about the concept of "microservices" as an alternative to monolithic applications
- Explains how breaking down a large codebase into smaller components can make it easier to manage and change over time
- Introduces the idea of using quantifiable metrics to track progress in improving a codebase
- Talks about the importance of comparing the state of a codebase at different points in time, as well as the challenges that come with it
- Discusses the use of test-driven development and how it can help improve the quality of a codebase
- Introduces the concept of "better" tools, which are designed to make incremental improvements to a codebase easier
- Talks about the importance of clear communication when making changes to a codebase
- Discusses the use of file tests and how they can help identify specific issues in a codebase
- Introduces the concept of "issue files" and how they can be used to track and resolve problems in a codebase
- Talks about the importance of using version control tools like Git to manage changes to a codebase
- Discusses the use of continuous integration (CI) and continuous deployment (CD) pipelines to automate the process of building, testing, and deploying software
- Introduces the concept of "deadlines" for migration projects and how they can help ensure that progress is made in a timely manner
- Talks about the importance of regularly monitoring and reporting on the status of a codebase
- Discusses the use of various tools and techniques to improve the quality, maintainability, and security of a codebase
- Emphasizes the importance of working together with others when making changes to a codebase
- Introduces the concept of "branching" as a way to manage changes to a codebase
- Talks about the importance of having a clear plan for managing changes to a codebase and how it can help ensure that progress is made in a timely manner


## Architecting for Accessibility | Martine Dowden | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=z8r_K9BG0d4](https://www.youtube.com/watch?v=z8r_K9BG0d4)

 - Introduction to Accessibility in Web Development
    + Accessibility started with Berners-Lee's vision in 1945
    + First commercial reading machine created in 1975 by Ray Kurzweil
    + W3C launched the Web Accessibility Initiative (WAI) in 1997
+ The Importance of Accessibility
    + Over 1 billion people have disabilities worldwide
    + Accessibility is essential for everyone, regardless of individual capability or disability
+ Challenges in Making Applications Accessible
    + Auditory: Hearing loss affects 15% of the world's population
    + Visual: Vision impairments affect over 13 billion people worldwide
    + Physical: Physical disabilities can limit movement and keyboard/mouse use
    + Cognitive & Neurological: Conditions such as dementia, epilepsy, or brain injuries can impact cognitive abilities and access to information
+ The Role of Legal Compliance in Accessibility
    + Many countries have laws that require digital accessibility
    + Some companies may lose contracts if they don't comply with these standards
+ How to Get Started with Making Your Application Accessible
    + Understand the standard testing and follow legal best practices
    + Test across different devices, browsers, and assistive technologies
    + Make sure your application is usable by people with disabilities, regardless of their ability to perceive information or discern content presented
+ The Importance of Training & Teamwork in Accessibility
    + A diverse team can help ensure that accessibility needs are considered throughout the development process
    + Training and education can help everyone understand the importance of accessibility and how to implement it effectively
+ The Role of Automated Testing in Ensuring Accessibility
    + Automated testing can help catch common errors and make sure your application is compliant with accessibility standards
    + However, automated testing should be supplemented by manual testing and user feedback
+ The Importance of User Feedback in Accessibility
    + User feedback can provide valuable insights into how people with disabilities interact with your application
    + Regularly monitoring user feedback can help you identify areas where your application may need improvement
+ The Role of Documentation & Scaling in Accessibility
    + Good documentation can help new team members understand the importance of accessibility and how to implement it effectively
    + As your application grows, it's important to continue scaling your efforts to ensure that all new features are accessible


## Climbing to the top of the Lighthouse with Scully | Robert Willemelis | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=dD74bhKnlkE](https://www.youtube.com/watch?v=dD74bhKnlkE)

 - Talk by Robert, Berlin-based frontend developer
- Journey to top Lighthouse score with Scully
- Scully: static side generator for Jamstack applications
- Prerender Angular application based on route
- Store additional data in markdown files
- Use Scully to analyze routes and generate static HTML
- Test website performance using Google Lighthouse
- Focus on 5 categories: Performance, Best Practice, Accessibility, Progressive Web Apps, SEO
- Continuously improve Lighthouse score through optimization
- Optimize DevTools PageSpeed Insights for different platforms
- Compare hosting providers to find the best result
- Test multiple times and take average results
- Follow Lighthouse recommendations and approve low-hanging fruit
- Optimize images using WebP format and caching techniques
- Use service workers to cache assets and improve performance
- Focus on largest contentful paint (LCP) optimization
- Optimize server response time for better Lighthouse score
- Use inline SVGs and reduce unnecessary CSS code
- Implement lazy loading for non-critical images
- Utilize Scully's caching capabilities to optimize static HTML files
- Create a reusable component for responsive layouts
- Define breakpoints using magic angular pipe
- Optimize Lighthouse score by improving accessibility and SEO
- Use WebP format for images to reduce file size
- Utilize CNDs like Cloudflare to improve website performance
- Implement service workers with Workbox to cache assets and improve performance
- Set different caching strategies based on asset type and priority
- Optimize render-blocking JavaScript by splitting and concatenating files
- Use class-based file splitting for better code organization
- Analyze unused dependencies and optimize bundle size
- Refactor duplicated code to reduce bundle size
- Leverage Lighthouse reports, Webpack Bundle Analyzer, and other tools for optimization


## The Immutable Web | Stephen Fluin | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=AsibupnDJic](https://www.youtube.com/watch?v=AsibupnDJic)

 - Intro: Excited to discuss the "Immutable Web" at the Web Summit
- Background: Stephen Fluin, Head Developer Relations at Chainlink Labs, previously worked at Google and has experience building web applications
- Key Concepts:
  - Blockchain: A decentralized network that securely stores data and records transactions in a transparent manner. It is an alternative to traditional centralized servers.
  - Bitcoin & Ethereum: Two popular blockchains, with Bitcoin being more focused on digital currency and Ethereum providing a platform for developers to build applications using smart contracts.
- Immutable Web:
  - Concept: A web application that directly interacts with decentralized networks (blockchain) instead of traditional APIs.
  - Benefits: Greater trust, transparency, and permanence of data stored on the blockchain.
- Smart Contracts & Dapps (Decentralized Applications):
  - Ethereum provides a platform for developers to create smart contracts and decentralized applications using its programming language, Solidity.
  - Example: A simple todo list application that stores data on the Ethereum blockchain.
- Interacting with Blockchains:
  - Providers like Alchemy and Infura allow web developers to interact with blockchain networks through JSON APIs.
- Payment & Gas:
  - Transactions on a blockchain require payment in the form of cryptocurrency, which is used to compensate network participants for processing transactions and computing power.
- Scalability Challenges:
  - Blockchains can have slow transaction times due to their decentralized nature and the need to verify each transaction across multiple nodes.
- Future Opportunities & Growth:
  - The blockchain ecosystem is growing rapidly, with new applications and services being developed every year.


## Testable Architecture in Angular | Rainer Hahnekamp | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=pAmdyvJ5VNY](https://www.youtube.com/watch?v=pAmdyvJ5VNY)

 - Introduced the speaker, Reina Hanekamp
- Discussed the concept of architecture and how it relates to testing
- Presented a brief overview of Angular and its role in the workshop
- Explained the differences between unit and integration tests, highlighting their strengths and weaknesses
- Showcased an example application for demonstration purposes
- Demonstrated various testing strategies using tools like Jest, Testbed, and Cypress
- Introduced the concept of Nx and how it can be used to promote better architecture and testing practices in Angular applications
- Explained the importance of domain-driven design (DDD) and its role in creating maintainable and scalable applications
- Discussed the use of storybook for visual regression testing
- Highlighted the importance of refactoring and how it can improve testability and code quality
- Encouraged attendees to experiment with different testing strategies and tools
- Provided a schedule for a public testing workshop related to Angular

The speaker provided an overview of various testing strategies, tools, and techniques used in Angular development. They discussed the differences between unit and integration tests, as well as how they can be combined effectively. The speaker also introduced the concept of Nx and its role in promoting better architecture and testing practices in Angular applications. Additionally, they explained the importance of domain-driven design (DDD) and demonstrated how it can be used to create maintainable and scalable applications. The speaker encouraged attendees to experiment with different testing strategies and tools and provided a schedule for a public testing workshop related to Angular.


## Testing with Component Harnesses for the Win | Alain Chautard | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=JJedYMmhe-A](https://www.youtube.com/watch?v=JJedYMmhe-A)

 - Introduction to Component Harness
  - Big Picture of Testing in Web Development
    - Unit Testing: Validate single piece of code
    - Integration Testing: Validate multiple pieces of code working together
    - End-to-End Testing: Simulate user interaction and validate application behavior
    - Performance Testing: Measure speed and responsiveness of an application
  - Component Harness: Applying Object Model Pattern at Component Level
    - Clear, well-defined API for component interactions
    - Reduces complexity and increases maintainability
    - Can be used across different testing frameworks and technologies
    - Provides a consistent way to interact with components regardless of context (e.g., unit test or end-to-end test)
  - Harness Libraries Available
    - Angular Material CDK Component Development Kit (CDK) provides a component harness API
    - Cypress, Jasmine, and other testing libraries support the use of component harnesses
  - How to Implement a Component Harness
    1. Target implementation: Choose which testing library or environment you want to use (e.g., Cypress, Jest, Angular Testbed)
    2. Select a component: Identify the specific component you want to test
    3. Interact with the component using its API: Use the harness API to perform actions on the component and retrieve information from it
  - Benefits of Using Component Harnesses
    - Increases productivity when writing unit tests
    - Reduces code duplication by reusing APIs across different test scenarios
    - Simplifies testing complex components like dropdowns or tabs


## The New Web | Stephen Fluin | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=ctEjPTlXaYI](https://www.youtube.com/watch?v=ctEjPTlXaYI)

 - New web development concepts
- Importance of modern tooling and process
- Success in the new web: fast, engaging, and delightful user experiences
- Static vs dynamic websites and web applications
- Typescript as a game changer for building applications
- Evolving browser technology and ECMAScript standards (ES2021)
- The rise of static site generators like 11ty and Gatsby
- Micro frontends: a solution to scaling web apps?
- Webpack as an essential tool in the modern web ecosystem
- Blockchain's impact on the future of the web: immutable web, decentralized identity, and cryptography-based authentication
- Rapid evolution of web development platforms, frameworks, and libraries
- The importance of staying up to date with industry trends and technologies
- Using conferences like Reliable Web Summit and Amazing Web as resources for learning and networking


## 3L-C's- Three Level Components Technique | Aziz Yazit | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=b15jOzJFKcI](https://www.youtube.com/watch?v=b15jOzJFKcI)

 - Introduced as a Stanford conference delegate and software architect from Malaysia
- Discussed competent pattern techniques in design systems
- Mentioned the importance of confidence levels (LC3) to understand component organization
- Talked about modern combination design system topologies
- Explained the concept of component-based architecture and its benefits
- Provided examples of popular frameworks such as AngularJS, React, and Vue.js
- Discussed the role of web components in modern UI development
- Showcased Google's Material Design System and how it influences product design
- Demonstrated Firebase's component library and its applications in various products
- Introduced the concept of "level confidence" to understand better the organization and structure of a design system
- Explained that the level of confidence does not necessarily mean superiority but rather complementarity
- Talked about the importance of context in designing components for different product types
- Discussed the concept of "le level attraction" and how it affects component extraction
- Provided examples of multi-app and multi-site designs within a workspace
- Explained that the le level attraction principle helps in better understanding the organization's needs and preferences
- Introduced the concept of "level confidence complement" as an alternative to the traditional three-level confidence approach
- Talked about the challenges faced when designing components for different teams and product types
- Discussed the importance of a design system library and how it helps in reusing application code
- Explained that the component library should be flexible enough to cater to various product requirements
- Provided an example of a micro frontend architecture, where each microservice has its own UI components
- Talked about the concept of "level extraction" and how it affects the overall design system structure
- Introduced the concept of "le level component" as a way to understand better the organization's needs and preferences
- Explained that the le level complement does not necessarily mean superiority but rather complementarity
- Talked about the challenges faced when designing components for different teams and product types
- Provided examples of how different design systems can be used together within an organization
- Discussed the importance of a "component process" in designing reusable components
- Explained that the "configuring technique" is essential for customizing component behavior
- Introduced the concept of "compound components" and how they help in creating more complex UI designs
- Talked about the challenges faced when designing compound components and how to overcome them
- Provided examples of how different design systems can be used together within an organization
- Explained that the "le level component" approach helps in understanding better the organization's needs and preferences
- Discussed the importance of a "component process" in designing reusable components
- Introduced the concept of "level confidence complement" as an alternative to the traditional three-level confidence approach
- Talked about the challenges faced when designing components for different teams and product types
- Provided examples of how different design systems can be used together within an organization
- Explained that the "le level component" approach helps in understanding better the organization's needs and preferences
- Discussed the importance of a "component process" in designing reusable components
- Introduced the concept of "level confidence complement" as an alternative to the traditional three-level confidence approach
- Talked about the challenges faced when designing components for different teams and product types
- Provided examples of how different design systems can be used together within an organization
- Explained that the "le level component" approach helps in understanding better the organization's needs and preferences
- Discussed the importance of a "component process" in designing reusable components
- Introduced the concept of "level confidence complement" as an alternative to the traditional three-level confidence approach
- Talked about the challenges faced when designing components for different teams and product types
- Provided examples of how different design systems can be used together within an organization
- Explained that the "le level component" approach helps in understanding better the organization's needs and preferences
- Discussed the importance of a "component process" in designing reusable components
- Introduced the concept of "level confidence complement" as an alternative to the traditional three-level confidence approach
- Talked about the challenges faced when designing components for different teams and product types
- Provided examples of how different design systems can be used together within an organization
- Explained that the "le level component" approach helps in understanding better the organization's needs and preferences
- Discussed the importance of a "component process" in designing reusable components
- Introduced the concept of "level confidence complement" as an alternative to the traditional three-level confidence approach
- Talked about


## Users Don't have to Suffer in the Cloud | Melissa Jurkoic | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=Vcy3kLJnYoU](https://www.youtube.com/watch?v=Vcy3kLJnYoU)

 - User-centered approach is crucial for successful technology adoption
- Executive buy-in and end-user buy-in are equally important in project success
- Include stakeholder feedback throughout the entire product life cycle
- Understand user needs and job requirements before designing solutions
- Use a hub-and-spoke model to ease transition, focusing on end-user experience first
- Collaborate with users during design process to create inclusive experiences
- Maintain database integrity and accuracy for better insights and decision making
- Listen to user feedback and continuously improve the product
- Successful implementation equals successful adoption and retention
- Engage users throughout the entire life cycle of a project to ensure continued use and satisfaction


## Mindblowing Google PageSpeed Scores with Qwik | Misko Hevery | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=sCPLWf2cEY0](https://www.youtube.com/watch?v=sCPLWf2cEY0)

 - Google Page Speed Insights emphasizes the importance of time interactive score
- Builder.io CTO presents a solution called "Quick First" to achieve an amazing time interactive score
- The problem with existing frameworks is that they are replayable, which means downloading and executing large amounts of code ahead of time
- Quick First aims to delay as much code execution as possible and focus on making the initial render fast
- Bootstrapping is a crucial part of Quick First. It involves starting by sending HTML from the server and then setting up listeners for user interactions on the client side
- Existing frameworks struggle with fine-grained control over component rehydration and rendering, leading to unnecessary code downloads and execution
- Quick First focuses on resumable applications rather than replayable ones. This means that when a user leaves an application and comes back, it can quickly resume where they left off without having to download and execute large amounts of code again
- The key is to serialize the state of the application into HTML and then ship it to the client. When the client resumes the application, it can quickly rehydrate the state from the HTML and continue where it left off
- Quick First also emphasizes the importance of lazy loading. It aims to load only the necessary code when a user interacts with an application, rather than downloading everything upfront
- The goal is to achieve 100/100 Google Page Speed Insights scores for all websites built using Builder.io's platform


## High-Performance Web UI with Web Components | Cory Rylan | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=QmDToR6mLhk](https://www.youtube.com/watch?v=QmDToR6mLhk)

 - Web Components provide a way to encapsulate CSS and HTML within a custom element
- Dependency management is crucial when building web components, as it can impact performance and maintainability
- Tree shaking allows developers to remove unused code from their build, resulting in smaller payload sizes
- CDNs (Content Delivery Networks) help serve static assets quickly and efficiently, providing global access and redundancy
- Text compression is an important aspect of web component performance, as it reduces the size of payloads by eliminating repetitive data
- CSS custom properties can be used to define fallback values for variables, ensuring that components render correctly even if a variable has not been defined
- CS contain and visibility auto are two CSS properties that help optimize rendering performance by allowing browsers to skip unnecessary layout calculations and render work
- Lighthouse is a useful tool for measuring web component performance and identifying areas for improvement
- Rollup build tools can be used to track tree shaking, build output time, and other important metrics when building web components


## Content is King: How Contentful and CaaS are Changing | Aaron Ladage | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=QtEDq1mxiHg](https://www.youtube.com/watch?v=QtEDq1mxiHg)

 - Introduced contentful as the platform of choice for the digital experience company, deg
- Described the platform's focus on headless content services and its impact on performance and flexibility in a digital experience context
- Explained how contentful allows for easy customization and integration with other platforms and tools
- Demonstrated the power of content modeling and how it enables content to be reused, scaled, and adapted across different channels and mediums
- Showcased contentful's app framework and its ability to embed custom experiences directly into the platform
- Discussed the importance of environment management in contentful and how it allows for easy deployment and version control of content models and content
- Demonstrated the use of contentful's graphql API to pull and manipulate content, highlighting the platform's flexibility and ease of use


## Autoscaling Apps without Supersizing Costs | Lara Newsom | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=fVP-hdLoDU8](https://www.youtube.com/watch?v=fVP-hdLoDU8)

 - Developer deploy a lot of work in the cloud, and the cost can be high
- Cloud spend wastage is an issue: unused resources, unattended storage volumes, idle load balancers, etc.
- Mismanaged resource usage can lead to unnecessary costs
- Understanding pricing structures and tagging resources are key to controlling costs
- Use built-in tools or external tools for visibility into cloud spend
- Implement comprehensive tagging and labeling of resources
- Regularly audit and enforce tagging and labeling within pipelines
- Consider right-sizing instances, using spot instances, reserving instances, and exploring bulk pricing options
- Evaluate if the chosen service option is cost-effective
- Refactor code to optimize resource usage and reduce unnecessary costs


## The Legend of Zelda, Hexagonal Architecture & You | Jonathan Turner | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=VVR8xlgo9Po](https://www.youtube.com/watch?v=VVR8xlgo9Po)

 - Legend Zelda Ascii Art Hexagonal Architecture Presentation
- 2008 Bootleg Dmake Competition: Remake Legend Zelda as ASCII-based Console Game
- Fable Griselda: Web Application Development from C# Console App
- Challenges in Cross-Platform Game Development
- Blazor: Compiling C# to WebAssembly for Browser Execution
- Porting Fable Griselda Codebase to Blazor
- Comparison of Hexagonal, Onion, and Clean Architectures
- Mob Programming: Collaborative Software Development Technique


## Adding a Second Pair of Eyes with Visual Testing | Colby Fayock | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=MR2kl8I4_uE](https://www.youtube.com/watch?v=MR2kl8I4_uE)

 - Introduced Add Second Pair Eye Project and its focus on visual testing
- Demonstrated a UI gone wrong example in a supermarket app
- Discussed the importance of maintaining customer privacy while ensuring usability and functionality
- Showcased how automated tests can save time and prevent bugs, but also lead to technical debt if not maintained properly
- Introduced Cypress as a Javascript-based testing framework that enables real-time browser testing
- Explained the use of Apple's Visual Testing Platform (Apple Tool) with Cypress SDK for automated visual testing
- Provided an example of how to set up and run tests using the Apple Tool in a Cypress project
- Demonstrated adding the Apple Tool SDK to an existing Cypress test, running the test, and catching potential UI issues


## Building Resilient Serverless Applications | Yan Cui | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=k4wjj-bnpZs](https://www.youtube.com/watch?v=k4wjj-bnpZs)

 - Resilience in service applications
- Importance of building applications that can recover quickly from different types of failures
- AWS CTO Verner Vogels' famous quote: "Everything fails, all the time. Eventually it will be your application."
- Building resilient APIs using AWS services like API Gateway, Lambda, and DynamoDB
- Using multirex zones to prevent failure in case of an entire availability zone or region going down
- Managing distributed transactions with Saga patterns
- Implementing retry logic for failed requests and handling poison messages
- Using Amazon Kinesis Data Streams (KDS) to process data streams and handle failures gracefully
- The importance of monitoring and testing in building resilient applications
- Chaos Engineering principles and how they can be applied to identify weaknesses in applications
- Case studies of real-world applications that have implemented these practices successfully


## Gaining Confidence with Cypress Tests | Rob Richardson | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=5Nhv7HIScWE](https://www.youtube.com/watch?v=5Nhv7HIScWE)

 - Introduction of Cypress as a reliable web testing tool
- Gaining confidence in using Cypress for test automation
- Demonstrating the use of Cypress with TypeScript and GitHub code examples
- Comparing different browser testing tools: Selenium, Cyprus, TestCafe, Playwright
- Exploring Cypress's features and advantages over other tools
- Walkthrough of Cypress IDE and its capabilities for end-to-end testing
- Setting up a test project with Cypress and running tests in the browser
- Discussion on debugging and troubleshooting tests using Cypress IDE
- Comparison between different frontend frameworks (MVC) using Cypress
- Testing API calls and working with mock data using Cyprus fixtures
- Best practices for writing maintainable and descriptive tests in Cypress
- Using commands to abstract away test implementation details
- Demonstrating how to use Cypress to authenticate and run end-to-end tests on a website
- Understanding the importance of using fixtures to reuse mock data across multiple tests
- Discussion on using CyIntercept command for intercepting API calls during testing


## Angular + Jest: Testing Titbits | Maria Korneeva | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=HfKdktNB9wA](https://www.youtube.com/watch?v=HfKdktNB9wA)

 - Introduction by Maria Corneva, Frontend Technology Lead at Aleri
- Focus on unit testing an Angular application
- Testing strategies: pragmatic and strategic approach to test critical features first
- Importance of mocking in testing
- Discussion about error handling in testing
- Code snippets showcasing different types of tests (component, service, pipe)
- Tips for writing effective unit tests
- Overview of the Nx workspace structure and its benefits
- Real-world examples of testing scenarios
- Demonstration of common testing patterns using Jest
- Discussion about the importance of testing HTTP requests and error handling
- Suggestions for improving test execution and rerun options
- Encouragement to use plugins like "Runner" for better testing experience
- Conclusion and Q&A session


## Challenges in Building Micro Front Ends| Vishal Kumar | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=cP7_GS5mN7I](https://www.youtube.com/watch?v=cP7_GS5mN7I)

 - Microfrontends: A solution to complex monolith applications
- Benefits of using microfrontends
  - Independent, deliverable frontend applications
  - Faster development and deployment cycles
  - Easier maintenance and scalability
  - Improved isolation and security
  - Better performance and flexibility
- Challenges of implementing microfrontends
  - Complexity: CI/CD pipelines, infrastructure, and operational complexity
  - Testing: Ensuring all components work well together
  - Security: Protecting sensitive data and preventing cross-site scripting attacks
  - UI inconsistency: Maintaining a consistent look and feel across different applications
  - Increased payload: Avoiding bloat and optimizing performance
- Solutions to challenges
  - Iframes, web components, module federation, and other techniques for building microfrontends
  - Security measures like CORS, Content Security Policies, and testing tools like Cypress and Aptly
  - Component interaction: Using custom events, callbacks, or APIs
  - Shared state management: Avoiding global state and using local storage instead
  - Testing strategies: Unit tests, integration tests, and end-to-end testing
  - Accessibility: Ensuring all users can access the application
  - UI consistency: Using design systems, component libraries, and consistent coding styles
  - Performance optimization: Minimizing payload size, using lazy loading, and avoiding heavy dependencies
  - Monorepo strategy: Managing multiple repositories as a single project for easier code sharing and maintenance
- Implementing microfrontends with module federation
  - Creating separate apps and components
  - Using nx or similar tools to manage the build process
  - Configuring webpack and setting up remote entry points
  - Dynamically importing components and using them in other applications
  - Testing and ensuring component compatibility
- Future of microfrontends: Model federation, module federation improvements, and new technologies like Angular Elements.


## Good Code is a Balancing Act | Jonathan Warrington | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=35OTQ-JYqsE](https://www.youtube.com/watch?v=35OTQ-JYqsE)

 - Full Stack Developer John Warrington discusses good code and balance in the software industry.
- Focus on easily understood, quickly readable code, while also considering performance.
- Rule 1: Function should be no more than 10 lines long (or less).
- Rule 2: Include only one control structure per function.
- Rule 3: Have only one return statement per function.
- Use interfaces to allow for mocking parts of the application away for testing.
- Balance descriptive, concise naming conventions for variables and functions.
- Comment code when necessary; avoid commenting simple, self-explanatory functions.
- Strive for balance in all aspects of coding, including readability, complexity, and maintainability.


## Develop from Anywhere with GitHub Codespaces | Brigit Murtaugh | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=ZHHk9wG4Cig](https://www.youtube.com/watch?v=ZHHk9wG4Cig)

 - GitHub Codespaces:
  - Removes the need to clone source code locally.
  - Provides a productive environment for contributing to projects.
  - Allows developers to start working on a project immediately without setting up local development environments.
- Dev Containers:
  - Customize and finetune the Codespaces environment for specific apps or use cases.
  - Ensure anyone else can work in the same environment with the exact same development experience.
  - Use Docker-based development to set up an isolated container environment.
- Remote Container Extension (VSC):
  - Allows developers to work locally on their machines while still taking advantage of Codespaces' features.
  - Provides a way to separate the local environment from Codespaces without needing cloud-based backend compute.
  - Enables the use of dev containers on local machines, remote VMs, and even within the browser.


## MFEs , Micro-Frontends with Module Federation and Angular| Manfred Steyer | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=EGdbmj-kj88](https://www.youtube.com/watch?v=EGdbmj-kj88)

 - Module federation and web components
  - Share code, libraries, and frameworks across different applications
  - Use module federation to load and share code from separate bundles
  - Web components provide a standard way of creating custom HTML elements
- Combining different versions and frameworks
  - Loading and sharing different versions of the same library or framework
  - Discussed potential issues when combining different technologies, such as loading multiple instances of the same framework
- Demonstration using module federation, web components, and different frameworks
  - Showcased a demo application that uses module federation to load and share code across different micro frontends built with Angular, React, and Web Components
- Pitfalls and challenges
  - Discussed potential pitfalls when combining different technologies, such as handling version conflicts and managing bundle size
  - Mentioned the need for a good reason to combine different versions of the same library or framework
  - Highlighted the importance of caching platform instances and using helper functions to handle router tricky situations


## Innovations with FAST Web Components | Rob Eisenberg & David Rickard | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=o5dylQiigUQ](https://www.youtube.com/watch?v=o5dylQiigUQ)

 - Web Components are a key part of Microsoft's Fast team, providing fast and reusable components for web development.
- They enable developers to build first-time reusable components that work across different libraries and frameworks, offering a technology-agnostic approach.
- The core standard was implemented in all major browsers beginning 2020, with Microsoft's Fast team shipping the necessary native set of components.
- Web Components have been used by various companies like Google, Nintendo, SpaceX, and Adobe, as well as Microsoft itself.
- A specific case study from David Rickard showcased the performance improvement when upgrading the Edge New Tab Page using Fast Web Elements, reducing page load time by 20% and 31% in total time to interactive (TTI).
- The use of Web Components also simplifies component development, eliminating the need for complex state management and redux.
- Fast Web Elements offer a more streamlined approach to component development, with features like delay loading elements and dynamic imports that make web pages load faster.


## A More Fluid Pyramid | Steve Upton | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=VFRXPjoaEUc](https://www.youtube.com/watch?v=VFRXPjoaEUc)

 - Test Pyramid: A common model in testing strategies, with the foundation being unit tests, followed by integration tests and ending with end-to-end tests.
- Layer Confusion: The presenter acknowledges that there's confusion about which layer is which, but emphasizes that every project and team labels tests differently.
- Test Pyramid Adaptation: The speaker suggests a more fluid approach to the test pyramid by using different layers based on the specific needs of the project or team.
- User Journey Tests: Highly important for testing real user journeys, but can be slow and expensive due to their comprehensive nature.
- API Tests: A layer lower in the pyramid, they're faster and simpler than user journey tests, but not as flaky.
- Test Duplication: The speaker advises against duplicating tests across layers, as it can lead to confusion and unnecessary maintenance work.
- Trade-offs: The presenter emphasizes that every layer in the test pyramid has its own trade-offs, and teams should be aware of these when deciding which tests to use.
- Test Pyramid Limitations: The speaker acknowledges that the test pyramid model isn't perfect and can't capture all possible risks or uncertainties in a system.
- Exploratory Testing: A powerful tool for discovering unknown issues, but it's not part of the traditional test pyramid model.
- Model Approximation: The speaker highlights that any model, including the test pyramid, is an approximation and doesn't perfectly capture reality. However, they are useful tools for understanding complex systems and making informed decisions.


## From Cobol to Node with DevOps | Alejandro Mercado Peña | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=8IlhYeYbtLI](https://www.youtube.com/watch?v=8IlhYeYbtLI)

 - Presenter introduces himself and shares his background in programming and development.
- He discusses the longevity of COBOL, a programming language designed in 1959, and its widespread use in financial institutions.
- The presenter highlights that despite being old, COBOL is still widely used due to its robustness and adaptability to business changes over time.
- He mentions the importance of developer experience and how tools like Visual Studio Code can help developers work more efficiently with older languages.
- The presenter talks about running COBOL programs in modern environments, such as cloud platforms and containers.
- He emphasizes that IBM Cloud supports COBOL programming, which is a significant factor for its continued use.
- The presenter discusses the importance of Docker containers in supporting legacy languages like COBOL.
- He mentions that running COBOL programs inside containers can help modernize and scale these systems more effectively.
- The presenter highlights the shift from monolithic architecture to microservices architecture as a way to improve scalability and flexibility in software development.
- He talks about how Node.js, a popular JavaScript runtime, can be used to extend COBOL programs by creating microservices that communicate with each other using APIs.
- The presenter suggests that running COBOL applications inside containers using Kubernetes orchestration can help streamline deployment and management processes.


## All the World's A Staging Server |Heidi Waterhouse | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=a1OBVrkBLS4](https://www.youtube.com/watch?v=a1OBVrkBLS4)

 - Importance of understanding deployment and release in reliable web development
- Difference between deployment and release: Deployment is about getting software to a destination (e.g., server, mobile device), while release is a business decision that involves user experience
- Challenges with testing production and staging environments
  - Production environment cannot be 100% uptime due to potential issues or dependencies
  - Staging environments may not accurately represent production behavior due to unstated assumptions, lack of real data, and incomplete feature implementation
  - Difficulty in replicating production environments due to complex dependencies and resource scaling
- Importance of feature flags and dark launching for managing deployment complexity
  - Feature flags allow controlled rollout of new features to specific user groups or environments
  - Dark launching involves releasing a new feature to a small, select audience without immediately broadcasting its availability
- The concept of continuous integration and continuous delivery (CI/CD) and their role in rapid feature development and deployment
  - CI/CD allows for frequent, automated testing and integration of code changes into the main codebase
  - It helps ensure that only high-quality, tested code is deployed to production environments
- The importance of understanding system behavior and dependencies in a microservices architecture
  - Microservices architectures require careful planning and testing to ensure that all components work together seamlessly
  - Feature flag testing can help identify potential issues or dependencies before they affect the overall system
- The concept of integration testing and its role in ensuring system reliability
  - Integration testing involves testing how different components of a system interact with each other, especially when using microservices architectures
  - It helps ensure that all parts of the system work together correctly and can handle unexpected inputs or failures


## Crafting Reliable and Testable Code with TypeScript | Doguhan Uluca | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=piBGqyjl-JE](https://www.youtube.com/watch?v=piBGqyjl-JE)

 - Importance of reliable code
- Crafting reliable and testable code with Typescript
  - High Cohesion, Low Coupling, DRY (Don't Repeat Yourself), KISS (Keep It Simple, Stupid) principles
  - AC/DC principle: Avoid Complexity, Depend on Code
  - Self-documenting code through comments and tools like Swagger
  - Unit Test Driven Development mindset
    * Write testable code
    * Red-Green-Refactor development cycle
    * Solid Principles: Single Responsibility Principle, Open/Closed Principle, Liskov Substitution Principle, Interface Segregation Principle, Dependency Inversion Principle
  - Stateless Data Driven Design and Shifting Complexity Back End
  - Iterative Incremental Design for implementing features
  - Embracing Reactive Programming
- Typescript benefits:
  * Enables solid code refactoring
  * Export reusable functions
  * Use interfaces to enforce data shape and type safety
  * Document code with JSDoc comments
  * Unit Testing using Jest or similar tools
  - Lean, Common Scrum methodologies for project management
- Case studies:
  * Weather API application
  * Landmark Luminar Server application
  - Use of GraphQL and MongoDB in backend development


## Achieving Zero Fronted Crashes in Production | Josh Goldberg | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=dfLa5DWZdbY](https://www.youtube.com/watch?v=dfLa5DWZdbY)

 - Static and Dynamic Analysis: Josh discusses the importance of static analysis tools like ESLint, Prettier, and TypeScript for catching bugs early in development. He mentions that dynamic analysis techniques such as unit tests and end-to-end testing are also crucial for finding issues later in the process.
- Frontend Monitoring: Josh explains the need for monitoring tools to understand crash production and scale. He highlights the importance of aggregating, filtering, and deduplicating bug reports to get a clear picture of the issue.
- Blameless Postmortem: Josh emphasizes the importance of learning from mistakes rather than blaming individuals. He suggests that teams should focus on understanding the root cause of an issue and improving the system to prevent similar problems in the future.
- Gradual Constriction: Josh proposes a strategy for reducing crash production over time by setting goals, implementing prevention techniques, and gradually tightening constraints.
- System Understanding: Josh stresses the importance of understanding the entire system, including user needs, team communication, and error handling processes. He suggests that teams should continuously learn from mistakes and improve their systems to prevent future issues.


## Using Storybook to Maintain Components and RedwoodJS | Milecia McGregor | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=QQ5ftrQTMnA](https://www.youtube.com/watch?v=QQ5ftrQTMnA)

 - Intro: Melissa is a Developer Advocate at IterativeAI, discussing Storybook and RedwoodJS.
- Background: 7+ years of experience in frontend/backend development and DevOps engineering.
- Component Driven Development (CDD): Model system better with independent components; use tools like Bootstrap or TypeUI libraries.
- Storybook: A tool to develop components in isolation, useful for testing and documentation.
- RedwoodJS: A full-stack JavaScript framework that integrates well with Storybook.
- Demo: Creating a new Redwood app and adding a custom component using Storybook.
- Key Points: 
  1. CDD makes it easier to maintain long-term projects, especially when there is a change in requirements or team members.
  2. Storybook allows developers to work on components without worrying about the overall application structure.
  3. RedwoodJS provides built-in support for Storybook integration and testing, making it easy to scale applications.


## Monitoring Your Apps is not About Devops | Iván Olivares Rojas | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=T0aBlzdv27g](https://www.youtube.com/watch?v=T0aBlzdv27g)

 - Observability 101: Ivan Olivares introduces the concept of interthings and talks about the importance of understanding an application's changes from a user perspective.
- DevOps Culture: He discusses the role of devops in organizations, emphasizing its benefits for business agility, speed, quality, and cultural change.
- Observability vs Monitoring: Ivan highlights the advantages of observability over traditional monitoring, including gaining focus on business growth, understanding application performance, and providing a multidisciplinary team approach to problem-solving.
- Importance of Observability: He explains how observability allows organizations to expose data, analyze trends, and make informed decisions based on system behavior.
- Open Telemetry: Ivan introduces the open telemetry standard, which helps standardize instrumentation, metric, log, and trace collection for applications.
- Anatomy of Observability: He discusses the three key components of observability - telemetry, storage, and visualization - and how they work together to provide a comprehensive view of application performance.
- Benefits of Observability: Ivan lists several benefits of applying observability practices, including improved communication between teams, faster incident response times, and better understanding of system health and impact on business.


## The Effective Development - End (What) End | Shai Reznik | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=RGtOXLKvisY](https://www.youtube.com/watch?v=RGtOXLKvisY)

 - Introduced as a test effective guy and known for his Angular testing expertise.
- Talks about the importance of cost-effective testing in companies with tight deadlines.
- Shares a personal experience of feeling overwhelmed by bugs and poor code quality while working on a startup.
- Learned that automating tests can save time and prevent bugs.
- Discusses the difference between unit and integration tests, and how they can be used to improve testing efficiency.
- Emphasizes the importance of writing end-to-end (E2E) tests to ensure that all parts of an application work together seamlessly.
- Explains how manual testing is time-consuming and inefficient, while automating E2E tests can help developers catch bugs earlier in the development process.
- Introduces a concept called "smoke testing," which involves writing automated tests to quickly identify critical issues before releasing software to users.
- Suggests using Cypress as a smoke testing tool due to its fast setup, easy debugging capabilities, and strong support for developers.
- Encourages developers to learn more about test effective strategies by taking a free quiz available on the website.


## From Horror Story to Fairy Tale: Writing Code | Michael Dowden | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=Eo4jgALvH30](https://www.youtube.com/watch?v=Eo4jgALvH30)

 - Importance of clear and concise code communication
- Avoid ambiguity in naming conventions
- Use semantics and context to convey meaning
- Choose meaningful names for variables, methods, classes, etc.
- Accessibility is crucial for understanding code
- Automation can help with code readability and consistency
- Inclusivity and diversity in coding language are important
- Good communication within a team helps maintain consistent code standards
- Code reviews can improve overall code quality and readability
- Testing and debugging are essential parts of the coding process


## Blazor Stability Testing for Bullet Proof Application| Ed Charbeneau | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=dKswEXxCXAw](https://www.youtube.com/watch?v=dKswEXxCXAw)

 - Ed Charbonneau, Principal Developer Advocate at Progress Software, discusses Blazer stability testing and tools
- He emphasizes the inherent testability of Blazer applications due to its C# foundation and ability to use the same language across back end and front end
- XUnit is the most downloaded testing framework for .NET with over a million downloads
- Blazer uses a component-based approach, allowing developers to easily identify and test individual components
- The speaker highlights the importance of using unit tests, integration tests, and full system tests when developing applications
- He mentions that XUnit is commonly used for front end unit testing in combination with BUnit (Blazor Unit Testing library) for component level testing
- He also discusses the use of Telerik UI Blazer, which provides a tightly integrated product deal and helps process integration
- The speaker demonstrates how to write an XUnit test for a Blazer application using the Fact attribute and describes the importance of writing tests that fail initially before they can be refactored safely
- He also discusses the use of BUnit for component testing within the Blazor framework, which allows developers to leverage their favorite unit test library alongside Telerik's Blazor testing tool
- The speaker provides a brief tour of a sample project using unit tests and demonstrates how to create an XUnit test for a component
- He emphasizes the importance of writing automated, repeatable tests that can be run in an end-to-end fashion
- The speaker discusses the use of Telerik Mocking Tool, which helps isolate code and focus on testing specific components
- He also talks about the importance of using mocks to handle external services and data sources
- The speaker demonstrates how to write an integration test for a Blazer application using BUnit and discusses the importance of setting up dependencies correctly to ensure that tests run successfully
- Finally, he discusses the use of Telerik Test Studio, which is a powerful tool for testing entire applications end-to-end, including browser compatibility testing


## Level-up Your DevOps with GitHub Actions & Kubernetes | Rob Richardson | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=OWJLV2ZKTgA](https://www.youtube.com/watch?v=OWJLV2ZKTgA)

 - Introduced GitHub Actions and Kubernetes for CI/CD
- Explained how to build a Dockerfile, push it to a container registry, and deploy it on Kubernetes
- Demonstrated setting up a GitHub repository with a .github/workflows file for automated builds
- Shared tips for managing secrets in GitHub Actions and Kubernetes
- Discussed using Helm for simplifying Kubernetes deployments
- Showcased how to set up logging and monitoring for Docker and Kubernetes clusters
- Demonstrated building and testing a web application with Docker, GitHub Actions, and Kubernetes
- Explained the importance of pull requests in managing code changes and builds
- Shared tips for optimizing CI/CD pipelines and reducing build times


## The Worlds Most Expensive React Component | Michael Chan | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=zxVZssf2o6U](https://www.youtube.com/watch?v=zxVZssf2o6U)

 - Talk about expensive React components and their performance
- Introduce Michael Chan, creator of the React Podcast and part of the new React working group
- Discuss the importance of collaborative performance and how it affects design decisions
- Focus on interface design and component API design as key aspects of performance optimization
- Define an "expensive" React component: one with many renders, heavy paint, or long load times due to unclear design or poor pattern usage
- Present a real-world example of a costly React component and its impact on the product suite
- Talk about the importance of refactoring components to improve their performance
- Discuss how linting rules can sometimes hinder collaboration and productivity
- Emphasize the need for clear communication, listening skills, and root problem identification within teams
- Highlight the benefits of component colocation in promoting collaboration and reducing organizational tension
- Mention the impact of cultural and social factors on team dynamics and performance


## Maintainable Styles- That's a Thing? | Alyssa Nicoll | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=h6q84Kk8lyU](https://www.youtube.com/watch?v=h6q84Kk8lyU)

 - Alyssa Nichol discusses her passion for CS due diligence and maintaining a style that is both accessible and maintainable.
- She shares her excitement about creating a plan to inspire others in the field of web development.
- The talk covers advanced plans, accessibility, inclusivity, and more.
- Alyssa explains the importance of understanding accessibility and how it can be used to create better user experiences.
- She introduces the concept of semantic markup, which involves using HTML elements correctly to enhance accessibility.
- The talk demonstrates how to create accessible components in a codepen environment.
- Alyssa emphasizes the importance of considering default and null states when designing user interfaces.
- She discusses the use of ARIA labels to improve accessibility for users with screen readers or other assistive technologies.
- The talk highlights the need for clear labeling and proper use of placeholders in web forms.
- Alyssa shares her experience with visually hidden classes and how they can be used to enhance accessibility while maintaining a clean design.
- She explains the importance of using semantic HTML elements, such as h1 and section, to improve accessibility and maintainability.
- The talk highlights the use of SASS variables for styling and the benefits of scoping styles.
- Alyssa shares her experience with designing buttons and how she uses mixins to create consistent styles across different components.
- She emphasizes the importance of considering browser compatibility when designing web interfaces.
- The talk introduces the concept of live regions, which can be used to provide real-time updates to users with screen readers or other assistive technologies.
- Alyssa shares her experience with using Figma for collaboration and how it has helped her team maintain consistency in their designs.
- She encourages the use of tools like Kendo UI to help developers create accessible and maintainable web interfaces.


## Reliability and Engineering Requirements | Giorgio Natili | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=VD8w-M18JV8](https://www.youtube.com/watch?v=VD8w-M18JV8)

 - Requirement validation is crucial for building a reliable system
- Use checklists, document-based reviews, and discussions to validate requirements effectively
- Dissecting requirements helps identify conflicts and areas of improvement
- Documentation is essential for tracking decisions and resolving conflicts
- Conflicts can arise due to different stakeholder perspectives, priorities, and constraints
- Escalating conflicts to higher levels may be necessary when negotiations fail
- Focus on system uniqueness and understanding constraints to develop a robust reliability checklist


## Azure Static Web Apps | Jon Papa & Dan Wahlin | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=ldWQT2HazGU](https://www.youtube.com/watch?v=ldWQT2HazGU)

 - Azure Static Web Apps provides a reliable, globally distributed web hosting platform with built-in CI/CD integration, custom domains, and serverless APIs.
- Dan Walling demonstrates building a shopping app using different frontend frameworks (Angular, React, etc.) and deploying it to Azure Static Web Apps.
- The demo showcases the ease of setting up continuous deployment from GitHub or Azure DevOps, as well as configuring authentication and authorization options.
- Key features include automatic SSL provisioning, custom domain support, and the ability to set serverless API routes and roles.
- Dan emphasizes the importance of a reliable deployment process, including the use of CDNs for global scale and the ability to create different environments (e.g., staging, production) for testing and deployment.
- The platform supports various authentication providers such as Twitter, Github, and Azure Active Directory, allowing developers to easily integrate user authentication into their applications.


## Tools of Intentional Architectures | Dinesh Ramadoss | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=lYasQYABabE](https://www.youtube.com/watch?v=lYasQYABabE)

 - Importance of Intentional Architecture
  - Avoids accidental architecture
  - Drives quality and success
- Architectural Decision Making Process
  - Stakeholder involvement crucial
  - Quality Attribute Workshop method
    * Characterize, prioritize, and refine scenarios
    * Use well-formed scenarios to guide downstream activities
  - Designing Satisfies Quality Attributes
    * Top-down and bottom-up approach
    * Balance business and technical requirements
  - Architecture Documentation
    * Communicates design decisions
    * Educates, negotiates, and gets buy-in
    * Documents decision rationale and impact
  - Evaluating Architecture
    * Aligns with fundamental evaluation principles
    * Complements scenario-driven approach
    * Identifies risks early in the life cycle
    * Improves communication among stakeholders
  - Managing Technical Depth
    * Understand debt repayment and impact on system properties
    * Quantify depth's impact on business indicators
    - Use a methodical process to manage technical depth
- Steering Architecture Away from Accidents
  - Follow a repeatable, predictable process
  - Focus on intentionally driving success
  - Leverage organization reference and highly recommended resources


## Reliable System +  Azure Static Web Apps | Craig Shoemaker | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=SQIcbIBcW3E](https://www.youtube.com/watch?v=SQIcbIBcW3E)

 - Craig Shoemaker presents a demo on building reliable systems with Azure Static Web Apps
- Demonstrates an application for a volunteer organization using UI, backend API, and various storage mechanisms
- Explains the use of different Azure services like Azure Functions, Storage, and Queue to build the application
- Uses GitHub and Bitly for sharing code and demo repositories
- Discusses the Nuance of using Azure Static Web Apps in a real-world scenario
- Shows how to combine an existing Azure Function App with Azure Static Web Apps instance
- Demonstrates the use of CLI commands to deploy and run the application locally and on Azure
- Explains the importance of linking UI and backend API using Azure Static Web Apps
- Discusses error handling, testing, and deployment process in detail


## Collaborative Code with Nx | Brandon Roberts | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=9g_87UG5dYE](https://www.youtube.com/watch?v=9g_87UG5dYE)

 - Nx build framework: A smart, extensible tool for building monorepos and promoting code sharing
- Monorepo benefits: Shared code visibility, reusability, atomic changes, developer mobility, consistent way of building/testing applications, and single version dependency management
- Nx drives monorepos: By providing a mental model (Nx way), efficient project graph, task graph, metadata driven tools, and integration with modern web development tools.
- Mental model: Helps to efficiently drive large codebases and projects in a consistent manner.
- Project graph: A tool that creates a graph based on the source code repository, external dependencies, and application libraries. It is used for code analysis tasks, running targets, and metadata driven tools.
- Task graph: A feature of Nx that allows developers to create task graphs anytime they run a command. This helps in efficient execution of tasks and provides a way to cache previously run computations based on state changes.
- Metadata driven tools: Enable toolability by providing default values, validation, auto completion, and integration along with the metadata used. 
- GitHub & IDE integrations: Nx provides seamless integration with popular platforms like GitHub and IDEs such as WebStorm and VS Code for a better developer experience.
- Consistent commands: Nx helps developers to define common commands that can be targeted across multiple applications within the same workspace.
- Computation caching: A feature of Nx that provides functionality for computation caching at both local and distributed levels, which improves performance and reduces redundancy in tasks.
- Extensibility & Ecosystem: Nx supports extensible plugins and has a rich ecosystem with support for popular frameworks like React, Angular, Node, etc., along with automatic upgrade to the latest versions of these tools.


## Knowing Your TCO (Total Cost of Ownership) | Owen Buckley | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=6QBf5QCRSPI](https://www.youtube.com/watch?v=6QBf5QCRSPI)

 - Owen Buckley discusses the concept of Total Cost of Ownership (TCO) in software development, specifically focusing on open-source projects and modern web development
- TCO goes beyond just the initial purchase price; it includes ongoing costs such as maintenance, updates, and potential security risks
- The analogy of an "inverse iceberg" is introduced to help visualize the hidden costs beneath the surface of a project or technology stack
- The importance of intentional decision making in selecting tools and technologies is emphasized, with the goal of minimizing risk and maximizing benefits for the user or client
- Acknowledgment that choosing the right tool or framework can be challenging due to the vast array of options available, but that careful consideration and research can lead to better outcomes
- The concept of "minimum viable developer experience" is discussed, emphasizing the importance of balancing productivity with the need for a stable and reliable development environment
- The speaker encourages attendees to always work backwards from the problem they are trying to solve when making decisions about technology choices, in order to ensure that the solution meets their specific needs and requirements


## TDD - It's About More Than Just the Tests | Jonathan Turner | Reliable Web Summit 2021

URL: [https://www.youtube.com/watch?v=ad0XTtZm83g](https://www.youtube.com/watch?v=ad0XTtZm83g)

 - Introduced Test Driven Development (TDD)
- Discussed three laws of TDD
- Explained red, green, refactor cycle in TDD
- Demonstrated TDD on a Roman Numeral to Arabic Number conversion problem using C# and NUnit
- Showcased how to write tests that fail first, make them pass, then refactor the code
- Discussed how to apply simple solutions to make tests pass
- Shared the importance of decomposition in breaking down complex problems into smaller ones
- Demonstrated how to use a test kata (a practice exercise used by martial artists) to improve coding skills and solve a problem
- Explained the concept of code smells and how refactoring can help make code better
- Showcased how to create a simple, maintainable solution using TDD
- Provided additional resources for learning more about TDD and code katas



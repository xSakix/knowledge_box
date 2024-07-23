## Nordic.js 2022 • Christophe Porteneuve - So, what’s new in ES2025?

URL: [https://www.youtube.com/watch?v=FaQA0qU5e6o](https://www.youtube.com/watch?v=FaQA0qU5e6o)

## Summary of Transcript

- JavaScript language evolution overview
  - ECMAScript standardization process
  - Key features introduced in recent years
    * ES6, ES2015: arrow functions, let/const, classes, modules
    * ES7, ES2016: exponentiation operator, async/await
    * ES8, ES2017: Object.values(), Object.entries()
    * ES9, ES2018: async generator functions, Promise.prototype.finally()
    * ES10, ES2019: Array.prototype.flat(), String.prototype.padStart/padEnd()
    * ES11, ES2020: BigInt, nullish coalescing operator (??), optional chaining (?.)
- Current and future JavaScript features
  - Optional chaining (?.)
  - Named capture groups in regular expressions
  - Static initializers for classes
  - Private class fields with # prefix
  - Promise.allSettled() method
  - Array.prototype.findLastIndex() method
- Proposed features and<|im_start|>6 month timeline (2023)
  * Temporal proposal (date/time library)
    * Moment.js, Luxon.js
  * Import assertions for JSON modules
  * Decorators for classes
  * Improved regular expression support
- Future features beyond 6 months timeline
  * Immutable arrays
  * Decorators for properties and methods
  * Pattern matching in JavaScript
  * Pipeline operator (|>)


## Nordic.js 2022 • Yuraima Estevez & Lo Kim - Evolving your Design System through Data

URL: [https://www.youtube.com/watch?v=3ElDmqSGkmY](https://www.youtube.com/watch?v=3ElDmqSGkmY)

- Introducing the speaker and their role at Shopify
  - Lo Im, Senior Frontend Developer at Shopify
  
- Briefly explaining what Shopify is
  - Ecommerce platform that helps merchants sell products online to customers anywhere in the world
  
- Introducing Polaris Design System
  - Created by Shopify back in 2017 as an internal tool for building apps and admin panels
  
- Discussing the growth of Polaris Design System
  - Began with a focus on ecommerce but has since expanded to cover various aspects of the platform
  
- Explaining the challenges faced when scaling the design system
  - Custom Solutions built using Polaris components made it difficult to implement sweeping changes across the admin panel
  
- Discussing the approach taken to address these challenges
  - Focused on enabling sweeping changes in the admin panel by creating a comprehensive data dashboard that tracks design token usage and component coverage
  
- Highlighting the success of this approach
  - Increased Polaris component coverage from 16% to 90% within one year
  
- Introducing the concept of "work inception"
  - A process used by Shopify teams to identify and prioritize projects based on their potential impact on the platform
  
- Showcasing some examples of successful projects that have used data to drive decision making
  - Breakpoints: Identified and consolidated frequently used breakpoints across the admin panel, reducing the number from 300 to five
  - Typography: Analyzed typography usage across the platform and rebuilt the typography component to improve flexibility and coverage
  
- Introducing a new tool called "Polaris Migrator"
  - A command-line interface that automates the process of migrating between different versions of the Polaris Design System, making it easier for developers to upgrade their apps and admin panels
  
- Discussing the future plans for the Polaris Design System
  - Continuing to expand coverage and improve flexibility while maintaining a strong focus on data-driven decision making


## Nordic.js 2022 • Carly Litchfield - Interviews for developers, by developers

URL: [https://www.youtube.com/watch?v=MOtkGvbKqaA](https://www.youtube.com/watch?v=MOtkGvbKqaA)

- Carly, a software engineer at Galileo Health, shares her experience and insights on the impact of traditional technical interviews in the hiring process.
- She mentions that traditional technical interviews can be stressful, time-consuming, and may discourage candidates from applying to certain companies.
- A study by Microsoft and North Carolina State University found that technical interviews are often structured poorly and can lead to poor candidate experiences.
- Carly suggests alternative interview methods such as take-home projects or pair programming exercises, which can help assess a candidate's skills more effectively and reduce the stress associated with traditional technical interviews.
- She also recommends allowing candidates to choose their preferred assessment method, so they can showcase their strengths better.
- Finally, she encourages companies to examine their current hiring processes and consider making changes that will make them more attractive to potential candidates.


## Nordic.js 2022 • Sara Vieira - From Blender to the Web - the Journey of a 3D Model

URL: [https://www.youtube.com/watch?v=ji6q_P-QY_E](https://www.youtube.com/watch?v=ji6q_P-QY_E)

- Introduced himself and his background
- Discussed his experience with 3D modeling software Blender, highlighting its intimidating interface but its free and open-source nature.
- Demonstrated the basics of using Blender for 3D modeling, such as selecting objects and manipulating their properties.
- Explained the concept of a "blend file" and how it can be exported in various formats, including GLTF.
- Showcased how to use React and Reactive Fiber to integrate 3D models into web applications.
- Demonstrated how to animate 3D models using JavaScript and the Three.js library, as well as how to apply lighting effects and shadows.
- Discussed the differences between Eevee and Cycles rendering engines in Blender.
- Explained how to use the Frosting library to easily modify the appearance of a 3D model in real time.
- Showcased some advanced techniques for working with 3D models, such as applying contact shadows and using orbit controls.
- Concluded by discussing his personal journey learning 3D modeling and web development, and encouraged others to explore these fields as well.


## Nordic.js 2022 • Piérre Reimertz - What the web3 is going on?!

URL: [https://www.youtube.com/watch?v=8LdS8GNFu9E](https://www.youtube.com/watch?v=8LdS8GNFu9E)

## Summary
- Pierre Ramez from HiFi Lab discusses web3, ethereum, and decentralized technology.
- He highlights the importance of open protocols, community-driven development, and read/write access in maintaining a decentralized ecosystem.
- He explains how gas is used as a form of payment for transactions on the blockchain, and how proof of stake can help reduce energy consumption.
- He demonstrates how to interact with ethereum wallets using tools like Rainbow Kit and Metamask, and how to create and deploy smart contracts using Solidity.
- He emphasizes the need for security measures when working with decentralized technology, and encourages users to stay informed about the latest developments in the field.


## Nordic.js 2022 • Ujjwal Sharma - Multicore JavaScript: Past, Present and Future

URL: [https://www.youtube.com/watch?v=pN1Ez6aDcSA](https://www.youtube.com/watch?v=pN1Ez6aDcSA)

- Introduced himself and his work
- Talked about the purpose of JavaScript and its evolution over time
- Discussed the concept of concurrency and how it's important in modern computing
- Explained the difference between a web-like model and a thread-based model
- Mentioned that JavaScript has a variety of ways to handle asynchronous programming, including promises and async/await syntax
- Talked about the challenges of writing multithreaded code in JavaScript and how it's evolving with new proposals like vasm GC
- Discussed the importance of hardware utilization and how it affects JavaScript performance
- Explained that there are different ways to write concurrent code in JavaScript, such as using workers or sharing data between threads
- Talked about some of the challenges of writing multithreaded code in JavaScript, including synchronization issues and data races
- Mentioned that there are new proposals for improving JavaScript's support for concurrency, such as the thread-based model and the concurrent standard library
- Discussed how these new proposals could help developers write better multithreaded code in JavaScript
- Encouraged listeners to follow along with the progress of these proposals on GitHub


## Nordic.js 2022 • Debbie O'Brien - Testing Web Applications with Playwright

URL: [https://www.youtube.com/watch?v=Cjg545ew1q8](https://www.youtube.com/watch?v=Cjg545ew1q8)

- Introduction of the speaker and his background.
- Explanation of Playwright, its features, and benefits.
- Demonstration of setting up and installing Playwright.
- Discussion on writing tests using Playwright and code generation.
- Testing across multiple domains, platforms, and devices.
- Visualization of test results using Trace Viewer.
- Component testing with Playwright.
- Importance of maintaining a healthy work-life balance and the role of Playwright in achieving it.


## Nordic.js 2022 • Emma Twersky - An aria of ARIA

URL: [https://www.youtube.com/watch?v=OMdpiiOP1HI](https://www.youtube.com/watch?v=OMdpiiOP1HI)

- Intro: The speaker starts by admitting they know little about music, but mentions their excitement for NordicJS and the fact that they work at Spotify. They share a fun fact about themselves being an avid listener of classical music on Spotify.

- Topic Introduction: The speaker introduces the topic of Aria in web development, specifically focusing on how to make websites more accessible using Aria attributes. They mention that they will be talking about both "Arya" and "Aria", despite them being different terms.

- Arya as a Web Pattern: The speaker discusses the concept of Arya as it relates to web development, describing it as a pattern used for making websites more accessible. They mention that they will be using a graph to illustrate how various attributes and roles fit together in an Arya-based system.

- Accessibility and Web Development: The speaker talks about the importance of accessibility in web development, highlighting how it can greatly impact user experience for people with disabilities. They mention that they will be discussing how to make websites more accessible using custom components and Aria attributes.

- Discussion on Aria Attributes: The speaker discusses the use of Aria attributes in web development, explaining how they can help improve accessibility by adding dynamic components behind the scenes. They also mention that these attributes can be added programmatically, which can make them more efficient to implement.

- The Importance of Testing and Linting: The speaker emphasizes the importance of testing and linting when working with Aria attributes, highlighting how they can help developers catch errors and ensure that their code is compliant with accessibility standards. They also mention that they will be discussing how to use Arya in conjunction with other tools and frameworks.

- The Use of Landmark Roles: The speaker discusses the concept of landmark roles in web development, explaining how they can help improve the overall structure and organization of a website. They mention that there are certain roles that should not be used, as they may conflict with other elements on the page.

- The Importance of Labeling: The speaker discusses the importance of labeling in web development, highlighting how it can help improve accessibility by providing clear and concise information about various elements on a website. They also mention that there are certain best practices that developers should follow when creating labels for their websites.

- The Use of Aria Labels: The speaker discusses the use of Aria labels in web development, explaining how they can help improve accessibility by providing additional information about various elements on a website. They also mention that there are certain best practices that developers should follow when creating Aria labels for their websites.

- The Importance of Capitalization: The speaker discusses the importance of capitalization in web development, highlighting how it can help improve accessibility by ensuring that labels and other elements are properly formatted. They also mention that there are certain best practices that developers should follow when creating capitalized labels for their websites.

- The Use of Aria Checked: The speaker discusses the use of Aria checked in web development, explaining how it can help improve accessibility by providing additional information about various elements on a website. They also mention that there are certain best practices that developers should follow when creating Aria checked attributes for their websites.

- The Importance of Alt Text: The speaker discusses the importance of alt text in web development, highlighting how it can help improve accessibility by providing additional information about various images on a website. They also mention that there are certain best practices that developers should follow when creating alt text for their websites.

- Conclusion and Recommendations: The speaker concludes their talk by discussing the importance of using Aria attributes correctly and efficiently in web development. They provide several recommendations for developers who want to improve accessibility on their websites, including testing their code thoroughly and following best practices when creating labels, alt text, and other elements.


## Nordic.js 2022 • Liran Tal - Let me show you how React applications get hacked in the real-world

URL: [https://www.youtube.com/watch?v=xR9wjk0Fdb4](https://www.youtube.com/watch?v=xR9wjk0Fdb4)

- Introduction to conference
- Presenter's background as a Developer Advocate
- Focus on security in React applications
- Demonstration of a CLI tool for handling Docker containers
- Discussion on npm package security and supply chain issues
- Presentation of an example application with security vulnerabilities
- Explanation of the importance of input validation, output encoding, and secure coding practices
- Live coding demonstrations to illustrate these concepts
- Brief discussion of the use of GitHub CoPilot for code assistance
- Demonstration of a tool for scanning npm packages for security vulnerabilities
- Conclusion and call to action for developers to stay vigilant about security in their projects


## Nordic.js 2022 • Christian Landgren - How to save the world with JavaScript

URL: [https://www.youtube.com/watch?v=fmIFJxL8ub0](https://www.youtube.com/watch?v=fmIFJxL8ub0)

**Summary of Transcript (Markdown Style)**
- Importance of value and creating value in a changing world
- Experimenting with different approaches to problem solving, including open source, virtual drones, and digital twins
- The need for agile thinking and adaptability in the face of complex problems
- Understanding the power dynamics between technology companies and society
- Encouraging collaboration, communication, and learning from failure as key components of successful projects


## Nordic.js 2022 • Colin Ihrig - The State of Deno 2022

URL: [https://www.youtube.com/watch?v=iHjSJwDh8A4](https://www.youtube.com/watch?v=iHjSJwDh8A4)

- Introduction to Deno
    - Deno is a JavaScript runtime built on Rust.
    - It has a similar API and ecosystem to Node.js, but with performance improvements and modern features.
    - Deno was introduced in 2018 by Colin Ehrig, an engineer at Node.js Foundation.
- Growth of Deno
    - GitHub stars for Deno have been increasing since its introduction, catching up to Node.js in terms of popularity.
    - The growth of Deno can be attributed to its similarity with Node.js and its focus on performance improvements.
- Core Technologies behind Deno
    - Deno uses the V8 JavaScript engine for execution, which is also used by Node.js.
    - It has a Rust-based runtime called "Deno core" that provides a minimalistic JavaScript runtime environment.
    - The event loop and asynchronous I/O in Deno are similar to those in Node.js, but with some differences such as using the Tokyo library for TLS crypto instead of OpenSSL.
- Architecture of Deno
    - Deno is built using a collection of Rust crates that provide various functionalities like networking, file system access, and cryptography.
    - The Deno core crate provides the main runtime environment, while other crates like "Deno_ops" and "Deno_crypto" add additional functionality.
    - Deno also has a CLI tool called "Deno-cli" that can be used to download and run Deno applications.
- Dependency Management in Deno
    - Deno uses a package manager similar to npm, called "Denolian X".
    - It supports import maps for loading dependencies and has a global cache system for storing compiled modules.
    - Deno also provides a feature called "vendor production apps" which allows developers to pre-install their dependencies in the application package.
- Standard Library in Deno
    - Deno has its own standard library that includes implementations of common JavaScript APIs like FS and HTTP.
    - The standard library is maintained alongside the runtime and is updated with each new release.
- Release Schedule of Deno
    - Deno follows a weekly patch release schedule for bug fixes, along with monthly minor releases for new features and improvements.
- Features of Deno
    - Deno supports typescript out-of-the-box and has built-in tools like linters, formatters, and task runners.
    - It also has a permission system that allows developers to control access to filesystem resources and network connections.
    - Deno is compatible with many Node.js modules and provides support for testing and packaging applications.
- Integrated Tool Chain in Deno
    - Deno comes with an integrated tool chain that includes tools like linters, formatters, bundlers, and test runners.
    - It also has a built-in task runner called "Deno Task" which can be used to automate tasks like building and testing applications.
- Permission System in Deno
    - Deno has a permission system that allows developers to control access to resources like filesystem, network, and subprocesses.
    - This system provides granular control over resource access and helps prevent security vulnerabilities.
- Nodejs Compatibility Layer in Deno
    - Deno provides a compatibility layer for running Node.js modules on its platform.
    - This layer allows developers to use existing Node.js code without making any changes, but with some limitations due to differences between the two platforms.
- Performance Improvements in Deno
    - Deno has made significant performance improvements over time, especially in areas like startup time and memory usage.
    - It also provides a new HTTP server called "Flash" which offers better performance than previous servers like LLHTTP.
- Deno Deploy
    - Deno Deploy is a service that allows developers to deploy their applications on a global network of edge servers.
    - It currently supports 34 regions around the world and is growing continuously.
    - Deno Deploy provides features like automatic deployment, real-time monitoring, and easy scaling for applications.


## Nordic.js 2022 • Jessy Jordan - Investing in Open-Source

URL: [https://www.youtube.com/watch?v=J3miXGv4pPE](https://www.youtube.com/watch?v=J3miXGv4pPE)

- Open Source Adoption: 95% of digital products use open source components.
- Benefits of Open Source: Shared development, reduced development time, and cost savings.
- Open Source Integration: Businesses adopt open source models to build applications faster and more efficiently.
- Investing in Open Source: Many investment opportunities exist within the open source space.
- Case Study: Maraxa, a software engineering company, uses open source tools for data engineering projects.
- The Importance of Contributing to Open Source: Passionate about open tech, the speaker has contributed to several open source communities and projects.
- The Evolution of Open Source: From Netscape's browser product to Mozilla Foundation, open source has grown significantly over time.
- Successful Business Models with Open Source: Companies like Red Hat, MongoDB, and Confluent have built successful businesses around open source products.
- Contributing to Home Source: The speaker shares their personal experience of contributing to the open source community and how it positively impacted their career.
- Benefits of Open Source for Individuals and Businesses: Learning opportunities, collaboration with smart people, and building a strong network within the industry.


## Nordic.js 2022 • Jenn Creighton - Now and .then: Debugging Async JS

URL: [https://www.youtube.com/watch?v=KuD1SW-2lGA](https://www.youtube.com/watch?v=KuD1SW-2lGA)

- Intro: Jen Craden talks about her love for meeting new people and how it helps with social anxiety.
- Talk focus: Debugging async JavaScript code, particularly the common pitfall of avoiding writing async code right from the start.
- Key points:
    + Importance of understanding asynchronous operations in JavaScript.
    + Common mistakes made while debugging async code.
    + Use of console logs and debuggers for debugging purposes.
    + Understanding how promises work, especially in handling errors and rejections.
    + The concept of async/await and its impact on error handling and readability.
    + Tips for avoiding common mistakes while working with async code.
- Summary: Jen Craden's talk focuses on the challenges of debugging asynchronous JavaScript code, highlighting common pitfalls and providing practical tips for improving one's understanding and debugging skills in this area.


## Nordic.js 2022 • Charlie Gerard - Simple JStures can go a long way

URL: [https://www.youtube.com/watch?v=67BsEXb7oBQ](https://www.youtube.com/watch?v=67BsEXb7oBQ)

- Introduction: The speaker introduces themselves as a Developer Advocate at Stripe. They talk about their work in creating educational resources, maintaining open-source sample code for integrating with Stripe's products, and conducting research on technological topics.

- Main Topic: The main topic of the talk is about using machine learning to create gesture recognition systems. The speaker explains how they have built a system that can detect different gestures using an Arduino board equipped with an accelerometer and gyroscope sensor. They also discuss how this system can be connected to a web application via Bluetooth, allowing for real-time prediction of gestures.

- Key Points:
  - The speaker emphasizes the importance of experimenting with different kinds of interaction and encourages developers to think beyond traditional input methods such as keyboards and mice.
  - They explain how their gesture recognition system uses machine learning models trained on data collected from sensor readings. These models can be exported and imported between devices, making it easy to create custom gestures or train the system on new datasets.
  - The speaker demonstrates how their system can be integrated into web applications using JavaScript code that communicates with the Arduino board via Bluetooth. This allows for real-time prediction of gestures within the application.
  
- Demonstration: The speaker shows a live demo of their gesture recognition system in action, demonstrating how it can detect and classify different types of gestures such as waving and swiping. They also discuss some potential applications for this technology, such as creating fitness apps that track movement or building gesture-based payment systems.

- Conclusion: The speaker concludes their talk by expressing their enthusiasm for exploring new ways to interact with technology using machine learning and encouraging developers to think creatively about how they can apply these techniques in their own projects. They also mention some related technologies and projects that they have been working on, such as a Chrome extension that triggers IoT devices based on user gestures.


## Nordic.js 2022 • Matthias Le Brun - Leveraging (algebraic data) types to make your UI rock solid

URL: [https://www.youtube.com/watch?v=4co_az7ipMA](https://www.youtube.com/watch?v=4co_az7ipMA)

## Summary
- Introduction to Algebraic Data Types (ADTs) and their practical applications in app development.
- Explanation of how ADTs help manage complex states in applications, particularly when dealing with asynchronous data.
- Discussion on the importance of good documentation and clear communication in using ADTs effectively.
- Mention of a specific open-source library called "ReasonML" that provides a JavaScript syntax for working with typescript and algebraic data types.
- Emphasis on the need to simplify complex concepts and tools when teaching others how to use them, especially in the context of app development.


## Nordic.js 2022 • Tadeu Zagallo - JavaScript VMs 101

URL: [https://www.youtube.com/watch?v=RRcsiuL3H6Q](https://www.youtube.com/watch?v=RRcsiuL3H6Q)

- Introduction
    - Speaker's background and passion for programming languages and virtual machines.
    
- History of JavaScript VMs (VMS)
    - Brief history of JavaScript engines from KJS to modern V8, Chrome, and Firefox.
    - Discussion on the competition between different browsers and their respective performance improvements in JavaScript execution.

- Components of a Modern VMS
    - Overview of the four main tiers in a modern JavaScript VM: The Interpreter, Baseline compiler, DFG (Data Flow Graph) optimizing compiler, and FTL (Fastest Time to Long-term) high-performance compiler.
    
- How JavaScript Code Runs Faster
    - Explanation of the different steps involved in executing a simple JavaScript function, including parsing, lexical analysis, syntactic analysis, and runtime execution.
    - Discussion on how modern VMS use adaptive optimization techniques like inline caching, speculation, and adaptive recompilation to optimize code performance.
    
- Structure of Objects in JavaScript
    - Explanation of the structure used by JavaScript engines to store object properties, including the use of hidden classes or "structures".
    - Discussion on how these structures help improve performance by reducing expensive lookups and enabling fast property access.

- The Role of Compilers in VMS
    - Overview of how compilers work within a modern JavaScript VM to transform source code into optimized machine code for faster execution.
    
- Future Directions in VMS Development
    - Discussion on the ongoing competition between different browsers and their respective performance improvements, including benchmarking results and the impact of new compiler technologies like DFG and FTL.


## Nordic.js 2022 • Emma Bostian - Building High-Performing Cross-Cultural Teams

URL: [https://www.youtube.com/watch?v=KUuuI1PtpTw](https://www.youtube.com/watch?v=KUuuI1PtpTw)

- Culture map: a tool to decode different cultures and facilitate cross-cultural communication.
- Communication Styles: High context (Asian countries) vs Low context (US, UK).
- Evaluating Performance: constructive criticism varies by culture.
- Decision Making Process: consensual vs top-down.
- Trust: task-based vs relationship-based.
- Time Perception: monochronic (linear time) vs polychronic (flexible time).
- Scheduling: linear scheduling vs fluid scheduling.
- Understanding culture is key to managing multicultural teams effectively and improving cross-cultural collaboration.


## Nordic.js 2022 • Feross Aboukhadijeh - What's Really Going on Inside Your Node_Modules Folder

URL: [https://www.youtube.com/watch?v=rEojm0UJyj8](https://www.youtube.com/watch?v=rEojm0UJyj8)

- Open Source Modules and Supply Chain Attacks
    - Discussed the rise of supply chain attacks, particularly those targeting open source modules
    - Mentioned that many organizations are now using over 100 packages in their applications
    - Highlighted that dependency management has become a critical issue due to the growing number of third-party dependencies and the potential for malicious code to be introduced through these dependencies
    - Discussed how the rise of cloud services, APIs, and open source software has changed the way developers write software, leading to an increase in the use of third-party dependencies
- The Rise of Supply Chain Attacks
    - Defined supply chain attacks as cyber threats where attackers infiltrate a software vendor's network and introduce malicious code into their products or services
    - Mentioned that this type of attack can compromise the software vendor's reputation and lead to legal liabilities for the organization
- The Impact of Supply Chain Attacks on Open Source Modules
    - Discussed how the use of open source modules has changed over time, with developers now relying heavily on these modules to build their applications quickly and efficiently
    - Highlighted that there is a significant amount of trust placed in the maintainers of open source modules, as they are responsible for ensuring that the code is secure and free from vulnerabilities
- The Challenges of Securing Open Source Modules
    - Discussed how the rapid pace of software development can make it difficult to thoroughly review and audit open source modules before they are used in an application
    - Mentioned that many organizations struggle with quickly updating dependencies when new vulnerabilities are discovered, as this can introduce additional risks into their applications
- The Importance of Proactive Security Measures
    - Emphasized the importance of proactively monitoring and analyzing open source modules to identify potential security risks before they become a problem
    - Discussed how tools like Socket can help developers and security teams work together to identify and address security issues in their applications
- The Role of Developers in Securing Open Source Modules
    - Highlighted the importance of empowering developers to take an active role in securing their applications by providing them with the tools and resources they need to identify and address potential security risks
    - Discussed how modern development practices, such as DevOps and Cloud services, can help developers work more efficiently and securely when building their applications


## Nordic.js 2022 • Tobias Ahlin - An Animated Journey through the new Page Transition API

URL: [https://www.youtube.com/watch?v=608RhJEKYsY](https://www.youtube.com/watch?v=608RhJEKYsY)

- New Page Transition API: A draft CSS module that aims to make page transitions feel more intuitive and native.
- Drafted by a Design Engineer working on GitHub Rail App.
- The goal of the new Page Transition API is to work with both Single Page Applications (SPAs) and Multi-Page Applications (MPAs).
- It allows for smooth DOM changes and state animations in web applications.
- The API uses pseudoelements to capture before and after states, which are then animated using CSS.
- The speaker demonstrates a live demo of the new Page Transition API in action.
- The API is still in draft stage and the speaker encourages feedback and contributions via GitHub repositories.
- Future plans for the API include support for cross-origin quoting, which would allow for dynamic DOM changes across different websites.


## Nordic.js 2022 • Vitaly Friedman - Boosting Web Performance in 2022

URL: [https://www.youtube.com/watch?v=uqLl-Yew2o8](https://www.youtube.com/watch?v=uqLl-Yew2o8)

- Introduction to the talk and speaker's background
  - Speaker has been working in web performance for a long time
  - Talk is about recent developments and best practices in web performance optimization

- Importance of web performance optimization
  - Users expect fast websites, and slow websites can lead to lost business
  - Optimized websites have better search engine rankings and better user engagement

- Overview of the main points covered in the talk
  - Discussion of various tools and techniques for optimizing web performance
  - Examples of real-world projects and case studies

- Key takeaways from the talk
  - Use modern frameworks that are optimized for performance, like React and Vue.js
  - Optimize images by using formats like Avif and WebP, and use responsive images to reduce file size
  - Use lazy loading and preloading techniques to improve page load times
  - Prioritize critical CSS and JavaScript to ensure they are loaded first
  - Use service workers and caching strategies to improve offline performance and reduce network latency
  - Monitor web vitals using tools like Lighthouse and Chrome DevTools

- Discussion of specific techniques and tools
  - Use of the SSR vs CSR debate, and when to use each approach
  - Overview of the main points covered in the talk
    - Discussion of various tools and techniques for optimizing web performance
    - Examples of real-world projects and case studies

- Conclusion and final thoughts
  - Web performance optimization is an ongoing process, and it's important to stay up-to-date with new technologies and best practices
  - Optimizing your website can lead to better user engagement and improved search engine rankings


## Nordic.js 2022 • Lightning talk: Peter Lundberg - Stop Wasting Time (waiting on build tools)

URL: [https://www.youtube.com/watch?v=Fl0yI6PEKoQ](https://www.youtube.com/watch?v=Fl0yI6PEKoQ)

- Peter from Funnel IO introduces himself and talks about the importance of quick feedback loops, continuous improvement, and high performing teams.
- He highlights that response time to a user should ideally be less than 10 seconds.
- He emphasizes the importance of maintaining flow while working and how delays in development can lead to loss of attention and productivity.
- He talks about the challenges with large applications and long development cycles, and introduces eBuild as a solution that can significantly speed up the process.
- He mentions that using modern build tools like ES Build or SWC can help developers work faster and more efficiently.
- He shares an example of moving from Webpack to EBuild in a Node.js service, which resulted in significant improvements in performance and development speed.
- He also talks about the importance of hot module reloading and how it can make a huge difference in the development process by providing instant feedback on changes made.
- He encourages developers to continuously improve their workflows and tools, and suggests that modern build tool paradigms could be a valuable area for exploration.


## Nordic.js 2022 • Lightning talk: Benny Carlsson - Getting 800 people to make a website

URL: [https://www.youtube.com/watch?v=tWmvk_Dx95Q](https://www.youtube.com/watch?v=tWmvk_Dx95Q)

- Penny is a software developer from Gothenburg who started an open source website called "Oktoberfest" in 2018.
- The project aimed to be simple, without installation or complicated steps, and encouraged contributions from anyone.
- Contributors added various features like a countdown timer and even a snake game.
- Penny managed the repository, dealing with merge conflicts and closing issues.
- The website has received 397 stars on GitHub and has had 171 issues closed.
- It has over 800 contributors and has been fun to work on for Penny.
- The project also helped her grow professionally and personally, as well as fostering a sense of community.


## Nordic.js 2022 • Lightning talk: Eric Selin - Cache all the things for fast and simple backends

URL: [https://www.youtube.com/watch?v=VLAuJO9ivOk](https://www.youtube.com/watch?v=VLAuJO9ivOk)

- Eric talks about the challenges of caching dynamic content in HTTP requests.
- Two main problems are: 
  1. Cache invalidation - based on time or maximum age, it can lead to unnecessary cache invalidations.
  2. First request after cache invalidation always creates a round trip to the server, making it slow.
- He's currently working on an order management system with a simple server for data read/write.
- The problem is that he cannot use HTTP caching due to API rate limits and network latency issues.
- His solution is to write a new reverse proxy that solves both problems:
  1. Cache invalidation - using the purge function of a favorite reverse proxy (not specified).
  2. Warm cache - writing a new reverse proxy to handle this.
- The idea is to mirror the system and resolve conflicts in a complex way, but it's still a simple system at its core.
- The benefits are:
  1. Regular HTTP headers can be used for updates.
  2. Content is always fresh without invalidating everything.
- Eric suggests using platforms that offer the best for HTTP parts and encourages web developers to do so. He also emphasizes open-sourcing ideas and efforts.


## Nordic.js 2022 • Britta Evans - How to use the Screen Reader you already have in your pocket

URL: [https://www.youtube.com/watch?v=Ggx-qYxD5dI](https://www.youtube.com/watch?v=Ggx-qYxD5dI)

- Britta is a mobile developer, currently working on React Native.
- She emphasizes the importance of accessibility in app development beyond legal and ethical aspects.
- The primary focus of her talk is on screen reader accessibility.
- TalkBack is an Android built-in screen reader, and VoiceOver is for iOS.
- Navigation using a screen reader involves swiping left or right, double tapping the screen, and scrolling.
- In Android, three-finger gestures are used to switch apps, while in iOS, it's done with two rising tone sounds.
- Accessible elements are announced by their roles (button, header, etc.) and states (checked, unchecked, disabled).
- React Native has an accessible prop that can be used to group elements together.
- To enable screen readers on Android devices, go to the TalkBack settings; for iOS, go to Accessibility > VoiceOver.


## Nordic.js 2022 • Lightning talk: Pierre Petersson - One API that rules them all

URL: [https://www.youtube.com/watch?v=xEiqxTUVchk](https://www.youtube.com/watch?v=xEiqxTUVchk)

- Introductory remarks about the evolution of technology and data
- Discussion on the challenges of working with relational databases in today's world
- Highlighting the need for flexibility, agility, and speed in implementing requirements
- Introduction to MongoDB as a solution for working with modern, multistructured data
- Explanation of the Document Model in MongoDB and its benefits
- Comparison between object programming languages and relational databases
- Conclusion: The promise of a unified API in MongoDB for handling different use cases


## Nordic.js 2022 • Lightning talk: Anton Gunnarsson - CSS *is* awesome

URL: [https://www.youtube.com/watch?v=uo3px1L3H70](https://www.youtube.com/watch?v=uo3px1L3H70)

- Anthony from Empire Digital presents a lightning talk on CSS.
- Demonstrates how to use the HSL color function in CSS and apply it to form validation.
- Explains the concept of container queries, which allow styles to be applied based on the size of a parent element's content box.
- Shares an example of using a hash selector in CSS to interactively change the scale and opacity of a grid item.
- Discusses how to build a tab component entirely with CSS.
- Explains that counting child elements can be useful for certain styles, like dark mode toggles.
- Talks about container queries and their ability to style components based on the size of their parent's content box rather than the entire viewport.
- Shares an example of using a container query to apply a background color when the width of a container reaches a specific character count.
- Mentions that there are many creative uses for CSS, including building card components and other interactive elements.
- Encourages attendees to find resources like CodePen and GitHub to learn more about advanced CSS techniques.


## Nordic.js 2022 • Lightning talk: Ruy Adorno - Advancing the Node.js runtime via Working Groups

URL: [https://www.youtube.com/watch?v=csE5rFWj6IM](https://www.youtube.com/watch?v=csE5rFWj6IM)

- Introduce Rio Dornu, Brazilian Canadian Node.js collaborator and releaser
- Autonomous groups in Node.js called 'working groups' need at least 3 people to start
- Core working group is the hardest part with a steep learning curve
- Working groups can be project-based (like building a system) or strategic (planning for the future of Node.js)
- Release working group is responsible for deciding release schedules and handling CI failures
- Package maintenance working group helps maintain important packages in the ecosystem
- Tooling group focuses on improving developer support and runtime tools
- Argument parser, a recent big win from this group
- Participation encouraged through recurring meetings and joining the Node.js slack channel


## Nordic.js 2022 • Lightning talk: Abdul Ajetunmobi - JS Rules Everything Around me

URL: [https://www.youtube.com/watch?v=LWXRGuWodHc](https://www.youtube.com/watch?v=LWXRGuWodHc)

- Speaker's name: Abdul
- Occupation: Team bondage tooling and focus mainly on building tooling to make people use platform easier.
- Language preference: Swift, but also enjoys JavaScript
- Recent project example: Volume CLI typescript iOS push notification uploader (mostly JavaScript)
- Secret project: Can't disclose
- Familiar with Swift compiler and its nuances
- Feels freeing working with JavaScript compared to other languages
- Experience with yearly release cycles
- Disagrees with certain language points, but doesn't elaborate on what they are
- Closing statement: Focuses on making people's lives easier through technology, rather than being tied to a specific programming language.

Summary: Abdul is a tooling developer who enjoys working with both Swift and JavaScript. He recently worked on a project involving volume CLI typescript iOS push notification uploader (mostly JavaScript). He has experience with the nuances of the Swift compiler and feels more freedom when working with JavaScript. He also has experience with yearly release cycles and disagrees with certain language points, but doesn't elaborate further. His closing statement emphasizes his focus on making people's lives easier through technology rather than being tied to a specific programming language.



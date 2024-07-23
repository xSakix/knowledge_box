## Typing the not so secret to customisation ngTemplateOutlet | Stephen Cooper |  ng-conf 2023

URL: [https://www.youtube.com/watch?v=ELRCT7ooNCU](https://www.youtube.com/watch?v=ELRCT7ooNCU)

- NG Template Outlet is a powerful tool for creating customizable components.
- Define template using NG Template tag and options.
- Use template variables to extract information from context.
- ND Template Outlet Context Guard provides client customization.
- In 2019, issues with template typing were addressed.
- New features in Angular 16 include generic types for templates.
- Type checking is crucial for ensuring correct rendering and preventing errors.
- The speaker discussed a repo example of entertainment Outlets using NG Template.


## The Magic and Mystery of Angular Change Detection | Anthony Scardapane | ng-conf 2023

URL: [https://www.youtube.com/watch?v=68GpNWO-4QM](https://www.youtube.com/watch?v=68GpNWO-4QM)

- Understand change detection in Angular
- Process: create mode, update mode, and bootstrapping
- Change detection workflow: traverse component tree, check bindings, and update views
- Zone JS: patching browser APIs to notify Angular of changes
- Push component strategy: mark dirty components and run change detection implicitly
- Signal-based components: signal value changes trigger template reading and change detection
- Efficiency improvements with signal components
- Future RFCs: coexist with existing features, optimize change detection strategies


## Power Angular with WebStorm Workshop | Paul Everitt | ng-conf 2023

URL: [https://www.youtube.com/watch?v=3CLxk-vvPhI](https://www.youtube.com/watch?v=3CLxk-vvPhI)

1. User is working on an angular project and using webstorm IDE.
2. They create a component for their app called Heroes and add tests to it.
3. The user encounters various issues, fixes them, and commits the changes.
4. They use tools like prettier to clean up code and make refactors.
5. Webstorm IDE helps with autocomplete, syntax highlighting, and other features that improve productivity.
6. The user also uses a test runner to run their tests, ensuring everything works as intended.
7. Throughout the process, they share their experience and learnings on how webstorm helps them build better apps efficiently.- Importance of CSS integration and maintaining local history
- GitHub Copilot extension, IntelliJ IDEA features for git
- Difficulty in managing multiple branches and commits without proper token
- Stash vs. Shelf: Stash allows selective rollbacks while Shelf is more limited
- Preference for fine Explorer over other project organizers
- Microsoft's UI evolution: New UI received mixed reactions, but people found it easier to focus
- Idea of bringing back a feature in the form of an option or menu
- Double-clicking files to view differences in IDEs
- The speaker appreciates the context and ideas shared


## Setting up Enterprise Frontend for Success |  Alex Okrushko | ng-conf 2023

URL: [https://www.youtube.com/watch?v=K4IvRizYM1w](https://www.youtube.com/watch?v=K4IvRizYM1w)

- Speaker's background: Born in Ukraine, now working as a principal architect at Cisco and organizing Angular Toronto events.
- Frontend success: Define objective, focus on engineering ownership of code, team building, communication, monorepo, feature flags, trunk-based development, code style, automation testing, planning, and daily release.
- Tools: NX monorepo, feature Flags, GitHub flow/trunk-based development, TypeScript linting rules, automated formatting tools, documentation, design reviews, and Discord for support.
- Key takeaways: Communication is crucial in distributed teams; trunk-based development simplifies deployment and bug fixes; adopting a daily release cycle enables faster rollbacks and better focus on specific features.


## Road to Module Federation | Sumit Arora & Abdella Ali | ng-conf 2023

URL: [https://www.youtube.com/watch?v=1vGWnvSXO6Y](https://www.youtube.com/watch?v=1vGWnvSXO6Y)

1. Module Federation is a solution for separating concerns in applications and breaking them into smaller, independently deployable parts.
2. It provides better scalability, flexibility, and collaboration between teams by allowing each part to be maintained and released individually while still maintaining consistency across the application.
3. Benefits include clear developer experience, faster deployment process, improved testing, and easier internationalization handling.
4. Important aspects are clear communication, shared guidelines, and a well-defined structure with separate teams for backend, frontend, and infrastructure.
5. Focus on creating a consistent look and feel across the application while allowing individual creativity.
6. To implement Module Federation, consider using mono repositories, shared libraries, and a well-designed architecture that enforces consistency and alignment between teams.


## Reactive Patterns For Angular | Lara Newsom | ng-conf 2023

URL: [https://www.youtube.com/watch?v=Tr2AHKdtHVA](https://www.youtube.com/watch?v=Tr2AHKdtHVA)

- Utilize input Setters and emit events for data changes
- Pattern 1: Use Setters with filtering logic instead of ngOnChange
- Pattern 2: Cut middleman, use a router module to manage application state
- Pattern 3: Compose data and get consumers
- Combine patterns for a clear data flow throughout the app
- Orchestrate data flow for better maintainability and performance
- Use signal-based reactive programming for easier testing and maintenance


## Mobile Deployments for Web Developers | Cecelia Martinez | ng-conf 2023

URL: [https://www.youtube.com/watch?v=NcnjNiuutGs](https://www.youtube.com/watch?v=NcnjNiuutGs)

- Mobile deployment is complex due to differences between web and mobile platforms.
- Testing: Web testing occurs in specific environments while mobile apps require real devices, emulators, or cloud services for testing.
- Build process: Web development uses transpilers and bundlers, while mobile development involves compilation and code signing.
- App Store approval process: Apple's App Store has strict requirements, and rejections are often due to privacy issues, substandard UI, and app functionality.
- Updating apps: Live updates allow bug fixes without App Store approval, but require platform-specific tools or general mobile tools like CodeMagic, Bitrise, or Cloud Services.
- Tool selection: Consider platform-specific or multi-functional tools for your team's expertise and existing infrastructure.
- CI/CD platforms: Relevant options include App Flow (free), CircleCI, Jenkins, and custom solutions.
- QR code scanning: Scan the provided QR code to access a free whitepaper on automating mobile deployment processes.


## MFE Production Gotchas, and thing you should prepare | Bruce Zhang | ng-conf 2023

URL: [https://www.youtube.com/watch?v=oHVweuiqJwY](https://www.youtube.com/watch?v=oHVweuiqJwY)

- Transcript from a conference discusses learning microfrontend architecture (MFE) and its benefits.
- MFE breaks applications into smaller, reusable modules.
- Common issues mentioned include network errors, remote app handling, and circular dependencies.
- Tips for fixing issues with MFE: use ESM format, fix component undefined errors, and optimize performance using service workers, prefetching, and preloading.
- MFE improves application scalability, maintainability, and flexibility for distributed teams.


## Lightweight Architectures with Angular's Latest Innovations | Manfred Steyer | ng-conf 2023

URL: [https://www.youtube.com/watch?v=-PRgw9exL-8](https://www.youtube.com/watch?v=-PRgw9exL-8)

- Lightweight Angular Architecture: Standalone components, Sheriff (access restriction), and custom Standalone APIs.
- Mosaic approach: Use simple tools to compose complex applications.
- Key features: Lazy loading, routing parameter configuration, lazy routing, functional guards, asynchronous State Management, and signal-based communication.
- Benefits: Easily reach The Sweet Spot engineering through modularity and reusability.


## Introducing the Identity Guardians - Auth tokens in a flash! | Alisa Duncan | ng-conf 2023

URL: [https://www.youtube.com/watch?v=cj7vGdRjzOo](https://www.youtube.com/watch?v=cj7vGdRjzOo)

- Identity Guardians is an authentication and authorization solution for Angular applications.
- It uses OAuth 2.0 and OpenID Connect (OIDC) standards, with an extra identity layer.
- The OIDC certified library handles the OAuth handshake and authorization server process.
- Three tokens are returned: access token, ID token, and refresh token.
- Access token is used for authorization; Interceptor ensures it's not sent to unsafe origins.
- ID token contains standard identity information and can be used for authentication.
- Refresh token extends the life of the authentication by allowing the user to log in again without reauthorizing.
- Use industry-recognized standards, OAuth 2.0 and OIDC, and an OIDC certified library for maximum protection.


## Go Reactive with Angular Signals | Deborah Kurata | ng-conf 2023

URL: [https://www.youtube.com/watch?v=VhIkDQ1TWl8](https://www.youtube.com/watch?v=VhIkDQ1TWl8)

- Discussed using signals for reactivity in web applications.
- Signals provide a way to notify consumers when values change without needing to subscribe like observables.
- Computed signals create new signals based on other signals, allowing recomputation and memoization for improved performance.
- Interoperability between signal and RxJS is possible through observable interop features.
- Signal services can be injected using dependency injection in Angular to manage data flow.
- Event handlers can still be used alongside signals for user actions, but computed signals are more reactive.
- Computed state data can help avoid static page titles and replace event-based solutions with signal frameworks.


## Fun with Feature Flags | Brooke Avery & Preston Lamb | ng-conf 2023

URL: [https://www.youtube.com/watch?v=yGCSPtwTFdc](https://www.youtube.com/watch?v=yGCSPtwTFdc)

- Importance of feature flags in application development
- Feature flag types: service, guard directive, and flagging
- Benefits of feature flags include ease of control, testing, debugging, and continuous deployment
- Triangular pennant programming as an example of threesided flag implementation
- Using feature flags in Stewarts comic book store website for selectively displaying features based on user conditions


## Fine-Tuning Your Angular Workflow with Nx: Beyond the CLI | Juri Strumpflohner | ng-conf 2023

URL: [https://www.youtube.com/watch?v=g_al2o54JL0](https://www.youtube.com/watch?v=g_al2o54JL0)

1. Transcript overview: A conference talk about NX, a toolkit for web development.
2. NX improves developer experience with features like caching, optimized CI pipelines, and customizable workspaces.
3. NX console extension helps manage projects, generating files, and running tasks efficiently.
4. Annex workspace provides customization options and integration with other tools like Angular CLI and Webpack.
5. NGX is a package for configuring project settings in the NX workspace.
6. NXvite is an executor that builds specifically for Analog.js, making it easier to use.
7. Annex console extension helps with local generator compilation and publishing to npm registries.
8. Angular schematic and NX generators have compatibility issues due to slight differences in versions.
9. Plugin development and dedicated sections in documentation offer deeper insights into various tools.


## Delighting users with performant apps | Mike Hartington | ng-conf 2023

URL: [https://www.youtube.com/watch?v=SoEOk_q0_xI](https://www.youtube.com/watch?v=SoEOk_q0_xI)

- A team built a music app with various features.
- They faced issues with web performance, particularly with shadows and animations.
- A flip animation technique was used to improve performance.
- Craig developed a library to analyze album artwork for dominant colors.
- Web workers were introduced to handle image processing without affecting the main app's speed.
- The team successfully completed the project with an amazing UI, rich contextual information, and great performance.


## Custom RxJS Operators are Standing By! Act Now! | Chris Perko | ng-conf 2023

URL: [https://www.youtube.com/watch?v=dG1-WNDGqWA](https://www.youtube.com/watch?v=dG1-WNDGqWA)

- Introducing Chris Perco, a Senior Engineer at Hero Devs.
- Co-organizer of the Angular Community Meetup and frequent speaker.
- Custom operator in RxJS: simplifying complex code with reusability.
- Understanding operators as higher order functions.
- Creating custom operators for specific use cases.
- Example: Double operator, a simplified version of Map function.
- Pokemon themed app built using Angular Material and RxJS.
- Autocomplete component with debounce and throttle implementation.
- Marble testing: a way to visualize and test Observable behavior.
- Refactoring components for better readability and maintainability.
- Writing custom operators in a modular manner for easy maintenance.


## Craig's Angular/Rust Spectacular (brought to you by Rust-eze) | Craig Spence | ng-conf 2023

URL: [https://www.youtube.com/watch?v=GHZ3rKoP7xA](https://www.youtube.com/watch?v=GHZ3rKoP7xA)

- Craig presents a simulation project in Rust and Typescript languages.
- Rust offers better performance, memory management, and type safety than Typescript.
- He demonstrates an optimized simulation rendering using Rust's terminal renderer.
- To integrate Rust with the web browser, he suggests WebAssembly (Wasm) which is a binary code standard to run in the browser.
- The final step involves compiling the Rust code into Wasm and integrating it with the Typescript application.
- This results in significant performance improvements for the simulation rendering process, making Lightning McQueen happy.


## Clean Up Your Old Angular Apps! | Stephen Fluin | ng-conf 2023

URL: [https://www.youtube.com/watch?v=kXH7lVhut2E](https://www.youtube.com/watch?v=kXH7lVhut2E)

- Whirlwind tour of Angular updates
- Migration process with 32 steps for updating apps
- Use NPM version 16, avoid legacy peer depth issues
- Apply strictness and create new projects for better compatibility
- Utilize force to update dependencies carefully
- Run clean commits regularly
- Consider creating a brand new project for Angular v16
- Keep up with updates as they improve the ecosystem


## Build Trust with Your Users Workshop | Brian Love & Mike Ryan | ng-conf 2023

URL: [https://www.youtube.com/watch?v=lpua8gHQqgQ](https://www.youtube.com/watch?v=lpua8gHQqgQ)

- SLOs (Service Level Objectives) help define reliability for web apps by setting measurable targets.
- They provide a shared understanding and anchor conversation about service reliability.
- SLOs can be used to measure and improve the performance of web applications, acting as a common language between teams.
- Error budgets are utilized to quantify errors and allow for flexibility in error handling.
- Reliability Targets should be set based on real user experience data.
- Polaris is an AI-powered tool that helps measure web app performance, providing real-time insights into website performance and incident management. It also offers personalized site reliability advice using AI.


## Auxiliary Routes - the Ant-Man of Angular | Ankita Sood | ng-conf 2023

URL: [https://www.youtube.com/watch?v=ANgGbeAbvP0](https://www.youtube.com/watch?v=ANgGbeAbvP0)

- Discussed Angular and its sub-products in relation to Marvel characters.
- Introduced Backroute, a page routing solution for web apps.
- Explained how it works with Marvel examples.
- Focused on consistent user experience across components.
- Highlighted the use of skip location change to simplify navigation.
- Emphasized maintaining a clear URL structure.
- Discussed adding features like chat consistently.
- Aimed for a consistent user experience in detail panels and apps.


## Angular Across the Stack with Analog | Brandon Roberts | ng-conf 2023

URL: [https://www.youtube.com/watch?v=sbiONrVyHY4](https://www.youtube.com/watch?v=sbiONrVyHY4)

- Speaker introduces themselves and talks about various tools, frameworks, and projects they're involved in.
- Mentioned the importance of integration between different frameworks and tools to improve developer experience.
- Highlights Angular's strengths and its ecosystem, including server-side rendering, static site generation, API routing, and server data fetching.
- Talks about Angular's meta frameworks like NextJS, Remix, Astro, and Solid JS.
- Emphasizes the need for faster ways to build applications by using Angular's file-based routing and server-side rendering features.
- Discusses the importance of integrating APIs within frameworks.
- Introduces a new project called Analog, an open-source tool that aims to expand the Angular ecosystem and provide better integration across different platforms.
- Encourages contributions from the community, including sponsoring the project for further development.


## Thinking Outside the Box: Taking Your LOB Apps to the Next Level | Dan Wahlin | ng-conf 2023

URL: [https://www.youtube.com/watch?v=TZnMTICby5E](https://www.youtube.com/watch?v=TZnMTICby5E)

1. Discussed the importance of building apps that focus on organizational data, communication, and AI integration.
2. Demonstrated using web components to integrate search functionality for files across different platforms like Microsoft 365, Google Workspace, and OneDrive.
3. Showcased a live calling app using Twilio and Azure Communication Services.
4. Highlighted the need for prompt engineering in AI models and provided tips on creating effective prompts.
5. Mentioned the importance of maintaining security and privacy while working with AI systems.


## A Monorepo Can't Save You From Your Own Corporate Dysfunction | Isaac Mann | ng-conf 2023

URL: [https://www.youtube.com/watch?v=Ix63AaS41dU](https://www.youtube.com/watch?v=Ix63AaS41dU)

- Foreign speaker discusses different characters and their roles in a company:
  - Looney devs: Creative developers, but can cause issues with code organization.
  - Night high standard: Strict reviewers who focus on code quality.
  - Sneetches: Employees who value status and want to protect it at all costs.
- Monorepo Man: Uses NX, a tool for managing large codebases and improving team collaboration.
- Multiple repo strategy: Separate repositories for different teams or projects.
- Interpersonal issues: Important to address in order to create a productive work environment.
- Balance between technical solutions and interpersonal solutions to build a better team culture and improve app development.


## Do More using GitHub, AI, and VS Code | John Papa | ng-conf 2023

URL: [https://www.youtube.com/watch?v=u2A0gTew31Q](https://www.youtube.com/watch?v=u2A0gTew31Q)

- Transcript from a conference discusses the importance of collaboration and AI in software development.
- GitHub Copilot is highlighted as an efficient tool for developers.
- The transcript showcases various features such as chat, code completion, and refactoring assistance.
- The speaker emphasizes that AI in development will continue to evolve and improve efficiency.


## Angular Team Panel | ng-conf 2023

URL: [https://www.youtube.com/watch?v=RlQZxr2jxGc](https://www.youtube.com/watch?v=RlQZxr2jxGc)

- Discussions around Angular's future, features, and improvements.
- Focus on signal library, Standalone components, and performance optimizations.
- Mention of potential AI involvement in development tools.
- Emphasis on the importance of community contributions and documentation.
- Updates on Angular Material, CDK, and CLI developments.
- Discussions around server-side rendering, hydration, and module federation.
- Highlights on signal integration with streaming, SSR, and micro frontends.
- Importance of learning observables for easier onboarding.
- Need for better documentation and guidance on Angular's learning curve.


## Faster apps with Angular SSR | Mark Thompson & Jessica Janiuk | ng-conf 2023

URL: [https://www.youtube.com/watch?v=fMrUh9Nuw8A](https://www.youtube.com/watch?v=fMrUh9Nuw8A)

- Mark discusses Angular Hydration, a new feature in version 16.
- It helps with server-side rendering and improves performance by transferring state between servers.
- The process involves serialization, annotation, and DOM manipulation.
- There's incremental enablement for Hydration and HTTP caching.
- Lazy loading routes can be hydrated later.
- Developer Preview allows testing improvements in large contentful paint (LCP) by 45%.
- Future enhancements include deferred loading, internationalization support, and post-hydration cleanup.
- Version 16 provides the latest goodness for apps.


## Superpowers with Signals | Emma Twersky & Alex Rickabaugh |  ng-conf 2023

URL: [https://www.youtube.com/watch?v=cv8u6k1MTfE](https://www.youtube.com/watch?v=cv8u6k1MTfE)

- Foreign Music, favorite animal shrimp
- Talk about granularity in Angular applications
- Build a superhero character generator app using signal
- Create a superhero service for storing data and updating metrics
- Use computed signals for fine-grained updates
- Leverage change detection for performance benefits
- Discuss the importance of ownership and component logic
- Live coding session to demonstrate Angular application building


## Angular Keynote | Minko Gechev & Jeremy Elbourn | ng-conf 2023

URL: [https://www.youtube.com/watch?v=yUDhlR73qiU](https://www.youtube.com/watch?v=yUDhlR73qiU)

- NG Conf keynote focused on past, present and future of Angular.
- Performance improvements through optimized JavaScript virtual machine and fine-grained reactivity model (Signal).
- Hydration feature for faster client rendering.
- Server-side rendering and deployment options with Firebase integration.
- New features like deferred loading and directive composition API.
- Improved developer experience via better control flow syntax, improved router configuration, and auto import functionality.
- Continued efforts to make Angular more performant, easier to use, and compatible across different platforms.



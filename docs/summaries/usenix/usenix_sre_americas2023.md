## SREcon23 Americas - The Endgame of SRE

URL: [https://www.youtube.com/watch?v=BEs6j-BOl20](https://www.youtube.com/watch?v=BEs6j-BOl20)

- SRE Khan discussed the concept of end game SRE, focusing on building adaptive capacity within organizations.
- He emphasized that technical work is important but should not overshadow the need for understanding and shaping the sociotechnical systems in which we operate.
- He highlighted the importance of empathy, communication, and collaboration among team members to foster a culture of learning and improvement.
- SRE Khan shared stories from his experience working with various teams at Equinix, highlighting common challenges and opportunities for growth.
- He discussed the need for leaders to create safe spaces where team members can share their experiences and learn from one another.
- He emphasized that incidents are not just technical problems but also social issues that require a multidisciplinary approach to resolve.
- SRE Khan encouraged engineers to build strong relationships with product managers and other stakeholders to better understand customer needs and expectations.
- He warned against the dangers of siloed thinking and encouraged teams to share knowledge and resources across departments.
- Finally, he stressed the importance of continuous learning and improvement in the pursuit of building more resilient systems and organizations.


## SREcon23 Americas - SRE's Critical Role in the COVID-19 Pandemic Response in Government

URL: [https://www.youtube.com/watch?v=mSZThSjfLLw](https://www.youtube.com/watch?v=mSZThSjfLLw)

- Intro: The speakers discuss the US Digital Service's role in delivering better government services using technology, design, and user experience. They mention that they will talk about three projects: Vaccines.gov, Cova Test.gov, and SRE for pandemic response.

- Vaccines.gov: The speaker talks about how they built a tool to help people find vaccine appointment availability by creating a searchable map with information on available appointments. They mention that the project was launched in two months and had 1101 million sessions in 2021, serving 736 million users.

- Cova Test.gov: The speaker discusses how they built an online platform for ordering at-home COVID tests, which involved scaling up to distribute 500 million tests across the US. They highlight that the project was launched within two months and had 150 million addresses distributed across the country.

- SRE for Pandemic Response: The speaker talks about how they used Site Reliability Engineering (SRE) principles to ensure that government websites could handle high traffic loads during key events like presidential announcements or vaccine rollouts. They mention that they used a "soft launch" approach, where they would gradually release new features to users while monitoring performance and making adjustments as needed.

- Key Takeaways: Some key takeaways from the talk include the importance of collaboration across different organizations and government agencies, the need for clear communication and alignment around project goals, and the value of using SRE principles to ensure that digital services can scale effectively during times of high demand. Additionally, the speakers emphasize the importance of user-centered design and continuous improvement in delivering better government services.


## SREcon23 Americas - We're Still Down: A Metastable Failure Tale

URL: [https://www.youtube.com/watch?v=5ksTcC3uSUE](https://www.youtube.com/watch?v=5ksTcC3uSUE)

- Title: Metastable Failure - A Surprising Cascading Failure Story
- Presenter: Kyle, Senior Production Engineer at Meta
- The speaker describes a memorable incident in his career that he refers to as "metastable failure". He explains the term and contrasts it with cascading failure.
- A metastable failure is when a system enters a bad state due to a trigger cause, stays in this bad state even after the trigger is removed, and becomes unusable. The sustaining effect prevents the system from self-recovering.
- The speaker shares his experience of an incident that could have been a cascading failure but was actually a metastable failure. He explains how he and his team discovered this and what they did to recover from it.
- They found that the incident was caused by a combination of factors: a machine crashing, another machine going unhealthy while still running, and a health check affecting load shedding causing traffic oscillation.
- The speaker describes how they mitigated the incident by making some changes to their design and configuration. They made explicit choices to count machines as healthy only if they pass certain thresholds, spread traffic evenly across machines instead of overloading remaining ones, and adjusted weight for periodic automated recalculation.
- He also recommends understanding behavior systems and how they work, as well as spreading traffic across services to avoid overloading surviving services and causing cascading failures.


## SREcon23 Americas - Watering the Roots of Resilience: Learning from Failure with Decision Trees

URL: [https://www.youtube.com/watch?v=LZ-bW9kz3tA](https://www.youtube.com/watch?v=LZ-bW9kz3tA)

- Adaptive capacity is the ability of a system to prepare, plan, and absorb changes while recovering successfully from adverse conditions.
- Resilience is the ability to sustain adaptations in response to changing conditions.
- Complex software systems are sociotechnical, meaning they involve both human and machine components.
- The mental model represents the cognitive representation of an external reality.
- A system's resilience depends on its capacity to adapt failure.
- Conducting a chaos experiment, or simulating a scenario like conducting a disaster recovery test, can help reveal how a system behaves under pressure and identify areas for improvement.
- Security Chaos Engineering is about enabling organizations to gracefully respond to failures and adapt evolving conditions.
- A decision tree is a visual representation of different actions and events that can help map out potential outcomes and inform iterative design improvements.
- Conducting experiments, like injecting logging statements or changing system configurations, can provide valuable insights into how a system behaves under stress and identify areas for improvement.
- Continuously refining mental models and understanding of system realities is essential to sustaining resilience in complex software systems.


## SREcon23 Americas - Scaling Telemetry Systems with Streaming

URL: [https://www.youtube.com/watch?v=MyWu4FWJzpU](https://www.youtube.com/watch?v=MyWu4FWJzpU)

- Honeycomb's scaled telemetry system now factors 250,000 event per second and 25 million events per second
- Kafka is the beating heart of honeycomb's architecture
- The company has been using Apache Kafka for over four years to handle a large volume of debugging data
- Apache Kafka provides decoupling between state systems, allowing quick release of production every hour
- Honeycomb uses Kafka for ingesting and processing real-time analytics data
- Kafka's ordered log is crucial for maintaining consistency across the system
- The company has adopted a multi-copy strategy for ensuring availability and redundancy in their Kafka clusters
- Apache Pulsar, AWS Kinesis, and other streaming services have been considered as alternatives to Kafka
- Honeycomb uses Kafka's built-in replication feature to store data across multiple availability zones
- The company has optimized its Kafka cluster by using Zstandard compression and efficient hardware configurations
- Honeycomb monitors its Kafka clusters using a combination of custom dashboards, metrics, and trace data
- The company is constantly working on improving its Kafka infrastructure to handle increasing volumes of data and traffic


## SREcon23 Americas - Hacking the Pachyderm: Scaling Servers and People

URL: [https://www.youtube.com/watch?v=qmt0ouHFgwY](https://www.youtube.com/watch?v=qmt0ouHFgwY)

- Introduction to Hackaderm and its challenges
- Importance of making change easy
- Building a systemic approach to problem solving
- The role of resilience and adaptability in infrastructure
- Managing expectations with volunteer teams
- Importance of transparency, documentation, and approachability
- Using NixOS as the foundation for Hazaderm's infrastructure
- Embracing multicloud environments
- Leveraging Terraform for managing infrastructure
- The importance of good issue descriptions and clear backlogs
- Conclusion: Continuous learning and improvement in infrastructure management


## SREcon23 Americas - Logs Told Us It Was DNS, It Looked like DNS, It Had to Be DNS, It Wasn't DNS

URL: [https://www.youtube.com/watch?v=zOkou37L2Wo](https://www.youtube.com/watch?v=zOkou37L2Wo)

- Elijah Andrews of Datadog presented a talk about troubleshooting a DNS issue in Kubernetes.
- The issue was that rolling restarts of the metric service were causing errors and high error rates.
- The speaker discovered that the problem was not actually with DNS, but rather with the way that Kubernetes handles networking.
- In Kubernetes, each pod gets its own IP address, and when a pod is deleted, it can take some time for the network to update. This can cause issues if multiple pods are trying to connect to the same service at once.
- The speaker also discovered that there was a limit on the number of DNS requests that could be made per second, which was causing some requests to fail.
- To fix the issue, the speaker increased the memory allocated to the local DNS process and adjusted some networking settings.
- The speaker also used network traffic analysis tools to identify the root cause of the problem.
- In conclusion, the speaker emphasized the importance of understanding both the underlying technology and the specific use case when troubleshooting complex issues like this one.


## SREcon23 Americas - Epic Incidents of History: The 1979 NORAD Nuclear Near Miss

URL: [https://www.youtube.com/watch?v=yJWkUWCYx7g](https://www.youtube.com/watch?v=yJWkUWCYx7g)

- Intro: Nick Travalini, a Technical Customer Success Manager at Honeycomb.io, is presenting on the 1979 NORAD nuclear near miss during a conference.
- Main points:
    - The story begins with World War II and the development of analog computers to control various things like antiaircraft ballistic missile systems.
    - By the mid-1950s, digital technology started gaining traction, especially in military contexts such as command and control systems.
    - This led to the creation of the SAGE (Semi-Automatic Ground Environment) system, which was a large-scale computerized command and control communication system used for early warning systems during the Cold War era.
    - The story then moves towards the 1970s when the NORAD alliance was established to detect incoming enemy attacks across the continental north of America.
    - In October 1979, an incident occurred where a test data reel was mistakenly used instead of a tagged nuclear attack data reel in the Honeywell computer system at Cheyenne Mountain Complex. This led to a false alarm that a nuclear missile was incoming.
    - The near-miss event highlights the importance of understanding the sociotechnical systems we work with and questioning the data we receive from them.
- Conclusion:
    - Nick encourages everyone to think critically about the information they receive, especially when dealing with complex systems like distributed computer networks. He also points out that even though the NORAD system has improved since the 1979 incident, there's still room for improvement in terms of asking critical questions and engaging in thoughtful discussions around technology and its impact on society.


## SREcon23 Americas - Scaling Terraform at ThousandEyes

URL: [https://www.youtube.com/watch?v=rb_LZH60_QI](https://www.youtube.com/watch?v=rb_LZH60_QI)

- Terraform scaling issues:
  - Single-file deployment becomes unmanageable with increasing infrastructure complexity.
  - Drift between environments due to manual changes or different configurations in separate files.
  - Boilerplate code proliferation across multiple deployments.
- Solutions presented:
  - Terraform Stax: A method of splitting deployment into smaller, more manageable chunks called "stacks" that can be reused across deployments and environments.
  - Ginger templating: A syntax for using variables within HCL code to avoid hardcoding values and make the code more flexible and maintainable.
- Additional tools mentioned:
  - Atlantis: An open-source tool that automates Terraform workflows, including plan and apply operations, and integrates with GitHub pull requests for easy review and approval of infrastructure changes.



## SREcon23 Americas - OpenTelemetry Metrics 101

URL: [https://www.youtube.com/watch?v=4ZRV_LsaDoM](https://www.youtube.com/watch?v=4ZRV_LsaDoM)

- Intro: Welcome to the conference on Open Telemetry Metrics. The speaker introduces themselves and their role at New Relic, with a focus on working with end users and understanding community needs. They mention that they have been involved in tech support and are now part of the Open Telemetry engineering team.
  - Fun Fact: The speaker shares that they were born in Malaysia and have lived in the Pacific Northwest for about 20 years. They also mention that they have climbed Mount Hood, which is the highest point in Oregon.
- Metric Overview: The speaker begins by discussing the importance of metrics in observability and how they can help understand the health of an application. They explain that there are two main types of tools used for monitoring performance and data visualization: signal tracing (used to trace requests through a system) and logging (used to record events).
  - Useful Metrics: The speaker discusses the importance of choosing useful metrics, which can be influenced by factors such as the organization's goals, team needs, and specific use cases. They emphasize that different teams within an organization may have different requirements for metrics.
- Open Telemetry: The speaker provides a brief overview of Open Telemetry, describing it as an observability framework built on open standards. They explain that it was formed by merging two existing open source projects: Open Census and OpenTracing. Open Telemetry aims to standardize application instrumentation and provide a consistent way to collect and transmit telemetry data across different services.
  - Benefits of Open Telemetry: The speaker highlights some key benefits of using Open Telemetry, including freedom from vendor lock-in (users can choose their own backend or service provider), flexibility in terms of language support and tooling options, and the ability to easily integrate with existing systems and platforms.
- Metric Instrumentation and Usage: The speaker dives deeper into the topic of metric instrumentation, discussing how it works within an Open Telemetry architecture. They explain that there are different types of instruments available for use, each with its own set of properties and capabilities. They also provide examples of how these instruments can be used to measure various aspects of an application's performance, such as latency, traffic, error rates, and resource utilization.
  - Instrument Selection: The speaker emphasizes the importance of choosing the right instrument for a given use case, taking into consideration factors such as the type of data being collected, the desired level of granularity, and the specific needs of the organization or team using the metric. They also provide guidance on how to select the appropriate measurement interval and aggregation strategy based on these factors.
- Metric Concepts: The speaker briefly touches on some key concepts related to metrics, including dimensions, cardinality, and aggregation strategies. They explain that dimensions are used to add contextual information to a metric, while cardinality refers to the number of unique values being tracked within a dataset. They also discuss how different types of aggregation strategies can be used to analyze and visualize metric data in different ways.
- Open Telemetry Instrument Types and Use Cases: The The speaker provides an overview of the six main instrument types available in Open Telemetry, along with examples of how they might be used in practice. They also discuss the differences between synchronous and asynchronous instruments, as well as the importance of selecting the right measurement interval and aggregation strategy based on the specific needs of the organization or team using the metric.
- Recap and Next Steps: The speaker recaps the key points covered during their presentation, emphasizing the importance of understanding metrics and how they can be used to improve observability within an application. They also provide some guidance on next steps for those interested in learning more about Open Telemetry and related technologies, including exploring online resources, attending monthly discussion groups, and participating in community-driven projects and initiatives.
  - Reference Material: The speaker recommends consulting various reference materials and online resources to learn more about metrics and Open Telemetry, including the official Open Telemetry website, blog posts, tutorials, and case studies. They also acknowledge the contributions of their colleagues at New Relic, eBay, and other organizations who have helped shape the development of Open Telemetry and related technologies.


## SREcon23 Americas - Incident Commanders to Incident Analysts: How We Got Here

URL: [https://www.youtube.com/watch?v=VLGxGrNnWrY](https://www.youtube.com/watch?v=VLGxGrNnWrY)

    - Introducing Incident Life Cycle
        * Taylor Swift ticket example
        * Post-incident activities (chat, debrief, postmortem)
    - Importance of Learning from Incidents
        * Industry view of incidents as distinct events
        * Realizing that incidents are part of the life cycle of a system or organization
    - The Role of an Incident Commander and an Incident Analyst
        * Both roles require a strong understanding of incident management processes, tools, and communication techniques
        * Analyzing how these roles can be scaled within organizations
    - Best Practices for Incident Analysis
        * Emphasizing the importance of investigative work, collaboration, and maintaining a positive attitude during incident analysis
        * Recommending that analysts spread their work across different individuals to avoid burnout
        - Suggesting that incident review meetings should be inclusive and involve diverse perspectives from various teams within an organization
    - The Importance of Learning Incident Review Meetings
        * Encouraging curiosity and judgment in these meetings, as they help people understand the problem better and make informed decisions
        * Recognizing when a conversation has gone off track and how to pivot back on topic
        * Highlighting the importance of trust-building activities within incident review meetings
    - Conclusion
        * Emphasizing that everyone in an organization should be considered as potential friends, as they can help make work better and improve organizational culture
        * Encouraging people to seek out opportunities for learning and growth through incidents and incident reviews


## SREcon23 Americas - Handover Communications in Software Operations: Findings from the Field

URL: [https://www.youtube.com/watch?v=_zgOCkneV6I](https://www.youtube.com/watch?v=_zgOCkneV6I)

- Introduction: Chad Todd introduces himself and his background in the tech industry. He mentions working at Handover Communications, a company that focuses on researching and developing software for efficient communication during high-stakes situations.
  
- Background of Handover Communications: Chad explains that Handover Communications was initially founded to help operators communicate effectively during high-stress scenarios. The concept originated from NASA, where researchers observed the need for quick operator handovers in mission-critical situations.
  
- Evolution of Handover Communications: Over time, the concept of Handover Communications has evolved beyond verbal communication between two people and now includes digital written communication platforms like Slack and Microsoft Teams. This evolution has been driven by the increasing use of technology in various industries, as well as the need for more efficient and effective ways to share information during handovers.
  
- Research on Handover Communications: Chad discusses his research into Handover Communications, which involved conducting interviews with engineers who work in different departments within organizations. He found that there is a lot of inconsistency in how handovers are conducted across different departments, and this can lead to confusion and miscommunication among team members.
  
- Confidence and Handover Communications: Chad talks about the importance of confidence when it comes to conducting effective handovers. He explains that engineers who feel confident in their ability to communicate during handovers are more likely to provide accurate and helpful information to their colleagues. This, in turn, can help improve overall team performance and reduce the risk of errors or mistakes being made.
  
- Departmental Background and Handover Communications: Chad discusses how different departments within organizations have different needs when it comes to conducting handovers. He explains that some departments may require more detailed information during handovers, while others may only need brief updates on the current situation. This can make it challenging for engineers to determine what kind of information they should provide during handovers, and it can also lead to confusion among team members if different departments are using different methods of communication.
  
- Methodology: Chad explains that he used a combination of interviews, semistructured conversations, and data analysis to conduct his research into Handover Communications. He also discusses the concept of "joint activity," which refers to the idea that effective handovers require both parties involved to actively participate in the communication process.
  
- Themes: Chad identifies several key themes that emerged from his research, including organizational context, information exchange, preparedness, guidance, and closing loops. He explains how each of these themes is important for conducting effective handovers and provides examples of how they can be applied in real-world situations.
  
- Conclusion: Chad wraps up his presentation by discussing the importance of continuous improvement when it comes to Handover Communications. He emphasizes the need for organizations to continually evaluate their processes and procedures to ensure that they are providing the most effective and efficient means of communication for their employees. He also encourages engineers to take an active role in improving Handover Communications within their own organizations by sharing their insights and experiences with colleagues.
```


## SREcon23 Americas - On the Wings of SREs; J.P. Morgan's Journey into the Cloud

URL: [https://www.youtube.com/watch?v=4ozOaJ3jYvw](https://www.youtube.com/watch?v=4ozOaJ3jYvw)

    - Intro: Talk about SRE in JPMorgan Chase and how it's integral to the company's cloud transformation journey.
        - Speaker's background: Executive Director of SRE at JPMorgan Chase, previously worked with startups and public companies.
        - Company overview: Large financial services firm with over 57,000 technologists working across four main business lines (Corporate Investment Bank, Commercial Bank, Asset & Wealth Management, and Consumer & Community Banking).
    - Problem Statement: Discuss the challenges faced while moving services to the cloud and how SRE played a crucial role in addressing them.
        - Scale and Complexity: Large organizations with thousands of engineers spread across different teams and regions need to align their efforts towards common goals, which can be challenging due to diverse tooling requirements and infrastructure languages.
    - Solution Approach: Talk about the approach taken by JPMorgan Chase SRE team to address these challenges.
        - Resource Management: Cloud native environments offer infinite resources that can scale based on demand; however, this also presents a challenge of managing resource allocation efficiently without incurring unnecessary costs or performance issues.
        - Reliability Measurement: Implementing service level objectives (SLOs) is essential for measuring reliability and ensuring consistent performance across different services running in the cloud.
        - Infrastructure Management: Establishing relationships between teams and regions is crucial to streamlining infrastructure management processes and ensuring that everyone works towards a common goal.
    - Conclusion: Discuss how establishing trust and empathy within the organization has helped the SRE team scale their efforts and address complex challenges effectively.
        - Trust Building: Building strong relationships with different teams across the organization helps establish credibility and understanding of each other's concerns, leading to better collaboration and problem-solving.
        - Empathy: Understanding the pain points faced by other teams allows SRE professionals to provide more effective solutions and support, ultimately contributing to the overall success of the cloud transformation initiative.


## SREcon23 Americas - SRE in Transition: From Startup to Established Business

URL: [https://www.youtube.com/watch?v=00FYcBDqalk](https://www.youtube.com/watch?v=00FYcBDqalk)

    - Introduces herself and her role at Datadog.
    - Focuses on the role of SRE in a startup environment, emphasizing the need for sustainability and scalability.
    - Discusses the concept of "debt" in a startup company, including technical debt (e.g., lack of API boundaries) and operational debt (e.g., manual operations).
    - Explains that as a startup grows, it becomes more important to address these debts and transition from a "dead default" mindset to one focused on sustainability and scalability.
    - Highlights the importance of building self-sustaining solutions and natural champions within an organization to drive cultural change.
    - Introduces the concept of an SRE toolkit, which includes tools like incident review, postmortem analysis, production readiness reviews, and limited call Ops expectations.
    - Emphasizes that these tools should be used incrementally and thoughtfully, rather than as rigid rituals.
    - Discusses the importance of celebrating small wins and maintaining a positive attitude when driving large-scale change within an organization.


## SREcon23 Americas - Lessons Learned from 7 Years of Running Developer Platforms

URL: [https://www.youtube.com/watch?v=vL9KNyVIdH4](https://www.youtube.com/watch?v=vL9KNyVIdH4)

- Platform Engineering Lessons Learned
  - Adopt Product Mindset
    - Incorporate product management, marketing, and user research into platform development
    
  - Learning the Art of Product Management
    - Conduct market research, competitive analysis, and user research to understand customer needs
    
  - Documentation is Key
    - Create a centralized knowledge base for users to find answers quickly
    
  - Platform as an Internal Development Portal
    - Provide a platform that enables developers to build, test, and deploy applications efficiently
    
  - Measure Impact with Metrics
    - Track key performance indicators (KPIs) to measure the success of your platform
    
  - Start with a Simple, Integrated Solution
    - Begin by implementing a pre-integrated platform that can be easily customized and scaled as needed
    
  - Build Golden Paths
    - Create an ideal end-to-end process for developers to follow when building and deploying applications
    
  - Brand and Market Your Platform
    - Develop a strong brand identity and marketing strategy to promote your platform within the organization

Note: The provided transcript was a video recording from a conference. I have summarized the key points of the talk based on the content of the speech without any additional context or information outside of the transcript.


## SREcon23 Americas - Cognitive Apprenticeship in Practice with Alert Triage Hour of Power

URL: [https://www.youtube.com/watch?v=c8uRsQPeg_g](https://www.youtube.com/watch?v=c8uRsQPeg_g)

- Introduction: The speaker introduces themselves and the topic of their talk, which is on SRE onboarding and how they implemented a learning program called "Alert Triage Power Hour" at their company.
- Learning Goals: The speaker emphasizes that the goal of their program is to teach new engineers about the system they're working on, how to triage alerts, and how to think systematically.
- Cognitive Apprenticeship: The speaker explains that they use a cognitive apprenticeship model in their program, which involves modeling expert behavior, coaching, scaffolding, and reflection.
- Modeling Expert Behavior: In this part of the program, experienced engineers demonstrate how to investigate alerts and triage them effectively.
- Coaching: The speaker explains that they provide one-on-one coaching to help new engineers understand the concepts being taught in the program.
- Scaffolding: The speaker discusses how they use scaffolding techniques to help new engineers learn, such as providing hints or guidance when needed.
- Reflection: The speaker emphasizes the importance of reflection in their program, as it allows new engineers to think about what they've learned and apply it to real-world situations.
- Alert Triage Power Hour: The speaker describes how their program works, including a regular meeting where engineers discuss alerts and learn from each other.
- Impact: The speaker discusses the impact of their program on their company, including improved incident response times, better understanding of the system, and reduced alert fatigue.
- Expansion: The speaker explains how their program has expanded beyond engineering to include product design and product management teams.
- Conclusion: The speaker thanks the audience for their attention and encourages them to implement similar programs in their own organizations.


## SREcon23 Americas - Building a Diverse SRE Talent Pipeline

URL: [https://www.youtube.com/watch?v=Em4k8hM0urY](https://www.youtube.com/watch?v=Em4k8hM0urY)

- SRE (Site Reliability Engineering) is a growing field in tech industry.
- Google built Field SRE teams around 20 years ago to maintain system reliability and diversity.
- Major League Hacking (MLH) partners with organizations like Google to build diverse talent pipelines through fellowship programs.
- MLH Fellowships provide real-world experience, mentorship, and networking opportunities for early career developers.
- The SRE field is not well known among traditional software engineering roles, leading to a lack of established hiring pipelines.
- Building diverse Talent Pipelines requires creating communal learning environments, incorporating skills-based training, and providing dedicated mentorship.
- MLH Fellowships offer structured training programs, hands-on projects, and networking events to help early career developers launch successful careers in SRE.
- Mentors play a crucial role in supporting program participants by offering guidance, technical support, and career advice.
- Diverse Talent Pipelines can help address the challenges faced by organizations when hiring tech industry professionals, particularly those in the field of SRE.
- By building diverse talent pipelines, organizations can create more inclusive and equitable work environments for all employees.


## SREcon23 Americas - The Best SREs Seem to Be the Ones without an SRE Title—And What We Can Do

URL: [https://www.youtube.com/watch?v=rvMbb8ET1o0](https://www.youtube.com/watch?v=rvMbb8ET1o0)

- SRE future: Platform competence, AI orchestration
    - Platform competence: 5 areas (capacity, risk, cost, observability/monitoring, tooling)
        + Capacity: Manage resources efficiently, scale applications effectively
        + Risk: Assess and mitigate potential risks to the platform
        + Cost: Optimize costs associated with running the platform
        + Observability/Monitoring: Implement robust monitoring and alerting systems
        + Tooling: Select and use appropriate tools for managing the platform
    - AI orchestration: Utilizing AI to automate tasks, improve decision-making, and enhance platform competence
- SRE role evolution: Aligning ICS managers with SRE teams
    - Role changes: ICS managers need to understand coding, review code, and manage projects effectively
        + Coding: Ability to write and review code is essential for effective collaboration between ICS managers and SREs
        + Reviewing code: Managers must be able to evaluate code quality and make informed decisions about its implementation
        - Managing projects: Effective project management is crucial for ensuring that initiatives are completed on time and within budget
- Practical solutions for complex incidents
    - Platform competence: Developing a strong foundation in the 5 areas of platform competence can help SREs better handle complex incidents
    - Tooling: Using appropriate tools to manage people, processes, and technology can improve incident response times and overall efficiency
        + Observability platforms: These platforms provide valuable insights into system performance and help identify potential issues before they become major problems
- Future trends in the industry
    - Generative AI: As AI technologies continue to evolve, there may be opportunities for SREs to leverage these tools to automate tasks and improve decision-making processes
        + Full-stack AI orchestration: This concept involves using AI to manage all aspects of the platform, from resource allocation to incident response
    - Platform competence: The ability to understand and effectively manage all aspects of the platform will become increasingly important as organizations continue to adopt new technologies and services


## SREcon23 Americas - Confessions of an SRE Manager

URL: [https://www.youtube.com/watch?v=y1rzaL_mOpM](https://www.youtube.com/watch?v=y1rzaL_mOpM)

- The speaker describes their 20-year-old management experience and how they have learned since then.
- They mention being a surfer, owning old Japanese cars, and starting their career in the culinary industry.
- The speaker talks about their current job role and responsibilities as a manager and a leader.
- They discuss the importance of understanding the difference between management and leadership roles in an organization.
- The speaker highlights the challenges they have faced while managing teams and how they have learned to handle them effectively.
- They talk about the need for transparency, communication, and trust within a team.
- The speaker emphasizes the importance of one-on-one meetings with each team member and maintaining open lines of communication.
- They discuss the challenges of dealing with unplanned work and how to manage it effectively.
- The speaker talks about the importance of diversity and inclusion in the workplace and how it can help create a better working environment for everyone.
- They mention their experience working with different organizations, both large and small, and how they have learned from each one.
- The speaker discusses the challenges of managing remote teams and the importance of building strong relationships with team members.
- They talk about the importance of continuous learning and self-improvement in order to become a better manager and leader.
- The speaker highlights some of the key lessons they have learned throughout their career, including the importance of feedback, communication, and trust.
- They discuss the challenges of managing teams with different personalities and how to handle them effectively.
- The speaker talks about the importance of setting clear goals and expectations for team members and how it can help improve overall performance.
- They mention some of the books they have read on management and leadership, including "Radical Candor" by Kim Scott.
- The speaker emphasizes the importance of staying organized and maintaining a healthy work-life balance as a manager.


## SREcon23 Americas - Exploring Disconnects between Reliability Practitioners and Management

URL: [https://www.youtube.com/watch?v=2JHmRTZ5nN4](https://www.youtube.com/watch?v=2JHmRTZ5nN4)

- **Introduction**
    - Kurt and Leo introduce themselves as coanalysts of the SRE Report 2023.
    - They invite the audience to scan a code, read an ungated page, or refer to their report based on a survey conducted in summer 2022. The report is available for purchase.
- **Key Findings from the SRE Report**
    - Kurt and Leo present key findings from their research:
        - A large majority of respondents reported that they felt their organizations prioritized revenue over brand/product efficiency.
        - There was a significant difference in how individual contributors (ICs) and executives perceived the value of AI Ops.
        - ICs tended to place more emphasis on low-value tasks, while executives focused on high-value tasks.
    - They note that these findings highlight an "us versus them" mentality between ICs and executives.
    - They emphasize the importance of understanding the underlying theme driving these perceptions and encourage open communication between different roles within organizations.
- **Role Play: Successful vs. Unsuccessful Conversations**
    - Kurt and Leo demonstrate how successful conversations can be facilitated by role-playing scenarios where one person (either an IC or executive) is attempting to communicate a problem or challenge to another person in the same role. They highlight the importance of understanding different perspectives and using clear, concise language when discussing issues.
    - They suggest that successful conversations often involve active listening, empathy, and a willingness to consider alternative viewpoints.
- **The Impact of Tool Sprawl on Business Value**
    - Kurt and Leo discuss the negative effects of tool sprawl on business value and how it can lead to confusion and inefficiencies within organizations. They suggest that companies should carefully evaluate their technology stack and prioritize tools that provide the most value to their employees and customers.
- **The Importance of Metrics in Measuring Success**
    - Kurt and Leo emphasize the importance of using metrics to measure success in SRE initiatives. They recommend selecting key performance indicators (KPIs) that align with business objectives and regularly monitoring these metrics to ensure that progress is being made towards achieving desired outcomes.
- **The Role of Culture in Promoting Successful SRE Practices**
    - Kurt and Leo discuss the importance of fostering a culture that supports successful SRE practices within organizations. They suggest that companies should encourage open communication, collaboration, and continuous learning among their employees to promote innovation and improve overall performance.
- **Conclusion**
    - Kurt and Leo conclude their presentation by reiterating the key findings from their research and emphasizing the importance of understanding the underlying themes driving perceptions within organizations. They encourage attendees to consider how they can apply these insights to improve their own SRE practices and promote better communication between different roles within their companies.


## SREcon23 Americas - Beacon: Intelligent Latency-Aware and Load Shedding Service Routing

URL: [https://www.youtube.com/watch?v=SfzAkxRY0Zg](https://www.youtube.com/watch?v=SfzAkxRY0Zg)

- Jason Griggs from Morgan Stanley's platform performance team discusses the Beacon service, a load shedding and intelligent routing system for trading services.
- Beacon was created to handle large amounts of data traffic during high-volume events like Ticketmaster's Taylor Swift presale concert.
- The architecture consists of three main components: Beacon Router, Beacon Status Server, and Replication Latency Server.
- The system uses a service infrastructure that can route queries directly to primary or replicated databases based on latency thresholds.
- Beacon 10 architecture focused on primary database replication, while Beacon 20 introduced domain-specific databases for better performance and resilience.
- The latest iteration of the system, Beacon 30, has been in production since November 2019 and has handled over 200 million calls per day.


## SREcon23 Americas - Resiliency Practices in Managing CDN (Content Delivery Network)

URL: [https://www.youtube.com/watch?v=0G5BolDEwvw](https://www.youtube.com/watch?v=0G5BolDEwvw)

- Yash Ive Netflix 2015 working on the CDN
- Focused on Open Connect, a program built by Netflix in 2011 to scale video delivery
- OCA (Open Connect Appliance) is a server that serves Netflix traffic and is deployed closer to the end user for better quality experience
- Push Architecture: Take content, encode it, and push servers when a play button is clicked
- IX (Internet Exchange): Sites where ISPs connect with each other and exchange traffic
- OCA has two deployment types: Edge Deployment (directly connected to an ISP) and ISP Deployment (within the network of an ISP)
- Global deployment map includes 230 million members and 18,000+ deployed OCAs
- Infrastructure Failure: Understands running running whole network and how to handle different types of failures
- Software Failure: Understands how to manage service like small object fill using backbone dedicated redundant capacity
- FTL (Faster Light) API Traffic: Manages API performance by terminating closest IX location and connecting directly with AWS
- DNS Service: Hosts domain names and manages service like small object JavaScript file image, text etc.
- Live Service: Top OCA platform launched recently that supports live streaming of events
- Three types of failure exercises: Stack Failure Test, Overload Test, and Client Overload Test
- Netflix's client design architecture is designed to handle day-to-day outages and is resilient to infrastructure failures
- Adaptive Streaming Engine: Designed to work with the Netflix client and understand internet weather and server go time
- Resiliency Exercise: Aimed at understanding how the system behaves during failures and ensuring that it can react quickly and efficiently
- Testing: Conducted using real-world data, including Twitter's average bitrate for 4K TV shows, to ensure that the system is capable of providing high-quality video even under high traffic conditions
- Stack Overload Test: A scenario where a sudden increase in traffic causes one or more stacks to fail, and the remaining stacks must handle the increased load
- Client Overload Test: A test conducted to understand how the client behaves when it is overwhelmed with traffic
- CDN (Content Delivery Network) Design: Focused on ensuring that the system can handle sudden increases in traffic and recover from failures gracefully
- Live Event Service Launch: A new service launched by Netflix that supports live streaming of events, such as Chris Rock's special
- Embrace Failure: The philosophy behind the resilience exercises is to embrace failure and learn from it, rather than avoiding it.


## SREcon23 Americas - Why This Stuff Is Hard

URL: [https://www.youtube.com/watch?v=Tm_qS5raszw](https://www.youtube.com/watch?v=Tm_qS5raszw)

Title: Adaptive Universe: The Complexity of Systems and Incidents
---
- The Adaptive Universe model proposes that a system is always pushed towards its capacity, making it difficult to build extra buffer time.
- Change is never-ending in the Adaptive Universe, which makes life harder for SREs as they must constantly adapt to new changes.
- Code freeze is often seen as an antipattern, but can be useful when used judiciously to control change within a system.
- The complexity of a system increases over time due to the accumulation of past decisions and changes.
- Control theory concepts like Ashby's Law of Requisite Variety can be adapted to help manage complexity in systems.
- Incident organization often involves adding more complexity to a system, which makes it harder to maintain and operate effectively.
- Communication and coordination are essential for solving problems in distributed systems and incident response teams.
- Effective communication requires constant repair of misunderstandings and is a difficult problem to solve, especially in remote or hybrid work environments.
- Coordinating people to work together effectively within constraints is crucial for managing complexity in systems and operations.
- The key takeaway from this talk is that treating skill involved in operation work as a first-class thing and learning to navigate constraints effectively can help manage the complexity of systems and incidents.


## SREcon23 Americas - Turning an Incident Report into a Design Issue with TLA+

URL: [https://www.youtube.com/watch?v=_-kthTsZ2qU](https://www.youtube.com/watch?v=_-kthTsZ2qU)

- The speaker discusses a 28-day incident involving Microsoft Azure, where a mitigation feature was reverted.
- The issue revolved around latency and how it broke the system's performance.
- The speaker explains that they used TLA+ to model the Cosmos DB system and identify the underlying design problem.
- They emphasize the importance of understanding the system at a detailed level, including its components and their interactions.
- The speaker shares insights into how the incident was caused by an optimization feature in Azure Cosmos DB, which led to latency issues and ultimately broke the system's performance.
- They explain that the problem could have been avoided if the session token had been correctly shared between different parts of the system.
- The speaker highlights the importance of using TLA+ for modeling systems and identifying potential problems before they occur.
- They also discuss how the tooling ecosystem can help in understanding complex systems like Azure Cosmos DB.
- The speaker provides a demonstration of how they used TLA+ to model the system and identify the underlying design problem.
- They emphasize that their approach allowed them to think beyond their initial assumptions and investigate the issue more thoroughly.


## SREcon23 Americas - The Making of an Ultra Low Latency Trading System with Go and Java

URL: [https://www.youtube.com/watch?v=6SXd0cNRVN8](https://www.youtube.com/watch?v=6SXd0cNRVN8)

- Coinbase Exchange Overview
  - Two main parts: OMS and matching engine
  - Market data feeds are critical for trading firms and market makers
  - Trading system architecture is simplified into a single state machine, with input and output events driving the system forward
  - Stateful trading system design allows for deterministic behavior and easy replication of the system
- Legacy System Improvements
  - Identify bottlenecks in the legacy system by tracing request paths end-to-end
  - Optimize performance by reducing unnecessary overhead, such as GC pauses or excessive CPU usage
  - Use profiling tools to monitor internal system behavior and identify potential bottlenecks
  - Implement load balancing strategies to distribute traffic evenly across multiple servers
  - Tune database queries for optimal performance
- New System Design Considerations
  - Prioritize deterministic behavior and consistency in the new system design
  - Use a high-performance messaging library, like Aeron, for reliable and fast communication between components
  - Implement a consistent naming convention and data structure format across all components of the system
  - Optimize memory usage by using efficient data structures and minimizing unnecessary allocations
  - Utilize hardware acceleration where possible to offload CPU-intensive tasks from the main processing cores
  - Use containerization and orchestration tools, like Docker and Kubernetes, to manage and deploy the new system components


## SREcon23 Americas - Seeing the Invisible: Two Years at Wikipedia with W3C's Network Error Logging

URL: [https://www.youtube.com/watch?v=p2uod64GSm8](https://www.youtube.com/watch?v=p2uod64GSm8)

- Speaker introduces himself as Chris, a Boston area SRE with 5 years at Wikimedia and 10 years at Google.
- He talks about the nonprofit open source project called Wikimedia, which is one of the top 10 websites.
- The project includes Wikipedia, Wiktionary, Wikimedia Commons, etc., and has a big emphasis on user requests.
- Chris mentions that they use an open-source solution whenever possible and have a mix of bare metal, rented cages, and cloud providers for their infrastructure.
- He explains that the critical mission is to serve data quickly and efficiently, especially when it comes to handling PII (Personally Identifiable Information).
- The Dallas data center has around 1800 physical servers with a two-core site. They also have a CDN Edge caching mini-site populated around the world.
- Chris talks about their infrastructure setup, including an app server that looks like a classic LAMP stack and how they use Kubernetes for container orchestration.
- He mentions that they are moving towards running top Kubernetes clusters instead of bare metal servers.
- They have a task tracker and Grafana for monitoring purposes.
- Chris discusses their CDN perspective, which is straightforward and easy to understand.
- The Dallas data center has a 200,000 RPS peak, but they can handle larger traffic surges when needed.
- He shares an interesting anecdote about a traffic surge due to the death of a celebrity and how their system handled it without any outages.
- Chris talks about their app server architecture and how they are working on running top Kubernetes clusters instead of bare metal servers.
- They use Grafana for monitoring purposes, and he shares some metrics like daily peak traffic and how they handle unexpected traffic surges.
- He mentions that they have three independent IP Transit providers and that their site is connected to at least one local internet peering point.
- Chris talks about the importance of understanding the internet as a forest with many entities, large and small, competing or cooperating with each other.
- He discusses the concept of a "forest" as an analogy for the internet and how it can be difficult to navigate at times.
- He mentions that he dislikes the cloud metaphor when discussing the internet and believes that the "forest" analogy is more appropriate.
- Chris talks about the importance of understanding the underlying network infrastructure and how it affects user experience.
- He explains that they have a Grafana dashboard for monitoring purposes, which helps them identify issues quickly.
- He discusses their use of Nell (Network Error Logging Library) to help diagnose and fix network issues.
- Chris talks about the importance of understanding the end-to-end user experience and how it can be affected by various factors such as ISP outages or DDoS attacks.
- He mentions that they have a paging system in place to alert them when there are significant issues affecting user experience.
- Chris discusses their use of Nell (Network Error Logging Library) to help diagnose and fix network issues.
- He talks about the importance of understanding the end-to-end user experience and how it can be affected by various factors such as ISP outages or DDoS attacks.
- He mentions that they have a paging system in place to alert them when there are significant issues affecting user experience.
- Chris shares some case studies about incidents he has worked on, including one involving a PDF download service and another involving a CDN issue.
- He talks about the importance of understanding the underlying network infrastructure and how it affects user experience.
- He mentions that they have a Grafana dashboard for monitoring purposes, which helps them identify issues quickly.



## SREcon23 Americas - Avoiding Cachepocalypse in the Land of the Monolith

URL: [https://www.youtube.com/watch?v=ry3EAPO8yRA](https://www.youtube.com/watch?v=ry3EAPO8yRA)

- Duolingo's large Python monolith faced a 'cash apocalypse' due to a bug lurking in the memcache cluster
- The bug caused duplicate connections, leading to an overload of the system and preventing it from scaling horizontally
- A team was formed to address the issue, but ownership was unclear as different teams owned different parts of the codebase
- Engineers held meetings to discuss the problem and establish a clear plan of action
- Potential solutions included introducing a memcache proxy tier or spinning up a secondary memcache cluster
- The team pursued both approaches simultaneously, with one team working on a potential fix for the bug and another team scaling the system by adding capacity
- After several weeks, the team identified that the issue was due to a non-backwards compatible change in a third-party library
- They fixed the issue by removing the cache read module from the staging environment and reintroducing it carefully
- The team also established better communication channels and created a blameless culture to encourage open discussion about problems and solutions
- They emphasized the importance of investing in fast, safe debugging practices and leveraging local development environments for testing changes before deploying them to production.
- By addressing the issue urgently and working together as a team, Duolingo was able to resolve the 'cash apocalypse' and ensure that their language learning app continued to provide high-quality service to its users.


## SREcon23 Americas - Incident Archaeology: Extracting Value from Paperwork and Narratives

URL: [https://www.youtube.com/watch?v=k4UaDDkLOhw](https://www.youtube.com/watch?v=k4UaDDkLOhw)

    - Introduces self as a Staff Engineer and Incident Manager at Spotify
    - Talks about the importance of psychological safety in resolving incidents quickly
    - Discusses the process of incident management, including filing tickets, updating statuses, estimating impacts, and coordinating post-incident reviews
    - Mentions the value of communication during stressful events like incidents, which can lead to accountability, cost reduction, and better collaboration
    - Shares their experience with a concept called "Incident Archeology" that involves digging into historical incident data to learn from past mistakes
    - Explains the difference between depth (in-depth analysis) and breadth (overview of an issue) in incident investigation
    - Talks about the challenges of extracting value from incident artifacts, including the difficulty of remembering details over time
    - Discusses the importance of data collection and analysis in understanding incident trends and patterns
    - Shares their learnings from a study they conducted on incident management at Spotify, which involved analyzing Jira tickets to identify common issues and trends
    - Mentions the challenges of correlating incident data with other variables, such as uptime or environment changes
    - Talks about the importance of starting and ending incident investigations accurately, as well as the challenges of detecting impacts during an incident
    - Shares their findings from a survey they conducted on developer sentiment around incidents, which revealed that many incidents are related to local changes in the environment
    - Encourages attendees to try conducting their own incident studies and share their findings with others


## SREcon23 Americas - An Organizational Response to Incidents: Designing for Smooth Coordination

URL: [https://www.youtube.com/watch?v=m6NlJFsfimw](https://www.youtube.com/watch?v=m6NlJFsfimw)

- Cognitive work in incident response: The speaker emphasizes the importance of cognitive work in incident response, which includes perception, reasoning, and attention. They discuss how these skills are essential for understanding and responding to incidents quickly and accurately.
   - Perception involves receiving cues from the environment and interpreting them to understand the situation at hand.
   - Reasoning is about making sense of the information received and inferring likely scenarios.
   - Attention refers to focusing on goal priorities in a given context, which helps in making decisions and taking action.
- Coordination cost: The speaker talks about coordination cost, which refers to the effort and resources required for people to work together effectively. They discuss how this cost can be minimized by improving communication, sharing knowledge, and reducing cognitive load.
   - Communication is essential for coordinating efforts among team members. It involves exchanging information, asking questions, and providing updates on progress.
   - Knowledge sharing helps in reducing the time required to understand a situation and respond to it effectively. It also allows people to learn from each other's experiences and avoid making similar mistakes.
   - Reducing cognitive load involves simplifying tasks, providing clear instructions, and eliminating distractions that can hinder decision-making and problem-solving abilities.
- Incident response strategies: The speaker discusses various incident response strategies that can help organizations improve their coordination capabilities. These include adaptive choreography, which involves adjusting the way people work together based on changing conditions; escalation principles, which involve identifying key stakeholders and involving them in decision-making processes; and task delegation, which involves assigning specific tasks to individuals who have the necessary skills and expertise.
   - Adaptive choreography involves adapting the way people work together based on changing conditions. This can help organizations respond more quickly and effectively to incidents by allowing them to adjust their strategies as needed.
   - Escalation principles involve identifying key stakeholders and involving them in decision-making processes. This can help organizations ensure that important decisions are made by individuals who have the necessary expertise and experience.
   - Task delegation involves assigning specific tasks to individuals who have the necessary skills and expertise. This can help organizations improve their coordination capabilities by ensuring that each person is working on tasks that they are best suited for.
- Common ground: The speaker emphasizes the importance of common ground in improving coordination among team members. They discuss how shared knowledge, beliefs, and assumptions can help people understand each other's perspectives and work together more effectively.
   - Shared knowledge helps individuals understand each other's expertise and experience, which can lead to better decision-making and problem-solving abilities.
   - Shared beliefs and assumptions help individuals understand each other's values and priorities, which can lead to better communication and collaboration.
   - Common ground also involves understanding the context in which people are working, such as organizational culture, goals, and constraints. This can help individuals work together more effectively by ensuring that they are aligned with each other's objectives and expectations.
- Antipatterns: The speaker discusses various antipatterns that can hinder coordination among team members. These include shaming and blaming, which involve attributing failures to individual mistakes rather than systemic issues; retraining, which involves trying to fix problems by teaching people new skills or techniques; and service-oriented mindsets, which involve focusing on providing services to others rather than working together as a team.
   - Shaming and blaming can lead to feelings of guilt, shame, and fear among individuals who are being criticized, which can hinder their ability to learn from mistakes and improve their performance.
   - Retraining can be ineffective if it does not address the underlying causes of problems or provide individuals with the necessary skills and knowledge to succeed.
   - Service-oriented mindsets can lead to siloed thinking and poor collaboration, which can hinder an organization's ability to respond effectively to incidents.
- Incident response analysis: The speaker discusses the importance of incident response analysis in improving coordination among team members. They suggest looking closely at post-incident reports and other sources of information to identify patterns and trends that can help organizations learn from their experiences and avoid making similar mistakes in the future.
   - Post-incident reports can provide valuable insights into how incidents were handled, what worked well, and what could be improved.
   - Other sources of information, such as customer feedback, social media posts, and news articles, can also provide useful insights into how organizations are perceived by others and how they can improve their performance.
- Conclusion: The speaker concludes by emphasizing the importance of good leadership and followership in improving coordination among team members. They suggest focusing on goal priorities, sharing knowledge and expertise, and working together as a


## SREcon23 Americas - Building an APM with OpenTelemetry and OpenSource

URL: [https://www.youtube.com/watch?v=LO9zlDVPAWg](https://www.youtube.com/watch?v=LO9zlDVPAWg)

- Introduced himself and his role in the Grafana Labs
- Explained the problem that OpenTelemetry is trying to solve: lack of standardization for vendor-specific observability tools
- Highlighted the features of OpenTelemetry, including:
  - Standard API/SDK specification
  - Semantic convention for consistent metadata across metrics, logs, and traces
  - Auto instrumentation agents that focus on business logic while capturing relevant data
  - Middleware collectors and collector pipelines
- Mentioned the community behind OpenTelemetry and its rapid growth in contributions
- Defined APM (Application Performance Monitoring) from his perspective: a system that easily instruments applications, provides high-quality dashboards, and helps monitor and understand application performance
- Demonstrated an example of how to use OpenTelemetry for APM using a demo application written in multiple languages
- Discussed the current state of OpenTelemetry, including its early journey and plans for future development
- Encouraged the audience to get involved with OpenTelemetry by contributing to the project and adopting the standardized conventions


## SREcon23 Americas - Measuring Real-Life Latency of the Internet: A Netflix Story

URL: [https://www.youtube.com/watch?v=wXWFrKiJXHE](https://www.youtube.com/watch?v=wXWFrKiJXHE)

- Tierra Ortiz introduces herself and her gaming background.
- She explains the concept of latency in online video games and how it affects the gameplay experience.
- She shares her journey from a small town to working at Netflix as a Senior CDN Reliability Engineer.
- She highlights the importance of managing a content delivery network (CDN) for providing a great viewing experience on Netflix.
- She explains the three main metrics that define quality experience: bit rate, rebuffers, and play delay.
- She emphasizes the role of latency in video streaming and how it can impact user experience.
- She introduces the concept of T-digest data structure for collecting and analyzing data without sacrificing accuracy or memory usage.
- She explains how T-digest helps in extracting insights from large datasets, such as round trip time (RTT) data.
- She demonstrates how T-digest can be used to analyze RTT data by looking at p50, p75, and p99 values.
- She discusses the importance of using T-digest for capacity planning and anomaly detection in a CDN environment.
- She concludes her talk by sharing a personal story about how she experienced latency while traveling and how it affected her experience.


## SREcon23 Americas - Founder/CTO Perspectives: The Future of Distributed Tracing

URL: [https://www.youtube.com/watch?v=V8ydf2mkUgY](https://www.youtube.com/watch?v=V8ydf2mkUgY)

- Distributed tracing is a powerful tool for understanding software systems
- It's especially useful in microservices architectures where services communicate over networks
- OpenTelemetry is an open standard for instrumenting software and collecting telemetry data
- Honeycomb, the company that Megan Johnson co-founded, provides a platform for analyzing distributed traces
- There are challenges involved with implementing distributed tracing, such as naming conventions and classification of data
- Autoinstrumentation is important for making distributed tracing easier to use, but it's not always perfect
- The future of observability may involve more integration between different tools and technologies


## SREcon23 Americas - Lightning Talks

URL: [https://www.youtube.com/watch?v=w0mQbZ7IIvw](https://www.youtube.com/watch?v=w0mQbZ7IIvw)

- Introductions and welcome remarks by the conference chair
    - Fatima, lightning talk chair
    - Karaoke event
- Lightning Talk Presentations
    - John Ben: Cryptography in TLS
        - Symmetric key encryption with public key cryptography
        - Securely sharing symmetric keys using public key cryptography
        - Authenticating two-party communication using symmetric key cryptography
        - Confidentiality, integrity, and non-repudiation in message exchange
    - Miz I: SRE and Cryptography
        - TLS used for secure data transmission
        - Public key encryption and symmetric key encryption
        - Establishing a secure channel using Diffie-Helman Key Exchange
        - Mutual authentication using TLS 1.2
        - Securely establishing a shared secret key
    - Siri Noble: SLOs for Developer Experience
        - Understanding user experience through logging and metrics
        - Defining success and failure based on error rates, latency, and request counts
        - Creating SLI dashboards to monitor application performance
        - Using automatrix to automatically generate Prometheus queries and alerts
    - Robert: Observability in DevOps Culture
        - The importance of blameless culture in incident handling
        - Transparency and collaboration among teams
        - Using tools like Grafana, Prometheus, and Slack for incident management
- Lightning Talk Presentations (continued)
    - Last Nine: Observability with Golang and Prometheus
        - Metrics collection using golang libraries
        - Histograms, counters, and gauges as observability tools
        - Labeling metrics for better visibility and analysis
        - Customizing labels based on route parameters and hostnames
    - Lisa: SRE Interviewing Horror Stories
        - Experiences with technical interviews in the SRE field
        - Common interview questions and challenges
        - Tips for preparing for an SRE interview
- Closing remarks and Q&A session


## SREcon23 Americas - Human Observability of Incident Response

URL: [https://www.youtube.com/watch?v=bduQmnF-z4Q](https://www.youtube.com/watch?v=bduQmnF-z4Q)

- Introduced himself as a musician and technologist who has worked in various roles including building data centers.
- Mentioned his journey into SRE and his involvement with the LFI (Learning From Incidents) community.
- Discussed how he combined his love for music and technology to help people learn.
- Talked about a joint activity involving music and improvisation, which was inspired by Pauline Olivieros' book "Deep Listening".
- Emphasized the importance of attention awareness in SRE and incident response, drawing parallels with musical concepts like adaptive choreography.
- Introduced the concept of an Incident Response Trio, highlighting its flexibility and adaptability to different situations.
- Discussed how improvisation is a key part of incident handling and how it can be practiced through various methods such as tabletop exercises and process rehearsals.
- Shared insights from a study on Arctic rescuers that emphasized the importance of collaboration and improvisation in extreme environments.
- Talked about the role of mental models in music, incident response, and software development.
- Discussed how the concept of listening goes beyond just hearing and involves actively engaging with one's surroundings.
- Highlighted the importance of building common ground when dealing with incidents and the need to include diverse perspectives.
- Mentioned the use of RSS feeds, dedicated channels, and email updates as ways to keep everyone informed about ongoing incidents.
- Shared his experience of using a "Rubber Duck Debugging" technique, where he would explain his problem out loud to a rubber duck toy, which helped him think through the issue more clearly.
- Talked about his experience with the Indonesian percussion orchestra Gamelan and how their iterative approach to building music can be applied to incident response.
- Discussed the concept of "wheel expertise" where different team members are given a chance to showcase their knowledge and expertise through a spinning wheel mechanism.
- Highlighted the importance of remote collaboration and how it can help teams learn from each other and build stronger relationships.
- Emphasized the need for continuous learning and improvement in SRE and incident response, using examples from his own experiences.


## SREcon23 Americas - Far from the Shallows: The Value of Deeper Incident Analysis

URL: [https://www.youtube.com/watch?v=qqsq81u7WD8](https://www.youtube.com/watch?v=qqsq81u7WD8)

- Started with a focus on the importance of depth in understanding incidents and systems.
- Discussed the limitations of shallow metrics, such as MTTR, which can be misleading or oversimplified.
- Mentioned severity as another concept that is often subjective and can vary between organizations.
- Talked about incident stories and how they provide a more holistic view of incidents than just numbers or metrics.
- Discussed the importance of understanding the context and history behind incidents, including cultural factors and human behavior.
- Highlighted the value of collaboration and communication among different teams and stakeholders in order to effectively respond to and learn from incidents.
- Emphasized the need for continuous learning and improvement, both individually and organizationally.
- Introduced the concept of a "safety boundary" as a way to help organizations better manage risk and prevent incidents.
- Talked about the importance of adaptability and resilience in systems, particularly in the face of changing operating conditions or unexpected events.
- Discussed the role of human judgment and decision-making in incident response and highlighted the importance of understanding how these factors can influence outcomes.
- Mentioned the concept of a "near miss" as an important learning opportunity that is often overlooked or underestimated.
- Highlighted the value of sharing knowledge and experiences across different teams and organizations, both for learning purposes and to build a stronger sense of community around incident response.


## SREcon23 Americas - How SRE Makes Electric Vehicles

URL: [https://www.youtube.com/watch?v=SuxOUwfC1BM](https://www.youtube.com/watch?v=SuxOUwfC1BM)

- The speaker, Adam Shake, is a Senior SRE Manager at Rivian.
- He started his career as an application developer and has experience in various roles such as tier 2 support, senior SRE manager, etc.
- At the time of the conference, he was working on applying SRE principles to manufacturing EVs but believes these principles can be applied outside of the EV world.
- The speaker mentioned that he had a background in various technologies and has knowledge of tier 2 support.
- He described his current role at Rivian as a Senior SRE Manager, where he manages a team responsible for implementing SRE practices in manufacturing.
- Adam talked about how he entered the field of SRE after attending his first conference and shared his experience of working with different companies such as insurance companies and ad tech companies.
- He mentioned that he was hired at Rivian to build an SRE practice within their manufacturing environment, leveraging principles from his previous experiences.
- Adam highlighted the similarities between software development and manufacturing, particularly in terms of code writing and observability.
- He described how he faced challenges while implementing SRE practices in a legacy manufacturing environment but managed to overcome them by using automation, CI/CD infrastructure, and code observability.
- The speaker emphasized the importance of building relationships with different stakeholders such as system owners, engineers, and network platform teams.
- He discussed how they were able to improve their production line efficiency by implementing SRE practices and highlighted the role of automation in making this possible.
- Adam also talked about the challenges he faced while working with legacy devices and the importance of maintaining a good relationship with vendors.
- The speaker mentioned that they have been able to reduce the time it takes to provision new devices from nine hours to one hour by using automation, APIs, containerization, and custom tooling.
- He highlighted the importance of observability in manufacturing environments and how they were able to build a centralized platform using Prometheus and Grafana.
- Adam talked about the challenges he faced while working with legacy firmware on devices and the importance of working closely with vendors to address these issues.
- The speaker mentioned that they are currently working on implementing Edge Computing in their manufacturing environment and have plans to use Kubernetes to manage their production line devices.
- He discussed the importance of collecting data from devices for tracing and APM purposes and how they plan to leverage microservices architecture for dynamic workload shifts.
- Adam also talked about the importance of maintaining customer focus while implementing SRE practices in manufacturing environments.
- The speaker shared a personal story about his journey into the field of SRE and how he was inspired by attending his first conference.
- He emphasized the importance of building relationships with different stakeholders within an organization and highlighted the role of leadership in driving innovation.
- Adam talked about his vision for the future of manufacturing environments, which includes implementing software-defined factories and leveraging automation to reduce human intervention.
- The speaker also discussed the importance of having a balanced team that combines both technical expertise and supervisory skills.
- He mentioned that he would love to see a future where humans are primarily involved in overseeing the manufacturing process while automation takes care of the rest.


## SREcon23 Americas - Warding against the Dark Arts: Crafting a Defense Strategy against Botnet DDoS

URL: [https://www.youtube.com/watch?v=r783WkJvSAE](https://www.youtube.com/watch?v=r783WkJvSAE)

- DDoS attacks are becoming more frequent and larger in volume.
- The speaker discusses their experience working on DDoS defense strategy, including incremental improvements made over the years.
- They mention that there's a lot of opportunity to create a homegrown observability service for hardening DDoS solutions.
- The use case discussed involves custom systems and end solutions, leading to technical debt.
- The speaker talks about the importance of understanding offline states during attacks and how different services may be affected differently.
- They discuss various types of attackers and their motivations, including Anonymous attacks, extortion attempts, and law enforcement involvement.
- The speaker emphasizes the need for a service hardening approach that includes graceful degradation to protect constrained resources during an attack.
- They mention that DDoS situations can look like system overload or internal failures, making it difficult to distinguish between them.
- The importance of incident management and leadership training is highlighted in handling sudden increases in resource constraint.
- The speaker discusses different types of attacks, including those with a protracted duration, social engineering elements, and those that aim to distract key personnel.
- They talk about the need for a service hardening approach that includes graceful degradation applied in a decentralized manner.
- The importance of informed higher layer decisions is emphasized, which can help reduce cost per request during an attack.
- The speaker discusses the role of priority queues and how they play a significant role in handling sudden increases in resource constraint.
- They talk about the importance of having spare capacity behind single service entry points and how common enrichment features can be used to improve system performance.
- The speaker emphasizes that DDoS situations often lead to damage even when defense is deployed effectively, making it necessary to invest more in service hardening.
- They discuss the concept of graceful degradation and how it can help reduce the impact of an attack on user experience.
- The importance of having a diverse and distributed attack mindset is emphasized, as it helps identify potential threats that may not be immediately apparent.
- The speaker talks about the challenges involved in identifying and blocking DDoS requests, especially when they come from legitimate sources or are disguised as normal traffic.
- They discuss the importance of having a robust filtering process to detect and block bot traffic effectively.
- The speaker highlights the need for automation in detecting and responding to bot traffic, as manual processes can be time-consuming and inefficient.
- They talk about the challenges involved in identifying and blocking DDoS requests that come from multiple sources or have a diverse range of characteristics.
- The importance of having a centralized incident management service is emphasized, as it helps ensure that all teams are aware of ongoing issues and can respond appropriately.
- The speaker discusses the concept of metastable failures and how they can make it difficult to identify and respond to DDoS attacks effectively.
- They talk about the importance of having a holistic view of system performance and how it can help identify potential issues before they become critical.
- The speaker emphasizes the need for engineers to have a good understanding of how different services interact with each other, as this can help them identify potential weaknesses in the system.
- They discuss the importance of having a robust logging and metric system in place to help identify potential DDoS attacks early on.
- The speaker talks about the challenges involved in identifying and blocking DDoS requests that come from multiple sources or have a diverse range of characteristics.
- They emphasize the need for engineers to have a good understanding of how different services interact with each other, as this can help them identify potential weaknesses in the system.
- The speaker discusses the concept of graceful degradation and how it can help protect services during an attack by allowing them to continue functioning at a reduced capacity.
- They talk about the importance of having a robust logging and metric system in place to help identify potential DDoS attacks early on.
- The speaker emphasizes the need for engineers to have a good understanding of how different services interact with each other, as this can help them identify potential weaknesses in the system.
- They discuss the concept of graceful degradation and how it can help protect services during an attack by allowing them to continue functioning at a reduced capacity.
- The speaker talks about the importance of having a robust logging and metric system in place to help identify potential DDoS attacks early on.
- The speaker emphasizes the need for engineers to have a good understanding of how different services interact with each other, as this can help them identify potential weaknesses in the system.
- They discuss the concept of graceful degradation and how it can help protect services during an attack by allowing them to continue functioning at a reduced capacity.
- The speaker talks


## SREcon23 Americas - The Revolution Will Not Be Terraformed: SRE and the Anarchist Style

URL: [https://www.youtube.com/watch?v=iW-DeWsHfYI](https://www.youtube.com/watch?v=iW-DeWsHfYI)

- Introduction: Speaker introduces himself and his role in a company that deals with observability and open Telemetry.
- Sociotechnical Movement: The speaker talks about the sociotechnical movement, which includes Agile, DevOps, and SRE. He mentions how these movements have influenced the way organizations work and emphasizes the importance of people working together in a collaborative manner.
- Agile Manifesto: The speaker discusses the Agile Manifesto, which focuses on individual interaction, working software, customer collaboration, and responding to change. He highlights that while agile emphasizes cultural values, it has been commodified by companies like Accenture and Deloitte, turning it into a product that can be bought and sold.
- DevOps: The speaker moves on to discuss the DevOps movement, which focuses on local decision-making and ownership. He mentions how books like "The Phoenix Project" have helped popularize this movement.
- SRE (Site Reliability Engineering): The speaker talks about the SRE movement, which is a reaction to both Agile and DevOps. It emphasizes the importance of both cultural values and technical practices, focusing on reliability, automation, and service-level objectives.
- Mutual Aid: The speaker introduces the concept of mutual aid, which is based on the idea that individuals can work together to achieve common goals. He uses examples from nature, such as ants working together in a colony, to illustrate this point.
- SRE and Mutual Aid: The speaker connects the concepts of SRE and mutual aid, suggesting that SRE practices can help build mutual confidence and individual initiative within organizations.
- Murray Bookchin: The speaker discusses the work of philosopher and ecologist Murray Bookchin, who wrote about social ecology and communalism. He suggests that these ideas can be applied to the world of technology and software development.
- Power Relationships: The speaker talks about the power dynamics within organizations and society, suggesting that successful movements like Agile, DevOps, and SRE rely on a sense of community and shared goals.
- Conclusion: The speaker concludes by emphasizing the importance of distributed power and authority within organizations, suggesting that leaders should create structures and regulations that allow individuals to work together safely and securely.


## SREcon23 Americas - Implementing SRE in a Regulated Environment

URL: [https://www.youtube.com/watch?v=vhtLYEunaQk](https://www.youtube.com/watch?v=vhtLYEunaQk)

Here is the summary:
- DBS Bank, a leading bank in Southeast Asia, implements SRE (Site Reliability Engineering) to enhance their resiliency and reliability.
- Myths busted include believing that every disruption has a single root cause and thinking that breaking an app will reveal unknown issues.
- The importance of continuous learning, collaboration, and data-driven insights is emphasized throughout the presentation.
- DBS Bank's SRE journey began in 2020 with the transformation of applications and people.
- Chaos engineering and incident response frameworks have been implemented to uncover unknown issues and improve system resilience.
- The use of in-house tools like Raccoon, an automated testing tool, has helped DBS Bank identify and fix issues more efficiently.
- SRE principles, such as postmortem analysis, are used to learn from incidents and make strategic improvements.
- A focus on multivariant disruptions and the use of error budgets help DBS Bank manage risk and improve system performance.
- The Beyond framework is a learning tool that encourages continuous improvement and knowledge sharing within the organization.
- DBS SRE accreditation program educates technical staff on best practices for implementing SRE principles.
- Moving to the cloud has allowed DBS Bank to build a more robust infrastructure and promote sustainability.


## SREcon23 Americas - Financial Resiliency Engineering: Taming Cloud Costs

URL: [https://www.youtube.com/watch?v=GOJO4weqwXs](https://www.youtube.com/watch?v=GOJO4weqwXs)

- Introduction to Financial Resiliency Engineering
- Overview of Shopify's tech stack and infrastructure
- Importance of cost efficiency in maintaining a sustainable business model
- Case study: Reducing Cloud Infrastructure Cost at Shopify
  - Problem: High monthly spend on Google Cloud Platform (GCP)
  - Solution: Implement cost optimization strategies across the organization
    + Efficiency effort: Prioritize work that delivers actual cost savings
      - Ex: Focus on reducing costs of infrastructure services with high priority timeframes
    + Cost efficiency in infrastructure stack
      - Example: Optimize HTTP router, load balancer, relational database, caching proxy, and connection multiplexer components
  - Challenges faced during implementation
    - Risk of over-optimizing performance boundaries
    - Difficulty in prioritizing work that delivers cost savings
      - Example: Avoid spending a lot of time on saving $50 if it doesn't contribute to achieving the overall business objective
  - Use of data and analysis tools for tracking progress
    - Ex: Google Cloud operations suite, Kubernetes, and custom-built tools
  - Lessons learned from the project
    - Importance of setting realistic expectations and goals
      - Example: Aiming for a 25% reduction in monthly spend
    - Need to understand the context behind cost savings estimates
      - Example: Team members may not always accurately estimate the impact of their work on costs
    - Use of visualization tools to help identify opportunities for optimization
      - Ex: Flame graphs, hierarchical tracing data, and custom-built dashboards
  - Importance of providing engineers with the right tools and context to make informed decisions about cost savings
    - Example: Giving engineers access to billing data and providing them with a clear understanding of how their work impacts overall costs
  - Challenges in attributing resource usage to specific workloads or teams
    - Ex: Difficulty in tracking inventory across different systems and regions
      - Solution: Use self-describing resources that provide detailed information about who is using them and why
  - Importance of understanding the relationship between cost and value
    - Ex: Understanding how much it costs to deliver a specific business objective (e.g., handling one million requests per minute)
      - Solution: Use unit cost calculations to help stakeholders understand the trade-offs involved in different spending decisions
  - Conclusion: The importance of continuously monitoring and optimizing infrastructure costs to maintain a sustainable business model


## SREcon23 Americas - Sto: A Better Way to Store and Query Profiler Data

URL: [https://www.youtube.com/watch?v=GvVkfS1LuQs](https://www.youtube.com/watch?v=GvVkfS1LuQs)

- Meadow Someru from the efficiency capacity engineering team at Facebook presented a talk about profiling data.
- Profiling data is often generated using tools like perf, lib BPF kit, and observational data.
- The presentation used a flame graph to visualize performance data.
- A stack snapshot was introduced as a way of gathering information on the system's performance.
- Stow is an open-source tool that optimizes profiler data storage by using a directed acyclic graph (DAG) model, which reduces the footprint of the data by five orders of magnitude.
- The DAG model allows for efficient querying and scaling of the data.
- Stack node data was identified as a key component in the Stow system, with each stack node containing a combination of positional and definitional information.
- Stow enables distributed aggregation and the ability to find regressions across reused code.
- The presentation demonstrated how to use Stow to identify performance issues in a binary application.
- The data model used by Stow enables efficient indexing and querying of stack node data, making it easy to find patterns and trends within the data.


## SREcon23 Americas - Chaos-Driven Development: TDD for Distributed Systems

URL: [https://www.youtube.com/watch?v=RkuA17ce7pU](https://www.youtube.com/watch?v=RkuA17ce7pU)

- Tucker Vento, a resilience engineer at Bloomberg, discusses the importance of chaos engineering in building reliable and resilient systems.
- Bloomberg has over 7000 software engineers maintaining one of the largest private networks in the world with high data processing capabilities.
- They have formalized their use of chaos engineering to make their systems more resilient.
- Chaos engineering allows for a shorter feedback cycle, enabling teams to learn proactively and respond quickly to potential issues before they become problems.
- The process involves carefully planning experiments, triggering expected alerts, and validating system expectations with unit tests.
- Test Driven Development (TDD) has been proven effective in improving code quality and understanding of systems, but it can sometimes lead to worse code depending on the specific context.
- Chaos engineering complements TDD by focusing on resilience and reliability testing early in the development process.
- The advantage of applying chaos engineering early in the life cycle is that it allows for better understanding of system behavior and helps identify potential issues before they become major problems.
- A real-world example of applying chaos engineering was given using a Kubernetes cluster to build a highly resilient log aggregation architecture.
- The process involved writing experiments, triggering failures, and monitoring the system's response to ensure that it could handle unexpected events.
- By incorporating chaos engineering into the development process, teams can identify potential issues earlier and make more informed decisions about design choices, leading to better overall system reliability.


## SREcon23 Americas - Adaptive Concurrency Control for Mixed Analytical Workloads

URL: [https://www.youtube.com/watch?v=-UDeh-kBRbc](https://www.youtube.com/watch?v=-UDeh-kBRbc)

- Introduced a system to manage capacity and concurrency in a data analytics service
    - Raw data is ingested, computed, and stored for answering targeted questions from users
    - The system was designed to serve fast analytical data across various use cases
- Discussed the challenges faced when the system grew and evolved
    - The system became unwieldy and expensive to maintain due to operational complexity
    - It was difficult to fit every use case into existing query patterns, which required materializing and storing data in a variety of ways
- Introduced a new approach for managing capacity and concurrency in the system
    - Developed an adaptive mechanism called AIMD (Additive Increase Multiplicative Decrease) to adjust limits based on latency measurements
    - Implemented a routing mechanism that finds the best server to process requests, which also serves as a load balancing and utilization mechanism
- Explained how the system can adapt to changes in traffic and complexity
    - The system can account for both increased traffic and arbitrary uncontrollable complexity by adjusting limits and reevaluating window measurements
- Showcased an example of how the system can handle different use cases and workloads
    - The system can partition its capacity based on preconfigured percentages, allowing it to serve different use cases while guaranteeing certain throughput levels
- Demonstrated how the system can monitor and respond to latency spikes in real-time
    - The system uses latency measurements and aggregation windows to identify spikes and adjust its capacity accordingly
- Explained the benefits of using the new approach for managing capacity and concurrency in the system
    - The system can now handle a mix of query types, workloads, and use cases more efficiently while maintaining high performance levels


## SREcon23 Americas - If I Can Do It on an Ambulance, You Can Do It in an Office: Scalable Incident

URL: [https://www.youtube.com/watch?v=aOP796AlOKE](https://www.youtube.com/watch?v=aOP796AlOKE)

- Presented a personal journey from ambulance service to technology.
- Described the ICS (Incident Command System) model and how it applies to incident response in software teams.
- Emphasized that adaptability is key in incident response, and that practice and teamwork are crucial for effective handling of incidents.
- Discussed the importance of coordination, communication, and expertise within an incident response team.
- Highlighted the need for flexibility and scalability in incident response processes.
- Suggested using a variety of methods to practice incident response, including tabletop exercises, simulations, and real-life non-incident scenarios.
- Encouraged attendees to plant seeds, grow their understanding, and ask questions to improve their incident response capabilities.


## SREcon23 Americas - How To Take Prometheus Planet Scale: Massively Large Scale Metrics Installations

URL: [https://www.youtube.com/watch?v=MVFnv347_q4](https://www.youtube.com/watch?v=MVFnv347_q4)

- Prometheus Planet Scale Journey: EBay's Observability Platform
  - Use Cases:
    - Instrumentation: Developers either use managed Frameworks, instrumentation libraries, or baked examples like Prometheus client.
    - Dashboarding and Visualization: Go application can say "Hey, I need a Prometheus endpoint monitored." Log file can be tailed.
  - Challenges and Lessons Learned:
    - Scalability: Given the scale of EBay's metric installation (125 million+ Prometheus endpoints), they needed to ensure high availability and fault tolerance.
      * Solution: They built a distributed architecture with many smaller Prometheus instances, each responsible for a subset of metrics. This allowed them to distribute load across multiple instances and provide redundancy in case one instance failed.
    - Query Performance: As the number of time series grew, query performance became a major issue.
      * Solution: They implemented a distributed query system that pushed queries down to the data source (the Prometheus instances) rather than pulling all the data up to a central server for processing. This significantly reduced the amount of data that needed to be transferred and improved query response times.
    - Data Consistency: Ensuring that all instances of Prometheus had consistent, up-to-date data was challenging.
      * Solution: They implemented a replication system that maintained multiple copies of each time series across different instances. This ensured that if one instance failed, the data could be quickly recovered from another instance.
    - Fan-Out and Federation: As the number of Prometheus instances grew, managing them all became increasingly complex.
      * Solution: They implemented a federated architecture where each instance was responsible for a specific subset of metrics (e.g., a particular namespace or cluster). This allowed them to manage smaller groups of instances more easily and reduce the complexity of the overall system.
    - Observability: EBay wanted to provide users with access to raw metric data, as well as pre-processed data like histograms and quantiles.
      * Solution: They implemented a storage management system that could handle both raw and processed data, and allowed users to query either type of data using the same interface.
    - Scaling and Performance: As the number of time series grew, they needed to ensure that their system could handle the increased load without compromising performance.
      * Solution: They implemented a distributed storage system that could scale horbizontally by adding more nodes as needed. This allowed them to handle large amounts of data without sacrificing performance or reliability.
    - Time Series Data Retention and Compression: As EBay collected more metric data, they needed to find ways to store it efficiently and cost-effectively.
      * Solution: They implemented a time series database (TSDB) that could compress data using techniques like delta encoding and sharding to distribute data across multiple nodes. This allowed them to store large amounts of data without using excessive storage resources.
    - Querying and Visualization: EBay wanted to provide users with powerful querying capabilities and intuitive visualizations for their metric data.
      * Solution: They implemented a query language called PromQL that could be used to create complex queries and visualize the results in tools like Grafana. This allowed users to quickly analyze their data and identify trends or anomalies.
    - Troubleshooting and Alerting: EBay wanted to provide users with real-time alerts when something went wrong in their system.
      * Solution: They implemented a monitoring system that could detect unusual patterns in the metric data and trigger alerts when necessary. This allowed users to quickly respond to issues before they became serious problems.
    - Future Directions and Open Source Contributions: EBay is considering open-sourcing their entire observability platform, which would allow other organizations to benefit from their experience and expertise in building a scalable, reliable, and efficient metric collection and analysis system.


## SREcon23 Americas - Your Infrastructure Needs to D.I.E.

URL: [https://www.youtube.com/watch?v=iO5d_tKwMfA](https://www.youtube.com/watch?v=iO5d_tKwMfA)

- Keynote presentation by Sarikon
- Focus on infrastructure security
- Divided into three parts: Heist, CIA Triad, and Distributed Immutable Ephemeral (DIE)
- The Heist: True story of a diamond heist in Antwerp, Belgium in 2003 as an analogy for how attackers think
- CIA Triad: Confidentiality, Integrity, Availability; still relevant today despite being "antiquated"
- DIE: Infrastructure should be distributed (avoid single points of failure), immutable (not changeable once deployed), and ephemeral (short-lived)
- Cloud native: A mindset that embraces the DIE principles using tools like Kubernetes, HashiCorp Vault, Terraform, and Packer
- Security should be built into infrastructure from the start rather than being an afterthought
- Chaos engineering: A method of testing infrastructure by intentionally causing failures to understand how it will react in real-world situations
- The goal is to create a resilient system that can withstand attacks and other unexpected events


## SREcon23 Americas - Not All Minutes Are Equal: The Secret behind SLO Adoption Failure

URL: [https://www.youtube.com/watch?v=OvWZ9WlEY4E](https://www.youtube.com/watch?v=OvWZ9WlEY4E)

- Introduced as a manager from Cre BOS
- Discussed issues with Kubernetes and S3
- Shared personal journey of implementing reliability measurements in an organization
- Mentioned the importance of adopting a strategy around new technologies, tools, or processes
- Discussed the concept of 'error budgets' and how they can be used to measure system reliability
- Highlighted the role of SLI (Service Level Indicators) in measuring system health
- Emphasized the importance of understanding customer needs and expectations when implementing reliability strategies
- Shared experiences with adopting new tools or processes, including challenges faced and lessons learned
- Discussed the concept of 'slow burns' and how they can impact system reliability
- Highlighted the importance of teamwork and collaboration in implementing successful reliability strategies
- Mentioned the role of leadership and management in supporting and guiding teams through the implementation process
- Provided examples of effective communication and collaboration techniques, including the use of '5 Ws' and 'how' questions
- Shared insights into the importance of continuous learning and improvement when implementing reliability strategies
- Discussed the role of policies and procedures in supporting successful implementation processes
- Highlighted the importance of understanding system behavior and instrumentation when implementing reliability strategies
- Emphasized the need for a clear baseline and objectives when implementing reliability strategies
- Shared examples of effective process implementation, including the use of 'start small' and 'iterative' approaches
- Discussed the role of customer experience in shaping successful reliability strategies
- Highlighted the importance of understanding and addressing system complexity when implementing reliability strategies
- Emphasized the need for ongoing validation and testing when implementing reliability strategies
- Shared insights into the importance of effective communication and collaboration when implementing reliability strategies


## SREcon23 Americas - Hell Is Other Platforms

URL: [https://www.youtube.com/watch?v=jNP4nzIMK8E](https://www.youtube.com/watch?v=jNP4nzIMK8E)

- The speaker shares his journey with devops, SRE, and platform engineering
- He talks about the confusion around these terms and their definitions
- The speaker emphasizes the importance of platforms for running reliable services
- He discusses the challenges of defining true platform and how it relates to human behavior and agency
- The speaker highlights the need for meaningful decision-making and taking action in a changing environment
- He shares his experience with system administration, distributed systems, and sociotechnical systems
- The speaker concludes by suggesting that we should let go of our dependencies on others' definitions and take control of our own platforms and systems.



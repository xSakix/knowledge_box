---
tags:
    - event-driven-architecture
---

# Building Distributed Applications with Event-Driven Architecture - Eric Johnson's presentation at GOTO 2023

In a world where technology evolves at a breakneck pace, keeping up with the latest trends and practices in software development can be daunting. One such emerging trend is the concept of Event-Driven Architecture (EDA) in building distributed applications. Eric Johnson, in his talk at GOTO 2023, brilliantly demystified this concept, providing valuable insights and practical advice. His presentation, "Building Distributed Applications with Event-Driven Architecture," now available on [YouTube](https://www.youtube.com/watch?v=9StQpMLC-5Q), serves as an excellent resource for developers and architects looking to deepen their understanding of EDA and its applications.

## The Essence of Event-Driven Architecture

The core idea behind EDA, as Eric puts it, is simple yet profound - "something happens, and we react." This approach is a significant shift from the traditional request-response model prevalent in many systems. In EDA, the focus is on events - occurrences or changes in state that trigger specific workflows or processes. This model is inherently more dynamic and can lead to more responsive, scalable, and flexible systems.

## Transitioning from Synchronous to Asynchronous Models

A pivotal point in Eric's talk is the emphasis on moving from synchronous to asynchronous models. Synchronous systems, while straightforward, have their drawbacks, particularly in terms of scalability and fault tolerance. Asynchronous systems, on the other hand, offer better resilience and flexibility. They allow components to operate independently, reducing the ripple effect of failures and improving system availability.

### Asynchronous Point-to-Point (Queue)

One method Eric discusses is the asynchronous point-to-point model, typically implemented using a queue. This setup decreases the direct coupling between sender and receiver, allowing for more resilient systems. If a receiver fails, the messages are safely queued, ready to be processed once the receiver is back online.

### Asynchronous Message-Router (Bus)

Another model highlighted is the asynchronous message-router, utilizing an event bus. This model centralizes the routing logic, decoupling it from individual senders and receivers. An event bus can efficiently distribute events to the appropriate services based on predefined rules, facilitating a more modular and maintainable system architecture.

## The Role of Choreography and Orchestration

In EDA, choreography and orchestration play crucial roles. Choreography is used for communication between different domains or services, allowing them to publish and subscribe to events autonomously. Orchestration, meanwhile, is employed within a domain to manage workflows and ensure tasks are executed in the correct sequence. AWS Step Functions, as Eric notes, is a prime example of a tool that facilitates orchestration in serverless architectures.

## Ensuring Idempotency in Distributed Systems

A key challenge in distributed systems is ensuring idempotency - the property that ensures operations can be performed multiple times without changing the result. Eric delves into practical strategies to maintain idempotency, such as using tokens and persistent layers. By embedding these practices into your systems, you can avoid issues like duplicate processing, which is particularly crucial in scenarios involving transactions or sensitive data.

## Harnessing AWS Services for EDA

Throughout his talk, Eric leverages AWS services to illustrate EDA concepts. Services like Amazon SQS (Simple Queue Service), Lambda, and EventBridge are shown to effectively implement the principles of EDA. For instance, SQS helps manage asynchronous communication through queues, while EventBridge acts as a robust event bus, routing events based on specified criteria.

## Key Takeaways

1. **Embrace Asynchrony**: Moving from synchronous to asynchronous models in distributed systems enhances resilience and flexibility.

2. **Leverage Queues and Event Buses**: Utilizing asynchronous queues and event buses can significantly reduce coupling and improve system maintainability.

3. **Choreography and Orchestration**: Effectively manage communication and workflows in distributed systems through choreography for inter-domain communication and orchestration within domains.

4. **Maintain Idempotency**: Implementing idempotency safeguards your systems against duplication and inconsistencies, especially in distributed environments.

5. **Use the Right Tools**: Explore AWS services like SQS, Lambda, and EventBridge to build robust, event-driven architectures.

Eric Johnson's presentation at GOTO 2023 is a treasure trove of insights for anyone looking to navigate the complexities of building distributed applications using event-driven architecture. By breaking down these concepts into understandable and actionable points, he provides a roadmap for developing more resilient, scalable, and efficient systems. Whether you're a seasoned architect or a budding developer, this talk is a must-watch, offering guidance and inspiration for your next big project. Don't forget to check out the full presentation on [YouTube](https://www.youtube.com/watch?v=9StQpMLC-5Q) for a deeper dive into the world of event-driven architecture.
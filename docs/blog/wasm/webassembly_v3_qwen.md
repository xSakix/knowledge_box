## Server-Side WebAssembly | DevNation Tech Talk

URL: [https://www.youtube.com/watch?v=BFZWFuFVIFU](https://www.youtube.com/watch?v=BFZWFuFVIFU)

# **Web Assembly: A Game-Changer in Cloud Computing and Edge Applications**

Good morning everyone, and welcome to today's discussion on the rapidly evolving technology of WebAssembly (WASM) and its potential impact on cloud computing. Our speaker, Ivan Font from Red Hat, will guide us through a journey that started with curiosity about WASM and has led to a deeper understanding of its capabilities and implications.

## Introduction: The Early Days
Ivan began his presentation by sharing how his background in embedded Linux and a shift towards cloud software at Red Hat exposed him to WebAssembly. Initially seen as a browser technology, WASM's potential went beyond expectations, challenging the notion that it could replace fundamental components like containers. 

### Container Revolution
Before diving into WASM, let's acknowledge the significance of containers in revolutionizing cloud computing. Docker introduced the concept of packaging applications neatly, offering developers a seamless experience and enabling container orchestration platforms like Kubernetes and OpenShift to thrive. Containers' success was built on their operating system-level abstraction, scalability, fault tolerance, and operability.

## WebAssembly: The Low-Level Player
WebAssembly is a binary instruction format that represents low-level hardware operations, making it OS-agnostic and compatible with various compilers (e.g., Rust, C, C++, Go). Its key features include:

1. **Portability**: WASM can be deployed anywhere, allowing developers to choose their preferred language without sacrificing platform compatibility.
2. **Lightweight Execution**: Single-threaded, stack-based virtual machines reduce CPU register requirements and result in faster execution compared to traditional VMs or interpreted languages.
3. **Sandboxing**: The sandbox nature of WASM execution ensures security by default, with explicit access granted for operations like file system interaction.

### WebAssembly Ecosystem
The ecosystem around WebAssembly is growing, with the OCI image standard supporting packaging and distribution. Although it doesn't replace Docker images entirely, WASM enables lightweight deployment and can be used alongside existing infrastructure.

## Comparing WebAssembly to Java Bytecode and Containers
Ivan discussed the differences between WebAssembly and Java bytecode (JVM), highlighting that while JVM supports multiple languages but lost its edge as a web platform technology, WASM emerged stronger with native performance and better integration into the web stack.

### The Future of WebAssembly
WebAssembly's roadmap includes support for multithreading, which is currently in development by the Wasm subgroup. This could open up new possibilities for server-side applications and event-driven microservices, without sacrificing portability like traditional VMs do.

## Key Benefits for Cloud Software
Here are the five key advantages of WebAssembly in the context of cloud computing:

1. **Generalizability**: WASM's compatibility with multiple languages means developers can write once, deploy anywhere.
2. **Security**: Built-in sandboxing and deny-by-default security model provide implicit protection.
3. **Efficiency**: Fast deployment (microseconds), small memory footprint, and low cold start times make it suitable for serverless use cases.
4. **Performance**: Depending on the compilation mode (interpreted, just-in-time, or ahead-of-time), WASM can offer near-native speeds.
5. **Portability**: Though not as portable as containers, WASM's architecture agnosticism allows for easier relocation across different environments.

## Edge Computing and WebAssembly
WebAssembly emerges as a promising technology for edge computing due to its small resource footprint and universal binary nature. It enables seamless application movement between the cloud, edge, and devices with limited resources, making it an ideal choice for edge applications.

In conclusion, Ivan believes that WebAssembly has the potential to become a complementary tool in the developer's toolbox, rather than a replacement for existing technologies like containers. As the technology continues to mature and evolve, it will likely play a significant role in shaping the future of cloud and edge computing. Stay tuned for more advancements in this exciting space!



## Introduction - Palmer Dabbelt

URL: [https://www.youtube.com/watch?v=1VfqoEjrn-I](https://www.youtube.com/watch?v=1VfqoEjrn-I)

 * Plumber Dabbelt introducing himself at a conference
* Not a discussion-oriented conference, expected to give presentation
* Sponsors provided food, thanks them
* Code of conduct slide presented, no harassment allowed
* Encourages note-taking using shared tools like Matrix BBB or text files
* Least some people take notes during talks
* Good for hallway tracking later
* Will try to stick to time with a few minutes left for next talk to start in three minutes.


## Deprecating Stuff - Palmer Dabbelt

URL: [https://www.youtube.com/watch?v=5bvnF316qXc](https://www.youtube.com/watch?v=5bvnF316qXc)

 * Speaker discusses deprecation of outdated or unused kernel features
* Mentioned specific examples: XIP, SBI 01, non-relocatable kernel
* Reasoning behind deprecation: low usage, maintenance burden, compatibility issues
* Decision making process: mailing list discussion, user feedback, potential impact on existing users
* Some features may still be in use and not worth the effort to remove
* Deprecated items may have replacement solutions or workarounds available
* Deprecation process might take time and involve communication with users.


## Run ILP32 on RV64 ISA (RV64ILP32) - Ren Guo

URL: [https://www.youtube.com/watch?v=vKUHIFYf6lU](https://www.youtube.com/watch?v=vKUHIFYf6lU)

 * Goran from Alibaba RISC-V ecosystem team discussing RV64ILP32 (RV64 with ILP32 ABI)
* Traditional 32bit API is RV32 i32, 64bit API is RV64 LP64
* Motivation for RV64ILP32:
  + Customer request to run IOP32 software on RV64 hardware
  + Improved memory footprint for small data workloads
  + Better data density and utilization in extreme benchmarking
* Differences between ILP32 and LP64:
  + Data type differences
  + ISA differences
* Implementation discussion:
  + Attempts to configure L kernel with tiny user case
  + Comparison of 64bit and 32bit kernels
  + Benefits of RV64ILP32: smaller memory footprint, better data density, improved performance for some workloads, better Atomic operations, ability to share code between traditional 64bit and ILP32 implementations.
* Challenges:
  + Lack of a robust ecosystem for ILP32 like x86
  + Complexity of introducing a new ABI in RISC-V
  + Convincing customers to switch from 32bit to 64bit ISA.
* Opinion:
  + Existing high performance hardware may not require ILP32 support
  + Running 32bit user space on 64bit hardware is generally sensible for small memory systems.


## RISCV patchwork CI - Björn Töpel

URL: [https://www.youtube.com/watch?v=hOqVycVtJmM](https://www.youtube.com/watch?v=hOqVycVtJmM)

 * Björn Töpel discusses Patchwork CI, a pre-merge hook system for building and merging patches
* Originally started as a RISC-V port of the patchwork subsystem in netdev
* Conor McKenna previously hosted patchwork CI, but it broke when he left
* Töpel considered moving to GitHub for community involvement and easier maintenance
* Decided to use BPF (Berkeley Packet Filter) for background processes
* Meta published KPD (Kernel Patch Demon) source code as part of the plan
* Intended to make it easier to maintain and allow for more contributions from the community
* GitHub CI was ported and runs on dedicated runners for faster build times
* Builds are synced from patchwork and GitHub repositories using Git
* If a pull request fails, a warning is generated and published on Patchwork for reviewers to address
* Builds can be performed locally using a simple bash script and Solidor's makefile
* Töpel suggests keeping the build matrix sane by limiting the number of variations
* Runners use Docker-based builds with cross-compilation toolchains for ARM64 systems
* Testing includes both 32-bit and 64-bit builds, and there's a need to ensure maximum utilization and performance
* Next steps include performing fixes, ensuring the build process works correctly, and collaborating on releases.


## Proposal of porting Trusted Execution Environment Provisioning (TEEP) Protocol... - Akira Tsukamoto

URL: [https://www.youtube.com/watch?v=g3qQSUILTUQ](https://www.youtube.com/watch?v=g3qQSUILTUQ)

 * Akira Tsukamoto is proposing the porting of the Trusted Execution Environment Provisioning (TEEP) Protocol
* He mentions that he couldn't attend a different conference last week due to financial constraints and wants to add "plumber" as a related term
* The implementation of TEEP goes back to his experience with PlayStation 3's secure boot and separate memory space for sensitive data
* World Guard CPU and secure mode firmware are mentioned as potential implementations, but not necessarily using a World card or the Keystone project
* Documentation and API specifications are available on GitHub
* The TP device side will provide an API and the implementation makes it easier to run applications in ARM trust zones
* Security is a priority, with hidden devices and SM regions underneath runtime S Mode regions being protected
* Assumptions include the need for secure boot and proper resource implementation, as well as use cases in automotive, network equipment, and drones
* Discussion of POC things and Opti version, as well as potential issues with Docker and current implementations using PMP
* Working group discussions involve SMTT domain IDs and memory protection for confidential computing.


## SBI Supervisor Software Events - Clément Léger

URL: [https://www.youtube.com/watch?v=FBXy334aGqY](https://www.youtube.com/watch?v=FBXy334aGqY)

 * Clément Léger, formerly of Exotic Architecture, discussing Supervisor Software Events (SBI) extension for S5 architecture
* Extension allows injection of high-priority events and interrupts in higher privilege mode
* Used for reliability, availability, and serviceability error handling
* Also uses Performance Monitoring Unit (PMU) Overflow and power management features
* Events can be local or global, divert execution and resume upon completion
* Supervisor mode OS remains orthogonal to normal operation, using regular interrupt path instead of SS entry
* Interrupt injection minimally modifies existing codebase, with no need to modify IRQ masks or hardware resources except memory stack allocation for events
* Proposed event priority scheme allows global and local events to be prioritized
* Implementers might want to prioritize platform events higher than others
* SBI context registration is discussed as a potential solution for getting the current task in RISC-V, but challenges remain due to the lack of a reliable way to know exactly where the current task is located based on its address previously executed
* Considered using annotations to mark event sections and source code to solve the issue, but no better ID scheme has been found yet
* Discusses potential advantages and disadvantages of S versus P Modes for handling interrupts and events, as well as advanced preemption implementation in SBI
* Raised issues include interrupt cancellation time, exception paths, current task location identification, and the need to modify specific registers for SS support.


## Perf feature improvements in RISCV - Atish Patra

URL: [https://www.youtube.com/watch?v=rxX6wUe3cJw](https://www.youtube.com/watch?v=rxX6wUe3cJw)

 * Speaker discussed improvements to RISCV's perf feature, specifically focusing on SS (Performance Counter Subsystem)
* ESOPe PMU extension for per-start sampling was implemented, but different versions have different dependencies and require different framework patches
* S Mode in RISCV relies on SPI pmu extension for hardware counter profiling, but it brings some issues and is not backward compatible
* The speaker suggested introducing a JSON file for event mapping to avoid naming conflicts and simplify the process of accessing counters
* Discussed the need to support raw events in the SBI (Supervisor Call Interface) driver without using SBPU (Software Performance Monitoring Unit)
* Proposed solutions included making the driver backward compatible, using a static key for I extension, and providing counter information to the driver.
* The speaker discussed the issue of event discovery and suggested using a standard event name mapping for vendors instead of raw events
* Discussed the problem of counter mapping on x86 and proposed using a JSON file infrastructure with vendor-specific counter constraints and a standard way of handling encoding schemes
* Mentioned some obscure use cases and the need to check the actual usage of encoding fields and config bits.


## RISC-V Vector: Current Status and Next? - Tao Chiu

URL: [https://www.youtube.com/watch?v=eht3PccEn5o](https://www.youtube.com/watch?v=eht3PccEn5o)

 * Tao Chiu discussing RISC-V Vector current development status and future plans
* UWR size is currently small, but will introduce larger sizes in V3 and V4
* Supports running Vector user mode context, lazy save/restore, P TR Signal interface
* Kernel Vector part supports running without preemption
* Challenges include Koral Vector like Bly, optimal performance with FPJ setup, net performance benchmarks
* Blindly enabling Vector operations results in around 54% improvement
* Proposed improvements include enabling Vector default booting and optimizing disable/enable plots
* Vendor may give number for optimal Vector size
* Depends on memory bandwidth and use cases (server vs FPGA scenarios)
* Discusses user space Vector lazy restore moment, kernel enable multiple saves, detecting boundary between Vector and scalar performance.


## Control Flow Integrity on RISCV - Deepak Gupta

URL: [https://www.youtube.com/watch?v=-Lu_cfIXGkQ](https://www.youtube.com/watch?v=-Lu_cfIXGkQ)

 * Control Flow Integrity (CFI) is a security mechanism to protect against memory safety issues, specifically function pointer and virtual function table attacks
* RISCV architecture proposes two extensions: ZFIC (Zero Forward Control Integrity) and ZFSS (Zero Frame Shadow Stack)
* ZFIC uses landing pads to enforce indirect branches must land on a specific instruction or raise a fault
* ZFSS extends the architecture with a shadow stack to store return addresses and ensure they are not corrupted during runtime
* CFI is still under development, with current directions leaning towards implementing both extensions together for improved security
* CFIs prologue would involve enabling relevant knobs, updating registers, and checking immutability of landing pads
* Shadow stacks need protection as their manipulation could compromise the security property
* Current implementation involves setting VM flags in user mode to protect shadow stack memory
* GDB patching of target functions may not work with CFI due to landing pad checks
* Long jumps and setjmp/longjmp are potential issues as they can bypass CFI protections
* Token switching is a possible solution for safely switching shadow stacks
* The control flow integrity issue has been addressed in x86 architecture using different techniques, but the implementation details were not specified.


## RISC-V irqbypass with KVM - Andrew Jones

URL: [https://www.youtube.com/watch?v=BWJZzv-fOsw](https://www.youtube.com/watch?v=BWJZzv-fOsw)

 * IQ bypass in RISC-V architecture
* Hypervisor (KVM) can inject interrupts on behalf of devices in the VM hierarchy
* Two approaches to guest interrupt handling: using a file or an in-memory representation (IMR)
* Injecting MSI directly to a virtual CPU is possible, but requires dedicated vCPU and special address range
* KVM supports both IMR and IMU (Interrupt Moderation Unit), each having their advantages and disadvantages
* Vfio provides a framework for bypassing the hypervisor, making it easier to configure RISC-V irqbypass with KVM
* Communication between KVM and IMU requires setting up a structure and handling interrupts directly within the IMU driver
* One issue is that the IMU driver doesn't know the virtual interrupt number when registering the handler, which needs to be resolved
* The goal is for KVM to handle MSI notifications for better performance and less context switching.


## Android MC Intro

URL: [https://www.youtube.com/watch?v=o86zR6RJ7-Q](https://www.youtube.com/watch?v=o86zR6RJ7-Q)

 * Welcome by Kareem on behalf of John Summit and the organization committee
* Android Microconference, 11th Edition: evolution of relationship between Android development team and ecosystem, including Linux community
* Discussing legal requirements for maintaining software long-term, hopefully encouraging silicon vendors to contribute upstream
* Upcoming topic: implications of a 16k page limit in user space Android, focusing on risk and architecture (mostly ARM)
* Hybrid format with online and in-person attendees
* Speak into mic for questions, and speakers will repeat them for everyone to hear
* Slides will be uploaded afterward, with a 15-minute speaking slot and 5 minutes for Q&A afterwards
* Breaks scheduled throughout the day, including a 405 buff on Wednesday morning for open discussion.


## Driver Development Kit DDK and Vendor Workflow - John Moon

URL: [https://www.youtube.com/watch?v=XF_AVjdGv84](https://www.youtube.com/watch?v=XF_AVjdGv84)

 * John Moon, software engineer at Qualcomm, discussing Driver Development Kit (DDK) and integrated workflow using Basil in Android 14.
* DDK is recommended for building external kernel modules.
* Kernel team manages common build definition, ABI compliance, and Tech pack which focuses on specific tech areas like display.
* Basil came along and the build system shifted from CLE to Basil.
* Buildsh was replaced with Basil build command for building kernel modules.
* DDK simplifies interdependency and reduces boilerplate code.
* Queries can be asked to the build system, making it easier to identify dependencies and resolve issues.
* Basil generates output files, helping with performance profiling.
* DDK provides native visibility, allowing dependent modules to access public headers easily.
* Learning a new build system is a con, as some developers may find it confusing and time-consuming.
* Debugging can be complicated due to the sandbox environment, which cleans up after each build by default.
* Config snippets have been added in DDK for defining feature flags per platform.
* DDK generates actual config files and resolves external mode files automatically.
* There is ongoing discussion about how DDK will handle conflicting build systems, like the Android build system and YAKO.
* Qualcomm has seen some upstreaming issues with DDK but is working on them.
* The learning curve for Basil may be a challenge for some developers.
* The majority of tech teams have mostly copied pasted templates to use Basil.
* John recommends watching a one-day introduction to Basil for getting started.


## Simplified Android Kernel Driver Development with DDK v2 - Matthias Männich, Mr Yifan Hong

URL: [https://www.youtube.com/watch?v=_enc4zy3TbE](https://www.youtube.com/watch?v=_enc4zy3TbE)

 * Matthias Männich from Android system team discusses simplified kernel driver development with DDK v2
* Goal is to create a simple, flashable kernel module in five minutes
* Using DDK involves inheriting the entire U-Boot build system and dependency resolution
* New feature: using `module depend ddk` to specify dependencies
* Build prebuilt signed image could be created through CI systems without building the kernel itself
* Specifying a particular repository and build number can help ensure consistent builds
* Upgrading LTS drivers within Android versions is possible, but may require changing strings or modifying makefiles
* DDK makes upstreaming easier by including license headers and dependency specifications in a friendly way
* Creating shadow copies of shared compiler files can save local cache space and make building prebuilt kernels more efficient
* DDK does not collide with source trees, but may require making modules available if multibranch systems are used
* Upstream alternative interface tables were not popular, so specifying a defined variable array with multiple options is an alternative
* Prebuilt kernel binaries can be downloaded and used in place of building from source with DDK.


## BPF Access Control and CO-RE in Android - Neill Kapron

URL: [https://www.youtube.com/watch?v=dimYrZLXh64](https://www.youtube.com/watch?v=dimYrZLXh64)

 * Neil Kapron from Android kernel Integrity team discusses enabling BPF (Berkeley Packet Filter) access control in Android
* Goal is to modernize BPF frameworks and enable secure vendor access with minimal impact on boot time
* BPF involves extending kernel functionality through user space in a secure manner
* BPF programs are compiled into bytecode, loaded by the kernel, and verified for potential infinite loops or uninitialized memory usage
* BPF maps allow communication between user space and kernel
* Current Android implementation has single point access to BPF loading and is based on a custom library
* Modern standard approach includes a block diagram of three different program classes: system (AOSP networking), vendor, and application
* Vendor programs are currently restricted in their ability to load BPF applications due to compatibility issues and lack of control over the file location
* Proposed solutions include extending the BPF loader with an additional allow list or creating a kernel module hook for validating lower-level function calls
* Security concerns around BPF include potential memory leaks and uninitialized memory access, which are addressed by the verifier
* Potential future use cases include extending SE Linux to provide greater control and enable vendor short-term solutions before full integration
* Key challenges include boot time compatibility, dealing with different kernel versions and library versions, and ensuring compatibility between BPF programs and the underlying kernel.


## Binder: fixing contention in buffer allocations - Carlos Llamas

URL: [https://www.youtube.com/watch?v=eLqYm97lWQc](https://www.youtube.com/watch?v=eLqYm97lWQc)

 * Carlos Llamas from Google discusses performance issues with Binder in Android's colonel team
* Binder uses memory mapping for buffer allocations, causing contention when multiple clients try to access the same region of memory
* Binder performs copying from user memory to service memory map area
* Memory regions are assigned as virtual memory areas (VMA) and transactions get individual binder buffers
* Virtual addresses need to be mapped to physical pages before copying, causing potential contention when pages aren't associated with the address
* Binder manually allocates pages for buffers and releases them using a least recently used list
* Memory pressure shrinker tries to reclaim pages and can cause contention during page release
* Contention occurs primarily in Graphics core pipeline and happens when low priority tasks take the mutex, blocking high priority tasks
* Nested memory maps can increase contention as acquiring memory map semaphores may require waiting for other unrelated VMAs to be released
* Turning mutexes into spin locks or using a per-binder page mutex for each process could improve performance significantly
* In V1, removing an operation might sleep and cause contention, so preallocating pages outside of mutexes is a solution
* Contention from map block changes was particularly bad in version 1, as locking per VMA led to significant contention
* Per-page mutexes under the binder page mutex could resolve serialization issues and improve performance
* Binder uses memory map logs in read mode instead of synchronizing operations via mutexes for better efficiency
* Consider using lockless synchronization methods like a maple tree or RCU (Read-Copy Update) for data structures
* The Rush implementation, which was replicated, mitigated the issue by removing the need for multiple clients to try raising faults on the same page without synchronization.


## Android Kernel testing with platform integration - Betty Zhou

URL: [https://www.youtube.com/watch?v=T7RhrQwh0xk](https://www.youtube.com/watch?v=T7RhrQwh0xk)

 * Betty Zhou discusses Android kernel platform integration testing
* Testing enabled on active kernel branch in Android Common Kernel Branch
* Goal is to catch regression early and ensure surprise U-phase issues
* Multistage test process starts with primitives checks at build time
* Covers ABI stability, simple tests like FOT, CTS, BTS, etc.
* External partners can also perform presubmit testing on physical devices
* Increases test coverage using virtual devices and x86 kernels
* Provides better debugging with current logs
* Performance regression detection is enabled in primitives tests
* Post-submit testing includes app compatibility, critical kernel tests
* New infrastructure introduced for better coverage and faster test runs
* Looking to add support for new verticals like Android TV and Android Auto
* Testing tools include Kernel Self Test (KST), local environments, trade fat test harnesses
* Results are made accessible to partners through Google's lab infrastructure.


## Improving suspend/resume time and runtime PM on Android - Saravana Kannan

URL: [https://www.youtube.com/watch?v=SmWaxhpYsaQ](https://www.youtube.com/watch?v=SmWaxhpYsaQ)

 * The speaker, Saravana Kannan, is discussing issues with suspend/resume time and runtime power management (PM) on Android.
* Suspend resume time is important for user experience as it affects display time and power usage.
* Cyclic dependencies between device firmware and drivers can cause issues during suspend/resume.
* The speaker proposes adding a property in the device tree for indicating if a supplier is not needed during probing to avoid cycle dependency issues.
* There is opposition to this proposal as it may lead to unnecessary initialization calls and polluting the device tree.
* The speaker suggests using standard properties instead, such as declaring driver probe time requirements.
* Android's runtime PM flag can be used to ensure that devices take care of supplier requirements during suspend/resume.
* The speaker mentions issues with Global acing (global power management), which may cause functional correctness problems and longer resume times in some cases.
* There is a discussion about using S2 idle instead of S2 RAM for power savings, but there are issues with the S2 idle path driver still using CIS orchestrator operations even when it shouldn't.
* The speaker mentions that some drivers do not properly handle runtime PM clock drivers, which can cause issues.
* There is a discussion about CPU PM notifiers and hot plug notifiers, with suggestions to simplify the transition between suspend and resume states for these notifiers.


## RISC-V support in Android - Curtis Galloway

URL: [https://www.youtube.com/watch?v=EW_AQk-490A](https://www.youtube.com/watch?v=EW_AQk-490A)

 * Curtis Galloway from Google's low-level operating system team providing update on RISC-V support in Android
* Vector crypto bit manipulation extension landed in Android, vector performance testing is ongoing
* Cuttlefish emulator now supports QEMU 8.1 with Vector available
* Working on upstreaming various things for full RISC-V compliance
* Discussing ABI (Application Binary Interface) decisions and importance of consensus
* RISC-V International Form is working on a risk VI international form factor board
* Android Ris five mailing list and GitHub issue list are good resources for following progress
* Goal is to have fully compliant Hardware support ratified RISC-V extensions
* Vector crypto, 32bit and 64bit instruction set combination supported
* Emulator testing and availability of development boards are important
* Encouraging community involvement and Upstream contributions for optimization and compliance.


## Adding Third-Party Hypervisor to Android Virtualization Framework - Elliot Berman, Prakruthi Heragu

URL: [https://www.youtube.com/watch?v=hLdUCrlheKg](https://www.youtube.com/watch?v=hLdUCrlheKg)

 * Elliot Berman presenting on adding third-party hypervisor to Android Virtualization Framework (AVF)
* AVF is a new framework for isolating Android apps with hypervisors, designed for VM isolation
* Hypervisor requirements for AVF are basic: able to launch virtual machines and handle mm access, vcpus, shutdown support, and essential Arch-specific devices
* Key differences from other hypervisors: begins with privileged VMs, el2 based scheduling, and supports Auto (IoT) use cases
* Upstream community changes include adding new hypervisor support using G driver in Linux kernel, enhancing debugging, and establishing chain trust
* Android 14 will focus on memory management for guest control and dynamic VM growth
* AVF has two primary components: user space component called Crossfum (virtual machine manager) and Linux kernel
* Adding new hypervisor requires creating a new crate in G and upstream changes to the Linux kernel
* Challenges include managing guest memory, improving debugging, extending DM communication, and sanitizing the device VM for longer runnability.


## Porting Android Automotive on Xen - Leo Yan

URL: [https://www.youtube.com/watch?v=gka4heCiUvM](https://www.youtube.com/watch?v=gka4heCiUvM)

 * Leo from Naro Session introduces project to run Android Automotive on Xen using Zen hypervisor
* Goal is to set up host-guest environment, integrate QEMU and enable NCSI and NDK support
* Using Yocto build system and Trusty reference stack for debugging
* Target is to use 64-bit Android image for automotive software on a cutfish virtual machine
* Three hardware platforms being tested: AA (Amlogic), TAS (Tegra), Rockie (open source)
* Software rendering used currently, no GPU acceleration
* Enabled ZF feature communication and event handling patches merged
* Virtual IO virtual device support tried, with some exceptions like virtual block devices
* Issue found with Android cutfish not supporting H.265 (HVVC) in the Virtual Console
* Added interactive console with a patch, enabled Virtual Console use
* Host side needs maintenance for QEMU repository and enabling virtual I/O virtual PCI bus support
* Guest side requires Android Automotive OS running on Zen virtual machine
* Offline patches need to be maintained as OS base code breaks every two months
* Goal is to reuse CFS USP image to run Zan virtual machine, dynamically generate Android image
* Developing a backend program for a standalone QEMU machine and device
* Volante GPU support progressing well
* Question: What's the end goal and benefit of running Android Automotive on Zen?
  * Proof-of-concept support for automotive and mixed criticality virtualization
  * Type 1 hypervisor with Zen as a prototype, integrating Verio demon later to run posix environment
  * Avoid reinventing the wheel by getting Verio accepted in the community and building a realtime hypervisor directly.


## Pixel 6 support on androidmainline - Peter Griffin, William McVicker

URL: [https://www.youtube.com/watch?v=tepy__nDQ-8](https://www.youtube.com/watch?v=tepy__nDQ-8)

 * William McVicker and Peter Griffin discussing Pixel 6 support on Android Mainline
* Goal is to increase testing, catch regressions, and propagate upstream merges for the Pixel 6
* Every kernel change made on the Pixel 6 is tested every GKI (Google Kernel Infrastructure) commit
* LTS merges from Upstream 510, 515, and Android Mainline branch are also tested on Pixel 6
* Allows kernel developer testing and evaluation of performance impact for potential contributions
* Project allows easier maintenance of functionality and performance incrementally with kernel release upgrades
* Bringing focus to specific kernel releases instead of upgrading older LTS versions
* List of changes landed or under review directly on the Pixel 6 Android Mainline development project
* Familiarity with pixel-specific features such as 16k support, VM CPU, and binder development
* Linux release lag reduction through earlier testing and integration of platform services like lkf and kernel C
* Discussed benefits of updating downstream drivers every kernel release
* Overlay solution to reduce technical debt and improve boot time
* Challenges with adding board IDs and enabling bootloader apply overlay
* Preference for boot time resolution over compile time concerns
* Discussion on using a single dtb image versus shipping several complete device trees for different variants.


## Can mainline Linux run on Android without vendor hooks - Qais Yousef

URL: [https://www.youtube.com/watch?v=QhiJ5UUOsKs](https://www.youtube.com/watch?v=QhiJ5UUOsKs)

 * Speaker, Qais Yousef, from Pixel Kel team, discusses the challenge of making mainline Linux run on Android without vendor hooks
* Vendor hooks are strategically placed in the kernel image by Android vendors to override functions or fix problems
* The primary motivation is to address quality issues such as stability, equality, UI, battery life, thermal, and hardware access
* Generic kernel image limitations include missing features, bugs that need fixing, and lack of tunability for the scheduler and other aspects
* Vendor hooks create inconsistency, fragmentation, and complexity, especially in the context of Android's diverse hardware topology and its differing approach to DVFS (Dynamic Voltage and Frequency Scaling)
* The speaker suggests a paradigm shift towards giving user space more control, as well as improvements like simpler Priority Inheritance and preventing circular deep inheritance
* The goal is to make Android workloads acceptable for commercial products while reducing the need for vendor hooks.


## 16KB Page Size Support - Juan Yescas, Kalesh Singh (Google)

URL: [https://www.youtube.com/watch?v=z5ge9ZzQgno](https://www.youtube.com/watch?v=z5ge9ZzQgno)

 * 16kB page size support on Android devices, specifically on the Pixel 6
* Benefits: decreased average load time, power consumption, and memory usage for certain apps like Google Search and Google News
* Trade-offs: increased alignment requirements, potential fragmentation, and possible compatibility issues with some drivers and libraries
* Challenges to implementing 16kB page size: ecosystem migration, virtual address alignment, loader complexity, and driver support
* Solutions: changing permissions, binary analysis, and driver fixes
* Impact on Android app developers: need to emulate 16kB page sizes for testing purposes on x86-based systems
* Performance improvement: reducing the number of page walks in a three-level page walk with larger 16kB pages.
* Misunderstanding in the chat: some participants suggested solutions that were not directly related to the topic, such as using a larger base size for the kernel or aligning binary data at 64KB.


## AOSP Devboards - Sumit Semwal

URL: [https://www.youtube.com/watch?v=pnUbw2LRiRw](https://www.youtube.com/watch?v=pnUbw2LRiRw)

 * Sumit Semwal, tech lead at Lenaro, discussing AOSP Devboards
* AOSP Devboards allow latest ASP development to overlap with Upstream development
* Supported devices include Hiiki, DBF 410C, 820C, DB 45C, and RB5 (working on enabling Xnos 850 based Devboard called 85096)
* Ensuring latest ASP work on supported Devboards, developers try to enable new features and validate them
* Community space proposed for people interested in running ASP on Devboards, with a focus on best practices and collaboration
* Over 820 million tests and 28 billion kernel combinations run since January 2021
* Regular testing keeps Upstream Linux stable, catching regression issues caused by changes in the merge window
* Discussion forum for ASP style collaboration and source navigation available at linaro.org/discussions
* Lenaro is looking for a trusted source to take ownership of adding new Devboards to the AOSP program
* Collaboration on creating a common scripting tool and consolidating essential info for Devboard work
* Long term initiative to ensure new Devboards work well with ASP, with a dashboard allowing building and testing mainline USP.


## Welcome message and DL Server - Daniel Bristot de Oliveira

URL: [https://www.youtube.com/watch?v=Hv26s4io3fo](https://www.youtube.com/watch?v=Hv26s4io3fo)

 * Daniel Bristot Oliveira welcomes attendees to Real Time Scheduling Micro Conference
* Thanks sponsors and organizers for making the conference possible
* Discusses idea of productive discussion during the conference using mailing list
* Encourages keeping a healthy ambience, letting ideas flow freely
* Introduces himself as a Red Hat employee working on real time verification and scheduling
* Discusses problem of real time schedulers causing starvation in fair tasks
* Proposes idea of boosting fair tasks during idle periods instead of boosting entire RT task queues
* Mentions previous attempts to fix the issue using mechanisms like deadline-based scheduling and throttling
* Talks about the importance of real time applications and their impact on system performance
* Discusses the potential use of a DL server for fair task scheduling and its implications.


## Do nothing fast: How to scale idle cpus? - Mathieu Desnoyers

URL: [https://www.youtube.com/watch?v=3z4-JP-KhPA](https://www.youtube.com/watch?v=3z4-JP-KhPA)

 * Mathieu Desnoyers presented at a micro conference about scaling idle CPUs in large systems
* Started investigation by adding concurrent C ID feature to Linux scheduler, but caused regression
* Tried removing spin lock and modifying algorithm, but caused another performance regression
* Noticed that idle context switching helped, so added delay loop for idling CPUs
* Also tried favoring previously used CPUs for waking tasks, rate limiting task migration, and biasing Run Q selection towards previous CPU
* Goal is to converge task placement based on communication pattern and improve system performance
* Discussed run metrics in Linux scheduler and the importance of taking account actual task utilization
* Tried using a predictor to keep track of interactions between tasks and wake relationships
* Working on task placement algorithm to create a heuristic for one-to-one workload pattern
* Goal is to reduce contention between tasks for CPU resources and improve system power efficiency.


## system pressure on CPUs capacity and feedback to scheduler - Vincent Guittot

URL: [https://www.youtube.com/watch?v=Nls5F6BS6Vw](https://www.youtube.com/watch?v=Nls5F6BS6Vw)

 * Vito Guittot from Laro Working Group discusses system pressure on CPU capacity and its impact on task placement, load balancing, and frequency scaling
* System pressure limits available compute capacity for CPUs even with powerful hardware
* High frequency scaling can impact CPU capacity in several ways: stealing CPU cycles, thermal limitations, and power management
* Hardware and firmware can cap maximum frequency to prevent wasting power or damaging the system
* User space CPU frequency scaling interfaces like Max Frack are used for capping frequency in distros
* System response time depends on current utilization and available compute capacity
* Deadline server example is a situation where knowing maximum available compute capacity is important for making task placement decisions
* Power and thermal pressure can affect available compute capacity
* Frequency scaling governors might not always make the best decisions regarding frequency switching
* Bringing down CPU frequency due to power limitations without proper notification can cause issues
* Scaling CPU capacity requires infrastructure to connect and communicate all components effectively
* Different systems may have unique ways of handling pressure, such as thermal frameworks and power capping interfaces
* VM scheduler awareness of host physical CPU contention can improve task placement on the host side.


## Optimizing Chromium Low-Power Workloads on Intel Notebooks - Len Brown, Ricardo Neri, Vaibhav Shanka

URL: [https://www.youtube.com/watch?v=jJr04sAinaQ](https://www.youtube.com/watch?v=jJr04sAinaQ)

 * Speakers: Ly Brown, Ricardo Neri, Vaibhav Shanka
* Topic: Optimizing Chromium low-power workloads on Intel notebooks
* Last year's talk mentioned Intel's Low Power Mode Demon and CPU isolation
* Focusing on performance vs power trade-offs in deca-core CPUs (big cores run fast but consume more power, small cores are power efficient but run slower)
* Implemented an autoload balancer with priority-based CPU scheduling
* Energy Performance Preference (EPP) knob for hardware P-state control
* Experiment 1: Power savings using EP task placement in video streaming, saving roughly 26% compared to default
* Experiment 2: Power savings from task binding in Chromium threads, saving roughly 72% compared to default
* Chromium work classifies tasks and sets priorities based on energy requirements
* Intel's hybrid processor uses dynamic power management and priority-based scheduling
* Q&A: Discussed limitations of low power mode, system orchestration, task migration, and kernel changes.


## How to reduce complexity in Proxy Execution - John Stultz

URL: [https://www.youtube.com/watch?v=HDtnNhLYsh0](https://www.youtube.com/watch?v=HDtnNhLYsh0)

 * John Stultz from Android system team discussing proxy execution to address priority inversion problem in Android
* Android cannot give untrusted applications real-time priority, instead uses throttling of background tasks to prevent interrupting foreground tasks
* Priority inheritance not effective as it causes inconsistent behavior and difficulty in throttling background tasks without affecting foreground tasks
* Proxy execution is a simple idea that tracks blocked relationship between mutex waiter and mutex owner, keeping the blocked mutex task running even if it's runnable, allowing the scheduler to pick important tasks
* Complexities include blocked chain migration across CPUs, resolving sleeping owner cases, and boosting run case DQ
* V5 was a big rework series with many patches, including changes to return migration, proxy migrated tasks, and wake path raciness, but introduced performance regression due to locks
* Current set issue is sleeping owner queuing, making it difficult to get right
* Other concerns include the complexity of midchain wakeup in unexpected owner cases and moving back through the wake path
* Implementation trick is using the scheduler's rb3 migrate to donor rb3 schedule the highest priority task while the lock owner is scheduled, eliminating the need for another rb3 chain
* Complexity comparison: proxy execution vs. priority inheritance, proxy execution might be more complex but is a viable option for dealing with real-world problems involving Sig group MX and contention in reader writer locks.


## 60 Adaptive userspace spinlocks with rseq - André Almeida, Mathieu Desnoyers

URL: [https://www.youtube.com/watch?v=6srYi1SM3GE](https://www.youtube.com/watch?v=6srYi1SM3GE)

 * Andrei from AlmaLinux discusses adaptive spin locks in user space using RAC
* Goal is to avoid the expense of contacting the kernel for mutex locks, especially in micro-contention scenarios
* RAC (Ring-based Adaptive Scheduler Capabilities) provides performance improvements by allowing user space to query CPU state without a C call
* Proposed structure:
  + Store current thread's state and trade ID in the same cache line
  + Eliminate shared structures to prevent contention
  + Use an auxiliary vector for reserved state information
* Concerns:
  + Robustness: interface requires reading thread information
  + Lipy (thread memory reclamation) could cause issues with memory access when using RAC as a mutex exit path
* Proposed solutions:
  + Use a user-space memory barrier to protect the state field from stale data
  + Implement a separate lock for shared memory cases

Key points:

* Adaptive spin locks in user space can improve performance by reducing the need for kernel context switches.
* RAC provides a way for user space to query CPU state without making a C call.
* Challenges include robustness, integration with existing thread and memory management systems, and trade-offs between complexity and performance.


## CPU Isolation state of the art - Frederic Weisbecker

URL: [https://www.youtube.com/watch?v=1lomUhSS82s](https://www.youtube.com/watch?v=1lomUhSS82s)

 * CPU isolation: preventing tasks from disturbing the kernel
* Issue with VM statistics gathering causing interruptions and affecting performance
* Attempts to solve problem using explicit and implicit queuing, but both had overhead and inaccuracy issues
* Realized memory management people were not the root cause of the problem
* New issue: artificially created memory pressure by vmstat causing contention on isolated CPUs
* Solution: deferring IPI execution to reduce interruptions and improve performance
* CPU set V2 has seen improvements with exclusive CPU sets and remote partitions
* C groups and containers require management of sub-containers and CPU isolation
* Differences between local and remote root partitions
* New feature in kernel version 67: CPU set exclusive, allowing distribution of exclusive CPUs without becoming a partitioner
* Discussion on differences between local and remote ancestor root partitions
* Overview of CPU set interface history and complexity
* Importance of protecting concurrent sources of disturbance using RCU and affinity settings.


## Improving CPU Isolation with per-cpu spinlocks: performance cost and analysis - Leonardo Bras Soares

URL: [https://www.youtube.com/watch?v=73dXIzqX5S4](https://www.youtube.com/watch?v=73dXIzqX5S4)

 * Leonardo Bras Soares presents on improving CPU isolation using per-CPU spinlocks
* Real-time tasks require CPU isolation to run without interruptions
* Problem: CPU isolation APIs can lead to scheduling work on isolated CPUs, which can result in contention and decreased performance
* Idea: Use local cache strategy and per-CPU spinlocks instead of global locks and scheduling work
* Per-CPU spinlocks reduce the need for remote access to shared resources and decrease contention
* Spinlocks are more efficient than global locks in terms of cost, but can be expensive due to contention and memory barrier contention
* Test results show that using per-CPU spinlocks instead of local locks can result in a significant reduction in clock cycles for both x86 and ARM architectures
* Implementing the new function to use local scheduling work and local spinlocks instead of remote spinlocks resulted in fewer overheads and improved performance.


## QA about PREEMP_RT - Thomas Gleixner

URL: [https://www.youtube.com/watch?v=O1dzeGJUvvU](https://www.youtube.com/watch?v=O1dzeGJUvvU)

 * Thomas Gleixner has been working on Linux real-time (RT) for almost 20 years
* The ongoing issue is synchronous vs asynchronous console output and handling in the kernel
* Original console implementation let print see what's happening but could cause issues with NMI, graphic driver, etc.
* Preempt RT was introduced to make console output useful in mainline non-RT systems
* Handover mechanism was developed to make thread collaboration easier for console output and emergency messages
* Estimation for bringing stuff from the RT tree to upstream involves a significant amount of work (around 800 patches) and could take around half a year
* Console driver compatibility is an ongoing issue, with some drivers still using old methods
* Graphics drivers are a challenge due to their virtual consoles and synchronous vs asynchronous output
* Linus Torvalds has asked for persistent memory options for printing important messages first
* Enabling RT on x86_64 architecture will require effort, especially in the generic code
* Fixing issues with specific drivers like i915 is ongoing and may involve writing new drivers from scratch
* There are arguments against merging preempt RT into the mainline kernel due to potential changes and compile time conditionals already being enabled
* AMD GPU driver instances have been merged successfully with minimal invasiveness
* I915 is a significant challenge due to its design and broken nature, which may require rewriting from scratch
* The future of Intel Graphics RT enablement is uncertain, with the new XE driver coming later.


## Introducing PAGEMAP_SCAN IOCTL for Windows syscalls translation... - Andrei Vagin, Muhammad Anjum

URL: [https://www.youtube.com/watch?v=EhzHz34w-tc](https://www.youtube.com/watch?v=EhzHz34w-tc)

 * Andrei Vagin and Muhammad Anjum discussed their experience implementing page map scan IOCTL for Windows syscalls translation.
* Use case: needed to track specific memory segments for large areas of memory in Windows, such as copying, security intrusion detection, garbage collection, etc.
* Linux approach considered: user space mechanism using M protect segmentation Handler and Page fault handler.
* Challenges: performance implications, potential merging of soft and non-soft dirty VMAs, atomicity problems with clearing page map entries.
* Solution: decided to use user fault FD (file descriptor) for asynchronous right protection with Windows API emulation.
* Benefits: simple, no need for complex atomic operations, efficient, and reduces the overhead of kernel interactions.
* Additional features added: support for huge pages, scanning functionality for memory type Pages, and a new page map interface.
* Considerations: unprivileged mode use of user fault FD for memory tracking, performance comparison between user space and kernel space solutions.


## User namespaces with host-isolated UIDs/GIDs - Aleksandr Mikhalitsyn, Stéphane Graber

URL: [https://www.youtube.com/watch?v=mSQeI1hePBQ](https://www.youtube.com/watch?v=mSQeI1hePBQ)

 * Stephan Graber from Canonical presenting work by Alex Mikhalitsyn on user namespaces and host-isolated UIDs/GIDs
* Issue: Containers often use high UIDs/GIDs for sandboxing, authentication, and other purposes, leading to overlapping maps and conflicts between container managers
* Solution: Usernamespaces allow creating a separate range of valid UIDs/GIDs within the namespace, helping ensure non-overlapping maps and reducing potential conflicts
* Benefits: Simplifies container management, decouples user IDs from file system, and allows for 64-bit UID/GID support
* Demonstration: Creating a new user namespace, setting UID/GID mappings within the namespace, and testing file creation and interaction with processes outside the namespace.
* Challenges: Ensuring compatibility with existing software that may not support 64-bit UIDs/GIDs and dealing with edge cases like interacting with external systems or handling nested namespaces.
* Other improvements: ID mapping mounts, QR code patch for easier container management, and VFS ID map integration.


## In Containers We Trust? Building Trust in Containerized Environments - Avery Blanchard

URL: [https://www.youtube.com/watch?v=g6uJaGEXUGA](https://www.youtube.com/watch?v=g6uJaGEXUGA)

 * Avery Blanchard is a first-year PhD student at Duke, discussing containerized environments and building trust
* Containers are popular due to scalability and lightweight design, but trust is often blindly given
* Trust in containers can be built using chain trust, which includes:
  + Hardware (TPM)
  + Individual container instance measurements
  + Verifying software component boot process
  + Cryptographic hash recorded in TPM registers
* Linux IMA (Integrity Measurement Architecture) is used to extend measurement throughout runtime for file integrity detection
* Goals of IMA: detect malicious or accidental changes, measure application execution
* TPM evidence is given to remote verifier for container attestation and decision making
* Current challenges include:
  + Scalability with many containers running
  + Name space identification and support for measurement in containers
  + Size issues with IMA
* Merkle trees can be used to show file content and potentially add metadata, but visibility into the file system is needed.


## Fuse mounts recovery and Checkpoint/Restore - Aleksandr Mikhalitsyn, Stéphane Graber

URL: [https://www.youtube.com/watch?v=ob5lraiXXVg](https://www.youtube.com/watch?v=ob5lraiXXVg)

 * Aleksandr Mikhalitsyn and Stéphane Graber discussed FUSE (Filesystem in Userspace) mount recovery
* Motivation: single point failure of FUSE demon, different storage solutions use FUSE, mounting FFS file system inside container is forbidden
* Approach: implement tool to reset internal state of FUSE mount, keep connection and restore mount stuff
* Challenges: dealing with fuse request, dentry revalidation mechanism, bind mount issue
* Solutions: dentry validation call back, extending FUSE algorithm, iode number problem, NFS state recovery comparison
* Conclusion: implementing recovery state in FUSE might be a bigger engineering effort, exploring alternatives like BPF program to keep track of file system state.


## Cgroups and Enterprise Users - Kamalesh Babulal, Tom Hromatka

URL: [https://www.youtube.com/watch?v=V4ppj3hY78M](https://www.youtube.com/watch?v=V4ppj3hY78M)

 * Kamalesh Babulal and Tom Hromatka discussing Cgroups and Enterprise users
* Cgroups support in Linux kernel since 2008, with V2 version controller added in 2015
* Cgroup V2 supports parity and freezer, and is considered stable for enterprise use
* Enterprise distributions may take a long time to adopt new cgroup versions due to long-term application support and certification processes
* Python binding available for managing Cgroups programmatically
* Cgroups allow managing complex hierarchies with multilevel nested groups and threaded mode
* Systemd does not support CPU setting directly in Cgroups, but there are workarounds using cgroup v2 hybrid mode or delegated cgroups
* Challenges with migrating from Cgroup V1 to V2 include maintaining different versions within applications and handling configuration changes
* Single writer rule simplifies requirement for writing cgroup hierarchies, but can lead to wasted CPUs in some cases
* Delegation support via CLI, C code, and Python was added to Cgroups to help with migration
* Systemd is planning to contribute to Cgroup V2 development
* Some distributions are shipping older images that no longer boot due to the removal of Cgroup One support
* There is ongoing discussion about supporting transient units in system D and how it relates to Cgroups.


## Protecting Sensitive Data in Container Checkpoints - Adrian Reber, Radostin Stoyanov, Wesley Armour

URL: [https://www.youtube.com/watch?v=PIlTA7H_87o](https://www.youtube.com/watch?v=PIlTA7H_87o)

 * Adrian introduced encryption mechanism for container checkpointing in Kubernetes to protect sensitive data
* Bor system encrypts checkpoint and saves it as a tar archive, but has performance overhead and key management issues
* Cre tool allows encrypting checkpoints by modifying container engine and adding encryption primitives
* Encryption can be applied to different types of images (prot image, row image, U memory page) using different ciphers
* Checkpointing mechanism works by creating a configuration file, encrypting tar archive, and decrypting it during restoration
* Encryption provides authentication and confidentiality, but restoration is more complicated than encryption
* Iterative checkpointing allows decrypting individual memory pages efficiently
* XTC is a suggested tool for implementing efficient encryption in container engines
* Different types of workloads require different encrypted image formats (OCA, symmetric keys)
* Memory page protection can be used to exclude sensitive information from checkpoints
* Iterative checkpointing allows applications to use streaming encryption and preserve the ability to decrypt content during migration.

Note: The transcript is quite long and technical, so it's important to read it carefully to fully understand the concepts discussed.


## Closing session - Stéphane Graber

URL: [https://www.youtube.com/watch?v=aaFSlcHxeOA](https://www.youtube.com/watch?v=aaFSlcHxeOA)

 * Stéphane Graber is speaking at the closing session of Microcon
* He mentions that it's exactly 6 pm, indicating the end of the conference
* He thanks everyone for coming and expresses hope to see them next year
* He mentions that they will be going to dinner and drinks.


## Opening session - Daniel Borkmann, Jakub Kicinski

URL: [https://www.youtube.com/watch?v=ujGDZV3jPmo](https://www.youtube.com/watch?v=ujGDZV3jPmo)

 * Welcome to Lino Plumbers Conference 2023 Networking BPF Summit
* Three-day event with growing number of submissions and participants
* Goal is to drive the ecosystem and subsystem kernel forward
* Respect time limits during discussions
* Technical Committee and networking BPF track maintainers: David Jacob, Eric, Alexe, Andre Martin
* 30-minute sessions with discussion time
* Breaks: 30 minutes morning and afternoon, 90 minutes lunch
* Monday: Core BPF and BPF security use cases
* Tuesday: Kickoff BPF tracing and networking
* Wednesday: Whole day around networking (morning transport, afternoon container, miscellaneous)
* Starts officially at 9:30 AM on Monday, ends at 6 PM on Wednesday
* Sessions will be video-streamed and recorded for later viewing
* Fun session optional on Monday evening with Quenton presenting a fun book project.
* Sponsors acknowledged for making the event possible.


## Evolving the BPF Type Format - Alan Maguire

URL: [https://www.youtube.com/watch?v=JQ8LukUCryE](https://www.youtube.com/watch?v=JQ8LukUCryE)

 * Alan McGuire talks about evolving the BPF (Berkeley Packet Filter) type format
* Modern BPF has become central and vital for tracing, with functions like F entry and exit, compile once and run everywhere
* BTF (Berkeley Type Format) provides argument types and return values, giving informative tracing output and making development easier
* Potential debugger information is always available without the need to download large Dwarf packages
* The EBPF Summit discussed how BTF makes debugging more efficient and solves performance issues within a five-day timeframe
* The challenge is ensuring BTF availability, as it can sometimes be embedded in VM Linux images, causing bloat or invalidation of the BTF module
* Splitting the BTF module representation from the core VM Linux image is suggested to avoid these problems
* The use of IDs and remapping is also discussed as a solution to prevent tooling issues when building modules
* Other usability issues, such as optimization during kernel builds and dealing with ambiguous function names, are also addressed.


## Exceptions in BPF - Kumar Kartikeya Dwivedi

URL: [https://www.youtube.com/watch?v=5mM9vTUPQdI](https://www.youtube.com/watch?v=5mM9vTUPQdI)

 * The speaker, Kumar Kartikeya Dwivedi, is a first-year PhD student at EPFL and has contributed to BPF for several years.
* He will be talking about exceptions in BPF, which was recently upstreamed.
* Exceptions allow aborting execution and returning control back to the kernel.
* They are similar to Panic or terminate APIs in Rust and C.
* In BPF, a program can throw an exception by calling `BPF_THROW`.
* The cookie parameter is used and can be overridden to change the return value.
* If an exception is thrown, the exception call back program is invoked to decide the return point.
* Verifier follows the program path and checks for VPF calls.
* Use cases include assertions, resource management, and error handling.
* Assertions can be used to update verifier knowledge with scalar values.
* Call sites can have exception handlers that catch exceptions and execute callbacks.
* The verifier keeps track of frame descriptors to unwind the stack and release resources upon program abortion.
* Global and static subprograms have different verification requirements.
* Landing pads are used to describe the behavior of the compiler when a throw exception occurs.
* Catching exceptions in frames can be useful for propagating exceptions through the call stack.
* The speaker mentions his work on integrating SCTX for handling user-space pointers and exception primitives for simplifying safety property enforcement.
* BPF exceptions allow getting rid of complexity and reducing termination overhead while ensuring basic safety properties.
* The verifier cannot reason about loop termination, so cancellation semantics can be used to enforce iteration logic, data structures, and memory management.
* Three new primitives have been added: `BPF_OBJECT_NEW`, `BPF_LINGLIST_MANAGED`, and `BPF_ARBITARY`. These help manage kernel resources and memory while keeping the verifier reasoning simpler.


## When BPF programs need to die:  exploring the design space for early BPF... - Dan William, Raj Sahu

URL: [https://www.youtube.com/watch?v=To6TyllXSEE](https://www.youtube.com/watch?v=To6TyllXSEE)

 * BPF (Berkeley Packet Filter) is a powerful and versatile technology used for hooking and modifying kernel functions
* BPF programs are guaranteed to terminate, but in some cases, early termination may be desirable or necessary
* Two use cases for dynamic termination: observability tools and BPF orchestrators
* Challenges with dynamic termination include memory leaks, deadlocks, and the inability to kill running BPF programs
* Explicit approach to dynamic termination involves adding explicit flags or checks to helper functions and using a cleanup mechanism
* Implicit approach proposes leveraging the fact that the BPF verifier already performs some cleanup steps when a helper function returns
* The presentation discusses advantages and limitations of both approaches, as well as potential issues with managing complex BPF programs and ensuring memory safety.


## Verifying the Verifier eBPF Range Analysis Verification - Harishankar Vishwanathan

URL: [https://www.youtube.com/watch?v=A_5UXLeQdfI](https://www.youtube.com/watch?v=A_5UXLeQdfI)

 * Hari from Rgar University discusses eBPF Verifier and its importance in ensuring safety and security in the eBPF ecosystem.
* AG-based formal verification tool is used to check correctness of static analysis results reported by eBPF verifier.
* The tool automatically generates proof concepts to demonstrate mismatches between concrete eBPF bytecode semantics and abstract verifier semantics.
* eBPF verifier focuses on value tracking analysis, which tracks program variables and their values across execution.
* It uses abstract domains such as the bitwise domain and range domain to approximate actual values and make reasoning sound.
* The refinement formal method is used to improve precision of analysis by updating results in another domain.
* eBPF verifier supports various types of arithmetic logic operations and jump instructions, but adding support for jump instructions can be difficult.
* Synthesizing proof concepts can take a significant amount of time and resources.
* The tool can generate false positives, so it's important to manually review the results to identify actual bugs.
* Developers are encouraged to use eBPF verifier to ensure kernel static analysis is sound with every commit.
* The tool performs verification on the C logic of the eBPF program and can detect well-formedness violations, such as invalid ranges or missing flags.
* It's important for developers to provide feedback on the tool to improve its effectiveness and reduce verification time.
* The future direction for eBPF verifier includes support for parallel verification, profiling verification, and ensuring code extraction from C logic.
* Integrating eBPF verifier with CI systems can help automate the verification process and make it easier for developers to use.


## BPF Memory Model Two Years On - Paul McKenney

URL: [https://www.youtube.com/watch?v=qDDZVWmv8W0](https://www.youtube.com/watch?v=qDDZVWmv8W0)

 * Paul McKenney discussed BPF memory model two years after his last talk
* PS ABI defines things for compiler writers to generate BPF code
* Strict subset of Linux internal memory model with promise ordering
* Needed to address concurrently sharing data between different places: multiple BPF programs, user space programs, helper kernel code
* Jose Marchesi suggested formal memory model for BPF instruction set
* Compiler writers want to know precisely what memory model generates proper code
* Atomics are used to make explicit tooling and compiler JIT take full advantage of implicit memory model in BPF instruction set
* Atomic instructions: exchange, compare-exchange, load, add/exor, fetch-combination
* Load and store instructions have ordering semantics, ensuring consistency across the whole system
* Linux kernel prefers to use relaxed compare-exchange put with full memory barrier for ordering
* Jump instruction ordering semantics can be strange on various architectures
* Control dependency is important for compiler optimization, but fragile and easily broken
* Avoid storing better thing before a statement that might follow it (broken dependency)
* Control memory model in Linux also relies on coding restrictions and control dependency to maintain order
* Different architectures handle control dependency differently, so be careful
* Atomic instructions provide strong ordering for CPUs, but they have limitations and are not always the best choice for scalability
* Memory instruction ordering involves single variables and may not be ideal for large-scale systems
* Linux kernel supports various memory models, including Tianium's volatile memory model, which provides heavy ordering for certain instructions.


## Overflowing the kernel stack with BPF - Dan Williams, Sai Roop Somaraju,  Siddharth Chintamaneni

URL: [https://www.youtube.com/watch?v=9id98jARhMQ](https://www.youtube.com/watch?v=9id98jARhMQ)

 * The speakers discuss issues with Extended Berkeley Packet Filter (EBPF) programs and their interaction with the kernel stack.
* EBPF assumes a small stack usage for helper functions, but BPF programs can consume large amounts of stack space through nesting and tail calls.
* Two critical assumptions made by the runtime verifier are: 1) there is always 8 kilobyte (KB) stack space available for BPF programs, and 2) total size of BPF program + helper function call stack is less than 8 KB.
* The first issue encountered was around attachment and nesting: when attaching a BPF program to an unclean stack, the XFS file system can grow the stack significantly, leading to potential overflow.
* A limitation approach to prevent nesting is using global variables or trace point restrictions, but this can be overcome by using BPF trampoline type programs.
* The second issue was around uncontrolled nesting and stack switching: when multiple BPF programs call each other's helpers recursively, it can lead to a stack overflow.
* Possible solutions for the first problem include ensuring kernel runtime accommodates the required stack space or providing a new stack for BPF programs with new stack-based memory requirements. For the second problem, limiting nesting points and asking for more stack space when needed are potential solutions.
* Other topics discussed included user space demons inserting BPF programs, analyzing kernel process stack usage, and using alternatives to BPF tail calls.


## BPF for Security and LSM updates - KP Singh

URL: [https://www.youtube.com/watch?v=vfIiXcIelEY](https://www.youtube.com/watch?v=vfIiXcIelEY)

 * KP Singh from Google spoke about his experience implementing BPF (Berkeley Packet Filter) for Linux Security Modules (LSM)
* He picked the "safe set ID" LSM as the simplest one to implement and faced several challenges during development
* He discussed issues with dynamic array sizes in inner maps, ref counting, and verifier errors
* He suggested using annotations in Clang, acquiring and releasing semantics for kernel functions, and carefully handling zero maps
* He mentioned productivity improvements with Andres Lippa's BPF bootstrap method and the use of a Loop iterator
* He shared his experiences on dealing with various errors and the importance of understanding BPF internals and kernel code.


## BPF_LSM + fsverity for Binary Authorization - Song Liu, Boris Burkov

URL: [https://www.youtube.com/watch?v=jAQ9d90V12M](https://www.youtube.com/watch?v=jAQ9d90V12M)

 * Binary Authorization: ensuring trusted binaries perform critical operations
* Two solutions proposed: IMA and Fsverity
* IMA (Integrity Measuring Architecture): complicated, designed for secure boot, not flexible enough for binary authorization
* Fsverity: built-in signature feature, uses Merkel tree hashing for file integrity checking
* Fsverity advantages: faster than reading whole files, can handle random read failures, powerful
* Disadvantages: cannot protect against hash manipulation or bypassing the signing service
* Proposed framework: use Fsverity for checksum integrity, BPF LSM (Linux Security Module) for policy enforcement
* Use case: prevent unauthorized binary access, update binaries without rebooting, smaller attack surface
* Implementation: sign binaries with a dedicated server or hardware like TPM, use BPF LSM to enforce access control
* Hook: access file, check signature against allow list in local storage, block if not matched
* Challenges: handle overlay file systems, avoid recursion issues with LSM hooks, ensure security in the BPF space.


## Sysarmor Metas eBPF Security Detection and Enforcement Tool- Liam Wisehart, Shankaran Gnanashanmugam

URL: [https://www.youtube.com/watch?v=K3YAqbW9F68](https://www.youtube.com/watch?v=K3YAqbW9F68)

 * Shankaran from Meta discusses Sysarmor Metas, an eBPF-based intrusion detection and prevention tool
* Problem statement: Meta collects data from billions of users daily, risk of cyber threats is high, need a strong intrusion reduction solution to prevent advanced threats in real time with low performance impact
* Si Armor is Meta's solution built using eBPF primarily, provides coverage for various use cases like hardware networking, system call privilege escalation, file monitoring, access control, and task process monitoring
* Si Armor uses BPF hooks to execute rule policies inside the code for high performance and can be highly configurable
* Use cases: Access control for sensitive data, prevention of unauthorized process invocation, detection based on container information, network access protection, and file operation prevention
* Si Armor supports response remediation flows, event flow offline pipeline, and automates deduction-based remediation steps
* Performance optimization features include tracking BPF memory and CPU utilization, and minimizing impact on the system by using elapse time and making decisions based on CPU time given to a program
* Examples of use cases discussed: Access control for sensitive data, prevention of unauthorized process invocation, and network traffic monitoring.


## Extending Non-Repudiable Logs with eBPF - Avery Blanchard, George Almasi

URL: [https://www.youtube.com/watch?v=jw7f_5Pz07A](https://www.youtube.com/watch?v=jw7f_5Pz07A)

 * Avery and George discuss extending non-repudiable logs using eBPF at IBM research
* eBPF is a large visibility system with various hooks available across kernel subsystems
* Non-repudiable logging allows verifying log integrity, ensuring trust in the system state
* Trust is built starting from the chain of trust during system boot using cryptographic measurements and hashes
* TPM (Trusted Platform Module) microcontroller is used to authenticate system configuration and ensure platform integrity
* IMA (Integrity Measurement Architecture) measures software components and logs PCR register values, providing a verifiable chain of trust
* eBPF programs can measure log output and store measurements in the kernel for verification
* IMA and eBPF can be used together to measure individual application containers and build trust in their environment
* Extending measurement throughout runtime allows measuring applications as they execute
* TPM is used to verify system integrity by providing evidence and attesting machine's state
* The process involves the relying party sending a challenge, the machine sends evidence, and the engine verifies it
* Non-repudiable logging using eBPF programs allows measuring log output from kernel modules and extending PCR values
* eBPF programs can be used to interact with TPM for hardware evaluation
* Virtual TPMs may have different performance characteristics compared to real TPMs, but they can be faster in some cases
* The use of a flexible logging format is important when dealing with large systems
* Additional patches and changes to the kernel might be required for implementing non-repudiable logging solutions
* Systemd journal and other log solutions can also provide attestation capabilities, but may have different performance characteristics.


## Advancing Kernel Control Flow Integrity with eBPF - Jinghao Jia

URL: [https://www.youtube.com/watch?v=LL0tDFQ1Ogk](https://www.youtube.com/watch?v=LL0tDFQ1Ogk)

 * Jinghao Jia discussing advanced kernel Control Flow Integrity (CFI) using eBPF
* Traditional CFI techniques like Kernel Control Flow Integrity (KCFI) have limitations, such as requiring static policies and kernel reboots for policy changes
* eBPF offers flexibility with runtime context and easier deployment of dynamic policies
* Two approaches to implementing eBPF-based CFI: Kprobe and Fprobe
* Kprobe attaches directly to function entry or return points but suffers from significant overhead and coverage limitations
* Fprobe uses a probabilistic approach based on function entry and synchronous invocation, which is more efficient in terms of interrupts and covers indirect calls
* EK CFI is a new framework that hooks evm programs onto indoor calls and performs synchronous invocations for policy checks, ensuring control flow integrity with low overhead.


## Modernizing Android BPF and the Android Security Model - Neill Kapron

URL: [https://www.youtube.com/watch?v=UM_tnuZhmt8](https://www.youtube.com/watch?v=UM_tnuZhmt8)

 * Neil Kapron from Android kernel Integrity team discusses modernizing Android's BPF (Berkeley Packet Filter) and security model.
* Goal is to enable core functionality of modern BPF, join the Century BPF project, and contribute back upstream.
* Android has a unique standard C library called bionic and a dedicated uid for system and user combination as security mechanisms.
* Two kernel versions per release, latest being Android 14 with 515 kernel branch (61 behind), and the challenge of older device upgrades to newer OSs.
* Interested in Kernel Mode Integrity (KMI) ABI stability mechanism.
* Older devices may have deprecated architecture support like armv7, which poses a risk for future Android versions (DRM 564).
* Goal is to allow vendor access to BPF while maintaining security restrictions.
* Challenges include boot time issues, memory overhead concerns, ABI compatibility, and kernel user space BPF object independence.
* Proposed approach: native BPF loader for developer/system integrator flexibility and access control mechanism in kernel space.
* Need a scalable solution for handling access to BPF programs and attach points.
* Considering a gatekeeper application token-based access control system.
* Long-term plan is to extend access control beyond LSM (Linux Security Module).
* Discussed the challenges of backporting new patches, adding kernel access control, and using LSM hooks for improving security.
* Recommendations: use libbpf for embedded applications, enable Read-only Trace Points for performance reasons, and investigate using hooks for better control.
* Vendor-requested type sharing and performing Trace Point observability were mentioned as open questions.


## Buzzing Across Space: The Illustrated Children’s Guide to eBPF - Quentin Monnet

URL: [https://www.youtube.com/watch?v=-Z0Z1H6a_qI](https://www.youtube.com/watch?v=-Z0Z1H6a_qI)

 * Quentin Monnet, author of the children's book "Buzzing Across Space: The Illustrated Children’s Guide to eBPF"
* Written in simple language for children, explains eBPF concept
* Inspired by existing books on Kubernetes
* Explanation uses a story about Captain Tux and his Starship
* Captain Tux carries cargo between planets, encounters challenges during repairs
* Needs help from EB, a small bee, to translate instructions for a special device
* eBPF used for defense and security on the Starship
* Passengers help improve the trip experience by optimizing communication
* XDP improves networking and observability
* Beast, an evil ship, tries to steal technology and destroy things
* eBPF used to defend the Starship and optimize laser performance
* Map component helps manage ship location
* Conclusion: eBPF is everywhere in space, spreading efficiency and flexibility in programming.


## Resolve and standardize early access to hardware for automotive industry with Linux - Khasim Syed

URL: [https://www.youtube.com/watch?v=RZr79yCroqs](https://www.youtube.com/watch?v=RZr79yCroqs)

 * Speaker, Khasim Syed, started working on Linux device drivers at TI in 2002
* He has contributed to various open source projects including bigle boardorg and Linaro
* Saw a need for open source hardware and open community platforms in the automotive industry
* Proposed using Linux as a solution for safety-qualified and compliant software, but faced challenges with safety certification and performance requirements
* The challenges included fault tolerance and boot time
* He observed that the automotive industry is moving towards electric vehicles and power management is crucial
* He suggests using Linux for its power management solutions and open source collaboration model
* Discussed the importance of standardizing and collaborating on bootloaders to meet safety certification requirements
* He also touched on the need for cost-effective solutions for two-wheeler clusters and remote Pro driver support in Linux
* He expressed a desire for more standardization and collaboration within the Linux community and automotive industry.


## Rust for Linux - Miguel Ojeda

URL: [https://www.youtube.com/watch?v=qvlgIaYrd3g](https://www.youtube.com/watch?v=qvlgIaYrd3g)

 * Miguel Ojeda discussing the growth and progress of the Rust for Linux community
* Community growing with over 8000 messages on the mailing list last year
* New members joining, such as Beno working on pin API, Andreas on mvme driver, and Alice on Android binder driver
* Companies like Isrg, Ssung, and Cisco showing interest and support for Rust in Linux development
* Discussion of maintaining Rust subsystem in the Linux kernel and challenges involved
* Long-term plan for Rust compiler support in distributions like Ubuntu
* Mention of the Rust Codex project and its potential to simplify contributing to Rust projects
* Ongoing efforts to improve performance and reduce compile times with GCC Rust integration
* Discussion of potential issues with compatibility, maintenance burden, and abstraction in Rust development for Linux.


## Beginner Linux kernel maintainers toolbox - Krzysztof Kozlowski

URL: [https://www.youtube.com/watch?v=doUuj1qCggY](https://www.youtube.com/watch?v=doUuj1qCggY)

 * Krzysztof Kozlowski, Linux kernel maintainer for device binding, shares tips and tricks for improving workflow as a beginner Linux kernel maintainer.
* He discusses his role in reviewing patches and dealing with pool requests, mentioning the importance of sending lots of patches.
* He notices patterns in how patches are handled and suggests ways to improve the process, such as using automation tools like integration trees and patchwork.
* He talks about common issues like patches being lost or receiving no response and offers solutions like resending patches or pinging maintainers.
* He also discusses the importance of transparency in the Linux kernel development community and the role of tools like GitHub and patchwork in the process.


## Speeding up Kernel Testing and Debugging with virt-meng - Andrea Righi

URL: [https://www.youtube.com/watch?v=SeOg6KR07to](https://www.youtube.com/watch?v=SeOg6KR07to)

 * Andrea Righi from Canonical's kernel team discusses the challenges of testing and debugging kernels, particularly with custom patches and different architectures
* Virtualization using tools like virt-meng can help speed up the process by creating a virtual copy of the system for testing without requiring redeployment or reboots
* Virt-meng allows for live snapshots, fast reboots, and efficient file system sharing (VerFS) between host and guest
* VerFS provides better performance by exchanging actual IO semantics using shared memory areas and the FUSE protocol
* Other improvements include faster boot times, support for microVM architecture, and reimplementing init scripts in Rust for improved maintainability and performance.
* The goal is to create a more efficient testing workflow that saves time, reduces distractions, and attracts newcomers to kernel development.
* Additional points discussed include power consumption reduction using virt-meng, supporting systemd, improving support across distributions, and adding features like live patching and module binding.


## Emulating NT synchronization primitives in Wine - Zeb Figura

URL: [https://www.youtube.com/watch?v=NjU4nyWyhU8](https://www.youtube.com/watch?v=NjU4nyWyhU8)

 * Zeb Fera discusses the problem of emulating Windows synchronization primitives in Wine, which is slower than expected
* Wine is a free software project that reimplements the Windows API in user space on Linux
* The challenge is implementing synchronization primitives such as events, mutexes, and semaphores, which can be complex to map to Linux equivalents
* Modern games with high parallelism and frequent synchronization calls are causing performance issues
* One solution could be a kernel-based implementation, but it would involve managing shared state across multiple processes and adding complexity to the Wine server
* Windows uses pulse events, which wake up threads even when they're not waiting, adding unnecessary overhead
* Event FDs (file descriptors for event handles) were implemented in user space but have performance issues with polling and pulsing
* A variation of futexes was tried but still had issues with ordering and pulsing
* Implementing a kernel driver to handle the weight operations directly was considered but was complicated and required taking internal locks on both the Wine server and the Linux kernel
* The event FD, futex, and vector implementations all have their advantages and disadvantages and no single solution works perfectly for all cases
* The goal is to find a user space solution that can match or exceed the performance of the Windows implementation while being more efficient than the current Wine server implementation.


## Optimizing sysfs and procfs - Ajay Kaher, Vamsi Krishna Brahmajosyula

URL: [https://www.youtube.com/watch?v=IPgvvTwN5V8](https://www.youtube.com/watch?v=IPgvvTwN5V8)

 * Agenda: Optimizing sysfs and procfs using CFS (Common File System)
* CFS is a file system that leverages the kernel object file system to allow user space tuning of different attributes
* Two-layer implementation: shared VFS layer, CFS Kernel FS (borrows code from VFS), CFS manages file I/O binding
* procfs also uses a two-layer implementation: shared VFS layer, and exposes process internal data
* Accessing a path in CFS: check whether the iode represents the path, find registered read operation, unlink file and add corresponding iode to lru list
* Problem statement: retain many Inodes in memory leading to high memory usage
* Proposed solution: don't cache Inode D entries (Dentry cache) in CFS and procfs
* Benefits of not caching Inode D entries: reduces overall memory requirements, faster boot time, and fewer system calls.
* Comparison between current implementation and proposed solution: 
  - Current implementation: retains all Inodes in memory, increases boot time (814s to 3s) and number of system calls (10K to 45K)
  - Proposed solution: frees unnecessary Inodes from the cache, reduces boot time (860s), and number of system calls (843s)
* Experiment results: dropping CFS procfs Inode D entries at boot significantly reduces memory usage (12MB vs. 18MB).


## Powering up "discoverable bus-attached" devices on DT-based platforms - Abel Vesa

URL: [https://www.youtube.com/watch?v=ZMAMC9KaEzI](https://www.youtube.com/watch?v=ZMAMC9KaEzI)

 * Abel Vesa from Linaro talks about powering discoverable bus-attached devices on DT-based platforms
* Discoverable bus devices require power when discovered, but DT platforms don't provide power automatically which can impact power consumption
* Specific use case: WiFi and Bluetooth on Lenovo ThinkPad X390
* Problem is with the order of enabling regulators for WiFi and Bluetooth chips
* Proposed solution: power sequencing subsystem to abstract power operations for consumers
* USB onboard hub can be used as a reference, but different devices may require specific power sequences
* The PCI hotplug driver could be improved to handle every device that is PCI-attached more efficiently
* Powering a WiFi or Bluetooth device before its discovery can solve the issue, but it's not always possible due to power management considerations.


## Improving kexec boot time - Usama Arif

URL: [https://www.youtube.com/watch?v=M-1AIT9mLS4](https://www.youtube.com/watch?v=M-1AIT9mLS4)

 * Speaker is from Colle McLeod team, discussing ways to improve Kexec boot time in private and public cloud environments.
* Motivation: Host environment change and kernel updates can result in long downtime for virtual machines, but updating host kernels brings security and performance benefits. Alternative methods like live patching and live migration have their own challenges.
* Live migration process: Moving a running VM to another physical host without causing much disruption. Advantages include dealing with physical hardware issues on the source host instead of trying to update it, and avoiding the need for extra resources or machines. However, it comes with challenges like network bandwidth requirements, complexity, and potential performance impact on virtual machines during migration.
* Performance impact on virtual machines: Post-copy live migration can cause virtual machines to access pages that are yet to be transferred to the target host, resulting in page faults and slow application response. This issue can add significant time to the overall downtime during live updates.
* Optimization methods: Deferred struct page initialization, optimized SP boot, parallel SMP boot, huge Pages reservation, and skipping Purgatory (a Kexec component for checking kernel image integrity).
* Struct page initialization optimization: Enabling deferred initialization of certain structures to reduce the overall time taken during boot.
* SP boot optimization: Linux kernel's 64-bit CPU support and state machine division to improve boot speed.
* Parallel SMP boot: Enabling parallel boot for multiple processors to decrease boot time.
* Huge Pages reservation: Reserving huge Pages for applications that require large amounts of memory to improve boot time but may result in memory fragmentation.
* Skipping Purgatory: Disabling the Purgatory check in the Kexec boot process can save around 200ms, although it may pose security concerns and should be tested before implementation.
* Future work: PCI device white list/blacklist, power management optimization, and persistent kernel memory for passing information across old and new kernels to eliminate unnecessary PCI probing.


## Security Features status update - Kees Cook, Qing Zhao, Bill Wendling

URL: [https://www.youtube.com/watch?v=OEFFqhP5sts](https://www.youtube.com/watch?v=OEFFqhP5sts)

 * Speaker is discussing security features in the toolchain, specifically focusing on Rust and C/C++
* Issues with arithmetic overflow handling in sanitizers, need to figure out a solution
* Progress on dealing with array bound checking and stack protector guard location
* Discussion of Edge CFI (Control Flow Integrity) and its hardware and software support
* Hardware support for CFI is coarse-grained, software control implementation using function prototypes
* Clang and GCC still need work to fully support CFI
* Discussing potential improvements to dynamic object size estimation and data dependence analysis in GCC
* New TCC internal function introduced to carry data dependence information and prevent incorrect transformations by the compiler
* Implementation of counted attribute for arrays in GCC, allowing reporting of actual array bounds
* Clang making progress on similar implementation for dynamic object size and addressing data dependency issues
* Future work includes extending counted attribute to flexible array members and integrating bound information into the type system for a more type-safe C language.


## Synthesized CFI for hand-written assembly in GNU assembler - Indu Bhagat

URL: [https://www.youtube.com/watch?v=rdvGt7kmYh4](https://www.youtube.com/watch?v=rdvGt7kmYh4)

 * The speaker is discussing the synthesis of Call Frame Information (CFI) for hand-written assembly in GNU assembler.
* CFI generates stack unwind information, allowing recovery of the Canonical Frame Address (CFA) and saving register assumptions.
* Gas implementation relies on CFI-ABI conformant code.
* Speaker mentions constraints for kernel use case and usefulness in both general kernel and user space.
* Discusses generating CFI automatically and the potential impact of non-conformant code.
* Speaks about the current state of support for x86 and future plans for AR64.
* Mentions the permissibility criterion and challenges such as complex control flow, untraceable control flow, and indirect branches.
* Talks about the importance of asynchronous stack unwinding awareness and DWARF expressions for recovering CFA.
* Discusses the need for explicit code to handle CFI save/restore registers in a symmetric way and the potential for warnings when using dynamic stack allocation.
* Speaks about the advantages of full coverage assembly, handling compiler-generated code, and dealing with new instructions or control flow patterns.
* Mentions the fragility of configuration files and the importance of explicit annotations.
* Talks about the need to honor manual annotations, the role of speculative optimizations, and the limitations of automatic tooling in some cases.
* Discusses the potential for turning per-function assembly directives on/off, using different CFI modes, and handling call boundaries.
* Mentions the need for toolchain support and the ability to infer or exclude CFI based on compiler attributes or command line flags.
* Talks about the importance of handwritten assembly validation features and the role of autogenerated CFI in identifying bugs.
* Suggests that obtool reverse engineering control flow graphs and GCC-compiled files could be useful for kernel development.
* Expresses a personal opinion that kernel maintenance and ARM64 support are important areas to focus on.
* Discusses the need for call-ahead time, the differences between static and dynamic generation of CFI directives, and the use of native assembly.
* Talks about the benefits of explicit annotations for handling unusual cases and the ability to put CFI inline using assembler macros or tools like colonel source.
* Mentions the need for simple straight-line code when dealing with common term instances and xtable-style exceptions, and the potential for manual annotation in more complex cases.
* Speaks about the importance of understanding implicit control flow and handling static calls and branches, as well as dealing with clobbered link registers and alternative branch instructions.


## Graph-based ABI analysis for fun and profit - Matthias Männich

URL: [https://www.youtube.com/watch?v=_299mcYiu3U](https://www.youtube.com/watch?v=_299mcYiu3U)

 * Matthias Männich from Google Android system team in London discusses AI monitoring in Android and Linux kernel
* Team focuses on stability, reducing fragmentation, and ensuring API stability for production devices
* Traditional ABI (Application Binary Interface) monitoring involves comparing dwarf type information at build time to detect changes
* CTF (Compile Test Format) and BTF (Binary Type Format) are alternatives to dwarf for extracting type information
* Comparing whole distributions instead of individual binaries is a new approach being explored
* Facebook uses BTF effectively in their production environment, but it's challenging to create a comparison algorithm for large, complex graphs
* Creating a library to facilitate BTF-based ABI comparison using strong component algorithms is under research
* Linux kernel build time is held back by issues like header dependencies, indirect includes, and macro expansion
* Automated header refactoring and precompiled headers are used to speed up build times
* The talk covers various methods for improving kernel build times, such as automated include way, mod post, and kbuild tree improvements.


## Compiling for verified targets BPF - Jose E Marchesi

URL: [https://www.youtube.com/watch?v=B6VApkaY86w](https://www.youtube.com/watch?v=B6VApkaY86w)

 * The speaker is discussing the challenges of compiling BPF (Berkeley Packet Filter) programs using GCC (GNU Compiler Collection).
* Goals include achieving parity with Clang, generating verifiable code, and optimizing compilation.
* BPF imposes peculiarities on the compiler due to its architecture and requires a specialized toolchain.
* Verifier development cycle involves writing PPF (Parallelizable Pipeline Function) program, compiling BPF assembly code, loading it into the kernel, getting verified, and executing it.
* Two approaches for optimizing compilation: 1) Optimizing compiler generating verifiable code and 2) Disabling optimization and allowing users to generate their own verifiable code.
* Challenges include ensuring source constructs are verifiable, managing large programs, and dealing with optimization passes that can introduce unverifiable code.
* GCC generates BPF code back end and handles many use cases but might not be optimal for all scenarios.
* A more granular approach involves intercalating additional passes to undo previous transformations or hooking generic passes specifically for the BPF back end.
* Adding a new option called Minos can help balance performance, size, and verifiability.
* Pragmas can be used to convey information to the compiler about bounds and loop optimizations.
* Verifiable code can be generated by using annotations in source code and having the verifier use them during compilation.
* BPF stuff like loops and arrays could benefit from variable tracking and bound checking, making the compiler verifiable.
* Verifiable pragmas don't convey anything to the verifier object file directly.
* Optimizing compilers can be used to generate more predictable and verifiable code.
* Assembler support can help detect potential issues at assembly time to prevent verification issues.
* The combination of various approaches is likely to lead to an effective solution for generating verifiable BPF code using GCC.
* Tools like Clang and GCC need to improve their coordination for supporting BPF generation.
* LVM (Linux Virtual Machine) might have a longer review process on GitHub.


## Towards data type profiling - Namhyung Kim

URL: [https://www.youtube.com/watch?v=gkoaTJlFvMI](https://www.youtube.com/watch?v=gkoaTJlFvMI)

 * Namhyung Kim discussing data type profiling for precise memory access profile
* Goal is to see frequently accessed data types and field structures
* Two kinds of memory profilers: PMU sampling-based (targets memory access) and general memory access profile using information from PMU samples
* PMU memory sampling provides precise information on actual memory accesses, including data address and latency
* Intel and AMD support different levels of precise memory sampling functionality
* Heap memory allocation based profilers also useful for identifying memory leaks and uninitialized memory
* Discussed limitations of PMU-based profiling and other techniques like statistical profiling and instruction-based sampling
* Used an example to explain the process of running a program with a memory profiler, analyzing disassembly functions, and identifying memory locations using DWARF information.
* Mentioned challenges such as complex location expressions, union types, and handling different variable types during data access.
* Suggestions for improving tools included adding type information to the profiler, better support for split debug information, and optimizing code layout.


## VSCode for kernel development - Florent Revest

URL: [https://www.youtube.com/watch?v=nmYaSqe0fGg](https://www.youtube.com/watch?v=nmYaSqe0fGg)

 * Speaker introduces himself and mentions his background in C development
* He shares his experience of setting up Visual Studio Code (VSCode) for kernel development instead of using VI
* Improved setup leads to better reproducibility and interoperability between tools
* Mentioned benefits include: mailing list tool, build tool, and virtual machine tool
* Mail list tool example: Patchwork vs Git's email maintenance
* Build tool example: make vs cache usage
* Virtual machine tool example: Debootstrap and KVM
* Interactive workflow example using a bot bug process
* Discussed extensions like Kid Send Email, Patchwork, and testsh for various tasks
* Talked about the importance of automation and integrating tools in VSCode setup.


## Callsite Trampolines - Mr. Aleksei Vetrov,  Steven Rostedt, Suren Baghdasaryan

URL: [https://www.youtube.com/watch?v=jvJLmdXnZSw](https://www.youtube.com/watch?v=jvJLmdXnZSw)

 * Presenters are discussing Callide Trampoline, a memory profiling and call site analysis tool
* Motivation: need to account for memory allocation at call sites in Linux kernel
* Callide Trampoline injects small data structures into code to track memory usage and location of each call site
* Implementation details include using macro-based injection and static variables for call site data
* Discussion of challenges, such as upstreaming changes and name collisions with existing macros
* Proposal for a user space tool to monitor allocation information and performance issues
* Alternative approaches mentioned include using preprocessor macros or compiler plugins
* Concerns raised about potential performance overhead and invasiveness of the proposed solution
* Discussion of potential use cases, such as diagnosing memory leaks in large fleets
* Suggestions for improving the implementation, such as reducing invasiveness and improving naming conventions
* Discussion of potential benefits, such as easier debugging and better understanding of code behavior.


## Generating BPF Verifier Friendly Code with Clang - Yonghong Song

URL: [https://www.youtube.com/watch?v=aTKYJ7L67lA](https://www.youtube.com/watch?v=aTKYJ7L67lA)

 * BPF program written in C or assembly, eventually loaded into kernel
* Compiled with GCC, library called libbfd for processing relocations and creating object file
* Inside kernel, verification is crucial to ensure safety and prevent crashes
* Verification involves exploring every possible execution path and ensuring exit safety
* Verifier explores control flow graphs, maintains register state, and performs precise liveness analysis
* Verifier may need precise range scalars for conditional instructions
* Compiler can generate verifier-friendly code by checking certain patterns and emulating functionality
* Modifying source code to address specific verification failures is also an option
* Older kernels sometimes require improvements to the verifier, which can be backported
* Different approaches to generating BPF-friendly code include intrinsics, TTI hooks, and custom optimization passes.


## Welcome - Sasha Levin, Shuah Khan

URL: [https://www.youtube.com/watch?v=wRsuA7zUhk4](https://www.youtube.com/watch?v=wRsuA7zUhk4)

 * Welcome to the Colleague Dependability Testing Microconference
* Sasha is coordinating the conversation for a discussion on Cal dependability testing in the next year
* There are several presentations taking place at the microconference
* Sasha wants to start the conversation on Cal dependability testing.


## the path to achieve a bug-free build on the mainline - Philip Li

URL: [https://www.youtube.com/watch?v=jnKnBVxN0wQ](https://www.youtube.com/watch?v=jnKnBVxN0wQ)

 * Philip Li, Intel maintainer, discusses achieving a bug-free build on the mainline
* Current status: kernel botton green box test suit developed and maintained
* Three parts: current practice, challenges, and potential solutions
* Practice: testing in various stages of development flow, static analysis tools used to discover issues
* Challenges: false positives from static analysis, long-term bugs, build errors
* Solutions: bisection testing, collaboration with the community, reducing escape issues
* Bisection testing: finding issue cause early, continuously adding new tests, improving success rate
* Challenges: force positive detected static analysis issues, dealing with false positives, analyzing change logs
* Proposal: whole process improvement, checking whether issues are already resolved, effective bisection techniques.


## Storing and Outputting Test Information: KUnit Attributes and KTAPv2 -  Rae Moar

URL: [https://www.youtube.com/watch?v=5tIcfbGx69o](https://www.youtube.com/watch?v=5tIcfbGx69o)

 * Ry, from Google's Cunit team, presented on storing and outputting test information in KUnit and KTAPv2.
* Test information includes test results, test names, diagnostic data, and other supplemental information.
* Current test information is organized but lacks a systematic way to access or filter useful information.
* KUnit attributes can be used to save and output supplemental test information manually or automatically.
  * Two existing attributes are speed and module name.
  * A new attribute, Canan, is proposed for storing identifiable and parsable metadata.
* KTAPv2 is being developed to improve test information handling and include a specification for a line format with hashtag type-value pairs.
* The presentation covered several examples of useful test information, including speed tests and init data functions.
* Filtering and organizing test results based on useful information can make test runs faster and more efficient.
* The KUnit team is open to feedback and suggestions for improving test information handling in KUnit and KTAPv2.


## Quality in embargoed patches - Sasha Levin

URL: [https://www.youtube.com/watch?v=yEq8zaVNG6E](https://www.youtube.com/watch?v=yEq8zaVNG6E)

 * Embargoed patches have been a persistent issue since the Meltdown and Spectre incidents
* Embargoed code can break systems and cause significant problems
* Testing embargoed code extensively is difficult due to limited testing, documentation, and potential leaks
* Complexity of embargoed fixes and assembly code changes add challenges
* Intel and other hardware vendors have concerns about testing embargoed code due to NDAs and potential intellectual property issues
* Setting up dedicated test infrastructure for embargoed patches is being considered
* Ideally, hardware vendors or users running specific workloads could provide tests for embargoed patches
* A standardized testing infrastructure, such as Colonel CI, could help streamline the process
* Debian and other distributions have mechanisms for handling embargoed patches
* There are concerns around security and access to hardware for testing embargoed code
* Embargoed test suites may not catch all issues and new tests may need to be written
* Rolling out embargoed patches to large fleets of machines can be challenging due to potential leaks or complex failure scenarios
* Providing a machine for testing embargoed patches could be a potential solution, but keeping it alive and secure is important.


## Detecting failed device probes - Laura Nao

URL: [https://www.youtube.com/watch?v=vKsP6MCFLZk](https://www.youtube.com/watch?v=vKsP6MCFLZk)

 * Nicholas is discussing device probe regression issues in hardware block kernel drivers.
* Problems are not immediately detectable as there is no task for validating device platform probing.
* Approach to address this issue involves reporting unprobed device platforms and verifying device probing.
* Challenges include handling error codes differently, discerning probe failure from error logs, and addressing false positives.
* A separate test called boot RR is proposed for detecting device probe issues.
* The use of ACPI and EFI tests is suggested to describe hardware topology in a stable way.
* There is a need for a definition of discoverable bus devices for USB and PCI, as the current approach relies on statically defined lists.
* It's important to maintain a stable definition of hardware topology across reboots.
* There is a proposal for a carot tree generic structure for testing peripherals, but it doesn't include external devices.
* The discussion also touches on the importance of checking device probing in non-good kernels and dealing with firmware versions.
* A suggestion is made to add test metadata to make tests clearer and easier to understand.
* It's proposed to add test files inside a T test folder, matched based on device or platform compatibility.
* There is a discussion about the challenges of maintaining and keeping up-to-date a catalog of Upstream boards for automated testing.
* It's suggested that a script could be used to generate metadata files for parametized tests.
* The use of an extension overlay on device trees is proposed as a solution for maintaining discoverable information.


## Unifying and improving test regression reporting and tracking - Gustavo Padovan, Ricardo Cañuelo

URL: [https://www.youtube.com/watch?v=2kE1KuIJc0I](https://www.youtube.com/watch?v=2kE1KuIJc0I)

 * The speakers discuss the challenge of analyzing and reporting test regressions in a CI system that runs tests on different hardware and reports results differently.
* They mention the importance of improving the quality of regression data provided by the CI system, including adding more context such as kernel version, build information, and log analysis.
* The speakers suggest using machine learning algorithms to automatically categorize regression failures based on log data and find similar regression cases.
* They also mention the importance of having a feedback loop for infrastructure errors and providing useful information for maintainers and developers.
* The speakers discuss the need for collaboration between different teams to address regression issues, especially in the context of testing across multiple systems.
* They suggest implementing a permanent solution for data collection and analysis using a community-driven project like KernelCI or Lo Foundation.
* The speakers mention the importance of providing regression reports to different audiences with different perspectives, such as maintainers and developers.
* They discuss various techniques for investigating regression issues, including bisecting test results, analyzing logs, and using statistical analysis tools.
* They also mention the challenges of dealing with non-reproducible test failures and suggest using automated crash signature analysis to help identify the root cause of crashes.
* The speakers emphasize the importance of having a reliable and efficient regression testing system to minimize the impact on maintainers and developers.


## Welcome/intro - Mr Davidlohr Bueso

URL: [https://www.youtube.com/watch?v=aThCrI4s3qI](https://www.youtube.com/watch?v=aThCrI4s3qI)

 * David Lohr Bueso welcomes everyone to the CXL Micro Conference
* He mentions the sponsor and reminds attendees of the anti-harassment policy
* The event is structured with a presentation on state-of-the-art in driver related work coming up first
* Memory management will be discussed towards the end
* Encourages participation and questions from everyone present.


## CXL Emulation in QEMU - Progress, status and most importantly what next? - Fan Ni, Jonathan Cameron

URL: [https://www.youtube.com/watch?v=XcIlnXbXzs4](https://www.youtube.com/watch?v=XcIlnXbXzs4)

 * Fan Ni and Jonathan Cameron presenting on CXL emulation in QEMU
* Agenda: Discuss what's new since last year, current status, and future plans for dynamic capacity device emulation
* Dynamic capacity device emulation allows host to add or remove memory capacity without reprogramming the HDM decoder
* Supports volatile, non-volatile, static, and dynamic capacity backed devices
* Dynamic capacity regions are also configurable and support read/write access with validation
* Currently supports adding and releasing dynamic capacity extends using mailbox commands
* Host retrieves dynamic capacity region information and extend list to dynamically change add or remove extends
* QEMU uses a QMP interface for simulating the device and sending commands
* Discussion of missing features, such as support for volatile regions, shared extends, and tag-based operations
* Dynamic capacity extension release is not currently supported since tags are used actively
* Motivation for non-volatile support: make it simpler, more usable, and easily testable
* Fabric management (FM) is debated whether to emulate it directly in QEMU or leave it to the host
* Current CXL specification does not fully support dynamic capacity device emulation yet
* Dynamic capacity events are currently hard-coded and need to be generated dynamically based on extend lists and tags
* Future work includes fixes for issues related to multiple extending requests, response payloads, and host responses to dynamic capacity events.


## CXL Type-2 core support - Ira Weiny

URL: [https://www.youtube.com/watch?v=dwp9CGpiQLI](https://www.youtube.com/watch?v=dwp9CGpiQLI)

 * Ira Weiny proposed talk about CXL Type-2 core support, but there hasn't been much interest in the community
* Dan is the main maintainer of CXL core and has posted RFC work for Type-2 device support
* Splitting data structures in Upstream kernel allows better core support for accelerator usage
* Creating regions and managing address space for accelerators is needed to avoid reimplementation of what's already in CXL core
* Providing a facility to check and enumerate link capabilities allows the driver to focus on managing hardware
* Dan believes that CXL testing is necessary, and Weiny has converted some work from DCd to CXL test
* Quu support may be needed for testing core, but it's unclear how much it will be used
* Intel is working on colonel page merging for FPGAs, which could potentially use Type-2 support
* The community accelerator driver needs to integrate with the CXL core like a patch
* Raz handling might not require M infrastructure, and the current infrastructure relies heavily on memory
* There are plans to refactor CCI stuff in the core going forward
* Separation of concerns might be warranted, and one fix is needed to break accelerator device testing
* A lot of protocol support has been added for core support recently, including memory device support
* It's important to give a pathway for generically supporting Type-2 devices
* Weiny would like someone to validate generic Type-3 device support and push it back upstream
* There are wishes for a type three side operation that invalidates the decoder when a button is hit.
* Weiny hopes there will be path towards getting HMDB kernel piggybacking Type-3 support.
* Jonathan is going to kick off discussion on validation of Type-2 and Type-3 support.


## Plumbing challenges in Dynamic capacity device -  Ira Weiny, Jonathan Cameron, Navneet singh

URL: [https://www.youtube.com/watch?v=XlXAixfSww4](https://www.youtube.com/watch?v=XlXAixfSww4)

 * Introducing IRA Weiny and Jonathan Cameron, who will discuss challenges in implementing dynamic capacity device (DCD) feature and asynchronous memory release
* Agenda covers DCD use case, memory release interaction between kernel and fabric manager, CXL specification, and asynchronous event processing
* Dynamic Capacity Device: a feature that allows memory changes dynamically without significant host system change, depending on implementation
* Fabric manager triggers ADD release operation when user-pinned memory is released asynchronously, but memory can't be released back to the device if it's mapped by the kernel or the driver
* Asynchronous release event: the device may extend the block without an immediate response from the host, or the host might avoid sending a response back to the device
* The device and kernel must communicate to ensure proper memory management when offlining the memory
* DCD inter living challenge: managing multiple CXL devices participating in interleaving and keeping track of received extents
* Linux implementation for supporting DCD feature, potential use cases, and virtualization considerations.


## Adding RAS Support ​for​ CXL Port Devices​ - Terry Bowman

URL: [https://www.youtube.com/watch?v=tMMF8Vhgtho](https://www.youtube.com/watch?v=tMMF8Vhgtho)

 * Presenter discussed adding RAS (Reliability, Availability, and Serviceability) support for CXL (Compute Express Link) Port devices
* Three different protocols in CXL: cxlDOIO, cxlDMA, and cxlDocash
* Error handling differs between protocols: PCI error reported to host vs device using event log and mailbox for interrupts
* Probing routine reads capabilities to check for AER (Advanced Error Reporting) support
* Service driver includes AER functionality but requires BIOS or OS to be set first
* Root complex register block (RCRB) needs patch set for bus device function presence
* PCI Port bus probe routine checks for AER flow bit and handles errors differently based on whether the device is a PCI or CXL port
* CXL 1.1 Downstream Port handling includes changing RCRB call and parsing RCI (Root Complex Interconnect) child endpoint events
* Considerations for implementing RAS support include scalability, performance monitoring, hot plug, power management, and virtual Channel support
* Solutions discussed included adding a CXL Raz port service driver, modifying the existing service driver, and using a PCI performance monitoring driver
* Discussion covered challenges with registration, callbacks, and handling errors in different ways for CXL and PCI devices.


## Shared CXL 3 memory what will be required - John Groves

URL: [https://www.youtube.com/watch?v=aA_DgO95gLo](https://www.youtube.com/watch?v=aA_DgO95gLo)

 * John Groves from Micron presented on the potential of shared CXL 3 memory for scaleout file systems
* Goal is to raise awareness about fabric attached memory capabilities and its advantages, specifically for large-scale data processing use cases
* Shared pooling refers to assigning a given host with online memory that can be leveraged for various purposes
* Persistent memory (Dax) devices could potentially be used as raw tagged capacity for shared memory applications
* Current implementations have limitations, such as the need for hardware-supported cache coherency which is expensive
* Existing FS Dax file systems have implemented special metadata handling but still face challenges like efficient VMA fault handling and metadata distribution
* Proposed prototype includes preallocating files with a special creating procedure using mmap to enable faster metadata handling
* The current implementation may not scale for handling large file systems and managing multiple mountable files efficiently
* Tolerating client stale copies of metadata is another requirement that needs to be addressed in the design
* Key challenges include handling VFS layer interactions, log playback, and dealing with multiple writers and readers
* Goal is to enable various use cases, such as data science toolchains and large-scale computation workloads, by distributing shared memory more efficiently.


## CXL Memory Tiering for heterogenous computing - Ravi Kiran Gummaluri

URL: [https://www.youtube.com/watch?v=W551FRqLVOg](https://www.youtube.com/watch?v=W551FRqLVOg)

 * Ravi Kiran Gummaluri from Micron Technology discussed CXL (Compute Express Link) memory tiering for heterogeneous computing
* Memory demand in data centers is growing while memory capacity is not keeping up with processor speed and latency improvement
* CXL memory expansion can help by providing additional capacity transparently to applications
* Hardware-based interleaving policy can be used for bandwidth expansion use cases
* Software interleaving, which is currently limited, can improve overall system bandwidth
* Balanced interleaving in BIOS configuration can help with latency-constrained applications
* Discussion around software heterogeneous interleaving and weighted interleaving in the Linux kernel
* Ongoing discussion on implementing MIM (Multi-Instance Memory) tier support, which would allow more granular control over memory allocation
* Traditional hardware interleaving is typically subpage granularity while software interleaving allocates pages at the VMA level
* Testing has shown performance improvement for purely bandwidth-constrained applications using CXL memory
* CXL 2.0 adoption is happening, and there are various kernel patch reviews underway to support different use cases.


## A move_pages() equivalent for physical memory - Mr Gregory Price, Svetly Todorov

URL: [https://www.youtube.com/watch?v=4gjJ1ubH_tk](https://www.youtube.com/watch?v=4gjJ1ubH_tk)

 * The speaker discusses the idea of moving pages in physical memory using a move\_pages() equivalent for physical memory
* Multiple level memory devices, such as DRAM and NAND, could potentially offload page faults
* Transparent page placement is proposed as a solution to monitor what's hot and demote or promote pages based on usage
* Vendors have discussed implementing this feature in hardware with idle bit tracking and heat maps
* Reverse lookup of virtual addresses to physical addresses can be expensive and requires admin access, but a standard interface could make it easier
* The speaker mentions concerns about prefetch overhead and the potential for polluting sampling data
* A possible solution is to implement an asynchronous promotion mechanism like KPromoteD
* There are challenges with cross-interface device communication and ensuring that virtual address pfn tracking is accurate
* The speaker discusses the limitations of reverse mapping and the potential for offloading tracking limits
* Implementing move Fizz Pages based on a version 66 prototype is mentioned, but there are concerns about cgroups and locking
* Validating whether pages are migratable and reutilizing existing code directly to move pages is suggested as a solution.


## Hypervisor-Enforced Kernel Integrity (Heki) for KVM - Mickaël Salaün, Mr Madhavan Venkataraman

URL: [https://www.youtube.com/watch?v=jk1FBJxJBgA](https://www.youtube.com/watch?v=jk1FBJxJBgA)

 * Mickaël Salaün and Madhavan Venkataraman discuss Hypervisor-Enforced Kernel Integrity (Heki) for KVM
* Heki aims to protect Linux guests against various attacks, especially those modifying guest memory
* Trust in the guest OS can be diminished, so it's important to use mechanisms like SELinux instance or Secure Boot to ensure initial trust
* Protecting the host VM is crucial for improving C protection and mitigating potential attacks on the hypervisor
* Heki includes features like memory restriction, resource protection, guest enforcement, and reaction to attacks
* It also supports simple implementation and user-friendly interfaces that rely on existing hardware and software
* Initial trust can be established by verifying the authenticity of the guest OS and applications in the guest's address space
* Memory permissions can be enforced at various levels, including CPU registers, page tables, and device mappings
* Linux kernel's end boot process can also enforce additional permission restrictions on guest memory
* One challenge is handling legitimate modifications related to Kel module loading or dynamic memory management
* Possible solutions include implementing memory page tables, tracking mapping changes, and setting permissions for specific instances or modules
* BPF program signature checking is a big issue, as it cannot currently be done efficiently within the hypervisor
* Control flow integrity (CFI) can help protect against code injection attacks but needs improvement
* Additional security boundaries, policy minimization, and trusted hypervisors are potential solutions for better kernel protection.


## Multi-KVM Abstract - Anish Ghulati, Sean Christopherson

URL: [https://www.youtube.com/watch?v=S_PUlxPwWB0](https://www.youtube.com/watch?v=S_PUlxPwWB0)

 * Anish Ghulati presenting Multi-KVM proposal
* Allows running multiple independent KVM modules on a single Linux host
* Goals: easier testing, version compatibility, rolling updates with minimal disruption
* Proposed approach: isolate KVM internals from the rest of the kernel
* Collapse vendor module, expose multiple KVM devices without requiring exporting vendor modules
* Introduce a new base module for virtualization acceleration code
* Minimize VAC and avoid singletons throughout the system
* Base allocation management serves as a mediator
* Discussed potential challenges: hardware enable/disable logic, VMCS VP IDs, and sharing resources
* Motivation: live updates, ability to update entire hypervisor, and isolation
* Q&A session covers various aspects of Multi-KVM, including guest information, prior art, and security concerns.


## Unifying KVM API for protected VM and utilities - Isaku Yamahata

URL: [https://www.youtube.com/watch?v=fsEJnaJN5aw](https://www.youtube.com/watch?v=fsEJnaJN5aw)

 * The speaker is discussing the unification of KVM API for protected VM and utilities, specifically in regards to vfio-dpdk and mapping ports
* There are conflicting attributes when combining mappings, requiring an unmap equivalent portion
* A skeleton needs to be created for this unified attribute specification across architectures
* The speaker mentions the complexity of combining guest and host attributes, potential conflicts, and different requirements for different architectures
* The goal is to allow users to combine write messages and message buffer devices without using DMA or low latency communication
* Combining programming registers requires careful consideration
* There are difficulties in defining semantically what "combining" means across architecture implementations
* The speaker proposes two completely separate mappings for user space drivers, passing guest one complicated thing to the host and vice versa
* The discussion touches on the use of MTRs (Memory Type Range Registers) and potential conflicts with machine checks
* There have been historical problems with ignoring MTRs, causing machine checks and crashes
* The speaker suggests removing existing limitations in KVM for better compatibility with different vendors and hardware
* The conversation covers Intel and AMD specific issues and potential solutions.


## pkernfs: Persisting guest memory and kernel/device state safely... - Alexander Graf, James Gowans

URL: [https://www.youtube.com/watch?v=cYrlV4bK1Y4](https://www.youtube.com/watch?v=cYrlV4bK1Y4)

 * Discussing ways to pass kernel state across old and new kernels during live updates in the context of KVM virtual machines
* Three categories proposed to solve the problem: memory pools, device state preservation, and serialization framework
* Memory pool solutions include persistent kernel driver modules and file system abstractions
* Device state preservation involves creating a single relocatable blob for each device, which can be passed across kernels using a serialization path
* Serialization framework could be used to serialize and deserialize data, providing hooks for drivers to get and reinject their state memory
* Need to avoid clobbering specific pages when passing information across the kernel boundary, especially in the case of persistent memory allocators like PCI cache
* Discussed the challenges of preserving device state during live updates, including power management, hibernation, and firmware updates
* Agreed on the need for care in handling guest memory live during live updates to ensure stability and measurement across the boundary
* Proposed using a separate pool or file system to store persistent data, keeping it separate from nonpersistent data
* Discussed the importance of backwards compatibility when making changes to kernel data structures and interfaces
* Agreed on the need for a sensible foundation for building solutions, with a focus on simplicity and reducing complexity
* Emphasized the importance of user space cooperation in handling live updates, especially in the case of virtual machine state and vfio drivers.


## Hyper-V's Virtual Secure Mode in KVM project update - Nicolas Saenz Julienne

URL: [https://www.youtube.com/watch?v=Sm4YfJdgnno](https://www.youtube.com/watch?v=Sm4YfJdgnno)

 * Nicholas Saenz from AWS discussing Hyper-V's Virtual Secure Mode (VSM) implementation in KVM
* Two approaches to implementing VSM in KVM:
  + Approach 1: Separate vCPU and memory protection with a VTL aware kernel and extra turn memory slot handling
  + Approach 2: Full struct KVM per vTL containing vTL vCPUs and shared state
* Simplifying memory management vs introducing complexity with the VTL awareness kernel
* Discussion of VTL awareness kernel's responsibilities and potential benefits, such as optimizing things and eventually showing necessity
* Question about whether the responsibility split in user space is clear and simplification of memory management
* Proposed vCPU event PO interface enhancement for memory slot IO control
* Comparison to Hyper-V's BTL awareness kernel
* Concerns about complexity and maintenance with a larger user space kernel
* Question about the necessity of VTL awareness in KVM and its impact on APIC isolation and M slots
* Discussion of the advantages of running a smaller kernel for higher vTL levels and trusting the lower level kernel
* Comparison to Intel's TDX and the challenges with its Hardware ABI
* Preference for the least amount of awareness in KVM and its composability
* Concerns about supporting user space VSSM and the potential downsides
* Discussion of the complexity of user space and the need for a clear model for state transfer
* Proposal for implementing one R descriptor way to serialize dynamic lists and register transfer
* Discussion of memory attribute differences between KVM and vTL awareness
* Comparison of VTL awareness in KVM versus separate struct kvms and the need for a UAPI form for fast state transfer
* Thoughts on VM introspection and trusted DM
* Question about polling and user space copying registers
* Discussion of handling multiple priority M slots and guest communication
* Comparison to multi-KVM and the potential simplicity of accepting common resources and sharing code
* Difficulty of making a single CM module for KVM with separate text, data, and layouts
* Conclusion: VSM implementation in KVM is a complex topic with many considerations.


## Supporting guest private memory in Protected KVM on Android - Fuad Tabba

URL: [https://www.youtube.com/watch?v=MMfAGNW9RVg](https://www.youtube.com/watch?v=MMfAGNW9RVg)

 * Fuad Tabba from Google's Android system team discusses supporting guest memory in Protected KVM (PKBM)
* PKBM manages stage two page tables to protect guest memory
* Host kernel maintains stage one page tables and ensures guest memory doesn't disappear
* Current method of donating host memory to guests isn't ideal as it could lead to user space processes accessing protected memory, potentially causing issues with confidentiality
* TDX (Trusted Virtual Machines) also requires private memory for guest machines
* PKBM was upstreamed in Android 13 and differs from original guest memory design by allowing the hypervisor to manage memory protection instead of relying on user space processes to report it
* PDX (Page Disambiguation Extension) is used for sharing memory between host and guest without destructive data conversion
* PKBM adds a notification mechanism for validating transitions, ensuring that only allowed changes occur
* Current solution doesn't support unsharing memory from the guest to the host smoothly
* Testing use cases for unsharing memory don't exist yet, but it could be useful for dynamic software TLB sizing and bounce buffer regions.


## libside: Giving the preprocessor a break with a tracer-agnostic instrumentation API - Mathieu Desnoy

URL: [https://www.youtube.com/watch?v=QuCZbBg54Xg](https://www.youtube.com/watch?v=QuCZbBg54Xg)

 * Libside is a user space tracer project for instrumentation agnostic of the underlying tracer
* Goal: design user space instrumentation API that is self-described, supports compound and nested types, and provides interaction with the kernel tracer
* Current situation: Linux kernel has stable ABI for tracing but it limits application instrumentation due to its dependency on the kernel ABI
* Proposed solution: Libside, a user space tracer that uses self-described event registration and supports compound and nested types
* Features:
  + Simple ABI for instrumented code
  + Interaction with the kernel tracer
  + Supports concurrent tracing and dynamic language instrumentation
  + Allows registering event payloads and conditionally enabling instrumentation
  + Synchronization through RCU user space
* Future work:
  + Extensibility: allow adding new types and extending existing ones
  + Trace point validation and call site probes
  + State dump: allowing the tracer to query certain aspects of the application state
  + Integration with LTTng USERSPACE Tracer
* Challenges:
  + Performance: keeping good performance while interpreting bite code and removing overhead instruction cache
  + Filtering mechanism for events
* Questions from audience:
  + Macro to save parameter type information (yes, using L section)
  + Integration with dynamic instrumentation tools like Ding (yes, but Libside doesn't provide this feature directly, it can be used in conjunction with such tools)


## Graphing tools for scheduler tracing - Julia Lawall

URL: [https://www.youtube.com/watch?v=oG6kA9Cful0](https://www.youtube.com/watch?v=oG6kA9Cful0)

 * Julia Lawall presented graphing tools for scheduler tracing
* Goal: see activity at the core level, create shareable files (PDFs), address interactivity and scalability issues with Colonel Shark
* Introduced two tools: DatGraph and Stepper
* DatGraph shows task running and waiting, multiple tasks at once, different color for each core, good for observing scheduler context switches
* Stepper shows instruction events, PID and thread status (running or waiting)
* Interested in virtualization and created HostGuest tool to monitor VM and vCPU usage
* Discussed pinning threads for better performance and its impact on NUMA balancing
* Comparison of Linux versions 65 and 66, evolution of evdf and time slice length changes
* Created Fly tool to visualize time slice question, record start and stop times, divide by yield and sleep
* Conclusion: understanding tracing data can help in performance analysis, looking for new ways to standardize trace data plotting, interested in hardware topology details and NUMA balancing correlation.
* Mentioned LibbyValve tool for easy reading of DAP files and collaboration through web view.


## Function return hook integration with Function graph tracer - Mr Masami Hiramatsu

URL: [https://www.youtube.com/watch?v=-CUMxqATd4w](https://www.youtube.com/watch?v=-CUMxqATd4w)

 * The speaker is discussing the current situation and plans for fixing return hook integration in Function graph tracer
* Previously, there were three different probe tracers using return hooks with shadow stacks that stored real return addresses
* In the old plan, Shadow stack and Trum print were inside Carbon, but it didn't work due to complications with many return hooks and their shadow stacks
* The speaker is currently trying to fix Fpro part of Function graph tracer by providing M64 interface for implementing FProx86_64
* They are also moving from F probe event to Fgraph function graph tracer, which uses a unified integrated function graph tracer with shadow using the shadow stack and Trum ring for backward compatibility
* The old Carbon hooks (Red Hook, Carro probe, Red Hook trampoline) still exist and provide functionality but may be removed in future
* The speaker is discussing removing some Carbon Pro users, recommending moving to FPro, and removing shadow stacks
* There are ongoing discussions about keeping current Cate Pro things like the ring list and reusing code as much as possible
* Some audience members have questions about understanding the concepts, using Kprobe tree with C, and differences between F probe and Krep probe
* Some use cases for Kprobe include perf, getting variable info, and bug info, while some use FPro for register instrumentation and context pointer passed along.
* There are potential issues with R64 ton things and ptrs getting exception boundaries, but F trace regs use case is interesting
* Car Pro interface needs to keep backward compatibility
* The speaker mentions system tap folk and thanks the audience for their questions.


## pt_regs - the good the bad and the ugly - Florent Revest

URL: [https://www.youtube.com/watch?v=Q91Mxda_2BM](https://www.youtube.com/watch?v=Q91Mxda_2BM)

 * In 1991, Linux introduced exception handler saving registers but no restoration yet.
* In 1995, PTX was introduced with a user-level API and the use of offsets.
* In 2001, FTrace was introduced, which could read the offset of the stack and access saved registers in exception handlers.
* In 2004, MAMI made the process faster by saving registers immediately and using a trampoline.
* In 2011, Red Hook introduced an idea similar to MAMI but with saving registers getting restored during a call to the handler.
* In 2015, eBPF was introduced, often misunderstood as a runtime sandbox for verified code, it can attach to different attachment modes depending on how it is attached, and its probes can take ptrace arguments.
* FTrace and FEntry/FExit are recommended to be used with Pyrex and an array of u64 instead of accessing the TraceFS subsystem directly.
* The PState issue arises because arm64 trampolines cannot save RS, so it might result in reading null or garbage fields if not properly handled.
* To avoid potential issues, it is recommended to:
  + Avoid using ptraces and trampolines as much as possible.
  + Keep good documentation about which registers need to be populated.
  + Be careful when accessing non-populated fields in the architecture.
* The issue remains that PState needs valid states and registered to ensure reliable trace data.
* In conclusion, there are ongoing discussions about replacing the current subsystem with a new one that exposes the PT interface and FRS for better backward compatibility while avoiding potential issues.


## RTLA Requests and TODOs - Daniel Bristot de Oliveira

URL: [https://www.youtube.com/watch?v=jnhmWVOMrAM](https://www.youtube.com/watch?v=jnhmWVOMrAM)

 * Daniel works on Real-Time Scheduling Tool (RTLA) for analyzing and solving real-time problem latency
* RTLA tool is a user space tool inside tracing toolings, helps analyze and solve real-time problems quickly
* RTLA includes three tools: timer, trace, and control
* Timer tool measures scheduling latency using cyclic tests and sampling
* Trace tool simulates workload in user space to measure operating system noise and hardware noise
* Control tool reports root cause of high latency issues and helps debugging
* RTLA aims to make real-time analysis easier and more accessible for users
* Tools use a hackish front end and allow extending analysis with tracing
* Timer tool measures scheduling latency by setting Trace points, optimizing KPI and avoiding false positive Trace points
* Trace tool collects information from user space to make human readable output
* RTLA facilitates user interaction using a friendly interface and allows communication using LTTng Trace
* Tools use BPF for tracing and analysis, but need to find a way to get value per CPU without system calls.
* Daniel is working on improving OS noise measurement with the help of Paul Bonini (KVM guy) and Valentine (working on API noise correlation)
* He also plans to add auto analysis for scheduling latency workload and create a specific testing workload for FI people
* He suggests adding a pseudo random workload generator, formally proof scheduling analysis tool, and using Tracy instead of function tracing with wake-ups.


## Function parameters with BTF - Steven Rostedt, Mr Masami Hiramatsu

URL: [https://www.youtube.com/watch?v=KZIFUmDzhWQ](https://www.youtube.com/watch?v=KZIFUmDzhWQ)

 * Steven Rostedt introduced Function Parameter Tracing BTF (Berkeley Thread Stack)
* BTF provides function prototype information and can be used to trace function parameters and return values
* BTF shows function graph with parameter types and number, but not the actual values
* Discussion about precision of function parameter tracing and performance implications
* F Probe event supports precise function parameter tracing, may require function graph tracer for low-value parameters
* Goal is to have a quick way to see function arguments and return values without extending trace output with excessive information
* Filtering type prototypes and enabling function type filtering mentioned as potential solutions
* Discussion about making filtering online in BTF, using a BP (Berkeley Packet Filter)
* Mention of object tracing and the possibility of exact tracing of global variables
* Idea of adding K probes for global variable tracing
* Desire to see parameter values at certain points, but not wanting to see much information for normal functions
* Discussion about creating a separate instance for data collection and using a quick table for lookups.
* Possibility of generating bite code for faster lookup times mentioned.


## HiSilicon Performance Monitor Control Unit - Jie Zhan

URL: [https://www.youtube.com/watch?v=WEwjaTlrGzE](https://www.youtube.com/watch?v=WEwjaTlrGzE)

 * Performance Monitor Control Unit (PMU) outlines motivation, unit design, software module, and challenges
* PMUs provide hardware counters for performance analysis, help identify problem areas affecting latency, and monitor process utilization
* Software design involves cooperating with the Oxra framework for quick data transfer between hardware and user space
* PMUs have a control unit, DMA function, and event list to read and set event IDs for counting and sampling
* External access to PMUs requires synchronization mechanisms to avoid incorrect results due to concurrent access from multiple devices or CPUs
* Design includes enabling support for CPU and kernel access, implementing security measures, and managing individual counter state
* Discussion needed offline regarding integration and potential workarounds for security issues and counter control affecting the whole system
* Typical use case involves monitoring large numbers of events in hypervisor systems where context switching is not a concern
* PMUs read counters periodically to take samples and store values, but overhead can be high due to context switching and saving/restoring state per thread
* Conversation to continue later regarding DTrace or Matrix LPC event tracing.


## DTrace and eBPF: new challenges - Kris Van Hee

URL: [https://www.youtube.com/watch?v=kGdCXUwTmUQ](https://www.youtube.com/watch?v=kGdCXUwTmUQ)

 * Chris Van Hee from Oracle Language Tools department giving an overview of DTrace and its challenges
* Goal is to have dynamic tracing without rebooting system
* Existing tools like DTrace provide scripting language, probe attachment, conditional clauses, and response capabilities
* Challenges include:
  + Support for various kernels, some limitations still exist
  + Verifier improvements and dealing with behavior changes
  + Multiple kernel support and verifier compatibility
  + Generating BPF code dynamically and ensuring its validity
  + Limited state tracking and evaluating a large number of instructions
  + Function visibility and filtering for probes
* Difficulties include:
  + Probe creation failures due to obscure combinations
  + Attaching/detaching probes causing issues
  + Slow performance when replacing PTrace interface using signals or emulating original instructions
* Current solutions being proposed involve using Linker map data and consistent naming conventions for modules and symbols.


## Implementing sframes - Steven Rostedt, Indu Bhagat

URL: [https://www.youtube.com/watch?v=gqtl58s8SnQ](https://www.youtube.com/watch?v=gqtl58s8SnQ)

 * Implementing sframes for getting stack traces in kernel NMIs
* Frame pointers add overhead and don't provide much perf clue
* Orc unwinding used instead of frame pointers within kernel, with fixed-size stacks
* Problems with getting accurate function information without orc unwinder
* Live kernel patching required for accurate unwinding
* Idea is to create a user space ELF section called "frame"
* Elaborating on differences between JIT environments and Linux
* Frame makes a difference in various JIT environments, stack frame layouts, and jitted code
* Need to ensure frame representation is compatible with ABI and JIT runtimes
* Dynamic linking required for representing S frames in JIT environment
* Option of using frame pointers in generated code or having the JIT compiler generate frame functions
* Interpreting problem: want to get instruction pointer in interpreted code
* Need format support for relocated addresses and shadowed stacks in jitted code
* Creating a table with frame information and constant modifications needed for perf and compatibility reasons.


## The taming of the kernel dump -  Petr Tesařík

URL: [https://www.youtube.com/watch?v=NpvbrnZ6B5o](https://www.youtube.com/watch?v=NpvbrnZ6B5o)

 * Petr Tesařík talks about his experience with debugging and the development of his library, Kump, for accessing crash dumps
* Background: Previously used tools like L crash were not ideal, so he wanted to create a reliable, universal library for interpreting kernel crash data
* Goals:
	+ Mimic actual hardware specifications
	+ Cross-platform compatibility
	+ Fast enough run time for crashed systems
	+ Detailed information exposure
	+ Extensibility
* Design:
	+ Based on existing LKCD library
	+ Added support for various architectures, including x86_64, ARM, and IBM zSeries
	+ Implemented page table translation for different hardware
	+ Exposed CPU register saved dump format
	+ Kept the library reliable by writing test cases
* Challenges:
	+ Handling various file formats (e.g., QEMU Kdump format)
	+ Converting existing megum files to the new format
	+ Implementing a GDB server-based LiK dump file
* Future work:
	+ Support for more architectures and paging formats
	+ Improving the API for easier use
	+ Handling larger dumps more efficiently
	+ Adding support for compressed data and other advanced features.


## drgn Writing to Memory and Breakpoints, Safely in Production? - Omar Sandoval

URL: [https://www.youtube.com/watch?v=6jRi44yp3YQ](https://www.youtube.com/watch?v=6jRi44yp3YQ)

 * Omar Sandoval from Meta discusses the idea of adding memory writing and breakpoints feature in Drgon debugger for production use
* Drgon is a programmable debugger that can be used in production to debug complex issues
* Memory writing and breakpoints could be implemented through an API with a bite buffer write function
* API would allow overwriting specific values, structures, and objects in memory
* Breakpoints could be set by address or function name with offset
* Watch points and error injection testing are other possible use cases for the proposed feature
* Concerns about production safety and potential for race conditions were discussed
* Alternative approaches such as bringing back Devkm, integrating KGDB, or using a custom kernel module were suggested
* Access control and security implications of the feature were also considered.


## Beyond DWARF: Debugging the Kernel with Drgn BTF/CTF & kallsyms  Stephen Brennan - Stephen Brennan

URL: [https://www.youtube.com/watch?v=Yqv1qwQ29ik](https://www.youtube.com/watch?v=Yqv1qwQ29ik)

 * Speaker is motivated to use Dragon debugger due to frustration with installing and managing debug info for various Linux distributions and the large size of debug info files.
* Dragon debugger aims to provide source code mapping, Call Frame Information (CFI), and a flexible pluggable type system for debugging.
* Dragon's implementation currently supports CTF and BTF, but there are challenges with symbol finding, kernel versioning, and compatibility.
* The speaker has been testing Dragon on different kernels and using the plugin system to use different type systems like CTF and BTF.
* The main issues they have encountered include handling per-CPU symbols and the lack of reliable code changing support in BTF.
* They also mention that they are working around kernel version checking by adding a versioning system.
* They plan to add support for CTF via binutils libCTF and implement BTF parsing, but are having some difficulties with compatibility and performance.
* The speaker mentions that the large size of debug info is a concern and wonders if using a smaller format like CTF or BTF would be an option.
* They also mention that interactively debugging and using stack traces are important use cases for them.
* They suggest that users might want to consider the impact of large debug info sizes on performance and whether they would prefer a smaller runtime debug info format.
* They briefly touch on the fact that some proprietary modules don't ship with debug info, but mention that leaving the BTF/CTF information in the binary is a necessary evil sometimes.
* They also mention that they have heard people complaining about the size of DWARF, and suggest that perhaps making DWARF generation more fine-grained could be an option.
* They ask if there is a way to selectively strip debug info using GCC or duplicate it like with dwz, and mention that they haven't seen anything like this for kernel debug info.
* They mention that in their experience, extracting compact debug info from full debug info takes longer than expected and is not always practical for live use cases.
* They briefly touch on the fact that BTF does not support variable CTF and mention that they have a patch to fix it.
* They mention that Dragon currently supports debugging user space stuff for free, but there are convenience factors to consider when downloading large debug info files.


## When kdump is way too much - Guilherme Piccoli

URL: [https://www.youtube.com/watch?v=HOewOQQfvP8](https://www.youtube.com/watch?v=HOewOQQfvP8)

 * Guilherme Piccoli works at Talia Cooperative and has experience with K debugging and open source software
* Talk is about considering alternatives to Kdump for collecting log data during system crashes in Arch Linux
* Current infrastructure collects logs manually using Wiki instructions, but it's not ideal due to the size of the logs and difficulty sharing them
* Considered using Pstore as a lightweight alternative to Kdump
* Benefits of Pstore include: transparent process, flexible data collection, and no need for a new kernel during reboot
* Challenges with Pstore include: risk of corrupting memory, difficulty finding enough reserved memory, and potential issues with locking mechanisms
* Discussed possible solutions, such as using a hypervisor or splitting notifiers into simpler parts
* Also mentioned the use of Ben Print to gather more information during crashes and the possibility of using BPF programs to print additional data during crashes.


## Minidump to debug end user device crashes - Mukesh Ojha, Elliot Berman

URL: [https://www.youtube.com/watch?v=3vL3gtAu84s](https://www.youtube.com/watch?v=3vL3gtAu84s)

 * The speakers discussed using mini dumps to analyze device crashes on end-user devices, focusing on Qualcomm devices
* Mini dumps are preferred over full system dumps due to privacy concerns and limited memory available on the devices
* Firmware can detect crashes and collect mini dumps instead of a full system dump
* Mini dumps have lower overhead than traditional methods and can be optimized for specific subsystems like Linux
* Collecting mini dumps involves registering regions of interest, such as kernel memory or log buffers, to be captured
* The speakers discussed various options for collecting mini dumps, including using existing solutions like KDump or developing custom implementations
* Mini dump frameworks can also collect additional information beyond just the crash, such as initial message logs and IP statistics
* The speakers mentioned that there is ongoing work to improve mini dump collection and reduce overhead.


## Kernel Livedump - Lukáš Hruška

URL: [https://www.youtube.com/watch?v=Kl9U72URdBE](https://www.youtube.com/watch?v=Kl9U72URdBE)

 * Speaker: Lukas Hruska, SuSE developer
* Project: Kernel Live Dump (KLD), a tool to create consistent image of kernel memory without stopping or restarting machine
* Motivation: Debugging complex issues in production and high-availability services without downtime
* Current limitations: Supports x86 architecture, one output format (crash dump), and has some performance issues
* Goals: Extend support for multiple targets, improve performance, and ensure correct page protection during conversion from virtual to physical addresses
* Challenges: Synchronization problems with memory, managing page frames, and handling virtual memory address protection
* Solutions: Implementing calibration phase, optimizing conversions, and considering alternative approaches like variant page Vault
* Future plans: Creating target storage support, implementing dump filtering, and addressing potential conflicts with software bits.


## Sensors aggregation - Alexandre Bailon, Daniel Lezcano

URL: [https://www.youtube.com/watch?v=ezPqzXYRe5I](https://www.youtube.com/watch?v=ezPqzXYRe5I)

 * Alexandre Bailon and Daniel Lezcano discuss sensor aggregation in the context of Mediatek drivers.
* Aggregation could be used for various purposes, such as IPA governor or drive BLop.
* Virtual sensors can aggregate values from multiple sensors.
* Aggregation can be done in user space using debugfs and CFS.
* Thermal Zones could be aggregated to provide new virtual thermal zones.
* The idea is to create a new device tree node for the aggregated sensor.
* Computation for aggregation may be simple or complex depending on the number of sensors involved.
* There are challenges in implementing sensor aggregation, such as avoiding unnecessary computation and dealing with broken sensors.
* Two proposals were made: one to create a driver for sensor aggregation and another to modify an existing function.
* The second proposal was accepted and the thermal framework is being reworked to make it more generic and efficient.
* IPA maintainer (Lucas Luba) thinks it's a nice feature for multisensor thermal zones.
* One use case for sensor aggregation is to mitigate CPU temperature issues using IPA.


## New thermal trip types - Daniel Lezcano

URL: [https://www.youtube.com/watch?v=kzChxV9SQuk](https://www.youtube.com/watch?v=kzChxV9SQuk)

 * Daniel Lezcano presented three new types of trip points for the Tam framework in this talk.
* Trip points are used to monitor temperature and trigger specific actions based on thermal conditions.
* There are passive, user-space, and writable trip points.
* Hardware needs to know the order of trip points and send signaling when they are crossed.
* User trip points can be set in user space and handled by the Tamar framework.
* Passive trip points are like look drivers that can misuse one trip point.
* Enabling writable trip points allows users to create their own entry points in CFS.
* Thermal debugfs information provides insights into thermal behavior, but it's complex and may not show all relevant information.
* Improving step-wise governors involves creating a new governor with more accurate temperature estimation and faster reactions to temperature changes.
* Polling mechanisms can be used instead of interrupts for monitoring temperature, but they have overhead and may not be able to handle fast temperature changes.
* Power management coprocessors can assist in handling thermal stuff quickly when the CPU cannot keep up.
* The Shred polling mechanism is similar to F task change and real-time tasks.
* User space trip points can use interrupts and hardware sensors for faster reactions, but they need careful programming to avoid conflicts.
* Two different temperature sensors might require two interrupts or different interrupt times to handle user trip points moving around.
* PID controllers are similar to regular interval monitoring and math-based interval estimation.
* Implementing Kel provides user-space K coefficients for proportional-integral-derivative (PID) based temperature control on different platforms.
* Force learning algorithms like IPA could optimize coefficient output and debounce FS for better thermal management.


## Use of Netlink for thermal kernel-user notification is problematic - Srinivas Pandruvada

URL: [https://www.youtube.com/watch?v=Ef-td6GV3TY](https://www.youtube.com/watch?v=Ef-td6GV3TY)

 * Shina works with Intel and has contributed to thermal subsystem for a decade
* Netlink is a user-kernel communication mechanism used in Linux for low-overhead, resource-efficient communication
* Netlink is primarily used for unicast and multicast messaging and is socket-based
* Netlink objects (U events) are used for user space governor notifications
* Intel platform uses netlink for thermal event notifications from driver to user space
* Thermal code calls netlink to set policy and update thermal zones
* Kobject U events use a string bit format for sending objective events to user space
* Netlink allows userspace to subscribe to specific events and receive notifications in real-time
* Fast mitigation is necessary for handling undershoot and overshoot issues
* User space governors have potential problems, including testing system instability and noise
* Multiple groups and types of events can be a problem as everyone gets all events
* Call time and message failures are also issues with netlink notifications
* Filtering mechanisms could improve efficiency but don't scale well
* Creator of the filter event instead of creating new multicast groups is suggested
* Netlink allows userspace to find and handle messages efficiently
* The delay between notification and taking action can be a problem, especially with character devices
* A 100-micsecond delay was reported in testing
* Netlink doesn't allow changing policy or filtering events for specific devices
* Creating filters instead of new multicast groups is suggested to improve efficiency
* Some people have tried dropping messages when they aren't needed to reduce noise.


## CPUfreq/sched and VM guest workload problems - David Dai, Saravana Kannan

URL: [https://www.youtube.com/watch?v=ZBpmSIchASQ](https://www.youtube.com/watch?v=ZBpmSIchASQ)

 * David Dai from Google's Android Jour team presented at LPC 2022 about VM workload and CPU frequency scheduling
* Two main reasons for terrible performance in VMs: low tracking inside the VM and lack of architecture awareness on the host side
* Updated FVM with relevant DT property and created M CPU frequency control device for better frequency awareness
* Host sets frequency, VM gets frequency via trap; host side reads current physical CPU frequency and sends back to VM
* Host-side performance contract (like AMU CPCC) writes register, sets frequency trap first on the virtual CPU
* Synthetic workloads showed improvement after fixing the issue: smaller thread runs continuously, less time taken for fmin/Fmax, etc.
* New thread starts get fmax feature sooner, reducing latency
* Two open issues: handling two threads taking 50% CPU capacity on different CPUs and applying additive UK clamp effectively
* Design goal was to use low-latency interfaces and communicate between host and guest efficiently
* Guest CB frequency driver makes hypercall for setting/getting frequencies, but current solution uses mm instead of making direct reads/writes in user space
* BPF could be a potential solution with fewer context switches and additional assist calls back to the kernel
* Benchmarks showed performance improvement using PC Mark inside an Android VM on Chromebooks
* Discussion will cover additive clamp versus max aggregation and potentially EBPF as well.


## VM-CPUFreq for x86: Scaling the guest frequency for performance and power savings - Mr Wyes Karny

URL: [https://www.youtube.com/watch?v=MqZ7vcdgatc](https://www.youtube.com/watch?v=MqZ7vcdgatc)

 * Wyes Karny from AMD's scheduling team discussing VM-CPUFreq for x86 and scaling guest frequency for performance and power savings
* Linux CLE scales core frequency based on utilization, formula: Fnext = Utilization * Fmax / (1 - Utilization)
* Measured utilization of a workload in virtualization case compared to bare metal case
* 90th percentile utilization for workload in virtualization was 41%, host was 42%, and bare metal was 17%
* Varying busy percentage affected guest frequency, idle became 40-5050 Hz, and busy became 133-1330 Hz
* Goal is to make guest perform similar to bare metal while minimizing VM exits and power consumption
* Guest Idle exit problem: cloud providers want lower latency but it leads to higher power consumption
* Tried V2 and V3 patches, no significant performance or power improvement
* Used idle pool inside Cas for power consumption measurement, saw minimal improvement in D benchmark
* Varying the number of vcpus showed power improvement in idle pool case with sustained workload
* Guest Po M still showing 100 utilization despite seeing higher utilization compared to normal cases
* Current VC patch considers lower and upper bounds but no significant improvement seen
* Question: can CPUs be clustered independently and if so, is VMCP stuff useful?
* Clusters can be scaled independently at the CPU level, request frequency change independently
* Suggestion: use ACPI CPU frequency scaling on server instead of VM-CPUFreq for better granularity in utilization reporting
* Question about host perspective idle polling and guest VCPU thread being busy while idle
* Host might not take into account next time the scheduler computes frequency based on guest thread usage
* Guest needs to find another way to communicate frequency requirements to the host instead of relying solely on utilization reporting.


## Virtualized Frequency Control for Telco Workloads - Mr Chris Macnamara, Srinivas Pandruvada

URL: [https://www.youtube.com/watch?v=uKbVfAcFxwY](https://www.youtube.com/watch?v=uKbVfAcFxwY)

 * Chris Macnamara from Intel discussing Telco workloads and power management opportunities
* Characteristics of Telco workloads: 24-hour period, varying load, long-running applications, polling, pinned processes
* Challenges in Telco space: fixed dimensioning, power management adoption, lack of privileged access for user space Power Governors
* Virtualized frequency control for VM case: need to build solution with launched VM, custom API, guest host proxy, and user space Governor backend
* Observations: Vero serial interface latency, SCMI implementation, Hypercall BPF solutions
* Questions from audience: clarification on SKULE, host-side decision making, expected performance changes, LAN vs WAN latency.


## uclamp in CFS: Fairness, latency, and energy efficiency - Dietmar Eggemann, Morten Rasmussen

URL: [https://www.youtube.com/watch?v=zSWO2x2ck70](https://www.youtube.com/watch?v=zSWO2x2ck70)

 * Dietmar Eggemann and Morten Rasmussen from Arm discuss issues with the current UK Clamp implementation in Compute Fairness Scheduler (CFS)
* Main issue is with aggregation per task UK Clamp setting and max utilization value tracking
* Current implementation uses max aggregation mechanism, which requires a lot of computation every time it's used
* Proposed solution: revisit implementation choice and consider summarizing UK Clamp as a performance hint instead of actual desired throughput
* Example: Min set takes the maximum of Min request and Min clamp applied utilization, resulting in a frequency that may not meet true compute demand
* Shared tasks in Run Queue (Run VI) are particularly affected by this issue
* Current implementation allows one task to monopolize CPU capacity, leading to underutilization for other tasks
* Proposed solution: use per-task clamp instead of max aggregation to maintain proper energy model calculation and true utilization representation
* Latest patch attempts to address the problem by separating clamped and non-clamped tasks and tracking their utilization separately
* Current implementation's bucket mechanism erodes accuracy in clamp setting tracking
* Proposed solutions: either hold deeper Max aggregation or create a new pillar to derive a signal for better load balancing
* It's unclear who is using UK Clamp extensively, as the mainline implementation may not be used by major users like Android
* Pixel devices use task-level throttling instead of full Upstream solution
* CED (CPU share) issue might be related to UK Max, but it's not clear if UK Max provides a solution for it directly
* Possible solutions: filter mechanism, per-task clamp, or creating another pillar to derive a signal for load balancing.


## Make sync_state()/handoff work for the common clk framework - Stephen Boyd

URL: [https://www.youtube.com/watch?v=tXYzM8yLIQA](https://www.youtube.com/watch?v=tXYzM8yLIQA)

 * The function clock framework issue has existed for over 10 years
* The problem is with the sync\_state()/handoff mechanism in the framework
* The goal is to ensure deferred probing happens and disable unused clocks
* The current code disables clocks even if they are still being used, causing issues
* Some solutions proposed:
  + Let the sync\_state logic run and call a generic clock sync State function for the entire tree of devices
  + Keep the clock enabled in hardware while someone calls the State device driver function
  + Use a separate flag to indicate that a ref count is not needed
  + Remove the need for a late call to disable clocks
* The ideal solution would be for everyone to switch to using the device clock driver instead of declaring their own clocks
* Recent approach allows for a sync State callback to be used instead of registering the clock, but it doesn't really handoff sense and can cause issues with multiple drivers sharing a clock
* The requirement is conflicting as some people want to keep clocks enabled while others want them disabled, based on the platform and board requirements
* The issue can cause problems when hardware isn't writing enable registers properly, requiring workarounds such as setting a handoff flag and not calling enable
* Other proposed solutions include scanning the entire DT for interconnect providers and turning off unused clocks, deleting the late call to disable clocks altogether, and using power management techniques to save power.


## Intel Low Power Mode Daemon on Hybrid CPUs - Rui Zhang, Srinivas Pandruvada

URL: [https://www.youtube.com/watch?v=pTF3qBALIsI](https://www.youtube.com/watch?v=pTF3qBALIsI)

 * Intel Low Power Mode Daemon on Hybrid CPUs
* Background: Hybrid platform with multiple CPU types, different power efficiency scenarios
* Low Power Mode Demon: Implemented in Intel's latest hybrid platform (Medfield)
* Challenges: Solutions not yet upstream, open questions welcome
* Hybrid Platform: Multiple CPUs, different power savings scenarios
* Located in compute low power die, keep other die active
* Decision based on system utilization and user space tools
* Low Power Mode Keep CPUs in quiescent state, need to migrate tasks
* AQ balance via socket messages or directly through task placement
* Challenges: Inefficient idle load balancing, unbound workers running on isolated CPUs, timer issue with C group isolate partition
* Solutions: Simple fix for idle load balancing, patch for unbound workers, fix for timer issue (not yet upstream)
* Low Power Demon: Needs to exit low power mode when task doesn't fit capacity, performance concerns, response time critical
* Monitoring system CPU utilization for entering and exiting low power modes
* Capacity-aware scheduling might be a solution
* Energy Aware Scheduling vs. Capacity Aware Scheduling: Different models, energy model needed
* Alder Lake: Max guaranteed frequency 800 MHz, max turbo frequency 5 GHz, big difference in capacity
* Linux concept of CPU capacity, hardware related but difficult to track software side
* Turbo Ratio Limit: Intel processor can handle multiple frequencies, average power and temperature also important
* Discussions on email.


## Enabling DDR segments on demand during memory pressure for DDR power reduction - Sudarshan Rajagop

URL: [https://www.youtube.com/watch?v=BecL1j3VuU0](https://www.youtube.com/watch?v=BecL1j3VuU0)

 * Sudarshan Rajagop from Compuverde presents on DDR segment power reduction for Linux systems
* Motivation: With increasing DDR size in mobile systems, saving unused memory can lead to significant power savings
* Two technologies used for DDR offlining: Partial array self refresh (PAR) and full rank
* PAR allows turning off particular ranks or segments of an array to save power
* Full rank involves shutting down entire VDD and certain ranks for significant power reduction
* Offline segment can be enabled based on memory pressure, user interaction, or system state
* Memory hotplug and page isolation migration can be used to manage offline segments
* Linux kernel divides RAM into different zones (normal, mobile, etc.) to manage offline segments
* Power saving mode, UI options, and system states can trigger memory offlining
* Pressure stall information (PSI) is used to detect memory pressure and enable offlining
* User space services can monitor memory pressure and send requests for offlining
* CFS node kernel driver manages memory hard plug and notifies the hardware of offline/online status
* Offline segments save power by reducing online time, but impact performance with increased latency.


## Improving monitoring of power saving states - Mr Stanislaw Kardach (Google), Sven van Ashbrook

URL: [https://www.youtube.com/watch?v=VSfkQ9DcPqI](https://www.youtube.com/watch?v=VSfkQ9DcPqI)

 * Speaker is from Chromium OS platform enablement team, discussing monitoring and improving power saving states, specifically idle and sleep states
* Big Forest Power (Linux) being focus, with emphasis on CPU idle state
* Current methods for tracking power savings are patchwork and disorganized (CFS, debugfs, ACPI, etc.)
* Issues include lack of atomicity, inaccurate statistics, and overlapping implementations
* Proposed solutions include standardizing and genericizing the process, adding static suspend modes, and using tools like Turbostat for better measurement
* Need for granular measurement and multiple implementation options
* Challenge is debugging and getting accurate information from various systems and vendors
* Goals are lower static resume latency and comparable power savings across different systems.


## bpftime: Fast uprobes with user space BPF runtime - Yusheng Zheng

URL: [https://www.youtube.com/watch?v=WEJ9MNO58Ac](https://www.youtube.com/watch?v=WEJ9MNO58Ac)

 * The speaker, Yusheng Zheng, is presenting on BPF Time, a new user space BPF runtime
* Current EBPF implementations have limitations such as performance issues and configuration complexities
* BPF Time aims to address these issues by providing a dynamic and flexible user space BPF runtime
* Use cases include dynamic tracing, memory allocation testing, and inter-process communication
* BPF Time supports large shared memory maps, per-event centers, and compatibility with existing EBPF tools and libraries
* It also brings new features like inline hook-based tracing and improved performance
* The speaker mentions potential use cases in network plugins, smart contracts, and system calls
* BPF Time is currently an open source project and is compatible with current EBPF behavior
* It can attach to running processes automatically without modifying the application or requiring kernel restart
* BPF Time also supports multiple injection runtimes and sharing libraries between processes
* The speaker discusses potential improvements and ongoing work, including optimizing performance and error propagation
* The presentation includes a demo of BPF Time in action.


## Make ftrace_regs a common trace interface for function entry/exit tracing -  Masami Hiramatsu

URL: [https://www.youtube.com/watch?v=UBHe2HqQW_A](https://www.youtube.com/watch?v=UBHe2HqQW_A)

 * Masami Hiramatsu discussing FTrace RS and function tracing
* Currently, PTX probe uses native PTX for tracing with Kprobe, March Pro, etc.
* PTX probe requires manual register saving in interrupt handlers
* FPro doesn't use interrupts; instead it hooks function calls using trampolines
* Problem: saving registers manually is inefficient and error-prone
* Goal: make PTX more flexible and efficient for function tracing
* Proposed solution: abstracting register access through FTrace RS interface
* FTrace RS can save and restore function entry/exit parameters, return values, and function pointers
* Discussion about using Carro probe with incomplete PTX and ebpf interface changes
* Future proposal: use FTrace regs directly instead of PTX interface for efficiency
* Q&A session follows the presentation.


## Where have all the kprobes gone - Jiri Olsa

URL: [https://www.youtube.com/watch?v=Erqy3rxDp4g](https://www.youtube.com/watch?v=Erqy3rxDp4g)

 * The presentation is about Linux kernel's kprobes and their usage in BPF (Berkeley Packet Filter) programs for tracing and attaching to functions.
* Kprobes are probes attached to the kernel, allowing execution of a BPF program when a specific condition is met or a function is entered/exited.
* There are different layers to attach kprobes: perf_event, FTrace, and raw Perf.
* Kprobes have some limitations, such as no nesting (one running kprobe prevents another from running), and counter access only through specific interfaces.
* The presentation covers various topics related to kprobes, including their usage, performance considerations, and limitations.
* There is a discussion on the difference between FTrace recursion locks and context-based nesting checks and how they affect the system.
* The speaker mentions some improvements, such as adding support for Mist counters and removing the need for recursion checks in some cases.
* The presentation includes examples and explanations of various use cases and scenarios related to kprobes and their application in the Linux kernel.


## xprobes: Hybrid User/Kernel eBPF Probes for Cross-Layer Observability - Lucas Castanheira

URL: [https://www.youtube.com/watch?v=p7myCfGIsrs](https://www.youtube.com/watch?v=p7myCfGIsrs)

 * The presentation discusses using Xprobe, a hybrid user/kernel eBPF probes tool, to enhance observability and understand system performance issues.
* Common performance indicators can suddenly shoot up, making it necessary to investigate the root cause with tools like CPU profiling or distributed tracing.
* Horsemen (outside userland latency tracing) is an example of a tool that doesn't show obvious play in userland. Xprobe aims to trace Horseman by using hybrid U probe and K probe together.
* Kprobe introspects kernel events like context switches, mutexes, and file system reads. Uprobe gives exact function begin and end times.
* BCC currently instruments with shadow stack process tracing. The goal is to make Kprobe talk to the shadow stack kept by Uprobe to get attribution logic.
* Attribution Logic assigns resources taken during invocation to the corresponding function.
* To understand CPU usage, it's essential to profile calls and see if they have significantly different resource usage depending on the call context.
* The presentation focuses on Xprobe overhead as an elephant in the room. A benchmark with Redis showed that tracing nothing had a baseline of 450,000 get requests per second, while using Xprobe, Uprobe, and Kprobe reduced performance to 400,000.
* Tracing one function and tracing Xprobe, Uprobe, and Kprobe together resulted in a trace Xprobe overhead and U probe overhead, which were unexpectedly high. The main overhead comes from trap work done inside the U probe.
* The presentation suggests that people might be overestimating BPF time and that not using U probe for manual instrumentation could reduce overhead.
* There is ongoing research into efficient data storage to serve several different application diagnosis tasks.
* The presentation discusses the difficulty in understanding stack trace in the context of multiple executions, where functions might have different execution start and end times and resource usage.
* Lawrence asks about half overhead instruction emulation in the kernel and Alex mentions that it might be a problem if the audience is not prepared for it. The worst-case scenario involves three traps per instruction, but the typical case is two traps with a single byte instruction being simulated.
* Reducing overhead using U probe involves call callsum in the BPF program and reducing the number of software breakpoints used by the user space program.
* The presentation introduces the idea of injecting an event into the kernel instead of injecting a probe, which might reduce overhead.
* Combining user-space writing with trampolines or special system calls could potentially make probes faster. However, there are limitations due to the need for Kernel interfacing and map updates, which can be slow.
* The presentation suggests that a hybrid solution using a small user space trampoline might be a good way forward to make probes faster while keeping the application uninstrumented.


## BPF programmable netdevice - Daniel Borkmann

URL: [https://www.youtube.com/watch?v=o6wdzYC3oi0](https://www.youtube.com/watch?v=o6wdzYC3oi0)

 * BPF programmable net device discussed for achieving lowest networking overhead in Kubernetes
* Goal: reduce networking overhead and improve scalability
* CIUM architecture overview: Weave Net device, CIUM agent, CNI plugin, and iptables
* Problem: long list of iptables rules, back pressure, and performance issues
* Solution: use BPF to redirect packets inside the host TC BPF layer, implement a new fast path call (tcx), and merge it into the kernel
* Benefits: reduced cycles, faster switching, and better handling of multiple user TC hooks
* New driver being developed for replacing Weave Net device with netkit device and executing BPF programs inside port drivers
* Challenges: IPVLAN limitations, L3 mode problems, and support for multiple physical devices
* Future work: adding support for go-based netlink library, fixing networking statistics, and improving performance.


## Application network security and observability in an encrypted future  -John Fastabend

URL: [https://www.youtube.com/watch?v=8MJh864668Y](https://www.youtube.com/watch?v=8MJh864668Y)

 * John Fastabend discussing application network security in an encrypted future
* Tetragon security tool: observability runtime enforcement, BPF filtering and enforcement
* Importance of maintaining visibility and CPU usage in the kernel for quick problem resolution
* BPF (Berkeley Packet Filter) provides low-level access to network traffic, avoids sending events to user space, and can maintain exact socket maps
* Kubernetes environment: labels, namespaces, privileged namespaces, and cgroups
* Trust domain model and security concerns with pushing everything into the kernel for visibility and correctness reasons
* Use cases of Tetragon: DNS parsing, HTTP event generation, namespace change privilege capability, and CVE mitigation
* Networking: collecting networking information, seeing binary execution inside containers, and understanding malicious connections
* Trust model: hooking the kernel to get data and maintaining trust boundaries
* L7 sock map socks operations advantage for manipulating data at the application layer
* Differences between TLS offloading and encryption in the kernel versus user space
* Controversy around BPF and its limitations, including bounded loops and header size concerns.


## Safe sharing of the network with eBPF - Balasubramanian Madhavan, Prankur Gupta

URL: [https://www.youtube.com/watch?v=1l-eiN--w9U](https://www.youtube.com/watch?v=1l-eiN--w9U)

 * Balasubramanian Madhavan and Prankur Gupta presented a solution for safely sharing network resources in data centers using eBPF.
* Common problem observed is microbursts in data center networking causing packet loss, queuing, and high latency.
* eBPF was used to develop custom congestion control algorithms like delay-based congestion control.
* Struct Top was used to get flow information for making decisions and predicting network conditions.
* Delay-based congestion control reduces queuing by setting specific delays based on INT region flows.
* eBPF helped handle signal collection, sampling, and decision making for prediction and condition detection.
* Custom Congestion Control (CCF) was built using eBPF to add signals and improve existing algorithms for handling new traffic patterns.
* Infrastructure was deployed fleetwide to observe impact on connections and deal with operational challenges such as long-lived connections and interoperability between versions.
* Atomic upgrades were implemented to reduce downtime and remove the need for pinning BPF objects.
* eBPF versioning manager was added to easily manage and solve complexities like synchronization and access control issues.


## BPF struct_ops - current status and the last developments - Kui-Feng Lee (Meta)

URL: [https://www.youtube.com/watch?v=sXHoa9eJtMA](https://www.youtube.com/watch?v=sXHoa9eJtMA)

 * BPF (Berkeley Packet Filter) Stops (Strategies) Operations (Ops) define set operations for specific types of objects and manage behavior as a kernel subsystem.
* Stops include network control algorithms, resource controllers, test modes, etc.
* Implement function pointers and register objects to be used by the BPF program.
* Test modes have two functions: user test one and user test two.
* User test one function signature matches a decared function point in the BPF program.
* Stops map is a key-value pair system where values are content bodies, and loading objects can cause problems if values are deleted or updated.
* Previously, Stops map reduced subsystems like TCP congestion control used a bit map to manage loaded values.
* New API creates BPF links directly instead of using St links.
* The new API also supports link updates and registration.
* Fuse BPF is a user space interface that allows running the BPF program without changing the kernel.
* It introduces a new StOps type called fuse D1, which installs filters in the kernel according to a number.
* The classic FUSE driver looks like every call from the file system is forwarded as a request to user space and then translated back by the BPF program.
* The benefit of using BBF Stops for scheduling is that it eliminates the need to compare kernels or reboot the system, as the loader can easily load new programs without changing the kernel and verifying them with the BPF verifier.
* Using BBF Stops can improve latency by allowing customized Paranoid scheduling algorithms and providing extension filters for security and resource limit checks.


## BPF Static Keys - Anton Protopopov

URL: [https://www.youtube.com/watch?v=HKmb0Oamtos](https://www.youtube.com/watch?v=HKmb0Oamtos)

 * BPF static keys are a feature added to the Linux kernel that utilizes compiler feature Tgo and requires PGE code support.
* They allow defining and initializing static keys, which can be used for branch prediction and debugging purposes.
* A key is defined using the `Define key` instruction in BPF assembly, with `static` being the compilation name.
* Key initialization is false by default, meaning it is disabled.
* The `Branch` instruction with an unlikely condition can be used to look up a static key and replace a jump op with the target address of the key.
* There are two types of branches: normal and inverse. Normal branch uses key X in one program and inverse uses it in another, with each controlling its own static key (X).
* To use BPF static keys, you need to provide additional formation for patch code, including setting instruction PGE, jump target, and the actual static key used for toggling branches.
* The static key map is a global variable represented as an array of size one in BPF.
* Static keys can be used multiple times in different programs, with each program controlling its own normal and inverse branches.
* When a static branch is triggered, the key value is written to the map (0 for disabled, 1 for enabled).
* The user space needs to prevent programs from accessing the static key map directly.
* To enable or disable BPF static keys at runtime, you can use the `BPF_PROG_LOAD` flag with a different kind of pointer const pointer map value.
* BPF verifier checks for static keys when uploading programs and re-verifying them if necessary.
* Performance improvements include bypassing one jump and avoiding recompiling programs.
* Static keys can be used for tracing, enabling or disabling features, and conditionally patching programs.
* Alternatives to static keys include using p instructions or replacing the entire program with a patched version.
* Verification is more complex for static keys as it requires saving state every occurrence of the branch and keeping track of the verifier path.
* The original API defines static keys using `Define static key true/false` with Wmap create map assign 01 load program world multiple program use static key share staticy map.
* Infrastructure for managing static keys automatically is needed without helper flags or manual intervention.


## Troubles and Tidbits from Datadogs eBPF journey -  Guillaume Fournier, Hemanth Malla

URL: [https://www.youtube.com/watch?v=FvaR0zbDQ1c](https://www.youtube.com/watch?v=FvaR0zbDQ1c)

 * Datadog is a cloud observability and security platform.
* The speakers have experience building a security product based on eBPF at Datadog.
* They want to share issues encountered during development.
* Product name: Cloud Security Management.
* Goal: Detect threats in time using eBPF in cloud environments.
* Initially, targeted major Linux distributions and Cloud providers.
* Needed to write deduction engine user space, not kernel space.
* Encountered issues with hook points, data collection, and environment.

**Hook Points:**

* Missing hook point led to blind spot bypass.
* Incompatible Trace Point (TC) classifier caused compatibility issue.
* Specificity of Trace Point needed for effective use.

**Data Collection:**

* Needed to collect CLE arguments and return values for context.
* UDP didn't send events within the product, causing missed coverage.
* The interpreter problem affected rule execution.

**Environment:**

* Ensured environment destruction does not affect the solution.
* Handled memory kill and Kernel parameters to optimize performance and security.

**Networking:**

* Service connectivity issue with Celum (Kubernetes networking layer).
* Identified BPF map pressure and resizing issues.
* Implemented a standalone DNS proxy to solve dependency problems.


## eBPF Shenanigans with Flux - Barret Rhoden

URL: [https://www.youtube.com/watch?v=MRvTDcadqIw](https://www.youtube.com/watch?v=MRvTDcadqIw)

 * Barrett Rhoden talks about Flux, a scheduling framework written in eBPF
* Flux is designed for large multicore machines with complex cache topologies and different types of thread workloads
* The idea is to partition CPUs for specific thread types using sub-schedulers
* Sub-schedulers are responsible for making scheduling decisions based on policies like EDF, FIFO, or fair share
* eBPF allows the framework to communicate with user space agents and adjust policies as needed
* The data structures used in Flux include arrays, maps, and linked lists, with a focus on object-oriented programming without function pointers
* Memory management is handled through arrays and maps, which are unmappable for security reasons
* Flux uses a hierarchical scheduler structure with smaller sub-schedulers responsible for specific thread types
* The framework uses a simple Blob code design for efficiency, with short names and minimal function calls
* The talk covers the overall architecture of Flux, focusing on the eBPF aspect and data structures used.


## Developing Continuous eBPF Profiler to look Beneath the Kernel to Beyond the Clouds - Sumera

URL: [https://www.youtube.com/watch?v=ZnCNv1_Eoac](https://www.youtube.com/watch?v=ZnCNv1_Eoac)

 * Speaker introduced herself and her background in graphics subsystem and profiling
* Described her experience with various tools like FTRACE, FlameGraph, and Coxal analysis
* Expressed the need for a developer-friendly continuous profiler that could provide high-resolution profiles across user space, kernel space, and different languages and runtimes
* Introduced Parker, an inverted stack trace profiler, which is like an inverse flame graph
* Discussed Parker's architecture, with one server component and one agent component using eBPF
* Explained how Parker collects and saves high-resolution dynamic profiles across the entire system, including user space and kernel space
* Demonstrated Parker's user interface, which provides detailed information like function names, memory addresses, and line numbers
* Discussed the challenges of making a continuous profiler work in a cloud native environment and the importance of low overhead and efficient processing
* Detailed how Parker works in user space, using eBPF to read stack traces across processes and extract unwinding information from debug info
* Explained how Parker builds unwind tables and extracts relevant information for various architectures like ARM64 and x86
* Discussed the importance of symbolization for providing human-readable information, which usually happens on the server side
* Mentioned that Parker sends profile data to the server every 10 seconds and uses a simple buffer for sending wine table row information.


## Towards a standardized eBPF ISA - Conformance testing - Alan Jowett

URL: [https://www.youtube.com/watch?v=f3-mP5Bu_do](https://www.youtube.com/watch?v=f3-mP5Bu_do)

 * Alan Jowett, developer at Microsoft and maintainer of the Windows eBPF conformance project, presents an overview of the BPF ISA conformance testing tool
* The goal is to validate the draft BPF ISA against Linux kernel BPF and ensure interoperability across platforms
* BPF is a synthetic ISA that doesn't rely on specific hardware, and a standardized part is necessary for portability
* The ETF working group developed the BPF conformance tool to measure actual behavior against the draft specification
* Identified discrepancies in the division operator behavior between different BPF runtimes
* Long-term goal is to provide an authoritative way to check whether a BPF runtime matches the ITF specification
* Also includes security testing using Prevail verifier and Behavior isolator
* The tool allows experimentation with various BPF byte code sequences without the complexity of Linux BPF runtime complications
* Conformance testing approach: declare initial state, test sequence, execute VPF instruction, check expected return value
* Challenges include handling platform-specific exceptions and APIs, as well as different ways to invoke and run the BPF runtime
* The conformance suite consists of a runner, test code, and plugins for each BPF runtime
* Linux plugin is relatively small and accepts BPF byte code, creates a program, loads it into the kernel, and executes the test
* Plugins are designed to be simple and overhead-friendly
* Prevail verifier emulates BPF byte code execution and checks post conditions to ensure they match the expected value.
* RBPF-UBF (Windows) uses a CLI-based approach and converts BPF byte code back to C before compiling it into a native executable that runs on the host system.
* Current challenges include testing against newer Linux kernels with V4 instruction sets, which can be complex and require enhancements to the test cases.


## Standardizing Linux DRM drivers implementations by interfacing DRM Bridge as a single...- Jagan Teki

URL: [https://www.youtube.com/watch?v=IVI30LzPzAA](https://www.youtube.com/watch?v=IVI30LzPzAA)

 * Jag Teki talks about standardizing Linux DRM bridge implementations
* DRM Bridge has been in Linux kernel since version 4.0
* Bridge driver handles plane, CRTC, encoder, and connector within the encoder driver
* With increasing display interfaces, hardware topology is becoming complex with single encoders handling multiple bridges
* Bridge APIs need to be standardized for new device drivers to follow
* Bridge API improvements include: bridge attachment, deferred calls, and bridge categorization based on attachment
* Recent kernel changes affecting bridge API include tagging issues with PDSIs and pre-enable/post-disable flags in bridge chains
* Differences between bridge types include host bridges, display host bridges, and converter bridges
* Advantages of standardizing bridge APIs include easier integration, simpler driver development, and better handling of underlying topology.


## Enabling Large Block Size devices in Linux - Luis Chamberlain, Pankaj Raghav

URL: [https://www.youtube.com/watch?v=ar72r5Xf7x4](https://www.youtube.com/watch?v=ar72r5Xf7x4)

 * Speaker: Lewis Chamberlain from Samsung Global Open Source Team
* Topic: Enabling Large Block Size devices in Linux
* Agenda: Review of use case and plumbing implementation, testing
* Existing storage device use case: Limitations with buffer head implementation, FS block size restriction
* Future technology: Allow new storage device experience with large block sizes
* LBA (Logical Block Addressing) format change: Enabling larger block sizes in Linux filesystems like XFS
* Large I/O workload: Improved performance with larger folios and Atomic support
* Database use case: Support for large atomics, direct IO, and large IU (Indirection Unit) size
* Implementation: Adding max support, enabling XR multiindex support, fixing bugs
* Testing: IO distribution analysis, benchmarking, stress testing
* Hardware consideration: NVMe device, preallocating zero pages for huge pages
* Ongoing discussion: Kernel improvements, large LBA format support, and large Atomic support.


## Linux Kernel Autotuning - Cong Wang

URL: [https://www.youtube.com/watch?v=92rMMVAmeH8](https://www.youtube.com/watch?v=92rMMVAmeH8)

 * The speaker, Cong Wang from System Technologies engineering team, discusses Linux kernel autotuning and the potential benefits of using machine learning (ML) in this area.
* Reasons for considering autotuning:
  + Tune performance to save engineering effort and time.
  + Difficulty in making optimal decisions as a performance engineer.
  + ML could potentially find optimal solutions with specific workloads.
* Differences between traditional programming and ML:
  + In traditional programming, the programmer writes code that takes data as input, performs computation, and produces output.
  + In ML, data is used as both input and output, and the model learns patterns from historical information to make predictions or decisions.
* Machine learning could help in the following areas of Linux kernel tuning:
  + Prediction based on historical data for knowledge tuning and analysis.
  + Cost analysis for resource optimization.
  + Classification of different problems and their solutions.
  + Optimization using machine learning algorithms to find optimal parameters for specific workloads.
* The speaker discusses three examples of Linux kernel subsystems that could benefit from ML:
  + Memory access optimization with Diamond (DTrace).
  + Performance evaluation of network servers using statistical tools.
  + Optimizing task scheduling in the scheduler (sched_core) using machine learning algorithms.
* The speaker also mentions some challenges and considerations when implementing ML in the Linux kernel:
  + Limited floating point resources and potential overhead.
  + Tolerance for errors and potential loss of accuracy or stability.
  + Use cases where floating point calculations are not necessary.
  + Possible use of ebpf (extended Berkeley Packet Filter) for machine learning in the Linux kernel.
* The speaker concludes by emphasizing the importance of ML in Linux kernel tuning and the potential benefits, despite the limitations discussed.


## Standardizing CPUID data for the open-source x86 ecosystem - Ahmed S. Darwish

URL: [https://www.youtube.com/watch?v=owZ-rXsPLh4](https://www.youtube.com/watch?v=owZ-rXsPLh4)

 * Ahmed Darwish from Latronics spoke about standardizing CPUID data for the open-source x86 ecosystem
* CPUID instruction: takes input in ECX register, outputs information about supported features of the CPU
* Output format is number bit fields in EAX,EBX,ECX,EDX registers and extended registers EX,EBX,ECX,EDX for modern CPUs
* Software ecosystem assumes availability of CPUID instruction in both kernel and user space
* Serializing instruction information for string manipulation using tools like GCC and LLVM
* CPUID instruction provides bit fields covering around 30 important features of the x86 architecture
* Demonstration using inline GCC assembly code
* Linux command "lscpu" and tool "Todd Allen CPU ID" show output of CPUID Leaf 1, which includes vendor ID string and standard feature information
* Modern Intel CPUs may have masking of MSRs and AMD CPUs might override mask to make features appear
* Challenge: Linux kernel representing CPUID information efficiently and accurately
* Ugly bitwise handling in existing Unix kernel code
* Proposed solution: a hierarchical, annotated tree data model for CPUID information that is extensible, understandable, and machine-readable.
* Evaluated various formats like yaml, toml, S expressions, and XML for the data model
* Plan to use XSLT to transform XML data into a usable format for Linux kernel and other projects
* Future work: building CPUID database and tools for evaluation and updating as new CPUs are released.


## Hunting Heisenbugs - Paul McKenney

URL: [https://www.youtube.com/watch?v=gshynRXwrm8](https://www.youtube.com/watch?v=gshynRXwrm8)

 * Paul McKenney discusses hunting Heisenbugs, which are bugs that are difficult to reproduce due to their timing dependence
* Heisenbugs can cause significant problems in software engineering, especially when they lead to long downtime or safety critical issues
* Heisenbugs can be hard to detect because they only occur under specific conditions and may not always replicate consistently
* One example given is a 10,000 year bug that occurred every hundred hours on a million system fleet
* The speaker mentions that avoiding Heisenbugs is important, as fixing them can be time-consuming and costly
* Techniques for hunting Heisenbugs include adding debugging tools, using statistical analysis, and looking for patterns in system logs
* One technique mentioned is RCU torturing, which involves injecting delays to promote race conditions and make Heisenbugs more likely to occur
* Another approach is to use a distributed tracing system to identify the root cause of complex issues
* The speaker shares some personal experiences of dealing with Heisenbugs in large-scale systems and the importance of proper testing and debugging practices.


## nouveau and kernel GPU VMA management - David Airlie

URL: [https://www.youtube.com/watch?v=k13dcUrSx40](https://www.youtube.com/watch?v=k13dcUrSx40)

 * The speaker discusses the history and challenges of managing GPU virtual memory address allocators in Linux, specifically with Nvidia GPUs
* The talk covers the motivations behind the Nouveau project and the limitations of using proprietary firmware
* The speaker mentions the design choices made in the Nvidia driver, such as versioning and message passing
* The discussion touches on the challenges of managing large firmware files and potential solutions like using common init ramfs or separate boot partitions
* The speaker discusses ongoing efforts to refactor and improve the Nouveau driver, including work on GSP (GPU Scalable Page Table) and Vulkan support
* The talk mentions the importance of community collaboration and the challenges of managing critical sections and memory allocation in the driver.


## Putting Linux into Context – Towards a reproducible example system with Linux... - Philipp Ahmann

URL: [https://www.youtube.com/watch?v=xUPOAUAbGwI](https://www.youtube.com/watch?v=xUPOAUAbGwI)

 * Philipp Ahmann, a traditional kernel developer and product manager, discusses the context of Linux in safety applications
* Functional safety refers to avoiding risk to human life and ensuring a system remains operational even if an intrusion occurs
* Elisa project, a Foundation project, aims to provide safety certified Linux for various industries, including aerospace and automotive
* Use cases include Boeing in Aerospace and medical devices like the open APS artificial pancreas system
* Open source engineering process is important in ensuring safety, with tools like workload tracing and static analysis used for investigation
* System setup and integration are crucial for safety, with documentation and admin guides playing a key role
* The community also plays a significant part in safety, with tools and support available to help ensure proper handling of Linux images and licenses
* Challenges include ensuring compatibility with specific hardware and dealing with complex use cases like autonomous driving vehicles
* The talk covers various topics including synchronization, resource management, memory allocation, and interrupt handling, among others.


## Dynamic vCPU priority boosting in KVM for latency sensitive workloads- Joel Fernandes, Vineeth Pilla

URL: [https://www.youtube.com/watch?v=47YzSIWUXeI](https://www.youtube.com/watch?v=47YzSIWUXeI)

 * The speakers discussed an issue of latency in virtual machines (VMs) running on Kernel-based Virtual Machine (KVM) for Chromebooks and Android apps.
* The main problem is double scheduling, where the host operating system doesn't know which VM vCPU is currently running, causing ineffective decisions and latency.
* To address this, they propose a solution of sharing scheduling parameters between the guest and host to make informed decisions.
* The speakers also mentioned a priority inversion issue with dynamic boosting of vCPUs, where an unboosted vCPU could take a spin lock, blocking a boosted vCPU from running.
* They went over an implementation using MSR writes, structure sharing, and hyper calls to enable and disable the feature globally for synchronous and asynchronous boosting.
* The discussion also touched on security concerns regarding untrusted VMs requesting priority boosts and potential impact on other VMs.


## RCU Office Hour - Paul McKenney

URL: [https://www.youtube.com/watch?v=WYhN99HouNo](https://www.youtube.com/watch?v=WYhN99HouNo)

 * Paul McKenney discussed RCU (Read-Copy Update) during an office hour session
* He mentioned several issues and experiences related to RCU in Linux Kernel development
* Some of the topics covered were: poll requests, CPU stall warnings, debugging tools, RCU momentary qu state, idle CPUs, power consumption, and testing
* He talked about the history of RCU and how it has evolved over time
* McKenney also discussed the importance of minimizing jitter in VM scheduling and using lazy RCUs in Ubuntu
* He mentioned some potential mitigations for performance regressions caused by lazy RCUs
* The conversation included questions from the audience and answers from McKenney.


## Improve Linux Perf tool to account for task sleep - Ajay Kaher, Alexey Makhalov

URL: [https://www.youtube.com/watch?v=sF2faKGRnjs](https://www.youtube.com/watch?v=sF2faKGRnjs)

 * AJ Kher and Alexey Makhalov discuss the issue of Linux Perf tool not accounting for task sleep time
* Puf Tool is useful for multithreaded application performance optimization, but it does not provide information on task sleeping time
* Goal is to consider sleeping time in CPU calculation
* Previous solutions considered CPU offline based BPF and capturing sample time instead of sending records
* Proposed solution: Capture sleep samples while the task is sleeping by using HR timer and software event
  * Set up HR timer to capture sample when the task goes to sleep and another one when it wakes up
  * Subtracting wake time from sleep time gives sleep duration
* Calculate CPU usage based on total time spent in user space, including sleep time
* Testing with a simple program demonstrates successful capture of sleeping samples
* Discussed the possibility of using Trace event to compute Sleep Time Delta and perf trace sketch switch for better profiling.


## Powering up “discoverable bus-attached” devices on DT-based platforms - Abel Vesa

URL: [https://www.youtube.com/watch?v=h1CDz-ARQo0](https://www.youtube.com/watch?v=h1CDz-ARQo0)

 * Abel Vesa presented a talk on powering up discoverable bus-attached devices on DT-based platforms
* Proposed solution involves introducing a PCI slot device driver for platform devices with child PCI host controller nodes
* Discussed the need to create and instantiate the device host controller node, probe it, and make it a parent of the PCI device
* Mentioned that Linux already has code for creating slots without a Bucking controller
* Discussed the possibility of using a power sequencing subsystem for simpler handling of generic PCI hot plug drivers
* Previously proposed adding a power sequencing subsystem related to specific Bluetooth WiFi chip, but it was rejected multiple times
* Noted that separate power management functional drivers are needed for devices like BPF and I2C drivers
* Discussed the need for proper power sequencing when hot-plugging multiple devices with shared resources
* Talked about the importance of device enumeration and logic encoding for specific types of buses and devices
* Proposed a single driver per PCI device to handle both device logic and power requirements
* Mentioned that PCI hot plug drivers could identify power sequencing based on device class and describe one set of required power sequences
* Discussed the need for a pre-probe hook call to handle powering up a device before it is probed by the driver
* Noted that hot plugging can cause conflicts with device power requirements, and devices may need to be reset in a specific order
* Talked about the importance of synchronizing power sequences for devices sharing resources, such as GPIOS or reset controllers
* Discussed the challenges of handling power sequencing for multiple devices connected to the same slot, especially when they have conflicting power requirements
* Mentioned that a separate power management subsystem might be necessary for more complex power sequencing requirements
* Noted that the Regulator framework already handles regulator resources, and a separate slot driver could handle Bluetooth and WiFi drivers' power sequencing
* Discussed the need to reference two devices and allow them to share power sequences, but noted that this can be a larger problem when dealing with shared reset GPIOs
* Talked about the importance of device link PM time scheduling and control for handling power sequences for multiple devices separately
* Noted that some devices may require specific timing requirements for power sequencing and that minimum and maximum times need to be considered
* Discussed the need for a hot plug driver to tell which driver should handle hot plugging, as there can be conflicts with multiple drivers fighting for the same slot
* Talked about creating virtual PCI slot devices based on device entries in the DT tree and the importance of identifying compatible strings for new hot plug drivers
* Mentioned that PCI abuses existing Linux interfaces and that there is already a lot of code related to power management in the kernel
* Discussed the need to recognize power sequences and put functional drivers in place as a short-term solution, but noted that a separate power management system may be necessary in the long term.


## Installing and Using the Linux-Kernel Memory Model (LKMM) - Paul McKenney

URL: [https://www.youtube.com/watch?v=YPpojI84WZk](https://www.youtube.com/watch?v=YPpojI84WZk)

 * The workshop is about installing and using the Linux-Kernel Memory Model (LKMM) with the help of tools like Herd7 and Camel.
* LKMM is a tool used to test concurrent code in the Linux kernel.
* Herd7 is a memory model checking tool, and Camel is a language for writing memory models.
* The speaker recommends using Herd7 to install the LKMM tools from source if they are not already installed.
* Camel needs to be installed before using Herd7.
* Installing Camel may require additional dependencies like Dune or Opam.
* Building and installing Herd7 can be a bit tricky and may require some troubleshooting.
* The Linux kernel memory model is important for ensuring atomicity and forward progress in concurrent programming.
* Different architectures like x86, ARM, and PowerPC implement the memory model differently.
* LKMM tests detect risks and ensure that atomic operations do not violate ordering requirements.
* Running litmus tests with Herd7 involves finding a test file within the Linux kernel source tree, building it, and running it to check for correctness.
* The speaker encourages using regression testing to validate changes to memory models.
* Camel uses a specific comment syntax for defining tests and test cases.
* LKMM can help catch bugs that are difficult to find with conventional testing methods.


## kdevops sync up - Luis Chamberlain

URL: [https://www.youtube.com/watch?v=l03FEVyaiKY](https://www.youtube.com/watch?v=l03FEVyaiKY)

 * Luis Chamberlain discussing Kubernetes and DevOps, focusing on moving away from Vagrant
* Convenience of Vagrant for distribution and easy setup, but long-term need for a replacement
* Current solutions: Plumber (vert.x), Kubernetes test frameworks like Clair and KTest
* Challenges with adopting these solutions: Kubernetes config, compatibility with cloud providers, resource utilization
* Possible solutions: Implementing Kubernetes configurations manually or using tools like AWS CLI, Terraform, or Cloudflare
* Potential issues: Storage inconsistencies between cloud providers, SSH connectivity in Kubernetes, pod scheduling and container drops, caching schemes for Docker images
* Discussion on PCI passthrough with dynamic Kconfig, using tools like Ansible and Python scripts to handle SSH configurations
* Cross-platform considerations: Vagrant vs. local virtualization or containers, macOS users' preferences
* Possible alternatives: OpenShift, Terraform, or a combination of both
* Discussion on resource constraints and testing file systems, creating baselines, and collaborating in the community for development
* Encouraging manual patch reviews and using GitHub for submitting and reviewing pull requests.


## Empowering Engagement: Introducing a Dynamic Dashboard for Proactive Retention Strategies

URL: [https://www.youtube.com/watch?v=Oy_t3wke6jk](https://www.youtube.com/watch?v=Oy_t3wke6jk)

 * Steve Im, PhD candidate in Computer Science at Oregon State University, discusses his research on retaining contributors in open source projects.
* Open source projects can lose contributors for various reasons, including technical difficulties and social challenges.
* Data from the Vesta dataset shows that gender minority and non-Western contributors are more likely to leave open source projects due to social barriers and process challenges.
* Retention strategies involve monitoring project status and engaging with contributors.
* The Survival Dashboard is a tool designed to make maintaining open source projects easier by providing quick insights into retention data and predicting the likelihood of contributor disengagement using statistical models.
* The dashboard allows project maintainers to compare survival probability across different demographic groups and regions, and take early action to retain contributors.
* The Survival Dashboard uses a line plot to provide statistical analysis and prediction tools for maintaining open source projects.
* The tool can be used to analyze retention data within an OS community, including the number of active and new contributors and those who have left.
* The dashboard allows project maintainers to send surveys asking contributors to self-report demographic information and identify signals that may impact contributor disengagement.
* The tool uses statistical prediction models to identify potential issues that can lead to contributor disengagement.
* The Survival Dashboard is inspired by GitHub's design and offers a user-friendly interface with four sections: time selector, project overview, demographic comparison, and newcomer analysis.
* The time selector allows maintainers to choose a specific time interval for analysis, while the project overview section provides retention data and the ability to send group emails.
* The demographic comparison section offers insights into survival probability across different demographic groups, while the newcomer analysis section focuses on inactive contributors.
* Project maintainers can use the dashboard to take early action and engage with contributors before they become disengaged.
* The tool uses both automated data mining and self-reported demographic information to provide accurate insights into open source communities.
* Concerns were raised about collecting sensitive demographic information, but it was suggested that the dashboard could be designed to protect privacy and maintain anonymity.
* Overall, the Survival Dashboard is a valuable tool for project maintainers to monitor retention and improve inclusivity and diversity within open source projects.


## KDLP: Kernel Development Learning Pipeline - Joel Savitz

URL: [https://www.youtube.com/watch?v=ANpp5f121Ck](https://www.youtube.com/watch?v=ANpp5f121Ck)

 * Joel Savitz presented Colonel Development Learning Pipeline (KDP)
* KDP is an open-source project aimed at addressing the documentation and onboarding problems in Linux kernel development
* The project includes free course material for a four-credit University course called "Introduction to Linux C Development"
* Students with software engineering background are recruited as interns to improve the curriculum using real student feedback
* KDP provides accessible content for people new to Linux kernel development without prior experience in the field
* The documentation problem includes outdated and difficult-to-navigate resources, while onboarding is a challenge without mentorship or guidance
* Students shared their experiences of struggling to learn and contribute to open source projects without proper resources and support
* KDP aims to create a community where students can learn from each other and work together to improve the documentation and contribute to the project.


## resctrl filesystem - Peter Newman

URL: [https://www.youtube.com/watch?v=j6SB_-CeFHo](https://www.youtube.com/watch?v=j6SB_-CeFHo)

 * Peter Newman discussing 'resctrl filesystem' in a presentation
* recontrol is used for managing and monitoring resources inside Google's shared hosting machines
* Googles Fleet requires sort mechanism, monitoring, bandwidth enforcement, and job isolation
* Intel-centric design with challenges for arm server fleet
* Discussed the difficulty of sharing code across different systems due to underlying hardware differences
* Mentioned issues with L3 cache monitoring and resource contention
* Discussed potential solutions like using a glue layer or an agnostic recontrol driver
* Emphasized the importance of keeping user space architecture standard while adding new features
* Mentioned ongoing discussions about feature parity between Intel and ARM implementations
* Discussed challenges in porting recontrol to different architectures and the need for collaboration
* Discussed potential solutions like adding a new resource type or using a common configuration header.


## Securing build platforms - Joshua Lock

URL: [https://www.youtube.com/watch?v=8zrmQCwogxM](https://www.youtube.com/watch?v=8zrmQCwogxM)

 * Joshua Lock from Verizon Open Source Program Office discussing securing build platforms
* Build platform vs build system: Build platform is software and hardware where trust is placed in produced artifacts, often used in open source projects
* Build systems can be compromised, leading to malicious code being introduced (e.g. GitHub, PHP, SolarWinds)
* Google's Borg and Sala architecture implement binary authorization for increased security
* Open source package managers like Homebrew and npm also adding verification mechanisms
* Linux distributions implementing measures to prevent tampering and improve integrity
* Reproducible builds can help ensure that the same artifact is produced every time, improving security and trust
* Tools like Nix, NYX, and trus XS can aid in ensuring reproducibility across ecosystems
* Containers (VMs) and isolated build environments can increase security by reducing attack surface
* The Sela project is an open source security initiative focusing on secure software supply chains
* Challenges include verifying claims without additional metadata, air-gapping, and ensuring hermeticity (isolation)
* Cube OS and the Linux Foundation have implemented measures to ensure trust in build systems by validating inputs offline and using fixed output derivations
* Bootstrappable builds can help establish trust in an initial binary or image, but care must be taken to ensure it is not already backdoored.


## Improving UAPI Compatibility Review with Automated Tooling - John Moon

URL: [https://www.youtube.com/watch?v=4ijcLgvmcek](https://www.youtube.com/watch?v=4ijcLgvmcek)

 * John Moon from Qualcomm discusses improving UAPI (User Application Programming Interface) compatibility review with automated tooling
* UAPI refers to interfaces in the kernel and user space, including system calls and header files, which can change and break user space programs
* The goal is to maintain UAPI compatibility and prevent user space programs from breaking due to changes in the kernel
* CheckUAPI.sh is a shell script used for automated checking of UAPI changes
* It compares header files and reports any incompatible changes, such as structure size changes or new members added to structures
* The script can also suppress certain types of changes if they are safe and not likely to cause incompatibilities
* However, it can sometimes produce false positives and needs to be supplemented with human review
* Abigail is a library used for ABI serialization analysis, which can help identify breaking changes in binary artifacts built from packages
* Documentation and testing are important for preventing UAPI breakages and ensuring compatibility across multiple Linux releases.


## kernel: build system outputs and workflows (and how to balance them) - Bruce Ashfield

URL: [https://www.youtube.com/watch?v=K2VVXHvS_l0](https://www.youtube.com/watch?v=K2VVXHvS_l0)

 * Bruce Ashfield, maintaining Colonel build system for AMD since 2006
* Build systems: balance reproducibility, flexibility, and speed
* Differing requirements from developers, integrators, and distributors
* Configuration management in embedded development with Colonel build system
* Flexibility allows building different architectures, performance levels, and maintenance support images
* Maintaining user space packages during kernel upgrades
* Verifying binary artifacts and license information
* Different package formats and output traceability
* Balancing priorities: release cadence, testing, and compatibility
* Challenges in embedded kernel development and complex build systems
* Inconsistent quality testing and provenance concerns
* Adopting efficient workflows and handling new requirements
* Communication and resource allocation for ensuring quality testing
* Different use cases and target audiences for open embedded projects
* Documentation, group agreement, and user expectations
* Adoption of build systems: offering flexibility vs. mandating processes
* Testing improvements and runtime reports
* Addressing unique issues in kernel development and deployment
* Increasing coverage through additional configurations and testing sets
* Streamlining developer workflow and reducing overhead.


## How big of a problem are Un-upstreamed patches - Jon Mason

URL: [https://www.youtube.com/watch?v=5QFZptFSgWM](https://www.youtube.com/watch?v=5QFZptFSgWM)

 * The problem of un-upstreamed patches in open source projects is a big issue, especially for beginners.
* Upstream patch refers to modifying the original source code in the upstream project and submitting it back to the project maintainer for acceptance and inclusion in future releases.
* Reasons for not upstreaming patches include:
  + Fear of rejection or lack of response from maintainers
  + Special build environments that may not be accepted by Upstream
  + Patches might contain ugly hacks that could make the Upstream codebase unnecessarily complex
  + Embedded industries may not have the resources to maintain both their customizations and the Upstream project
* The advantages of upstreaming patches include:
  + Using the latest version of software
  + Reducing duplication of effort
  + Improving the overall quality of the codebase
  + Being part of a collaborative community
* Challenges in upstreaming patches include:
  + Long waiting times for maintainers to respond or review patches
  + The need for patches to be of high quality and fully baked before submission
  + The potential for patches to be rejected due to technical debt or conflicting priorities
  + Maintainers may have strict policies around patch submission, such as using specific formats or tagging conventions.
* Strategies for upstreaming patches include:
  + Being persistent and patient in following up with maintainers
  + Making sure patches are well-explained and easy to understand
  + Submitting patches against the latest version of the codebase
  + Engaging with the community around the project to build relationships and gain insight into the development process.


## Building for Heterogeneous Systems - Alejandro Hernandez Samaniego

URL: [https://www.youtube.com/watch?v=Ml8LnbMsRbE](https://www.youtube.com/watch?v=Ml8LnbMsRbE)

 * Alejandro Hernandez discussing building heterogeneous systems using an example of a Raspberry Pi Pico
* Heterogeneous systems: multiple architecture devices with different operating systems (Linux, RTOS, bare metal)
* Current build solutions include BitBake for Linux and vendor-provided toolchains for bare metal applications
* Bare metal application development: clone repo, set environment, build using bare metal toolchain
* Challenges in heterogeneous development: different developer workflows, dependencies, and integrating vendor SDKs
* Two approaches to handling vendor SDKs: creating a native recipe that fetches the SDK or including it in the application recipe
* Multi-config dependency: allows BitBake to use different toolchains and open source software for each configuration
* Shared state reuse: accelerates building by reusing previously built components across multiple configurations
* Example of using multi-config variables, directories, and dependencies in BitBake
* Conclusion: using cross tool chains provides advantages such as quick access to new versions and ease of integration. However, challenges include managing vendor workflows and dealing with multiple configurations.


## Confidential Computing Microconference Introduction - Dhaval Giani, Joerg Roedel

URL: [https://www.youtube.com/watch?v=MXd2uQRV5S0](https://www.youtube.com/watch?v=MXd2uQRV5S0)

 * Welcome to the Confidential Computing Microconference
* Instructions for making the conference a success: volunteers for note-taking, remote audience participation, use of microphones and chat for discussions during Q&A sessions.
* Remote audience encouraged to join discussions but keep mic usage minimal to allow for smooth conversations.
* Multiple discussions are welcomed and can continue after a talk's end in the "hallway track."
* Invitation to begin the session by inviting a speaker.


## COCONUT Secure VM Service Module Discussion - Joerg Roedel

URL: [https://www.youtube.com/watch?v=ogaxVqUzVOk](https://www.youtube.com/watch?v=ogaxVqUzVOk)

 * Coconut SSM (State Service Module) is a project that supports Linux VM management and virtual memory, with features like checker support, R format support, and clippy for Rust safety checks.
* The future roadmap includes getting CP3 support, cleaning up the codebase, adding a persistence layer, and supporting IGM file format for storing initial state information securely.
* IBM's IGM file format is used to describe initial memory and register states of confidential virtual machines. Hypervisors use this file to get unified hypervisor interface information.
* Implementing a dedicated block device or object store for persistence layer storage is being considered, with encryption and integrity protection required.
* Memory management involves getting rid of direct map support and implementing smart pointers, possibly using different backend allocators.
* Smart pointers in Rust need to be stabilized before implementation, along with governance and ownership issues.
* Other topics for discussion include LSM calls, life migration, UFI variable store, secure IQ injection, T architecture support, device emulation, running non-Linux operating systems, and providing secure service VMs.
* A question was raised about Rust's shared memory ownership model and how it can be reconciled with page sharing in host memory.
* Predictable launch measurement is a goal, with IBM's IVM taking the initial state file and comparing it to the expected launch measurement to ensure correct loading across hypervisors.
* Coconut was initially written for dedicated guest mode memory allocation (256MB) but now wants to isolate CPUs, tasks, and pcpu mappings for better isolation promises.


## Remote Attestation in AMD SEV-SNP Confidential VMs - Claudio Carvalho

URL: [https://www.youtube.com/watch?v=whBG9t67RcY](https://www.youtube.com/watch?v=whBG9t67RcY)

 * Claudio Carvalho from IBM discusses remote attestation in AMD SEV-SNP confidential virtual machines
* Virtual TPM (vTPM) is used for securing confidential virtual machines, which cannot be accessed directly by the hypervisor due to trust issues
* vTPM runs inside a secure enclave within the confidential virtual machine
* Confidential virtual machine memory is encrypted and only the hypervisor can access the vTPM state when running inside the SVM (Secure Virtual Machine)
* vTPM state includes SES key hierarchy, object store, DPM, etc., and its security depends on whether it needs to persist across boots, which varies by application requirements
* Initial vTPM state is generated during manufacturing and securely persisted outside the confidential virtual machine for every boot
* Remote attestation using keyme setup includes registering the confidential virtual machine with a verifier that enforces policy, launching measurement validation, and runtime attestation
* Keyme tool is used to upload the initial state and load the expected initial state on every boot for secure communication between the confidential virtual machine and the verifier
* SP report contains information about the vTPM and its endorsement public key, which is used for verification by open-source frameworks and hardware certifiers.


## Shrinking The Elephant - A Confidential Computing Attestation Sequel - Samuel Ortiz

URL: [https://www.youtube.com/watch?v=VFqjhrAu8Go](https://www.youtube.com/watch?v=VFqjhrAu8Go)

 * Samuel Ortiz discussing attestation in Confidential Computing
* Importance of attestation for remote and local scenarios, especially in cloud environments
* Fragmentation is a challenge in attestation due to various interfaces and formats used by different manufacturers
* Attestation report format verification is complicated as each manufacturer has their own format and verifier requirements
* Verifiers need to check both the attestation report format and the reference value provided by the issuer
* The use of a trusted third-party attestation service can simplify the process, but it introduces additional complexity
* Attestation evidence is often architecture-specific, which makes it difficult to manage and verify across different platforms
* Intel's Amber project is an example of an open specification for attestation results and tokens
* Device attestation is also important in the context of Trusted Platform Modules (TPMs) and virtual machines (VMs)
* The overall attestation process involves detecting devices, verifying their attestation results, and combining them into an overall report
* User space components can also be involved in the attestation flow, sending and receiving attestation reports
* There are ongoing efforts to improve the attestation evidence format and make it more standardized across different silicon manufacturers.


## How to Build a Confidential Attestation Client - Tobin Feldman-Fitzthum

URL: [https://www.youtube.com/watch?v=-KlxhL078jk](https://www.youtube.com/watch?v=-KlxhL078jk)

 * Tobin Feldman-Fitzthum discusses building a confidential attestation client and potential security considerations
* Worst possible thing that could happen is an attacker gaining access to the guest and generating a valid measurement report, impersonating the guest and stealing secrets or reports
* Two strategies proposed: revoking access ability to generate reports or using unique host data in reports
* Complexity of implementing Evidence Factory as a barrier is debated, with concerns about potential attacker conspiring with the host or CSP
* Discussion on metadata verification and internal vs external ways of resolving tacit agreements
* Network communication between the confidential attestation client and key broker service needs to be resolved.


## Supporting Live Migration of Confidential VMs in KVM - Pankaj Gupta

URL: [https://www.youtube.com/watch?v=Zp30_kF_4u8](https://www.youtube.com/watch?v=Zp30_kF_4u8)

 * Pankaj Gupta discussing live migration in KVM
* Common API used for live migration with QEMU and Coco BMS
* Source and destination hypervisors communicate to generate and validate migration data
* Public and private keys exchanged between source and destination
* Metadata needs to be gathered by the source and sent to the destination
* Private pages are transferred in a steady state migration, using KVM's SVSM
* Live migration may be used for upgrading hosts, handling platform failures, and improving performance
* Migration completion involves taking the VM out of service and destroying it
* Design involves migrating SVSM state to the destination and upgrading SPSM if necessary
* Security concerns include ensuring trusted communication between hypervisors and managing CPU states
* Live migration attestation may involve changing the machine's attestation report or implementing policies for older and newer machines.


## Secure IO - Dan Williams, Jeremy Powell, Samuel Ortiz, Steffen Eiden, Thomas Lendacky

URL: [https://www.youtube.com/watch?v=ZNISljqvpAQ](https://www.youtube.com/watch?v=ZNISljqvpAQ)

 * Secure I/O: encrypted guest kernel, virtualized platform, trusted device communication
* State machine: locked/unlocked virtual functions, firmware trust, spdm session, secure channel
* CoIO risk: eliminate bounce buffering, prevent malicious device replaying
* TSM specification: binding virtual function within physical device, establishing secure encrypted channel
* TDI vs PCI: different security measures for different types of devices
* AMD vs Intel: similar architecture but different approaches to security
* SPDM vs TLS: two methods for establishing secure logical channels
* Key exchange and certification: secure key exchange protocols, certificate signing and reporting
* Principle: simplicity as a guiding principle in designing security solutions
* TSM boundary: managing keys, defining trust relationships between devices
* TDX vs TPA: differences in function, potential need for separate components.

The speakers discuss the concept of Secure I/O, focusing on encryption and virtualization to secure guest communication with trusted devices, as well as preventing malicious device replaying and bounce buffering. They explore different approaches to establishing secure channels using state machines, spdm sessions, and secure key exchange protocols with certificate signing and reporting. The importance of simplicity in designing security solutions is emphasized, along with managing trust relationships between devices and understanding the differences between TSM and TDX implementations.


## Taming the Incoherent Cache Issue in Confidential VMs - Mingwei Zhang

URL: [https://www.youtube.com/watch?v=UJt8dok4oPU](https://www.youtube.com/watch?v=UJt8dok4oPU)

 * The speaker, Mingwei Zhang, discusses the issue of incoherent caches in Confidential VMs and how it was addressed
* Incoherent cache refers to physically different cache lines holding independent dirty data for different virtual machines (VMs)
* This can result in data corruption when one VM's cache line is evicted and another VM writes to the same physical page
* A simple solution proposed in 2017 was a cache flush whenever a VM is destroyed
* However, this approach has performance implications and can cause significant segregation of caches
* The speaker then introduces the use of MM Notifier as a better solution for handling cache coherency at the hardware level
* AMD implemented a CPU feature called Coherent Cache to recognize and enforce cache coherency at the hardware level, reducing the need for cache flushing
* KVM, a popular virtual machine manager, uses an MM Notifier interface to hook into the memory management system and manage cache flushing
* The order of cache flushing is important to retain security properties and minimize performance regression
* Filtering which pages are flushed can help reduce the number of cache flushes and minimize performance impact on VMs running on the host
* The speaker suggests that beyond cache flushing, other approaches such as NUMA balancing or SCVs may be needed to prevent attacks
* There is a need for careful consideration when implementing cache management solutions in virtual environments.


## Towards unified confidential computing ABIs - Dan Williams

URL: [https://www.youtube.com/watch?v=E3ScXIpkL3Y](https://www.youtube.com/watch?v=E3ScXIpkL3Y)

 * Dan Williams discussed the need for a unified Confidential Computing ABIs in the Linux community
* There have been discussions about different claim handling and assertion methods between AMD and Intel
* The goal is to bring people together with a common language and negotiate better
* Adaptation reports are a concern as they can be binary incompatible and cause ABI breaks
* Differentiation among vendors is an instinct, but standardization did not happen before
* Colonial ABI was proposed to address these issues, but there were concerns about enforcement and compliance
* A code-first approach was suggested for confidential computing specifications
* The ACPI working group and Consortium have identified the need for change in their processes
* TDX way of asking for a common transport format was proposed, with Intel and AMD both agreeing to it
* Discussions about data structures and interfaces continue, with the goal of minimizing collisions and simplifying things
* Nitro secure module (NSM) was proposed as a multifunction device, but its complex TPM report format is not a good fit
* The need for public key provision and random user data in the adaptation report was discussed
* Different TDX SP flavors were acknowledged, with Intel and AMD having different perspectives
* Colonel said they would try to move towards a common interface to make things easier
* Discussions about complexity and potential complications were addressed, with the goal of moving towards a baseline and not letting things stray too far.


## Update on RISC-V Confidential VM Extension (CoVE) - ATISH PATRA,  RAVI SAHITA

URL: [https://www.youtube.com/watch?v=mz9H6jUDP2g](https://www.youtube.com/watch?v=mz9H6jUDP2g)

 * Update on RISC-V Confidential VM Extension (CoVE)
* Cove is a confidential VM extension for RISC-V
* Allows multiple supervisor domains: tee and confidential computing domain
* Proposed extensions include memory tracking table (MTT) and advanced interrupt architecture
* MTT adds physical access checks to PA coming translations, biased towards large pages
* Peer model uses second level translation structure with root hypervisor not requiring MTT
* CoVE aims to keep the ABI consistent across different use cases: TSM root mode, peer model, and hypervisor
* CoI (Co-processing Interface for I/O) ABI is being worked on to extend Co ABI for Tee I/O
* Goal is to define a clear ABI instead of defining architectural building blocks for software to build upon
* Memory tracking table is a simple structure operating in conjunction with SV paging architecture in RISC-V
* Cove architecture keeps things simple and enforces access allowed by the supervisor domain.


## Secure TSC for AMD SEVSNP guests - Nikunj Dadhani

URL: [https://www.youtube.com/watch?v=SHyH-CfS0rc](https://www.youtube.com/watch?v=SHyH-CfS0rc)

 * Nikun discusses securing Time Stamp Counter (TSC) for AMD Secure Processor (SEV-SNP) guests
* TSC is a counter that tracks processor cycles
* Two methods: Legacy method using RDTSC interface, and SCV (Secure Virtual Machine) method
* SCV guest produces feature called secure TSC
* Hypervisor cannot change guest TSC value through hypervisor-controlled parameters
* New MSRs introduced for guest read frequency and rTSC instruction to prevent interception by the hypervisor
* Live migration involves getting information from physical TSC, calculating new ratio, and keeping it consistent
* Secure TSC enables VM to run at desired frequency by updating vmsa page
* AMD security processor values need to be queried during boot
* Communication channel is encrypted using SNP guest message for secure TSC offset and scale information exchange
* Guest decrypts and programs auxiliary processors with the scaled VMSA value
* SCV SNP feature is optional, guest may need patching for enabling secure TSC
* Check if guest supports secure TSC and SCV SNP feature before launching
* Some SPM (Security Processor Management) related things might require enlightenment for the guest
* VM entry/exit might be slow with Enlightenment, but it's worth considering for better security.


## Secure AVIC: Securing Interrupt Injection from a 'malicious' Hypervisor -Kishon Vijay Abraham I

URL: [https://www.youtube.com/watch?v=0LGqYAS2u5w](https://www.youtube.com/watch?v=0LGqYAS2u5w)

 * Speaker is Kishon Vijay Abraham presenting about AMD's Secure AIC (Advanced Programmable Interrupt Controller)
* Secure AIC is a security feature for APIC virtualization, focusing on three main areas: ACC relation, acceleration, and interrupt injection
* Interrupt injection device is the focus
* Secure AIC operates in single VMPL mode with enlightened guest support (VC Handler emulates additional functionality)
* Supports X2 APIC mode
* New set register called "allow IRS" mimics normal IR and allows for interrupt injection
* Hardware architecture: APIC backing page is managed by the hypervisor, and a new set register called "requested IR mechanism" is used for interrupt injection
* Software architecture: IPI (Interrupt Processor Interrupt) handling, apic register access, and emulated device interrupt
* In single VMPL mode, guest tries to inject an emulated device interrupt, which requires the host to set the allow IR bit in the guest's epic backing page
* Data structures and different scenarios involve VM exit, requested IR code movement, clear bit, handle injection, and update IR bit
* AIC secure and AMD-Vi are mutually exclusive and require feature enable through MSR (Machine Status Register)
* New IRQ domain is being introduced to block irqs for specific purposes
* Goals include preventing guest from eating interrupts and avoiding potential races
* VC Handler couldn't fully customize APIC model, but it could potentially be an option
* Current status includes IPI and SCP injection support; prototyping is ongoing for NMI, timer, and other emulation supports
* An issue with requiring the gas backing page to always be present is currently being addressed.


## Improve Xeon IRQ throughput with posted interrupt - Jacob Pan

URL: [https://www.youtube.com/watch?v=vzKBnBrPYY0](https://www.youtube.com/watch?v=vzKBnBrPYY0)

 * Jacob Pan from Intel discusses improving Xeon IRQ throughput using posted interrupts
* Background: Performance dropped in Cloud engineer's Gen 5 MME disc attached to socket, issue related to interrupts
* Previously, interrupt delivery involved system software control and was inefficient
* With posted interrupts, notification is sent directly to the CPU without hypervisor intervention
* Hardware flow of interrupt delivery involves IMU (Interrupt Moderation Unit) fetching and sending notifications to the CPU
* Posting interrupts eliminates software touchpoints, reducing latency
* Problem: High-frequency interrupts arrive when CPU is already busy processing interrupt handlers, resulting in a slowdown
* Solution: Coalescing of interrupts using posted MSI (Message Signaled Interrupts) coalescing patch
* Differences between MSI and posted interrupts: MSI vector multiplexed to one single notification vector, system software control required for MSI ordering
* Posted interrupts can be delivered in a transparent way without requiring system software intervention
* Testing showed significant performance improvement with Fio benchmark testing on Samsung Gen5 MVME drives
* Feedback and evaluation ongoing to address potential downsides and impacts on lower interrupt rates and Intel interop remapping chip change.


## PCI Endpoint Subsystem Open Items Discussion - Manivannan Sadhasivam e3

URL: [https://www.youtube.com/watch?v=1tqOTge0eq0](https://www.youtube.com/watch?v=1tqOTge0eq0)

 * Manivannan Sadhasivam from Quanta Cloud Services discussing PCI Endpoint Subsystem Open Items
* Agenda: Vero APF driver interoperability, device integration, managing output window memory
* Vero: open standard communication driver for different types of devices
* Developed by Rusty Russell for Algust hypervisor, used in virtualization environments and outside of it
* Independence of two entities: single hypervisor can run multiple guest operating systems without worry about exposing frontend drivers to each other
* Proposed adding Vero support to endpoint framework for simplified architecture and reduced fragmentation
* Linux traditionally uses host PCI subsystem, but separate PC Endpoint Subsystem added for better management of endpoint controllers and functions
* Host machine runs Linux operating system, endpoint device can have proprietary firmware
* Endpoint controller manages PCI transport on behalf of the endpoint soft system
* Endpoint function driver defines actual behavior of the device
* Proposed using Vero for PC Endpoint Subsystem to reduce development time and fragmentation, using existing frontend drivers without modification
* Three proposals discussed:
	+ Haian Bank's proposal from 2019 used Legacy PCI transport due to endpoint subsystem limitations with vendor-specific capability registers
	+ Kishon's proposal introduced Vhost EPF driver for offloading data plane handling using the vhost library and existing Vos net driver
	+ Shuk's recent proposal used Ving H helper in the vhost library for transferring data between frontend and backend and creating a vertical net device host.
* Discussion did not reach a conclusion, but major use case is RP message-based communication in automotive industry
* Using Vero for hardware offloading via VDPA is an option, but not discussed in detail
* Other possible approaches include symmetrical driver side and using a generic polling mechanism.


## Non-discoverable devices in PCI devices - Lizhi Hou, Rob Herring

URL: [https://www.youtube.com/watch?v=MVGElnZW7BQ](https://www.youtube.com/watch?v=MVGElnZW7BQ)

 * Discussion about nondiscoverable devices behind PCI devices
* Problems with using existing solutions like device tree and ACPI for discovering and managing these devices
* Use cases include AMD FPGA PCI cards, microchip ethernet switches, CXL testing, BMC devices, and FTVI serial chips
* Need to dynamically describe and program nondiscoverable devices
* Challenge is that the number of bars (TCI, PCF, etc.) and their sizes may vary between different images
* Discussion about using a data-driven approach for discovering these devices rather than hardcoding in drivers
* Use of device tree overlay as a solution to add support for nondiscoverable devices without needing to leverage the device tree maturity or introducing another way to describe profiles
* Need to address runtime addressing translation issues and potential conflicts between ACPI and device tree nodes
* Discussion about adding test clock subsystems and the need to add test DT nodes for them
* Issue with node ref counting and the difficulty of getting it right
* Possible solutions include creating a new PCI device node, using an ACPI overlay as a debug feature, or considering SCPI overlays if SPI support is available.


## IOMMU overhead optimizations and observability - Pasha Tatashin, Yu Zhao

URL: [https://www.youtube.com/watch?v=lsf_j9VTS8s](https://www.youtube.com/watch?v=lsf_j9VTS8s)

 * Pasha Tatashin from Google discusses observability and optimizations for IOMMU (Input/Output Memory Management Unit) page table overhead
* The goal is to understand kernel memory usage, reduce size of hypervisor, and find uncategorized memory used by the kernel
* A problem encountered was seeing OOMs (Out of Memory) due to larger than expected page tables
* AMD and Intel machines were tested, with AMD not showing the issue because of a larger hypervisor slot on the machine
* The idea is to reuse VA (Virtual Address) space for mapping pages and freeing unused map entries inefficiently
* A proposal includes using a rev count number for each page table level entry to determine when it reaches one allocated byte, at which point it can be freed asynchronously
* The conversation also covers the possibility of adding a free list or implementing a different algorithm for IO page table sharing between drivers like VFIO and IUFD
* Other concerns include thread synchronization for freeing pages, the impact on performance, and the use of RCU (Real-Time Computing) work in freeing pages.


## iommufd discussion - Mr Jason Gunthorpe

URL: [https://www.youtube.com/watch?v=IE_A8wSWV7g](https://www.youtube.com/watch?v=IE_A8wSWV7g)

 * Jason Gunthorpe discussed IOMMU and advanced hardware features in the context of IUFD (Intel Unified Memory Architecture for Direct Memory Access)
* IUFD allows virtual machines to access advanced hardware features directly, such as CPUs, PCI devices, and QEMU
* The team has developed a new vfio-cdev interface for easier access to vfio devices without the need for containers or groups
* IOMMU hardware will be integrated with KVM in future processors
* New features include language objects for managing IOMMU resources and support for non-KVM based applications
* Work is ongoing on shadowed I/O, VIMU emulation, accelerated guest IO page tables, and PCI device migration
* The team has made progress on live migration of PCI devices using the system IO menu generic processor feature
* Ongoing challenges include IO TLB invalidation forwarding, dma dirty logging, and support for peer-to-peer DMA.


## Linux-wpan updates - Mr Stefan Schmidt

URL: [https://www.youtube.com/watch?v=yqdGdEmLRrU](https://www.youtube.com/watch?v=yqdGdEmLRrU)

 * Linux Wpan updates presented by Stefan Schmidt
* Kernel and user space updates for Linux Wpan (Wireless Personal Area Network)
* E8254 subsystem for low power, low rate wireless systems
* Discussion on encryption and security issues in the kernel
* User space update: Netlink interface for managing IPv6 over low-rate wireless networks
* Simplification of code and bug fixes in previous releases
* Introduction of new features like coordinator interfaces, beaconing support, and passive scanning
* Ongoing work on management handling and limited device support
* Potential integration with Network Manager for easier setup and configuration
* Current challenges include IPv6 handling, battery usage, and coordinator functionality in embedded systems.


## TSCH@Zephyr: IEEE 802.15.4 SubG IIoT in the Making - Florian Grandel

URL: [https://www.youtube.com/watch?v=0_nGPXTejgw](https://www.youtube.com/watch?v=0_nGPXTejgw)

 * Florian Grandel spoke about TSCH@Zephyr and Sub-GHz IIoT at IEEE 802.15.4
* Originally discussed CC13XX driver for Zephyr and time synchronization in TSCH (Time Synchronized Channel Hopping)
* Discussed the progression of physical layers, from simple transmit/receive to ultra-wide band with spatial resolution and timing issues
* Mentioned applications such as home automation, industrial use cases, and indoor navigation
* Talked about Zephyr's role in time network interfaces and dual-stack support
* Discussed the collaboration between Linux Foundation, Nordic Semiconductor, NXP, Texas Instruments, and Microchip
* Mentioned real-time location services (RTLS), which are primarily used in medical industries for asset tracking
* Discussed the importance of interoperability between different radio technologies
* Talked about ongoing work on Ultra Wide Band support in Zephyr, specifically with Corva and DECA wave hardware
* Mentioned potential challenges such as Linux Foundation solidifying its strategy and dealing with different silicon vendors.


## Zephyr Retro-&-Prospective: Project Growth, Long Term Support, & Linux Interoperability - Chris Fri

URL: [https://www.youtube.com/watch?v=8r3Eb2f-_GQ](https://www.youtube.com/watch?v=8r3Eb2f-_GQ)

 * Chris Freed, Zephyr project engineer, discussing last 5 years of Zephyr Project growth and improvements
* Highlights:
  + Shipping first unit in IoT microconference (fifth year)
  + Added 64bit arch support, ARMv8a, new TCP stack, Open Protocol Laura GPI API
  + Improved power management, added realtime clock API
  + Added Spark architecture, multicast DNS Discovery
  + Continued development of Zephyr prefix header, CIS build system
  + Added Apache Thrift module, Google Summer of Code projects
  + Community growth with increased contributors and board support
* Challenges faced:
  + Porting boards, fixing bugs
  + Posix API improvements, addressing thread safety, realtime system compliancy

* Zephyr now supports over 600 boards and has taken a modular approach to architecture.
* Linux has taken a different approach by not requiring specific architectures anymore.
* Continuous improvement through bug fixing, feature delivery, and new contributors.
* New features include: SMP improvements, logging enhancements, and virtual memory support.
* Ongoing work includes providing best support for LTS releases and ensuring TLS version synchronization.


## Shared FPU Support in Zephyr for ARM64 and RISC-V - Nicolas Pitre

URL: [https://www.youtube.com/watch?v=VUmd9k0kd98](https://www.youtube.com/watch?v=VUmd9k0kd98)

 * Nicola P. has been working with Linux for 25 years, presenting at LPC for 12 years
* Discussing FPU context switching in Zephyr for ARM64 and RISC-V
* Floating point basics: significant digit, exponent, encoding, single vs double precision
* Multiplication involves determining sign, extracting significand, adjusting exponent
* Addition is more complicated due to carry-over and potential overflow
* Software floating point calculation requires many CPU instructions
* Dedicated hardware FPUs perform operations much faster
* Zephyr is a small realtime operating system with configurable options for FPU support
* Global FPU usage means all threads use FPUs, while FPU sharing allows OS to manage FP resource and arbitrate access during context switching
* Lazy FPU context switching saves overhead by only loading/saving FPU context when necessary
* Exceptions and interrupt handling involve saving/restoring FPU context to prevent corruption of thread content or unexpected FPU usage
* Different approaches to handle FPU usage during exception context, including disabling access or using a separate exception context
* ARM64 uses variable argument passing in registers, which can enable FPU traps if not handled properly
* Ticket spin locks and IPI handling can complicate FPU management
* Power saving considerations may involve keeping FPUs disabled to save power unless actively using them.


## Challenges in Device Tree Sync - kernel, Zephyr, U-boot, System DT - Nishanth Menon

URL: [https://www.youtube.com/watch?v=kr-Yd56so9M](https://www.youtube.com/watch?v=kr-Yd56so9M)

 * The speaker, Nishanth Menon, is a plumber who has worked with Linux and TI since 2004, and is currently working on device tree synchronization between the kernel, U-boot, Zephyr, and System DT.
* Devices in a heterogeneous system, such as BeaglePlay, can present challenges due to their complexity compared to regular microcontrollers.
* Device Tree (DT) is a way to describe hardware using a schema, with the device following the schema and the DT compiler checking it.
* Linux sees devices from an a53 perspective, while M4 or other processors may have different perspectives.
* The device tree represents hardware from different perspectives, such as the main domain (MC domain), actual peripheral domain, and DTSi file corresponding to the bus.
* There are various software ecosystems that use different approaches to handle device trees, such as using separate projects for the kernel and DT or using a tool like DTC to parse the DT blob.
* The speaker mentions the importance of understanding the nuances involved in partitioning, licensing terms (such as GPLv2+ versus Linux-stess GPL v2), and virtualization environments like jailhouse.
* The speaker also discusses the challenges of maintaining a heterogeneous system with multiple perspectives and the need for clear communication between developers.
* The presentation covers the history of device trees, their importance in the Linux ecosystem, and the different approaches to handling them.


## Breaking Barriers: Arduino Core API advancements in Zephyr, Linux and IoT Systems - Dhruva Gole

URL: [https://www.youtube.com/watch?v=bvpeq0RNcWo](https://www.youtube.com/watch?v=bvpeq0RNcWo)

 * Dhruva Gole from Texas Instruments talks about Arduino Core API advancements in Zephyr and Linux for IoT systems.
* Arduino is an open-source electronics platform that uses C language and has a simple setup process. Arduino Core API is a standard defined API that allows anyone to implement their own hardware back end.
* The project started when someone suggested porting Arduino to Zephyr, a scalable, non-vendor specific open source operating system.
* The benefits of combining Arduino and Zephyr include easier development for people comfortable with the Arduino ecosystem, and the ability to migrate new APIs more easily.
* One challenge is adding support for C threads in Arduino code using Zephyr, which would allow for better performance and more efficient use of resources.
* Another challenge is the licensing issue between Arduino (GPL) and Zephyr (Apache 2.0), but there are ways to isolate GPL code within Zephyr.
* Extending library support in Arduino, such as adding native SPI library support, would be beneficial for the Arduino ecosystem.
* Enhanced debugging abilities are also a benefit of using Zephyr with Arduino.
* The goal is to have better integration between Arduino and Zephyr, expand Arduino API libraries, and make it easier to add new variants using lower-level device tree support.
* Using native POSIX in Zephyr would allow for host level debugging and testing of Arduino code on a Linux based system.
* Future plans include expanding Arduino API library and adding support for native simulators, as well as making Arduino code work on POSIX-based systems like Raspberry Pi without the need to learn new scripting languages.


## Livepatch Visibility at Scale - Breno Leitao

URL: [https://www.youtube.com/watch?v=ILTqn1EYIXQ](https://www.youtube.com/watch?v=ILTqn1EYIXQ)

 * Breno Leitao from Meta discussing challenges with live patch monitoring at scale
* Upstream patches require custom patches, but upstream doesn't need them
* Live patch monitoring challenges: slow installation, rolling new kernels, and rollback problems
* KOP (Kernel Overlays for Production) used to improve rollout process
* Roll mechanism involves multiple phases and RPM packages
* Screenshot tool used to control metrics
* Difficulties with sharding, rolling out kernels across a fleet, and dealing with crashes and warnings
* Need to report kernel versions, web server performance, and application crashes to different teams
* Challenges in finding applied patches, investigating crashes, and improving the system
* Suggestions for changes: changing UTS names, creating new dictionaries, and finding patch dependencies
* Discussion about potential issues with changing user space parsing and enabling modules
* Proposed solutions include adding warnings to console, creating active module lists, and using Ftrace for debugging.


## KLP for Clang LTO Kernel - Yonghong Song

URL: [https://www.youtube.com/watch?v=ru-cVMuCh7g](https://www.youtube.com/watch?v=ru-cVMuCh7g)

 * Speaker discusses live patching in Kernel Persistent (KP) LTO kernel
* Current Upstream K patch does not provide good experience for hacking
* Discusses history of LTO use with PG and Clang, issues encountered
* Shows performance improvement from using LTO 519
* Kernel already uses meta-LTO for internal K patches
* Need additional changes for LTO to be fully supported by KP
* Describes workflow differences between compiler perspective in LTO and non-LTO kernel
* Discusses potential issues with VM Linux workflow, 10-hour experiment failure
* Describes need for profile data fitting and optimization for compiler, profile optimization accuracy
* Discusses Upstream discussion on LTO support and potential alternatives, such as using regular kernel instead of special kernel
* Mentioned concerns about binary differences and VM Linux performance
* IBT (Intel Binary Translation) suggested as a solution but may complicate matters with indirect branch merging
* Discusses potential safety issues with patching functions called indirectly and unconditional jumps
* Kpatch build process changes, such as Merion time stamp file
* Mentioned the need for more discussion on LTO support in Upstream
* Concludes that safe binary rewriting and VM Linux performance are the main concerns and suggests further exploration to improve live patching with LTO.


## Kbuild support for klprelocation generation - Lukáš Hruška

URL: [https://www.youtube.com/watch?v=MKwzSw_i7FU](https://www.youtube.com/watch?v=MKwzSw_i7FU)

 * Luka Hruska from SuSE discusses Kbuild support for KP relocation generation
* Need to generate relocations for Standalone, Isolated Pro modules without reference symbols in exported functions
* Current implementation uses ELF life page relocation which requires modification in KO file and modpost script
* Proposed tool called KP convert which started in 2016, allows testing exact relocations and generates special format for relocation entries
* History of KP convert includes various versions with new features and improvements
* Current relocation infrastructure is tested but minimal version of KP convert could provide more testing infrastructure
* Concerns about maintaining Kpage since minimal version might use it, and potential performance impact of IP optimization
* Idea of disabling some optimizations for live patching and using function attributes to enable or disable them
* Discussion about detecting safe patches automatically and the potential risks of false positives
* Live patching requires ability to handle IPA optimization programs first, and GCC has a live patching option but it disables some optimizations
* Unreachable warning issue when using live patching and potential workarounds like fixing the code or using a generic solution
* Question about cable integration and whether it needs to be preserved in KP convert
* Discussion about generating relocation names, modifying section prefixes, and renaming location sections
* Concerns about artificially generating relocations and potential real-world cases where compiler might generate crashes in the kernel.


## Simplify Livepatch Callbacks Shadow Variables and States handling - Petr Mladek

URL: [https://www.youtube.com/watch?v=5IncwQ2XFCw](https://www.youtube.com/watch?v=5IncwQ2XFCw)

Error


## Moving livepatching module building to kselftests - Marcos de Souza

URL: [https://www.youtube.com/watch?v=ku0Log23OL4](https://www.youtube.com/watch?v=ku0Log23OL4)

 * Marcos Souza from Red Hat discusses moving live patch testing to K self tests
* Current problem: user space test for live patching module is not included in case test
* Goal of case test: to check exact code path and verify that the kernel accepts user space tests
* Need to run test on target system with specific kernel source and configure
* Proposed solution: moving the test code inside the case test structure
* Current obstacles: need to build and install a new kernel with life patch config, test module might not load on different systems due to kernel version differences, lack of kernel module inclusion in case test
* Future proposal: enabling case test for testing life patches, but it would require changes to the kernel build system and dependencies
* QA team at Red Hat is using GitHub for testing new versions, they might move testing infrastructure to a more flexible model
* Discussion on moving K source machine, building module without cloned kernel source, and enabling self test in the kernel repository
* Marcos shares his experience with writing K unit tests and creating test infrastructure for a reliable stack trace
* Suggestions for creating a standalone test tool like ltp test to test kernel version latest self test, making it universal and easier to maintain.
* Discussion on enabling a flag to copy source or keep the current approach, moving source person-created and choosing binary search code built.
* Future work: making self tests runnable on older kernels, keeping in mind that some modules might have different behavior depending on the kernel version and some APIs might change.
* Recommendation to test modules together with the kernel for better coverage and fewer security implications when moving modules around.


## Arm64 live patching - Mark Rutland

URL: [https://www.youtube.com/watch?v=PGaaWFCTjz0](https://www.youtube.com/watch?v=PGaaWFCTjz0)

 * Mark Rutland discussing live patching on Arm64 architecture
* Preparatory work has been done for reliable stack tracing, but unwinding across exception boundaries is still a challenge
* Unwinding process involves looking at the link register and frame pointer to find the parent function record
* Consistency model for patching is important to ensure that the function being patched is still active
* Arm64 architecture uses a different calling convention, which makes unwinding more difficult
* Proposed solutions include using metadata or annotation assembly to provide information on return addresses and frame pointers
* Live patching consistency model needs to consider whether the function being patched has returned or not
* Microsoft is interested in addressing code generation issues related to live patching and Arm64 architecture
* Rust compiler generates CFI annotations, but support for S frames and unwinding exceptions is needed
* Proposed solutions include using LLVM assembler, generating traps for unreachable functions, or creating kernel-specific annotations.


## Klint: Compile-time Detection of Atomic Context Violations for Kernel Rust Code - Dr Gary Guo

URL: [https://www.youtube.com/watch?v=xCWfoxAGWQk](https://www.youtube.com/watch?v=xCWfoxAGWQk)

 * Introduction to a talk by Gary Guo about a new tool called Pink for detecting atomic context violations in Rust kernel code at compile time
* Background on Russ safety and undefined behavior in Rust
* Introducing Pink, a tool designed to detect multiple kinds of code misuse with a focus on atomic context violation detection
* Atomic context violations include things like sleeping inside an atomic context or trying to acquire a lock while holding another one
* RCU (Read-Copy Update) is a simple use case where a compiler generates compile-time barriers (fence instructions) to ensure that context switches don't happen during critical sections
* The goal is to prevent assumptions about the absence of context switches inside RCU critical sections from being broken, which can lead to deadlocks or memory safety issues
* Three possible solutions for addressing sleeping atomic misuse: using tokens, dynamic checks, and ignoring the problem
* Pink's design goals include simplicity, ease of use, providing useful diagnostics, and giving full control while minimizing friction
* Case study of running Pink on the Rust LTS kernel and detecting issues related to asynchronous context and wake functions.


## pin-init: Solving Address Stability in Rust - Benno Lossin e3

URL: [https://www.youtube.com/watch?v=s5Rd3QZND1E](https://www.youtube.com/watch?v=s5Rd3QZND1E)

 * Miguel will talk about address stability in Rust, focusing on initialization and field projection
* Initialization in Rust involves ensuring variables are initialized to avoid memory issues
* Uninitialized memory is a common issue that can lead to errors
* Address stability is important for kernel data structures like linked lists
* In Rust, we use move semantics which prevent moving pointers once they're pinned
* Pinning pointers ensures stable addresses and prevents memory issues
* Field projection is a technique used in Rust to safely access fields of structs without moving them
* With field projection, you can turn a pointer to a whole struct into a pointer to a single field
* However, this can lead to issues with uninitialized memory if not handled carefully
* In the context of pinning, some functions and types require pinned mutable references for safety reasons
* Pinning ensures that pointers don't get updated, preventing memory issues caused by moving or updating pointers.


## Coccinelle for Rust - Julia Lawall

URL: [https://www.youtube.com/watch?v=Gh9lOyddqbY](https://www.youtube.com/watch?v=Gh9lOyddqbY)

 * Julia Lawall presents Coccinelle for Rust, a tool for large-scale code transformations
* Goal: perform repetitive transformations on a large scale, such as in the Linux kernel (16 million lines of code)
* Came up with idea to lift abstraction level, focusing on semantic patches instead of superficial changes
* Semantic patch context includes line number and information part of the code that is being changed
* Semantic patch rules specify type bound type calls and sub-identity calls
* Rules can automate existing patches or extend them to handle more cases
* Coxinelle for Rust uses Rust analyzer parser and rustfmt for pretty printing
* Previously tried to develop Co code in C, but ran into issues with rustfmt and concurrent processing
* Semantic patch language is important as it allows matching code exactly and accommodating attributes or wiggle room context
* Challenges include handling variable borrows, pub modifiers, and async functions
* Also discusses potential features for future development, such as disjunction and function macro call transformations.


## Using Rust in the binder driver - Alice Ryhl

URL: [https://www.youtube.com/watch?v=Kt3hpvMZv8o](https://www.youtube.com/watch?v=Kt3hpvMZv8o)

 * Carlos Alihl talks about using Rust in the binder driver of Android
* Binder is a IPC (Inter-Process Communication) system used for service communication in Android, similar to RPC
* Unique features of binder include direct memory exchange between client and server, priority inheritance, and object management
* Rewriting binder code can be complex due to its feature-packed design and the risk of introducing bugs or vulnerabilities
* Rust's ownership semantics can prevent certain types of mistakes in the driver implementation
* In Rust, function signatures encode type information and the compiler enforces annotations, making the code self-documenting
* Rust uses different pointer types and nullability handling than C
* Rust does not prevent out-of-bound array access, but it can still help prevent some types of vulnerabilities
* The binder implementation in Rust includes a module called "binder FS" which keeps the C implementation unsafe code
* The abstraction layer in Rust uses work Cube as an example and wraps around it with safe Rust code
* Rust's performance is generally comparable to C, but it may have some optimization opportunities
* Rust has a larger code size than C, but it offers better maintainability and ease of use for developers
* There are ongoing efforts to optimize Rust performance and reduce its code size.


## Block Layer Rust API - Mr Andreas Hindborg

URL: [https://www.youtube.com/watch?v=lI9DLvxUA4Q](https://www.youtube.com/watch?v=lI9DLvxUA4Q)

 * Andreas Hindborg discussing Block Layer Rust API and abstraction project
* Goal is to allow implementation of block device drivers in Rust
* Discussion on benefits such as increased security, providing a reference implementation for the community, and reducing risk for early adopters
* NVMe driver abstraction being discussed, with a focus on PCI transport and timer support
* Recommendation to pull the git repository of the abstraction project and rebase it against the latest Linux release
* Comparison of performance between different block drivers, including C mvme driver and Rust driver
* Discussion on challenges such as rebasing NVMe driver changes and handling real hardware with abstractions
* Mention of a timer API demonstration and its implementation using Alice's work as a basis
* Question and answer session covering topics such as code size, helper functions, and LTO (Link Time Optimization) enablement.


## Rust in V4L2: a status report - Daniel Almeida

URL: [https://www.youtube.com/watch?v=ap1_EOJgydo](https://www.youtube.com/watch?v=ap1_EOJgydo)

 * Daniel Almeida discussing Rust support in V4L2 (Video for Linux)
* Initial support submitted early this year, includes abstractions like buffer allocation and device enumeration
* Experimenting with using Rust for video codecs due to potential vulnerabilities in C code
* Medium subsystem is overwhelmed with patches and lacks review bandwidth
* Proposed creating a virtual driver for Rust in the V4L2 subsystem
* Virtual driver would communicate with real hardware drivers through abstractions
* Concerns about breaking existing C code and the complexity of video codecs
* Suggested separating experimental Rust code into its own configuration option
* Discussed potential benefits and challenges of using Rust in V4L2
* Audience question: How to detect automatic breaks in Rust code?
* Suggested adding markers in the code or testing for specific cases
* Maintainer involvement is crucial to addressing issues and ensuring compatibility
* Discussed potential risks and benefits of using Rust in V4L2 subsystem, with a focus on education and experimentation.


## Converting a DRM driver to Rust - Mrs Maíra Canal

URL: [https://www.youtube.com/watch?v=fPvDgxnNJ6I](https://www.youtube.com/watch?v=fPvDgxnNJ6I)

 * Maíra Canal is a G developer who converted a Vulkan graphics driver (DRM) to Rust
* The presentation covers her experience and challenges during the conversion process
* DRM stands for Direct Rendering Manager, it's a subsystem handling graphics memory efficiently in a hardware-agnostic way
* The original driver was written in C and provided Jam service using IOS synchronization objects (fences)
* The challenge was to write a safe abstraction without relying on hardware-specific details
* Rewriting the driver in Rust would allow better safety and easier memory management
* Rust's timer abstraction was found to be natural for writing the DRM binding
* Legacy platform initialization, DMA reservation object binding, and driver access code were also written
* The presentation covers the challenges encountered while managing unsafe code in Rust, the importance of safety reviews, and documenting the process
* The discussion touches on how Rust's community is communicative and helpful, with a focus on improving documentation and writing safe abstractions.


## Zero Copy Receive using io_uring - David Wei

URL: [https://www.youtube.com/watch?v=LCuTSNDe1nQ](https://www.youtube.com/watch?v=LCuTSNDe1nQ)

 * David Wei, software engineer at Meta, discussed adding zero copy RX (receive) in Linux kernel using IO uring user API
* Current networking stack in Linux has overhead and multiple trips between PCIe, system DRAM, and user space for receiving packets
* Zero copy solutions involve bypassing the kernel entirely but require handling networking stack in user space
* Proposed solution is a hybrid approach: splitting the networking stack into two parts - control plane processed by the kernel, data path goes straight to user space
* Using I uring's shared ring buffer and registration of buffer pages for efficient data transfer
* Benefits include reduced CPU overhead, less memory bandwidth usage, and the networking stack still gets visibility
* Early results show a significant drop in system bandwidth with Broadcom hardware using zero copy RX
* Future work includes testing, proper support for multiple sockets, and GPU device memory.


## Enhancing Homa Linux for Efficient RPC Transportation - Dr Xiaochun Lu

URL: [https://www.youtube.com/watch?v=AcWsHW_qf-A](https://www.youtube.com/watch?v=AcWsHW_qf-A)

 * Dr. Xiaochun Lu from Tan Tang Dan System Technologies discusses enhancing Homa Linux for efficient RPC (Remote Procedure Call) transportation
* Agenda: review Homa, its limitations, enhancement of Homa's congestion control, and future improvements
* TCP was designed for wide area network connections but is inefficient for RPC as it prioritizes orderly delivery over low latency
* Homa, a data center protocol, addresses these issues by using connectionless, state message-based protocol that prioritizes short messages
* Overview of Homa's sender and receiver side mechanisms: unscheduled and scheduled packets, explicit grants, and packet scheduling
* Limitations of Homa include inefficient pipelining for large RPC messages and weak congestion control
* Proposed enhancements to Homa include improving congestion control through dynamic per-peer adjustable window algorithm and realtime RTT measurement.
* Current issues: fixed RTT configuration, insufficient buffer management, and lack of support for zero copy sender/receiver side optimization.
* Results show that optimized Homa can improve throughput and reduce latency compared to vanilla Homa in both small and large workloads.
* Future improvements may include distinguishing fabric delay from network delay, optimizing dynamic window algorithm, and supporting zero copy sender/receiver side.


## An introduction to the DPLL subsystem - Vadim Fedorenko

URL: [https://www.youtube.com/watch?v=PJiGyHR9jk8](https://www.youtube.com/watch?v=PJiGyHR9jk8)

 * Vadim is introducing the DPL (Digital Phase Locked Loop) subsystem in Linux kernel 67
* DPL device is a digital face synchronized input device with a feedback path, output signal, and digital comparator loop filter
* It extends the PTP (Precision Time Protocol) device and introduces configuration priority input signals
* The main problem is that it doesn't have enough I/O pins, so an external chip is used for multiplexing
* DPL device has a netlink interface for transport and control
* API documentation and driver implementations are available
* DPL device supports four operations: get current mode, set mode, get pin status, and change pin direction
* The driver implementation includes a simple PPS (Precision Clock Synchronization) mode configuration for external pins connected to the DPL device
* NVIDIA's mlx5 driver has been implemented with complex configurations for multiple DPL devices on one physical board
* Temperature, phase offset, and temperature compensation are monitoring metrics for DPL devices
* The DPL device does not require any hardware integration but uses the testing infrastructure in the Linux kernel.


## Unblocking the softirq lock for PREEMPT_RT - Sebastian Siewior

URL: [https://www.youtube.com/watch?v=rrb9KdHrFSw](https://www.youtube.com/watch?v=rrb9KdHrFSw)

 * Sebastian Siewior talks about softirq problem in RT (Real-Time) kernel and optimization from a correctness and workload perspective
* Preemptable RT kernel vs non-RT: in RT, networking instances cannot raise hard irq or softirq, and softirqs are run in vanilla piggyback mode without local BM disable and act CPU lock synchronization
* Downside: long running threads could block important higher priority tasks
* In RT, setting reskpi boost priority instead of promoting thread is used to get things done quicker and release the lock earlier
* SKB allocating in networking uses a guard notation for locks and unlocks
* Bottom half reason requires hard explanation as it involves driver control in userland and kernel, and interrupt injection
* The goal is to preserve softirq race execute semantics while ensuring proper protection of resources
* PCP resource protection methods are being worked on through proof of concept implementations to make locks smaller and more efficient
* Recursion in the networking stack and BPF locking also need consideration
* XPvpf runs without redirection, but there may be performance issues if it switches back to the previous context within the code
* The Flash needs protection against tackling driver passions, which could ideally be solved by a simple guard at the beginning of the call and BPF return function unlock
* Changes to the kernel or drivers might involve making sacrifices in terms of performance for correctness purposes
* Possible way forward: identifying the necessary spots for serialization in the network stack and implementing protection accordingly
* Ports, RT issues, and locking mechanisms need thorough investigation and potential rework.


## Offloading QUIC Encryption to Enabled NICs - Andy Gospodarek

URL: [https://www.youtube.com/watch?v=qDHWHkqaW6U](https://www.youtube.com/watch?v=qDHWHkqaW6U)

 * Amy Gospodarek from Broadcom presents on offloading QUIC encryption to enabled NICs
* QUIC is a transport protocol that runs over UDP and is used in HTTP/3 for fast transport
* QUIC uses TLS 1.3 handshake and supports connection IDs for movement between sessions
* Hardware offload can be used for QUIC encryption to reduce CPU usage
* Offloading can be selective, with some tasks better suited for software and others for hardware
* Netlink interface can be used in the kernel to manage offloaded connections and crypto information
* User space can add offloaded connection information to the netlink database
* Kernel module keeps track of flow context, including connection IDs and direction
* Receive offload can be controlled via netlink messages instead of individual TCP sockets
* QUIC flow context could be added to TLS Dev ndo like ktls socket information
* User space sends a request for offloading via netlink and receives an xid back
* Encrypted data is handled by the network driver, decryption is done in the socket layer
* Application chooses whether to use software or hardware encryption
* Quick device offload has been shown to work well in practice, especially for one RTT traffic
* Some challenges exist in implementing and adopting quick, such as netlink support in libraries and fine-grain control over flow deletion.


## Extending AF_XDP with hardware metadata - Stanislav Fomichev

URL: [https://www.youtube.com/watch?v=HYqxxVb48os](https://www.youtube.com/watch?v=HYqxxVb48os)

 * Stanislav Fomichev from Google's host networking team discusses extending Access Flow Control (AF-XDP) with hardware metadata
* AF-XDP: new protocol family, socket-based like modern raw sockets, designed for efficient handling of packet processing use cases, plays well with kernel bypass solutions
* XDP: used for flow steering mechanism, usually involves installing an XDP program to forward packets through an AF-XDP socket instead of the regular kernel path
* AF-XDP socket pair: involves creating a socket and user space memory chunk for payload, partitioned into thick chunks with specific sizes
* Kernel registration: involves registering the transmit side's pair ring and receive side's fill ring with the kernel
* XDP program: creates BPF redirect map to forward packets from an AF-XDP socket and performs flow filtering (if needed)
* Metadata offloads: modern NICs have the capability to receive metadata alongside packets, which can offload tasks like checksum verification, flow hash computation, and time stamping from the CPU
* Limitations of AF-XDP: previously limited to sending packets in large chunks, but recent work supports scatter gather to send multiple smaller chunks at once
* Transmit side: also benefits from metadata offloads for requesting and receiving completion timestamps, which can save CPU cycles by asking the NIC to calculate checksums and put them at specific offsets
* Receive side: currently supports timestamp and receive hash offloads; future work includes transmit time stamp and other transmit-side offloads (e.g., transmit crypto offloads, segmentation load)
* Driver support required for some offloads (e.g., TCH loading and cryptographic offloads), but many are already supported by popular vendors like Melanox and Intel.


## connect() - why you so slow?! - Frederick Lawler

URL: [https://www.youtube.com/watch?v=UVidhdQgR9A](https://www.youtube.com/watch?v=UVidhdQgR9A)

 * Frederick Lawler, Cloudflare system engineer, discusses the issue of slow connect() function in Cloudflare's traffic control system
* The problem arises when many connections are made to a single origin, causing congestion and increased latency
* The connect() algorithm follows a simplistic workflow: asset request arrives at Cloudflare Network, eventually reaches the Colo location machine, and is sent back to the user's eyeball
* Cloudflare servers typically set a port range (56000) for establishing many connections using TCP, but this can lead to issues with binding IP addresses and ports
* The solution involves implementing late binding of ports and load balancing between multiple IP addresses
* The presentation covers the issue in detail, including code examples and performance data from stress tests
* The main takeaway is that looping and port contention are the main causes of the problem, and patches have been submitted to address these issues.


## Container Networking: The Play of BPF and Network NS with different...- Martin Lau, Takshak Chahande

URL: [https://www.youtube.com/watch?v=Xow6I-E6WZE](https://www.youtube.com/watch?v=Xow6I-E6WZE)

 * Container networking evolution: isolation and configuration requirements are key elements
* Different types of container workloads require varying network isolations and resource allocation
* Single host with multiple containers faces challenges in port management and traffic policies
* eBPF (Extended Berkeley Packet Filter) can help in isolating containers, managing ports, and identifying container sending traffic
* Cgroup BPF programs can help attach identities to containers, bind IP addresses, and manage connectivity
* Challenges include multi-tenant environments, wildcard binding limitations, and performance management
* eBPF has evolved to address various network issues like TLS interception, UDP traffic redirections, and network emulation.


## Evolution of Direct Server Return (DSR) implementation for containerized applications - Lalit Gupta

URL: [https://www.youtube.com/watch?v=jzwH5-WkWtg](https://www.youtube.com/watch?v=jzwH5-WkWtg)

 * Lalit Gupta, production engineer at Meta, discussing evolution of Direct Server Return (DSR) implementation for containerized applications and its benefits
* Traditional load balancer distributes traffic among backends based on transport header for high availability and scalability
* DSR allows server to respond directly to client, bypassing load balancer, resulting in improved performance
* Initial challenge was CPU-heavy collocation of connection tables causing poor performance
* BPF XDP technology emerged as a solution to handle high traffic with minimal CPU usage
* XDP changer program released to dynamically attach and execute XDP programs in order on network devices
* XDP decapsulation implementation led to minor performance gain but also discovered security issues requiring container privileges
* TC Decap solution implemented instead, providing better decapsulation statistic and isolation without the need for elevated privileges
* Hardware challenges included different vendor behavior and performance gaps
* Difference between TC BPF program and xtp based decapitation approach lies in SK buff data structure sizes
* XDP changer attach time and program update considerations were addressed to avoid downtime
* Question about L port usage and its impact on UDP mentioned but not elaborated.


## SYN Proxy at Scale with BPF - Kuniyuki Iwashima

URL: [https://www.youtube.com/watch?v=n0qQ9PuxXeU](https://www.youtube.com/watch?v=n0qQ9PuxXeU)

 * Kuniyuki Iwashima discussing SYN proxy implementation using MODULO-S subtitle: "SYN Proxy at Scale with BPF - Kuniyuki Iwashima"
* Explanation of SYN problem and stateful server keeping state for each connection
* Discussion of DS attacks like SYN flood and allocation of resources for connection requests
* Description of internal sequence number, time stamp cookie, and encryption used in SYN proxy
* Overview of SYN key generation and format
* Comparison of Linux Canoe and Windows scaling in relation to SYN proxy
* Explanation of stateless network's challenges with SYN proxy and the use of a single key
* Discussion of SYN proxy handling three-way handshake, reducing false requests, and managing connections
* Overview of BPF (Berkeley Packet Filter) implementation for SYN proxy
* Suggestion to add functionality to access TCP header data in BPF program
* Explanation of how K fun works in the context of a BPF program
* Summary of presentation on SYN key, scalability, and performance.


## bpfilter: a BPF-based packet filtering framework - Quentin Deslandes

URL: [https://www.youtube.com/watch?v=1wJPKnbRjRE](https://www.youtube.com/watch?v=1wJPKnbRjRE)

 * Quentin Deslandes from Linux user space team has been working on BPF-based packet filtering framework named BP filter for almost a year.
* Originally, BPF filter was a user model per canal module developed in user space that could read content and create BPF programs using IP table Legacy.
* However, the earlier version of patch series for generating packet BPF programs was never merged in mainline project since 2021.
* The structure of BP filter consists of a library with a demon running in user space. The client communicates with the demon using netlink messages and sends IP table data to be translated into BPF programs.
* BP filter uses Unix domain sockets to transmit data across, allowing for lightweight communication between components.
* IP table Legacy is used for proof of concept, but its limitations include not being able to fetch a single rule or request one specific thing without fetching the whole rule set.
* To address this issue, BP filter can change rules and generate new BPF programs if necessary, with mandatory technical issues like time being the primary concern.
* BP filter supports filtering based on IP table entries, NF tables, protocols, and ports using Maps. The difference between IP table and NF table lies in how they communicate with the kernel, with NF table using netlink messages to send rules directly to the kernel.
* Recently, work has been done to support NF table using a prototype modified version of libp filter instead of netlink messages for better performance.
* BP filter can also offload NF table rule creation and use XDP programs attached to net filter hooks.
* The cut generation part of BP filter happens by creating rules, filter packets, and generating the corresponding BPF code. It uses a structure that represents client hooks and tries to filter packet input/output hooks based on IP table hooks.
* BP filter supports XDP, TC, net filter hooks, and IP table hooks, with the choice between input and output hooks determining whether it drops or passes packets.
* The main difference between IP table and NF table is that IP table provides a more traditional way of creating rules and filtering packets, while NF table offers offload capabilities using XDP programs.
* BP filter uses dynamic pointers for TC, xtp net filter hooks, and generated programs, and maps rules to the appropriate buckets in user space. It also supports one program per interface and creates rules based on drop packets defined per interface per program.


## Blinking Lights getting it wrong again again and again - Andrew Lunn

URL: [https://www.youtube.com/watch?v=FTlcWWLeJXg](https://www.youtube.com/watch?v=FTlcWWLeJXg)

 * The speaker is discussing issues with controlling blinking lights in networking systems
* Two different ways to control LEDs in RJ45 connectors, neither of which are standardized
* Older methods involved writing random values to registers
* Device tree was used in the past but is no longer recommended due to lack of consistency
* Consistency is important for user experience and vendors should not implement differently
* The speaker expresses frustration with people trying to solve problems in silos and not communicating effectively
* The Linux kernel already has a Blink LEDs subsystem
* Different types of LEDs, such as num lock keys or display backlights, are controlled differently
* Kernel space controls LEDs while user space can adjust brightness and other settings
* Triggers for blinking lights include network activity, disc activity, and power issues
* The speaker suggests extending the cclass LED interface for better offloading and control
* Different vendors have different approaches to showing RX/TX time with LEDs, making it difficult to standardize
* The speaker advises against trying to offload blinking network activity LEDs to hardware as it can be expensive and unreliable.


## Syzbot: 7 years of continuous kernel fuzzing - Aleksandr Nogikh

URL: [https://www.youtube.com/watch?v=sDMNEBoTtrI](https://www.youtube.com/watch?v=sDMNEBoTtrI)

 * Alexander Nogikh from Google talking about Syzbot, a continuous kernel fuzzer used by Google since 2017
* Syzbot checks latest Colar Vision builds for vulnerabilities and reports findings to developers
* Syzbot has detected over 17,000 findings in Linux kernels, with approximately 1,000 new findings reported per year
* Syzbot uses BCH testing functionality to test kernel patches
* Syzbot's finding resolution time has been analyzed using a mutual information key square approach
* Important predictors for determining whether an issue is addressed include the average daily number of hours the report exists, the complexity of the reproducer, and the subsystem affected
* Surprising insights from the data include the strong correlation between the number of times a finding has been hit during fuzzing and its likelihood of being resolved, and the importance of the cost section in predicting issue resolution
* Notable changes last year include improvements in cost section quality, automatic obsolete finding detection, and the implementation of a new web dashboard for discussion and filtering of findings
* Discussion on mailing lists has included topics such as the perceived quality of Cbot reports, low severity/priority reporting, and false positives
* Syzbot's analysis functionality includes the ability to automatically classify LTS kernels and find related commits, and attempts to minimize duplicate work by batching series of reports
* Challenges include the reliability of producers, the possibility of a single producer triggering multiple unrelated crashes, and the difficulty of dealing with commits that introduce bugs
* New features include a web dashboard for aggregate discussion and filtering, as well as commands for setting priority and excluding findings from monthly reporting.


## Linux Virtualization Based Security (LVBS) - Thara Gopinath

URL: [https://www.youtube.com/watch?v=WSsG-4FJxmg](https://www.youtube.com/watch?v=WSsG-4FJxmg)

 * Linux Virtualization Based Security (LVBS) project has been in development for a year
* Goal is to enhance security of guest OS by leveraging virtualization and the hypervisor as a security boundary
* Architecture is flexible and can support different types of hypervisors (type one or two) and different security monitors
* Primary features include: protecting integrity of critical guest structures, memory permission, CPU register state, and configuration variables
* Support for trusted execution environments and credential management
* Implementation using Hyper-V was discussed, focusing on virtual secure mode and its ability to provide isolation and execute code with different privilege levels
* Discussion also touched upon the threat model and the need to protect critical kernel resources from user space attackers
* Hardware requirements include support for second level address translation and a CPU that distinguishes between execute modes (kernel, user)
* Goal is to create a hypervisor-agnostic solution with protection mechanisms at a common layer
* Comparison was made to confidential computing, emphasizing that LVBS complements it by providing kernel space protection in addition to user space protection
* Discussion also touched upon the importance of interfaces and communication between the hypervisor, secure kernel, and guest OS.


## Is Linux Suspend ready for the next decade - Len Brown

URL: [https://www.youtube.com/watch?v=Pv5KvN0on0M](https://www.youtube.com/watch?v=Pv5KvN0on0M)

 * Lynn Brown introduces the topic of Linux suspend and resumption, specifically focusing on issues with laptops not suspending or resuming properly.
* Todd Brandt, maintainer of the sleep graph tool, is thanked for his dedication to improving suspend and resume performance over the past decade.
* The discussion covers various power states in Linux, including suspend idle, hibernate, and freeze, with a focus on suspend idle as the fastest power saving state.
* Todd demonstrates the use of tools like sleep graph and the Intel PM graph to diagnose and analyze suspend and resume issues.
* Some common causes of slow or failed suspend and resume include long-running processes, firmware issues, and wake events from devices.
* Tips for improving suspend and resume performance include setting shorter RTC wake times, using X2 (backlight) mode, and testing with multiple devices to identify the slowest one.
* The importance of proper testing and endurance testing is emphasized to ensure that new device drivers support suspend and resume correctly.
* Other topics briefly touched upon include WiFi connectivity issues during suspend and resume, the use of virtual machines instead of hibernation, and the role of the Linux kernel in managing power states.


## Encryption for filesystems with advanced features new fscrypt functionality - Sweet Tea Dorminy

URL: [https://www.youtube.com/watch?v=mmMnIxAwJq0](https://www.youtube.com/watch?v=mmMnIxAwJq0)

 * Sweet Tea Dorminy from UH Meta worked on integrating encryption in file systems, specifically with FS Crypt, which is an extent-based encryption solution for FS script.
* FS Crypt encrypts data based on the extent and offset within the extent data instead of per file basis.
* It stores encryption information per extent and uses a separate key for each subvolume to ensure different keys cannot be mixed.
* One limitation is that it does not allow deleting files without losing the key, which is a tradeoff compared to whole file system encryption solutions like Lux.
* FS Crypt integrates encryption in the file system layer using standard hooks and functions in the FS script library, making it convenient for developers.
* It can be used with different backends like block crypto or device mapper Target.
* The design document was initially shared in October 2021 by Omar Sandal but faced challenges due to mismatched expectations between the code and design.
* FS Crypt currently supports extent-based encryption using block crypto, and a new design is being developed that adds support for nested subvolumes and changing keys within a single tree.
* The goal is to make file system encryption more extensible and flexible while maintaining performance and security.
* Other alternatives include using Butfs or FS script for encryption per subvolume basis.
* A hot topic in the community is the use of authenticated encryption instead of checksums to ensure data integrity.
* The current design does not support changing keys within a single tree, making it difficult to delete files without losing the key and reformatting the entire file system.
* However, there are ongoing discussions about adding the ability to change keys for subvolumes that have already been encrypted.
* There is also a proposal to use Butfs encryption for Fedora, which involves a multistep encryption process with individual contributors reencrypting data using new keys.
* Meta might consider installing packages with subvolume encryption in the future.
* The challenge is to change the keys for existing encrypted data while ensuring that users can still read everything in the subvolumes.
* It remains unclear whether this would involve per-subvolume keys or updating inodes recursively to reencrypt data.
* Another question is whether FS script needs to support online encryption or if it should only be used for offline encryption.
* Authenticated encryption is also being considered as an option, which can detect corruption cryptographically and return the authentication tag instead of checking checksums in-place.
* The long-term goal is to make FS Crypt more extensible and future-proof by adding features like authenticated encryption and nested subvolume encryption.


## Trust, confidentiality, and hardening: the virtio lessons - Michael S Tsirkin

URL: [https://www.youtube.com/watch?v=Gu0B9J4ZNNI](https://www.youtube.com/watch?v=Gu0B9J4ZNNI)

 * Michael Hyoty presenting on trust, confidentiality, and hardening with focus on the Linux Verdeo driver
* Verdeo is an open standard I/O device supported across various hypervisors and guest operating systems
* Traditional virtualization use case: Verdeo driver in hypervisor sends IO buffers to device, which can lead to accessing guest memory and potential security risks
* Hardware Verdeo device (like a PCI device) is separate from the hypervisor, providing isolation and hardening
* Confidential Computing: reducing trusted computing base and protecting workloads from untrusted infrastructure
* Linux Verdeo driver introduced to allow user space Vero device communication without kernel involvement for improved security
* Input validation and memory isolation are important aspects of securing Verdeo devices
* Hardware Verdeo devices can provide additional isolation and hardening by confining the device and not allowing it to access memory directly
* Encryption is used to protect guest RAM, network traffic, and storage data in confidential computing scenarios
* Confidential Computing requires trust in specific hardware components and device drivers, with Linux Verdeo driver being audited for vulnerabilities
* Interrupt handling and speculative execution attacks are potential open issues with Verdeo devices
* User policy configuration is necessary to ensure secure use of Verdeo devices.


## Using hardware hints for optimal page placement - Mr Bharata Bhasker Rao

URL: [https://www.youtube.com/watch?v=btv7LUoPS1Q](https://www.youtube.com/watch?v=btv7LUoPS1Q)

 * Bharata Rao discussed using Hardware provided memory access hints for optimal page placement in the Linux kernel.
* The goal is to efficiently use available system capacity and keep pages that are frequently accessed closer to the node they're being used on, while discarding infrequently used ones.
* The hardware provides memory access information in various ways, such as instruction-based sampling or event-based sampling.
* AMD CPUs use instruction-based sampling through the IBS feature, which provides metrics related to instruction fetch and execution.
* Hardware provided memory access hints can be used for NUMA balancing by understanding the target address, memory load/store information, and cache misses.
* The data source of the memory access information includes cache, DRAM, and external memory.
* AMD processors use an independent PMU subsystem to collect hardware counters with a limited number of PMCS.
* IBS is useful for memory access profiling in a precise way, but filtering would be required due to the large amount of data generated.
* Hardware provides a programmable bit to report samples for load/store missed L3 cache, which can be useful for memory access profiling.
* The traditional NUMA balancing subsystem employs software-based mechanisms like scanning process address space periodically and marking pages with NUMA hints based on their access pattern.
* IBS-driven NUMA balancing uses hardware-provided hints instead of software-based mechanisms, which can be more efficient and accurate.
* The experiment using a 2p 3 node N4 system with two regular Puma nodes and one CXL node showed that IBS-driven NUMA balancing had slightly different behavior but similar Benchmark scores compared to traditional NUMA balancing.
* IBS reported many more samples, which led to more efficient migration of pages.
* The overhead of IBS was minimally noticeable and could be mitigated by playing the sampling rate.
* In virtualization use cases, there is a possibility of conflict between host and guest IBS, but it can be optimized by changing the sampling rate and enabling THP instead of 4K pages.
* IBM Power processors provide sort memory access information using hot/cold affinity and instruction-based sampling.
* The NUMA balancing scan rate is minimum, maximum, or based on convergence workload, and it cannot be set to a certain value.
* The overhead time spent on page table scanning versus CPU usage can be tuned for better performance.
* LSF MM session in May could discuss the idea of using cache monitoring instead of page table migrating for task placement.
* It would be interesting to know the overhead time spent on page table scanning and compare it with the CPU usage.
* Grain tuning can help optimize the overhead by reducing the number of context switches and improving the sampling rate.


## Linux perf tool metrics - Ian Rogers

URL: [https://www.youtube.com/watch?v=DpKQLEMGjwU](https://www.youtube.com/watch?v=DpKQLEMGjwU)

 * Speaker is giving a presentation on Linux perf tool metrics and the challenges of creating clear, consistent metrics
* Metrics can be unclear due to different units (bytes versus cycles), clock sources, and counters used for different events
* Perf tool allows multiple aggregation methods and PMUs, making it important to create human-readable metric groups
* Metric group could consist of related data sharing individual metrics within the group
* Speaker mentions TMA core bound and backend bound as examples of complicated metrics
* Intel's Valkyrie project is working on standardizing event metrics and providing common ones for different architectures
* Ahmed Yazing proposed a methodology for top-down microarchitecture analysis in 2014, which can be used without deep microarchitecture knowledge
* TMA (Time Multi-threaded Assists) is a metric that can cause controversy due to EBS (Event Based Sampling) mode and stalled slot issues
* Intel's perf tool historically gave branch misrate count for Atom Processor, but it doesn't have enough counters to calculate accurately
* Speaker proposes a new event grouping method to improve accuracy by collecting events that belong to the same metric together.
* Three steps of proposed method: first, know what events and restrictions are needed; second, collect events based on PMUs; third, generate groupings and strings.
* Speaker also discusses Intel's Timed PS enhancement and its potential impact on TMA metric accuracy.


## Ship your Critical Section, Not Your Data: Enabling Transparent Delegation with... - Vishal Gupta

URL: [https://www.youtube.com/watch?v=xn8_082ZpLw](https://www.youtube.com/watch?v=xn8_082ZpLw)

 * Vishal Gupta from EPFL discussed shipping critical sections instead of sharing data for better lock scalability
* Locality and fine-grain locking have been important in Linux kernel synchronization, but data movement can lead to performance issues
* Sharing data between threads trying to acquire a lock can result in increased latency and contention
* Data movement is often necessary when accessing shared resources within critical sections
* Q spin locks, a popular lock type used in Linux, can cause additional latency when multiple threads are trying to acquire the lock
* Transparent delegation is an alternative approach to reduce lock contention and improve performance by using standard lock APIs and minimizing shared data movement
* Reusing register context for thread context switching and capturing thread context within critical sections are key components of transparent delegation
* The design involves a server-client model where the server holds the lock and clients request access, with the server safely transferring context to the waiting client
* Linux kernel has implemented counter-based and timer-based threshold strategies for lock contention management, but there are challenges in implementing transparent delegation transparently without modifying critical sections
* Transparent delegation can lead to improved performance by reducing the amount of time spent in critical sections and improving cache locality.


## Kernel handling of CPU and memory hot un/plug events for crash - Eric DeVolder

URL: [https://www.youtube.com/watch?v=8e1YBOc3O68](https://www.youtube.com/watch?v=8e1YBOc3O68)

 * Speaker: Sorab Jane from IBM India, discussing improvements to Linux kernel's Kump feature for handling CPU and memory hot plug events
* Motivation: Existing solution keeps updating old information when a hot plug event occurs, leading to potential inaccurate dumps. Proposed solution aims to update only relevant components and reduce service window time.
* Overview of Kump: Linux kernel feature that collects crash dumps whenever there's a kernel crash. It reserves memory area for the production kernel to store the dump when needed.
* Existing Solution: UD rule monitors CPU memory hot plug events and reloads the entire Kump image when necessary, but this is inefficient as it takes time and can cause issues during bulk operations.
* Proposed Solution: Update relevant GEXi segment and kernel image based on hot plug operation type to avoid reloading the entire Kump image. This results in significant time savings.
* Implementation:
  + Load Kum kernel via two system calls (kxi load and kxi file load).
  + Prepare kernel with kxic tool before loading it.
  + Update relevant components based on system call used.
  + Enable feature through a dedicated config file and Sha verification.
* Additional Features:
  + Udev rule to make user space aware of the updated Kump service without reloading it.
  + Support for architecture-specific crash hot plug handlers.
* Benefits: Reduces Kump service window time significantly, especially during bulk operations. Improves overall system reliability and performance.


## A kernel documentation update - Jonathan Corbet

URL: [https://www.youtube.com/watch?v=H97wxIVZ09s](https://www.youtube.com/watch?v=H97wxIVZ09s)

 * John Corbet discussed updates to Linux kernel documentation in a talk
* Moved architecture documentation into one directory and reorganized it
* Integrated Rust documentation with the existing documentation
* Added Spanish translation for kernel documentation and switched to Alabaster theme
* Made progress on rendering DocBook info format (Spinks)
* Wanted to continue reorganizing documentation, but faced opposition due to impedance mismatch between markdown and restructured text formats
* Discussed the balance between plain text and HTML documentation and the cost-benefit analysis of producing both
* Added ability to render RST info format for Spinks
* Continued working on improving top-level index and adding new tutorials and subsystem documentation
* Planned to reorganize device documentation to match top-level device directories
* Discussed the challenges of maintaining documentation, especially in terms of keeping it up-to-date with source code changes
* Mentioned that documentation is a crucial part of the development process and that maintainers play an important role in enforcing good documentation practices.


## Tips and Strategies for Reducing Stress and Burnout by Creating Psychological... - Dr Gloria Chance

URL: [https://www.youtube.com/watch?v=9YFRuXrah5s](https://www.youtube.com/watch?v=9YFRuXrah5s)

 * Dr. Gloria Chance, Chief Psychologist and Chief Information Officer at Musa Group, discussing psychological safety and reducing stress and burnout
* Importance of understanding humans are not machines, but complex beings with emotions and thoughts
* Discussing the impact of negative thoughts on productivity and the importance of shifting thinking to positive behavior
* Psychological safety in the workplace: listening, acknowledging hard work, empathy, and creating a supportive environment
* Building trust through transparency and communication
* Empathy in understanding others and responding appropriately
* The importance of acknowledging emotions behind masks and showing compassion
* Techniques for managing stress: exercise, setting realistic expectations, prioritizing tasks, and asking for help
* The impact of chronic stress on physical and emotional health and performance
* Mindfulness techniques for relaxation and reducing stress response
* Importance of taking breaks and engaging in activities that bring joy and relaxation
* Cross-crawl exercises to reduce stress and improve focus
* Encouraging a growth mindset and learning from mistakes
* The importance of self-talk and shifting negative thoughts to positive affirmations.


## DAMON Current Status and Future Plans - SeongJae Park

URL: [https://www.youtube.com/watch?v=rwHCGA3ppT4](https://www.youtube.com/watch?v=rwHCGA3ppT4)

 * SJ Park (SJ) currently works at AWS maintaining a small Linux Corner system called Demon
* Introducing Demon shell and updates made since last year's conference
* Discussing future plans for Demon, which includes three sub-projects:
  + Damon region: target memory size, split regions randomly, merge snapshots, and control accuracy overhead
  + Access continuity mem scaling: background process, keep free page continuity, and report free pages
  + Corner feature: access continuity aware memory autoscaling
* Challenges include managing time effectively during presentations and dealing with complex corner cases
* Demon's current architecture assumes offline monitoring usage but has evolved for online usage
* New features include Damon filter, sh moving average access rate based snapshot generation, and feedback driven aggression tuning.


## Kernel Samepage Merging (KSM) at Meta and Future Improvements to KSM -Stefan Roesch

URL: [https://www.youtube.com/watch?v=lZUgUE2zkyo](https://www.youtube.com/watch?v=lZUgUE2zkyo)

 * Kernel Samepage Merging (KSM) is a feature used at Meta to reduce memory usage by merging duplicate anonymous pages in the kernel
* KSM uses a three-phase process: try, enable, and scan
* Try phase: check if a memory region can be marked for KSM using an advisory system call
* Enable phase: mark the memory region for KSM use with a kernel control system call
* Scan phase: background thread scans memory and merges duplicated pages
* KSM requires compatible memory regions and excludes huge TLB shared EMAs
* New process control options added to enable or disable KSM for specific memory regions
* Systemwide configuration is possible through CIS kernel mm
* KSM has benefits such as memory saving, improved system performance, and reduced paging
* Challenges include monitoring KSM, optimizing page scanning, and considering security concerns.
* New features in development include Proactive Page Sharing, Autotune Advisor, and Smart Scan.
* Kernel approach to implementing KSM involves calculating hash pages and keeping a stable tree for accurate information sharing.
* Meta has seen significant memory savings with KSM, up to 6 gigabytes on a 64-gig machine.
* Future improvements include optimizing page scan parameters, reducing CPU overhead, and addressing security concerns.


## VSOCK: From Convenience to Performant VirtIO Communication - Amery Hung

URL: [https://www.youtube.com/watch?v=wXVz_oBGKVc](https://www.youtube.com/watch?v=wXVz_oBGKVc)

 * Emory Hung from Linux kernel Engineering department talks about VSOCK (Virtual Sockets), a socket-based communication interface for zero configuration communication between virtual machine host and guest.
* VSOCK doesn't require setting IP network like traditional sockets; it allows the guest to start socket communication directly with the host.
* Addressing scheme in VSOCK uses context IDs (CIDs) that are unique to each guest, allowing for efficient communication between the guest and host.
* Use cases include implementing agents inside guests for managing containers or supporting ESO (Elastic Network Adapter) and CAT (Cloud Application Platform).
* TCP/IP is often used for simple communication but requires maintaining network configuration and can be unreliable and inefficient. VSOCK provides a simpler, more reliable, and efficient alternative.
* VSOCK protocol has a straightforward design, using a two-way handshake for connection establishment, and supports point-to-point datagrams with control flow managed via credit allocation.
* Recent improvements to VSOCK include datagram support, which could potentially replace TCP/IP in performance-sensitive workloads, and the introduction of sockmap, which allows for programmable escape redirection using EBPF (Extended Berkeley Packet Filter) programs.
* Testing shows that VSOCK has lower latency and higher throughput than UDP (User Datagram Protocol), making it a promising replacement for TCP/IP in performance-sensitive applications.
* Other features of VSOCK include support for multiple virtual queues, which can improve scalability and reduce the need for networking stack routing and filtering.


## Improving resource ownership and life-time in linux device drivers - Bartosz Golaszewski

URL: [https://www.youtube.com/watch?v=bHaMMnIH6AM](https://www.youtube.com/watch?v=bHaMMnIH6AM)

 * Speaker: Bartosz Golaszewski from Qualcomm Landing Team at Linaro
* Discussed resource ownership and lifetime issues in Linux device drivers
* Investigated memory issue where a device's embedded structure was freed before the driver was detached, causing problems
* Proposed solutions to prevent resource leaks when a provider goes away
* Distinguished between kernel and software representations of hardware assets and resource handles
* Discussed the role of kernel drivers as subsystems that provide abstraction layers for consumer drivers
* Explored the importance of proper reference counting and synchronization in managing resources across multiple layers of abstraction
* Suggested using srcu (Software Reference Count Update) to ensure that providers are not accessed after they have gone away
* Discussed the need for a common interface for resource providers and consumers, as well as the use of wrapper functions to manage resource lifetime
* Mentioned the challenges of handling provider-consumer relationships when a provider goes away, particularly in the context of subsystems that fail miserably when a provider is detached
* Proposed using a wrapper approach to maintain a shell around the safe interface of a driver and its subsystem, allowing for better handling of provider detachment
* Discussed the importance of keeping resources within scope and avoiding typos in function pointers to prevent logic breaks.


## How to make syzbot reports easier to debug? - Aleksandr Nogikh

URL: [https://www.youtube.com/watch?v=gZfhi7OgLLI](https://www.youtube.com/watch?v=gZfhi7OgLLI)

 * Speaker discusses methods for making Syzbot reports easier to debug
* Ideas include using kernel dumps, tracing tools, and prioritizing issues based on impact
* Speaker mentions using kgdb tool, analyzing customer requests, and minimizing config files
* Discussion of bisecting to find problematic revisions and the importance of maintaining stable kernels
* Mention of potential automation in reporting and catching mistakes
* Speaker expresses frustration with context changes and missing fixes in backports
* Ideas for improving communication between developers and maintainers, and the use of mailing lists and dashboards.


## UEFI Setvariable at runtime -- Problems status and solutions - Mr Ilias Apalodimas

URL: [https://www.youtube.com/watch?v=UdQk0SCUAlA](https://www.youtube.com/watch?v=UdQk0SCUAlA)

 * The speaker, Ilias Apalodimas, discusses the status of UEFI (Unified Extensible Firmware Interface) and its use in embedded systems and bootloaders.
* UEFI is a firmware interface that allows various architectures to boot operating systems while providing common ways to handle platform-specific things and system security.
* One challenge with UEFI is the need for tamper-protected, delete-resistant media for storing keys and variables, but there are different approaches to solving this issue.
* The speaker mentions that EFI specification requires a tamper-protected, delete-resistant medium for storing keys, but it doesn't specify how this should be done at runtime.
* Some boards have flash memory connected to the secure world that is delete-resistant and tamper-protected, such as emmc or replay-protected memory partitions.
* The speaker discusses the challenges of setting variables in UEFI and the importance of doing so for configuring EFI boot managers and installers.
* Some solutions for setting variables at runtime include using standalone mm (Microcode Monkey) and OptiROM, which can support PK-authenticated variables and cryptographic checks.
* The speaker mentions that some issues with setting variables at runtime have been addressed in recent years, such as the problem of rpmb (Runtime Package Manager for Boot) not being able to preserve firmware context during the applicant exit.
* The speaker discusses the advantages and disadvantages of various approaches to storing variables, including using a file system or using a variable file stored in ROM.
* The discussion covers the potential challenges of implementing UEFI secure boot, such as the need for synchronous updates, authenticated storage, and dealing with platform-specific issues.


## Embedded Linux BOF - Tim Bird

URL: [https://www.youtube.com/watch?v=1sIW64Qip-I](https://www.youtube.com/watch?v=1sIW64Qip-I)

 * Tim Bird discussed embedded Linux technology areas of interest: architecture, bootloaders, file systems, networking, security, power management, and testing
* He mentioned the importance of reducing boot time in embedded Linux and shared some techniques such as using custom bootloaders, removing slab memory allocator, and using 64-bit ISA
* He also discussed tools like libc and system tap for improving boot time and system size
* Bird mentioned the challenges of maintaining an ecosystem for embedded Linux, including inadequate investment in infrastructure and heterogeneous core support
* He suggested creating a Discord server for better communication within the community and encouraged collaboration between companies to share resources.
* He also spoke about the Embedded Leadership Summit (ELC) and the need for stronger community building and more standardized APIs.
* Bird mentioned the importance of addressing issues related to AI and camera processing in embedded systems, as well as the lack of documentation and communication between different players in the ecosystem.


## PCI device authentication  encryption - Jonathan Cameron

URL: [https://www.youtube.com/watch?v=ZqMIlZ5lPAw](https://www.youtube.com/watch?v=ZqMIlZ5lPAw)

 * Lucas discusses PCI device authentication encryption and compares two approaches: letting the kernel handle it or using a Trusted Security Module (TSM)
* TSM approach lets the security module inside the CPU handle SPDM session authentication, measurement retrieval, and encrypted channel establishment
* However, TSM approach has limitations such as not being transport independent and requiring the OS kernel to interpret host-kernel communication
* Native kernel approach allows for a more flexible implementation but requires the host to set encryption keys for IDE devices and handle potential performance issues
* A joint effort among multiple vendors (Jonathan, Huawei, Intel, Alis, Western Digital) is proposed to establish policy-based type decisions and ensure everything looks secure before use
* Virtual function virtualization and SPDM session handling are also discussed, with the possibility of using TSM for both
* The use of measurement retrieval and attestation formats in SPDM is explained, with the potential for vendor-specific standardized report formats
* Exposing certificate chains and implementing challenge responses for third-party verification are also touched upon.


## Secure IO BoF - Dhaval Giani

URL: [https://www.youtube.com/watch?v=ID-krNWY5wE](https://www.youtube.com/watch?v=ID-krNWY5wE)

 * Dhaval Giani discussed the need for a common Linux guest host interface for secure IO in the context of vendor differentiation and complexity in Intel and AMD implementations.
* The discussion touched upon various topics such as:
  + gcx layer as a common wrapper for vendor-specific guest host interfaces (Intel's MD, GCI/GCB, etc.)
  + Linux native guest host interface and its use cases
  + Common set verb across drivers for different vendors
  + The role of SPSM in handling configuration devices and DMA operations
  + The need for a common communication protocol between the hypervisor and the guest.
* Some suggestions were made to simplify the process, like using a standard way to communicate device capabilities to the guest (SPDM, IDE, etc.) and adding device enumeration via the interface manifest.
* It was also mentioned that filtering devices based on trust and verifying their ID before allowing them to run could help mitigate potential security risks.
* The discussion acknowledged the challenges of implementing a common Linux guest host interface across vendors due to the need for vendor-specific code within the guest (TDX modules, etc.) but emphasized the importance of addressing these issues in order to improve the overall security and compatibility of virtual environments.


## Android BOF

URL: [https://www.youtube.com/watch?v=HXgMdmLmGhU](https://www.youtube.com/watch?v=HXgMdmLmGhU)

 * Android memory management: conventionally, reclaim algorithm uses Intive Active List idea
* Multiple generations control music and EV (Early Validation)
* Youngest generation moves independently, causing order issues
* Reclaim order: oldest generation progresses forward, youngest stays put
* Zone configuration: normal zone is used for reclaim work, movable zone is not
* Eligible page checking: reclaim still looks at normal DMA32 zones
* Page allocation and FD (File Descriptor) references
* Anonymous pages are added to oldest generation's page table
* Reclaiming CL (Cleaner Log) and FD access pages might not work due to page table updates
* Workload changes may need read of configuration files, app launch regression
* Protection mechanisms for FDX Pages
* Balancing performance vs. security: tradeoffs exist
* Android device checks for free swap space, usually at zero
* Swap memory management and reclaim
* Early memory kill can affect performance negatively but is rare
* Ideas for handling swap full case include checking swap pages and updating PT entries
* Discardable memory used daily like Ashm unpinned ashm Pages as a balancing alternative to dealing with shrinker stuff
* Balancing problem: overshooting high water mark reclaim latency, lot of small end reclaims
* Current approach: eviction and eligible zone checking at watermark, shrinking H pages.
* Open questions include MG (Malloc Guard) discussion, handling swap full case, and early memory kill impact.


## Android: memcg v1 - v2 - T.J. Mercier

URL: [https://www.youtube.com/watch?v=Be02sYAzpro](https://www.youtube.com/watch?v=Be02sYAzpro)

 * The speaker is discussing the upgrade from MCG v1 to MCG v2 in Android's cgroups (memory controller)
* MCG interacts with memory management and affects reclaims, such as kill throttle and app allocation based on current memory usage threshold
* Reasons for upgrading include avoiding potential deprecation of V1, extending MCG for additional accounting features, and addressing issues related to DMA buffer tracking and proactive reclaim since Android 14
* Current accounting solution for DMA buffers takes a global kernel lock every allocation and causes performance issues; MCG aims to account per CPU counter instead
* MCG v2 introduces proactive reclaim where background applications try to shrink memory footprint, running garbage collection, and trying memory reclaim
* Working set protection might help keep foreground applications fast by protecting their minimum working set and skipping reclaim for visible apps
* Android's memory pressure relief (LMKD) might benefit from MCG and mgu enabled, as mgu lru ordering likely influences reclaim memory apps going to be killed anyways
* The speaker encountered issues with zombie MCG in testing, where it consumed kernel memory and impacted performance significantly with thousands of zombie cgroups
* Other tests revealed a pixel driver bug, a Cas swap issue, and an unexpected test result with almost no memory usage increase when switching from MCG v1 to MCG v2
* The speaker is still investigating a large slab increase in testing and plans to continue the discussion.


## Reporting and tracking regressions across the ecosystem - Thorsten Leemhuis

URL: [https://www.youtube.com/watch?v=ibXahj-1sYs](https://www.youtube.com/watch?v=ibXahj-1sYs)

 * Discussion on regression tracking across the ecosystem at testing conference
* Regression tracking has been a frustration for maintainers for over a decade
* Process improvements are ongoing to address this issue
* Regression tracking methods include bot reports, JIRA, and email notifications
* Rebot tracks issues by replying to long emails with regression reports
* Rpot also looks for regressions among other things in messages
* Key things looked for in a regression report are the closest TXS patch submission link and the commit message
* Regression tracking can be manual or automated, but separation of actionable and non-actionable reports is important
* Central databases could store regression information for better tracking
* CI systems could generate test data and regression reports, with automated emails sent to developers
* Hexbot process and US experience were discussed as important aspects of regression tracking
* Maintaining a reputation and avoiding another buck tracker filled with issues was mentioned as a limitation
* Extracting information from CI systems and getting it back to users was suggested as valuable for closing the loop
* Rebot provides features for integrating source data into reports, but more detailed information is sometimes missing
* Dynamic scheduling and test generation were discussed as potential improvements
* Static analysis could identify bugs, but human review is still necessary
* Mining data to improve test processes was suggested as a helpful approach.


## 16k page size support - Juan Yescas, Kalesh Singh

URL: [https://www.youtube.com/watch?v=BaKdbcon8CQ](https://www.youtube.com/watch?v=BaKdbcon8CQ)

 * Issue: 16k page size support not working with some hardware controllers
* Controller doesn't follow standard and doesn't allow transfer of greater than 16KB
* Hardware issue that requires modification to support 16k page size
* Million devices using hardware that needs support, but it depends on the maintainer
* Discussion with maintainers needed for adding logic to support 16k page size indefinitely
* Possible solutions:
  + Load binary with appropriate permissions (R executable)
  + Convert 4K binary into a 60k binary and adjust alignment of program headers
  + Use virtual machine or emulator to run apps with 16k page size
  + Increase memory on device for better performance, especially for foldable phones
* Other solutions under discussion:
  + Rewrite ELF file, relocations, and PLT sections
  + Transform instructions in code, like ARM's ADRP instruction
  + Use recursive disassembly to find functions and fix offsets
* Idea to map everything as writable by default and use signal handlers to handle write access
* Long-term goal is to ask developers to transition from 4K to 16k page size in apps.


## Testing Drivers with KUnit (Does hardware have to be hard?) -David Gow

URL: [https://www.youtube.com/watch?v=eyy6NoJ-iN8](https://www.youtube.com/watch?v=eyy6NoJ-iN8)

 * David Gow, KUnit maintainer, discussing testing drivers with KUnit in Linux kernel
* Self-contained code like data structures and algorithms are easier to test
* Added features in KUnit: automatic resource allocation, deferred actions, parameterized testing, function call redirection
* Testing hardware is more complicated due to Global state and interdependent components
* Difficulty with testing drivers due to Global state, coupled components, and hardware interaction
* Challenges of testing drivers: mutating state without breaking the system, safely modifying kernel while it's running
* Proposed solutions for testing drivers: swapping fake client devices, function redirection, variable redirection
* Current limitations of KUnit: single threaded assumption, limited integration with device trees and I/O memory access
* Future possibilities: using Device trees for testing, Vero PCI support, and static data stubbing extension
* Challenges in emulating hardware within the kernel and partitioning hardware testing.


## toolchain-agnostic build time improvements - Tanzir Hasan, Google & Nick Desaulniers, Google

URL: [https://www.youtube.com/watch?v=eFq_oqLiXPM](https://www.youtube.com/watch?v=eFq_oqLiXPM)

 * Speakers: Tanzir Hasan and Nick Desaulniers from Google
* Goal: Making kernel build faster by refactoring headers, using precompiled headers, and improving include handling
* Problems with header files:
  + Large number of headers leading to long parsing time and bloated compiler cache
  + Indirect includes and dead includes increasing build time
  + Preprocessing taking a significant amount of time
* Solutions:
  + Automatically removing unnecessary headers and refactoring large ones
  + Using precompiled headers for frequently used headers
  + Improving include handling by using faster mapping techniques and avoiding indirect includes
  + Using tooling like Clang's Cway and Dash to handle include files more efficiently
* Other improvements:
  + Splitting large header files into smaller ones
  + Using hierarchical clustering to partition headers and reduce dependencies
* Future research:
  + Automatically analyzing and optimizing include usage in the kernel build system
  + Improving parallelism in the build process using tools like Kbuild and Plumber.



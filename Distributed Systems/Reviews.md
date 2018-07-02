<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD007 -->
<!-- markdownlint-disable MD026 -->
<!-- markdownlint-disable MD040 -->

# Distributed system

## Contents

- [Introduction](#Introduction)

---

## Introduction

### Distributed System definitions

- A system in which hardware or software components located at networked computers communicate and coordinate their actions only by passing message
- A collection of independent computers that appears to its users as a single coherent system

**A Computer Network:** Is a collection of spatially separated, interconnected computers that exchange messages based on specific protocols. Computers are addressed by IP addresses.

**A Distributed System:** Multiple computers on the network working together as a system. The spatial separation of computers and communication aspects are hidden from users.

### Why Distributed Systems?

- Resource Sharing:
    - Hardware Resources (Disks, printers, scanners etc)
    - Software Resources (Files, databases etc)
    - Other (Processing power, memory, bandwidth)

- Benefits of resource sharing:
    - Economy
    - Reliability
    - Availability
    - Scalability

### Consequences (problem) of Distributed Systems:

- Concurrency (having mulitple processes/threads on different computer, executed out-of-order or in partial order)
- No global clock (not all computers having the exact same time)
- Independent failures

### Computer Networks

Common distributed systems are based on widely used computer networks, e.g.:

- **The Internet**, a large number of interconnected collection of computer networks of different types
    - computers interacting by message passing using a common means of communication(Internet protocol)
    - Many different services (applications) (World Wide Web (www), email, file transfer)
    - A number of Intranets linked by backbones
    - Internet Service Providers (ISPs), that provide access to the services on the Internet while providing local service such as email and web hosting. Without a subscription with an ISP, you won't have a connection to the Internet.
    - A backbone network link with high transmission capacity
    - Communication via Satellite, fiber optic cables and other high-bandwidth circuits
    <img src="images/internet.png" alt="550" width="550">

```
Backbone connection:
1. At the local level, a backbone is a line or set of lines that local
area networks connect to for a wide area network connection or within a
local area network to span distances efficiently (for example, between
buildings).
2. On the Internet or other wide area network, a backbone is a set of
paths that local or regional networks connect to for long-distance
interconnection.
```

- **Intranets**, a portion of the Internet that is accessed only  by authorized person of organizations
    - A boundary that can be configured to enforce local security policies
    - Several local area connection (LANs) linked by backbone connections
    - A connection to the Internet via a router allowing users within the intranet to access services on the Internet
    - Firewalls to protect an intranet by preventing unauthorized messages leaving or entering by filtering incoming and outgoing messages e.g. by source or destination
    <img src="images/intranet.png" alt="550" width="550">
- **Wireless networks**, allows the integration of small and portable computing devices into distributed systems
    - Mobile Computing (Nomadic Computing)
    - Ubiquitous Computing
    - Internet of Things
    <img src="images/Portable_device.png" alt="550" width="550">

### Distributed system challenges

- **Heterogeneity**, Distributed systems use hardware and software resources of varying characteristics (heterogeneous resources):
    - Networks
    - Computer Hardware
    - Operating Systems
    - Programming Languages
    - Implementation by different developers

    Some approaches for handling heterogeneity issues are:
    - Using standard protocols
    - Using agreed upon message formats and data types
    - Adhering to an agreed upon Application Program Interfaces (APIs)
    - Using Middleware
    - Portable code

    Middleware is a software layer between the application layer and the operating systems, and certain   middleware solutions address some heterogeneity issues but not others

    Middleware Models:
    - Distributed File Systems
    - Remote Procedure Call (RPC) (procedural languages)
    - Remote Method Invocation (RMI) (object-oriented languages)
    - Distributed Documents
    - Distributed Data Bases

    Mobile code is sent from one computer to the anther to run at the destination (e.g. Java applets):
    - Code that is compiled to run in one OS does not run in another:
        - different hardware
        - different OS versions
    - Virtual Machine approach provides a way of making code executable on any hardware - compiler produces code that is interpreted by the virtual machine
    - Cross-platform compilation and code portability is another way, that compiles source code to multiple targets.

- Openness, refers to the ability of extend the system in different ways by adding hardware or software resources. Following are some approaches to address openness:
    - Publishing key interfaces
    - Allowing a uniform communication mechanism to communicate over the published interfaces
    - Ensuring all implementations adhere to the published standards

- Security
    - There has three aspects of security:
        - Confidentiality (protection against disclosure to unauthorized individuals)
        - Integrity (protection against alteration and corruption)
        - Availability (protection against interference with the means of access)
    - Security Mechanisms:
        - Encryption (e.g. Blowfish, RSA)
        - Authentication (e.g. passwords, public key authentication)
        - Authorization (e.g. access control lists)
    - Types of security challenges have not yet been resolved completely:
        - Denial of service attacks
        - Security against mobile code (executables as attachments)

- Scalability, A system is considered to be scalable if it can handle the growth of the number of users. Scalability Challenges:
    - Cost of physical resources: For a system with n users to be scalable, the quantity of physical resources required to support the system should be O(n) - if one file server can support 20 users, then two servers should be able to support 40 users.
    - Controlling the performance loss: Complexity of algorithms that are used for searches, lookup etc should be scalable - for example a search algorithm for n data items requiring O(log(n)) search steps is scalable but one that requires n^2 is not.
    - Resources should not run out: e.g. 32-bit Internet IP addresses running out requiring a new version of 128-bit address.
    - Avoiding Performance bottlenecks: Decentralized architectures and algorithms can be used to avoid performance bottlenecks.

    ```
    The term “bottleneck” refers to both an overloaded network and the
    state of a computing device in which one component is unable to keep
    pace with the rest of the system, thus slowing overall performance
    ```

- Failure Handling
    - **Detecting**: some types of failures can be detected, e.g. checksums can be used to detect corrupted data in a message, and some kinds of failure are hard to be certain about, e.g. the failure of a remote server.
    - Masking: some failures that have been detected can be hidden or made less severe, e.g. timeout and message retransmission.

    <img src="images/masking_failure.png" alt="550" width="550">

    - **Tolerating**: it is sometimes impractical to try and handle every failure that occurs, sometimes it is better to tolerate them, e.g. failure is reported back to the user, e.g. web server not being available, try again later, or video is rendered with errors
    - **Recovery**: failure sometimes leads to corrupted data and software can be designed so that it can recover the original state after failure, e.g. implementing a roll back mechanism.
    - **Redundancy**: services can be made to tolerate failures using redundant components, e.g. multiple servers that provide the same service, as so called fail over.

- Concurrency
    - Multiple clients can access the same resource at the same time, in some cases for updates
    - One approach to handling concurrency is making access sequential - slows down the system
    - Semaphores supported by the operating system is a well accepted mechanism to handle concurrency

    ```
    Mutex: exclusive-member access to a resource
    Semaphore: n-member access to a resource
    ```

- Transparency, the aspect of hiding the components of a distributed system from the user and the application programmer. Types of  transparencies:

    - Access transparency
    - Location transparency
    - Concurrency transparency
    - Replication transparency
    - Failure transparency
    - Mobility transparency
    - Performance transparency
    - Scaling transparency

### World Wide Web

The three main standard technological components used in the web
are:

- HypterText Markup Language (HTML) - This is a language for specifying the contents and layout of pages to be displayed by browsers.
- Uniform Resource Locators (URLs) - These identify the resources stored on the web. A URL has two components: scheme and scheme-specific-identifier. Scheme - declares the type of resource. Scheme-specific-identifier - identifies the resource. E.g., mailto:xxx@yahoo.com
- HyperText Transfer Protocol (HTTP) - This is the protocol used for transferring resources between web servers and clients (e.g. browsers). The main features are:
    - Uses request-reply interactions
    - Supports different content types
    - Requires one request per resource
    - Supports simple access control

### Dynamic pages

- Static web pages allow data to be made available for retrieval
- Dynamic web pages allow users to interact with resources by taking user input, executing programs and returning results
- Programs executed on the request can take different forms

### Summary

- Communication networks that enable distributed systems are the Internet, intranets and wireless networks
- Resource sharing is the main motivation for distributed systems
- There are many challenges associated with these systems - Heterogeneity, Openness, Security, Scalability, Failure handling, Concurrency, Transparency
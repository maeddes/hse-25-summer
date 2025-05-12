# hse-25-summer

## 2025-03-17 Initial session - Distributed Systems & Cloud Introduction

![Brainstorming](/images/2025_03_17_brainstorm.png)

### **Content Overview**

1. **Distributed Systems**
   - Difference distributed and non-distributed systems
   - Reasons to use/implement distributed-systems
   - Categories of heterogenity and resilience
   - Role communication protocols, service registry, distributed configuration
   - The fallacies of distributed computing

2. **The NIST Cloud Definition (2011)**
   - Breakdown of the NIST’s five essential cloud characteristics, deployment models, and service models. 

3. **Cloud Service/Abstraction Models**
   - IaaS, PaaS, SaaS revisited, with modern examples.
   - The evolution of abstraction models, including FaaS and Containers-as-a-Service (CaaS).

4. **Introduction to CNCF**
   - Role of the Cloud Native Computing Foundation (CNCF) in the cloud ecosystem.
   - CNCF Landscape: technologies, tools, and projects.

---

### **Learning Objectives**
By the end of this lecture, students will be able to:
- Distinguish between distributed and non-distributed systems
- Explain the importance of heterogeneity and resilience as key drivers for distributed systems.
- Describe the NIST cloud definition and its significance in the modern cloud landscape.
- Identify the major cloud providers and tell about their evolution.
- Differentiate between cloud service models and discuss their evolution, including modern abstraction models like CaaS.

### **Student/Review Questions**
- What are the five essential characteristics of cloud computing according to NIST, and how do they apply to modern cloud services?
- Identify 3 main cloud providers and list their most important services
- What are the differences between IaaS, PaaS, and SaaS? Give examples of each in today's cloud ecosystem.
- What is the CNCF, and why is it important in the context of cloud-native technologies?
- Describe 3 of the fallacies of distributed computing

---

### **Suggested Reading & Resources**
- [NIST 2011 Cloud Computing Definition](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf)
- CNCF [Cloud Native Landscape](https://landscape.cncf.io/)

## **2025 / 03 / 24 - Recap Distributed Systems & Cloud**  

### **Content Overview**
1. **The NIST Cloud Definition (2011)** 
2. **Overview of Major Cloud Providers**
   - Key players in the cloud space (AWS, Azure, Google Cloud, etc.).
   - Comparing evolution.

3. **Cloud Service/Abstraction Models**
4. **Introduction to CNCF**
   - Role of the Cloud Native Computing Foundation (CNCF) in the cloud ecosystem.
   - CNCF Landscape: technologies, tools, and projects.

5. **Popular CNCF Technologies**
   - **Kubernetes**: Container orchestration in cloud-native environments.
   - **eBPF**: Extending kernel capabilities for monitoring and security.
   - **OpenTelemetry**: Observability standards and practices in modern cloud systems.

---

## **2025 / 03 / 24 - Cloud-based IDEs**

### **Content Overview**

1. **Overview of Cloud-Based IDEs**
   - Introduction to cloud-based integrated development environments (IDEs).
   - **GitHub Codespaces**: Full development environments in the cloud.
   - **Google IDX**: Automating and provisioning cloud-based workspaces for development.
   - Benefits of cloud-based IDEs for distributed systems development.

---

### **Learning Objectives**
By the end of this lecture, students will be able to:

- Explain the advantages of using cloud-based IDEs, such as GitHub Codespaces and IDX, for distributed system development.
- Demonstrate an understanding of how these tools enhance collaboration and scalability in cloud-native environments.

---

### **Student/Review Questions**
1. Analyze GitHub Codespaces and IDX. What are the key features that make them suitable for developing distributed systems?
2. What are the main benefits of using cloud-based IDEs compared to traditional, local development environments?

---

### **Suggested Reading & Resources**
- [GitHub Codespaces Documentation](https://github.com/features/codespaces)
- [IDX Website](https://idx.dev/)

---

## **2025 / 03 / 31 - Distributed Systems & Cloud-native Theory**

### **Content Overview**  

This lecture focused on the theoretical foundations of **cloud-native software design**, revisiting core motivations for distributed systems. The discussion was structured around two main drivers:  
- **Heterogeneity**: leveraging diverse platforms, operating systems, and languages in one system.  
- **Resilience**: enabling scalability, fault-tolerance, load balancing, and modern deployment strategies like blue-green deployments.

Students also reviewed the **technical requirements** for distributed system architecture, including network communication, service discovery, distributed configuration, and observability. The main part of the lecture introduced the **12-Factor App methodology** as a widely adopted guideline for building robust, maintainable, and portable distributed applications.

---  
### **Learning Objectives**  

By the end of this lecture, students will be able to:  
1. Explain key motivations behind building distributed systems, focusing on heterogeneity and resilience.  
2. Identify the foundational technical needs of distributed architectures.  
3. Understand and describe the purpose and impact of the 12 factors in the 12-Factor App methodology.  
4. Apply the 12-Factor principles as guidelines for designing and building cloud-native applications.

---  
### **Student/Review Questions**  

1. What are typical reasons for building distributed systems instead of monolithic applications?  
2. How do distributed systems enable heterogeneity in software development?  
3. What infrastructure and platform features are required to support distributed systems?  
4. Name and explain at least four principles from the 12-Factor App methodology and how they relate to distributed system needs.  
5. Why is configuration management especially important in a distributed environment?  
6. How do deployment practices like blue-green deployments contribute to system resilience?  

## **2025 / 04 / 07 - Containers & Docker**

### Content Overview

1. Development in distributed teams withouth containers and the potential problems:
   - Polyglot application landscapes are challenging as all work environments need to match all runtime requirements for all languages
   - Transporting application from environment A to environment B introduces challenges and problems with mismatching runtimes

2. **Containers**
   - Isolate Applications from each other
   - Package Applications along with all Runtime requirements for easy execution and transportation between working environments
   - Simplify configuration of working environments -> only container engine needed
   - handling of all application containers through same mechanisms: docker build, docker run

3. **Docker**
   - Docker ecosystem consists of the Docker Daemon, Docker CLI and Docker Hub
   - Creation of Dockerfiles
   - Building Images - Understanding the layer concept in container images
   - Running Containers
   - Running multiple container apps with Docker Compose

### **Student/Review Questions**
1. What is Docker, and how does it differ from traditional virtual machines?
2. Explain the concept of a Docker image and a Docker container. How are they related?
3. What are the main components of a Dockerfile? Describe the purpose of each component.
4. How does Docker ensure isolation and security between containers?
5. What is a container registry, and how do you use Docker Hub to share or deploy images?
6. Describe the process of building and running a containerized application using Docker, including common commands.
7. In which way does Docker Compose use existing fuctionality and in which way does it extend it?.

### Homework
- Get a Docker account
- Add Containerization to your Lab project

## **2025 / 04 / 14 - CAP Theorem, scalability, state, persistence**

![Brainstorming](images/2025_04_14_scalability_persistence.png)

---

### **Content Overview**

This lecture explored the theoretical and practical aspects of **data persistence** and **scalability** in distributed systems.  
We revisited the **CAP Theorem** to understand the trade-offs between consistency, availability, and partition tolerance. Students compared **scale-up** (vertical scaling) vs. **scale-out** (horizontal scaling) strategies.  
The differences between **in-memory persistence** and **real database persistence** were illustrated through examples using **Spring Data JPA** with **H2 (in-memory)** and **PostgreSQL (external database)**.

---

### **Learning Objectives**

By the end of this lecture, students will be able to:  
1. Explain the CAP Theorem and the implications for distributed system design.  
2. Differentiate between scale-up and scale-out approaches and recognize their trade-offs.  
3. Compare in-memory persistence with external database persistence in terms of simplicity, performance, and scalability.  
4. Why did the CAP theorem become so relevant in the last decade even though it already exists since 1990?

---

![CAP theorem](images/2025_04_14_CAP.png)

### **Student/Review Questions**

1. What does the CAP Theorem state, and why is it relevant for distributed systems?  
2. What are the key differences between scaling up and scaling out? Provide examples of each.  
3. What are the pros and cons of using an in-memory database like H2 compared to a full external database like PostgreSQL?  
4. How does Spring Data JPA help simplify database interactions in a Java application?  
5. Why might an application start with in-memory persistence during development but move to an external database later?

---

## **2025 / 04 / 28 - Onsite Lab Session**

## **2025 / 05 / 05 - API and REST**

![image](https://github.com/user-attachments/assets/9257f225-430e-471e-8be6-f428ae8cfe6f)

### **Content Overview**

This lecture aimed to explore common principles of establishing communication between distributed applications.
We introduced the foundational principles and real-world application of RESTful APIs in distributed systems.
While the communication interface can be implemented freely in a multitude of ways, the **REST** architectural style provides guidelines for implementation focusing on concepts such as stateless communication, resource-based URIs, and the use of HTTP methods (GET, POST, PUT, DELETE).


### Learning Objectives
By the end of this lecture, students will be able to:
1. Define REST and explain its significance in distributed system design.
2. Identify the key components of RESTful APIs (Resources, Verbs, Representations.
3. Use appropriate HTTP methods and status codes in REST API design.
4. Identify the Maturity of an API via the Richardson Maturity Model

### Student/Review Questions

1. What are the main constraints that define a RESTful system?
2. When should you use each of the HTTP methods: GET, POST, PUT, DELETE?
3. What is idempotency, and why is it important in REST APIs?



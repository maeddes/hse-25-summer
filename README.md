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


Great! Here's your lecture documentation in the usual structure:

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

## **2025 / 01 / 07 - Containers & Docker**

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
   - Docker ecosystem consists of the Docker Daemon, Docker CLI and Docker Hub+
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
7. In which way does Docker Compose use existing fuctionality and in which way does it extend it?

### Homework
- Get a Docker account
- Add Containerization to your Lab project


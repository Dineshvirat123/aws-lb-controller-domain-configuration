 Built a Complete Microservices Access Architecture on AWS EKS using AWS Load Balancer Controller, Kubernetes Ingress, Route53, ACM SSL, and Docker.

GitHub Repository:
[https://github.com/Dineshvirat123/aws-lb-controller-domain-configuration.git](https://github.com/Dineshvirat123/aws-lb-controller-domain-configuration.git)

 Live Demo:
[https://dineshcloud.co.in](https://dineshcloud.co.in)

This project focuses on Kubernetes networking and different ways to expose microservices in production environments using AWS cloud-native services.

Instead of focusing on application functionality, the main goal was to understand how enterprise applications are exposed using:

✅ AWS ALB DNS
✅ Custom Domains
✅ Subdomains
✅ Path-Based Routing
✅ Host-Based Routing
✅ HTTPS using ACM SSL
✅ Kubernetes Ingress

━━━━━━━━━━━━━━━━━━━
 Microservices Used
━━━━━━━━━━━━━━━━━━━

• Home Service
• Profile Service
• Projects Service

All services were containerized using Docker and deployed into Kubernetes (AWS EKS).

━━━━━━━━━━━━━━━━━━━
 PHASE 1 — Access Using AWS ALB DNS
━━━━━━━━━━━━━━━━━━━

In the first phase, applications are accessed directly using the AWS Application Load Balancer DNS generated automatically by AWS Load Balancer Controller.

Examples:

/home
/profile
/projects

Architecture Flow:

Users → AWS ALB → Kubernetes Ingress → Services → Pods

Implemented:

✅ AWS Load Balancer Controller
✅ Kubernetes Ingress
✅ Path-Based Routing
✅ Dockerized Flask Microservices
✅ Service-to-Pod Communication

━━━━━━━━━━━━━━━━━━━
 PHASE 2 — Access Using Custom Domain
━━━━━━━━━━━━━━━━━━━

Integrated Route53 and ACM SSL with ALB Ingress to expose applications securely using a custom domain.

Live Domain:

[https://www.dineshcloud.co.in](https://www.dineshcloud.co.in)

Examples:

[https://www.dineshcloud.co.in/home](https://www.dineshcloud.co.in/home)
[https://www.dineshcloud.co.in/profile](https://www.dineshcloud.co.in/profile)
[https://www.dineshcloud.co.in/projects](https://www.dineshcloud.co.in/projects)

Implemented:

✅ Route53 DNS Mapping
✅ ACM SSL Certificate
✅ HTTPS Redirection
✅ SSL Policies
✅ Domain-Based Routing using Ingress

━━━━━━━━━━━━━━━━━━━
 PHASE 3 — Access Using Subdomains
━━━━━━━━━━━━━━━━━━━

In the final phase, each microservice was exposed using dedicated subdomains through Host-Based Routing.

Examples:

home.dineshcloud.co.in
profile.dineshcloud.co.in
projects.dineshcloud.co.in

Implemented:

✅ Host-Based Routing
✅ Route53 Subdomain Records
✅ Multi-Service Ingress Architecture
✅ Enterprise-Style Kubernetes Exposure

━━━━━━━━━━━━━━━━━━━
 Technologies Used
━━━━━━━━━━━━━━━━━━━

• Docker
• Kubernetes (EKS)
• AWS Load Balancer Controller
• AWS ALB
• Route53
• ACM SSL
• Flask
• Ingress
• GitHub
• AWS ECR

━━━━━━━━━━━━━━━━━━━
 Key Learnings
━━━━━━━━━━━━━━━━━━━

✅ Kubernetes Ingress Deep Understanding
✅ Path-Based Routing
✅ Host-Based Routing
✅ ALB + Kubernetes Integration
✅ Route53 Domain & Subdomain Mapping
✅ SSL/TLS Configuration using ACM
✅ Production-Style Kubernetes Networking
✅ IRSA & OIDC Configuration
✅ Real-World Microservices Exposure on AWS

This project gave me strong practical experience in Kubernetes networking and cloud-native ingress architecture using AWS services.

#AWS #Kubernetes #EKS #Ingress #AWSALB #Route53 #Docker #DevOps #Microservices #CloudNative #Flask #ACM #LoadBalancer #KubernetesIngress #AWSCloud #DevOpsEngineer #DineshCloud

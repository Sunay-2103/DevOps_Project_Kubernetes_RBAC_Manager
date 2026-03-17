# Kubernetes RBAC Policy Manager

Student Name: Sunay Mukherjee  
Course: DevOps  
Difficulty: Intermediate  

---

## Project Overview

This project is a DevOps tool to manage Kubernetes RBAC policies.

It allows users to:
- View roles
- Create roles
- Delete roles
- Detect over-permissive roles

---

## Features

- RBAC role management
- Kubernetes integration
- Security warning system
- Simple web dashboard

---

## Tech Stack

- Python (FastAPI)
- Kubernetes
- Docker
- HTML + JS

---

## How to Run

1. Start Kubernetes:
   minikube start

2. Run backend:
   python3 -m uvicorn main:app --reload

3. Run frontend:
   cd frontend
   python3 -m http.server 5500

4. Open:
   http://localhost:5500

---

## DevOps Features

- Containerization using Docker
- Kubernetes deployment support
- CI/CD pipeline using GitHub Actions

---

## Future Improvements

- Multi-cluster support
- Authentication
- Full UI dashboard

---

## Author

Sunay Mukherjee

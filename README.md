# Mini-Project: Dockerized Flutter App with Jenkins CI/CD

This mini-project demonstrates how to Dockerize a Flutter app and set up CI/CD pipelines using Jenkins. 

## Prerequisites

- Docker
- Flutter
- Jenkins

## Followed Steps t Create the project

1. **Prerequisites**

    ```bash
    flutter create foile
    // workspaceFolder: Sets the default path that VS Code should open when connecting to the container.
    // THe devcontainer.json file tells VS Code how to access or create a development container with a well-defined tool and runtime stack.
    // 
    ```

2. **Build & Run Docker Image:**

    ```bash
    // RUN: python3 launcher_flutter.py that will build and run the container
    // Alternative: docker build -t flutter-foile .
    ```

3. **Jenkins CI/CD Pipeline:**

    - Installed Jenkins.
    - Created a new Jenkins pipeline project.
    - Configured the pipeline using the provided Jenkinsfile.
    - Run the Jenkins pipeline to automate Flutter app builds and deployments.

Thanks for your time and considerations!
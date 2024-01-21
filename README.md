# Mini-Project: Dockerized Flutter App with Jenkins CI/CD
This mini-project demonstrates how to Dockerize a Flutter app and set up CI/CD pipelines using Jenkins. 

## Process Screenshots:

![Screenshot from 2024-01-21 17-35-34](https://github.com/aliMissaoui/mini-project-flutter-devops/assets/68671238/ad57b691-d36c-4f8e-802f-f20ba23a7a5e)
---
![Screenshot from 2024-01-21 17-37-54](https://github.com/aliMissaoui/mini-project-flutter-devops/assets/68671238/ea57a42d-0739-42b0-a5a7-0aeea511f135)
---
![Screenshot from 2024-01-21 17-38-30](https://github.com/aliMissaoui/mini-project-flutter-devops/assets/68671238/d8307852-34e4-4aba-8116-78b09888ea0b)


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

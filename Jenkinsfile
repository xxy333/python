pipeline {
    agent any  // Runs on any available agent

    environment {
        // You can define environment variables here if needed
        // E.g., MAVEN_HOME = "/path/to/maven"
    }

    stages {
        // Stage 1: Checkout the source code
        stage('Checkout') {
            steps {
                // Checkout code from GitHub (make sure your Jenkins has GitHub credentials)
                git branch: 'master', url: 'https://github.com/xxy333/python.git'
            }
        }

        // Stage 2: Build the project
        stage('Build') {
            steps {
                // Example with Maven: mvn clean install
                // Replace with the appropriate build tool for your project
                script {
                    echo 'Building the project...'
                    sh 'mvn clean install'  // Adjust this based on your build system (e.g., Maven, Gradle, etc.)
                }
            }
        }

        // Stage 3: Run tests
        stage('Test') {
            steps {
                // Example with Maven: mvn test
                // Adjust based on your testing framework
                script {
                    echo 'Running tests...'
                    sh 'mvn test'  // Run tests with Maven, adjust based on your setup
                }
            }
        }

        // Stage 4: Deploy to a staging environment (example)
        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying to staging...'
                    // Replace with your deployment command or script
                    sh './deploy.sh'  // Adjust based on how your deployment works (e.g., Kubernetes, Docker, etc.)
                }
            }
        }
    }

    post {
        // Post-build actions, like sending notifications
        always {
            echo 'Cleaning up...'
            // Clean up any resources or perform any actions that should always run
        }
        success {
            echo 'Build was successful!'
            // Notify success (e.g., send an email or Slack message)
        }
        failure {
            echo 'Build failed!'
            // Notify failure (e.g., send an email or Slack message)
        }
    }
}

pipeline {
    agent any  // Runs on any available agent

    environment {
        MAVEN_HOME = "/path/to/maven"
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
                    sh """
                    echo "Hello world"
                    """
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

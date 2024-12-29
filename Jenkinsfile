pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/yasmoun/task-api'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t flask-task-api .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run flask-task-api pytest'
            }
        }
        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: '**/test-reports/*.xml', allowEmptyArchive: true
            }
        }
    }
}

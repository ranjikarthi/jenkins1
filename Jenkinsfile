pipeline {
    agent any
    
    environment {
        DOCKER = '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe"'
    }


    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t python-app .'
            }
        }

        stage('Run Tests Inside Docker') {
            steps {
                bat 'docker run --rm python-app python -m pytest'
            }
        }

        stage('Run Application Inside Docker') {
            steps {
                bat 'docker run --rm python-app'
            }
        }
    }
}
